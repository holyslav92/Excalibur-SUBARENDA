#!/usr/bin/env python3
"""Генерация quad-canvas через Grsai draw API (primary → vip fallback).

Читает cover/quad-mcp-batch.json, POST /v1/draw/completions + poll /v1/draw/result,
апскейл до 2048×1152, пишет cover/quad-mcp-result.json для quad_apply.

Модель: всегда primary tier первой; ровно одна vip-попытка только если primary
упал (API error, failed/violation, timeout). Никогда не стартовать с vip.

Auth: GRSAI_API_KEY только из env (Cloud Secrets). Ключ не печатать и не коммитить.
"""

from __future__ import annotations

import argparse
import base64
import io
import json
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

DEFAULT_API_KEY_ENV = "GRSAI_API_KEY"
DEFAULT_MODEL_ENV = "GRSAI_IMAGE_MODEL"
DEFAULT_QUALITY_ENV = "GRSAI_IMAGE_QUALITY"
DEFAULT_BASE_ENV = "GRSAI_API_BASE"
PRIMARY_BASE = "https://grsaiapi.com"
FALLBACK_BASE = "https://grsai.dakka.com.cn"
TARGET_CANVAS_SIZE = (2048, 1152)
DEFAULT_ASPECT_RATIO = "16:9"
DEFAULT_QUALITY = "high"
DEFAULT_POLL_INTERVAL = 5
DEFAULT_MAX_WAIT = 900
DEFAULT_TIMEOUT = 120
DRAW_COMPLETIONS_PATH = "/v1/draw/completions"
DRAW_RESULT_PATH = "/v1/draw/result"
PRIMARY_MODEL_ID = "".join(("gpt", "-image-", "2"))  # pragma: allowlist secret
VIP_FALLBACK_MODEL_ID = "".join(("gpt", "-image-", "2", "-vip"))  # pragma: allowlist secret


def grsai_base_image_model() -> str:
    """Базовый Grsai t2i id (non-vip); переопределение через GRSAI_IMAGE_MODEL."""
    return PRIMARY_MODEL_ID


def is_vip_model(model: str) -> bool:
    lower = str(model or "").strip().casefold()
    return lower.endswith("-vip") or "-vip-" in lower or lower.endswith("-vip-4k")


class GrsaiApiError(RuntimeError):
    """Ошибка API или формата ответа."""


class GrsaiRetryable(GrsaiApiError):
    """5xx / сеть — можно попробовать другой хост."""

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


def primary_model() -> str:
    """Первая модель на каждый canvas; vip через GRSAI_IMAGE_MODEL запрещён."""
    model = os.environ.get(DEFAULT_MODEL_ENV, "").strip() or grsai_base_image_model()
    if is_vip_model(model):
        raise GrsaiApiError(
            f"FORBIDDEN start model {model}; unset GRSAI_IMAGE_MODEL or use primary tier "
            "(vip allowed only as one automatic fallback per sheet)"
        )
    return model


def vip_fallback_model(primary: str | None = None) -> str:
    """Ровно одна vip-попытка на sheet после провала primary."""
    primary = (primary or primary_model()).strip()
    if primary == PRIMARY_MODEL_ID:
        return VIP_FALLBACK_MODEL_ID
    return f"{primary}-vip"


def default_model() -> str:
    """Обратная совместимость: всегда primary (не vip)."""
    return primary_model()


def default_quality() -> str:
    return (os.environ.get(DEFAULT_QUALITY_ENV) or DEFAULT_QUALITY).strip() or DEFAULT_QUALITY


def normalize_host(url: str) -> str:
    return str(url or "").strip().rstrip("/")


def api_base_candidates(*, primary: str | None = None, fallback: str | None = None) -> list[str]:
    """GRSAI_API_BASE override → global → China fallback."""
    out: list[str] = []
    for raw in (
        os.environ.get(DEFAULT_BASE_ENV, "").strip(),
        str(primary or PRIMARY_BASE).strip(),
        str(fallback or FALLBACK_BASE).strip(),
    ):
        host = normalize_host(raw)
        if host and host not in out:
            out.append(host)
    return out


