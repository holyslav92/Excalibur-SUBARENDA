#!/usr/bin/env python3
"""Fetch and cache live /blog/ slug+title catalog from the tenant site."""

from __future__ import annotations

import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

from excalibur_blog_site_base import (
    SITE_BASE_PLACEHOLDER,
    normalize_public_base,
    redact_structure,
    resolve_public_base_from_env,
)

DEFAULT_CATALOG_PATH = "memory/live-catalog.json"
MAX_LISTING_PAGES = 8
USER_AGENT = "ExcaliburBlogLiveCatalog/1.0"


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def slug_from_blog_href(href: str, *, site_host: str = "") -> str | None:
    """Return blog post slug from href or None if not a /blog/{slug}/ link."""
    href = (href or "").strip()
    if not href or href.startswith("#"):
        return None
    if href.startswith("javascript:") or href.startswith("mailto:"):
        return None
    parsed = urlparse(href)
    path = parsed.path or href
    if not path.startswith("/"):
        if "://" in href:
            if site_host and parsed.netloc and parsed.netloc.lower() != site_host.lower():
                return None
            path = parsed.path or ""
        else:
            return None
    path = path.rstrip("/")
    parts = [p for p in path.split("/") if p]
    if len(parts) < 2 or parts[0] != "blog":
        return None
    if parts[1].startswith("page") or parts[1] in {"feed", "category", "tag"}:
        return None
    slug = parts[1]
    if not slug or slug == "blog":
        return None
    return slug


class BlogListingParser(HTMLParser):
    """Parse /blog/ listing cards: anchor href + visible title text."""

    def __init__(self) -> None:
        super().__init__()
        self.entries: list[dict[str, str]] = []
        self._in_article_link = False
        self._current_href = ""
        self._title_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        attr = {k: (v or "") for k, v in attrs}
        href = attr.get("href", "").strip()
        classes = attr.get("class", "")
        if "articles__item" in classes or "/blog/" in href:
            slug = slug_from_blog_href(href)
            if slug:
                self._in_article_link = True
                self._current_href = href
                self._title_parts = []

    def handle_data(self, data: str) -> None:
        if self._in_article_link and data.strip():
            self._title_parts.append(data.strip())

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != "a" or not self._in_article_link:
            return
        title = unescape(" ".join(self._title_parts)).strip()
        title = re.sub(r"\s+", " ", title)
        title = re.sub(r"(?i)\s*смотреть подробнее\s*$", "", title).strip()
        slug = slug_from_blog_href(self._current_href)
        if slug:
            self.entries.append(
                {
                    "slug": slug,
                    "title": title or slug,
                    "href": self._current_href,
                }
            )
        self._in_article_link = False
        self._current_href = ""
        self._title_parts = []


def _fetch_url(url: str, *, timeout: float = 20.0) -> str:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return resp.read().decode("utf-8", errors="replace")


def fetch_listing_page(site_base: str, page: int) -> str:
    base = normalize_public_base(site_base)
    if page <= 1:
        url = f"{base}/blog/"
    else:
        url = f"{base}/blog/page/{page}/"
    return _fetch_url(url)


def parse_listing_html(html: str) -> list[dict[str, str]]:
    parser = BlogListingParser()
    parser.feed(html)
    return parser.entries


def merge_catalog_entries(entries: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    merged: dict[str, dict[str, str]] = {}
    for row in entries:
        slug = str(row.get("slug") or "").strip()
        if not slug:
            continue
        title = str(row.get("title") or slug).strip()
        href = str(row.get("href") or f"/blog/{slug}/").strip()
        if slug not in merged or len(title) > len(merged[slug].get("title", "")):
            merged[slug] = {"slug": slug, "title": title, "href": href}
    return merged


def fetch_live_catalog(
    site_base: str | None = None,
    *,
    max_pages: int = MAX_LISTING_PAGES,
    timeout: float = 20.0,
) -> dict[str, Any]:
    base = normalize_public_base(site_base or resolve_public_base_from_env())
    if not base:
        raise ValueError("PUBLIC_SITE_URL / --site-base required for live catalog refresh")
    if SITE_BASE_PLACEHOLDER in base or base == SITE_BASE_PLACEHOLDER:
        raise ValueError(f"live catalog requires real site base, not {SITE_BASE_PLACEHOLDER}")

    host = (urlparse(base).hostname or "").lower()
    all_entries: list[dict[str, str]] = []
    pages_fetched = 0
    for page in range(1, max_pages + 1):
        try:
            html = fetch_listing_page(base, page)
        except urllib.error.HTTPError as exc:
            if exc.code == 404 and page > 1:
                break
            raise
        pages_fetched = page
        page_entries = parse_listing_html(html)
        if not page_entries and page > 1:
            break
        all_entries.extend(page_entries)

    by_slug = merge_catalog_entries(all_entries)
    posts = sorted(by_slug.values(), key=lambda row: row["slug"])
    return {
        "site_base": base,
        "site_host": host,
        "pages_fetched": pages_fetched,
        "count": len(posts),
        "posts": posts,
        "slug_index": {row["slug"]: row for row in posts},
    }


def catalog_path(root: Path | None = None) -> Path:
    root = root or project_root()
    return root / DEFAULT_CATALOG_PATH


def save_catalog(catalog: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    safe = redact_structure(catalog, catalog.get("site_base"))
    path.write_text(json.dumps(safe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_catalog(path: Path | None = None) -> dict[str, Any]:
    path = path or catalog_path()
    if not path.is_file():
        return {"posts": [], "slug_index": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    posts = data.get("posts") or []
    slug_index = data.get("slug_index")
    if not isinstance(slug_index, dict):
        slug_index = {str(row.get("slug")): row for row in posts if row.get("slug")}
    data["slug_index"] = slug_index
    return data


def refresh_catalog(
    root: Path | None = None,
    *,
    site_base: str | None = None,
    write: bool = True,
) -> dict[str, Any]:
    root = root or project_root()
    catalog = fetch_live_catalog(site_base=site_base)
    if write:
        save_catalog(catalog, catalog_path(root))
    return catalog


def catalog_post_for_slug(catalog: dict[str, Any], slug: str) -> dict[str, str] | None:
    idx = catalog.get("slug_index") or {}
    row = idx.get(slug)
    return row if isinstance(row, dict) else None


def blog_path_for_slug(slug: str) -> str:
    return f"/blog/{slug.strip('/')}/"


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--site-base", default="")
    ap.add_argument("--output", type=Path, default=None)
    ap.add_argument("--max-pages", type=int, default=MAX_LISTING_PAGES)
    args = ap.parse_args()

    try:
        catalog = fetch_live_catalog(
            site_base=args.site_base or None,
            max_pages=max(1, args.max_pages),
        )
    except ValueError as exc:
        print(f"BLOCKER: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL live catalog: {exc}", file=sys.stderr)
        return 1

    out = args.output or catalog_path()
    save_catalog(catalog, out)
    print(json.dumps({"status": "OK", "count": catalog["count"], "path": str(out)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
