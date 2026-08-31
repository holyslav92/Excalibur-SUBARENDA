#!/usr/bin/env python3
"""Cover meme rotation: topic-tag overlap pick, skip last N used ids."""

from __future__ import annotations

import argparse
import json
import os
import re
from datetime import date
from pathlib import Path

MEME_CATALOG_REL = "memory/cover/meme-top100.json"
MEME_USED_REL = "memory/cover/meme-used.json"
MEME_ASSETS_DIR = "memory/cover/memes"
DEFAULT_ROTATION_WINDOW = 8

TOPIC_TAG_KEYWORDS: dict[str, tuple[str, ...]] = {
    "pets": ("лап", "собак", "животн", "pet", "кот", "кошк", "paw", "dog", "cat"),
    "money": ("₽", "руб", "цен", "оплат", "деньг", "дорог", "бюджет", "счёт", "чек"),
    "extra-fee": ("доплат", "нацен", "сверх", "extra fee", "3000", "скрыт"),
    "betrayal": ("обман", "не верн", "предат", "сказали", "обещал", "врань"),
    "surprise": ("внезап", "после засел", "оказал", "неожид", "шок", "вскрыл"),
    "deal": ("снять", "брон", "посуточ", "аренд", "avito", "авито", "хозяин"),
    "keys": ("ключ", "код", "домофон", "keybox", "замок"),
    "check-in": ("засел", "заезд", "выезд", "check-in", "checkin", "self check"),
    "family": ("семь", "дет", "родител", "студент", "ребён"),
    "documents": ("паспорт", "договор", "документ", "скан", "фото паспорт"),
    "neighbors": ("сосед", "шум", "стуч", "подъезд", "двор"),
    "cleaning": ("уборк", "чист", "бель", "полотен", "housekeep"),
    "deposit": ("залог", "депозит", "задат", "удерж"),
}


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_meme_catalog(root: Path) -> dict:
    path = root / MEME_CATALOG_REL
    if not path.is_file():
        return {"entries": []}
    return load_json(path)


def load_meme_used(root: Path) -> dict:
    path = root / MEME_USED_REL
    if not path.is_file():
        return {
            "schema_version": 1,
            "rotation_window": DEFAULT_ROTATION_WINDOW,
            "recent_covers": [],
            "burned_for_article": {},
        }
    return load_json(path)


def topic_blob(manifest: dict) -> str:
    parts: list[str] = [
        str(manifest.get("topic_id") or ""),
        str(manifest.get("slug") or ""),
        str(manifest.get("cover_hook") or ""),
        str(manifest.get("cover_scene") or ""),
        str(manifest.get("cover_emotion") or ""),
        " ".join(str(x) for x in (manifest.get("cover_keys_ru") or [])),
        " ".join(str(x) for x in (manifest.get("wordstat_stickers") or [])),
    ]
    motifs = manifest.get("cover_motifs") or {}
    for key in ("composition", "location", "meme", "prop_set", "sticker_set", "joke"):
        value = motifs.get(key)
        if isinstance(value, list):
            parts.append(" ".join(str(x) for x in value))
        else:
            parts.append(str(value or ""))
    slots = manifest.get("slots") or {}
    for key in ("cover", "inline_1", "inline_2", "inline_3", "inline_4", "inline_5", "inline_6", "inline_7"):
        slot = slots.get(key) or {}
        parts.append(str(slot.get("h2_anchor") or ""))
        parts.append(str(slot.get("scene_hint") or ""))
        parts.append(str(slot.get("sticky") or ""))
    return " ".join(parts).casefold()


def infer_topic_tags(manifest: dict) -> set[str]:
    blob = topic_blob(manifest)
    tags: set[str] = set()
    for tag, keywords in TOPIC_TAG_KEYWORDS.items():
        if any(keyword in blob for keyword in keywords):
            tags.add(tag)
    if not tags:
        tags.add("deal")
    return tags


