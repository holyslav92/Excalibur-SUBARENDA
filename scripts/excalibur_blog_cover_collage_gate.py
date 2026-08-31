#!/usr/bin/env python3
"""Cover gates for dobry_dom_type_meme_sticker_v3 — type+meme+phone-sticker poster."""

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


def _meme_zone_energy(zone: np.ndarray) -> dict[str, Any]:
    if zone.size == 0:
        return {"detected": False, "reason": "empty_zone"}

    luma = zone.mean(axis=2)
    color_std = float(zone.std(axis=(0, 1)).mean())
    edge_energy = float(np.abs(np.diff(luma, axis=1)).mean()) if luma.shape[1] > 2 else 0.0
    edge_energy += float(np.abs(np.diff(luma, axis=0)).mean()) if luma.shape[0] > 2 else 0.0
    dark_frac = float((luma < 80).mean())
    bright_frac = float((luma > 220).mean())

    detected = edge_energy > 16 and color_std > 32 and (dark_frac > 0.06 or bright_frac > 0.10)
    return {
        "detected": detected,
        "edge_energy": round(edge_energy, 2),
        "color_std": round(color_std, 2),
        "dark_frac": round(dark_frac, 3),
        "bright_frac": round(bright_frac, 3),
    }


def detect_meme_sticker_zones(image_path: Path) -> dict[str, Any]:
    """Detect high-contrast cutout sticker energy in corner zones (cover v3 requires ≥1)."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    zones = {
        "bottom_left": arr[int(h * 0.55) :, : int(w * 0.32)],
        "bottom_right": arr[int(h * 0.55) :, int(w * 0.68) :],
        "top_left": arr[: int(h * 0.42), : int(w * 0.32)],
        "top_right_pad_adjacent": arr[: int(h * 0.42), int(w * 0.58) : int(w * 0.82)],
    }
    hits: list[str] = []
    details: dict[str, Any] = {}
    for name, zone in zones.items():
        result = _meme_zone_energy(zone)
        details[name] = result
        if result.get("detected"):
            hits.append(name)
    return {"count": len(hits), "hits": hits, "zones": details}


def detect_cover_meme_sticker_zone(image_path: Path) -> dict[str, Any]:
    """Backward-compat alias — bottom-left zone only."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    zone = arr[int(h * 0.62) :, : int(w * 0.28)]
    result = _meme_zone_energy(zone)
    result["detected"] = bool(result.get("detected"))
    return result


def detect_display_headline(image_path: Path) -> dict[str, Any]:
    """PASS heuristic: spectacular display headline — dark typography energy in top band."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    top = arr[: int(h * 0.40), : int(w * 0.92)]
    if top.size == 0:
        return {"detected": False, "reason": "empty_top"}

    luma = top.mean(axis=2)
    dark_frac = float((luma < 95).mean())
    edge_h = float(np.abs(np.diff(luma, axis=1)).mean()) if luma.shape[1] > 2 else 0.0
    edge_v = float(np.abs(np.diff(luma, axis=0)).mean()) if luma.shape[0] > 2 else 0.0
    edge_energy = edge_h + edge_v
    luma_std = float(luma.std())

    detected = dark_frac >= 0.035 and edge_energy >= 12 and luma_std >= 22
    return {
        "detected": detected,
        "dark_frac": round(dark_frac, 4),
        "edge_energy": round(edge_energy, 2),
        "luma_std": round(luma_std, 2),
    }


def detect_large_phone_sticker(image_path: Path) -> dict[str, Any]:
    """PASS heuristic: LARGE die-cut phone sticker — bright/colorful block, not tiny in-scene text."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    # Search lower 55% and side margins — sticker is a designed graphic, not headline band.
    band = arr[int(h * 0.38) :, :]
    if band.size == 0:
        return {"detected": False, "reason": "empty_band"}

    gray = band.mean(axis=2)
    hue, sat, val = _rgb_to_hsv_numpy(band)
    # Sticker: saturated OR high-contrast rectangular patch with sufficient area.
    colorful = (sat > 0.22) & (val > 0.35)
    high_contrast = gray > 200
    candidate = colorful | high_contrast

    min_area = int(w * h * 0.012)
    visited = np.zeros(candidate.shape, dtype=bool)
    best_area = 0
    best_bbox = (0, 0, 0, 0)

    rows, cols = candidate.shape
    for y in range(0, rows, 4):
        for x in range(0, cols, 4):
            if not candidate[y, x] or visited[y, x]:
                continue
            stack = [(y, x)]
            area = 0
            x0 = x1 = x
            y0 = y1 = y
            while stack:
                cy, cx = stack.pop()
                if cy < 0 or cy >= rows or cx < 0 or cx >= cols:
                    continue
                if visited[cy, cx] or not candidate[cy, cx]:
                    continue
                visited[cy, cx] = True
                area += 1
                x0, x1 = min(x0, cx), max(x1, cx)
                y0, y1 = min(y0, cy), max(y1, cy)
                stack.extend([(cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)])
            if area > best_area:
                best_area = area
                best_bbox = (x0, y0, x1, y1)

    bbox_w = max(1, best_bbox[2] - best_bbox[0])
    bbox_h = max(1, best_bbox[3] - best_bbox[1])
    area_ratio = best_area / max(w * h, 1)
    aspect = bbox_w / bbox_h
    detected = best_area >= min_area and area_ratio >= 0.012 and 1.8 <= aspect <= 9.0
    return {
        "detected": detected,
        "area_ratio": round(area_ratio, 4),
        "aspect": round(aspect, 2),
        "best_area": best_area,
        "bbox": best_bbox,
    }


