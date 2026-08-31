#!/usr/bin/env python3
"""Cover collage/meme gates for scene_poster_v2 — FAIL accidental collage covers."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np


def np_array_rgb(image_path: Path) -> np.ndarray:
    from PIL import Image

    with Image.open(image_path) as img:
        return np.asarray(img.convert("RGB"))


def detect_split_white_collage(image_path: Path) -> dict[str, Any]:
    """FAIL: hard vertical split — bright white left panel + photo right (legacy wow_poster)."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    if w < 200 or h < 100:
        return {"detected": False, "reason": "too_small"}

    split_x = int(w * 0.38)
    left = arr[:, :split_x]
    right = arr[:, split_x:]
    left_luma = left.mean(axis=2)
    right_luma = right.mean(axis=2)
    left_white_frac = float((left_luma > 240).mean())
    right_white_frac = float((right_luma > 240).mean())
    left_std = float(left_luma.std())
    right_std = float(right_luma.std())

    detected = (
        left_white_frac > 0.55
        and right_white_frac < 0.35
        and left_std < 45
        and right_std > 25
        and split_x > int(w * 0.28)
        and split_x < int(w * 0.52)
    )
    return {
        "detected": detected,
        "left_white_frac": round(left_white_frac, 3),
        "right_white_frac": round(right_white_frac, 3),
        "left_std": round(left_std, 2),
        "right_std": round(right_std, 2),
        "split_x": split_x,
    }


def detect_cover_meme_sticker_zone(image_path: Path) -> dict[str, Any]:
    """FAIL: high-contrast cutout sticker in bottom-left meme zone."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    zone = arr[int(h * 0.62) :, : int(w * 0.28)]
    if zone.size == 0:
        return {"detected": False, "reason": "empty_zone"}

    luma = zone.mean(axis=2)
    color_std = zone.std(axis=(0, 1)).mean()
    edge_energy = float(np.abs(np.diff(luma, axis=1)).mean()) if luma.shape[1] > 2 else 0.0
    dark_frac = float((luma < 80).mean())
    bright_frac = float((luma > 220).mean())

    detected = edge_energy > 18 and color_std > 35 and (dark_frac > 0.08 or bright_frac > 0.12)
    return {
        "detected": detected,
        "edge_energy": round(edge_energy, 2),
        "color_std": round(float(color_std), 2),
        "dark_frac": round(dark_frac, 3),
        "bright_frac": round(bright_frac, 3),
    }


def detect_scene_poster_pass(image_path: Path) -> dict[str, Any]:
    """PASS heuristic: full-bleed scene — not split collage, no meme zone."""
    split = detect_split_white_collage(image_path)
    meme = detect_cover_meme_sticker_zone(image_path)
    pass_scene = not split.get("detected") and not meme.get("detected")
    return {
        "pass": pass_scene,
        "split_white_collage": split,
        "meme_sticker_zone": meme,
    }


def validate_cover_scene_poster_gates(cover_path: Path) -> list[str]:
    errors: list[str] = []
    if not cover_path.is_file():
        return errors

    split = detect_split_white_collage(cover_path)
    if split.get("detected"):
        errors.append(
            "cover.png: split white-panel collage detected "
            f"(left_white={split.get('left_white_frac')}) — regenerate as full-bleed scene poster"
        )

    meme = detect_cover_meme_sticker_zone(cover_path)
    if meme.get("detected"):
        errors.append(
            "cover.png: meme/sticker cutout zone detected bottom-left "
            f"(edge={meme.get('edge_energy')}) — memes forbidden on cover"
        )

    return errors
