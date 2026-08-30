#!/usr/bin/env python3
"""Bump live WP posts for Yandex Dzen RSS: refresh media refs + post_modified."""

from __future__ import annotations

import argparse
import base64
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))

from excalibur_blog_live_cover_regen_aug22 import (  # noqa: E402
    AUG22_REGEN_SLUGS,
    build_spec_from_wp,
)
from excalibur_blog_site_base import resolve_public_base_from_env  # noqa: E402
from excalibur_blog_wp_publish import (  # noqa: E402
    delete_bootstrap_sftp,
    load_env,
    project_root,
    upload_bootstrap_sftp,
)

YEKT = ZoneInfo("Asia/Yekaterinburg")
ROOT = project_root()
REPORT_PATH = ROOT / "memory/blog/live-dzen-bump-report.json"


def run_php_bootstrap(env: dict[str, str], php: str, public_base: str, *, bootstrap_name: str) -> str:
    """SFTP upload + curl trigger (no WebFetch fallback wait)."""
    runtime_env = dict(env)
    configured_root = (runtime_env.get("FTP_ROOT") or runtime_env.get("SSH_ROOT") or "").strip()
    if configured_root:
        runtime_env["SSH_ROOT"] = configured_root
        runtime_env["FTP_ROOT"] = configured_root
    if not (runtime_env.get("SSH_HOST") or "").strip():
        runtime_env["SSH_HOST"] = (runtime_env.get("FTP_HOST") or "188.225.40.162").strip()
    if not (runtime_env.get("SSH_PORT") or "").strip():
        runtime_env["SSH_PORT"] = "22"

    uploaded_path = upload_bootstrap_sftp(runtime_env, bootstrap_name, php.encode("utf-8"))
    url = public_base.rstrip("/") + "/" + bootstrap_name
    try:
        proc = subprocess.run(
            ["curl", "-sS", "-m", "180", url],
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError(f"curl bootstrap failed rc={proc.returncode}: {proc.stderr}")
        return proc.stdout
    finally:
        try:
            delete_bootstrap_sftp(runtime_env, bootstrap_name, uploaded_path)
        except Exception:
            pass


def build_touch_modified_bootstrap(slugs: list[str]) -> str:
    encoded = base64.b64encode(json.dumps({"slugs": slugs}, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
$p = json_decode(base64_decode('{encoded}'), true);
if (!is_array($p) || empty($p['slugs'])) {{
    echo 'ERR dzen_touch: empty slugs' . PHP_EOL;
    exit(1);
}}
$now_local = current_time('mysql');
$now_gmt = current_time('mysql', true);
foreach ($p['slugs'] as $slug) {{
    $slug = sanitize_title((string) $slug);
    if ($slug === '') {{
        continue;
    }}
    $posts = get_posts([
        'name' => $slug,
        'post_type' => 'post',
        'post_status' => 'publish',
        'numberposts' => 1,
    ]);
    if (!$posts) {{
        echo 'ERR dzen_touch: missing slug=' . $slug . PHP_EOL;
        continue;
    }}
    wp_update_post([
        'ID' => (int) $posts[0]->ID,
        'post_modified' => $now_local,
        'post_modified_gmt' => $now_gmt,
    ]);
    echo 'OK dzen_touch=' . $slug . PHP_EOL;
}}
echo 'OK dzen_touch_done' . PHP_EOL;
"""


def build_bump_bootstrap(items: list[dict[str, Any]], cache_bust: int) -> str:
    payload = {"items": items, "cache_bust": cache_bust}
    encoded = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
$p = json_decode(base64_decode('{encoded}'), true);
if (!is_array($p) || empty($p['items'])) {{
    echo 'ERR dzen_bump: empty items' . PHP_EOL;
    exit(1);
}}
$cache_bust = (int) ($p['cache_bust'] ?? time());
$find_attachment = static function (string $basename): int {{
    $basename = trim($basename);
    if ($basename === '') {{
        return 0;
    }}
    $attachments = get_posts([
        'post_type' => 'attachment',
        'posts_per_page' => 10,
        'post_status' => 'inherit',
        'meta_query' => [
            [
                'key' => '_wp_attached_file',
                'value' => $basename,
                'compare' => 'LIKE',
            ],
        ],
    ]);
    if ($attachments) {{
        return (int) $attachments[0]->ID;
    }}
    global $wpdb;
    $like = '%' . $wpdb->esc_like($basename);
    $id = $wpdb->get_var($wpdb->prepare(
        "SELECT ID FROM {{$wpdb->posts}} WHERE post_type='attachment' AND guid LIKE %s ORDER BY ID DESC LIMIT 1",
        $like
    ));
    return (int) $id;
}};
foreach ($p['items'] as $item) {{
    $slug = sanitize_title((string) ($item['slug'] ?? ''));
    if ($slug === '') {{
        echo 'ERR dzen_bump: bad slug' . PHP_EOL;
        continue;
    }}
    $posts = get_posts([
        'name' => $slug,
        'post_type' => 'post',
        'post_status' => 'publish',
        'numberposts' => 1,
    ]);
    if (!$posts) {{
        echo 'ERR dzen_bump: missing post slug=' . $slug . PHP_EOL;
        continue;
    }}
    $post = $posts[0];
    $post_id = (int) $post->ID;
    $content = (string) $post->post_content;
    $cover_remote = (string) ($item['cover_remote'] ?? '');
    $inline_remote = (string) ($item['inline_remote'] ?? '');
    $inline_count = (int) ($item['inline_count'] ?? 7);
    if ($inline_remote !== '' && $inline_count > 0) {{
        for ($n = 1; $n <= $inline_count; $n++) {{
            $remote = str_replace('{{{{n:02d}}}}', sprintf('%02d', $n), $inline_remote);
            $pattern = preg_quote($remote, '/');
            $content = preg_replace(
                '/(' . $pattern . ')(\\?[^"\\']*)?/',
                '$1?v=' . $cache_bust,
                $content
            );
        }}
    }}
    if ($cover_remote !== '') {{
        $pattern = preg_quote($cover_remote, '/');
        $content = preg_replace(
            '/(' . $pattern . ')(\\?[^"\\']*)?/',
            '$1?v=' . $cache_bust,
            $content
        );
    }}
    $now_local = current_time('mysql');
    $now_gmt = current_time('mysql', 1);
    wp_update_post([
        'ID' => $post_id,
        'post_content' => wp_slash($content),
        'post_modified' => $now_local,
        'post_modified_gmt' => $now_gmt,
    ]);
    $cover_att = $cover_remote !== '' ? $find_attachment($cover_remote) : 0;
    if ($cover_att > 0) {{
        set_post_thumbnail($post_id, $cover_att);
        echo 'OK dzen_thumb=' . $cover_att . ' slug=' . $slug . PHP_EOL;
    }} else {{
        echo 'WARN dzen_thumb_missing slug=' . $slug . PHP_EOL;
    }}
    $result = [
        'post_id' => $post_id,
        'slug' => $slug,
        'modified_gmt' => $now_gmt,
        'cover_remote' => $cover_remote,
        'cover_attachment_id' => $cover_att,
    ];
    echo 'OK dzen_bump=' . base64_encode(json_encode($result, JSON_UNESCAPED_UNICODE)) . PHP_EOL;
}}
echo 'OK dzen_bump_done' . PHP_EOL;
"""


def parse_bump_lines(output: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in output.splitlines():
        if not line.startswith("OK dzen_bump="):
            continue
        encoded = line.split("=", 1)[1].strip()
        rows.append(json.loads(base64.b64decode(encoded).decode("utf-8")))
    return rows


def wp_modified_gmt(slug: str, public_base: str) -> str:
    url = f"{public_base.rstrip('/')}/wp-json/wp/v2/posts?slug={slug}"
    req = Request(url, headers={"User-Agent": "ExcaliburBlog/1.0"})
    with urlopen(req, timeout=90) as resp:
        posts = json.loads(resp.read().decode("utf-8"))
    if not posts:
        return ""
    return str(posts[0].get("modified_gmt") or "")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", action="append", default=[], help="slug(s) to bump (repeatable)")
    ap.add_argument("--slugs-file", help="newline-separated slugs file")
    ap.add_argument("--touch-modified-only", action="store_true", help="Only bump post_modified (no cover/media refresh)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    env = load_env(ROOT)
    public_base = resolve_public_base_from_env() or (env.get("PUBLIC_SITE_URL") or "").strip()
    if not public_base:
        print("BLOCKER: PUBLIC_SITE_URL missing", file=sys.stderr)
        return 1

    slugs: list[str] = [s.strip() for s in args.slug if s.strip()]
    if args.slugs_file:
        slugs.extend(
            line.strip()
            for line in Path(args.slugs_file).read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        )
    if not slugs:
        slugs = list(AUG22_REGEN_SLUGS)
    slugs = sorted(set(slugs))

    if args.touch_modified_only:
        if args.dry_run:
            print(json.dumps({"slugs": slugs, "touch_modified_only": True}, indent=2))
            return 0
        php = build_touch_modified_bootstrap(slugs)
        out = run_php_bootstrap(env, php, public_base, bootstrap_name="excalibur-blog-dzen-touch-once.php")
        if "OK dzen_touch_done" not in out:
            print("FAIL dzen touch bootstrap", file=sys.stderr)
            print(out)
            return 1
        print(out)
        return 0

    items: list[dict[str, Any]] = []
    before: dict[str, str] = {}

    for slug in slugs:
        spec = build_spec_from_wp(slug)
        before[slug] = wp_modified_gmt(slug, public_base)
        items.append(
            {
                "slug": slug,
                "cover_remote": spec["cover_remote"],
                "inline_remote": spec["inline_remote"],
                "inline_count": 7,
            }
        )

    cache_bust = int(datetime.now(timezone.utc).timestamp())
    php = build_bump_bootstrap(items, cache_bust)

    if args.dry_run:
        print(json.dumps({"slugs": slugs, "before_modified_gmt": before, "cache_bust": cache_bust}, indent=2))
        return 0

    out = run_php_bootstrap(
        env,
        php,
        public_base,
        bootstrap_name="excalibur-blog-dzen-bump-once.php",
    )
    if "OK dzen_bump_done" not in out:
        print("FAIL dzen bump bootstrap", file=sys.stderr)
        print(out)
        return 1

    bumped = parse_bump_lines(out)
    after: dict[str, str] = {}
    for slug in slugs:
        after[slug] = wp_modified_gmt(slug, public_base)

    report = {
        "bumped_at_yekt": datetime.now(YEKT).isoformat(),
        "cache_bust": cache_bust,
        "slugs": slugs,
        "before_modified_gmt": before,
        "after_modified_gmt": after,
        "bootstrap_rows": bumped,
        "permalink": {slug: f"/blog/{slug}/" for slug in slugs},
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
