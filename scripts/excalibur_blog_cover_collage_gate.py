#!/usr/bin/env python3
"""Cover gates — dzen_story_collage_v1 anti-collage + factory type overlay poster."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

# HARD factory thresholds (dobry_dom_dzen_story_collage_v1)
GIANT_GLYPH_CANVAS_FRAC = 0.12
TEXT_BLOCK_MIN_CANVAS_FRAC = 0.04
TEXT_BLOCK_OVERLAP_IOU = 0.18
TRADE_OFFER_SPLIT_BAND = (0.38, 0.62)
MODEL_MEME_SKIN_FRAC = 0.055
SCENE_ONLY_MAX_TEXT_EDGE = 14.0
SCENE_ONLY_MAX_DARK_UPPER = 0.028


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

def detect_metallic_gold_dominance(image_path: Path) -> dict[str, Any]:
    """FAIL: metallic gold / brass / 3D gold type energy in upper frame."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    zone = arr[: int(h * 0.55), :]
    hue, sat, val = _rgb_to_hsv_numpy(zone)
    # Gold/brass band: yellow-orange hue, high saturation, mid-high value
    gold_mask = (hue >= 28) & (hue <= 58) & (sat > 0.35) & (val > 0.45)
    gold_frac = float(gold_mask.mean())
    detected = gold_frac > 0.045
    return {"detected": detected, "gold_frac": round(gold_frac, 4)}


def detect_dark_leather_dominance(image_path: Path) -> dict[str, Any]:
    """FAIL: dark leather / noir brown dominance (tender-light uses cream/oatmeal)."""
    arr = np_array_rgb(image_path)
    luma = arr.mean(axis=2)
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    brown = (r > g) & (g > b) & (luma < 95)
    dark_frac = float((luma < 80).mean())
    leather_frac = float(brown.mean())
    detected = dark_frac > 0.22 or leather_frac > 0.18
    return {
        "detected": detected,
        "dark_frac": round(dark_frac, 4),
        "leather_frac": round(leather_frac, 4),
    }


