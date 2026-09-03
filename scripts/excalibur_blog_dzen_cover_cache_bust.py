#!/usr/bin/env python3
"""Hard Dzen cover cache-bust: NEW filenames + WP attachment + /feed/zen/ enclosure swap.

Дзен CDN кэширует enclosure по URL. Перезапись того же файла не помогает —
нужен новый путь (version suffix), напр. `{slug}-cover-dzen-v3.png` +
`{slug}-cover-dzen-v3-1024x576.png`.

См. shared/dzen-cover-cache-bust.md
"""

from __future__ import annotations

import argparse
import base64
import json
import re
import sys
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_live_plate_remove_relogo import fix_image  # noqa: E402
from excalibur_blog_wp_publish import (  # noqa: E402
    load_env,
    project_root,
    publish_via_sftp,
    sftp_remote_path,
    sftp_root_candidates,
    _ssh_creds,
    is_missing_remote_path_error,
)

LOGO = ROOT / "memory/cover/assets/brand/logo-dobry-dom.png"
UPLOAD_SUBDIR = "2026/08"
DZEN_SIZE = (1024, 576)
DEFAULT_VERSION_SUFFIX = "dzen-v3"

ARTICLES: list[dict[str, str]] = [
    {
        "slug": "dogovor-arendy-pravila-prozhivaniya-posutochno",
        "old_cover_remote": "dogovor-arendy-pravila-prozhivaniya-posutochno-cover-1.png",
    },
    {
        "slug": "otmena-bronirovaniya-posutochno-vozvrat-predoplaty",
        "old_cover_remote": "otmena-bronirovaniya-posutochno-vozvrat-predoplaty-cover.png",
    },
    {
        "slug": "pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti",
        "old_cover_remote": "pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti-cover.png",
    },
    {
        "slug": "zabroniroval-posutochno-vyyasnilos-kvartira-v-subarende",
        "old_cover_remote": "zabroniroval-posutochno-vyyasnilos-kvartira-v-subarende-cover-2.png",
    },
]


def download_bytes(url: str) -> bytes:
    with urlopen(url, timeout=120) as resp:
        return resp.read()


def make_dzen_thumb(data: bytes, size: tuple[int, int] = DZEN_SIZE) -> bytes:
    from PIL import Image

    img = Image.open(BytesIO(data)).convert("RGB")
    target_w, target_h = size
    target_ratio = target_w / target_h
    w, h = img.size
    current_ratio = w / h
    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        box = (left, 0, left + new_w, h)
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        box = (0, top, w, top + new_h)
    cropped = img.crop(box).resize(size, Image.Resampling.LANCZOS)
    out = BytesIO()
    cropped.save(out, format="PNG", optimize=True)
    return out.getvalue()


def new_filenames(slug: str, version_suffix: str) -> tuple[str, str]:
    stem = f"{slug}-cover-{version_suffix}"
    return f"{stem}.png", f"{stem}-1024x576.png"


def prepare_cover(source_bytes: bytes, *, skip_fix: bool = False) -> tuple[bytes, dict[str, Any]]:
    if skip_fix:
        return source_bytes, {"skipped_fix": True}
    if not LOGO.is_file():
        raise RuntimeError(f"logo missing: {LOGO}")
    fixed, verify = fix_image(
        source_bytes,
        add_phone=False,
        paste_logo=True,
        strict=False,
    )
    return fixed, verify


def upload_sftp_files(
    env: dict[str, str],
    files: list[tuple[str, bytes]],
    *,
    public_base: str,
    upload_subdir: str,
) -> dict[str, str]:
    import paramiko

    host, port, user, password = _ssh_creds(env)
    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    urls: dict[str, str] = {}
    remote_dir = f"wp-content/uploads/{upload_subdir}"
    try:
        for remote_name, data in files:
            remote_path = f"{remote_dir}/{remote_name}"
            uploaded = False
            for root_candidate in sftp_root_candidates(env):
                full = sftp_remote_path(env, remote_path, root_candidate)
                try:
                    with sftp.open(full, "wb") as handle:
                        handle.write(data)
                    print(f"SFTP upload OK: {full} ({len(data)} bytes)")
                    uploaded = True
                    break
                except OSError as exc:
                    if is_missing_remote_path_error(exc):
                        continue
                    raise
            if not uploaded:
                raise RuntimeError(f"SFTP upload failed for {remote_path}")
            urls[remote_name] = f"{public_base.rstrip('/')}/{remote_dir}/{remote_name}"
    finally:
        sftp.close()
        transport.close()
    return urls


