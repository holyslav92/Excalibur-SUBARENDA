#!/usr/bin/env python3
"""Live regen: 8 images per article — Grsai logo reference + CDN filenames + WP/Dzen."""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from excalibur_blog_live_cover_regen_aug22 import (  # noqa: E402
    META_BY_SLUG,
    ROOT,
    article_dir,
    bootstrap,
    build_spec_from_wp,
    ensure_logo_asset,
    pipeline,
    wp_get,
)
from excalibur_blog_site_base import resolve_public_base_from_env  # noqa: E402
from excalibur_blog_wp_publish import (  # noqa: E402
    delete_bootstrap_sftp,
    is_missing_remote_path_error,
    load_env,
    sftp_remote_path,
    sftp_root_candidates,
    upload_bootstrap_sftp,
    _ssh_creds,
)

DEFAULT_SLUGS: tuple[str, ...] = (
    "poprosili-foto-pasporta-pri-zaselenii-posutochno-chto-zakonno",
    "dogovor-arendy-pravila-prozhivaniya-posutochno",
)
VERSION_TAG = "logo-ref-v2"
DZEN_SIZE = (1024, 576)
REPORT_PATH = ROOT / "memory/blog/live-logo-ref-regen-report.json"

SLUG_META: dict[str, dict[str, Any]] = {
    "poprosili-foto-pasporta-pri-zaselenii-posutochno-chto-zakonno": {
        "topic_id": "LIVE-passport-photo",
        "hook": "Просят фото паспорта при заселении",
        "highlight": "паспорта",
        "sticky": "законно?",
        "wordstat": ["фото паспорта", "Тюмень", "заселение посуточно"],
        "cover_emotion": "шок: хозяин требует фото паспорта в чат до заселения",
        "cover_scene": "Phone chat passport demand vs blurred ID; bold hook; daylight; logo ref top-right no plate",
        "motif_composition": "passport photo request chat + blurred document comparison poster",
        "motif_meme": "cat magnifying glass sticker bottom-left ≤10%",
        "motif_props": "phone chat, blurred passport, torn sticky, gold tape",
        "motif_joke": "cat inspects suspicious passport request",
    },
}


def spec_with_logo_ref_names(slug: str, version_tag: str = VERSION_TAG) -> dict[str, Any]:
    spec = build_spec_from_wp(slug)
    meta = dict(META_BY_SLUG.get(slug) or SLUG_META.get(slug) or {})
    spec.update(meta)
    spec["cover_remote"] = f"{slug}-cover-{version_tag}.png"
    spec["inline_remote"] = f"{slug}-inline-{{n:02d}}-{version_tag}.png"
    spec["version_tag"] = version_tag
    return spec


def make_dzen_thumb(cover_path: Path) -> bytes:
    from PIL import Image

    with Image.open(cover_path) as img:
        thumb = img.convert("RGBA").resize(DZEN_SIZE, Image.Resampling.LANCZOS)
        buf = BytesIO()
        thumb.save(buf, format="PNG", optimize=True)
        return buf.getvalue()


