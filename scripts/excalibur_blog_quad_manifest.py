#!/usr/bin/env python3
"""Scaffold quad-manifest.json structure only — agent writes all prose.

Script may: pick visual_type from H2 keywords, wire slots/quadrants, preserve
agent fields on --merge, keep meme_caption_ru empty.

Script must NOT invent cover_hook, scene_hint, or alt. White hoodie / face lock
live in memory/cover/blog-hero.json + style prompts, not in scene_hint boilerplate.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from excalibur_blog_quad_slots import (
    CANVAS_1_SLOTS,
    active_inline_keys,
    all_canvas_specs,
    canvas_specs_for_inline_count,
    inline_count_from_tenant,
    uses_one_2k_slice4,
    uses_scene_poster_v2,
)

TYPE_PRIORITY = [
    "comparison_table_ui",
    "workflow_diagram",
    "checklist_board",
    "schema_faq_ui",
    "tool_screenshot",
    "infographic_card",
]
from excalibur_blog_quad_slots import DEFAULT_SLOT_MAP  # noqa: E402


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def extract_h2_titles(article_html: Path) -> list[str]:
    if not article_html.is_file():
        return []
    text = article_html.read_text(encoding="utf-8")
    titles: list[str] = []
    for match in re.finditer(r"<h2[^>]*>(.*?)</h2>", text, flags=re.I | re.S):
        title = re.sub(r"<[^>]+>", "", match.group(1))
        title = re.sub(r"\s+", " ", title).strip()
        if not title:
            continue
        if title.lower() in {"частые вопросы", "faq"}:
            break
        titles.append(title)
    return titles


def score_type(h2: str, type_def: dict) -> int:
    hay = h2.lower()
    score = 0
    for kw in type_def.get("keywords") or []:
        if kw.strip().lower() in hay:
            score += 2
    return score


def pick_visual_type(h2: str, types_catalog: dict, used: set[str]) -> str:
    types = types_catalog.get("types") or {}
    scored: list[tuple[int, str]] = []
    for type_id, type_def in types.items():
        scored.append((score_type(h2, type_def), type_id))
    scored.sort(key=lambda item: (-item[0], TYPE_PRIORITY.index(item[1]) if item[1] in TYPE_PRIORITY else 99))
    for score, type_id in scored:
        if score > 0 and type_id not in used:
            return type_id
    for type_id in TYPE_PRIORITY:
        if type_id not in used:
            return type_id
    return TYPE_PRIORITY[0]


def _load_tenant_inline_count(root: Path, preserve: dict | None) -> int:
    if preserve and preserve.get("inline_count") in (3, 7):
        return int(preserve["inline_count"])
    tenant_path = root / "shared/tenant-config.json"
    tenant = load_json(tenant_path) if tenant_path.is_file() else {}
    return inline_count_from_tenant(tenant)


def build_manifest(article_dir: Path, root: Path, preserve: dict | None) -> dict[str, Any]:
    meta_path = article_dir / "article.meta.json"
    meta = load_json(meta_path) if meta_path.is_file() else {}
    types_catalog = load_json(root / "memory/cover/inline-visual-types.json")
    h2s = extract_h2_titles(article_dir / "article.html")
    inline_count = _load_tenant_inline_count(root, preserve)
    inline_keys = active_inline_keys(inline_count)
    min_h2 = len(inline_keys)
    if len(h2s) < min_h2:
        raise ValueError(
            f"article needs at least {min_h2} real H2 anchors for "
            f"inline-01..{inline_count:02d}; found {len(h2s)}"
        )
    topic_id = meta.get("topic_id") or article_dir.name.split("-")[0]

    old_cover = ((preserve or {}).get("slots") or {}).get("cover") or {}
    # cover-text.json (Cover-text agent) owns the exact Russian inscriptions.
    cover_text_path = article_dir / "cover" / "cover-text.json"
    cover_text = load_json(cover_text_path) if cover_text_path.is_file() else {}
    ct_labels = cover_text.get("inline_labels") or {}
    # Prose fields: preserve agent text only. Never invent scene_hint/alt/hook.
    cover = {
        "quadrant": "top_left",
        "role": "cover_editorial_hero",
        "alt": str(old_cover.get("alt") or "").strip(),
        "scene_hint": str(old_cover.get("scene_hint") or "").strip(),
        "meme_caption_ru": "",
        "sticky": str(cover_text.get("sticky") or old_cover.get("sticky") or "").strip(),
    }

    used: set[str] = set()
    slots: dict[str, Any] = {"cover": cover}
    for idx, slot_key in enumerate(inline_keys, start=1):
        h2 = h2s[idx - 1] if idx - 1 < len(h2s) else f"Секция {idx}"
        old = ((preserve or {}).get("slots") or {}).get(slot_key) or {}
        visual_type = str(old.get("visual_type") or "").strip() or pick_visual_type(
            h2, types_catalog, used
        )
        used.add(visual_type)
        labels = ct_labels.get(slot_key) or old.get("labels") or []
        slots[slot_key] = {
            "quadrant": DEFAULT_SLOT_MAP[slot_key],
            "h2_anchor": old.get("h2_anchor") or h2,
            "visual_type": visual_type,
            "scene_hint": str(old.get("scene_hint") or "").strip(),
            "alt": str(old.get("alt") or "").strip(),
            "labels": [str(x).strip() for x in labels if str(x).strip()],
        }

    hook = (
        str(cover_text.get("hook") or "").strip()
        or str((preserve or {}).get("cover_hook") or "").strip()
    )
    highlight = (
        str(cover_text.get("highlight") or "").strip()
        or str((preserve or {}).get("cover_hook_highlight") or "").strip()
    )

    scene_v2 = uses_scene_poster_v2(root)
    if uses_one_2k_slice4(root) or scene_v2:
        canvas_specs = all_canvas_specs(inline_count)
    else:
        canvas_specs = canvas_specs_for_inline_count(inline_count)
    pipeline = (
        "quad_canvas_2x_image_api_longform"
        if inline_count == 7
        else ("slice4_grid_1x_image_api" if uses_one_2k_slice4(root) else "quad_canvas_1x_image_api")
    )
    style_file = str(
        (preserve or {}).get("style_file")
        or "memory/cover/quad-style-dobry-dom.json"
    )
    # Точные строки заголовка обложки и носитель надписи (граффити/бумага/экран) —
    # владеет Cover-text; manifest только переносит их в prompt builder.
    headline_fields: dict[str, str] = {}
    for key in ("cover_headline_line1", "cover_headline_line2", "cover_headline_line3", "cover_headline_medium"):
        value = str(cover_text.get(key) or (preserve or {}).get(key) or "").strip()
        if value:
            headline_fields[key] = value

    return {
        "topic_id": topic_id,
        **headline_fields,
        "canvas_file": canvas_specs[0]["canvas_file"],
        "layout": "2x2",
        "pipeline": pipeline,
        "inline_count": inline_count,
        "canvases": [
            {
                "index": spec["index"],
                "canvas_file": spec["canvas_file"],
                "batch_file": spec["batch_file"],
                "prompt_file": spec["prompt_file"],
                "result_file": spec["result_file"],
                "slots": list(spec["slots"]),
                "has_cover": bool(spec.get("has_cover")),
            }
            for spec in canvas_specs
        ],
        "style_preset": "the_rieltor_twilight_gold",
        "style_file": style_file,
        "blog_hero": "memory/cover/blog-hero.json",
        "inline_types_catalog": "memory/cover/inline-visual-types.json",
        "cover_hook": hook,
        "cover_hook_highlight": highlight,
        "cover_hook_contract": "shared/blog-cover-quad-canvas-contract.md",
        "mcp_note": (
            "PRIMARY: Derouter REST (DEROUTER_API_KEY) — 2K 16:9, one job per canvas "
            f"({len(canvas_specs)}×). Cover agent invents cover_hook + scene_hint/alt "
            "before --write-batch. Host lock = blog-hero.json (navy blazer, not hoodie)."
        ),
        "slots": slots,
        "cover_keys_ru": list((preserve or {}).get("cover_keys_ru") or []),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--out", default="cover/quad-manifest.json")
    ap.add_argument("--merge", action="store_true")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = article_dir / out_path

    preserve = load_json(out_path) if args.merge and out_path.is_file() else None
    try:
        manifest = build_manifest(article_dir, root, preserve)
    except ValueError as exc:
        print(f"❌ QUAD MANIFEST BLOCKER: {exc}", file=sys.stderr)
        return 1
    out_path.parent.mkdir(parents=True, exist_ok=True)
    save_json(out_path, manifest)
    print(f"OK manifest={out_path}")
    missing = []
    if not manifest.get("cover_hook"):
        missing.append("cover_hook")
    slot_keys = ("cover",) + active_inline_keys(manifest.get("inline_count") or 7)
    for key in slot_keys:
        slot = manifest["slots"][key]
        if not slot.get("scene_hint"):
            missing.append(f"{key}.scene_hint")
        if not slot.get("alt"):
            missing.append(f"{key}.alt")
    if missing:
        print(
            "WARN agent must invent before image API: " + ", ".join(missing),
            file=sys.stderr,
        )
    for key in active_inline_keys(manifest.get("inline_count") or 7):
        s = manifest["slots"][key]
        print(f"  {key}: {s['visual_type']} -> {s['h2_anchor']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
