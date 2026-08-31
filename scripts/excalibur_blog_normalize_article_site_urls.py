#!/usr/bin/env python3
"""Normalize article.html hrefs to git-safe {{SITE_BASE}} (post Sol/Writer Derouter)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from excalibur_blog_site_base import (
    find_punycode_href_hits,
    find_secret_scan_hits,
    normalize_committed_html_site_urls,
    resolve_public_base_from_env,
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def normalize_file(path: Path, public_base: str | None, *, dry_run: bool) -> dict:
    before = path.read_text(encoding="utf-8")
    after = normalize_committed_html_site_urls(before, public_base)
    changed = after != before
    if changed and not dry_run:
        path.write_text(after, encoding="utf-8")
    return {
        "path": str(path),
        "changed": changed,
        "punycode_before": find_punycode_href_hits(before),
        "punycode_after": find_punycode_href_hits(after),
        "secret_scan_after": find_secret_scan_hits(after, public_base),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize article HTML site URLs to {{SITE_BASE}}")
    parser.add_argument("--article-dir", type=Path, required=True)
    parser.add_argument("--public-base", type=str, default="")
    parser.add_argument("--fix", action="store_true", help="Write normalized HTML back to disk")
    parser.add_argument(
        "--also-variant-a",
        action="store_true",
        help="Also normalize drafts/variant-a.html when present",
    )
    parser.add_argument("-o", "--output", type=str, default="normalize-site-urls-report.json")
    args = parser.parse_args()

    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    html_path = article_dir / "article.html"
    if not html_path.is_file():
        print(f"BLOCKER: article.html missing: {html_path}", file=sys.stderr)
        return 2

    public_base = (args.public_base or resolve_public_base_from_env() or "").strip() or None
    dry_run = not args.fix
    files = [html_path]
    variant = article_dir / "drafts" / "variant-a.html"
    if args.also_variant_a and variant.is_file():
        files.append(variant)

    results = [normalize_file(path, public_base, dry_run=dry_run) for path in files]
    any_changed = any(r["changed"] for r in results)
    remaining = [h for r in results for h in r["secret_scan_after"]]

    report = {
        "script": "normalize_article_site_urls",
        "dry_run": dry_run,
        "article_dir": str(article_dir.relative_to(root)).replace("\\", "/"),
        "files": results,
        "any_changed": any_changed,
        "remaining_secret_scan_hits": remaining[:20],
        "status": "PASS" if not remaining else "FAIL",
    }
    out_path = article_dir / Path(args.output).name
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    if remaining:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
