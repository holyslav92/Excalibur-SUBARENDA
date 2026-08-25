#!/usr/bin/env python3
"""Cat-meme quota gate: max 1 cat-meme slot per article (cover + 7 inlines)."""

from __future__ import annotations

import json
import re
from pathlib import Path

# Единое семейство для anti-repeat 14д: любой cat-meme = одна коллизия.
CAT_MEME_FAMILY_TOKEN = "__cat_meme_family__"

_CAT_TEXT_PATTERNS = (
    re.compile(r"\bcat\b", re.IGNORECASE),
    re.compile(r"\bкот(?:ик|а|ы)?\b", re.IGNORECASE),
    re.compile(r"\bкошк", re.IGNORECASE),
    re.compile(r"grumpy\s*cat|tardar", re.IGNORECASE),
    re.compile(r"smudge|table\s*cat", re.IGNORECASE),
    re.compile(r"nyan\s*cat|pop\s*cat|keyboard\s*cat|long\s*cat", re.IGNORECASE),
    re.compile(r"cheems|doge|shiba", re.IGNORECASE),
    re.compile(r"meme[\s-]*cat|cat[\s-]*sticker|cat[\s-]*meme", re.IGNORECASE),
    re.compile(r"tabby|ginger\s*cat", re.IGNORECASE),
    re.compile(r"crying\s*cat|polite\s*cat", re.IGNORECASE),
    re.compile(r"surprised\s*tom", re.IGNORECASE),
    re.compile(r"capybara|nihilist\s*penguin", re.IGNORECASE),
)


def load_meme_catalog(root: Path) -> dict:
    path = root / "memory" / "cover" / "meme-top100.json"
    if not path.is_file():
        return {"entries": []}
    return json.loads(path.read_text(encoding="utf-8"))


def cat_meme_entry_ids(catalog: dict) -> set[str]:
    ids: set[str] = set()
    for entry in catalog.get("entries") or []:
        if str(entry.get("category") or "").casefold() == "cat":
            entry_id = str(entry.get("id") or "").strip()
            if entry_id:
                ids.add(entry_id.casefold())
    return ids


def is_cat_meme_text(text: str) -> bool:
    normalized = " ".join(str(text or "").casefold().split())
    if not normalized:
        return False
    return any(pattern.search(normalized) for pattern in _CAT_TEXT_PATTERNS)


def is_cat_meme_entry(entry_id: str, catalog: dict) -> bool:
    needle = str(entry_id or "").strip().casefold()
    if not needle:
        return False
    return needle in cat_meme_entry_ids(catalog)


def normalize_meme_for_antirepeat(value: str, catalog: dict | None = None) -> str:
    """Любой cat-meme сводится к одному токену семейства для 14д anti-repeat."""
    text = " ".join(str(value or "").casefold().split())
    if not text:
        return ""
    entry_id = ""
    if catalog and ":" in text:
        prefix, _, suffix = text.partition(":")
        if prefix.strip().casefold() in cat_meme_entry_ids(catalog):
            return CAT_MEME_FAMILY_TOKEN
        entry_id = suffix.strip()
    if entry_id and is_cat_meme_entry(entry_id, catalog or {}):
        return CAT_MEME_FAMILY_TOKEN
    if is_cat_meme_text(text):
        return CAT_MEME_FAMILY_TOKEN
    return text


def slot_has_cat_meme(slot_key: str, slot: dict, manifest: dict, catalog: dict) -> bool:
    meme_id = str(slot.get("meme_id") or "").strip()
    if meme_id and is_cat_meme_entry(meme_id, catalog):
        return True

    texts: list[str] = []
    if slot_key == "cover":
        motifs = manifest.get("cover_motifs") or {}
        texts.append(str(motifs.get("meme") or ""))
        texts.append(str(motifs.get("joke") or ""))
    if slot.get("meme_sticker"):
        texts.append(str(slot.get("meme_sticker_hint") or "meme sticker"))
        if meme_id:
            texts.append(meme_id)
    texts.append(str(slot.get("scene_hint") or ""))
    texts.append(str(slot.get("meme") or ""))
    return any(is_cat_meme_text(text) for text in texts if text)


def count_cat_meme_slots(manifest: dict, catalog: dict) -> tuple[int, list[str]]:
    slots = manifest.get("slots") or {}
    hits: list[str] = []
    for key in ("cover", "inline_1", "inline_2", "inline_3", "inline_4", "inline_5", "inline_6", "inline_7"):
        slot = slots.get(key) or {}
        if slot_has_cat_meme(key, slot, manifest, catalog):
            hits.append(key)
    return len(hits), hits


def validate_max_one_cat_meme(manifest: dict, catalog: dict, *, max_slots: int = 1) -> list[str]:
    count, hits = count_cat_meme_slots(manifest, catalog)
    if count <= max_slots:
        return []
    return [
        f"cat-meme quota exceeded: {count} slots {hits} (max {max_slots} across cover+7 inlines)"
    ]


def pick_non_cat_meme_hint(catalog: dict, *, used_ids: set[str] | None = None) -> str:
    """Подсказка для промпта: people-meme из каталога (не cat)."""
    used = {x.casefold() for x in (used_ids or set())}
    people: list[dict] = []
    for entry in catalog.get("entries") or []:
        category = str(entry.get("category") or "").casefold()
        entry_id = str(entry.get("id") or "").strip()
        if category != "people" or not entry_id:
            continue
        if entry_id.casefold() in used:
            continue
        people.append(entry)
    if not people:
        return "Roll Safe / Hide the Pain Harold / Pepe reaction sticker ≤12%"
    entry = people[0]
    name = str(entry.get("name_ru") or entry.get("id") or "people-meme")
    return f"{name} tiny sticker ≤12% from meme-top100.json"
