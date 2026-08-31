#!/usr/bin/env python3
"""Shared constants for Excalibur BLOG quad cover / inline slots."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

# Longform canon: standalone cover + 7 inline from 2 quad canvases (scene_poster_v2).
INLINE_SLOT_KEYS: tuple[str, ...] = tuple(f"inline_{i}" for i in range(1, 8))
INLINE_FILES: dict[str, str] = {key: f"inline-{i:02d}.png" for i, key in enumerate(INLINE_SLOT_KEYS, start=1)}

# Legacy wow_poster: cover in quad canvas 1 TL.
CANVAS_1_SLOTS: tuple[str, ...] = ("cover", "inline_1", "inline_2", "inline_3")
CANVAS_2_SLOTS: tuple[str, ...] = ("inline_4", "inline_5", "inline_6", "inline_7")

# scene_poster_v2: cover standalone; inlines only on quads.
SCENE_POSTER_CANVAS_1_SLOTS: tuple[str, ...] = ("inline_1", "inline_2", "inline_3", "inline_4")
SCENE_POSTER_CANVAS_2_SLOTS: tuple[str, ...] = ("inline_5", "inline_6", "inline_7", "panel_quiet_pad")
NON_EXPORT_SLOTS: frozenset[str] = frozenset({"panel_quiet_pad"})

DEFAULT_SLOT_MAP: dict[str, str] = {
    "cover": "top_left",
    "inline_1": "top_right",
    "inline_2": "bottom_left",
    "inline_3": "bottom_right",
    "inline_4": "top_left",
    "inline_5": "top_right",
    "inline_6": "bottom_left",
    "inline_7": "bottom_right",
}

SCENE_POSTER_SLOT_MAP: dict[str, str] = {
    "inline_1": "top_left",
    "inline_2": "top_right",
    "inline_3": "bottom_left",
    "inline_4": "bottom_right",
    "inline_5": "top_left",
    "inline_6": "top_right",
    "inline_7": "bottom_left",
    "panel_quiet_pad": "bottom_right",
}

STANDALONE_COVER_SPEC: dict[str, Any] = {
    "index": 0,
    "standalone_cover": True,
    "canvas_file": "cover/cover-canvas.png",
    "batch_file": "cover/cover-mcp-batch.json",
    "prompt_file": "cover/cover-mcp-prompt.txt",
    "result_file": "cover/cover-mcp-result.json",
    "slots": ("cover",),
    "has_cover": True,
    "export_size": "1200x675",
}

CANVAS_SPECS: tuple[dict[str, Any], ...] = (
    {
        "index": 1,
        "canvas_file": "cover/canvas-quad-01.png",
        "batch_file": "cover/quad-mcp-batch-01.json",
        "prompt_file": "cover/quad-mcp-prompt-01.txt",
        "result_file": "cover/quad-mcp-result-01.json",
        "slots": CANVAS_1_SLOTS,
        "has_cover": True,
    },
    {
        "index": 2,
        "canvas_file": "cover/canvas-quad-02.png",
        "batch_file": "cover/quad-mcp-batch-02.json",
        "prompt_file": "cover/quad-mcp-prompt-02.txt",
        "result_file": "cover/quad-mcp-result-02.json",
        "slots": CANVAS_2_SLOTS,
        "has_cover": False,
    },
)

SCENE_POSTER_CANVAS_SPECS: tuple[dict[str, Any], ...] = (
    {
        "index": 1,
        "canvas_file": "cover/canvas-quad-01.png",
        "batch_file": "cover/quad-mcp-batch-01.json",
        "prompt_file": "cover/quad-mcp-prompt-01.txt",
        "result_file": "cover/quad-mcp-result-01.json",
        "slots": SCENE_POSTER_CANVAS_1_SLOTS,
        "has_cover": False,
    },
    {
        "index": 2,
        "canvas_file": "cover/canvas-quad-02.png",
        "batch_file": "cover/quad-mcp-batch-02.json",
        "prompt_file": "cover/quad-mcp-prompt-02.txt",
        "result_file": "cover/quad-mcp-result-02.json",
        "slots": SCENE_POSTER_CANVAS_2_SLOTS,
        "has_cover": False,
    },
)

LEGACY_INLINE_SLOT_KEYS: tuple[str, ...] = ("inline_1", "inline_2", "inline_3")
LEGACY_CANVAS_FILE = "cover/canvas-quad.png"
LEGACY_BATCH_FILE = "cover/quad-mcp-batch.json"
LEGACY_RESULT_FILE = "cover/quad-mcp-result.json"

SCENE_POSTER_CANON_ID = "dobry_dom_scene_poster_v2"


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_cover_canon_id(root: Path | None = None) -> str:
    root = root or project_root()
    path = root / "memory/cover/cover-canon.json"
    if not path.is_file():
        return ""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ""
    return str(data.get("canon_id") or "").strip()


def uses_scene_poster_v2(root: Path | None = None) -> bool:
    return load_cover_canon_id(root) == SCENE_POSTER_CANON_ID


def slot_map_for_mode(*, scene_poster_v2: bool) -> dict[str, str]:
    return dict(SCENE_POSTER_SLOT_MAP if scene_poster_v2 else DEFAULT_SLOT_MAP)


def exportable_slots(slot_keys: tuple[str, ...] | list[str]) -> tuple[str, ...]:
    return tuple(k for k in slot_keys if k not in NON_EXPORT_SLOTS)


def inline_count_from_manifest(manifest: dict[str, Any] | None) -> int:
    if not manifest:
        return 7
    if manifest.get("inline_count") in (3, 7):
        return int(manifest["inline_count"])
    canvases = manifest.get("canvases")
    if isinstance(canvases, list) and canvases:
        return 7
    pipeline = str(manifest.get("pipeline") or "")
    if "longform" in pipeline or "2x" in pipeline or "scene_poster" in pipeline:
        return 7
    return 3


def inline_count_from_tenant(tenant: dict[str, Any] | None) -> int:
    if not tenant:
        return 7
    if tenant.get("inline_image_count") in (3, 7):
        return int(tenant["inline_image_count"])
    if str(tenant.get("publish_format") or "").casefold() == "longform":
        return 7
    if str(tenant.get("publish_format") or "").casefold() == "daily":
        return 0
    return 7


def active_inline_keys(inline_count: int) -> tuple[str, ...]:
    if inline_count <= 0:
        return ()
    if inline_count == 3:
        return LEGACY_INLINE_SLOT_KEYS
    return INLINE_SLOT_KEYS[:inline_count]


def canvas_specs_for_inline_count(
    inline_count: int,
    *,
    scene_poster_v2: bool | None = None,
) -> tuple[dict[str, Any], ...]:
    v2 = uses_scene_poster_v2() if scene_poster_v2 is None else scene_poster_v2
    if inline_count == 3:
        return (
            {
                "index": 1,
                "canvas_file": LEGACY_CANVAS_FILE,
                "batch_file": LEGACY_BATCH_FILE,
                "prompt_file": "cover/quad-mcp-prompt.txt",
                "result_file": LEGACY_RESULT_FILE,
                "slots": CANVAS_1_SLOTS,
                "has_cover": True,
            },
        )
    if v2:
        return SCENE_POSTER_CANVAS_SPECS
    return CANVAS_SPECS


def all_canvas_specs(inline_count: int, *, scene_poster_v2: bool | None = None) -> tuple[dict[str, Any], ...]:
    v2 = uses_scene_poster_v2() if scene_poster_v2 is None else scene_poster_v2
    if inline_count == 7 and v2:
        return (STANDALONE_COVER_SPEC,) + SCENE_POSTER_CANVAS_SPECS
    return canvas_specs_for_inline_count(inline_count, scene_poster_v2=v2)


def all_split_slot_keys(inline_count: int, *, scene_poster_v2: bool | None = None) -> tuple[str, ...]:
    v2 = uses_scene_poster_v2() if scene_poster_v2 is None else scene_poster_v2
    if inline_count == 3:
        return CANVAS_1_SLOTS
    if inline_count == 7 and v2:
        return ("cover",) + active_inline_keys(inline_count)
    if inline_count == 7:
        return CANVAS_1_SLOTS + CANVAS_2_SLOTS
    return ("cover",) + active_inline_keys(inline_count)
