#!/usr/bin/env python3
"""Fix live WP post cross-links via FTP bootstrap (href-only surgery)."""

from __future__ import annotations

import argparse
import base64
import json
import re
import subprocess
import sys
from datetime import datetime
from html import unescape
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from excalibur_blog_crosslink_qa_gate import anchor_matches_catalog_title, validate_article_crosslinks
from excalibur_blog_live_catalog import (
    catalog_path,
    fetch_listing_page,
    load_catalog,
    parse_listing_html,
    refresh_catalog,
    slug_from_blog_href,
)
from excalibur_blog_link_verify import check_url_with_connection_reset_retry
from excalibur_blog_site_base import (
    SITE_BASE_PLACEHOLDER,
    blog_path_for_slug,
    canonical_blog_xlink_href,
    expand_blog_xlinks_in_html,
    expand_site_base,
    is_root_relative_blog_href,
    normalize_public_base,
    resolve_public_base_from_env,
)
from excalibur_blog_wp_publish import load_env, project_root


def run_bootstrap(env: dict[str, str], php: str, public_base: str, *, bootstrap_name: str) -> str:
    """Upload bootstrap via SFTP and trigger with curl (avoid FTP PASV hangs + webfetch fallback)."""
    from excalibur_blog_wp_publish import delete_bootstrap_sftp, upload_bootstrap_sftp

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
            ["curl", "-sS", "-m", "120", url],
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


YEKT = ZoneInfo("Asia/Yekaterinburg")


def build_meta_bootstrap(slugs: list[str]) -> str:
    payload = {"slugs": slugs}
    encoded = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
$p = json_decode(base64_decode('{encoded}'), true);
if (!is_array($p) || empty($p['slugs'])) {{
    echo 'ERR xfix: empty slugs' . PHP_EOL;
    exit(1);
}}
foreach ($p['slugs'] as $slug) {{
    $slug = sanitize_title((string) $slug);
    if ($slug === '') {{
        echo 'ERR xfix: bad slug' . PHP_EOL;
        continue;
    }}
    $posts = get_posts([
        'name' => $slug,
        'post_type' => 'post',
        'post_status' => 'publish',
        'numberposts' => 1,
    ]);
    if (!$posts) {{
        echo 'ERR xfix: missing post slug=' . $slug . PHP_EOL;
        continue;
    }}
    $post = $posts[0];
    $payload = [
        'post_id' => (int) $post->ID,
        'slug' => $slug,
        'date' => (string) $post->post_date,
    ];
    echo 'OK xfix_meta=' . base64_encode(json_encode($payload, JSON_UNESCAPED_UNICODE)) . PHP_EOL;
}}
echo 'OK xfix_meta_done' . PHP_EOL;
"""


def build_fetch_bootstrap(slugs: list[str]) -> str:
    payload = {"slugs": slugs}
    encoded = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
$p = json_decode(base64_decode('{encoded}'), true);
if (!is_array($p) || empty($p['slugs'])) {{
    echo 'ERR xfix: empty slugs' . PHP_EOL;
    exit(1);
}}
foreach ($p['slugs'] as $slug) {{
    $slug = sanitize_title((string) $slug);
    if ($slug === '') {{
        echo 'ERR xfix: bad slug' . PHP_EOL;
        continue;
    }}
    $posts = get_posts([
        'name' => $slug,
        'post_type' => 'post',
        'post_status' => 'publish',
        'numberposts' => 1,
    ]);
    if (!$posts) {{
        echo 'ERR xfix: missing post slug=' . $slug . PHP_EOL;
        continue;
    }}
    $post = $posts[0];
    $payload = [
        'post_id' => (int) $post->ID,
        'slug' => $slug,
        'date' => (string) $post->post_date,
        'content_b64' => base64_encode((string) $post->post_content),
    ];
    echo 'OK xfix_fetch=' . base64_encode(json_encode($payload, JSON_UNESCAPED_UNICODE)) . PHP_EOL;
}}
echo 'OK xfix_fetch_done' . PHP_EOL;
"""


