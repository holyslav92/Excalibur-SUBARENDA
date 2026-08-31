#!/usr/bin/env python3
"""Live cover-only regen for B04 — scene_poster_v2, cover-v2.png cache-bust."""

from __future__ import annotations

import base64
import json
import os
import subprocess
import sys
import time
from io import BytesIO
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from excalibur_blog_site_base import resolve_public_base_from_env  # noqa: E402
from excalibur_blog_wp_publish import (  # noqa: E402
    delete_bootstrap_sftp,
    load_env,
    project_root,
    publish_via_ftp,
    upload_bootstrap_sftp,
)

ROOT = project_root()
SLUG = "oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego"
TOPIC_ID = "B04"
POST_ID = 4178
VERSION_TAG = "cover-v2"
REMOTE_SUBDIR = "2026/08"
DZEN_SIZE = (1024, 576)
COVER_PROMPT = (
    "EDITORIAL SCENE POSTER 16:9 full-bleed cinematic still, comfort+ Tyumen apartment doorway "
    "natural daylight August evening. Three guests at apartment door: couple plus third person with "
    "suitcase; host in doorway holds small paper card showing extra fee +1500 rubles per night — "
    "readable but subtle, not collage headline. Lived-in bright stairwell, warm natural light, "
    "magazine-clean designed still like premium infographic frame. "
    "Phone EXACT +7 (993) 574-83-22 painted IN SCENE on door intercom plate or paper on door — "
    "readable Cyrillic, NOT opaque pill. "
    "TOP-RIGHT empty clear pad 10% — no logo, no house icon, no Добрый дом lettering, no plate. "
    "BAN: meme cutouts, cat stickers, Roll Safe, sticker soup, torn-paper, gold glitter, yellow sticky, "
    "split white-panel collage, phone pill, model-drawn logo, house-with-heart, empty stock, WP UI."
)


def article_dir() -> Path:
    return ROOT / f"memory/blog/articles/{TOPIC_ID}-{SLUG}"


def remote_cover_name() -> str:
    return f"{SLUG}-{VERSION_TAG}.png"


def remote_dzen_name() -> str:
    return f"{SLUG}-{VERSION_TAG}-1024x576.png"


def generate_cover_canvas(adir: Path) -> Path:
    cover_dir = adir / "cover"
    cover_dir.mkdir(parents=True, exist_ok=True)
    batch_path = cover_dir / "cover-mcp-batch.json"
    result_path = cover_dir / "cover-mcp-result.json"
    prompt_path = cover_dir / "cover-mcp-prompt.txt"
    prompt_path.write_text(COVER_PROMPT + "\n", encoding="utf-8")
    batch = {
        "pipeline": "scene_poster_v2_live_b04",
        "canvas_index": 0,
        "standalone_cover": True,
        "output_canvas": "cover/cover-canvas.png",
        "result_path": "cover/cover-mcp-result.json",
        "jobs": [
            {
                "slot": "cover_standalone",
                "tool": "grsai",
                "mcp_args": {
                    "prompt": COVER_PROMPT,
                    "aspect_ratio": "16:9",
                    "resolution": "2K",
                },
            }
        ],
    }
    batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/excalibur_blog_grsai_gpt_image2_api.py"),
            "--article-dir",
            str(adir),
            "--batch",
            "cover/cover-mcp-batch.json",
            "--result",
            "cover/cover-mcp-result.json",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"Grsai generation failed: {proc.stderr or proc.stdout}")

    result = json.loads(result_path.read_text(encoding="utf-8"))
    local_rel = str(result.get("local_path") or "cover/cover-canvas.png")
    canvas_path = adir / local_rel
    if not canvas_path.is_file():
        canvas_path = cover_dir / "cover-canvas.png"
    if not canvas_path.is_file():
        raise FileNotFoundError("cover-canvas.png missing after generation")
    return canvas_path


def apply_cover_pipeline(adir: Path) -> Path:
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/excalibur_blog_cover_standalone_apply.py"),
            "--article-dir",
            str(adir),
            "--source",
            "cover-canvas.png",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"standalone apply failed: {proc.stderr or proc.stdout}")
    cover_path = adir / "cover" / "cover.png"
    if not cover_path.is_file():
        raise FileNotFoundError("cover.png missing after apply")
    return cover_path


def make_dzen_thumb(cover_path: Path) -> bytes:
    from PIL import Image

    with Image.open(cover_path) as img:
        thumb = img.convert("RGBA").resize(DZEN_SIZE, Image.Resampling.LANCZOS)
        buf = BytesIO()
        thumb.save(buf, format="PNG", optimize=True)
        return buf.getvalue()


def upload_cover_files(cover_path: Path) -> dict[str, str]:
    from excalibur_blog_remote_transport import connect_ftp, _ftp_cwd_root, _ftp_stor_with_retry

    env = load_env(ROOT)
    public = resolve_public_base_from_env() or os.environ.get("PUBLIC_SITE_URL", "").rstrip("/")
    cover_remote = remote_cover_name()
    dzen_remote = remote_dzen_name()
    files = {
        cover_remote: cover_path.read_bytes(),
        dzen_remote: make_dzen_thumb(cover_path),
    }
    root = (env.get("FTP_ROOT") or ".").strip() or "."
    remote_dir = f"wp-content/uploads/{REMOTE_SUBDIR}"
    cache_bust = int(time.time())
    urls: dict[str, str] = {}
    for remote_name, data in files.items():
        ftp = connect_ftp(env, timeout=180)
        try:
            login_cwd = ftp.pwd()
            _ftp_cwd_root(ftp, root, login_cwd)
            for part in remote_dir.split("/"):
                if part:
                    ftp.cwd(part)
            _ftp_stor_with_retry(ftp, remote_name, data, attempts=5, retry_pause_s=3.0)
            print(f"FTP upload OK: {remote_dir}/{remote_name} ({len(data)} bytes)", flush=True)
            urls[remote_name] = f"{public}/{remote_dir}/{remote_name}?v={cache_bust}"
        finally:
            try:
                ftp.quit()
            except Exception:
                ftp.close()
    return urls


