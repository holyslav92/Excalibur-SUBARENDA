#!/usr/bin/env python3
"""Run Derouter image model through REST API (OpenAI-compatible).

Reads ``cover/quad-mcp-batch.json``, calls Derouter ``/images/generations`` (t2i)
or ``/images/edits`` (i2i with local identity-real file), writes the same
``cover/quad-mcp-result.json`` shape for ``excalibur_blog_quad_apply.py``.

Auth: ``DEROUTER_API_KEY`` only (Cloud Secrets). Never print the key.

Provider order (Cover): Derouter REST → Kie script → BLOCKER.
Forbidden: flux2-pro-*, Seedream, nano_banana*, z-image, mcp-derouter/start-mcp.sh.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from excalibur_blog_site_base import (
    SITE_BASE_PLACEHOLDER,
    expand_site_base,
    resolve_public_base_from_env,
)

DEFAULT_API_KEY_ENV = "DEROUTER_API_KEY"
DEFAULT_MODEL_ENV = "DEROUTER_IMAGE_MODEL"
DEFAULT_SIZE_ENV = "DEROUTER_IMAGE_SIZE"
DEFAULT_QUALITY_ENV = "DEROUTER_IMAGE_QUALITY"
# Quad canvas exact 2K 16:9 per Derouter Image tab (not aspect_ratio API field).
DEFAULT_SIZE_2K_16_9 = "2048x1152"
DEFAULT_QUALITY = "auto"
# Images MUST use api-direct — api.derouter.ai hits Cloudflare ~100s → HTTP 524 on gen.
PRIMARY_DIRECT_BASE = "https://api-direct.derouter.ai/openai/v1"
FALLBACK_DIRECT_BASE = "https://api-direct.apikey.cloud/openai/v1"
# Ordered probe list (user canon 2026-08-22): swap only host, same /openai/v1 path + key.
DEFAULT_IMAGE_API_BASE_CANDIDATES = [
    "https://api.derouter.ai/openai/v1",
    "https://api.apikey.cloud/openai/v1",
    "https://api-direct.derouter.ai/openai/v1",
    "https://api-direct.apikey.cloud/openai/v1",
]
DEROUTER_IMAGE_API_BASE_ENV = "DEROUTER_IMAGE_API_BASE"
DEROUTER_API_BASE_ENV = "DEROUTER_API_BASE"
DEFAULT_TIMEOUT_SECONDS = 600
MIN_TIMEOUT_SECONDS = 240
DEFAULT_MAX_RETRIES = 1
DEFAULT_RETRY_WAIT_SECONDS = 5
DEFAULT_LOCAL_REFERENCE = "memory/cover/assets/blog-hero-reference.png"


class DerouterApiError(RuntimeError):
    """Raised for API or response-shape failures."""


def default_model() -> str:
    model = os.environ.get(DEFAULT_MODEL_ENV, "").strip()
    if not model:
        raise DerouterApiError(
            "DEROUTER_IMAGE_MODEL unset; set image model id in Cloud Secrets "
            "(see shared/derouter-gpt-image-api-contract.md)"
        )
    return model


class DerouterRetryable(DerouterApiError):
    """Auth/5xx — one retry + optional Kie fallback."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        self.status = status
        super().__init__(message)


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def resolve_path(root: Path, article_dir_arg: str, path_arg: str) -> Path:
    article_dir = Path(article_dir_arg)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    path = Path(path_arg)
    if not path.is_absolute():
        path = article_dir / path
    return path


def default_size() -> str:
    return (os.environ.get(DEFAULT_SIZE_ENV) or DEFAULT_SIZE_2K_16_9).strip() or DEFAULT_SIZE_2K_16_9


def default_quality() -> str:
    return (os.environ.get(DEFAULT_QUALITY_ENV) or DEFAULT_QUALITY).strip() or DEFAULT_QUALITY


def normalize_api_base(url: str) -> str:
    base = str(url or "").strip().rstrip("/")
    if not base:
        return ""
    if not base.endswith("/openai/v1"):
        if base.endswith("/openai"):
            base = f"{base}/v1"
        elif base.endswith("/v1"):
            base = base
        else:
            base = f"{base}/openai/v1"
    return base