def detect_people_heavy_scene(image_path: Path) -> dict[str, Any]:
    """FAIL: flesh/skin-tone clusters occupying large center — people-heavy scene photo."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    center = arr[int(h * 0.12) : int(h * 0.88), int(w * 0.10) : int(w * 0.90)]
    hue, sat, val = _rgb_to_hsv_numpy(center)
    # Skin-ish hues with moderate saturation.
    skin = ((hue < 45) | (hue > 330)) & (sat > 0.12) & (sat < 0.65) & (val > 0.25) & (val < 0.92)
    skin_frac = float(skin.mean())
    # Secondary: high local variance blobs (crowd/photo texture).
    luma = center.mean(axis=2)
    texture = float(luma.std())
    detected = skin_frac > 0.11 and texture > 28
    return {
        "detected": detected,
        "skin_frac": round(skin_frac, 4),
        "texture_std": round(texture, 2),
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


def detect_type_meme_sticker_pass(image_path: Path) -> dict[str, Any]:
    """PASS heuristic: type-led poster with headline + meme + large phone sticker."""
    headline = detect_display_headline(image_path)
    meme = detect_meme_sticker_zones(image_path)
    phone = detect_large_phone_sticker(image_path)
    people = detect_people_heavy_scene(image_path)
    split = detect_split_white_collage(image_path)
    pass_v3 = (
        headline.get("detected")
        and meme.get("count", 0) >= 1
        and meme.get("count", 0) <= 1
        and phone.get("detected")
        and not people.get("detected")
        and not split.get("detected")
    )
    return {
        "pass": pass_v3,
        "headline": headline,
        "meme_zones": meme,
        "phone_sticker": phone,
        "people_heavy": people,
        "split_white_collage": split,
    }


def validate_cover_type_meme_sticker_gates(cover_path: Path) -> list[str]:
    """COVER-only gates for dobry_dom_type_meme_sticker_v3."""
    errors: list[str] = []
    if not cover_path.is_file():
        return errors

    split = detect_split_white_collage(cover_path)
    if split.get("detected"):
        errors.append(
            "cover.png: split white-panel collage detected "
            f"(left_white={split.get('left_white_frac')}) — regenerate as type-led poster, not split collage"
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
            f"(edge={torn.get('edge_energy')}) — cover must be designed type poster, not sticker soup"
        )

    headline = detect_display_headline(cover_path)
    if not headline.get("detected"):
        errors.append(
            "cover.png: missing spectacular display headline typography "
            f"(dark_frac={headline.get('dark_frac')}, edge={headline.get('edge_energy')})"
        )

    meme = detect_meme_sticker_zones(cover_path)
    if meme.get("count", 0) < 1:
        errors.append(
            "cover.png: missing required catalog meme sticker on cover "
            f"(zones={meme.get('hits')}) — exactly ONE meme from meme-top100.json required"
        )
    elif meme.get("count", 0) > 1:
        errors.append(
            "cover.png: meme soup — more than one meme sticker zone detected "
            f"(hits={meme.get('hits')}) — exactly ONE meme allowed on cover"
        )

    phone = detect_large_phone_sticker(cover_path)
    if not phone.get("detected"):
        errors.append(
            "cover.png: missing LARGE die-cut phone sticker "
            f"(area_ratio={phone.get('area_ratio')}) — phone must be big designed graphic, not tiny in-scene number"
        )

    people = detect_people_heavy_scene(cover_path)
    if people.get("detected"):
        errors.append(
            "cover.png: people-heavy scene photo detected "
            f"(skin_frac={people.get('skin_frac')}) — cover must be type-led poster, default zero people"
        )

    empty = detect_empty_stock_room(cover_path)
    if empty.get("detected") and not headline.get("detected"):
        errors.append(
            "cover.png: empty stock room detected "
            f"(std={empty.get('global_std')}) — cover must be designed type poster with headline"
        )

    try:
        from excalibur_blog_drawn_logo_gate import (
            detect_phone_pill_post_composite,
            detect_white_plate_in_pad,
        )

        pill = detect_phone_pill_post_composite(cover_path)
        if pill.get("detected") and not phone.get("detected"):
            errors.append(
                "cover.png: opaque phone pill detected "
                f"(area={pill.get('area_ratio')}) — phone must be LARGE die-cut sticker, not beige/gray UI pill"
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


# Backward-compatible aliases (scene_poster_v2 gates inverted → v3)
validate_cover_scene_poster_gates = validate_cover_type_meme_sticker_gates
detect_scene_poster_pass = detect_type_meme_sticker_pass