def recent_used_ids(used_log: dict, *, window: int | None = None) -> set[str]:
    window = window or int(used_log.get("rotation_window") or DEFAULT_ROTATION_WINDOW)
    ids: list[str] = []
    for row in used_log.get("recent_covers") or []:
        meme_id = str((row or {}).get("meme_id") or "").strip()
        if meme_id:
            ids.append(meme_id.casefold())
    return {x for x in ids[-window:]}


def burned_for_topic(used_log: dict, manifest: dict) -> set[str]:
    topic_id = str(manifest.get("topic_id") or "").strip()
    burned: set[str] = set()
    mapping = used_log.get("burned_for_article") or {}
    if topic_id and isinstance(mapping, dict):
        for meme_id in mapping.get(topic_id) or []:
            burned.add(str(meme_id).casefold())
    slug = str(manifest.get("slug") or "").strip()
    if slug and isinstance(mapping, dict):
        for meme_id in mapping.get(slug) or []:
            burned.add(str(meme_id).casefold())
    return burned


def skip_ids(manifest: dict, used_log: dict) -> set[str]:
    return recent_used_ids(used_log) | burned_for_topic(used_log, manifest)


def entry_tags(entry: dict) -> set[str]:
    raw = entry.get("tags") or []
    return {str(tag).casefold() for tag in raw if str(tag).strip()}


def score_entry(entry: dict, topic_tags: set[str]) -> int:
    overlap = len(entry_tags(entry) & topic_tags)
    year = int(entry.get("era_year") or 0)
    # Prefer fresher memes on ties; stable sort by id for determinism.
    return overlap * 1000 + min(year, 2099)


def cover_candidates(catalog: dict, *, skip: set[str]) -> list[dict]:
    out: list[dict] = []
    for entry in catalog.get("entries") or []:
        category = str(entry.get("category") or "").casefold()
        entry_id = str(entry.get("id") or "").strip()
        if category in {"banned", ""} or not entry_id:
            continue
        if entry_id.casefold() in skip:
            continue
        allowed = [str(x).casefold() for x in (entry.get("allowed_on") or [])]
        if allowed and "cover" not in allowed:
            continue
        out.append(entry)
    return out


def resolve_meme_asset(root: Path, entry: dict) -> str:
    """Return relative asset path when a real file exists under memory/cover/memes/."""
    entry_id = str(entry.get("id") or "").strip()
    if not entry_id:
        return ""
    assets = root / MEME_ASSETS_DIR
    for name in (
        entry.get("asset_file"),
        f"{entry_id}.png",
        f"{entry_id}.jpg",
        f"{entry_id}.webp",
    ):
        if not name:
            continue
        path = assets / str(name)
        if path.is_file():
            return f"{MEME_ASSETS_DIR}/{path.name}"
    return ""


def pick_cover_meme(
    manifest: dict,
    catalog: dict,
    root: Path,
    *,
    used_log: dict | None = None,
) -> dict:
    """Pick one catalog meme for cover; never same face as last rotation_window covers."""
    used = used_log or load_meme_used(root)
    skip = skip_ids(manifest, used)
    cover_slot = (manifest.get("slots") or {}).get("cover") or {}
    explicit_id = str(cover_slot.get("meme_id") or (manifest.get("cover_motifs") or {}).get("meme_id") or "").strip()
    entries = {str(e.get("id") or ""): e for e in (catalog.get("entries") or [])}
    if explicit_id and explicit_id in entries and explicit_id.casefold() not in skip:
        entry = entries[explicit_id]
        return {
            "id": explicit_id,
            "name_ru": str(entry.get("name_ru") or explicit_id),
            "asset": resolve_meme_asset(root, entry),
            "picked_by": "manifest_explicit",
            "topic_tags": sorted(infer_topic_tags(manifest)),
        }

    topic_tags = infer_topic_tags(manifest)
    candidates = cover_candidates(catalog, skip=skip)
    if not candidates:
        candidates = cover_candidates(catalog, skip=set())
    if not candidates:
        return {
            "id": "wojak",
            "name_ru": "Wojak / Feels Guy",
            "asset": "",
            "picked_by": "fallback",
            "topic_tags": sorted(topic_tags),
        }
    ranked = sorted(
        candidates,
        key=lambda e: (-score_entry(e, topic_tags), str(e.get("id") or "")),
    )
    entry = ranked[0]
    entry_id = str(entry.get("id") or "")
    return {
        "id": entry_id,
        "name_ru": str(entry.get("name_ru") or entry_id),
        "asset": resolve_meme_asset(root, entry),
        "picked_by": "topic_tag_overlap",
        "topic_tags": sorted(topic_tags),
        "tag_overlap": len(entry_tags(entry) & topic_tags),
        "skipped_ids": sorted(skip),
    }