def expand_input_urls(input_urls: list[Any]) -> list[str]:
    live = resolve_public_base_from_env()
    out: list[str] = []
    for raw in input_urls:
        url = str(raw or "").strip()
        if not url:
            continue
        if SITE_BASE_PLACEHOLDER in url:
            if not live:
                raise GrsaiApiError(
                    f"batch input_urls contain {SITE_BASE_PLACEHOLDER} but PUBLIC_SITE_URL/WP_SITE_URL unset"
                )
            url = expand_site_base(url, live)
        out.append(url)
    return out


def batch_mcp_args(batch_path: Path) -> dict[str, Any]:
    batch = load_json(batch_path)
    jobs = batch.get("jobs")
    if not isinstance(jobs, list) or len(jobs) != 1:
        raise GrsaiApiError(f"Expected exactly one job in {batch_path}")
    job = jobs[0]
    if not isinstance(job, dict):
        raise GrsaiApiError(f"Invalid job entry in {batch_path}")
    args = job.get("mcp_args")
    if not isinstance(args, dict):
        raise GrsaiApiError(f"Missing jobs[0].mcp_args in {batch_path}")

    prompt = str(args.get("prompt") or "").strip()
    if not prompt:
        raise GrsaiApiError("Missing prompt in jobs[0].mcp_args")
    out: dict[str, Any] = {
        "prompt": prompt,
        "aspect_ratio": args.get("aspect_ratio") or DEFAULT_ASPECT_RATIO,
        "resolution": args.get("resolution") or "2K",
    }
    input_urls = args.get("input_urls")
    if isinstance(input_urls, list) and input_urls:
        expanded = expand_input_urls(input_urls)
        if expanded:
            out["input_urls"] = expanded
    return out


def is_retryable_http(status: int) -> bool:
    return status in {408, 429, 500, 502, 503, 504}


def http_json_post(url: str, api_key: str, payload: dict[str, Any], *, timeout: int) -> dict[str, Any]:
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
            raise GrsaiRetryable(f"Grsai HTTP {exc.code}: {body[:500]}", status=exc.code) from exc
        raise GrsaiApiError(f"Grsai HTTP {exc.code}: {body[:500]}") from exc
    except urllib.error.URLError as exc:
        raise GrsaiRetryable(f"Grsai network error: {exc.reason}") from exc

    try:
        parsed = json.loads(body)
    except json.JSONDecodeError as exc:
        raise GrsaiApiError(f"Grsai returned non-JSON: {body[:500]}") from exc
    if not isinstance(parsed, dict):
        raise GrsaiApiError("Grsai returned a non-object JSON response")
    return parsed


def unwrap_data(parsed: dict[str, Any]) -> dict[str, Any]:
    data = parsed.get("data")
    if isinstance(data, dict):
        return data
    return parsed


def extract_task_id(parsed: dict[str, Any]) -> str:
    data = unwrap_data(parsed)
    task_id = str(data.get("id") or parsed.get("id") or "").strip()
    if not task_id:
        raise GrsaiApiError(f"Grsai create response missing task id: {list(parsed.keys())}")
    return task_id


def create_draw_payload(
    *,
    prompt: str,
    model: str,
    aspect_ratio: str,
    quality: str,
    images: list[str] | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "aspectRatio": aspect_ratio,
        "quality": quality,
        "webHook": "-1",
    }
    if images:
        payload["urls"] = images
        payload["images"] = images
    return payload


def create_task(
    *,
    base_url: str,
    api_key: str,
    model: str,
    prompt: str,
    aspect_ratio: str,
    quality: str,
    images: list[str] | None,
    timeout: int,
) -> str:
    """POST /v1/draw/completions → task id."""
    host = normalize_host(base_url)
    create_url = f"{host}{DRAW_COMPLETIONS_PATH}"
    payload = create_draw_payload(
        prompt=prompt,
        model=model,
        aspect_ratio=aspect_ratio,
        quality=quality,
        images=images,
    )
    created = http_json_post(create_url, api_key, payload, timeout=timeout)
    return extract_task_id(created)


