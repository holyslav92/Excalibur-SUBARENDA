#!/usr/bin/env python3
"""HARD gate: daily-rental CASE delivery — block how-to H1, TOC openings, thin leads.

Checks title-brief.json (after Title), drafts/writer.html (after Writer),
article.html (after Sol). Cron/slots cannot ship encyclopedia guides.

Klyshin TG (30.08.2026): two-beat stop-factor H1; §1 = smooth holyslav paragraphs
(quote-first, no duty-log date/clock stamp); short vertical ladder lines are BAN in opening only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from excalibur_blog_opening_meta_gate import (
    CLOCK_RE,
    _is_chopped_lead,
    _is_duty_log_lead,
    _opening_duty_slice,
)


def _plain(html: str) -> str:
    text = re.sub(r"<script[^>]*>.*?</script>", " ", html or "", flags=re.I | re.S)
    text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# How-to / guide H1 skeleton — HARD FAIL on Title.
HOW_TO_H1_RES = (
    re.compile(r"\bкак\s+снять\b", re.I),
    re.compile(r"\bкак\s+арендовать\b", re.I),
    re.compile(r"\bчто\s+проверить\b", re.I),
    re.compile(r"\bчто\s+делать\s+если\b", re.I),
    re.compile(r"\bразбер[её]м\b", re.I),
    re.compile(r"\bлучш(ие|ий|ая|ую|их)\b", re.I),
    re.compile(r"\bполный\s+гайд\b", re.I),
    re.compile(r"\bтоп[-\s]?10\b", re.I),
    re.compile(r"\bинструкция\s+по\b", re.I),
    re.compile(r"\bгайд\s+по\b", re.I),
    re.compile(r"\bпошагов\w*\b", re.I),
    re.compile(r"\bсоветы\s+по\b", re.I),
    re.compile(r"\bчек[-\s]?лист\s+(для|по)\b", re.I),
    re.compile(
        r"\b\d+\s+(совет\w*|шаг\w*|вопрос\w*|способ\w*|правил\w*)\b",
        re.I,
    ),
    re.compile(r"\bseo\b", re.I),
    re.compile(r"\.{3}\s*$"),
)

TOPIC_LABEL_H1_RE = re.compile(
    r"^(?:о|об|про|всё\s+о)\s+[\w«\"]",
    re.I,
)

TWO_BEAT_MARKERS = (
    re.compile(r"\.\s+\S"),
    re.compile(r"—\s*\S"),
    re.compile(r":\s*\S"),
    re.compile(r"\?\s*\S"),
    re.compile(r"!\s+\S"),
    re.compile(r"\bа\s+потом\b", re.I),
    re.compile(r"\bтолько\b", re.I),
    re.compile(r"\bпохоже,\s*да\b", re.I),
    re.compile(r"\bне\s+значит\b", re.I),
    re.compile(r"\bпока\s+вы\b", re.I),
)

# TOC / guide opening — HARD FAIL on Writer/Sol body opening.
TOC_OPENING_RES = (
    re.compile(r"\bразбер[её]м\b", re.I),
    re.compile(r"\bв\s+этой\s+статье\b", re.I),
    re.compile(r"\bсодержание\b", re.I),
    re.compile(r"\bоглавление\b", re.I),
    re.compile(r"\btl;dr\b", re.I),
    re.compile(r"\bбыстрый\s+инсайт\b", re.I),
    re.compile(r"\bчто\s+проверить\s+первым\b", re.I),
    re.compile(r"\bкратко\s*:\s*", re.I),
    re.compile(r"\bсписок\s+проверок\b", re.I),
)

DATE_TIME_RE = re.compile(
    r"(?:"
    r"\b\d{1,2}\s+(?:январ|феврал|март|апрел|ма[йя]|июн|июл|август|сентябр|октябр|ноябр|декабр)\w*\b"
    r"|\b\d{1,2}[./]\d{1,2}(?:[./]\d{2,4})?\b"
    r"|\b\d{1,2}:\d{2}\b"
    r"|\b(?:первый|второй|третий)\s+день\b"
    r"|\b\d{1,2}\s+ноч"
    r")",
    re.I,
)

# Legacy anchor kept for body-timeline detection only — NOT required in opening.

QUOTE_RE = re.compile(r"[«\"][^»\"]{4,}[»\"]")

MONEY_NIGHTS_RE = re.compile(
    r"(?:"
    r"\d[\d\s]*\s*(?:₽|руб\.?)"
    r"|\d+\s*₽"
    r"|\bзалог\s+\d"
    r"|\b\d+\s+ноч"
    r"|\b\d+\s+минут"
    r")",
    re.I,
)

ILLUSION_BREAK_RE = re.compile(
    r"(?:"
    r"нет\.\s+так\s+не"
    r"|была\.\s+и\s+(?:она\s+)?не\s+соврал"
    r"|так\s+не\s+(?:работает|заселяем|отвечаем|переводим)"
    r"|обещание\s+было"
    r"|не\s+наоборот"
    r"|даже\s+за\s+двойную"
    r")",
    re.I,
)

COMMENT_BAIT_RE = re.compile(r"напиш\w*\s+в\s+комментар", re.I)

# Host-operator / realtor plots — audience is GUEST booking a night.
HOST_OPERATOR_RE = (
    re.compile(r"загрузк\w*\s*%", re.I),
    re.compile(r"\boccupancy\b", re.I),
    re.compile(r"процент\s+заполн", re.I),
    re.compile(r"\badr\b", re.I),
    re.compile(r"как\s+хост\s+увелич", re.I),
    re.compile(r"сдайте\s+квартиру", re.I),
    re.compile(r"гость\s+съехал", re.I),
)

REALTOR_BLOCKED_RE = (
    re.compile(r"\bегрн\b", re.I),
    re.compile(r"\bнаследств", re.I),
    re.compile(r"\bипотек", re.I),
    re.compile(r"\bнотариус", re.I),
    re.compile(r"\bшакин", re.I),
    re.compile(r"tymenrieltor", re.I),
    re.compile(r"\+7\s*922\s*001\s*65\s*05", re.I),
    re.compile(r"\+79032334201", re.I),
    re.compile(r"\bклышин\b", re.I),
)


def check_h1(h1: str) -> list[str]:
    errors: list[str] = []
    title = (h1 or "").strip()
    if not title:
        errors.append("h1: empty")
        return errors
    if title == title.upper() and len(title) > 12:
        errors.append("h1: ALL CAPS clickbait")
    length = len(title)
    if length < 28:
        errors.append(f"h1: too short ({length} chars; Dzen CASE needs ~40–70)")
    if length > 85:
        errors.append(f"h1: too long ({length} chars; max ~70)")
    low = title.casefold()
    if TOPIC_LABEL_H1_RE.match(title):
        errors.append("h1: topic label («О проверке…») — need two-beat stop-factor CASE")
    for rx in HOW_TO_H1_RES:
        if rx.search(low):
            errors.append(f"h1: how-to skeleton")
            break
    if re.search(r"\bкак\s+", low) and re.search(r"\bснять\b", low):
        errors.append("h1: how-to «как снять»")
    if CLOCK_RE.search(title):
        errors.append(
            "h1: clock time (HH:MM) — use story words («Утром её уже сдали»), not dispatch log"
        )
    if not any(rx.search(title) for rx in TWO_BEAT_MARKERS):
        errors.append(
            "h1: missing two-beat stop-factor "
            "(clause break: . — : ? ! «А потом» «Только» contrast)"
        )
    return errors


def _opening_slice(html: str, *, max_chars: int = 1600) -> str:
    raw = html or ""
    paras = re.findall(r"<p[^>]*>(.*?)</p>", raw, flags=re.I | re.S)
    if paras:
        joined = " ".join(_plain(p) for p in paras[:3])
        return joined[:max_chars]
    return _plain(raw)[:max_chars]


def _raw_opening_head(html: str, *, max_chars: int = 2000) -> str:
    return (html or "")[:max_chars]


def check_opening_body(html: str, *, label: str) -> list[str]:
    errors: list[str] = []
    opening = _opening_slice(html)
    raw_head = _raw_opening_head(html)
    if not opening or len(opening.split()) < 25:
        errors.append(f"{label}: opening too thin for dense CASE (need 1–2 full paragraphs)")
    low = opening.casefold()
    for rx in TOC_OPENING_RES:
        if rx.search(low):
            errors.append(f"{label}: TOC/guide opener")
            break
    if re.search(r"^\s*1\.\s", opening, re.M) or re.search(
        r"<ol[^>]*>", raw_head, re.I
    ):
        errors.append(f"{label}: numbered list opening (checklist spine, not CASE)")
    if _is_chopped_lead(opening) or _is_chopped_lead(raw_head):
        errors.append(
            f"{label}: chopped TG-cosplay lead — need 1–2 dense paragraphs, not 8+ short lines"
        )
    duty_slice = _opening_duty_slice(opening) or _opening_duty_slice(raw_head)
    if _is_duty_log_lead(opening) or _is_duty_log_lead(raw_head) or _is_duty_log_lead(duty_slice):
        errors.append(
            f"{label}: duty-log / clock-stamp lead "
            "(smooth holyslav quote-first opening; no weekday/date/clock in §1)"
        )
    if not QUOTE_RE.search(opening):
        errors.append(f"{label}: opening missing host/guest quote")
    if not MONEY_NIGHTS_RE.search(opening):
        errors.append(f"{label}: opening missing ₽/nights/minutes figure")
    if not ILLUSION_BREAK_RE.search(opening):
        errors.append(f"{label}: opening missing illusion-break beat")
    if COMMENT_BAIT_RE.search(low):
        errors.append(f"{label}: WP comment bait — send readers to TG/MAX")
    return errors


def check_body_timeline(html: str, *, label: str) -> list[str]:
    """Ban body-as-timeline spine (multiple HH:MM stamps through the piece)."""
    plain = _plain(html)
    clocks = CLOCK_RE.findall(plain)
    if len(clocks) >= 3:
        return [
            f"{label}: body-as-timeline spine ({len(clocks)} clock stamps) "
            "— one red line through the case, not dispatch log"
        ]
    return []


def check_audience_and_bans(html: str, *, label: str) -> list[str]:
    errors: list[str] = []
    low = (html or "").casefold()
    for rx in HOST_OPERATOR_RE:
        if rx.search(low):
            errors.append(f"{label}: host-operator plot — audience is GUEST booking a night")
            break
    for rx in REALTOR_BLOCKED_RE:
        if rx.search(low):
            errors.append(f"{label}: banned realtor/Klyshin plot or contact")
            break
    return errors


def count_words(html: str) -> int:
    return len(_plain(html).split())


def check_word_count(
    html: str, *, label: str, min_words: int = 1000, max_words: int = 1950
) -> list[str]:
    wc = count_words(html)
    errors: list[str] = []
    if wc < min_words:
        errors.append(f"{label}: too short ({wc} words; CASE target 1100–1800)")
    if wc > max_words:
        errors.append(
            f"{label}: too long ({wc} words; CASE target 1100–1800, not encyclopedia)"
        )
    return errors


def check_identity(html: str, *, label: str) -> list[str]:
    low = (html or "").casefold()
    if "хост посуточной" not in low and "добрый дом" not in low:
        return [
            f"{label}: missing identity line "
            "(«Я хост посуточной в Тюмени. Это «Добрый дом».»)"
        ]
    return []


def check_article_dir(article_dir: Path, *, stage: str = "all") -> dict[str, Any]:
    errors: list[str] = []
    checks_run: list[str] = []

    title_path = article_dir / "title-brief.json"
    if stage in {"all", "title"} and title_path.is_file():
        checks_run.append("title-brief")
        try:
            brief = json.loads(title_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append("title-brief.json: invalid JSON")
            brief = {}
        h1 = str(brief.get("h1") or brief.get("title") or "").strip()
        for err in check_h1(h1):
            errors.append(f"title-brief.json: {err}")

    writer_path = article_dir / "drafts" / "writer.html"
    if stage in {"all", "writer", "article"} and writer_path.is_file():
        checks_run.append("writer.html")
        writer_html = writer_path.read_text(encoding="utf-8")
        errors.extend(check_opening_body(writer_html, label="writer.html"))
        errors.extend(check_body_timeline(writer_html, label="writer.html"))
        errors.extend(check_audience_and_bans(writer_html, label="writer.html"))
        if stage in {"all", "writer"}:
            errors.extend(check_identity(writer_html, label="writer.html"))
        if COMMENT_BAIT_RE.search(writer_html):
            errors.append("writer.html: WP comment bait — use TG/MAX")

    html_path = article_dir / "article.html"
    if stage in {"all", "article"} and html_path.is_file():
        checks_run.append("article.html")
        article_html = html_path.read_text(encoding="utf-8")
        errors.extend(check_opening_body(article_html, label="article.html"))
        errors.extend(check_body_timeline(article_html, label="article.html"))
        errors.extend(check_audience_and_bans(article_html, label="article.html"))
        errors.extend(check_identity(article_html, label="article.html"))
        errors.extend(check_word_count(article_html, label="article.html"))
        if COMMENT_BAIT_RE.search(article_html):
            errors.append("article.html: WP comment bait — use TG/MAX")
        meta_path = article_dir / "article.meta.json"
        if meta_path.is_file():
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
                meta_h1 = str(meta.get("h1") or meta.get("title") or "").strip()
                for err in check_h1(meta_h1):
                    errors.append(f"article.meta.json: {err}")
            except json.JSONDecodeError:
                errors.append("article.meta.json: invalid JSON")

    status = "PASS" if not errors else "BLOCK"
    return {
        "gate": "case-delivery",
        "status": status,
        "stage": stage,
        "checks_run": checks_run,
        "errors": errors,
        "article_dir": str(article_dir),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", type=Path, required=True)
    ap.add_argument(
        "--stage",
        choices=("all", "title", "writer", "article"),
        default="all",
        help="title=after Title; writer=after Writer; article=after Sol; all=whatever exists",
    )
    ap.add_argument("-o", "--output", type=str, default="case-delivery-gate.json")
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    if not article_dir.is_dir():
        print(f"BLOCKER: article-dir not found: {article_dir}", file=sys.stderr)
        return 2
    report = check_article_dir(article_dir, stage=args.stage)
    out_path = article_dir / Path(args.output).name
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