def image_api_base_candidates(
    *,
    primary_base: str | None = None,
    fallback_base: str | None = None,
) -> list[str]:
    """DEROUTER_IMAGE_API_BASE / DEROUTER_API_BASE override, then ordered fallbacks."""
    out: list[str] = []
    for raw in (
        os.environ.get(DEROUTER_IMAGE_API_BASE_ENV, "").strip(),
        os.environ.get(DEROUTER_API_BASE_ENV, "").strip(),
        str(primary_base or "").strip(),
        str(fallback_base or "").strip(),
    ):
        norm = normalize_api_base(raw)
        if norm and norm not in out:
            out.append(norm)
    for candidate in DEFAULT_IMAGE_API_BASE_CANDIDATES:
        norm = normalize_api_base(candidate)
        if norm and norm not in out:
            out.append(norm)
    return out


def is_discontinued_image_error(exc: BaseException) -> bool:
    msg = str(exc).lower()
    return "discontinued" in msg or "not available" in msg and "image" in msg


def is_retryable_http(status: int) -> bool:
    # 524 = Cloudflare timeout when hitting non-direct api.derouter.ai for images.
    return status in {401, 403, 408, 429, 500, 502, 503, 504, 524}


def _guess_mime(path: Path) -> str:
    guessed, _ = mimetypes.guess_type(str(path))
    return guessed or "application/octet-stream"


def expand_input_urls(input_urls: list[Any]) -> list[str]:
    live = resolve_public_base_from_env()
    out: list[str] = []
    for raw in input_urls:
        url = str(raw or "").strip()
        if not url:
            continue
        if SITE_BASE_PLACEHOLDER in url:
            if not live:
                raise DerouterApiError(
                    f"batch input_urls contain {SITE_BASE_PLACEHOLDER} but PUBLIC_SITE_URL/WP_SITE_URL is unset"
                )
            url = expand_site_base(url, live)
        out.append(url)
    return out


def batch_mcp_args(batch_path: Path) -> dict[str, Any]:
    batch = load_json(batch_path)
    jobs = batch.get("jobs")
    if not isinstance(jobs, list) or len(jobs) != 1:
        raise DerouterApiError(f"Expected exactly one job in {batch_path}")
    job = jobs[0]
    if not isinstance(job, dict):
        raise DerouterApiError(f"Invalid job entry in {batch_path}")
    args = job.get("mcp_args")
    if not isinstance(args, dict):
        raise DerouterApiError(f"Missing jobs[0].mcp_args in {batch_path}")

    prompt = str(args.get("prompt") or "").strip()
    if not prompt:
        raise DerouterApiError("Missing prompt in jobs[0].mcp_args")
    out: dict[str, Any] = {
        "prompt": prompt,
        "aspect_ratio": args.get("aspect_ratio") or "16:9",
        "resolution": args.get("resolution") or "2K",
    }
    input_urls = args.get("input_urls")
    if isinstance(input_urls, list) and input_urls:
        expanded = expand_input_urls(input_urls)
        if expanded:
            out["input_urls"] = expanded
    return out


def resolve_local_reference_paths(
    *,
    root: Path,
    batch_path: Path,
) -> list[Path]:
    """Local identity-real files for /images/edits — never input_urls or data-URL JSON."""
    batch = load_json(batch_path)
    candidates: list[str] = []
    if batch.get("prefer_local_reference"):
        local_ref = str(batch.get("local_reference") or "").strip()
        if local_ref:
            candidates.append(local_ref)
    identity_local = str(batch.get("identity_reference_local") or "").strip()
    if identity_local and identity_local not in candidates:
        candidates.append(identity_local)
    if not candidates:
        return []
    paths: list[Path] = []
    for rel in candidates:
        path = Path(rel)
        if not path.is_absolute():
            path = root / path
        if path.is_file():
            paths.append(path)
            break
    if not paths:
        raise DerouterApiError(
            f"prefer_local_reference/identity_reference_local set but file missing: {candidates[0]}"
        )
    return paths