def build_php(payload: dict[str, Any]) -> str:
    b64 = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/image.php';

$p = json_decode(base64_decode('{b64}'), true);
$slug = (string) ($p['slug'] ?? '');
$subdir = (string) ($p['upload_subdir'] ?? '2026/08');
$full_fn = (string) ($p['full_filename'] ?? '');
$dzen_fn = (string) ($p['dzen_filename'] ?? '');
$old_fragments = $p['old_url_fragments'] ?? [];

$post = get_page_by_path($slug, OBJECT, 'post');
if (!$post instanceof WP_Post) {{
    echo 'ERR post_not_found slug=' . $slug . PHP_EOL;
    exit(1);
}}
$post_id = (int) $post->ID;
$guid_before = (string) get_post_field('guid', $post_id);

$upload = wp_upload_dir();
$full_path = $upload['basedir'] . '/' . $subdir . '/' . $full_fn;
$dzen_path = $upload['basedir'] . '/' . $subdir . '/' . $dzen_fn;
if (!is_file($full_path) || !is_file($dzen_path)) {{
    echo 'ERR missing_uploaded_file full=' . (int) is_file($full_path) . ' dzen=' . (int) is_file($dzen_path) . PHP_EOL;
    exit(1);
}}

$attachment = [
    'post_mime_type' => 'image/png',
    'post_title' => sanitize_file_name(preg_replace('/\\.png$/i', '', $full_fn)),
    'post_content' => '',
    'post_status' => 'inherit',
];
$att_id = (int) wp_insert_attachment($attachment, $full_path, $post_id);
if ($att_id <= 0) {{
    echo 'ERR attachment_insert_failed' . PHP_EOL;
    exit(1);
}}

$size = @getimagesize($full_path);
$full_w = is_array($size) ? (int) ($size[0] ?? 0) : 0;
$full_h = is_array($size) ? (int) ($size[1] ?? 0) : 0;
$dzen_size = @getimagesize($dzen_path);
$dzen_w = is_array($dzen_size) ? (int) ($dzen_size[0] ?? 1024) : 1024;
$dzen_h = is_array($dzen_size) ? (int) ($dzen_size[1] ?? 576) : 576;

$size_entry = [
    'file' => $dzen_fn,
    'width' => $dzen_w,
    'height' => $dzen_h,
    'mime-type' => 'image/png',
];
$meta = [
    'width' => $full_w,
    'height' => $full_h,
    'file' => $subdir . '/' . $full_fn,
    'sizes' => [
        'medium_large' => $size_entry,
        'large' => $size_entry,
        'post-thumbnail' => $size_entry,
    ],
];
wp_update_attachment_metadata($att_id, $meta);
set_post_thumbnail($post_id, $att_id);

$full_url = $upload['baseurl'] . '/' . $subdir . '/' . $full_fn;
$dzen_url = $upload['baseurl'] . '/' . $subdir . '/' . $dzen_fn;

$content = (string) get_post_field('post_content', $post_id);
$updated = $content;
foreach ($old_fragments as $frag) {{
    $frag = (string) $frag;
    if ($frag === '') {{
        continue;
    }}
    $updated = preg_replace(
        '#https?://[^"\\'\\s>]+' . preg_quote($frag, '#') . '(?:-1024x576|-\\d+x\\d+)?\\.png#i',
        $full_url,
        $updated
    ) ?? $updated;
}}
if ($updated !== $content) {{
    wp_update_post([
        'ID' => $post_id,
        'post_content' => wp_slash($updated),
    ]);
    echo 'OK post_content_cover_swapped=1' . PHP_EOL;
}} else {{
    echo 'WARN post_content_cover_swap=0' . PHP_EOL;
}}

$og_image_keys = [
    '_yoast_wpseo_opengraph-image',
    'rank_math_facebook_image',
    '_og_image',
    'og_image',
];
$og_id_keys = [
    '_yoast_wpseo_opengraph-image-id',
    'rank_math_facebook_image_id',
];
foreach ($og_image_keys as $key) {{
    $val = get_post_meta($post_id, $key, true);
    if ($val !== '' && $val !== null) {{
        update_post_meta($post_id, $key, $full_url);
        echo 'OK og_meta=' . $key . PHP_EOL;
    }}
}}
foreach ($og_id_keys as $key) {{
    $val = get_post_meta($post_id, $key, true);
    if ($val !== '' && $val !== null) {{
        update_post_meta($post_id, $key, (string) $att_id);
        echo 'OK og_meta=' . $key . PHP_EOL;
    }}
}}