def build_update_bootstrap(updates: list[dict[str, Any]]) -> str:
    encoded = base64.b64encode(json.dumps({"updates": updates}, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
$p = json_decode(base64_decode('{encoded}'), true);
if (!is_array($p) || empty($p['updates'])) {{
    echo 'ERR xfix: empty updates' . PHP_EOL;
    exit(1);
}}
foreach ($p['updates'] as $u) {{
    $post_id = (int) ($u['post_id'] ?? 0);
    $content_b64 = (string) ($u['content_b64'] ?? '');
    if ($post_id <= 0 || $content_b64 === '') {{
        echo 'ERR xfix: bad update row' . PHP_EOL;
        continue;
    }}
    $content = base64_decode($content_b64, true);
    if (!is_string($content)) {{
        echo 'ERR xfix: decode post=' . $post_id . PHP_EOL;
        continue;
    }}
    wp_update_post([
        'ID' => $post_id,
        'post_content' => wp_slash($content),
    ]);
    echo 'OK xfix_updated=' . $post_id . PHP_EOL;
}}
echo 'OK xfix_update_done' . PHP_EOL;
"""


def parse_meta_lines(output: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in output.splitlines():
        if not line.startswith("OK xfix_meta="):
            continue
        encoded = line.split("=", 1)[1].strip()
        rows.append(json.loads(base64.b64decode(encoded).decode("utf-8")))
    return rows


def parse_fetch_lines(output: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in output.splitlines():
        if not line.startswith("OK xfix_fetch="):
            continue
        encoded = line.split("=", 1)[1].strip()
        raw = base64.b64decode(encoded).decode("utf-8")
        row = json.loads(raw)
        row["content"] = base64.b64decode(row["content_b64"]).decode("utf-8")
        rows.append(row)
    return rows


def normalize_blog_hrefs(content: str, slug_index: dict[str, Any]) -> tuple[str, list[dict[str, str]]]:
    changes: list[dict[str, str]] = []

    def repl(match: re.Match[str]) -> str:
        quote = match.group(1)
        path = match.group(2).strip()
        if not path.startswith("/") or path.startswith("/blog/"):
            return match.group(0)
        slug_match = re.match(r"^/([a-z0-9][a-z0-9-]+)/?$", path.rstrip("/") + "/")
        if not slug_match:
            return match.group(0)
        slug = slug_match.group(1)
        if slug not in slug_index:
            return match.group(0)
        new_href = blog_path_for_slug(slug)
        if new_href != path and not path.startswith(new_href.rstrip("/")):
            changes.append({"from": path, "to": new_href, "slug": slug})
            return f"href={quote}{new_href}{quote}"
        return match.group(0)

    updated = re.sub(r'href=(["\'])(/[^"\']+)\1', repl, content)
    return updated, changes


def absolute_blog_hrefs(content: str, site_base: str) -> tuple[str, list[dict[str, str]]]:
    """Rewrite root-relative /blog/… hrefs to absolute URLs (Dzen-safe)."""
    changes: list[dict[str, str]] = []
    base = normalize_public_base(site_base)
    if not base:
        return content, changes

    def repl(match: re.Match[str]) -> str:
        quote = match.group(1)
        href = match.group(2).strip()
        if href.startswith(SITE_BASE_PLACEHOLDER):
            expanded = expand_site_base(href, base)
            if expanded != href:
                changes.append({"from": href, "to": expanded, "action": "expand_site_base"})
                return f"href={quote}{expanded}{quote}"
            return match.group(0)
        if is_root_relative_blog_href(href):
            path = href if href.endswith("/") else f"{href}/"
            new_href = f"{base.rstrip('/')}{path}"
            changes.append({"from": href, "to": new_href, "action": "absolute_blog"})
            return f"href={quote}{new_href}{quote}"
        return match.group(0)

    updated = re.sub(r'href=(["\'])([^"\']+)\1', repl, content)
    return updated, changes


def absolute_blog_index_href(content: str, site_base: str) -> tuple[str, list[dict[str, str]]]:
    """«Вернуться назад»: href=\"/blog\" → absolute https://site/blog/."""
    changes: list[dict[str, str]] = []
    base = normalize_public_base(site_base)
    if not base:
        return content, changes
    pattern = re.compile(
        r'<a\b([^>]*?)href=(["\'])/blog\2([^>]*)>(.*?)</a>',
        re.I | re.S,
    )

    def repl(match: re.Match[str]) -> str:
        anchor = unescape(re.sub(r"\s+", " ", match.group(4))).strip()
        new_href = f"{base.rstrip('/')}/blog/"
        changes.append(
            {
                "action": "blog_index_absolute",
                "from": "/blog",
                "to": new_href,
                "anchor": anchor[:80],
            }
        )
        return (
            f"<a{match.group(1)}href={match.group(2)}{new_href}{match.group(2)}"
            f"{match.group(3)}>{match.group(4)}</a>"
        )

    updated = pattern.sub(repl, content)
    return updated, changes


def fix_mashed_cta_spacing(content: str) -> tuple[str, list[str]]:
    changes: list[str] = []
    replacements = [
        (r"MAXили", "MAX или"),
        (r"MAX\s*<a", "MAX <a"),
        (r"Telegram\s*<a", "Telegram <a"),
        (r"отдельно:скрытые", "отдельно: скрытые"),
        (r"отдельно:<a", "отдельно: <a"),
        (r"на\s*<a([^>]+)>добрыйдом-72\.рф", r"на <a\1>добрыйдом-72.рф"),
        (r"заселение:добрыйдом", "заселение: добрыйдом"),
        (r"на\s*<a([^>]+)>@Dobriy_dom_Tyumen", r"в Telegram <a\1>@Dobriy_dom_Tyumen"),
        (r"менеджер в Telegram\s*<a", "менеджер в Telegram <a"),
    ]
    out = content
    for pattern, repl in replacements:
        new_out, n = re.subn(pattern, repl, out, flags=re.I)
        if n:
            changes.append(f"{pattern} -> {repl} ({n}x)")
            out = new_out
    return out, changes


def restore_plain_crosslinks(content: str, *, catalog: dict[str, Any]) -> tuple[str, list[dict[str, str]]]:
    changes: list[dict[str, str]] = []
    restores = [
        {
            "plain": "Если бронируете с ценой «от» в объявлении",
            "linked": 'Если бронируете с <a href="/blog/czena-ot-v-reklame-pochemu-vsegda-nuzhno-utochnyat-realnuyu-stoimost/">ценой «от» в объявлении</a>',
            "slug": "czena-ot-v-reklame-pochemu-vsegda-nuzhno-utochnyat-realnuyu-stoimost",
        }
    ]
    out = content
    for row in restores:
        if row["slug"] not in (catalog.get("slug_index") or {}):
            continue
        if row["linked"] in out or row["plain"] not in out:
            continue
        out = out.replace(row["plain"], row["linked"], 1)
        changes.append({"action": "restore", "slug": row["slug"], "plain": row["plain"]})
    return out, changes


def unwrap_dead_blog_links(
    content: str,
    *,
    site_base: str,
    catalog: dict[str, Any],
    timeout: float = 8.0,
) -> tuple[str, list[dict[str, str]]]:
    """Unwrap <a> when /blog/{slug}/ is not in live catalog or returns non-200."""
    changes: list[dict[str, str]] = []
    slug_index = catalog.get("slug_index") or {}
    base = normalize_public_base(site_base)
    pattern = re.compile(
        r'<a\b([^>]*?)href=(["\'])(/blog/[^"\']+)\2([^>]*)>(.*?)</a>',
        re.I | re.S,
    )

    def repl(match: re.Match[str]) -> str:
        href = match.group(3).strip()
        anchor = unescape(re.sub(r"\s+", " ", match.group(5))).strip()
        slug = slug_from_blog_href(href)
        if not slug:
            return match.group(0)
        row = slug_index.get(slug)
        if not row:
            changes.append({"action": "unwrap_dead", "href": href, "slug": slug, "reason": "not_in_catalog"})
            return anchor
        return match.group(0)

    updated = pattern.sub(repl, content)
    return updated, changes


def unwrap_mismatched_blog_links(
    content: str,
    *,
    catalog: dict[str, Any],
) -> tuple[str, list[dict[str, str]]]:
    """Drop <a> when anchor intent does not match the live catalog title for slug."""
    changes: list[dict[str, str]] = []
    pattern = re.compile(
        r'<a\b([^>]*?)href=(["\'])(/blog/[^"\']+)\2([^>]*)>(.*?)</a>',
        re.I | re.S,
    )

    def repl(match: re.Match[str]) -> str:
        href = match.group(3)
        anchor = unescape(re.sub(r"\s+", " ", match.group(5))).strip()
        slug = slug_from_blog_href(href)
        if not slug:
            return match.group(0)
        row = (catalog.get("slug_index") or {}).get(slug)
        if not row:
            return match.group(0)
        if anchor_matches_catalog_title(anchor, str(row.get("title") or slug)):
            return match.group(0)
        changes.append(
            {
                "action": "unwrap",
                "href": href,
                "anchor": anchor[:120],
                "catalog_title": str(row.get("title") or ""),
            }
        )
        return anchor

    updated = pattern.sub(repl, content)
    return updated, changes


def verify_hrefs(content: str, site_base: str, *, timeout: float = 8.0) -> list[str]:
    errors: list[str] = []
    for match in re.finditer(r'href=(["\'])([^"\']+)\1', content):
        href = match.group(2)
        if is_root_relative_blog_href(href):
            errors.append(f"Dzen-unsafe relative blog href remains: {href}")
            continue
        slug = slug_from_blog_href(href)
        if not slug:
            continue
        url = href if href.startswith("http") else site_base.rstrip("/") + blog_path_for_slug(slug)
        result = check_url_with_connection_reset_retry(url, timeout, "ExcaliburBlogLiveXlinkFix/1.0")
        if not result.get("ok"):
            errors.append(f"{href} -> HTTP {result.get('status')} {result.get('error')}")
    return errors


def post_date_is_target(post_date: str, target: str) -> bool:
    try:
        dt = datetime.fromisoformat(post_date.replace(" ", "T"))
    except ValueError:
        return False
    local = dt.astimezone(YEKT).date().isoformat()
    return local == target


def chunk_list(items: list[str], size: int) -> list[list[str]]:
    if size <= 0:
        return [items]
    return [items[i : i + size] for i in range(0, len(items), size)]


def process_slug_batch(
    *,
    env: dict[str, str],
    public_base: str,
    slugs: list[str],
    catalog: dict[str, Any],
    slug_index: dict[str, Any],
    apply: bool,
    dry_run: bool,
    bootstrap_tag: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Fetch, fix, optionally update one slug batch. Returns (report_rows, updates)."""
    fetch_out = run_bootstrap(
        env,
        build_fetch_bootstrap(slugs),
        public_base,
        bootstrap_name=f"excalibur-blog-xfix-fetch-{bootstrap_tag}.php",
    )
    rows = parse_fetch_lines(fetch_out)
    if not rows:
        raise RuntimeError(f"FAIL: no posts fetched for batch {bootstrap_tag}: {fetch_out[:500]}")

    report_rows: list[dict[str, Any]] = []
    updates: list[dict[str, Any]] = []

    for row in rows:
        slug = str(row.get("slug") or "")
        content = str(row.get("content") or "")
        fixed, href_changes = normalize_blog_hrefs(content, slug_index)
        fixed, dead_unwrap = unwrap_dead_blog_links(fixed, site_base=public_base, catalog=catalog)
        fixed, abs_changes = absolute_blog_hrefs(fixed, public_base)
        fixed, blog_index_changes = absolute_blog_index_href(fixed, public_base)
        fixed, mashed_changes = fix_mashed_cta_spacing(fixed)
        fixed, unwrap_changes = unwrap_mismatched_blog_links(fixed, catalog=catalog)
        fixed, restore_changes = restore_plain_crosslinks(fixed, catalog=catalog)
        fixed, abs_final = absolute_blog_hrefs(fixed, public_base)
        abs_changes.extend(abs_final)
        validation = validate_article_crosslinks(
            fixed,
            catalog=catalog,
            site_base=public_base,
            tenant=json.loads((project_root() / "shared/tenant-config.json").read_text(encoding="utf-8")),
            timeout=8.0,
            skip_http=True,
        )
        href_errors: list[str] = []
        for match in re.finditer(r'href=(["\'])([^"\']+)\1', fixed):
            if is_root_relative_blog_href(match.group(2)):
                href_errors.append(f"Dzen-unsafe relative blog href remains: {match.group(2)}")
        entry = {
            "slug": slug,
            "post_id": row.get("post_id"),
            "href_changes": href_changes,
            "dead_unwrap_changes": dead_unwrap,
            "absolute_blog_changes": abs_changes,
            "blog_index_changes": blog_index_changes,
            "unwrap_changes": unwrap_changes,
            "restore_changes": restore_changes,
            "mashed_changes": mashed_changes,
            "validation_status": validation.get("status"),
            "validation_errors": validation.get("errors"),
            "href_http_errors": href_errors,
            "changed": fixed != content,
        }
        report_rows.append(entry)
        if fixed != content and apply and not dry_run:
            updates.append(
                {
                    "post_id": row.get("post_id"),
                    "content_b64": base64.b64encode(fixed.encode("utf-8")).decode("ascii"),
                }
            )

    if apply and not dry_run and updates:
        out = run_bootstrap(
            env,
            build_update_bootstrap(updates),
            public_base,
            bootstrap_name=f"excalibur-blog-xfix-update-{bootstrap_tag}.php",
        )
        if "OK xfix_update_done" not in out:
            raise RuntimeError(f"FAIL update bootstrap {bootstrap_tag}: {out[:500]}")

    return report_rows, updates


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--slug", action="append", default=[])
    ap.add_argument("--slugs-file", help="newline-separated slugs to fix")
    ap.add_argument("--exclude-slug", action="append", default=[], help="Skip slug(s), e.g. already-fixed B04")
    ap.add_argument("--from-catalog", action="store_true", help="All slugs from live-catalog.json")
    ap.add_argument("--batch-size", type=int, default=8, help="Slugs per fetch/update bootstrap batch")
    ap.add_argument("--date", default="", help="Asia/Yekaterinburg YYYY-MM-DD")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    root = project_root()
    env = load_env(root)
    public_base = normalize_public_base(
        env.get("PUBLIC_SITE_URL") or env.get("WP_SITE_URL") or resolve_public_base_from_env()
    )
    if not public_base:
        print("BLOCKER: PUBLIC_SITE_URL missing", file=sys.stderr)
        return 2

    catalog_path_file = catalog_path(root)
    if catalog_path_file.is_file():
        catalog = load_catalog(catalog_path_file)
    else:
        catalog = refresh_catalog(root)
    slug_index = catalog.get("slug_index") or {}

    audit_extras = (
        "beskontaktnoe-zaselenie-posutochno-tyumen",
        "perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem",
    )
    exclude = {s.strip() for s in args.exclude_slug if s.strip()}

    slugs = [s.strip() for s in args.slug if s.strip()]
    if args.slugs_file:
        slugs.extend(
            line.strip()
            for line in Path(args.slugs_file).read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith("#")
        )
    candidate_slugs = slugs[:]
    if args.from_catalog:
        candidate_slugs = sorted(str(s) for s in (slug_index.keys()) if str(s) not in exclude)
    elif not candidate_slugs:
        listing_slugs: list[str] = []
        for page in (1, 2, 3, 4, 5, 6, 7, 8):
            try:
                html = fetch_listing_page(public_base, page)
            except Exception:
                break
            for row in parse_listing_html(html):
                slug = str(row.get("slug") or "").strip()
                if slug and slug not in exclude:
                    listing_slugs.append(slug)
        candidate_slugs = sorted(set(listing_slugs + list(audit_extras)))

    candidate_slugs = [s for s in candidate_slugs if s not in exclude]

    if not candidate_slugs:
        print("Nothing to fix (no slugs).", file=sys.stderr)
        return 1

    if args.date and not slugs:
        meta_out = run_bootstrap(
            env,
            build_meta_bootstrap(candidate_slugs),
            public_base,
            bootstrap_name="excalibur-blog-xfix-meta-once.php",
        )
        dated = [
            str(row.get("slug") or "")
            for row in parse_meta_lines(meta_out)
            if post_date_is_target(str(row.get("date") or ""), args.date)
        ]
        slugs = sorted(set(dated + [s for s in audit_extras if s not in exclude]))
    else:
        slugs = candidate_slugs if not slugs else sorted(set(slugs))

    slugs = [s for s in slugs if s not in exclude]

    if not slugs:
        print(f"No posts for date {args.date}", file=sys.stderr)
        return 1

    report_rows: list[dict[str, Any]] = []
    all_updates: list[dict[str, Any]] = []
    batches = chunk_list(slugs, max(1, args.batch_size))
    print(
        f"xlink-fix: {len(slugs)} slug(s) in {len(batches)} batch(es) "
        f"(apply={args.apply and not args.dry_run})",
        flush=True,
    )

    for batch_idx, batch_slugs in enumerate(batches, start=1):
        tag = f"b{batch_idx:02d}"
        print(f"xlink-fix batch {tag}: {len(batch_slugs)} slugs", flush=True)
        rows, updates = process_slug_batch(
            env=env,
            public_base=public_base,
            slugs=batch_slugs,
            catalog=catalog,
            slug_index=slug_index,
            apply=bool(args.apply),
            dry_run=bool(args.dry_run),
            bootstrap_tag=tag,
        )
        report_rows.extend(rows)
        all_updates.extend(updates)

    changed_count = sum(1 for row in report_rows if row.get("changed"))
    dead_unwraps = [
        change
        for row in report_rows
        for change in (row.get("dead_unwrap_changes") or [])
    ]

    report = {
        "status": "OK",
        "dry_run": bool(args.dry_run or not args.apply),
        "public_base": public_base,
        "posts_total": len(report_rows),
        "posts_changed": changed_count,
        "dead_unwrap_count": len(dead_unwraps),
        "dead_unwraps": dead_unwraps,
        "posts": report_rows,
    }
    out_path = root / "memory/live-xlink-fix-report.json"
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