def http_json_post(
    url: str,
    api_key: str,
    payload: dict[str, Any],
    *,
    timeout: int,
) -> dict[str, Any]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if is_retryable_http(exc.code):
            raise DerouterRetryable(f"Derouter HTTP {exc.code}: {body[:500]}", status=exc.code) from exc
        raise DerouterApiError(f"Derouter HTTP {exc.code}: {body[:500]}") from exc
    except urllib.error.URLError as exc:
        raise DerouterRetryable(f"Derouter network error: {exc.reason}") from exc

    try:
        parsed = json.loads(body)
    except json.JSONDecodeError as exc:
        raise DerouterApiError(f"Derouter returned non-JSON: {body[:500]}") from exc
    if not isinstance(parsed, dict):
        raise DerouterApiError("Derouter returned a non-object JSON response")
    return parsed


def http_multipart_post(
    url: str,
    api_key: str,
    *,
    fields: dict[str, str],
    files: list[tuple[str, Path]],
    timeout: int,
) -> dict[str, Any]:
    """Multipart POST; multi-ref uses repeated image[] parts per Derouter docs."""
    boundary = "----ExcaliburDerouterBoundary"
    parts: list[bytes] = []
    for name, value in fields.items():
        parts.append(
            (
                f"--{boundary}\r\n"
                f'Content-Disposition: form-data; name="{name}"\r\n\r\n'
                f"{value}\r\n"
            ).encode("utf-8")
        )
    for field_name, file_path in files:
        mime = _guess_mime(file_path)
        file_bytes = file_path.read_bytes()
        parts.append(
            (
                f"--{boundary}\r\n"
                f'Content-Disposition: form-data; name="{field_name}"; filename="{file_path.name}"\r\n'
                f"Content-Type: {mime}\r\n\r\n"
            ).encode("utf-8")
        )
        parts.append(file_bytes)
        parts.append(b"\r\n")
    parts.append(f"--{boundary}--\r\n".encode("utf-8"))
    body = b"".join(parts)

    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        err_body = exc.read().decode("utf-8", errors="replace")
        if is_retryable_http(exc.code):
            raise DerouterRetryable(
                f"Derouter edits HTTP {exc.code}: {err_body[:500]}", status=exc.code
            ) from exc
        raise DerouterApiError(f"Derouter edits HTTP {exc.code}: {err_body[:500]}") from exc
    except urllib.error.URLError as exc:
        raise DerouterRetryable(f"Derouter edits network error: {exc.reason}") from exc

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise DerouterApiError(f"Derouter edits returned non-JSON: {raw[:500]}") from exc
    if not isinstance(parsed, dict):
        raise DerouterApiError("Derouter edits returned a non-object JSON response")
    return parsed


def parse_image_response(parsed: dict[str, Any]) -> bytes:
    """Derouter images API returns data[0].b64_json (PNG), not a URL."""
    data = parsed.get("data")
    if not isinstance(data, list) or not data:
        raise DerouterApiError(f"Derouter response missing data[]: {list(parsed.keys())}")
    item = data[0]
    if not isinstance(item, dict):
        raise DerouterApiError("Derouter data[0] is not an object")
    b64 = item.get("b64_json")
    if not b64:
        raise DerouterApiError("Derouter response missing data[0].b64_json (URL field not used)")
    try:
        return base64.b64decode(str(b64))
    except Exception as exc:  # noqa: BLE001
        raise DerouterApiError("Derouter b64_json decode failed") from exc


def call_generations(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    size: str,
    quality: str,
    timeout: int,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/images/generations"
    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "size": size,
        "quality": quality,
    }
    return http_json_post(url, api_key, payload, timeout=timeout)


