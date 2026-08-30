#!/usr/bin/env python3
"""Shared helpers for Excalibur BLOG interlink (outbound + inbound)."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from excalibur_blog_live_catalog import slug_from_blog_href
from excalibur_blog_site_base import SITE_BASE_PLACEHOLDER, blog_path_for_slug, canonical_blog_xlink_href

XLINK_MIN = 3
XLINK_MAX = 4

INTERLINK_MARKER_PREFIX = 'data-excalibur-interlink-from="'


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_tenant(root: Path) -> dict[str, Any]:
    path = root / "shared/tenant-config.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def parse_ledger(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    if not path.is_file():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("| topic") or line.startswith("|-"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        if len(cells) >= 5 and cells[0][:4].isdigit():
            topic_id, slug, permalink, status = cells[1], cells[2], cells[3], cells[4]
        else:
            topic_id, slug, status, permalink = cells[0], cells[1], cells[2], cells[3]
        if status.lower() != "published":
            continue
        rows.append(
            {
                "topic_id": topic_id,
                "slug": slug,
                "permalink": permalink,
            }
        )
    return rows


def load_siblings(root: Path) -> list[dict[str, Any]]:
    path = root / "shared/interlink-siblings.json"
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    siblings = data.get("siblings") or []
    return [item for item in siblings if isinstance(item, dict) and item.get("slug")]


def post_id_from_article_meta(root: Path, slug: str) -> int | None:
    """Resolve wp_post_id from a published sibling's article.meta.json when ledger lacks it."""
    articles_root = root / "memory/blog/articles"
    if not articles_root.is_dir():
        return None
    for meta_path in articles_root.glob("*/article.meta.json"):
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if str(meta.get("slug") or "").strip() != slug:
            continue
        raw = meta.get("wp_post_id") or meta.get("post_id")
        if raw:
            try:
                return int(raw)
            except (TypeError, ValueError):
                return None
    return None


def all_interlink_candidates(root: Path, *, exclude_topic_id: str = "") -> list[dict[str, Any]]:
    ledger = parse_ledger(root / "shared/published-articles.md")
    siblings = load_siblings(root)
    merged: dict[str, dict[str, Any]] = {}
    for row in ledger:
        slug = str(row.get("slug") or "").strip()
        if not slug:
            continue
        if exclude_topic_id and str(row.get("topic_id") or "").upper() == exclude_topic_id.upper():
            continue
        merged[slug] = {
            "slug": slug,
            "title": row.get("title") or slug,
            "permalink": row.get("permalink") or "",
            "topic_id": row.get("topic_id") or "",
            "post_id": row.get("post_id"),
            "source": "ledger",
        }
    for row in siblings:
        slug = str(row.get("slug") or "").strip()
        if not slug:
            continue
        if slug not in merged:
            merged[slug] = {
                "slug": slug,
                "title": row.get("title") or slug,
                "permalink": "",
                "topic_id": "",
                "post_id": row.get("post_id"),
                "source": "siblings",
            }
        else:
            if row.get("post_id"):
                merged[slug]["post_id"] = row.get("post_id")
            if row.get("title"):
                merged[slug]["title"] = row.get("title")
    for slug, row in merged.items():
        if not row.get("post_id"):
            pid = post_id_from_article_meta(root, slug)
            if pid:
                row["post_id"] = pid
    return list(merged.values())


def slug_in_html(html: str, slug: str) -> bool:
    return slug in (html or "")


