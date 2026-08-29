#!/usr/bin/env python3
"""Hard gate: live-catalog cross-link QA before publish.

Validates article.html outbound /blog/ links against the live site catalog,
HTTP 200, anchor/title intent, mashed-link prose, and locked CTA URLs.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from excalibur_blog_interlink_lib import compute_xlink_quota, unique_blog_slugs_in_html
from excalibur_blog_link_verify import check_url_with_connection_reset_retry
from excalibur_blog_live_catalog import (
    blog_path_for_slug,
    catalog_path,
    catalog_post_for_slug,
    load_catalog,
    refresh_catalog,
    slug_from_blog_href,
)
from excalibur_blog_site_base import (
    SITE_BASE_PLACEHOLDER,
    expand_site_base,
    normalize_public_base,
    redact_structure,
    resolve_public_base_from_env,
)

BANNED_HOSTS = frozenset({"tymenrieltor.ru", "www.tymenrieltor.ru"})
MASHED_PLAIN_PATTERNS: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"пробесконтакт", re.I), "mashed plain text: «пробесконтактное» (missing space/link)"),
    (re.compile(r"отдельно:скрытые", re.I), "mashed plain text: «отдельно:скрытые»"),
    (re.compile(r"MAXили\s*Telegram", re.I), "mashed plain text: «MAXили Telegram»"),
    (re.compile(r"надобрыйдом", re.I), "mashed plain text: «надобрыйдом»"),
    (re.compile(r"заселение:добрыйдом", re.I), "mashed plain text glued site domain"),
)
MASHED_HTML_PATTERNS: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"отдельно:<a\b", re.I), "mashed HTML: «отдельно:<a» missing space before link"),
    (re.compile(r"MAX<a\b[^>]*>\s*или", re.I), "mashed HTML: «MAX<a>или»"),
    (re.compile(r"Telegram<a\b", re.I), "mashed HTML: glued Telegram anchor"),
    (re.compile(r"[а-яё]{4,}<a\b", re.I), "mashed HTML: Cyrillic glued directly before <a"),
    (re.compile(r"</a>[а-яё]{3,}", re.I), "mashed HTML: Cyrillic glued directly after </a>"),
)
JUNK_HREF_PREFIXES = ("javascript:", "mailto:", "data:", "vbscript:")


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_tenant(root: Path) -> dict[str, Any]:
    path = root / "shared/tenant-config.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_title(value: str) -> str:
    value = unescape(value or "").casefold()
    value = value.replace("ё", "е")
    value = re.sub(r"[«»\"'„“]", " ", value)
    value = re.sub(r"[^\w\s]+", " ", value, flags=re.UNICODE)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def title_tokens(value: str) -> set[str]:
    stop = {
        "и",
        "в",
        "на",
        "по",
        "к",
        "с",
        "о",
        "об",
        "от",
        "до",
        "за",
        "из",
        "как",
        "что",
        "это",
        "не",
        "или",
        "а",
        "the",
        "про",
        "при",
    }
    tokens: set[str] = set()
    for tok in normalize_title(value).split():
        if len(tok) < 3 or tok in stop:
            continue
        tokens.add(tok)
        if len(tok) > 5:
            tokens.add(tok[:5])
    return tokens


def anchor_matches_catalog_title(anchor: str, catalog_title: str) -> bool:
    anchor_norm = normalize_title(anchor)
    title_norm = normalize_title(catalog_title)
    if not anchor_norm or not title_norm:
        return False
    if anchor_norm in title_norm or title_norm in anchor_norm:
        return True
    if "от" in anchor_norm and "от" in title_norm and ("цен" in anchor_norm or "цен" in title_norm):
        return True
    a_tokens = title_tokens(anchor)
    t_tokens = title_tokens(catalog_title)
    if not a_tokens:
        return False
    overlap = a_tokens & t_tokens
    if len(overlap) >= 1:
        return True
    # Short anchors like «правила проживания» vs long title.
    for token in a_tokens:
        if token in title_norm:
            return True
    return False


class ArticleLinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[dict[str, str]] = []
        self._in_a = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        attr = {k: (v or "") for k, v in attrs}
        href = attr.get("href", "").strip()
        if not href:
            return
        self.links.append({"href": href, "anchor": ""})
        self._in_a = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a":
            self._in_a = False

    def handle_data(self, data: str) -> None:
        if not self._in_a or not self.links:
            return
        if data.strip():
            self.links[-1]["anchor"] += data


def extract_article_links(html: str) -> list[dict[str, str]]:
    parser = ArticleLinkExtractor()
    parser.feed(html or "")
    return parser.links


def strip_tags(html: str) -> str:
    return re.sub(r"<[^>]+>", " ", html or "")


def detect_mashed_prose(html: str) -> list[str]:
    errors: list[str] = []
    plain = strip_tags(html)
    for pattern, message in MASHED_PLAIN_PATTERNS:
        if pattern.search(plain):
            errors.append(message)
    for pattern, message in MASHED_HTML_PATTERNS:
        if pattern.search(html or ""):
            # Allow normal «MAX</a> или <a>Telegram» spacing.
            if "MAX<a" in message and re.search(r"MAX\s*<a\b", html or "", re.I):
                continue
            if "Telegram<a" in message and re.search(r"Telegram\s*<a\b", html or "", re.I):
                continue
            if pattern.search(html or ""):
                errors.append(message)
    return errors


def is_cta_href(href: str, tenant: dict[str, Any]) -> bool:
    href_l = href.lower()
    if href_l.startswith("tel:"):
        return True
    cta_links = [str(x) for x in (tenant.get("cta_links") or [])]
    channels = tenant.get("cta_channels") or {}
    for raw in cta_links + list(channels.values()):
        val = str(raw or "").strip().lower()
        if val and val in href_l:
            return True
    booking = str(channels.get("booking") or "").strip().lower()
    site = str(channels.get("site") or "").strip().lower()
    if booking and booking.rstrip("/") in href_l:
        return True
    if site and (href_l == site or href_l == site.rstrip("/") + "/"):
        return True
    if "t.me/dobriy_dom" in href_l or "max.ru/id660300569233_biz" in href_l:
        return True
    if "добры" in href_l and ".рф" in href_l:
        return True
    if "{{site_base}}" in href_l:
        return True
    return False


def resolve_runtime_base(site_base: str | None) -> str:
    raw = normalize_public_base(site_base or resolve_public_base_from_env())
    if not raw:
        raise ValueError("PUBLIC_SITE_URL / --site-base required for crosslink QA")
    if SITE_BASE_PLACEHOLDER in raw:
        live = resolve_public_base_from_env()
        if not live:
            raise ValueError(f"{SITE_BASE_PLACEHOLDER} requires PUBLIC_SITE_URL in env")
        return live
    return raw


def validate_article_crosslinks(
    html: str,
    *,
    catalog: dict[str, Any],
    site_base: str,
    tenant: dict[str, Any],
    timeout: float = 15.0,
    skip_http: bool = False,
    current_slug: str = "",
) -> dict[str, Any]:
    runtime_base = resolve_runtime_base(site_base)
    site_host = (urlparse(runtime_base).hostname or "").lower()
    slug_index = catalog.get("slug_index") or {}
    errors: list[str] = []
    warnings: list[str] = []
    checks: list[dict[str, Any]] = []

    errors.extend(detect_mashed_prose(html))

    for link in extract_article_links(html):
        href = link.get("href", "").strip()
        anchor = unescape(link.get("anchor", "")).strip()
        if not href or href.startswith("#"):
            continue

        lower = href.lower()
        if lower.startswith(JUNK_HREF_PREFIXES):
            errors.append(f"junk href scheme: {href}")
            continue

        parsed = urlparse(href if "://" in href else f"https://{site_host}{href if href.startswith('/') else '/' + href}")
        host = (parsed.netloc or "").lower()
        if host.startswith("www."):
            host = host[4:]
        if host in BANNED_HOSTS or host.endswith(".tymenrieltor.ru"):
            errors.append(f"banned host in href: {href}")
            continue

        slug = slug_from_blog_href(href, site_host=site_host)
        if slug is None:
            if href.startswith("/") and not is_cta_href(href, tenant):
                # Root-relative article-ish paths without /blog/ prefix.
                root_match = re.match(r"^/([a-z0-9][a-z0-9-]+)/?$", href.rstrip("/") + "/")
                if root_match and root_match.group(1) != "blog":
                    maybe = root_match.group(1)
                    if maybe in slug_index:
                        errors.append(
                            f"internal article href missing /blog/ prefix: {href} "
                            f"(use {blog_path_for_slug(maybe)})"
                        )
            continue

        catalog_row = catalog_post_for_slug(catalog, slug)
        check: dict[str, Any] = {
            "href": href,
            "slug": slug,
            "anchor": anchor,
            "catalog_title": (catalog_row or {}).get("title"),
            "http_ok": None,
            "title_ok": None,
        }

        if not catalog_row:
            errors.append(f"invented /blog/ slug not in live catalog: {slug} ({href})")
            check["error"] = "slug_not_in_catalog"
            checks.append(check)
            continue

        if not anchor_matches_catalog_title(anchor, str(catalog_row.get("title") or slug)):
            errors.append(
                f"anchor/title mismatch for {href}: «{anchor}» vs catalog "
                f"«{catalog_row.get('title')}»"
            )
            check["title_ok"] = False
        else:
            check["title_ok"] = True

        canonical_path = blog_path_for_slug(slug)
        if href.startswith("/") and not href.startswith("/blog/"):
            errors.append(f"/blog/ link must use catalog path {canonical_path}, got {href}")
            check["path_ok"] = False
        else:
            check["path_ok"] = True

        if skip_http:
            check["http_ok"] = True
            check["http_skipped"] = True
        else:
            check_target = href
            if SITE_BASE_PLACEHOLDER in check_target:
                check_target = expand_site_base(check_target, runtime_base)
            elif check_target.startswith("/"):
                check_target = runtime_base.rstrip("/") + check_target
            result = check_url_with_connection_reset_retry(check_target, timeout, "ExcaliburBlogCrosslinkQA/1.0")
            check["http_status"] = result.get("status")
            check["http_ok"] = bool(result.get("ok"))
            if not result.get("ok"):
                errors.append(f"HTTP check failed for {href}: status={result.get('status')} {result.get('error')}")

        checks.append(check)

    slug_index = catalog.get("slug_index") or {}
    catalog_slugs = set(slug_index.keys())
    if current_slug:
        catalog_slugs.discard(current_slug.strip())
    available_live = len(catalog_slugs)
    min_required, max_allowed, quota_warnings = compute_xlink_quota(available_live)
    warnings.extend(quota_warnings)

    valid_outbound_slugs: list[str] = []
    for check in checks:
        slug = str(check.get("slug") or "")
        if not slug or check.get("error"):
            continue
        if check.get("title_ok") and check.get("path_ok") and check.get("http_ok") is not False:
            valid_outbound_slugs.append(slug)

    unique_valid = list(dict.fromkeys(valid_outbound_slugs))
    outbound_count = len(unique_valid)
    if min_required > 0 and outbound_count < min_required:
        errors.append(
            f"xlink quota: need {min_required}–{max_allowed} unique live /blog/ URLs "
            f"(found {outbound_count} valid); related to topic, never invent slugs"
        )
    if max_allowed > 0 and outbound_count > max_allowed:
        errors.append(
            f"xlink quota: too many unique /blog/ cross-links ({outbound_count}); max {max_allowed}"
        )

    status = "PASS" if not errors else "FAIL"
    return {
        "status": status,
        "errors": errors,
        "warnings": warnings,
        "checks": checks,
        "catalog_count": len(slug_index),
        "outbound_unique_slugs": unique_valid,
        "outbound_required_min": min_required,
        "outbound_required_max": max_allowed,
        "site_base": runtime_base,
    }


def git_safe_report(report: dict[str, Any], public_base: str | None) -> dict[str, Any]:
    return redact_structure(report, public_base)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--root", type=Path, default=None)
    ap.add_argument("-o", "--output", default="crosslink-qa-gate.json")
    ap.add_argument("--site-base", default="")
    ap.add_argument("--skip-http", action="store_true")
    ap.add_argument("--use-cache", action="store_true", help="Do not refresh live catalog")
    ap.add_argument("--timeout", type=float, default=15.0)
    args = ap.parse_args()

    root = args.root or project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    html_path = article_dir / "article.html"
    if not html_path.is_file():
        print("BLOCKER: article.html missing", file=sys.stderr)
        return 2

    html = html_path.read_text(encoding="utf-8")
    tenant = load_tenant(root)

    try:
        if args.use_cache:
            catalog = load_catalog(catalog_path(root))
            if not catalog.get("posts"):
                catalog = refresh_catalog(root, site_base=args.site_base or None)
        else:
            catalog = refresh_catalog(root, site_base=args.site_base or None)
    except ValueError as exc:
        print(f"BLOCKER: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:  # noqa: BLE001
        print(f"BLOCKER: live catalog refresh failed: {exc}", file=sys.stderr)
        return 2

    meta_path = article_dir / "article.meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.is_file() else {}
    current_slug = str(meta.get("slug") or "").strip()

    try:
        report = validate_article_crosslinks(
            html,
            catalog=catalog,
            site_base=args.site_base or None,
            tenant=tenant,
            timeout=args.timeout,
            skip_http=args.skip_http,
            current_slug=current_slug,
        )
    except ValueError as exc:
        print(f"BLOCKER: {exc}", file=sys.stderr)
        return 2

    report["article_dir"] = str(article_dir.relative_to(root)).replace("\\", "/")
    report["catalog_path"] = str(catalog_path(root).relative_to(root)).replace("\\", "/")
    report["gate"] = "crosslink-qa"

    out_path = article_dir / Path(args.output).name
    runtime_base = report.get("site_base")
    safe = git_safe_report(report, str(runtime_base or ""))
    out_path.write_text(json.dumps(safe, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

    if report["status"] != "PASS":
        for err in report.get("errors") or []:
            print(f"BLOCKER: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