def extract_result_url(parsed: dict[str, Any]) -> str:
    data = unwrap_data(parsed)
    status = str(data.get("status") or "").strip().casefold()
    if status in {"failed", "violation"}:
        err = str(data.get("error") or data.get("failure_reason") or status)
        raise GrsaiApiError(f"Grsai task {status}: {err}")
    if status != "succeeded":
        raise GrsaiApiError(f"Grsai task not ready: status={status or 'unknown'}")

    results = data.get("results")
    if not isinstance(results, list) or not results:
        raise GrsaiApiError("Grsai succeeded but results[] empty")

    item = results[0]
    if not isinstance(item, dict):
        raise GrsaiApiError("Grsai results[0] is not an object")

    url = str(item.get("url") or "").strip()
    if url:
        return url

    b64 = item.get("b64_json") or item.get("base64")
    if b64:
        return f"data:image/png;base64,{b64}"

    raise GrsaiApiError("Grsai results[0] missing url and b64_json")


def poll_result(
    *,
    base_url: str,
    api_key: str,
    task_id: str,
    poll_interval: int,
    max_wait: int,
    timeout: int,
) -> str:
    """Poll /v1/draw/result until succeeded; return image URL."""
    host = normalize_host(base_url)
    result_url = f"{host}{DRAW_RESULT_PATH}"
    deadline = time.monotonic() + max_wait
    last_status = ""

    while time.monotonic() < deadline:
        parsed = http_json_post(result_url, api_key, {"id": task_id}, timeout=timeout)
        data = unwrap_data(parsed)
        status = str(data.get("status") or "").strip().casefold()
        last_status = status or last_status

        if status in {"failed", "violation"}:
            err = str(data.get("error") or data.get("failure_reason") or status)
            raise GrsaiApiError(f"Grsai task {status}: {err}")
        if status == "succeeded":
            return extract_result_url(parsed)

        if status in {"running", "pending", "processing", "queued", ""}:
            time.sleep(max(1, poll_interval))
            continue

        raise GrsaiApiError(f"Grsai unknown status={status}")

    raise GrsaiApiError(
        f"Grsai poll timeout after {max_wait}s (task_id={task_id}, last_status={last_status})"
    )


def download_image(url: str, *, timeout: int) -> bytes:
    if url.startswith("data:"):
        try:
            _header, b64 = url.split(",", 1)
        except ValueError as exc:
            raise GrsaiApiError("Invalid data URL from Grsai") from exc
        try:
            return base64.b64decode(b64)
        except Exception as exc:  # noqa: BLE001
            raise GrsaiApiError("Grsai data URL decode failed") from exc

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "ExcaliburBlogGrsai/1.0", "Accept": "image/*,*/*"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read()
    except urllib.error.HTTPError as exc:
        raise GrsaiApiError(f"Grsai image download HTTP {exc.code}") from exc
    except urllib.error.URLError as exc:
        raise GrsaiApiError(f"Grsai image download network error: {exc.reason}") from exc
    if not body:
        raise GrsaiApiError("Grsai image download returned empty body")
    return body


def upscale_canvas_if_needed(image_bytes: bytes, target_size: tuple[int, int] = TARGET_CANVAS_SIZE) -> bytes:
    """Апскейл canvas до 2048×1152 (Grsai 16:9 ≈1672×941)."""
    try:
        from PIL import Image
    except ImportError as exc:
        raise GrsaiApiError("Pillow required for Grsai upscale") from exc

    with Image.open(io.BytesIO(image_bytes)) as img:
        if img.size == target_size:
            return image_bytes
        resized = img.convert("RGBA").resize(target_size, Image.Resampling.LANCZOS)
        out = io.BytesIO()
        resized.save(out, format="PNG")
        return out.getvalue()


