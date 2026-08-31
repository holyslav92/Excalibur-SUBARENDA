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


def _rgb_to_hsv_numpy(arr: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    rgb = arr.astype("float32") / 255.0
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    cmax = np.max(rgb, axis=2)
    cmin = np.min(rgb, axis=2)
    delta = cmax - cmin

    hue = np.zeros_like(cmax)
    mask = delta > 1e-6
    rmask = mask & (cmax == r)
    gmask = mask & (cmax == g)
    bmask = mask & (cmax == b)
    hue[rmask] = ((g[rmask] - b[rmask]) / delta[rmask]) % 6.0
    hue[gmask] = ((b[gmask] - r[gmask]) / delta[gmask]) + 2.0
    hue[bmask] = ((r[bmask] - g[bmask]) / delta[bmask]) + 4.0
    hue = (hue / 6.0) * 360.0

    sat = np.zeros_like(cmax)
    sat[cmax > 1e-6] = delta[cmax > 1e-6] / cmax[cmax > 1e-6]
    val = cmax
    return hue, sat, val


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


def detect_empty_stock_room(image_path: Path) -> dict[str, Any]:
    """FAIL: timid empty stock — uniform mid-gray/white, almost no scene detail."""
    arr = np_array_rgb(image_path)
    luma = arr.mean(axis=2)
    hue, sat, _val = _rgb_to_hsv_numpy(arr)
    global_std = float(luma.std())
    low_sat_frac = float((sat < 0.12).mean())
    mid_band_frac = float(((luma > 165) & (luma < 235)).mean())
    edge_energy = float(np.abs(np.diff(luma, axis=1)).mean() + np.abs(np.diff(luma, axis=0)).mean())
    detected = global_std < 28 and low_sat_frac > 0.72 and mid_band_frac > 0.55 and edge_energy < 12
    return {
        "detected": detected,
        "global_std": round(global_std, 2),
        "low_sat_frac": round(low_sat_frac, 3),
        "mid_band_frac": round(mid_band_frac, 3),
        "edge_energy": round(edge_energy, 2),
    }


def detect_yellow_sticky_soup(image_path: Path) -> dict[str, Any]:
    """FAIL: multiple yellow sticky-note clusters (torn-paper/sticky collage soup)."""
    arr = np_array_rgb(image_path)
    hue, sat, val = _rgb_to_hsv_numpy(arr)
    yellow = (hue >= 38) & (hue <= 62) & (sat >= 0.28) & (val >= 0.45)
    yellow_frac = float(yellow.mean())
    h, w = arr.shape[:2]
    quadrants = [
        arr[: h // 2, : w // 2],
        arr[: h // 2, w // 2 :],
        arr[h // 2 :, : w // 2],
        arr[h // 2 :, w // 2 :],
    ]
    quad_hits = 0
    for quad in quadrants:
        qh, qs, qv = _rgb_to_hsv_numpy(quad)
        qy = (qh >= 38) & (qh <= 62) & (qs >= 0.28) & (qv >= 0.45)
        if float(qy.mean()) > 0.018:
            quad_hits += 1
    detected = yellow_frac > 0.035 and quad_hits >= 2
    return {
        "detected": detected,
        "yellow_frac": round(yellow_frac, 4),
        "quad_hits": quad_hits,
    }


def detect_torn_paper_edge_soup(image_path: Path) -> dict[str, Any]:
    """FAIL: high edge density on white field — torn-paper / tape collage energy."""
    arr = np_array_rgb(image_path)
    luma = arr.mean(axis=2)
    white_mask = luma > 235
    white_frac = float(white_mask.mean())
    if white_frac < 0.25:
        return {"detected": False, "reason": "not_white_heavy"}
    edges = np.abs(np.diff(luma, axis=1)).mean() + np.abs(np.diff(luma, axis=0)).mean()
    detected = white_frac > 0.38 and float(edges) > 22
    return {
        "detected": detected,
        "white_frac": round(white_frac, 3),
        "edge_energy": round(float(edges), 2),
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
    """COVER-only gates — inlines are not checked here."""
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

    empty = detect_empty_stock_room(cover_path)
    if empty.get("detected"):
        errors.append(
            "cover.png: empty stock room detected "
            f"(std={empty.get('global_std')}) — cover must be lived-in scene poster"
        )

    sticky = detect_yellow_sticky_soup(cover_path)
    if sticky.get("detected"):
        errors.append(
            "cover.png: yellow sticky-note soup detected "
            f"(yellow_frac={sticky.get('yellow_frac')}) — no torn-paper/sticky collage on cover"
        )

    torn = detect_torn_paper_edge_soup(cover_path)
    if torn.get("detected"):
        errors.append(
            "cover.png: torn-paper collage energy detected "
            f"(edge={torn.get('edge_energy')}) — cover must be cinematic scene, not sticker soup"
        )

    try:
        from excalibur_blog_drawn_logo_gate import (
            detect_drawn_lockup_in_image,
            detect_phone_pill_post_composite,
            detect_white_plate_in_pad,
        )

        pill = detect_phone_pill_post_composite(cover_path)
        if pill.get("detected"):
            errors.append(
                "cover.png: opaque phone pill detected "
                f"(area={pill.get('area_ratio')}) — phone must be in-scene, not post-composite pill"
            )

        plate = detect_white_plate_in_pad(cover_path)
        if plate.get("detected"):
            errors.append(
                "cover.png: logo plaque/plate detected in top-right pad "
                f"(kind={plate.get('plate_kind')}) — leave clean pad for factory logo paste"
            )
    except ImportError:
        errors.append("excalibur_blog_drawn_logo_gate.py missing — cover phone/plaque QA unavailable")

    return errors