def update_wp_featured(urls: dict[str, str]) -> str:
    public = resolve_public_base_from_env() or os.environ.get("PUBLIC_SITE_URL", "").rstrip("/")
    payload: dict[str, Any] = {
        "post_id": POST_ID,
        "slug": SLUG,
        "cover_remote": remote_cover_name(),
        "dzen_remote": remote_dzen_name(),
        "cache_bust": int(time.time()),
        "cover_only": True,
    }
    encoded = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    php = f"""<?php
require __DIR__ . '/wp-load.php';
$p = json_decode(base64_decode('{encoded}'), true);
$post_id = (int) ($p['post_id'] ?? 0);
$post = get_post($post_id);
if (!$post) {{ echo 'ERR post not found' . PHP_EOL; exit(1); }}
$upload_dir = wp_upload_dir();
$subdir = '{REMOTE_SUBDIR}';
$cover_remote = (string) ($p['cover_remote'] ?? '');
$dzen_remote = (string) ($p['dzen_remote'] ?? '');
$cover_path = $upload_dir['basedir'] . '/' . $subdir . '/' . $cover_remote;
$dzen_path = $dzen_remote !== '' ? $upload_dir['basedir'] . '/' . $subdir . '/' . $dzen_remote : '';
if (!is_file($cover_path)) {{
    echo 'ERR cover file missing: ' . $cover_path . PHP_EOL;
    exit(1);
}}
require_once ABSPATH . 'wp-admin/includes/image.php';
$filetype = wp_check_filetype($cover_remote, null);
$attachment = [
    'post_mime_type' => $filetype['type'] ?: 'image/png',
    'post_title' => sanitize_file_name($cover_remote),
    'post_content' => '',
    'post_status' => 'inherit',
];
$attach_id = wp_insert_attachment($attachment, $cover_path, $post_id);
if (!$attach_id || is_wp_error($attach_id)) {{
    echo 'ERR attachment' . PHP_EOL;
    exit(1);
}}
$meta = wp_generate_attachment_metadata((int) $attach_id, $cover_path);
if (is_array($meta)) {{
    if ($dzen_remote !== '' && is_file($dzen_path)) {{
        $meta['sizes']['dzen'] = [
            'file' => $dzen_remote,
            'width' => 1024,
            'height' => 576,
            'mime-type' => 'image/png',
        ];
    }}
    wp_update_attachment_metadata((int) $attach_id, $meta);
}}
set_post_thumbnail($post_id, (int) $attach_id);
update_post_meta($post_id, '_excalibur_cover_remote', $cover_remote);
$now_local = current_time('mysql');
$now_gmt = current_time('mysql', 1);
wp_update_post([
    'ID' => $post_id,
    'post_modified' => $now_local,
    'post_modified_gmt' => $now_gmt,
]);
echo 'OK featured_image=' . (int) $attach_id . PHP_EOL;
echo 'OK cover_url=' . $upload_dir['baseurl'] . '/' . $subdir . '/' . $cover_remote . PHP_EOL;
"""
    env = load_env(ROOT)
    bootstrap_name = f"excalibur-cover-v2-{SLUG[:24]}.php"
    if (env.get("FTP_TRANSPORT") or "").strip().lower() == "ftp":
        return publish_via_ftp(env, php, public, bootstrap_name=bootstrap_name)
    uploaded_path = upload_bootstrap_sftp(env, bootstrap_name, php.encode("utf-8"))
    url = public.rstrip("/") + "/" + bootstrap_name
    proc = subprocess.run(
        ["curl", "-sS", "-m", "180", url],
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr or proc.stdout)
        return proc.stdout
    finally:
        try:
            delete_bootstrap_sftp(env, bootstrap_name, uploaded_path)
        except Exception:
            pass


def verify_http(url: str) -> int:
    proc = subprocess.run(
        ["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", url],
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        return int(proc.stdout.strip())
    except ValueError:
        return 0


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--upload-only", action="store_true", help="Skip generation; upload existing cover.png")
    args = ap.parse_args()

    adir = article_dir()
    if not adir.is_dir():
        print(f"BLOCKER: missing {adir}", file=sys.stderr)
        return 1
    if not args.upload_only:
        print("STEP generate cover canvas", flush=True)
        generate_cover_canvas(adir)
        print("STEP apply standalone cover + logo", flush=True)
        apply_cover_pipeline(adir)
    cover_path = adir / "cover" / "cover.png"
    if not cover_path.is_file():
        print("BLOCKER: cover.png missing", file=sys.stderr)
        return 1
    print("STEP upload SFTP", flush=True)
    urls = upload_cover_files(cover_path)
    print("STEP update WP featured", flush=True)
    wp_out = update_wp_featured(urls)
    print(wp_out, flush=True)
    public_url = urls[remote_cover_name()].split("?")[0]
    code = verify_http(public_url)
    report = {
        "slug": SLUG,
        "topic_id": TOPIC_ID,
        "version_tag": VERSION_TAG,
        "cover_remote": remote_cover_name(),
        "public_url": public_url,
        "http_status": code,
        "wp_output": wp_out.strip(),
    }
    report_path = ROOT / "memory/blog/live-cover-b04-scene-v2-report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if code == 200 else 1


if __name__ == "__main__":
    raise SystemExit(main())
