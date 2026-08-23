#!/usr/bin/env python3
"""Live regen: passport article — 8 images with logo Grsai reference + logo-ref-v1 filenames."""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from excalibur_blog_live_cover_regen_aug22 import (  # noqa: E402
    ROOT,
    article_dir,
    bootstrap,
    build_spec_from_wp,
    ensure_logo_asset,
    pipeline,
    run,
    wp_get,
)
from excalibur_blog_site_base import resolve_public_base_from_env  # noqa: E402
from excalibur_blog_wp_publish import (  # noqa: E402
    delete_bootstrap_sftp,
    load_env,
    upload_bootstrap_sftp,
)

SLUG = "poprosili-foto-pasporta-pri-zaselenii-posutochno-chto-zakonno"
VERSION_TAG = "logo-ref-v1"
DZEN_SIZE = (1024, 576)


def spec_with_logo_ref_names(slug: str) -> dict[str, Any]:
    spec = build_spec_from_wp(slug)
    spec.update(
        {
            "topic_id": "LIVE-passport-photo",
            "hook": "Просят фото паспорта при заселении",
            "highlight": "паспорта",
            "sticky": "законно?",
            "wordstat": ["фото паспорта", "Тюмень", "заселение посуточно"],
            "cover_emotion": "шок: хозяин требует фото паспорта в чат до заселения",
            "cover_scene": (
                "Phone chat passport photo demand vs blurred ID; bold hook; daylight, no yellow cast; logo ref top-right"
            ),
            "motif_composition": "passport photo request chat + blurred document comparison poster",
            "motif_meme": "cat with magnifying glass sticker bottom-left ≤10%",
            "motif_props": "phone chat, blurred passport, torn sticky, gold tape",
            "motif_joke": "cat inspects suspicious passport request",
            "cover_remote": f"{slug}-cover-{VERSION_TAG}.png",
            "inline_remote": f"{slug}-inline-{{n:02d}}-{VERSION_TAG}.png",
        }
    )
    return spec


def make_dzen_thumb(cover_path: Path) -> bytes:
    from PIL import Image

    with Image.open(cover_path) as img:
        thumb = img.convert("RGBA").resize(DZEN_SIZE, Image.Resampling.LANCZOS)
        buf = BytesIO()
        thumb.save(buf, format="PNG", optimize=True)
        return buf.getvalue()


def upload_logo_ref_files(spec: dict, adir: Path) -> dict[str, str]:
    """FTP upload cover + 7 inline + dzen 1024x576 thumb (single connection)."""
    from excalibur_blog_remote_transport import connect_ftp, _ftp_cwd_root, _ftp_stor_with_retry

    env = dict(os.environ)
    root = (env.get("FTP_ROOT") or ".").strip() or "."
    remote_dir = "wp-content/uploads/2026/08"
    public = resolve_public_base_from_env() or os.environ.get("PUBLIC_SITE_URL", "").rstrip("/")
    urls: dict[str, str] = {}
    cover_remote = spec["cover_remote"]
    dzen_remote = f"{spec['slug']}-cover-{VERSION_TAG}-1024x576.png"
    files: dict[str, bytes] = {}
    for n in range(1, 8):
        remote = spec["inline_remote"].format(n=n)
        files[remote] = (adir / "cover" / f"inline-{n:02d}.png").read_bytes()
    files[cover_remote] = (adir / "cover" / "cover.png").read_bytes()
    files[dzen_remote] = make_dzen_thumb(adir / "cover" / "cover.png")

    ftp = connect_ftp(env, timeout=180)
    try:
        login_cwd = ftp.pwd()
        _ftp_cwd_root(ftp, root, login_cwd)
        for part in remote_dir.split("/"):
            if part:
                ftp.cwd(part)
        for remote_name, data in files.items():
            _ftp_stor_with_retry(ftp, remote_name, data, attempts=5, retry_pause_s=3.0)
            print(f"FTP OK {remote_dir}/{remote_name} ({len(data)} bytes)", flush=True)
            urls[remote_name] = f"{public}/{remote_dir}/{remote_name}?v={int(time.time())}"
    finally:
        try:
            ftp.quit()
        except Exception:
            ftp.close()

    urls["cover"] = urls.get(cover_remote, "")
    urls["dzen"] = urls.get(dzen_remote, "")
    return urls