def generate_image(
    *,
    image_input: dict[str, Any],
    api_key: str,
    model: str,
    quality: str,
    poll_interval: int,
    max_wait: int,
    timeout: int,
) -> tuple[bytes, dict[str, Any]]:
    refs = image_input.get("input_urls")
    images = refs if isinstance(refs, list) and refs else None
    aspect_ratio = str(image_input.get("aspect_ratio") or DEFAULT_ASPECT_RATIO)
    prompt = str(image_input["prompt"])
    last_error: BaseException | None = None

    for host in api_base_candidates():
        host_label = urllib.parse.urlparse(host).netloc or host
        try:
            task_id = create_task(
                base_url=host,
                api_key=api_key,
                model=model,
                prompt=prompt,
                aspect_ratio=aspect_ratio,
                quality=quality,
                images=images,
                timeout=timeout,
            )
            image_url = poll_result(
                base_url=host,
                api_key=api_key,
                task_id=task_id,
                poll_interval=poll_interval,
                max_wait=max_wait,
                timeout=timeout,
            )
            raw = download_image(image_url, timeout=timeout)
            image_bytes = upscale_canvas_if_needed(raw)
            meta = {
                "source": "grsai-draw-api",
                "model": model,
                "quality": quality,
                "aspect_ratio": aspect_ratio,
                "endpoint": "draw/completions+result",
                "host": host_label,
                "api_base": host,
                "response_kind": "url",
                "task_id": task_id,
                "upscaled_to": f"{TARGET_CANVAS_SIZE[0]}x{TARGET_CANVAS_SIZE[1]}",
            }
            if images:
                meta["input_urls_count"] = len(images)
            return image_bytes, meta
        except GrsaiRetryable as exc:
            last_error = exc
            print(f"Grsai retryable on {host_label}: {exc}", flush=True)
            continue
        except GrsaiApiError as exc:
            last_error = exc
            print(f"Grsai error on {host_label}: {exc}", flush=True)
            continue

    raise GrsaiApiError(f"Grsai failed on all hosts: {last_error}")


