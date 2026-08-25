#!/usr/bin/env python3
"""Генерация quad-canvas через Grsai draw API (PRIMARY_MODEL_ID only, vip disabled).

Читает cover/quad-mcp-batch.json, POST /v1/draw/completions + poll /v1/draw/result,
проверяет ≥2K (длинная сторона ≥2048), пишет cover/quad-mcp-result.json для quad_apply.

Модель: только PRIMARY_MODEL_ID; любые *-vip запрещены навсегда.
При undersized (~1672×941): одна доп. попытка тем же non-vip (другой host / explicit size).
Если после ретрая всё ещё undersized — отгружаем native non-vip кадр (vip_disabled, native WxH).

Auth: GRSAI_API_KEY только из env (Cloud Secrets). Ключ не печатать и не коммитить.
"""

from __future__ import annotations

import argparse
import base64
import io
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

DEFAULT_API_KEY_ENV = "GRSAI_API_KEY"
DEFAULT_MODEL_ENV = "GRSAI_IMAGE_MODEL"
DEFAULT_QUALITY_ENV = "GRSAI_IMAGE_QUALITY"
DEFAULT_BASE_ENV = "GRSAI_API_BASE"
PRIMARY_BASE = "https://grsaiapi.com"
FALLBACK_BASE = "https://grsai.dakka.com.cn"
TARGET_CANVAS_SIZE = (2048, 1152)
MIN_LONG_SIDE_2K = 2048
# Апскейл только если native уже «2K-class» (близко к 2K); ~1672×941 → ship native, не upscale.
NATIVE_2K_CLASS_MIN_LONG_SIDE = 1920
DEFAULT_ASPECT_RATIO = "16:9"
DEFAULT_RESOLUTION = "2K"
DEFAULT_QUALITY = "high"
# Grsai aspectRatio → native long side при resolution=2K (документировано в contract).
ASPECT_RATIO_2K_LONG_SIDE: dict[str, int] = {
    "16:9": 2048,
    "9:16": 2048,
    "1:1": 2048,
    "4:3": 2048,
    "3:4": 2048,
}
DEFAULT_POLL_INTERVAL = 5
DEFAULT_MAX_WAIT = 900
DEFAULT_TIMEOUT = 120
DRAW_COMPLETIONS_PATH = "/v1/draw/completions"
DRAW_RESULT_PATH = "/v1/draw/result"
PRIMARY_MODEL_ID = "".join(("gpt", "-image-", "2"))  # pragma: allowlist secret
# VIP навсегда отключён — не вызывать, не POST, не эскалировать.
VIP_DISABLED = True


def grsai_base_image_model() -> str:
    """Базовый Grsai t2i id (non-vip); переопределение через GRSAI_IMAGE_MODEL."""
    return PRIMARY_MODEL_ID


def is_vip_model(model: str) -> bool:
    lower = str(model or "").strip().casefold()
    return lower.endswith("-vip") or "-vip-" in lower or lower.endswith("-vip-4k")


def assert_non_vip_model(model: str) -> None:
    """Запрет любых *-vip моделей — навсегда."""
    if is_vip_model(model):
        raise GrsaiApiError(
            f"FORBIDDEN vip model {model}; vip_disabled forever — use {PRIMARY_MODEL_ID} only"
        )


class GrsaiApiError(RuntimeError):
    """Ошибка API или формата ответа."""


class GrsaiRetryable(GrsaiApiError):
    """5xx / сеть — можно попробовать другой хост."""

    def __init__(self, message: str, *, status: int | None = None) -> None:
        self.status = status
        super().__init__(message)


class Grsai2KNotMetError(GrsaiApiError):
    """Non-vip не отдал ≥2K — можно explicit-size retry или ship native."""

    def __init__(
        self,
        message: str,
        *,
        native_size: tuple[int, int] | None = None,
        image_bytes: bytes | None = None,
    ) -> None:
        self.native_size = native_size
        self.image_bytes = image_bytes
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
    """Единственная модель на каждый canvas; vip через GRSAI_IMAGE_MODEL запрещён."""
    model = os.environ.get(DEFAULT_MODEL_ENV, "").strip() or grsai_base_image_model()
    assert_non_vip_model(model)
    return model


