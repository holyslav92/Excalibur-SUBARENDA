#!/usr/bin/env python3
"""Case-delivery gate — two-beat H1 and stage checks (title, later writer/sol)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

HOW_TO_RES = (
    re.compile(r"^\s*\d+\s+вопрос", re.I),
    re.compile(r"\bполный\s+гайд\b", re.I),
    re.compile(r"\bтоп[-\s]?\d+\b", re.I),
    re.compile(r"\bлучш(ие|ий|их)\b", re.I),
    re.compile(r"\b20\d{2}\b"),
    re.compile(r":\s*\d+\s+вопрос", re.I),
    re.compile(r"^как\s+", re.I),
    re.compile(r"^что\s+делать\s+если\b", re.I),
)

LABEL_HEAD_RES = (
    re.compile(r"^проверка\s+", re.I),
    re.compile(r"^заселение\s*:", re.I),
    re.compile(r"^посуточная\s+аренда\s*:", re.I),
)

TWO_BEAT_RE = re.compile(
    r"(?<=[.!?…])\s+.+|(?<=—)\s*.+|(?<=-)\s*.+",
    re.UNICODE,
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def published_h1s(article_dir: Path) -> list[str]:
    titles: list[str] = []
    for rel in ("published-titles-only.md",):
        p = article_dir / rel
        if not p.is_file():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            if "| published" not in line.lower():
                continue
            parts = [c.strip() for c in line.split("|")]
            if len(parts) >= 4:
                titles.append(parts[3])
    return titles


def check_title_stage(article_dir: Path) -> dict[str, Any]:
    errors: list[str] = []
    brief_path = article_dir / "title-brief.json"
    data = load_json(brief_path)
    if not data:
        return {"status": "BLOCK", "stage": "title", "errors": ["title-brief.json missing or invalid JSON"]}

    h1 = str(data.get("h1") or data.get("title") or "").strip()
    if not h1:
        errors.append("h1/title empty")

    verdict = str(data.get("verdict") or "").strip().upper()
    if verdict != "PASS":
        errors.append(f"verdict must be PASS (got {verdict or 'empty'})")

    topic_id = str(data.get("topic_id") or data.get("brief_id") or "").strip()
    if topic_id and topic_id.upper() not in ("B03", "B03-POSUTOCHNO"):
        if not topic_id.upper().startswith("B03"):
            errors.append(f"topic_id mismatch: {topic_id}")

    if h1:
        n = len(h1)
        if n < 45 or n > 75:
            errors.append(f"h1 length {n} outside ~50–70 (soft 45–75)")

        if not TWO_BEAT_RE.search(h1) and "." not in h1 and "—" not in h1:
            errors.append("h1 must be two-beat case (period or em-dash between beats)")

        for rx in HOW_TO_RES:
            if rx.search(h1):
                errors.append(f"h1 looks how-to/SEO, not case: {rx.pattern[:40]}")
                break

        for rx in LABEL_HEAD_RES:
            if rx.search(h1):
                errors.append(f"h1 label-head pattern: {rx.pattern[:40]}")
                break

        if h1.isupper() or sum(1 for c in h1 if c.isupper()) > 8:
            errors.append("h1 CAPS wall")

        for prev in published_h1s(article_dir):
            if prev and prev.casefold() == h1.casefold():
                errors.append("h1 duplicates published-titles-only.md entry")

    stamp = article_dir / "derouter-opus-stamp-title.json"
    if not stamp.is_file():
        errors.append("derouter-opus-stamp-title.json missing (title must use Derouter)")

    status = "PASS" if not errors else "BLOCK"
    return {
        "status": status,
        "stage": "title",
        "h1": h1,
        "errors": errors,
        "article_dir": str(article_dir),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Case delivery gate")
    parser.add_argument("--article-dir", required=True)
    parser.add_argument("--stage", required=True, choices=["title"])
    parser.add_argument("--json-out", help="Write gate result JSON next to article")
    args = parser.parse_args(argv)

    root = project_root()
    ad = Path(args.article_dir)
    if not ad.is_absolute():
        ad = root / ad

    if args.stage == "title":
        result = check_title_stage(ad)
    else:
        result = {"status": "BLOCK", "errors": [f"unknown stage {args.stage}"]}

    out_path = Path(args.json_out) if args.json_out else ad / "case-delivery-gate-title.json"
    if not out_path.is_absolute():
        out_path = root / out_path
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