def record_cover_meme_used(
    root: Path,
    *,
    topic_id: str,
    slug: str,
    meme_id: str,
    when: str | None = None,
) -> None:
    path = root / MEME_USED_REL
    used = load_meme_used(root)
    row = {
        "date": when or date.today().isoformat(),
        "topic_id": topic_id,
        "slug": slug,
        "meme_id": meme_id,
    }
    recent = list(used.get("recent_covers") or [])
    recent.append(row)
    window = int(used.get("rotation_window") or DEFAULT_ROTATION_WINDOW)
    used["recent_covers"] = recent[-max(window * 3, 24) :]
    used["updated_at"] = date.today().isoformat()
    save_json(path, used)


def cmd_pick(root: Path, manifest_path: Path) -> int:
    manifest = load_json(manifest_path)
    catalog = load_meme_catalog(root)
    picked = pick_cover_meme(manifest, catalog, root)
    print(json.dumps(picked, ensure_ascii=False, indent=2))
    return 0


def cmd_record(root: Path, args: argparse.Namespace) -> int:
    record_cover_meme_used(
        root,
        topic_id=args.topic_id,
        slug=args.slug or "",
        meme_id=args.meme_id,
        when=args.date or None,
    )
    print(f"OK recorded meme_id={args.meme_id} topic_id={args.topic_id}")
    return 0


def cmd_doctor(root: Path) -> int:
    catalog = load_meme_catalog(root)
    entries = [e for e in (catalog.get("entries") or []) if str(e.get("category") or "") != "banned"]
    if len(entries) < 60:
        print(f"FAIL meme catalog has {len(entries)} usable entries, need ≥60", file=__import__("sys").stderr)
        return 1
    missing_tags = [str(e.get("id")) for e in entries if not e.get("tags")]
    if missing_tags:
        print(f"FAIL entries missing tags: {', '.join(missing_tags[:8])}", file=__import__("sys").stderr)
        return 1
    used_path = root / MEME_USED_REL
    if not used_path.is_file():
        print("FAIL meme-used.json missing", file=__import__("sys").stderr)
        return 1
    used = load_meme_used(root)
    if int(used.get("rotation_window") or 0) < 1:
        print("FAIL meme-used rotation_window invalid", file=__import__("sys").stderr)
        return 1
    print(f"OK meme rotation canon: {len(entries)} catalog entries, window={used.get('rotation_window')}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Cover meme rotation by topic tags")
    sub = parser.add_subparsers(dest="command", required=True)
    pick = sub.add_parser("pick", help="Pick meme for manifest")
    pick.add_argument("--manifest", required=True)
    record = sub.add_parser("record", help="Append meme id to recent_covers log")
    record.add_argument("--topic-id", required=True)
    record.add_argument("--slug", default="")
    record.add_argument("--meme-id", required=True)
    record.add_argument("--date", default="")
    sub.add_parser("doctor", help="Validate meme catalog + used log")
    args = parser.parse_args()
    root = project_root()
    if args.command == "pick":
        manifest_path = Path(args.manifest)
        if not manifest_path.is_absolute():
            manifest_path = root / manifest_path
        return cmd_pick(root, manifest_path)
    if args.command == "record":
        return cmd_record(root, args)
    if args.command == "doctor":
        return cmd_doctor(root)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
