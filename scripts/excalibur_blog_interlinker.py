#!/usr/bin/env python3
"""Hard gate: outbound interlink to published siblings when enabled."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from excalibur_blog_interlink_lib import (
    all_interlink_candidates,
    compute_xlink_quota,
    load_tenant,
    outbound_links_in_html,
    project_root,
    unique_blog_slugs_in_html,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article-dir", required=True)
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("-o", "--output", default="interlink-gate.json")
    args = parser.parse_args()

    root = args.root or project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    tenant = load_tenant(root)
    if not tenant.get("interlink_old_articles"):
        report = {"status": "PASS", "skipped": True, "reason": "interlink_old_articles=false"}
        out = article_dir / args.output
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False))
        return 0

    meta_path = article_dir / "article.meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.is_file() else {}
    topic_id = str(meta.get("topic_id") or "").upper()
    slug = str(meta.get("slug") or "").strip()

    candidates = all_interlink_candidates(root, exclude_topic_id=topic_id)
    html_path = article_dir / "article.html"
    html = html_path.read_text(encoding="utf-8") if html_path.is_file() else ""
    found = outbound_links_in_html(html, candidates)
    unique_slugs = unique_blog_slugs_in_html(html)
    min_required, max_allowed, quota_warnings = compute_xlink_quota(len(candidates))
    warnings: list[str] = list(quota_warnings)

    errors: list[str] = []
    outbound_count = len(unique_slugs)
    if min_required > 0 and outbound_count < min_required:
        missing = [row for row in candidates if row not in found][:4]
        errors.append(
            "interlink outbound: add 3–4 unique live /blog/ links to related published articles "
            f"(found {outbound_count}, need {min_required}–{max_allowed}; "
            f"missing examples: {', '.join(str(r.get('slug')) for r in missing)})"
        )
    if max_allowed > 0 and outbound_count > max_allowed:
        errors.append(
            f"interlink outbound: too many /blog/ cross-links ({outbound_count}); max {max_allowed}"
        )

    report = {
        "status": "PASS" if not errors else "BLOCK",
        "topic_id": topic_id,
        "slug": slug,
        "candidates_count": len(candidates),
        "outbound_found": [{"slug": r.get("slug"), "title": r.get("title")} for r in found],
        "outbound_unique_slugs": unique_slugs,
        "outbound_required_min": min_required,
        "outbound_required_max": max_allowed,
        "warnings": warnings,
        "errors": errors,
    }
    out = article_dir / args.output
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if errors:
        for err in errors:
            print(f"BLOCKER: {err}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