def detect_gold_brass_phone_plaque(image_path: Path) -> dict[str, Any]:
    """FAIL: gold/brass realtor plaque instead of cream/sage info board."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    # Phone/taboo zones: center-right and bottom-right lower half
    zone = arr[int(h * 0.35) :, int(w * 0.45) :]
    hue, sat, val = _rgb_to_hsv_numpy(zone)
    brass = (hue >= 25) & (hue <= 55) & (sat > 0.4) & (val > 0.35)
    brass_frac = float(brass.mean())
    detected = brass_frac > 0.06
    return {"detected": detected, "brass_frac": round(brass_frac, 4)}


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

    detected = (
        dark_frac >= 0.035 and luma_std >= 22 and (edge_energy >= 12 or dark_frac >= 0.08)
    ) or (
        edge_energy >= 16 and luma_std >= 24 and dark_frac >= 0.006
    ) or (
        dark_frac >= 0.045 and luma_std >= 30 and edge_energy >= 3.5
    )
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


def _connected_bbox(mask: np.ndarray, *, min_area: int) -> tuple[int, int, int, int, int] | None:
    """Largest connected component bbox (x0,y0,x1,y1,area) on bool mask."""
    if mask.size == 0:
        return None
    visited = np.zeros(mask.shape, dtype=bool)
    rows, cols = mask.shape
    best: tuple[int, int, int, int, int] | None = None
    for y in range(0, rows, 3):
        for x in range(0, cols, 3):
            if not mask[y, x] or visited[y, x]:
                continue
            stack = [(y, x)]
            area = 0
            x0 = x1 = x
            y0 = y1 = y
            while stack:
                cy, cx = stack.pop()
                if cy < 0 or cy >= rows or cx < 0 or cx >= cols:
                    continue
                if visited[cy, cx] or not mask[cy, cx]:
                    continue
                visited[cy, cx] = True
                area += 1
                x0, x1 = min(x0, cx), max(x1, cx)
                y0, y1 = min(y0, cy), max(y1, cy)
                stack.extend([(cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)])
            if area >= min_area and (best is None or area > best[4]):
                best = (x0, y0, x1 + 1, y1 + 1, area)
    return best


def _bbox_iou(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> float:
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    ix0, iy0 = max(ax0, bx0), max(ay0, by0)
    ix1, iy1 = min(ax1, bx1), min(ay1, by1)
    if ix1 <= ix0 or iy1 <= iy0:
        return 0.0
    inter = (ix1 - ix0) * (iy1 - iy0)
    area_a = max(1, (ax1 - ax0) * (ay1 - ay0))
    area_b = max(1, (bx1 - bx0) * (by1 - by0))
    return inter / max(1.0, area_a + area_b - inter)


def _text_like_regions(arr: np.ndarray, *, canvas_area: int) -> list[dict[str, Any]]:
    """Heuristic text-block blobs: dark rectangular patches with boundary edge energy."""
    h, w = arr.shape[:2]
    luma = arr.mean(axis=2)
    edge_h = np.abs(np.diff(luma, axis=1, prepend=luma[:, :1]))
    edge_v = np.abs(np.diff(luma, axis=0, prepend=luma[:1, :]))
    edge = edge_h + edge_v
    dark = luma < 120
    min_area = int(canvas_area * TEXT_BLOCK_MIN_CANVAS_FRAC)
    regions: list[dict[str, Any]] = []
    visited = np.zeros(dark.shape, dtype=bool)
    for y in range(0, h, 3):
        for x in range(0, w, 3):
            if not dark[y, x] or visited[y, x]:
                continue
            stack = [(y, x)]
            area = 0
            x0 = x1 = x
            y0 = y1 = y
            boundary_edge = 0.0
            while stack:
                cy, cx = stack.pop()
                if cy < 0 or cy >= h or cx < 0 or cx >= w:
                    continue
                if visited[cy, cx] or not dark[cy, cx]:
                    continue
                visited[cy, cx] = True
                area += 1
                x0, x1 = min(x0, cx), max(x1, cx)
                y0, y1 = min(y0, cy), max(y1, cy)
                boundary_edge = max(boundary_edge, float(edge[cy, cx]))
                stack.extend([(cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)])
            if area >= min_area and boundary_edge >= 10:
                regions.append(
                    {
                        "bbox": (x0, y0, x1 + 1, y1 + 1),
                        "area": area,
                        "area_frac": round(area / max(canvas_area, 1), 4),
                        "boundary_edge": round(boundary_edge, 2),
                    }
                )
    return regions


def detect_stacked_type_layers(image_path: Path) -> dict[str, Any]:
    """FAIL: 2+ horizontal dark typography bands stacked in top frame (overlapping type layers)."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    top = arr[: int(h * 0.42), : int(w * 0.88)]
    luma = top.mean(axis=2)
    row_dark = (luma < 115).mean(axis=1)
    bands: list[tuple[int, int]] = []
    in_band = False
    start = 0
    for y, frac in enumerate(row_dark):
        if frac > 0.22 and not in_band:
            in_band = True
            start = y
        elif frac <= 0.22 and in_band:
            if y - start >= int(top.shape[0] * 0.08):
                bands.append((start, y))
            in_band = False
    if in_band and len(row_dark) - start >= int(top.shape[0] * 0.08):
        bands.append((start, len(row_dark)))
    overlaps = 0
    for i, a in enumerate(bands):
        for b in bands[i + 1 :]:
            inter = max(0, min(a[1], b[1]) - max(a[0], b[0]))
            if inter > 0:
                overlaps += 1
    detected = len(bands) >= 2 and (overlaps >= 1 or len(bands) >= 2)
    return {"detected": detected, "bands": bands, "band_count": len(bands), "overlaps": overlaps}