def outbound_links_in_html(html: str, candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [row for row in candidates if slug_in_html(html, str(row.get("slug") or ""))]


def unique_blog_slugs_in_html(html: str) -> list[str]:
    """Уникальные slug из href=/blog/... в HTML (порядок первого появления)."""
    slugs: list[str] = []
    seen: set[str] = set()
    for match in re.finditer(r"""href=["']([^"']+)["']""", html or "", re.I):
        slug = slug_from_blog_href(match.group(1).strip())
        if slug and slug not in seen:
            seen.add(slug)
            slugs.append(slug)
    return slugs


def compute_xlink_quota(available_count: int) -> tuple[int, int, list[str]]:
    """(min_required, max_allowed, warnings) для квоты перекрёстных ссылок."""
    warnings: list[str] = []
    if available_count <= 0:
        return 0, 0, warnings
    if available_count < XLINK_MIN:
        warnings.append(
            f"xlink: only {available_count} live sibling(s) available — "
            "link all live posts, never invent URLs"
        )
        return available_count, available_count, warnings
    return XLINK_MIN, min(XLINK_MAX, available_count), warnings


def interlink_block_html(*, from_slug: str, target_url: str, target_title: str) -> str:
    marker = f'{INTERLINK_MARKER_PREFIX}{from_slug}"'
    safe_title = target_title.replace('"', "&quot;")
    return (
        f'<p class="excalibur-interlink-readalso" {marker}>'
        f"<b>Читайте также:</b> "
        f'<a href="{target_url}">{safe_title}</a></p>'
    )


def append_interlink_block(content: str, *, from_slug: str, target_url: str, target_title: str) -> str:
    marker = f'{INTERLINK_MARKER_PREFIX}{from_slug}"'
    if marker in content:
        return content
    return (content or "").rstrip() + "\n" + interlink_block_html(
        from_slug=from_slug,
        target_url=target_url,
        target_title=target_title,
    )


def permalink_path_for_slug(slug: str, category_slug: str = "") -> str:
    """Canonical git-safe xlink href for a published sibling (Dzen-safe after publish expand)."""
    _ = category_slug  # legacy arg; blog posts live at /blog/{slug}/
    return canonical_blog_xlink_href(slug.strip("/"))


def resolve_public_path(candidate: dict[str, Any], public_base: str = "") -> str:
    permalink = str(candidate.get("permalink") or "").strip()
    if permalink.startswith("/"):
        return permalink
    if permalink.startswith("http") and public_base:
        parsed = urlparse(permalink)
        return parsed.path or f"/{candidate.get('slug')}/"
    slug = str(candidate.get("slug") or "").strip()
    return permalink_path_for_slug(slug)


def build_inbound_updates(
    *,
    new_slug: str,
    new_title: str,
    new_url: str,
    targets: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    updates: list[dict[str, Any]] = []
    for target in targets:
        post_id = target.get("post_id")
        if not post_id:
            continue
        updates.append(
            {
                "post_id": int(post_id),
                "marker": f'{INTERLINK_MARKER_PREFIX}{new_slug}"',
                "html": interlink_block_html(
                    from_slug=new_slug,
                    target_url=new_url,
                    target_title=new_title,
                ),
            }
        )
    return updates


def build_interlink_bootstrap_php(payload: dict[str, Any]) -> str:
    import base64

    encoded = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';

$p = json_decode(base64_decode('{encoded}'), true);
if (!is_array($p) || empty($p['updates']) || !is_array($p['updates'])) {{
    echo 'ERR interlink: empty payload' . PHP_EOL;
    exit(1);
}}
foreach ($p['updates'] as $u) {{
    $post_id = (int) ($u['post_id'] ?? 0);
    $marker = (string) ($u['marker'] ?? '');
    $html = (string) ($u['html'] ?? '');
    if ($post_id <= 0 || $marker === '' || $html === '') {{
        echo 'ERR interlink: bad update row' . PHP_EOL;
        continue;
    }}
    $post = get_post($post_id);
    if (!$post instanceof WP_Post) {{
        echo 'ERR interlink: missing post=' . $post_id . PHP_EOL;
        continue;
    }}
    $content = (string) $post->post_content;
    if (strpos($content, $marker) !== false) {{
        echo 'OK interlink_skip=' . $post_id . PHP_EOL;
        continue;
    }}
    $content = rtrim($content) . "\\n" . $html;
    wp_update_post([
        'ID' => $post_id,
        'post_content' => wp_slash($content),
    ]);
    echo 'OK interlink_inbound=' . $post_id . PHP_EOL;
}}
echo 'OK interlink_done' . PHP_EOL;
"""


def pick_inbound_targets(
    candidates: list[dict[str, Any]],
    *,
    new_slug: str,
    max_inbound: int = 3,
) -> list[dict[str, Any]]:
    filtered = [row for row in candidates if str(row.get("slug") or "") != new_slug]
    filtered.sort(key=lambda row: (0 if row.get("source") == "ledger" else 1, str(row.get("slug") or "")))
    return filtered[: max(0, max_inbound)]