def upload_logo_ref_files(spec: dict, adir: Path) -> dict[str, str]:
    import paramiko

    env = load_env(ROOT)
    remote_dir = "wp-content/uploads/2026/08"
    public = resolve_public_base_from_env() or os.environ.get("PUBLIC_SITE_URL", "").rstrip("/")
    urls: dict[str, str] = {}
    cover_remote = spec["cover_remote"]
    version_tag = spec.get("version_tag") or VERSION_TAG
    dzen_remote = f"{spec['slug']}-cover-{version_tag}-1024x576.png"
    files: dict[str, bytes] = {}
    for n in range(1, 8):
        remote = spec["inline_remote"].format(n=n)
        files[remote] = (adir / "cover" / f"inline-{n:02d}.png").read_bytes()
    files[cover_remote] = (adir / "cover" / "cover.png").read_bytes()
    files[dzen_remote] = make_dzen_thumb(adir / "cover" / "cover.png")

    host, port, user, password = _ssh_creds(env)
    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    cache_bust = int(time.time())
    try:
        for remote_name, data in files.items():
            remote_path = f"{remote_dir}/{remote_name}"
            uploaded = False
            for root_candidate in sftp_root_candidates(env):
                full = sftp_remote_path(env, remote_path, root_candidate)
                try:
                    with sftp.open(full, "wb") as handle:
                        handle.write(data)
                    print(f"SFTP OK {full} ({len(data)} bytes)", flush=True)
                    uploaded = True
                    break
                except OSError as exc:
                    if is_missing_remote_path_error(exc):
                        continue
                    raise
            if not uploaded:
                raise RuntimeError(f"SFTP upload failed for {remote_path}")
            urls[remote_name] = f"{public}/{remote_dir}/{remote_name}?v={cache_bust}"
    finally:
        sftp.close()
        transport.close()

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
    proc = __import__("subprocess").run(
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
    slug = spec["slug"]
    version_tag = spec.get("version_tag") or VERSION_TAG
    dzen_remote = f"{spec['slug']}-cover-{version_tag}-1024x576.png"
    payload = {
        "post_id": post_id,
        "slug": slug,
        "cover_remote": spec["cover_remote"],
        "dzen_remote": dzen_remote,
        "inline_remote": spec["inline_remote"],
        "inline_count": 7,
        "cache_bust": int(time.time()),
    }
    encoded = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    slug_quoted = slug.replace("'", "\\'")
    php = f"""<?php
require __DIR__ . '/wp-load.php';
$p = json_decode(base64_decode('{encoded}'), true);
$post_id = (int) ($p['post_id'] ?? 0);
$post = get_post($post_id);
if (!$post) {{ echo 'ERR post not found' . PHP_EOL; exit(1); }}
$content = (string) $post->post_content;
$inline_remote = (string) ($p['inline_remote'] ?? '');
$slug_pat = preg_quote('{slug_quoted}', '/');
for ($n = 1; $n <= (int) ($p['inline_count'] ?? 7); $n++) {{
    $remote = str_replace('{{n:02d}}', sprintf('%02d', $n), $inline_remote);
    $content = preg_replace(
        '/' . $slug_pat . '[^"\\']*inline-' . sprintf('%02d', $n) . '[^"\\']*\\.png(\\?[^"\\']*)?/i',
        $remote . '?v=' . (int) $p['cache_bust'],
        $content
    );
}}
$cover_remote = (string) ($p['cover_remote'] ?? '');
$content = preg_replace(
    '/' . $slug_pat . '[^"\\']*cover[^"\\']*\\.png(\\?[^"\\']*)?/i',
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
$subdir = '2026/08';
$cover_path = $upload_dir['basedir'] . '/' . $subdir . '/' . $cover_remote;
$dzen_remote = (string) ($p['dzen_remote'] ?? '');
$dzen_path = $dzen_remote !== '' ? $upload_dir['basedir'] . '/' . $subdir . '/' . $dzen_remote : '';
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
        $size = @getimagesize($cover_path);
        $full_w = is_array($size) ? (int) ($size[0] ?? 0) : 0;
        $full_h = is_array($size) ? (int) ($size[1] ?? 0) : 0;
        $meta = [
            'width' => $full_w,
            'height' => $full_h,
            'file' => $subdir . '/' . $cover_remote,
            'sizes' => [],
        ];
        if ($dzen_remote !== '' && is_file($dzen_path)) {{
            $dzen_size = @getimagesize($dzen_path);
            $dzen_w = is_array($dzen_size) ? (int) ($dzen_size[0] ?? 1024) : 1024;
            $dzen_h = is_array($dzen_size) ? (int) ($dzen_size[1] ?? 576) : 576;
            $size_entry = [
                'file' => $dzen_remote,
                'width' => $dzen_w,
                'height' => $dzen_h,
                'mime-type' => 'image/png',
            ];
            $meta['sizes'] = [
                'medium_large' => $size_entry,
                'large' => $size_entry,
                'post-thumbnail' => $size_entry,
            ];
        }} else {{
            $meta = wp_generate_attachment_metadata($attach_id, $cover_path);
        }}
        wp_update_attachment_metadata($attach_id, $meta);
        set_post_thumbnail($post_id, $attach_id);
        echo 'OK featured=' . $attach_id . PHP_EOL;
        if ($dzen_remote !== '') {{
            echo 'OK dzen_remote=' . $dzen_remote . PHP_EOL;
        }}
    }}
}}
echo 'OK post_updated=' . $post_id . PHP_EOL;
"""
    env = load_env(ROOT)
    return run_php_bootstrap(env, php, public, bootstrap_name=f"excalibur-logo-ref-{slug[:24]}.php")


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


def process_slug(slug: str, *, upload_only: bool, version_tag: str) -> dict[str, Any]:
    print(f"\n=== {slug} ===", flush=True)
    spec = spec_with_logo_ref_names(slug, version_tag=version_tag)
    adir = article_dir(spec)
    if not upload_only:
        if adir.is_dir():
            import shutil

            shutil.rmtree(adir)
        bootstrap(spec)
        pipeline(adir)
    urls = upload_logo_ref_files(spec, adir)
    posts = wp_get(f"/wp-json/wp/v2/posts?slug={slug}")
    post_id = int(posts[0]["id"])
    php_out = update_wp_post(spec, urls, post_id)
    print(php_out, flush=True)
    enclosure = fetch_zen_enclosure(slug)
    row = {
        "slug": slug,
        "version_tag": version_tag,
        "cover_url": urls.get("cover"),
        "dzen_thumb_url": urls.get("dzen"),
        "zen_enclosure": enclosure,
        "post_id": post_id,
    }
    print(json.dumps(row, ensure_ascii=False, indent=2), flush=True)
    return row


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", action="append", help="process specific slug(s)")
    ap.add_argument("--upload-only", action="store_true")
    ap.add_argument("--version-tag", default=VERSION_TAG)
    args = ap.parse_args()

    if not os.environ.get("GRSAI_API_KEY", "").strip() and not args.upload_only:
        print("❌ GRSAI API KEY MISSING", file=sys.stderr)
        return 1

    ensure_logo_asset()
    slugs = tuple(args.slug) if args.slug else DEFAULT_SLUGS
    report_rows: list[dict[str, Any]] = []
    for slug in slugs:
        report_rows.append(process_slug(slug, upload_only=args.upload_only, version_tag=args.version_tag))

    report = {
        "version_tag": args.version_tag,
        "articles": report_rows,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