def vip_fallback_model(primary: str | None = None) -> str:
    """VIP отключён навсегда — вызов запрещён."""
    raise GrsaiApiError(
        "vip_disabled: *-vip permanently disabled; use PRIMARY_MODEL_ID only"
    )


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

    logo_ref_url = str(args.get("logo_reference_url") or batch.get("logo_reference_url") or "").strip()
    if logo_ref_url:
        if SITE_BASE_PLACEHOLDER in logo_ref_url:
            live = resolve_public_base_from_env()
            if not live:
                raise GrsaiApiError(
                    f"batch logo_reference_url contains {SITE_BASE_PLACEHOLDER} but PUBLIC_SITE_URL unset"
                )
            logo_ref_url = expand_site_base(logo_ref_url, live)
        out.setdefault("input_urls", [])
        if logo_ref_url not in out["input_urls"]:
            out["input_urls"].append(logo_ref_url)

    logo_local = str(
        args.get("logo_reference_local")
        or batch.get("logo_reference_local")
        or ""
    ).strip()
    if logo_local:
        out["logo_reference_local"] = logo_local
    if args.get("logo_reference_in_generation") or batch.get("logo_reference_in_generation"):
        out["logo_reference_in_generation"] = True
    if _tenant_forbids_logo_reference(project_root()):
        _strip_logo_reference_fields(out)
    return out


