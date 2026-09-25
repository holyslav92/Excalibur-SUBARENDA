#!/usr/bin/env python3
"""Case-delivery gate — two-beat case H1, not how-to (Title stage)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

CYRILLIC_RE = re.compile(r"[А-Яа-яЁё]")
HOWTO_RE = re.compile(
    r"(?i)(полный гайд|топ-\d+|топ\s*\d+|^\d+\s+вопрос|\d+\s+совет|как\s+(вернуть|снять|проверить|не\s+потерять)|"
    r"что\s+делать\s+если|инструкция|чеклист\s+из)",
)
LABEL_HEAD_RE = re.compile(
    r"(?i)^(проверка|залог|горячая вода|посуточная аренда|бесконтактное заселение)\s*:"
)
BANNED_H1_RE = re.compile(r"(?i)(2026|лучшие|секрет|seo|риэлтор\s+тюмень)")
CAPS_RUN_RE = re.compile(r"[A-ZА-ЯЁ]{5,}")


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def normalize_h1(text: str) -> str:
    return " ".join(str(text or "").split())


def validate_title_brief(article_dir: Path) -> dict:
    errors: list[str] = []
    brief_path = article_dir / "title-brief.json"
    stamp_path = article_dir / "derouter-opus-stamp-title.json"

    if not brief_path.is_file():
        return {"status": "BLOCK", "errors": ["title-brief.json missing"]}

    try:
        data = json.loads(brief_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"status": "BLOCK", "errors": [f"title-brief.json invalid JSON: {exc}"]}

    h1 = normalize_h1(str(data.get("h1") or ""))
    title = normalize_h1(str(data.get("title") or ""))
    subject = str(data.get("subject") or "").strip()
    angle = str(data.get("angle") or "").strip()
    topic_id = str(data.get("topic_id") or "").strip()
    verdict = str(data.get("verdict") or "").strip().upper()

    if not topic_id:
        errors.append("topic_id missing")
    if not h1:
        errors.append("h1 empty")
    if not title:
        errors.append("title empty")
    if h1 and title and h1 != title:
        errors.append("h1 must equal title")
    if verdict != "PASS":
        errors.append(f"verdict must be PASS (got {verdict or 'empty'})")
    if not subject:
        errors.append("subject missing")
    if not angle:
        errors.append("angle missing")

    if h1 and not CYRILLIC_RE.search(h1):
        errors.append("h1 must contain Cyrillic")

    if h1:
        n = len(h1)
        if n < 45 or n > 75:
            errors.append(f"h1 length {n} outside 45–75 (target ~50–70)")

        parts = [p.strip() for p in h1.split(".") if p.strip()]
        if len(parts) < 2:
            errors.append("h1 must be two-beat case (two clauses separated by '.')")
        elif len(parts) > 3:
            errors.append("h1 has too many beats (max two short clauses + optional time)")

        if HOWTO_RE.search(h1):
            errors.append("h1 looks like how-to, not case hook")
        if LABEL_HEAD_RE.search(h1):
            errors.append("h1 looks like label head")
        if BANNED_H1_RE.search(h1):
            errors.append("h1 contains banned SEO/year/clickbait token")
        if CAPS_RUN_RE.search(h1):
            errors.append("h1 contains CAPS run")

    if not stamp_path.is_file():
        errors.append("derouter-opus-stamp-title.json missing (title must use Derouter)")

    status = "PASS" if not errors else "BLOCK"
    return {
        "status": status,
        "stage": "title",
        "h1": h1,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Case delivery gate (title: two-beat case H1)")
    parser.add_argument("--article-dir", required=True, help="Article directory")
    parser.add_argument("--stage", default="title", choices=("title",))
    args = parser.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    if args.stage != "title":
        print(f"BLOCK unsupported stage {args.stage}", file=sys.stderr)
        return 1

    result = validate_title_brief(article_dir)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