def call_edits(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    image_paths: list[Path],
    timeout: int,
) -> dict[str, Any]:
    url = f"{base_url.rstrip('/')}/images/edits"
    fields = {
        "model": model,
        "prompt": prompt,
    }
    file_field = "image[]" if len(image_paths) > 1 else "image"
    files = [(file_field, path) for path in image_paths]
    return http_multipart_post(
        url,
        api_key,
        fields=fields,
        files=files,
        timeout=timeout,
    )


def generate_image(
    *,
    root: Path,
    batch_path: Path,
    image_input: dict[str, Any],
    api_key: str,
    model: str,
    size: str,
    quality: str,
    timeout: int,
    primary_base: str,
    fallback_base: str,
    max_retries: int,
    retry_wait: int,
) -> tuple[bytes, dict[str, Any]]:
    local_refs = resolve_local_reference_paths(root=root, batch_path=batch_path)
    use_edits = bool(local_refs)
    bases = image_api_base_candidates(primary_base=primary_base, fallback_base=fallback_base)

    last_error: BaseException | None = None
    attempts = 0
    discontinued_hosts: list[str] = []
    for base in bases:
        for attempt in range(max_retries + 1):
            attempts += 1
            host = urllib.parse.urlparse(base).netloc
            try:
                if use_edits:
                    parsed = call_edits(
                        base_url=base,
                        api_key=api_key,
                        model=model,
                        prompt=str(image_input["prompt"]),
                        image_paths=local_refs,
                        timeout=timeout,
                    )
                    kind = "edits"
                    ref_names = [p.name for p in local_refs]
                else:
                    parsed = call_generations(
                        base_url=base,
                        api_key=api_key,
                        model=model,
                        prompt=str(image_input["prompt"]),
                        size=size,
                        quality=quality,
                        timeout=timeout,
                    )
                    kind = "generations"
                    ref_names = []
                image_bytes = parse_image_response(parsed)
                meta = {
                    "source": "derouter-api",
                    "model": model,
                    "size": size,
                    "quality": quality,
                    "endpoint": kind,
                    "host": host,
                    "api_base": base,
                    "response_kind": "b64_json",
                    "attempts": attempts,
                }
                if ref_names:
                    meta["local_reference"] = ref_names[0]
                    if len(ref_names) > 1:
                        meta["local_references"] = ref_names
                return image_bytes, meta
            except DerouterRetryable as exc:
                last_error = exc
                print(
                    f"Derouter retryable ({exc}); host={host} "
                    f"attempt={attempt + 1}/{max_retries + 1}",
                    flush=True,
                )
                if attempt < max_retries and retry_wait > 0:
                    time.sleep(retry_wait)
                continue
            except DerouterApiError as exc:
                last_error = exc
                if is_discontinued_image_error(exc):
                    discontinued_hosts.append(host)
                    print(
                        f"Derouter image discontinued on {host}; trying next base",
                        flush=True,
                    )
                    break
                raise
    if discontinued_hosts and len(discontinued_hosts) >= len(bases):
        raise DerouterApiError(
            f"Derouter image model discontinued on all bases ({', '.join(discontinued_hosts)})"
        )
    raise DerouterApiError(f"Derouter failed after retries: {last_error}")


