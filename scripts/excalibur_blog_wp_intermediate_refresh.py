#!/usr/bin/env python3
"""Regenerate WordPress intermediate image sizes from live full PNGs (Dzen /feed/zen/)."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))

from excalibur_blog_live_cover_regen_aug22 import AUG22_REGEN_SLUGS  # noqa: E402
from excalibur_blog_site_base import resolve_public_base_from_env  # noqa: E402
from excalibur_blog_wp_publish import (  # noqa: E402
    is_missing_remote_path_error,
    load_env,
    project_root,
    sftp_remote_path,
    sftp_root_candidates,
    _ssh_creds,
)

ROOT = project_root()
UPLOADS_PREFIX = "wp-content/uploads/2026/08/"
INTERMEDIATE_RE = re.compile(r"-\d+x\d+(?=\.[a-z]+$)", re.I)
SCALED_RE = re.compile(r"-scaled(?=\.[a-z]+$)", re.I)
ZEN_UPLOAD_RE = re.compile(
    r"uploads/2026/08/([^\"'\s?#]+\.(?:png|jpe?g|webp))",
    re.I,
)


@dataclass
class SizeTarget:
    remote_name: str
    width: int
    height: int
    crop: bool
    source_full: str


def wp_constrain_dimensions(orig_w: int, orig_h: int, max_w: int, max_h: int) -> tuple[int, int]:
    if orig_w <= 0 or orig_h <= 0:
        return max_w, max_h
    if max_w <= 0:
        max_w = orig_w
    if max_h <= 0:
        max_h = orig_h
    if orig_w <= max_w and orig_h <= max_h:
        return orig_w, orig_h
    scale = min(max_w / orig_w, max_h / orig_h)
    return max(1, int(round(orig_w * scale))), max(1, int(round(orig_h * scale)))


def resize_wp_image(img: Image.Image, width: int, height: int, *, crop: bool) -> Image.Image:
    if crop:
        src_w, src_h = img.size
        scale = max(width / src_w, height / src_h)
        new_w = max(1, int(round(src_w * scale)))
        new_h = max(1, int(round(src_h * scale)))
        resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        left = max(0, (new_w - width) // 2)
        top = max(0, (new_h - height) // 2)
        return resized.crop((left, top, left + width, top + height))
    new_w, new_h = wp_constrain_dimensions(img.width, img.height, width, height)
    return img.resize((new_w, new_h), Image.Resampling.LANCZOS)


def png_bytes(img: Image.Image) -> bytes:
    buf = io.BytesIO()
    rgb = img.convert("RGBA") if img.mode in {"RGBA", "LA", "P"} else img.convert("RGB")
    rgb.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download_url(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "ExcaliburBlog/1.0"})
    with urlopen(req, timeout=120) as resp:
        return resp.read()


def wp_get_json(public_base: str, path: str) -> Any:
    url = f"{public_base.rstrip('/')}{path}" if path.startswith("/") else path
    req = Request(url, headers={"User-Agent": "ExcaliburBlog/1.0"})
    with urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))


def full_name_from_intermediate(name: str) -> str | None:
    if SCALED_RE.search(name):
        return SCALED_RE.sub("", name)
    if INTERMEDIATE_RE.search(name):
        return INTERMEDIATE_RE.sub("", name)
    return None


def is_intermediate_name(name: str) -> bool:
    return bool(INTERMEDIATE_RE.search(name) or SCALED_RE.search(name))


def size_targets_from_media(media: dict[str, Any]) -> list[SizeTarget]:
    sizes = (media.get("media_details") or {}).get("sizes") or {}
    full_file = sizes.get("full", {}).get("file") or media.get("source_url", "").rsplit("/", 1)[-1]
    if not full_file:
        return []
    targets: list[SizeTarget] = []
    for key, meta in sizes.items():
        if key == "full":
            continue
        remote = str(meta.get("file") or "").strip()
        if not remote or remote == full_file:
            continue
        width = int(meta.get("width") or 0)
        height = int(meta.get("height") or 0)
        if width <= 0 or height <= 0:
            continue
        crop = key == "thumbnail"
        targets.append(SizeTarget(remote, width, height, crop, full_file))
    return targets


def zen_feed_block(public_base: str, slug: str) -> str:
    feed = download_url(f"{public_base.rstrip('/')}/feed/zen/").decode("utf-8", errors="replace")
    pattern = (
        rf"<item>.*?<link>[^<]*/blog/{re.escape(slug)}/[^<]*</link>.*?</item>"
    )
    match = re.search(pattern, feed, re.S | re.I)
    if not match:
        raise RuntimeError(f"zen feed item not found for slug={slug}")
    return match.group(0)


def zen_upload_names(public_base: str, slug: str) -> list[str]:
    block = zen_feed_block(public_base, slug)
    return sorted(set(ZEN_UPLOAD_RE.findall(block)))


def post_media(public_base: str, slug: str) -> tuple[int, list[dict[str, Any]]]:
    posts = wp_get_json(public_base, f"/wp-json/wp/v2/posts?slug={slug}&_embed")
    if not posts:
        raise RuntimeError(f"WP post missing slug={slug}")
    post = posts[0]
    post_id = int(post["id"])
    media = wp_get_json(public_base, f"/wp-json/wp/v2/media?parent={post_id}&per_page=100")
    featured = ((post.get("_embedded") or {}).get("wp:featuredmedia") or [])
    if featured:
        fm = featured[0]
        if fm and fm.get("id"):
            media.append(fm)
    dedup: dict[int, dict[str, Any]] = {}
    for item in media:
        dedup[int(item["id"])] = item
    return post_id, list(dedup.values())


def collect_targets(public_base: str, slug: str) -> dict[str, list[SizeTarget]]:
    """Map full remote basename -> intermediate SizeTarget list."""
    _, media_items = post_media(public_base, slug)
    by_full: dict[str, list[SizeTarget]] = {}
    for media in media_items:
        targets = size_targets_from_media(media)
        if not targets:
            continue
        full_name = targets[0].source_full
        existing = {t.remote_name for t in by_full.get(full_name, [])}
        merged = list(by_full.get(full_name, []))
        for target in targets:
            if target.remote_name not in existing:
                merged.append(target)
                existing.add(target.remote_name)
        by_full[full_name] = merged

    for name in zen_upload_names(public_base, slug):
        if not is_intermediate_name(name):
            continue
        full_name = full_name_from_intermediate(name)
        if not full_name:
            continue
        dim = re.search(r"-(\d+)x(\d+)(?=\.[a-z]+$)", name, re.I)
        if not dim:
            continue
        width, height = int(dim.group(1)), int(dim.group(2))
        crop = width == height and width <= 200
        target = SizeTarget(name, width, height, crop, full_name)
        bucket = by_full.setdefault(full_name, [])
        if target.remote_name not in {t.remote_name for t in bucket}:
            bucket.append(target)
    return by_full


def upload_bytes_sftp(env: dict[str, str], remote_rel: str, data: bytes) -> str:
    import paramiko

    host, port, user, password = _ssh_creds(env)
    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    try:
        for root_candidate in sftp_root_candidates(env):
            full = sftp_remote_path(env, remote_rel, root_candidate)
            try:
                with sftp.open(full, "wb") as handle:
                    handle.write(data)
                print(f"SFTP upload OK: {full} ({len(data)} bytes)", flush=True)
                return full
            except OSError as exc:
                if is_missing_remote_path_error(exc):
                    continue
                raise
        raise RuntimeError(f"SFTP upload failed for {remote_rel}")
    finally:
        sftp.close()
        transport.close()


def refresh_slug(
    slug: str,
    *,
    public_base: str | None = None,
    env: dict[str, str] | None = None,
    upload: bool = True,
    dry_run: bool = False,
) -> dict[str, Any]:
    public_base = (public_base or resolve_public_base_from_env() or os.environ.get("PUBLIC_SITE_URL", "")).rstrip("/")
    if not public_base:
        raise RuntimeError("PUBLIC_SITE_URL missing")

    env = env or load_env(ROOT)
    targets_by_full = collect_targets(public_base, slug)
    uploads_dir = f"{public_base}/{UPLOADS_PREFIX}"
    report: dict[str, Any] = {
        "slug": slug,
        "full_images": [],
        "uploads": [],
        "skipped_same_hash": [],
        "zen_enclosures": [],
    }

    for full_name, targets in sorted(targets_by_full.items()):
        full_url = uploads_dir + full_name
        full_bytes = download_url(full_url)
        full_hash = sha256_hex(full_bytes)
        img = Image.open(io.BytesIO(full_bytes))
        entry: dict[str, Any] = {
            "full_remote": full_name,
            "full_bytes": len(full_bytes),
            "full_sha256": full_hash,
            "intermediates": [],
        }
        for target in sorted(targets, key=lambda t: t.remote_name):
            resized = resize_wp_image(img, target.width, target.height, crop=target.crop)
            out_bytes = png_bytes(resized)
            out_hash = sha256_hex(out_bytes)
            live_url = uploads_dir + target.remote_name
            try:
                live_bytes = download_url(live_url)
                live_hash = sha256_hex(live_bytes)
            except Exception:
                live_bytes = b""
                live_hash = ""
            changed = live_hash != out_hash
            row = {
                "remote": target.remote_name,
                "width": target.width,
                "height": target.height,
                "crop": target.crop,
                "bytes": len(out_bytes),
                "sha256": out_hash,
                "live_sha256": live_hash,
                "live_bytes": len(live_bytes),
                "changed": changed,
                "url": live_url,
            }
            entry["intermediates"].append(row)
            if target.remote_name.endswith("-1024x576.png") or "cover" in target.remote_name:
                report["zen_enclosures"].append(row)
            if not changed:
                report["skipped_same_hash"].append(target.remote_name)
                continue
            if dry_run:
                report["uploads"].append({**row, "dry_run": True})
                continue
            if upload:
                remote_rel = UPLOADS_PREFIX + target.remote_name
                upload_bytes_sftp(env, remote_rel, out_bytes)
                report["uploads"].append(row)
        report["full_images"].append(entry)
    return report


def refresh_after_full_upload(
    spec: dict[str, Any],
    *,
    public_base: str | None = None,
    env: dict[str, str] | None = None,
) -> dict[str, Any]:
    """После SFTP overwrite full PNG — обновить WP intermediates для cover (+ inline sizes)."""
    slug = str(spec.get("slug") or "").strip()
    if not slug:
        return {}
    return refresh_slug(slug, public_base=public_base, env=env, upload=True, dry_run=False)


def main() -> int:
    ap = argparse.ArgumentParser(description="Refresh WP intermediate PNGs used by /feed/zen/")
    ap.add_argument("--slug", help="single slug")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-upload", action="store_true", help="compute only")
    ap.add_argument(
        "--report",
        default=str(ROOT / "memory/blog/live-dzen-intermediate-refresh-report.json"),
        help="JSON report path",
    )
    args = ap.parse_args()

    slugs = [args.slug] if args.slug else list(AUG22_REGEN_SLUGS)
    combined: dict[str, Any] = {"slugs": slugs, "results": []}
    for slug in slugs:
        print(f"\n=== {slug} ===", flush=True)
        result = refresh_slug(slug, upload=not args.no_upload, dry_run=args.dry_run)
        combined["results"].append(result)
        print(json.dumps(result, ensure_ascii=False, indent=2))

    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(combined, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
