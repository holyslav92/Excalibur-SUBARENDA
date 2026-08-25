#!/usr/bin/env python3
"""Validate description-brief.json — Dzen card teaser after Sol."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


CYRILLIC_RE = re.compile(r"[А-Яа-яЁё]")
TAG_RE = re.compile(r"<[^>]+>")
FORBIDDEN_AUTHOR_RE = re.compile(
    r"шакин|the\s*риэлтор|история\s+святослава",
    re.IGNORECASE,
)
BRAND_PRICE_RE = re.compile(r"добр\w*\s+дом", re.IGNORECASE)
PRICE_LADDER_RE = re.compile(
    r"\d{3,5}\s*(?:₽|руб\.?)?\s*(?:→|->|—>|–>| стало | выходит | преврат)",
    re.IGNORECASE,
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def strip_html(text: str) -> str:
    return " ".join(TAG_RE.sub(" ", text or "").split())


def first_paragraphs_text(article_path: Path, count: int = 2) -> str:
    if not article_path.is_file():
        return ""
    raw = article_path.read_text(encoding="utf-8")
    paragraphs: list[str] = []
    for match in re.finditer(r"<p[^>]*>(.*?)</p>", raw, flags=re.IGNORECASE | re.DOTALL):
        text = strip_html(match.group(1))
        if text:
            paragraphs.append(text)
        if len(paragraphs) >= count:
            break
    return " ".join(paragraphs)


def normalize(text: str) -> str:
    return " ".join(str(text or "").casefold().split())


def description_og_factory_errors(description: str) -> list[str]:
    """OG/description factory rules (Добрый дом)."""
    errors: list[str] = []
    if not description:
        return errors
    if FORBIDDEN_AUTHOR_RE.search(description):
        errors.append(
            "description must not mention Шакин / The Риэлтор "
            "(author = Добрый дом; live bug: «история Святослава Шакина»)"
        )
    if BRAND_PRICE_RE.search(description) and re.search(r"\d{3,5}", description):
        errors.append(
            "description must not pair «Добрый дом» with ₽ amounts "
            "(guest-burn arithmetic as brand price; e.g. «у Доброго дома … 2500 … 6500»)"
        )
    prices = re.findall(r"\b\d{3,5}\b", description)
    if len(set(prices)) >= 2 and (
        PRICE_LADDER_RE.search(description)
        or re.search(r"по\s+\d{3,5}", description, re.I)
    ):
        errors.append(
            "description must not use guest-burn price arithmetic in og:description "
            "(e.g. 2500→6500 as if it is Добрый дом's own price)"
        )
    return errors


def validate_description_brief(article_dir: Path) -> dict:
    errors: list[str] = []
    brief_path = article_dir / "description-brief.json"
    title_path = article_dir / "title-brief.json"
    article_path = article_dir / "article.html"

    if not brief_path.is_file():
        return {"status": "FAIL", "errors": ["description-brief.json missing"]}

    try:
        data = json.loads(brief_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"status": "FAIL", "errors": [f"description-brief.json invalid JSON: {exc}"]}

    description = str(data.get("description") or "").strip()
    if not description:
        errors.append("description empty")
    elif len(description) < 40:
        errors.append(f"description too short ({len(description)} chars, min 40)")
    elif len(description) > 250:
        errors.append(f"description too long ({len(description)} chars, max 250)")
    if description and not CYRILLIC_RE.search(description):
        errors.append("description must contain Cyrillic")

    errors.extend(description_og_factory_errors(description))

    title_h1 = ""
    if title_path.is_file():
        try:
            title_data = json.loads(title_path.read_text(encoding="utf-8"))
            title_h1 = str(title_data.get("h1") or title_data.get("title") or "").strip()
        except json.JSONDecodeError:
            errors.append("title-brief.json invalid JSON")
    else:
        errors.append("title-brief.json missing")

    if title_h1 and description and normalize(description) == normalize(title_h1):
        errors.append("description must not equal title/h1")

    lead = first_paragraphs_text(article_path, 2)
    if lead and description:
        norm_desc = normalize(description)
        norm_lead = normalize(lead)
        if norm_desc in norm_lead or norm_lead.startswith(norm_desc[: min(60, len(norm_desc))]):
            errors.append("description looks like truncated lead (double card)")
        first_p = first_paragraphs_text(article_path, 1)
        if first_p and normalize(description).startswith(normalize(first_p)[:40]):
            errors.append("description must not repeat article opening paragraph")

    verdict = str(data.get("verdict") or "").strip().upper()
    status = "PASS" if not errors else "FAIL"
    return {
        "status": status,
        "verdict": verdict or status,
        "errors": errors,
        "description_chars": len(description),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Description brief gate for Dzen card teaser")
    parser.add_argument("--article-dir", help="Article directory to validate")
    parser.add_argument("--doctor", action="store_true", help="Repo-level doctor check")
    args = parser.parse_args()
    root = project_root()

    if args.doctor:
        rules = root / "shared/dzen-description-rules.md"
        if not rules.is_file():
            print("FAIL dzen-description-rules.md missing", file=sys.stderr)
            return 1
        print("OK dzen-description-rules.md exists")
        return 0

    if not args.article_dir:
        print("FAIL --article-dir required", file=sys.stderr)
        return 1
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    result = validate_description_brief(article_dir)
    if result["status"] != "PASS":
        print(f"FAIL DESCRIPTION GATE: {'; '.join(result['errors'])}", file=sys.stderr)
        return 1
    print(f"OK description-brief ({result['description_chars']} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