$now_gmt = gmdate('Y-m-d H:i:s');
$now_local = current_time('mysql');
wp_update_post([
    'ID' => $post_id,
    'post_modified' => $now_local,
    'post_modified_gmt' => $now_gmt,
]);

$guid_after = (string) get_post_field('guid', $post_id);
echo 'OK post=' . $post_id . ' slug=' . $slug . PHP_EOL;
echo 'OK guid_unchanged=' . ($guid_before === $guid_after ? '1' : '0') . PHP_EOL;
echo 'OK featured_image=' . $att_id . PHP_EOL;
echo 'OK full_url=' . $full_url . PHP_EOL;
echo 'OK dzen_url=' . $dzen_url . PHP_EOL;
echo 'OK post_modified_gmt=' . get_post_field('post_modified_gmt', $post_id) . PHP_EOL;
"""


def parse_cover_from_enclosure_url(url: str) -> tuple[str, str]:
    """Return (upload_subdir, full_cover_filename) from a /feed/zen/ enclosure URL."""
    if not url:
        raise ValueError("empty enclosure url")
    m = re.search(
        r"/wp-content/uploads/(\d{4}/\d{2})/([^/\"?]+?)(?:-\d+x\d+)?\.png",
        url,
        re.IGNORECASE,
    )
    if not m:
        raise ValueError(f"cannot parse upload path from enclosure url: {url}")
    subdir, filename = m.group(1), m.group(2)
    # Enclosure is usually the -1024x576 intermediate; strip size suffix for full cover name.
    filename = re.sub(r"-\d+x\d+$", "", filename, flags=re.IGNORECASE)
    if not filename.lower().endswith(".png"):
        filename = f"{filename}.png"
    return subdir, filename


def resolve_article_spec(
    slug: str,
    *,
    public_base: str,
    upload_subdir: str = "",
    old_cover_remote: str = "",
) -> dict[str, str]:
    """Build cache-bust spec from ARTICLES table or live enclosure / CLI overrides."""
    for entry in ARTICLES:
        if entry["slug"] == slug:
            spec = dict(entry)
            spec.setdefault("upload_subdir", UPLOAD_SUBDIR)
            if upload_subdir:
                spec["upload_subdir"] = upload_subdir
            if old_cover_remote:
                spec["old_cover_remote"] = old_cover_remote
            return spec

    subdir = upload_subdir.strip()
    remote = old_cover_remote.strip()
    if not remote:
        enclosure = fetch_zen_enclosure(public_base, slug)
        if not enclosure:
            raise RuntimeError(f"no zen enclosure for slug={slug}; pass --old-cover-remote")
        subdir, remote = parse_cover_from_enclosure_url(enclosure)
    elif not subdir:
        raise RuntimeError("--upload-subdir required when --old-cover-remote is set without ARTICLES entry")
    return {"slug": slug, "upload_subdir": subdir, "old_cover_remote": remote}


def fetch_zen_enclosure(public_base: str, slug: str) -> str:
    feed = download_bytes(f"{public_base.rstrip('/')}/feed/zen/").decode("utf-8", "replace")
    for item in re.split(r"<item>", feed)[1:]:
        if slug not in item:
            continue
        m = re.search(r'<enclosure[^>]+url="([^"]+)"', item)
        return m.group(1) if m else ""
    return ""


def process_article(
    spec: dict[str, str],
    *,
    env: dict[str, str],
    public_base: str,
    version_suffix: str,
    work_dir: Path,
    skip_fix: bool,
    dry_run: bool,
) -> dict[str, Any]:
    slug = spec["slug"]
    upload_subdir = spec.get("upload_subdir") or UPLOAD_SUBDIR
    old_remote = spec["old_cover_remote"]
    full_fn, dzen_fn = new_filenames(slug, version_suffix)
    old_url = f"{public_base.rstrip('/')}/wp-content/uploads/{upload_subdir}/{old_remote}"
    old_enclosure = fetch_zen_enclosure(public_base, slug)

    print(f"\n=== {slug} ===", flush=True)
    print(f"old enclosure: {old_enclosure}", flush=True)

    source = download_bytes(old_url)
    full_bytes, verify = prepare_cover(source, skip_fix=skip_fix)
    dzen_bytes = make_dzen_thumb(full_bytes)

    article_work = work_dir / slug
    article_work.mkdir(parents=True, exist_ok=True)
    (article_work / full_fn).write_bytes(full_bytes)
    (article_work / dzen_fn).write_bytes(dzen_bytes)

    result: dict[str, Any] = {
        "slug": slug,
        "old_cover_url": old_url,
        "old_enclosure_url": old_enclosure,
        "new_full_filename": full_fn,
        "new_dzen_filename": dzen_fn,
        "new_full_bytes": len(full_bytes),
        "new_dzen_bytes": len(dzen_bytes),
        "fix_verify": verify,
        "guid_must_stay": True,
    }

    if dry_run:
        result["dry_run"] = True
        return result

    urls = upload_sftp_files(
        env,
        [(full_fn, full_bytes), (dzen_fn, dzen_bytes)],
        public_base=public_base,
        upload_subdir=upload_subdir,
    )
    result["uploaded_urls"] = urls

    old_fragments = [
        old_remote,
        re.sub(r"\.png$", "", old_remote),
        slug + "-cover",
        slug + "-cover-1",
        slug + "-cover-2",
    ]
    payload = {
        "slug": slug,
        "upload_subdir": upload_subdir,
        "full_filename": full_fn,
        "dzen_filename": dzen_fn,
        "old_url_fragments": sorted(set(old_fragments)),
    }
    runtime_env = dict(env)
    runtime_env["FTP_TRANSPORT"] = "sftp"
    php_out = publish_via_sftp(
        runtime_env,
        build_php(payload),
        public_base,
        bootstrap_name="excalibur-dzen-cover-cache-bust-once.php",
    )
    result["php_output"] = php_out
    if "ERR " in php_out or "OK post=" not in php_out:
        raise RuntimeError(f"WP bootstrap failed for {slug}:\n{php_out}")

    new_enclosure = fetch_zen_enclosure(public_base, slug)
    result["new_enclosure_url"] = new_enclosure
    result["enclosure_changed"] = bool(new_enclosure and new_enclosure != old_enclosure)
    if not result["enclosure_changed"]:
        raise RuntimeError(
            f"enclosure URL did not change for {slug}\nold={old_enclosure}\nnew={new_enclosure}"
        )
    if dzen_fn not in new_enclosure:
        raise RuntimeError(f"new enclosure missing {dzen_fn}: {new_enclosure}")

    return result


def main() -> int:
    ap = argparse.ArgumentParser(description="Hard Dzen cover cache-bust (new filenames)")
    ap.add_argument("--slug", help="single slug (auto-detect cover path from /feed/zen/ if not in ARTICLES)")
    ap.add_argument("--upload-subdir", default="", help="YYYY/MM under wp-content/uploads (optional with --slug)")
    ap.add_argument("--old-cover-remote", default="", help="existing full cover filename on host (optional)")
    ap.add_argument("--version-suffix", default=DEFAULT_VERSION_SUFFIX)
    ap.add_argument("--skip-fix", action="store_true", help="skip pad-clear + logo composite")
    ap.add_argument("--dry-run", action="store_true", help="prepare files only, no upload/WP")
    ap.add_argument("--verify-only", action="store_true", help="print current zen enclosures")
    args = ap.parse_args()

    env = load_env(project_root())
    public_base = (env.get("PUBLIC_SITE_URL") or env.get("WP_HOME") or "").rstrip("/")
    if not public_base:
        print("PUBLIC_SITE_URL missing", file=sys.stderr)
        return 1

    if args.slug:
        try:
            specs = [
                resolve_article_spec(
                    args.slug,
                    public_base=public_base,
                    upload_subdir=args.upload_subdir,
                    old_cover_remote=args.old_cover_remote,
                )
            ]
        except (RuntimeError, ValueError) as exc:
            print(str(exc), file=sys.stderr)
            return 1
    else:
        specs = list(ARTICLES)
    if not specs:
        print("no matching articles", file=sys.stderr)
        return 1

    if args.verify_only:
        for spec in specs:
            enc = fetch_zen_enclosure(public_base, spec["slug"])
            print(f"{spec['slug']}: {enc}")
        return 0

    work_dir = ROOT / "memory/blog/dzen-cache-bust-work"
    work_dir.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "run_at": datetime.now(timezone.utc).isoformat(),
        "version_suffix": args.version_suffix,
        "articles": {},
    }

    for spec in specs:
        entry = process_article(
            spec,
            env=env,
            public_base=public_base,
            version_suffix=args.version_suffix,
            work_dir=work_dir,
            skip_fix=bool(args.skip_fix),
            dry_run=bool(args.dry_run),
        )
        report["articles"][spec["slug"]] = entry
        print(json.dumps(entry, ensure_ascii=False, indent=2))

    out_path = ROOT / "memory/blog/dzen-cover-cache-bust-report.json"
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nreport: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