def detect_overlapping_text_blocks(image_path: Path) -> dict[str, Any]:
    """FAIL: 2+ large overlapping text blocks (model collage headline symptom)."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    canvas_area = h * w
    regions = _text_like_regions(arr, canvas_area=canvas_area)
    large = [r for r in regions if r["area_frac"] >= TEXT_BLOCK_MIN_CANVAS_FRAC]
    overlaps: list[dict[str, Any]] = []
    for i, a in enumerate(large):
        for b in large[i + 1 :]:
            iou = _bbox_iou(a["bbox"], b["bbox"])
            if iou >= TEXT_BLOCK_OVERLAP_IOU:
                overlaps.append({"iou": round(iou, 3), "a": a, "b": b})
    detected = len(overlaps) >= 1 and len(large) >= 2
    return {
        "detected": detected,
        "large_blocks": len(large),
        "overlaps": overlaps,
        "regions": large[:6],
    }


def detect_giant_cropped_glyph(image_path: Path) -> dict[str, Any]:
    """FAIL: single giant cropped glyph occupying >12% canvas (magnified letter crop)."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    canvas_area = h * w
    luma = arr.mean(axis=2)
    dark = luma < 95
    min_area = int(canvas_area * 0.03)
    best = _connected_bbox(dark, min_area=min_area)
    if not best:
        return {"detected": False, "reason": "no_large_dark_blob"}
    x0, y0, x1, y1, area = best
    bw, bh = max(1, x1 - x0), max(1, y1 - y0)
    area_frac = area / max(canvas_area, 1)
    aspect = bw / bh
    # Magnified partial glyph: huge dark blob, often extreme aspect or fills band
    glyph_like = area_frac > GIANT_GLYPH_CANVAS_FRAC or (
        area_frac > 0.06 and (aspect > 2.5 or aspect < 0.4 or (bw > w * 0.28 and bh > h * 0.14))
    )
    return {
        "detected": bool(glyph_like),
        "area_frac": round(area_frac, 4),
        "aspect": round(aspect, 2),
        "bbox": [x0, y0, x1, y1],
    }


