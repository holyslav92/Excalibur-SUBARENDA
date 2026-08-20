#!/usr/bin/env python3
"""Validate writer-ready.json (or legacy editor-choice.json) + article.html."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from excalibur_blog_html_linter import ALLOWED_TAGS, lint_html_file

CHOICE_NAMES = ("writer-ready.json", "editor-choice.json")
FORBIDDEN_KEYS = ("critic_verdict_ref", "critic_actions_resolved", "title_id", "hook_id")


def _load_choice(article_dir: Path) -> tuple[Path | None, dict]:
    for name in CHOICE_NAMES:
        path = article_dir / name
        if path.is_file():
            return path, json.loads(path.read_text(encoding="utf-8"))
    return None, {}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article-dir", required=True)
    parser.add_argument("--root", default=".")
    parser.add_argument("-o", "--output", default="writer-ready-gate.json")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    article_dir = (
        root / args.article_dir
        if not Path(args.article_dir).is_absolute()
        else Path(args.article_dir)
    )
    errors: list[str] = []

    path, data = _load_choice(article_dir)
    if path is None:
        errors.append("missing writer-ready.json")
    elif data:
        winner = str(data.get("winner_variant") or "").strip().lower()
        if winner != "a":
            errors.append("winner_variant must be a")
        if not str(data.get("rationale") or "").strip():
            errors.append("rationale required")
        reviewed_by = str(data.get("reviewed_by") or "")
        if reviewed_by != "excalibur-blog-writer":
            errors.append("reviewed_by must be excalibur-blog-writer")
        for key in FORBIDDEN_KEYS:
            if key in data:
                errors.append(f"forbidden choice key: {key}")
        prior = data.get("required_prior_articles")
        if not isinstance(prior, list) or prior:
            errors.append("required_prior_articles must be empty")
        draft = article_dir / "drafts" / "variant-a.html"
        if not draft.is_file():
            errors.append("missing drafts/variant-a.html")

    html = article_dir / "article.html"
    if not html.is_file():
        errors.append("missing article.html (Writer final)")
    elif html.stat().st_size < 500:
        errors.append("article.html too small")
    else:
        lint = lint_html_file(html, ALLOWED_TAGS)
        if lint.get("verdict") != "pass":
            for err in lint.get("errors") or []:
                errors.append(f"html_linter: {err}")

    report = {
        "gate": "writer-ready",
        "status": "PASS" if not errors else "BLOCK",
        "errors": errors,
        "choice_file": path.name if path else None,
    }
    out = article_dir / Path(args.output).name
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Also write legacy gate name so old publish checklists still find a PASS file.
    legacy = article_dir / "editor-choice-gate.json"
    if Path(args.output).name != legacy.name:
        legacy.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