def run_php_bootstrap(env: dict[str, str], php: str, public_base: str, *, bootstrap_name: str) -> str:
    runtime_env = dict(env)
    configured_root = (runtime_env.get("FTP_ROOT") or runtime_env.get("SSH_ROOT") or "").strip()
    if configured_root:
        runtime_env["SSH_ROOT"] = configured_root
        runtime_env["FTP_ROOT"] = configured_root
    if not (runtime_env.get("SSH_HOST") or "").strip():
        runtime_env["SSH_HOST"] = (runtime_env.get("FTP_HOST") or "").strip()
    if not (runtime_env.get("SSH_PORT") or "").strip():
        runtime_env["SSH_PORT"] = "22"
    uploaded_path = upload_bootstrap_sftp(runtime_env, bootstrap_name, php.encode("utf-8"))
    url = public_base.rstrip("/") + "/" + bootstrap_name
    proc = subprocess.run(
        ["curl", "-sS", "-m", "180", url],
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        if proc.returncode != 0:
            raise RuntimeError(f"curl bootstrap failed: {proc.stderr}")
        return proc.stdout
    finally:
        try:
            delete_bootstrap_sftp(runtime_env, bootstrap_name, uploaded_path)
        except Exception:
            pass


def update_wp_post(spec: dict, urls: dict[str, str], post_id: int) -> str:
    public = resolve_public_base_from_env() or os.environ.get("PUBLIC_SITE_URL", "").rstrip("/")
    payload = {
        "post_id": post_id,
        "slug": spec["slug"],
        "cover_remote": spec["cover_remote"],
        "inline_remote": spec["inline_remote"],
        "inline_count": 7,
        "cover_url": urls.get("cover", ""),
        "dzen_url": urls.get("dzen", ""),
        "cache_bust": int(time.time()),
    }
    encoded = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    php = f"""<?php
require __DIR__ . '/wp-load.php';
$p = json_decode(base64_decode('{encoded}'), true);
$post_id = (int) ($p['post_id'] ?? 0);
if ($post_id <= 0) {{
    echo 'ERR missing post_id' . PHP_EOL;
    exit(1);
}}
$post = get_post($post_id);
if (!$post) {{
    echo 'ERR post not found' . PHP_EOL;
    exit(1);
}}
$content = (string) $post->post_content;
$inline_remote = (string) ($p['inline_remote'] ?? '');
for ($n = 1; $n <= (int) ($p['inline_count'] ?? 7); $n++) {{
    $remote = str_replace('{n:02d}', sprintf('%02d', $n), $inline_remote);
    $content = preg_replace(
        '/poprosili-foto-pasporta[^"\\']*inline-' . sprintf('%02d', $n) . '[^"\\']*\\.png(\\?[^"\\']*)?/i',
        $remote . '?v=' . (int) $p['cache_bust'],
        $content
    );
}}
$cover_remote = (string) ($p['cover_remote'] ?? '');
$content = preg_replace(
    '/poprosili-foto-pasporta[^"\\']*cover[^"\\']*\\.png(\\?[^"\\']*)?/i',
    $cover_remote . '?v=' . (int) $p['cache_bust'],
    $content
);
$now_local = current_time('mysql');
$now_gmt = current_time('mysql', 1);
wp_update_post([
    'ID' => $post_id,
    'post_content' => $content,
    'post_modified' => $now_local,
    'post_modified_gmt' => $now_gmt,
]);
$upload_dir = wp_upload_dir();
$cover_path = $upload_dir['basedir'] . '/2026/08/' . $cover_remote;
if (is_file($cover_path)) {{
    require_once ABSPATH . 'wp-admin/includes/image.php';
    $filetype = wp_check_filetype($cover_remote, null);
    $attachment = [
        'post_mime_type' => $filetype['type'] ?: 'image/png',
        'post_title' => sanitize_file_name($cover_remote),
        'post_content' => '',
        'post_status' => 'inherit',
    ];
    $attach_id = wp_insert_attachment($attachment, $cover_path, $post_id);
    if ($attach_id && !is_wp_error($attach_id)) {{
        $meta = wp_generate_attachment_metadata($attach_id, $cover_path);
        wp_update_attachment_metadata($attach_id, $meta);
        set_post_thumbnail($post_id, $attach_id);
        echo 'OK featured=' . $attach_id . PHP_EOL;
    }}
}}
echo 'OK post_updated=' . $post_id . PHP_EOL;
"""
    env = load_env()
    out = run_php_bootstrap(env, php, public, bootstrap_name="excalibur-passport-logo-ref-once.php")
    return out


def fetch_zen_enclosure(slug: str) -> str:
    public = resolve_public_base_from_env() or os.environ.get("PUBLIC_SITE_URL", "").rstrip("/")
    feed = urlopen(Request(f"{public}/feed/zen/", headers={"User-Agent": "Excalibur/1.0"}), timeout=90).read().decode(
        "utf-8", "replace"
    )
    for item in re.split(r"<item>", feed)[1:]:
        if slug not in item:
            continue
        m = re.search(r'<enclosure[^>]+url="([^"]+)"', item)
        if m:
            return m.group(1)
    return ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--upload-only", action="store_true")
    args = ap.parse_args()

    if not os.environ.get("GRSAI_API_KEY", "").strip() and not args.upload_only:
        print("❌ GRSAI API KEY MISSING", file=sys.stderr)
        return 1

    ensure_logo_asset()
    spec = spec_with_logo_ref_names(SLUG)
    adir = article_dir(spec)

    if not args.upload_only:
        bootstrap(spec)
        pipeline(adir)

    urls = upload_logo_ref_files(spec, adir)
    posts = wp_get(f"/wp-json/wp/v2/posts?slug={SLUG}")
    post_id = int(posts[0]["id"])
    php_out = update_wp_post(spec, urls, post_id)
    print(php_out, flush=True)

    enclosure = fetch_zen_enclosure(SLUG)
    report = {
        "slug": SLUG,
        "version_tag": VERSION_TAG,
        "cover_url": urls.get("cover"),
        "dzen_thumb_url": urls.get("dzen"),
        "zen_enclosure": enclosure,
        "post_id": post_id,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    out_path = ROOT / "memory/blog/live-passport-logo-ref-report.json"
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