def detect_model_drawn_trade_offer_template(image_path: Path) -> dict[str, Any]:
    """FAIL: TRADE OFFER two-panel meme drawn by model (not pasted PNG)."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    # Trade Offer: left ~45% two stacked panels with skin/hand tones + vertical divider
    left = arr[:, : int(w * 0.48)]
    hue, sat, val = _rgb_to_hsv_numpy(left)
    skin = ((hue < 45) | (hue > 330)) & (sat > 0.10) & (sat < 0.70) & (val > 0.22) & (val < 0.92)
    skin_frac = float(skin.mean())
    # Horizontal mid-band split inside left zone (two-offer panels)
    mid_y = int(left.shape[0] * 0.5)
    top = left[:mid_y]
    bot = left[mid_y:]
    top_luma = top.mean(axis=2).mean() if top.size else 0
    bot_luma = bot.mean(axis=2).mean() if bot.size else 0
    band_contrast = abs(float(top_luma) - float(bot_luma))
    # Vertical divider edge near center-left
    divider_x = int(w * 0.46)
    col = arr[:, max(0, divider_x - 2) : min(w, divider_x + 3)].mean(axis=2)
    divider_energy = float(np.abs(np.diff(col, axis=0)).mean()) if col.shape[0] > 2 else 0.0
    detected = (
        skin_frac > MODEL_MEME_SKIN_FRAC
        and band_contrast > 4.5
        and divider_energy > 3.0
        and left.shape[1] > w * 0.35
    )
    return {
        "detected": detected,
        "skin_frac": round(skin_frac, 4),
        "band_contrast": round(band_contrast, 2),
        "divider_energy": round(divider_energy, 2),
    }


def detect_model_drawn_drake_template(image_path: Path) -> dict[str, Any]:
    """FAIL: Drake pointing meme two-panel vertical layout drawn by model."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    zone = arr[int(h * 0.15) : int(h * 0.85), : int(w * 0.42)]
    if zone.size == 0:
        return {"detected": False, "reason": "empty_zone"}
    zh = zone.shape[0]
    top = zone[: zh // 2]
    bot = zone[zh // 2 :]
    hue, sat, val = _rgb_to_hsv_numpy(zone)
    skin = ((hue < 45) | (hue > 330)) & (sat > 0.10) & (sat < 0.70) & (val > 0.22)
    skin_frac = float(skin.mean())
    top_mean = float(top.mean())
    bot_mean = float(bot.mean())
    panel_contrast = abs(top_mean - bot_mean)
    detected = skin_frac > MODEL_MEME_SKIN_FRAC and panel_contrast > 18 and zh > h * 0.35
    return {
        "detected": detected,
        "skin_frac": round(skin_frac, 4),
        "panel_contrast": round(panel_contrast, 2),
    }


def detect_model_drawn_wojak_template(image_path: Path) -> dict[str, Any]:
    """FAIL: Wojak/Feels face blob drawn large by model."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    zone = arr[int(h * 0.08) : int(h * 0.72), : int(w * 0.38)]
    if zone.size == 0:
        return {"detected": False, "reason": "empty_zone"}
    hue, sat, val = _rgb_to_hsv_numpy(zone)
    # Wojak: pale skin oval + dark hair band top
    skin = ((hue < 40) | (hue > 330)) & (sat > 0.05) & (sat < 0.45) & (val > 0.55) & (val < 0.95)
    dark_hair = (val < 0.35) & (sat < 0.35)
    skin_frac = float(skin.mean())
    hair_frac = float(dark_hair.mean())
    detected = skin_frac > 0.09 and hair_frac > 0.04 and zone.shape[0] * zone.shape[1] > h * w * 0.08
    return {
        "detected": detected,
        "skin_frac": round(skin_frac, 4),
        "hair_frac": round(hair_frac, 4),
    }


def detect_model_drawn_meme_templates(image_path: Path) -> dict[str, Any]:
    """FAIL if any classic meme template appears model-drawn."""
    trade = detect_model_drawn_trade_offer_template(image_path)
    drake = detect_model_drawn_drake_template(image_path)
    wojak = detect_model_drawn_wojak_template(image_path)
    hits = [name for name, r in (("trade_offer", trade), ("drake", drake), ("wojak", wojak)) if r.get("detected")]
    return {
        "detected": bool(hits),
        "hits": hits,
        "trade_offer": trade,
        "drake": drake,
        "wojak": wojak,
    }


def detect_phone_tablo_in_scene(image_path: Path) -> dict[str, Any]:
    """Detect saturated blue/cream phone tablo block typical of model-drawn phone in scene."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    zone = arr[int(h * 0.35) :, int(w * 0.45) :]
    if zone.size == 0:
        return {"detected": False, "reason": "empty_zone"}
    hue, sat, val = _rgb_to_hsv_numpy(zone)
    blue_tablo = (hue >= 180) & (hue <= 240) & (sat > 0.25) & (val > 0.25)
    blue_frac = float(blue_tablo.mean())
    luma = zone.mean(axis=2)
    cream_board = (luma > 200) & (luma < 245)
    edge = float(np.abs(np.diff(luma, axis=1)).mean() + np.abs(np.diff(luma, axis=0)).mean())
    cream_frac = float(cream_board.mean())
    detected = blue_frac > 0.025 or (cream_frac > 0.12 and edge > 16)
    return {
        "detected": detected,
        "blue_frac": round(blue_frac, 4),
        "cream_frac": round(cream_frac, 4),
        "edge": round(edge, 2),
    }


def validate_story_scene_canvas(scene_path: Path) -> list[str]:
    """Pre-composite gate: story scene canvas must have NO model typography/meme/phone."""
    return validate_scene_only_canvas(scene_path)


def validate_scene_only_canvas(scene_path: Path) -> list[str]:
    """Pre-composite gate: scene canvas must have NO model typography/meme/phone."""
    errors: list[str] = []
    if not scene_path.is_file():
        return errors
    arr = np_array_rgb(scene_path)
    h, w = arr.shape[:2]
    upper = arr[: int(h * 0.45), :]
    luma = upper.mean(axis=2)
    dark_frac = float((luma < 95).mean())
    edge = float(np.abs(np.diff(luma, axis=1)).mean() + np.abs(np.diff(luma, axis=0)).mean())
    if dark_frac > SCENE_ONLY_MAX_DARK_UPPER and edge > SCENE_ONLY_MAX_TEXT_EDGE:
        errors.append(
            f"scene canvas has model typography energy (dark_frac={dark_frac:.3f}, edge={edge:.1f}) "
            "— regenerate story scene without Cyrillic/type in generation"
        )
    meme = detect_model_drawn_meme_templates(scene_path)
    if meme.get("detected"):
        errors.append(
            f"scene canvas has model-drawn meme template ({meme.get('hits')}) — meme must be factory PNG paste only"
        )
    phone = detect_phone_tablo_in_scene(scene_path)
    if phone.get("detected"):
        errors.append("scene canvas has phone/tablo in generation — phone must be factory-drawn post-composite")
    headline = detect_display_headline(scene_path)
    if headline.get("detected") and dark_frac > SCENE_ONLY_MAX_DARK_UPPER:
        errors.append("scene canvas has headline typography in generation — type must be factory post-process only")
    return errors


def validate_cover_anti_collage_gates(cover_path: Path) -> list[str]:
    """HARD factory anti-collage gates — FAIL overlapping type, glyph crops, model meme templates."""
    errors: list[str] = []
    if not cover_path.is_file():
        return errors

    stacked = detect_stacked_type_layers(cover_path)
    if stacked.get("detected"):
        errors.append(
            "cover.png: overlapping/stacked type layers detected "
            f"(bands={stacked.get('band_count')}) — use factory typography post-process, not model collage headlines"
        )

    overlap = detect_overlapping_text_blocks(cover_path)
    if overlap.get("detected"):
        errors.append(
            "cover.png: overlapping text blocks detected "
            f"(blocks={overlap.get('large_blocks')}, overlaps={len(overlap.get('overlaps') or [])}) "
            "— no stacked collage headlines; use factory typography post-process"
        )

    glyph = detect_giant_cropped_glyph(cover_path)
    if glyph.get("detected"):
        errors.append(
            "cover.png: giant cropped glyph detected "
            f"(area_frac={glyph.get('area_frac')}, aspect={glyph.get('aspect')}) "
            f"— magnified letter crops >{int(GIANT_GLYPH_CANVAS_FRAC * 100)}% canvas are forbidden"
        )

    meme_tpl = detect_model_drawn_meme_templates(cover_path)
    if meme_tpl.get("detected"):
        errors.append(
            "cover.png: model-drawn meme template detected "
            f"({meme_tpl.get('hits')}) — paste exactly ONE catalog meme PNG, never draw Trade Offer/Drake/Wojak"
        )

    return errors


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
            "cover.png: missing LARGE information-board phone tablo "
            f"(area_ratio={phone.get('area_ratio')}) — phone must be big cream/sage board graphic, not tiny in-scene number"
        )

    gold = detect_metallic_gold_dominance(cover_path)
    if gold.get("detected"):
        errors.append(
            "cover.png: metallic gold/brass/3D gold type detected "
            f"(gold_frac={gold.get('gold_frac')}) — tender-light canon uses matte terracotta only, no gold"
        )

    leather = detect_dark_leather_dominance(cover_path)
    if leather.get("detected"):
        errors.append(
            "cover.png: dark leather/noir dominance detected "
            f"(dark_frac={leather.get('dark_frac')}, leather_frac={leather.get('leather_frac')}) — use cream/oatmeal hallway"
        )

    brass_plaque = detect_gold_brass_phone_plaque(cover_path)
    if brass_plaque.get("detected") and phone.get("detected"):
        errors.append(
            "cover.png: gold/brass phone plaque detected "
            f"(brass_frac={brass_plaque.get('brass_frac')}) — phone must be cream/sage info board, not gold plaque"
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
                f"(area={pill.get('area_ratio')}) — phone must be LARGE cream/sage info-board tablo, not beige/gray UI pill"
            )

        plate = detect_white_plate_in_pad(cover_path)
        if plate.get("detected"):
            errors.append(
                "cover.png: logo plaque/plate detected in top-right pad "
                f"(kind={plate.get('plate_kind')}) — leave clean pad for factory logo paste"
            )
    except ImportError:
        errors.append("excalibur_blog_drawn_logo_gate.py missing — cover phone/plaque QA unavailable")

    errors.extend(validate_cover_anti_collage_gates(cover_path))

    return errors


# Backward-compatible aliases (scene_poster_v2 gates inverted → v3)
validate_cover_scene_poster_gates = validate_cover_type_meme_sticker_gates
detect_scene_poster_pass = detect_type_meme_sticker_pass