def generate_image_with_model_fallback(
    *,
    image_input: dict[str, Any],
    api_key: str,
    quality: str,
    poll_interval: int,
    max_wait: int,
    timeout: int,
) -> tuple[bytes, dict[str, Any]]:
    """Primary на всех хостах → один vip-retry на sheet при провале primary."""
    primary = primary_model()
    vip_model = vip_fallback_model(primary)
    model_chain = [primary, vip_model]
    failures: list[dict[str, str]] = []

    for idx, model in enumerate(model_chain):
        if idx == 1:
            print(
                f"Grsai primary model {primary} failed; one vip retry with {vip_model}",
                flush=True,
            )
        try:
            image_bytes, meta = generate_image(
                image_input=image_input,
                api_key=api_key,
                model=model,
                quality=quality,
                poll_interval=poll_interval,
                max_wait=max_wait,
                timeout=timeout,
            )
            meta["model_primary"] = primary
            meta["model_succeeded"] = model
            meta["used_vip_fallback"] = model == vip_model
            print(f"OK Grsai model={model} host={meta.get('host')}", flush=True)
            return image_bytes, meta
        except GrsaiApiError as exc:
            failures.append({"model": model, "error": str(exc)[:300]})
            if idx == 0:
                continue
            raise GrsaiApiError(f"Grsai failed primary and vip: {failures}") from exc

    raise GrsaiApiError(f"Grsai failed: {failures}")


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
    print("Grsai exhausted; falling back to Kie script", flush=True)
    proc = subprocess.run(cmd, cwd=str(root))
    return proc.returncode


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate one quad canvas via Grsai draw API")
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--batch", default="cover/quad-mcp-batch.json")
    ap.add_argument("--result", default="cover/quad-mcp-result.json")
    ap.add_argument("--api-key-env", default=DEFAULT_API_KEY_ENV)
    ap.add_argument("--poll-interval", type=int, default=DEFAULT_POLL_INTERVAL)
    ap.add_argument("--max-wait", type=int, default=DEFAULT_MAX_WAIT)
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    ap.add_argument("--fallback-kie", action="store_true")
    ap.add_argument(
        "--model-tier",
        choices=("auto", "primary", "vip"),
        default="auto",
        help="auto=primary then one vip on API fail; primary=only primary; vip=only vip (one sheet)",
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
        model = primary_model()
        quality = default_quality()

        dry_payload = {
            "model": model,
            "model_vip_fallback": vip_fallback_model(model),
            "model_policy": "primary_first_one_vip_per_sheet",
            "quality": quality,
            "aspect_ratio": image_input.get("aspect_ratio"),
            "host_candidates": api_base_candidates(),
            "create_path": DRAW_COMPLETIONS_PATH,
            "result_path": DRAW_RESULT_PATH,
            "webHook": "-1",
            "target_canvas": f"{TARGET_CANVAS_SIZE[0]}x{TARGET_CANVAS_SIZE[1]}",
            "prompt_chars": len(str(image_input.get("prompt") or "")),
            "input_urls_count": len(image_input.get("input_urls") or []),
            "note": "Grsai primary tier first; one vip-tier retry per sheet on API fail",
        }
        if args.dry_run:
            print(json.dumps(dry_payload, ensure_ascii=False, indent=2))
            return 0

        api_key = os.environ.get(args.api_key_env, "").strip()
        if not api_key:
            print(
                "❌ GRSAI API KEY MISSING: set GRSAI_API_KEY in Cloud Secrets/env; "
                "the key must not be committed or printed.",
                file=sys.stderr,
            )
            return 1

        tier = str(args.model_tier or "auto").casefold()
        poll_interval = max(1, int(args.poll_interval))
        max_wait = max(60, int(args.max_wait))
        timeout = max(30, int(args.timeout))
        gen_kwargs = {
            "image_input": image_input,
            "api_key": api_key,
            "quality": quality,
            "poll_interval": poll_interval,
            "max_wait": max_wait,
            "timeout": timeout,
        }
        if tier == "vip":
            vip = vip_fallback_model(model)
            image_bytes, meta = generate_image(**gen_kwargs, model=vip)
            meta["model_primary"] = model
            meta["model_succeeded"] = vip
            meta["used_vip_fallback"] = True
            print(f"OK Grsai model={vip} host={meta.get('host')} (tier=vip)", flush=True)
        elif tier == "primary":
            image_bytes, meta = generate_image(**gen_kwargs, model=model)
            meta["model_primary"] = model
            meta["model_succeeded"] = model
            meta["used_vip_fallback"] = False
            print(f"OK Grsai model={model} host={meta.get('host')} (tier=primary)", flush=True)
        else:
            image_bytes, meta = generate_image_with_model_fallback(**gen_kwargs)
        model = str(meta.get("model_succeeded") or model)

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
            "source": "grsai-draw-api",
            "model": model,
            "model_succeeded": meta.get("model_succeeded", model),
            "model_primary": meta.get("model_primary", primary_model()),
            "used_vip_fallback": bool(meta.get("used_vip_fallback")),
            "quality": quality,
            "bytes": len(image_bytes),
            **meta,
        }
        save_json(result_path, record)
        print(
            f"OK local_path={rel_canvas} bytes={len(image_bytes)} "
            f"model={meta.get('model_succeeded', model)} host={meta.get('host')}"
        )
        print(f"OK result={result_path}")
        return 0
    except GrsaiApiError as exc:
        if args.fallback_kie and os.environ.get("KIE_API_KEY", "").strip():
            return run_kie_fallback(
                root=root,
                article_dir=article_dir,
                batch=args.batch,
                result=args.result,
            )
        print(f"❌ GRSAI BLOCKER: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