def run_kie_fallback(*, root: Path, article_dir: Path, batch: str, result: str) -> int:
    kie_script = root / "scripts" / "excalibur_blog_kie_gpt_image2_api.py"
    cmd = [
        sys.executable,
        str(kie_script),
        "--article-dir",
        str(article_dir.relative_to(root) if article_dir.is_relative_to(root) else article_dir),
        "--batch",
        batch,
        "--result",
        result,
    ]
    print("Derouter exhausted; falling back to Kie script", flush=True)
    proc = subprocess.run(cmd, cwd=str(root))
    return proc.returncode


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Generate one quad canvas via Derouter REST image API"
    )
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--batch", default="cover/quad-mcp-batch.json")
    ap.add_argument("--result", default="cover/quad-mcp-result.json")
    ap.add_argument("--api-key-env", default=DEFAULT_API_KEY_ENV)
    ap.add_argument("--primary-base", default=PRIMARY_DIRECT_BASE)
    ap.add_argument("--fallback-base", default=FALLBACK_DIRECT_BASE)
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    ap.add_argument("--max-retries", type=int, default=DEFAULT_MAX_RETRIES)
    ap.add_argument("--retry-wait", type=int, default=DEFAULT_RETRY_WAIT_SECONDS)
    ap.add_argument(
        "--fallback-kie",
        action="store_true",
        help="On Derouter auth/5xx after retries, run Kie script once",
    )
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    batch_path = resolve_path(root, args.article_dir, args.batch)
    result_path = resolve_path(root, args.article_dir, args.result)

    try:
        image_input = batch_mcp_args(batch_path)
        batch_meta = load_json(batch_path)
        model = default_model()
        size = default_size()
        quality = default_quality()
        local_refs = resolve_local_reference_paths(root=root, batch_path=batch_path)
        mode = "edits" if local_refs else "generations"

        dry_payload = {
            "mode": mode,
            "model": model,
            "size": size,
            "quality": quality,
            "api_base_candidates": image_api_base_candidates(
                primary_base=args.primary_base,
                fallback_base=args.fallback_base,
            ),
            "primary_base": args.primary_base,
            "fallback_base": args.fallback_base,
            "timeout_seconds": max(MIN_TIMEOUT_SECONDS, int(args.timeout)),
            "prompt_chars": len(str(image_input.get("prompt") or "")),
            "local_references": [
                str(p.relative_to(root)) if p.is_relative_to(root) else str(p) for p in local_refs
            ],
            "note": "images: try DEROUTER_IMAGE_API_BASE then 4 canonical hosts; b64_json only",
        }
        if args.dry_run:
            print(json.dumps(dry_payload, ensure_ascii=False, indent=2))
            return 0

        api_key = os.environ.get(args.api_key_env, "").strip()
        if not api_key:
            print(
                "❌ DEROUTER API KEY MISSING: set DEROUTER_API_KEY in Cloud Secrets/env; "
                "the key must not be committed or printed.",
                file=sys.stderr,
            )
            return 1

        image_bytes, meta = generate_image(
            root=root,
            batch_path=batch_path,
            image_input=image_input,
            api_key=api_key,
            model=model,
            size=size,
            quality=quality,
            timeout=max(MIN_TIMEOUT_SECONDS, int(args.timeout)),
            primary_base=args.primary_base,
            fallback_base=args.fallback_base,
            max_retries=max(0, int(args.max_retries)),
            retry_wait=max(0, int(args.retry_wait)),
        )

        output_canvas = str(batch_meta.get("output_canvas") or "").strip()
        if output_canvas:
            canvas_path = article_dir / output_canvas
        else:
            canvas_index = int(batch_meta.get("canvas_index") or 1)
            canvas_path = article_dir / "cover" / f"canvas-quad-{canvas_index:02d}.png"
        canvas_path.parent.mkdir(parents=True, exist_ok=True)
        canvas_path.write_bytes(image_bytes)
        rel_canvas = str(canvas_path.relative_to(article_dir))

        record: dict[str, Any] = {
            "local_path": rel_canvas,
            "source": "derouter-api",
            "model": model,
            "size": size,
            "quality": quality,
            "bytes": len(image_bytes),
            **meta,
        }
        save_json(result_path, record)
        print(f"OK local_path={rel_canvas} bytes={len(image_bytes)} mode={mode}")
        print(f"OK result={result_path}")
        return 0
    except DerouterRetryable as exc:
        if args.fallback_kie and os.environ.get("KIE_API_KEY", "").strip():
            return run_kie_fallback(
                root=root,
                article_dir=article_dir,
                batch=args.batch,
                result=args.result,
            )
        print(f"❌ DEROUTER BLOCKER: {exc}", file=sys.stderr)
        return 1
    except DerouterApiError as exc:
        if args.fallback_kie and os.environ.get("KIE_API_KEY", "").strip():
            return run_kie_fallback(
                root=root,
                article_dir=article_dir,
                batch=args.batch,
                result=args.result,
            )
        print(f"❌ DEROUTER BLOCKER: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
