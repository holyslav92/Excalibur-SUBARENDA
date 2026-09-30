#!/usr/bin/env python3
"""Topic repeat detection for ViralDzen angle vs live Добрый дом posts."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from excalibur_blog_editorial_anti_clone import (
    RECENT_LIVE_COUNT,
    _load_recent_live,
    detect_wound_families,
    first_n_words,
)

BLOCKLIST_PATH = "shared/viral-topic-repeat-blocklist.json"
HANDOFF_NAME = "viral-dzen-handoff.json"


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").casefold()).strip()


def _pattern_hits(text: str, patterns: list[str]) -> list[str]:
    low = _norm(text)
    hits = [p for p in patterns if p.casefold() in low]
    return hits


def load_blocklist(root: Path) -> list[dict[str, Any]]:
    path = root / BLOCKLIST_PATH
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data.get("committed_live_wounds") or [])


def probe_text_from_article_dir(root: Path, article_dir: Path | None) -> str:
    chunks: list[str] = []
    if article_dir is not None:
        ad = article_dir if article_dir.is_absolute() else root / article_dir
        handoff_path = ad / HANDOFF_NAME
        if handoff_path.is_file():
            handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
            chunks.append(str(handoff.get("guest_angle_ru") or ""))
            chunks.append(str(handoff.get("tyumen_wound_hint") or ""))
            src = handoff.get("viral_source") or {}
            chunks.append(str(src.get("title") or ""))
        title_brief = ad / "title-brief.json"
        if title_brief.is_file():
            brief = json.loads(title_brief.read_text(encoding="utf-8"))
            chunks.append(str(brief.get("h1") or brief.get("title") or ""))
        art = ad / "article.html"
        if art.is_file():
            from excalibur_blog_editorial_anti_clone import _plain

            chunks.append(_plain(art.read_text(encoding="utf-8"))[:500])
    return " ".join(chunks)


def check_blocklist_signatures(root: Path, text: str) -> list[str]:
    errors: list[str] = []
    for entry in load_blocklist(root):
        patterns = [str(p) for p in (entry.get("patterns") or [])]
        min_hits = int(entry.get("min_pattern_hits") or 2)
        hits = _pattern_hits(text, patterns)
        if len(hits) >= min_hits:
            errors.append(
                f"viral-topic-repeat: blocklist {entry.get('id')} "
                f"({len(hits)} pattern hits: {', '.join(hits[:5])})"
            )
    return errors


def check_near_duplicate_h1(root: Path, text: str, *, limit: int = RECENT_LIVE_COUNT) -> list[str]:
    errors: list[str] = []
    probe_words = first_n_words(text, 6)
    if len(probe_words.split()) < 4:
        return errors
    for row in _load_recent_live(root, limit=limit):
        live_h1 = row.get("h1") or ""
        live_open = row.get("opening") or ""
        for candidate in (live_h1, live_open[:200]):
            if not candidate:
                continue
            if first_n_words(candidate, 6) == probe_words:
                errors.append(
                    f"viral-topic-repeat: first-6-words match live slug={row.get('slug')}"
                )
                return errors
    return errors


def check_wound_family_saturation(root: Path, text: str, *, limit: int = RECENT_LIVE_COUNT) -> list[str]:
    errors: list[str] = []
    probe_families = detect_wound_families(text)
    if not probe_families:
        return errors
    recent = _load_recent_live(root, limit=limit)
    saturated: set[str] = set()
    for row in recent:
        saturated |= detect_wound_families((row.get("h1") or "") + " " + (row.get("opening") or ""))
    overlap = probe_families & saturated
    if len(overlap) >= 2:
        errors.append(
            f"viral-topic-repeat: wound families overlap recent live ({', '.join(sorted(overlap))})"
        )
    return errors


def check_topic_repeat(
    root: Path,
    text: str,
    *,
    article_dir: Path | None = None,
) -> list[str]:
    if not text.strip():
        if article_dir is not None:
            text = probe_text_from_article_dir(root, article_dir)
    if not text.strip():
        return ["viral-topic-repeat: empty probe text"]
    errors: list[str] = []
    errors.extend(check_blocklist_signatures(root, text))
    errors.extend(check_near_duplicate_h1(root, text))
    errors.extend(check_wound_family_saturation(root, text))
    return errors
