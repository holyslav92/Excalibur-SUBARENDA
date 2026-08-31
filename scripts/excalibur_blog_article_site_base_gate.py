#!/usr/bin/env python3
"""Gate: committed article.html must use {{SITE_BASE}}, not live/punycode tenant URLs."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from excalibur_blog_site_base import (
    SITE_BASE_PLACEHOLDER,
    find_punycode_href_hits,
    find_secret_scan_hits,
    resolve_public_base_from_env,
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(description="Article HTML git-safe site URL gate")
    parser.add_argument("--article-dir", type=Path, required=True)
    parser.add_argument("--public-base", type=str, default="")
    parser.add_argument("-o", "--output", type=str, default="article-site-base-gate.json")
    args = parser.parse_args()

    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    html_path = article_dir / "article.html"
    if not html_path.is_file():
        print(f"BLOCKER: article.html missing: {html_path}", file=sys.stderr)
        return 2

    public_base = (args.public_base or resolve_public_base_from_env() or "").strip()
    html = html_path.read_text(encoding="utf-8")
    hits = find_secret_scan_hits(html, public_base)
    punycode_hits = find_punycode_href_hits(html)
    errors: list[str] = []
    if punycode_hits:
        errors.append(
            f"article.html has punycode tenant href(s); use {SITE_BASE_PLACEHOLDER}/path — "
            f"run excalibur_blog_normalize_article_site_urls.py --fix"
        )
    live_hits = [h for h in hits if h not in punycode_hits and h != "[REDACTED]"]
    if live_hits:
        errors.append(
            f"article.html has live site URL/host literals ({len(live_hits)} hit(s)); "
            f"use {SITE_BASE_PLACEHOLDER} placeholders"
        )

    status = "PASS" if not errors else "FAIL"
    report = {
        "gate": "article_site_base",
        "status": status,
        "article_dir": str(article_dir.relative_to(root)).replace("\\", "/"),
        "punycode_href_hits": punycode_hits[:20],
        "secret_scan_hits": hits[:20],
        "errors": errors,
    }
    out_path = article_dir / Path(args.output).name
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
