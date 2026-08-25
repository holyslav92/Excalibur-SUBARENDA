#!/usr/bin/env python3
"""Block research-brief / API-calque junk in article opening + meta description.

Opening lives in article.html (Writer). Optional orphan lead.md is scanned
if present; missing file is OK.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


# Calque of "API" that reads as machine Russian, not Lebedev.
STYK_API_RE = re.compile(
    r"стык(?:а|у|ом|е|и)?\s+(?:для\s+программ|с\s+(?:сайтом|api)|с\s+api)"
    r"|без\s+(?:готового\s+)?стыка"
    r"|где\s+стыка\s+нет"
    r"|открытого\s+стыка",
    re.IGNORECASE,
)

# Pipeline / research brief leaking into public text.
RESEARCH_BRIEF_RES = (
    re.compile(r"факты\s+запуска", re.I),
    re.compile(r"оговорк[аиуеы]\s+пресс", re.I),
    re.compile(r"смотрите\s+на\s+факты", re.I),
    re.compile(r"не\s+путайте\s+с\s+готовым", re.I),
    re.compile(r"VentureBeat\s+просит", re.I),
    re.compile(r"сверять\s+поколение", re.I),
    re.compile(r"reader_outcome|reader_problem|WORDSTAT|research_date", re.I),
    re.compile(r"^\s*\d{1,2}\s+[а-яё]+\s+20\d{2}\b", re.I | re.M),
    re.compile(r"^\s*\d{2}\.\d{2}\.20\d{2}\b", re.M),
)


def _plain(text: str) -> str:
    return re.sub(r"<[^>]+>", " ", text or "")


def _hits(text: str) -> list[str]:
    found: list[str] = []
    if STYK_API_RE.search(text):
        found.append("api-calque-styk")
    for rx in RESEARCH_BRIEF_RES:
        m = rx.search(text)
        if m:
            found.append(f"research-brief:{m.group(0)[:48]}")
    return found


# Telegram-cosplay / chopped 3-word line spam instead of dense CASE lead.
CHOPPED_TIME_CITY_RE = re.compile(
    r"^\s*\d{1,2}:\d{2}\.\s+\S+[.!]\s+\S+[.!]",
    re.M,
)


def _is_chopped_lead(text: str) -> bool:
    """True when opening is rubbled short lines instead of 1–2 dense case paragraphs."""
    head = (text or "").strip()
    if not head:
        return False
    lines = [ln.strip() for ln in re.split(r"[\n\r]+", head) if ln.strip()]
    if len(lines) >= 6:
        sample = lines[:12]
        short = sum(1 for ln in sample if len(ln.split()) <= 4)
        if short >= 5 and short / len(sample) >= 0.6:
            return True
    if CHOPPED_TIME_CITY_RE.search(head):
        return True
    # HTML: many tiny <p> one-liners in opening
    paras = re.findall(r"<p[^>]*>(.*?)</p>", head, flags=re.I | re.S)
    if len(paras) >= 6:
        plain_paras = [_plain(p).strip() for p in paras[:12] if _plain(p).strip()]
        if len(plain_paras) >= 6:
            short_p = sum(1 for p in plain_paras if len(p.split()) <= 4)
            if short_p >= 5 and short_p / len(plain_paras) >= 0.6:
                return True
    return False


def check_article(article_dir: Path) -> dict[str, Any]:
    errors: list[str] = []
    orphan_lead = article_dir / "lead.md"
    meta_path = article_dir / "article.meta.json"
    html_path = article_dir / "article.html"

    if orphan_lead.is_file():
        lead = _plain(orphan_lead.read_text(encoding="utf-8"))
        for h in _hits(lead):
            errors.append(f"lead.md: {h}")

    meta: dict[str, Any] = {}
    if meta_path.is_file():
        try:
            loaded = json.loads(meta_path.read_text(encoding="utf-8"))
            meta = loaded if isinstance(loaded, dict) else {}
        except json.JSONDecodeError:
            errors.append("article.meta.json: invalid JSON")
            meta = {}
        blobs = [
            str(meta.get("description") or ""),
            str((meta.get("meta_ab") or {}).get("description_seo") or ""),
            str((meta.get("meta_ab") or {}).get("description_ctr") or ""),
            str((meta.get("meta_ab") or {}).get("description_aeo") or ""),
            str(meta.get("cover_hook") or ""),
        ]
        for i, blob in enumerate(blobs):
            for h in _hits(blob):
                errors.append(f"article.meta.json[{i}]: {h}")
    else:
        errors.append("article.meta.json missing")

    if html_path.is_file():
        raw_html = html_path.read_text(encoding="utf-8")
        html = _plain(raw_html)
        head = html[:900]
        raw_head = raw_html[:1400]
        for h in _hits(head):
            errors.append(f"article.html-head: {h}")
        if _is_chopped_lead(head) or _is_chopped_lead(raw_head):
            errors.append("article.html-head: chopped-lead (dense CASE paragraph required)")
        if STYK_API_RE.search(html):
            errors.append("article.html: api-calque-styk")
    else:
        errors.append("article.html missing")

    status = "PASS" if not errors else "BLOCK"
    return {
        "gate": "opening-meta",
        "status": status,
        "errors": errors,
        "article_dir": str(article_dir),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", type=Path, required=True)
    ap.add_argument("-o", "--output", type=str, default="opening-meta-gate.json")
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    if not article_dir.is_dir():
        print(f"BLOCKER: article-dir not found: {article_dir}", file=sys.stderr)
        return 2
    report = check_article(article_dir)
    out_name = Path(args.output).name
    out_path = article_dir / out_name
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