def _tenant_forbids_logo_reference(root: Path) -> bool:
    cfg_path = root / "shared" / "tenant-config.json"
    if not cfg_path.is_file():
        return False
    try:
        tenant = json.loads(cfg_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    img = tenant.get("image_generation") or {}
    if img.get("logo_never_as_generation_reference") is True:
        return True
    mode = str(tenant.get("cover_mode") or "").strip().casefold()
    logo_mode = str(tenant.get("logo_mode") or mode).strip().casefold()
    if logo_mode in {
        "reference_in_generation",
        "logo_reference_in_generation",
        "reference_in_gen",
    }:
        return False
    return mode in {"brand_logo_paste", "brand_logo_composite", "paste_png"}


def _strip_logo_reference_fields(out: dict[str, Any]) -> None:
    out.pop("logo_reference_local", None)
    out.pop("logo_reference_in_generation", None)
    urls = out.get("input_urls")
    if isinstance(urls, list):
        filtered = [
            u
            for u in urls
            if "cropped-img_7143" not in str(u)
            and "logo-dobry-dom" not in str(u)
        ]
        if filtered:
            out["input_urls"] = filtered
        else:
            out.pop("input_urls", None)


def local_image_to_data_url(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def resolve_logo_reference_images(
    image_input: dict[str, Any],
    *,
    root: Path,
) -> list[str] | None:
    """Full-res logo reference для Grsai urls/aroma — локальный PNG без downscale."""
    if _tenant_forbids_logo_reference(root):
        return None
    refs: list[str] = []
    logo_local = str(image_input.get("logo_reference_local") or "").strip()
    if logo_local:
        local_path = Path(logo_local)
        if not local_path.is_absolute():
            local_path = root / local_path
        if local_path.is_file():
            refs.append(local_image_to_data_url(local_path))

    if refs:
        return refs

    raw_urls = image_input.get("input_urls")
    if isinstance(raw_urls, list):
        for raw in raw_urls:
            url = str(raw or "").strip()
            if url:
                refs.append(url)
    return refs or None


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


def is_2k_request_rejected(exc: BaseException) -> bool:
    """True если API отклонил size/aspect/resolution на non-vip."""
    msg = str(exc).casefold()
    needles = (
        "size",
        "aspect",
        "resolution",
        "dimension",
        "2k",
        "2048",
        "invalid parameter",
        "not support",
        "unsupported",
    )
    return any(n in msg for n in needles)


def image_dimensions(image_bytes: bytes) -> tuple[int, int]:
    try:
        from PIL import Image
    except ImportError as exc:
        raise GrsaiApiError("Pillow required for Grsai dimension check") from exc
    with Image.open(io.BytesIO(image_bytes)) as img:
        return img.size


def long_side(width: int, height: int) -> int:
    return max(width, height)


def create_draw_payload(
    *,
    prompt: str,
    model: str,
    aspect_ratio: str,
    quality: str,
    resolution: str = DEFAULT_RESOLUTION,
    images: list[str] | None = None,
    explicit_size: bool = False,
) -> dict[str, Any]:
    assert_non_vip_model(model)
    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "quality": quality,
        "webHook": "-1",
    }
    if explicit_size:
        # non-vip retry: явный pixel size 2048×1152
        payload["size"] = f"{TARGET_CANVAS_SIZE[0]}x{TARGET_CANVAS_SIZE[1]}"
    else:
        # non-vip: явный 2K request (aspectRatio + resolution)
        payload["aspectRatio"] = aspect_ratio
        payload["resolution"] = resolution
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
    resolution: str,
    images: list[str] | None,
    timeout: int,
    explicit_size: bool = False,
) -> str:
    """POST /v1/draw/completions → task id."""
    host = normalize_host(base_url)
    create_url = f"{host}{DRAW_COMPLETIONS_PATH}"
    payload = create_draw_payload(
        prompt=prompt,
        model=model,
        aspect_ratio=aspect_ratio,
        quality=quality,
        resolution=resolution,
        images=images,
        explicit_size=explicit_size,
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
    """Апскейл canvas до 2048×1152 только если native уже 2K-class."""
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


def ensure_2k_canvas(
    image_bytes: bytes,
    *,
    model: str,
    target_size: tuple[int, int] = TARGET_CANVAS_SIZE,
    accept_undersized: bool = False,
) -> tuple[bytes, dict[str, Any]]:
    """Проверка ≥2K; upscale только для 2K-class native; иначе Grsai2KNotMetError или ship native."""
    assert_non_vip_model(model)
    width, height = image_dimensions(image_bytes)
    native_long = long_side(width, height)
    meta: dict[str, Any] = {
        "native_width": width,
        "native_height": height,
        "native_long_side": native_long,
        "min_long_side_required": MIN_LONG_SIDE_2K,
    }

    if native_long >= MIN_LONG_SIDE_2K:
        if (width, height) == target_size:
            meta["delivery"] = "native_2k"
            return image_bytes, meta
        upscaled = upscale_canvas_if_needed(image_bytes, target_size)
        meta["delivery"] = "native_2k_normalized"
        meta["normalized_to"] = f"{target_size[0]}x{target_size[1]}"
        return upscaled, meta

    if native_long >= NATIVE_2K_CLASS_MIN_LONG_SIDE:
        upscaled = upscale_canvas_if_needed(image_bytes, target_size)
        meta["delivery"] = "upscaled_2k_class"
        meta["upscaled_to"] = f"{target_size[0]}x{target_size[1]}"
        return upscaled, meta

    if accept_undersized:
        meta["delivery"] = "native_undersized_vip_disabled"
        meta["vip_disabled"] = True
        meta["shipped_native"] = f"{width}x{height}"
        print(
            f"vip_disabled: shipping largest native non-vip frame {width}x{height}",
            flush=True,
        )
        return image_bytes, meta

    raise Grsai2KNotMetError(
        f"primary returned undersized {width}x{height} (long={native_long} < "
        f"{NATIVE_2K_CLASS_MIN_LONG_SIDE}); explicit-size retry allowed",
        native_size=(width, height),
        image_bytes=image_bytes,
    )


def generate_image(
    *,
    image_input: dict[str, Any],
    api_key: str,
    model: str,
    quality: str,
    poll_interval: int,
    max_wait: int,
    timeout: int,
    root: Path | None = None,
    explicit_size: bool = False,
    accept_undersized: bool = False,
    host_candidates_override: list[str] | None = None,
) -> tuple[bytes, dict[str, Any]]:
    assert_non_vip_model(model)
    root = root or project_root()
    images = resolve_logo_reference_images(image_input, root=root)
    aspect_ratio = str(image_input.get("aspect_ratio") or DEFAULT_ASPECT_RATIO)
    resolution = str(image_input.get("resolution") or DEFAULT_RESOLUTION)
    prompt = str(image_input["prompt"])
    last_error: BaseException | None = None
    last_2k_error: Grsai2KNotMetError | None = None
    last_undersized_bytes: bytes | None = None

    hosts = host_candidates_override if host_candidates_override is not None else api_base_candidates()
    for host in hosts:
        host_label = urllib.parse.urlparse(host).netloc or host
        try:
            task_id = create_task(
                base_url=host,
                api_key=api_key,
                model=model,
                prompt=prompt,
                aspect_ratio=aspect_ratio,
                quality=quality,
                resolution=resolution,
                images=images,
                timeout=timeout,
                explicit_size=explicit_size,
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
            image_bytes, size_meta = ensure_2k_canvas(
                raw,
                model=model,
                accept_undersized=accept_undersized,
            )
            meta = {
                "source": "grsai-draw-api",
                "model": model,
                "quality": quality,
                "aspect_ratio": aspect_ratio,
                "resolution": resolution,
                "explicit_size": explicit_size,
                "endpoint": "draw/completions+result",
                "host": host_label,
                "api_base": host,
                "response_kind": "url",
                "task_id": task_id,
                "target_canvas": f"{TARGET_CANVAS_SIZE[0]}x{TARGET_CANVAS_SIZE[1]}",
                "vip_disabled": VIP_DISABLED,
                **size_meta,
            }
            if images:
                meta["input_urls_count"] = len(images)
                meta["logo_reference_in_generation"] = bool(image_input.get("logo_reference_in_generation"))
            return image_bytes, meta
        except Grsai2KNotMetError as exc:
            last_2k_error = exc
            if exc.image_bytes is not None:
                last_undersized_bytes = exc.image_bytes
            print(f"Grsai 2K not met on {host_label}: {exc}", flush=True)
            if accept_undersized and last_undersized_bytes is not None:
                image_bytes, size_meta = ensure_2k_canvas(
                    last_undersized_bytes,
                    model=model,
                    accept_undersized=True,
                )
                meta = {
                    "source": "grsai-draw-api",
                    "model": model,
                    "quality": quality,
                    "aspect_ratio": aspect_ratio,
                    "resolution": resolution,
                    "explicit_size": explicit_size,
                    "endpoint": "draw/completions+result",
                    "host": host_label,
                    "api_base": host,
                    "response_kind": "url",
                    "target_canvas": f"{TARGET_CANVAS_SIZE[0]}x{TARGET_CANVAS_SIZE[1]}",
                    "vip_disabled": VIP_DISABLED,
                    **size_meta,
                }
                return image_bytes, meta
            raise
        except GrsaiRetryable as exc:
            last_error = exc
            print(f"Grsai retryable on {host_label}: {exc}", flush=True)
            continue
        except GrsaiApiError as exc:
            last_error = exc
            if is_2k_request_rejected(exc):
                raise Grsai2KNotMetError(str(exc)) from exc
            print(f"Grsai error on {host_label}: {exc}", flush=True)
            continue

    if last_2k_error is not None:
        raise last_2k_error
    raise GrsaiApiError(f"Grsai failed on all hosts: {last_error}")


def _alternate_host_order() -> list[str]:
    """Для explicit-size retry: сначала fallback host, потом primary."""
    hosts = api_base_candidates()
    if len(hosts) <= 1:
        return hosts
    return list(reversed(hosts))


def generate_image_with_model_fallback(
    *,
    image_input: dict[str, Any],
    api_key: str,
    quality: str,
    poll_interval: int,
    max_wait: int,
    timeout: int,
    root: Path | None = None,
) -> tuple[bytes, dict[str, Any]]:
    """Только PRIMARY_MODEL_ID: aspectRatio+2K → explicit-size retry → ship native undersized."""
    primary = primary_model()
    gen_kwargs = {
        "image_input": image_input,
        "api_key": api_key,
        "quality": quality,
        "poll_interval": poll_interval,
        "max_wait": max_wait,
        "timeout": timeout,
        "root": root,
        "model": primary,
    }

    try:
        image_bytes, meta = generate_image(**gen_kwargs, explicit_size=False)
        meta["model_primary"] = primary
        meta["model_succeeded"] = primary
        meta["used_vip_fallback"] = False
        meta["vip_disabled"] = True
        meta["vip_trigger"] = None
        print(f"OK Grsai model={primary} host={meta.get('host')} (native 2K)", flush=True)
        return image_bytes, meta
    except Grsai2KNotMetError as exc:
        print(
            f"Grsai primary {primary} undersized ({exc}); "
            f"one explicit-size retry on same model (vip_disabled)",
            flush=True,
        )
        try:
            image_bytes, meta = generate_image(
                **gen_kwargs,
                explicit_size=True,
                host_candidates_override=_alternate_host_order(),
            )
            meta["model_primary"] = primary
            meta["model_succeeded"] = primary
            meta["used_vip_fallback"] = False
            meta["vip_disabled"] = True
            meta["vip_trigger"] = None
            meta["undersized_retry"] = "explicit_size_alternate_host"
            print(
                f"OK Grsai model={primary} host={meta.get('host')} "
                f"(explicit-size retry, delivery={meta.get('delivery')})",
                flush=True,
            )
            return image_bytes, meta
        except Grsai2KNotMetError as retry_exc:
            if retry_exc.image_bytes is not None:
                image_bytes, size_meta = ensure_2k_canvas(
                    retry_exc.image_bytes,
                    model=primary,
                    accept_undersized=True,
                )
                meta = {
                    "source": "grsai-draw-api",
                    "model": primary,
                    "quality": quality,
                    "vip_disabled": True,
                    "undersized_retry": "ship_native_vip_disabled",
                    **size_meta,
                }
                meta["model_primary"] = primary
                meta["model_succeeded"] = primary
                meta["used_vip_fallback"] = False
                meta["vip_trigger"] = None
                print(
                    f"OK Grsai model={primary} shipped native {meta.get('shipped_native')} "
                    f"(vip_disabled)",
                    flush=True,
                )
                return image_bytes, meta
            raise GrsaiApiError(
                f"Grsai primary {primary} undersized after retries and no native bytes to ship"
            ) from retry_exc


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
        choices=("auto", "primary"),
        default="auto",
        help="auto|primary=PRIMARY_MODEL_ID only (vip permanently disabled)",
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
            "model_policy": "gpt_image_2_only_vip_disabled",
            "vip_disabled": True,
            "quality": quality,
            "aspect_ratio": image_input.get("aspect_ratio"),
            "resolution": image_input.get("resolution") or DEFAULT_RESOLUTION,
            "min_long_side_2k": MIN_LONG_SIDE_2K,
            "target_canvas": f"{TARGET_CANVAS_SIZE[0]}x{TARGET_CANVAS_SIZE[1]}",
            "host_candidates": api_base_candidates(),
            "create_path": DRAW_COMPLETIONS_PATH,
            "result_path": DRAW_RESULT_PATH,
            "webHook": "-1",
            "prompt_chars": len(str(image_input.get("prompt") or "")),
            "input_urls_count": len(image_input.get("input_urls") or []),
            "note": (
                "PRIMARY_MODEL_ID only; vip permanently disabled; "
                "aspectRatio+resolution=2K first, one explicit-size retry, then ship native undersized"
            ),
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
            "root": root,
        }
        if tier == "primary":
            image_bytes, meta = generate_image(**gen_kwargs, model=model)
            meta["model_primary"] = model
            meta["model_succeeded"] = model
            meta["used_vip_fallback"] = False
            meta["vip_disabled"] = True
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
            "used_vip_fallback": False,
            "vip_disabled": True,
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
