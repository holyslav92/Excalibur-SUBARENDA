#!/usr/bin/env python3
"""Detect AI-drawn «Добрый дом» lockups; verify factory PNG paste only."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_LOGO_REL = "memory/cover/assets/brand/logo-dobry-dom.png"
PAD_WIDTH_FRACTION = 0.12
PAD_HEIGHT_FRACTION = 0.26
DRAWN_LOCKUP_SCORE_THRESHOLD = 0.38
OFFICIAL_PASTE_MAE_MAX = 36.0
OFFICIAL_PASTE_MATCH_MIN = 0.78
LIGHT_PLATE_LUMA_MIN = 200.0
LIGHT_PLATE_STD_MAX = 26.0
LIGHT_PLATE_MIN_PAD_RATIO = 0.06
WHITE_PLATE_LUMA_MIN = 235.0
WHITE_PLATE_STD_MAX = 16.0
WHITE_PLATE_MIN_AREA_RATIO = 1.12
WHITE_PLATE_RING_PX = 12
GRAY_PLATE_LUMA_MIN = 145.0
GRAY_PLATE_LUMA_MAX = 234.0
GRAY_PLATE_STD_MAX = 22.0
GRAY_PLATE_MIN_PAD_RATIO = 0.28
GRAY_PLATE_UNIFORMITY_RATIO = 0.72


@dataclass
class PadAnalysis:
    score: float
    reasons: list[str]
    green_ratio: float
    terracotta_ratio: float
    edge_density: float


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _load_rgb(path: Path):
    from PIL import Image

    with Image.open(path) as img:
        return img.convert("RGB")


def _pad_box(width: int, height: int, *, pad_w_frac: float, pad_h_frac: float) -> tuple[int, int, int, int]:
    pad_w = max(24, int(width * pad_w_frac))
    pad_h = max(24, int(height * pad_h_frac))
    x0 = max(0, width - pad_w)
    y0 = 0
    return x0, y0, pad_w, pad_h


def _rgb_to_hsv_numpy(arr):
    import numpy as np

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


def analyze_top_right_pad(
    rgb_arr,
    *,
    pad_w_frac: float = PAD_WIDTH_FRACTION,
    pad_h_frac: float = PAD_HEIGHT_FRACTION,
) -> PadAnalysis:
    import numpy as np

    h, w = rgb_arr.shape[:2]
    x0, y0, pad_w, pad_h = _pad_box(w, h, pad_w_frac=pad_w_frac, pad_h_frac=pad_h_frac)
    pad = rgb_arr[y0 : y0 + pad_h, x0 : x0 + pad_w]
    if pad.size == 0:
        return PadAnalysis(0.0, [], 0.0, 0.0, 0.0)

    hue, sat, val = _rgb_to_hsv_numpy(pad)
    reasons: list[str] = []
    score = 0.0

    green_mask = ((hue >= 65) & (hue <= 170) & (sat >= 0.12) & (val >= 0.10))
    green_ratio = float(green_mask.mean())
    terracotta_mask = (
        ((hue <= 40) | (hue >= 325))
        & (sat >= 0.16)
        & (val >= 0.14)
        & (val <= 0.95)
    )
    terracotta_ratio = float(terracotta_mask.mean())

    gray = pad.mean(axis=2)
    edge_y = np.abs(np.diff(gray, axis=0)).mean() if gray.shape[0] > 1 else 0.0
    edge_x = np.abs(np.diff(gray, axis=1)).mean() if gray.shape[1] > 1 else 0.0
    edge_density = float(edge_y + edge_x)

    gold_mask = ((hue >= 35) & (hue <= 58) & (sat >= 0.35) & (val >= 0.45))
    gold_ratio = float(gold_mask.mean())

    if green_ratio >= 0.02:
        score += min(0.42, green_ratio * 6.0)
        reasons.append(f"green_curtain_pixels={green_ratio:.1%}")
    if terracotta_ratio >= 0.012:
        score += min(0.32, terracotta_ratio * 6.5)
        reasons.append(f"terracotta_wordmark_pixels={terracotta_ratio:.1%}")
    if edge_density >= 0.045:
        score += min(0.24, edge_density * 1.4)
        reasons.append(f"logo_pad_edge_density={edge_density:.3f}")
    if gold_ratio >= 0.04:
        score += min(0.18, gold_ratio * 3.0)
        reasons.append(f"gold_house_logo_pixels={gold_ratio:.1%}")

    stacked = float(np.std(gray))
    if stacked >= 28.0 and green_ratio >= 0.02 and terracotta_ratio >= 0.015:
        score += 0.12
        reasons.append("stacked_icon_wordmark_structure")

    dashed_score = _dashed_frame_score(pad)
    if dashed_score >= 0.12:
        score += min(0.2, dashed_score)
        reasons.append(f"dashed_logo_frame={dashed_score:.2f}")

    return PadAnalysis(min(1.0, score), reasons, green_ratio, terracotta_ratio, edge_density)


def _dashed_frame_score(pad) -> float:
    import numpy as np

    gray = pad.mean(axis=2)
    h, w = gray.shape
    if h < 16 or w < 16:
        return 0.0
    border = np.concatenate(
        [
            gray[0, :],
            gray[-1, :],
            gray[:, 0],
            gray[:, -1],
        ]
    )
    if border.size < 8:
        return 0.0
    diffs = np.abs(np.diff(border))
    peaks = (diffs > float(border.std()) * 0.85).astype("float32")
    return float(peaks.mean())


def _largest_low_variance_rect(gray, *, luma_min: float, std_max: float) -> dict[str, Any]:
    """Find largest near-uniform near-white axis-aligned block in a gray patch."""
    import numpy as np

    h, w = gray.shape
    if h < 8 or w < 8:
        return {"found": False, "area": 0, "bbox": None, "mean": 0.0, "std": 0.0}

    best: dict[str, Any] = {"found": False, "area": 0, "bbox": None, "mean": 0.0, "std": 0.0}
    step_y = max(1, h // 24)
    step_x = max(1, w // 24)
    for y0 in range(0, h - 7, step_y):
        for x0 in range(0, w - 7, step_x):
            for y1 in range(y0 + 8, h + 1, step_y):
                for x1 in range(x0 + 8, w + 1, step_x):
                    block = gray[y0:y1, x0:x1]
                    mean = float(block.mean())
                    std = float(block.std())
                    if mean < luma_min or std > std_max:
                        continue
                    area = int(block.size)
                    if area > int(best["area"]):
                        best = {
                            "found": True,
                            "area": area,
                            "bbox": (x0, y0, x1, y1),
                            "mean": mean,
                            "std": std,
                        }
    return best


def _plate_uniformity_vs_pad(gray, rect: dict[str, Any]) -> float:
    """Насколько блок однороднее остального pad (1.0 = одинаково)."""
    import numpy as np

    bbox = rect.get("bbox")
    if not bbox:
        return 1.0
    x0, y0, x1, y1 = bbox
    mask = np.zeros(gray.shape, dtype=bool)
    mask[y0:y1, x0:x1] = True
    rest = gray[~mask]
    block = gray[mask]
    if block.size < 12 or rest.size < 12:
        return 1.0
    block_std = float(block.std())
    rest_std = float(rest.std())
    if rest_std < 1e-3:
        return 0.0
    return block_std / rest_std


def detect_white_plate_in_pad(
    image_path: Path,
    *,
    pad_w_frac: float = PAD_WIDTH_FRACTION,
    pad_h_frac: float = PAD_HEIGHT_FRACTION,
) -> dict[str, Any]:
    """FAIL helper: AI generation drew a white/gray card/plate in the logo pad."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    x0, y0, pad_w, pad_h = _pad_box(w, h, pad_w_frac=pad_w_frac, pad_h_frac=pad_h_frac)
    pad = arr[y0 : y0 + pad_h, x0 : x0 + pad_w]
    if pad.size == 0:
        return {"detected": False, "reason": "empty_pad"}

    gray = pad.mean(axis=2)
    global_mean = float(arr.mean())
    pad_area = int(pad_w * pad_h)
    min_area = max(400, int(pad_area * LIGHT_PLATE_MIN_PAD_RATIO))

    light_rect = _largest_low_variance_rect(
        gray, luma_min=LIGHT_PLATE_LUMA_MIN, std_max=LIGHT_PLATE_STD_MAX
    )
    light_area = int(light_rect.get("area") or 0)
    light_mean = float(light_rect.get("mean") or 0.0)
    light_std = float(light_rect.get("std") or 0.0)
    light_pad_ratio = light_area / max(pad_area, 1)
    brighter_than_scene = light_mean >= max(LIGHT_PLATE_LUMA_MIN, global_mean + 8.0)
    light_detected = (
        bool(light_rect.get("found"))
        and light_area >= min_area
        and brighter_than_scene
        and light_std <= LIGHT_PLATE_STD_MAX
        and light_pad_ratio >= LIGHT_PLATE_MIN_PAD_RATIO
    )
    if light_detected:
        plate_kind = "white" if light_mean >= WHITE_PLATE_LUMA_MIN else "light"
        if light_mean < WHITE_PLATE_LUMA_MIN and GRAY_PLATE_LUMA_MIN <= light_mean <= GRAY_PLATE_LUMA_MAX:
            plate_kind = "gray"
        if light_mean >= WHITE_PLATE_LUMA_MIN - 15 and light_mean < WHITE_PLATE_LUMA_MIN:
            plate_kind = "cream"
        return {
            "detected": True,
            "plate_kind": plate_kind,
            "pad_box": [x0, y0, pad_w, pad_h],
            "plate_area": light_area,
            "plate_mean_luma": round(light_mean, 2),
            "plate_std": round(light_std, 2),
            "plate_bbox_local": light_rect.get("bbox"),
            "min_area": min_area,
            "pad_ratio": round(light_pad_ratio, 3),
        }

    white_rect = _largest_low_variance_rect(
        gray, luma_min=WHITE_PLATE_LUMA_MIN, std_max=WHITE_PLATE_STD_MAX
    )
    plate_mean = float(white_rect.get("mean") or 0.0)
    plate_std = float(white_rect.get("std") or 0.0)
    white_brighter = plate_mean >= max(WHITE_PLATE_LUMA_MIN, global_mean + 12.0)
    white_area = int(white_rect.get("area") or 0)
    white_detected = (
        bool(white_rect.get("found"))
        and white_area >= min_area
        and white_brighter
        and plate_std <= WHITE_PLATE_STD_MAX
    )
    if white_detected:
        return {
            "detected": True,
            "plate_kind": "white",
            "pad_box": [x0, y0, pad_w, pad_h],
            "plate_area": white_area,
            "plate_mean_luma": round(plate_mean, 2),
            "plate_std": round(plate_std, 2),
            "plate_bbox_local": white_rect.get("bbox"),
            "min_area": min_area,
        }

    gray_rect = _largest_low_variance_rect(
        gray, luma_min=GRAY_PLATE_LUMA_MIN, std_max=GRAY_PLATE_STD_MAX
    )
    gray_mean = float(gray_rect.get("mean") or 0.0)
    gray_std = float(gray_rect.get("std") or 0.0)
    gray_area = int(gray_rect.get("area") or 0)
    pad_ratio = gray_area / max(pad_area, 1)
    uniformity = _plate_uniformity_vs_pad(gray, gray_rect)
    gray_detected = (
        bool(gray_rect.get("found"))
        and gray_area >= min_area
        and GRAY_PLATE_LUMA_MIN <= gray_mean <= GRAY_PLATE_LUMA_MAX
        and gray_std <= GRAY_PLATE_STD_MAX
        and pad_ratio >= GRAY_PLATE_MIN_PAD_RATIO
        and uniformity <= GRAY_PLATE_UNIFORMITY_RATIO
    )
    rect = gray_rect if gray_detected else white_rect
    return {
        "detected": gray_detected,
        "plate_kind": "gray" if gray_detected else "",
        "pad_box": [x0, y0, pad_w, pad_h],
        "plate_area": int(rect.get("area") or 0),
        "plate_mean_luma": round(float(rect.get("mean") or 0.0), 2),
        "plate_std": round(float(rect.get("std") or 0.0), 2),
        "plate_bbox_local": rect.get("bbox"),
        "min_area": min_area,
        "pad_ratio": round(pad_ratio, 3) if gray_rect.get("found") else 0.0,
        "uniformity_ratio": round(uniformity, 3) if gray_rect.get("found") else 1.0,
    }


def detect_white_plate_under_logo(
    image_path: Path,
    logo_path: Path,
    *,
    logo_xy: tuple[int, int],
    logo_width_px: int,
    logo_height_px: int,
) -> dict[str, Any]:
    """FAIL helper: near-white opaque rectangle under lockup larger than glyph bbox."""
    from PIL import Image

    import numpy as np

    from excalibur_blog_brand_logo_composite import prepare_logo_rgba

    x, y = logo_xy
    if logo_width_px <= 0 or logo_height_px <= 0:
        return {"detected": False, "reason": "invalid_logo_bbox"}

    logo = prepare_logo_rgba(logo_path, logo_width_px)
    if logo.width != logo_width_px:
        scale = logo_width_px / max(logo.width, 1)
        logo = logo.resize(
            (logo_width_px, max(1, int(logo.height * scale))),
            Image.Resampling.LANCZOS,
        )
    logo_h = min(logo.height, logo_height_px)

    with Image.open(image_path) as base_img:
        base = base_img.convert("RGBA")
    w = min(logo.width, base.width - x)
    h = min(logo_h, base.height - y)
    if w <= 0 or h <= 0:
        return {"detected": False, "reason": "out_of_bounds"}

    region = np.array(base.crop((x, y, x + w, y + h)), dtype="float32")
    logo_arr = np.array(logo.crop((0, 0, w, h)), dtype="float32")
    alpha = logo_arr[..., 3] / 255.0
    glyph_mask = alpha > 0.35
    glyph_area = int(glyph_mask.sum())
    if glyph_area < 24:
        glyph_mask = alpha > 0.08
        glyph_area = int(glyph_mask.sum())
    if glyph_area < 12:
        return {"detected": False, "reason": "glyph_mask_empty"}

    gray = region[..., :3].mean(axis=2)
    ys, xs = np.where(glyph_mask)
    gy0, gy1 = int(ys.min()), int(ys.max()) + 1
    gx0, gx1 = int(xs.min()), int(xs.max()) + 1
    glyph_bbox_area = max(1, (gy1 - gy0) * (gx1 - gx0))

    ring = max(4, WHITE_PLATE_RING_PX)
    ry0 = max(0, gy0 - ring)
    ry1 = min(h, gy1 + ring)
    rx0 = max(0, gx0 - ring)
    rx1 = min(w, gx1 + ring)
    ring_mask = np.zeros((h, w), dtype=bool)
    ring_mask[ry0:ry1, rx0:rx1] = True
    ring_mask[gy0:gy1, gx0:gx1] = False
    transparent = alpha < 0.12
    inspect = ring_mask | transparent
    if not inspect.any():
        return {"detected": False, "glyph_bbox_area": glyph_bbox_area}

    sample = gray[inspect]
    mean_luma = float(sample.mean())
    std_luma = float(sample.std())
    white_frac = float((sample >= WHITE_PLATE_LUMA_MIN).mean()) if sample.size else 0.0
    low_var_white = mean_luma >= WHITE_PLATE_LUMA_MIN and std_luma <= WHITE_PLATE_STD_MAX
    white_rect = _largest_low_variance_rect(
        gray, luma_min=WHITE_PLATE_LUMA_MIN, std_max=WHITE_PLATE_STD_MAX
    )
    plate_area = int(white_rect.get("area") or 0)
    plate_ratio = plate_area / max(glyph_bbox_area, 1)
    # Uniform near-white under transparent logo margins = backing plate on a non-white scene.
    backing_under_glyphs = (
        low_var_white
        and white_frac >= 0.45
        and mean_luma >= WHITE_PLATE_LUMA_MIN
        and std_luma <= 8.0
    )
    white_detected = backing_under_glyphs or (
        low_var_white and plate_ratio >= WHITE_PLATE_MIN_AREA_RATIO
    )

    gray_rect = _largest_low_variance_rect(
        gray, luma_min=GRAY_PLATE_LUMA_MIN, std_max=GRAY_PLATE_STD_MAX
    )
    gray_area = int(gray_rect.get("area") or 0)
    gray_ratio = gray_area / max(glyph_bbox_area, 1)
    gray_mean = float(gray_rect.get("mean") or 0.0)
    gray_std = float(gray_rect.get("std") or 0.0)
    gray_uniformity = _plate_uniformity_vs_pad(gray, gray_rect)
    gray_detected = (
        bool(gray_rect.get("found"))
        and GRAY_PLATE_LUMA_MIN <= gray_mean <= GRAY_PLATE_LUMA_MAX
        and gray_std <= GRAY_PLATE_STD_MAX
        and gray_ratio >= WHITE_PLATE_MIN_AREA_RATIO
        and gray_uniformity <= GRAY_PLATE_UNIFORMITY_RATIO
        and (
            mean_luma >= GRAY_PLATE_LUMA_MIN
            and std_luma <= GRAY_PLATE_STD_MAX
        )
    )
    detected = white_detected or gray_detected
    plate_kind = "white" if white_detected else ("gray" if gray_detected else "")
    return {
        "detected": detected,
        "plate_kind": plate_kind,
        "mean_luma": round(mean_luma, 2),
        "std_luma": round(std_luma, 2),
        "glyph_bbox_area": glyph_bbox_area,
        "plate_area": plate_area if white_detected else gray_area,
        "plate_ratio": round(plate_ratio if white_detected else gray_ratio, 3),
        "plate_bbox_local": (white_rect if white_detected else gray_rect).get("bbox"),
    }


def detect_drawn_lockup_in_image(
    image_path: Path,
    *,
    pad_w_frac: float = PAD_WIDTH_FRACTION,
    pad_h_frac: float = PAD_HEIGHT_FRACTION,
) -> dict[str, Any]:
    arr = np_array_rgb(image_path)
    analysis = analyze_top_right_pad(arr, pad_w_frac=pad_w_frac, pad_h_frac=pad_h_frac)
    detected = analysis.score >= DRAWN_LOCKUP_SCORE_THRESHOLD
    return {
        "path": str(image_path),
        "detected": detected,
        "score": round(analysis.score, 4),
        "threshold": DRAWN_LOCKUP_SCORE_THRESHOLD,
        "reasons": analysis.reasons,
        "green_ratio": round(analysis.green_ratio, 4),
        "terracotta_ratio": round(analysis.terracotta_ratio, 4),
        "edge_density": round(analysis.edge_density, 4),
    }


def np_array_rgb(path: Path):
    import numpy as np

    return np.array(_load_rgb(path))


def verify_official_logo_paste(
    image_path: Path,
    logo_path: Path,
    *,
    logo_xy: tuple[int, int],
    logo_width_px: int,
    logo_height_px: int | None = None,
) -> dict[str, Any]:
    from PIL import Image

    from excalibur_blog_brand_logo_composite import prepare_logo_rgba

    with Image.open(image_path) as base_img:
        base = base_img.convert("RGBA")
    if logo_width_px <= 0:
        return {"ok": False, "reason": "logo_width_px missing"}

    logo_resized = prepare_logo_rgba(logo_path, logo_width_px)
    target_h = logo_height_px or logo_resized.height
    if logo_resized.height != target_h:
        scale = target_h / max(logo_resized.height, 1)
        logo_resized = logo_resized.resize(
            (max(1, int(logo_resized.width * scale)), target_h),
            Image.Resampling.LANCZOS,
        )

    x, y = logo_xy
    x = max(0, min(x, base.width - 1))
    y = max(0, min(y, base.height - 1))
    w = min(logo_resized.width, base.width - x)
    h = min(logo_resized.height, base.height - y)
    if w <= 0 or h <= 0:
        return {"ok": False, "reason": "logo region out of bounds"}

    region = base.crop((x, y, x + w, y + h))
    logo_crop = logo_resized.crop((0, 0, w, h))

    import numpy as np

    reg = np.array(region, dtype="float32")
    ref = np.array(logo_crop, dtype="float32")
    alpha = ref[..., 3] / 255.0
    strong_mask = alpha > 0.85
    if int(strong_mask.sum()) < 24:
        strong_mask = alpha > 0.35
    diff = np.abs(reg[..., :3] - ref[..., :3])
    mae = float(diff[strong_mask].mean()) if strong_mask.any() else 999.0
    match_ratio = float((diff[strong_mask] < 40).mean()) if strong_mask.any() else 0.0

    ok = mae <= OFFICIAL_PASTE_MAE_MAX and match_ratio >= OFFICIAL_PASTE_MATCH_MIN
    return {
        "ok": ok,
        "mae": round(mae, 2),
        "match_ratio": round(match_ratio, 4),
        "match_min": OFFICIAL_PASTE_MATCH_MIN,
        "mae_max": OFFICIAL_PASTE_MAE_MAX,
        "logo_xy": [x, y],
        "logo_size": [w, h],
    }


def detect_logo_text_overlap(
    image_path: Path,
    *,
    logo_xy: tuple[int, int],
    logo_width_px: int,
    logo_height_px: int,
    margin_px: int = 8,
) -> dict[str, Any]:
    import numpy as np

    arr = np.array(_load_rgb(image_path))
    h, w = arr.shape[:2]
    x, y = logo_xy
    lw = min(logo_width_px, w - x)
    lh = min(logo_height_px, h - y)
    if lw <= 0 or lh <= 0:
        return {"overlap": False, "reason": "invalid logo bbox"}

    x0 = max(0, x - margin_px)
    y0 = max(0, y - margin_px)
    x1 = min(w, x + lw + margin_px)
    y1 = min(h, y + lh + margin_px)
    roi = arr[y0:y1, x0:x1]
    gray = roi.mean(axis=2)

    logo_local_x = x - x0
    logo_local_y = y - y0
    pad = np.ones((lh, lw), dtype=bool)
    outside = np.ones(gray.shape, dtype=bool)
    outside[logo_local_y : logo_local_y + lh, logo_local_x : logo_local_x + lw] = False

    logo_region = gray[logo_local_y : logo_local_y + lh, logo_local_x : logo_local_x + lw]
    outside_region = gray[outside] if outside.any() else gray.reshape(-1)
    if outside_region.size == 0:
        return {"overlap": False, "score": 0.0}

    logo_edges = np.abs(np.diff(logo_region, axis=0)).mean() + np.abs(np.diff(logo_region, axis=1)).mean()
    outside_edges = (
        np.abs(np.diff(gray, axis=0)).mean() + np.abs(np.diff(gray, axis=1)).mean()
        if gray.size
        else 0.0
    )
    overlap_score = float(logo_edges / max(outside_edges, 1e-3))
    overlap = overlap_score > 1.35 and logo_edges > 0.09
    return {
        "overlap": overlap,
        "score": round(overlap_score, 3),
        "logo_edges": round(float(logo_edges), 4),
    }


def is_bright_window_pad_false_positive(
    image_path: Path,
    *,
    lockup: dict[str, Any] | None = None,
    plate: dict[str, Any] | None = None,
) -> bool:
    """Agent judgment: outdoor window blowout in TR pad mimics white plate, not an AI logo card."""
    if lockup is None:
        lockup = detect_drawn_lockup_in_image(image_path)
    if lockup.get("detected"):
        return False
    if float(lockup.get("score") or 0.0) >= DRAWN_LOCKUP_SCORE_THRESHOLD:
        return False
    if plate is None:
        plate = detect_white_plate_in_pad(image_path)
    if not plate.get("detected") or plate.get("plate_kind") != "white":
        return False
    green_ratio = float(lockup.get("green_ratio") or 0.0)
    terracotta_ratio = float(lockup.get("terracotta_ratio") or 0.0)
    if green_ratio >= 0.02 or terracotta_ratio >= 0.012:
        return False
    plate_std = float(plate.get("plate_std") or 0.0)
    return 12.0 <= plate_std <= WHITE_PLATE_STD_MAX + 1.5


def validate_full_grsai_cover_gates(article_dir: Path, root: Path) -> list[str]:
    """Full Grsai cover QA: logo/phone/type IN generation — no factory paste stamps."""
    errors: list[str] = []
    from excalibur_blog_brand_logo_composite import IMAGE_NAMES

    cover_dir = article_dir / "cover"
    cover_path = cover_dir / "cover.png"
    if not cover_path.is_file():
        errors.append("cover/cover.png missing for full Grsai QA")
        return errors

    plate = detect_white_plate_in_pad(cover_path)
    if plate.get("detected") and plate.get("plate_kind") in {"white", "gray", "beige"}:
        if not is_bright_window_pad_false_positive(cover_path, lockup={"detected": True}, plate=plate):
            errors.append(
                "cover.png: logo plate/card under top-right pad "
                f"(kind={plate.get('plate_kind')}, area={plate.get('plate_area')})"
            )

    pill = detect_phone_pill_post_composite(cover_path)
    if pill.get("detected"):
        errors.append(
            "cover.png: factory post-composite phone pill detected — full Grsai mode forbids overlay"
        )

    for name in IMAGE_NAMES:
        if name == "cover.png":
            continue
        live = cover_dir / name
        if not live.is_file():
            continue
        result = detect_drawn_lockup_in_image(live)
        if result["detected"]:
            errors.append(
                f"{name}: forbidden company logo on inline panel (score={result['score']})"
            )
    return errors


def validate_article_logo_gates_slim(article_dir: Path, root: Path) -> list[str]:
    """Slim logo QA: cover pre-composite drawn-lockup + no-logo panels only; skip pixel/plate heuristics."""
    errors: list[str] = []
    from excalibur_blog_brand_logo_composite import (
        IMAGE_NAMES,
        load_tenant_logo_config,
        resolve_inline_logo_slots,
        uses_brand_logo_paste,
    )

    cfg = load_tenant_logo_config(root)
    if not uses_brand_logo_paste(cfg):
        return errors

    cover_dir = article_dir / "cover"
    pre_dir = cover_dir / "pre-composite"
    pre_cover = pre_dir / "cover.png"
    if pre_cover.is_file():
        result = detect_drawn_lockup_in_image(pre_cover)
        if result["detected"]:
            reasons = ", ".join(result.get("reasons") or [])
            errors.append(
                f"pre-composite cover.png: AI-drawn lockup detected (score={result['score']}, {reasons})"
            )
        plate = detect_white_plate_in_pad(pre_cover)
        if plate.get("detected") and plate.get("plate_kind") == "white":
            if not is_bright_window_pad_false_positive(pre_cover, lockup=result, plate=plate):
                errors.append(
                    "pre-composite cover.png: white logo plate/card in generation pad "
                    f"(area={plate.get('plate_area')})"
                )
    else:
        errors.append("cover/pre-composite/cover.png missing — composite must snapshot before logo paste")

    inline_files = resolve_inline_logo_slots(article_dir, cfg)
    for name in IMAGE_NAMES:
        if name == "cover.png" or name in inline_files:
            continue
        live = cover_dir / name
        if not live.is_file():
            continue
        result = detect_drawn_lockup_in_image(live)
        if result["detected"]:
            errors.append(
                f"{name}: forbidden drawn logo on panel without factory paste "
                f"(score={result['score']})"
            )
    return errors


def validate_article_logo_gates_reference_mode(article_dir: Path, root: Path) -> list[str]:
    """Reference-in-generation QA: no gray/white plate under logo pad; no pre-composite stamp required."""
    errors: list[str] = []
    from excalibur_blog_brand_logo_composite import (
        IMAGE_NAMES,
        load_tenant_logo_config,
        resolve_inline_logo_slots,
        uses_logo_reference_in_generation,
    )

    cfg = load_tenant_logo_config(root)
    if not uses_logo_reference_in_generation(cfg):
        return errors

    cover_dir = article_dir / "cover"
    inline_files = resolve_inline_logo_slots(article_dir, cfg)
    logo_panels = ["cover.png", *inline_files]

    for name in logo_panels:
        live = cover_dir / name
        if not live.is_file():
            errors.append(f"missing {name} for logo reference QA")
            continue
        plate = detect_white_plate_in_pad(live)
        if plate.get("detected"):
            errors.append(
                f"{name}: logo plate/card under top-right pad "
                f"(kind={plate.get('plate_kind')}, area={plate.get('plate_area')})"
            )

    for name in IMAGE_NAMES:
        if name in logo_panels:
            continue
        live = cover_dir / name
        if not live.is_file():
            continue
        result = detect_drawn_lockup_in_image(live)
        if result["detected"]:
            errors.append(
                f"{name}: forbidden drawn logo on panel without logo reference "
                f"(score={result['score']})"
            )
    return errors


def validate_article_logo_gates(article_dir: Path, root: Path) -> list[str]:
    errors: list[str] = []
    from excalibur_blog_brand_logo_composite import (
        IMAGE_NAMES,
        load_tenant_logo_config,
        resolve_inline_logo_slots,
        uses_brand_logo_paste,
    )

    cfg = load_tenant_logo_config(root)
    if not uses_brand_logo_paste(cfg):
        return errors

    logo_path = root / cfg["logo_rel"]
    if not logo_path.is_file():
        errors.append(f"brand logo missing: {cfg['logo_rel']}")
        return errors

    cover_dir = article_dir / "cover"
    pre_dir = cover_dir / "pre-composite"
    stamp_path = cover_dir / "logo-composite-stamp.json"
    stamp: dict[str, Any] = {}
    if stamp_path.is_file():
        try:
            stamp = json.loads(stamp_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append("logo-composite-stamp.json invalid JSON")

    inline_files = resolve_inline_logo_slots(article_dir, cfg)
    check_names: list[str] = ["cover.png", *inline_files]

    for name in check_names:
        pre_path = pre_dir / name
        live_path = cover_dir / name
        source = pre_path if pre_path.is_file() else None
        if source is None:
            errors.append(
                f"cover/pre-composite/{name} missing — composite must snapshot before logo paste"
            )
            continue
        result = detect_drawn_lockup_in_image(source)
        if result["detected"]:
            reasons = ", ".join(result.get("reasons") or [])
            errors.append(
                f"pre-composite {name}: AI-drawn lockup detected (score={result['score']}, {reasons})"
            )
        plate = detect_white_plate_in_pad(source)
        if plate.get("detected"):
            kind = plate.get("plate_kind") or "light"
            errors.append(
                f"pre-composite {name}: {kind} logo plate/card in generation pad "
                f"(area={plate.get('plate_area')}, luma={plate.get('plate_mean_luma')})"
            )

    if not stamp:
        return errors

    placements: dict[str, Any] = {"cover.png": stamp.get("cover_logo_placement") or {}}
    placements.update(stamp.get("panel_logo_placements") or {})

    for name in check_names:
        img_path = cover_dir / name
        if not img_path.is_file():
            errors.append(f"missing composed image cover/{name}")
            continue
        placement = placements.get(name) or {}
        xy = placement.get("logo_xy") or []
        logo_w = int(placement.get("logo_width_px") or 0)
        if len(xy) != 2 or logo_w <= 0:
            errors.append(f"{name}: logo placement missing in composite stamp")
            continue
        logo_h = int(placement.get("logo_height_px") or max(1, int(logo_w * 1.6)))
        verify = verify_official_logo_paste(
            img_path,
            logo_path,
            logo_xy=(int(xy[0]), int(xy[1])),
            logo_width_px=logo_w,
            logo_height_px=logo_h,
        )
        if not verify.get("ok"):
            errors.append(
                f"{name}: post-composite logo is not official PNG pixels "
                f"(mae={verify.get('mae')}, match={verify.get('match_ratio')})"
            )
        overlap = detect_logo_text_overlap(
            img_path,
            logo_xy=(int(xy[0]), int(xy[1])),
            logo_width_px=logo_w,
            logo_height_px=logo_h,
        )
        if overlap.get("overlap"):
            errors.append(f"{name}: logo overlaps readable text in logo pad zone")
        plate = detect_white_plate_under_logo(
            img_path,
            logo_path,
            logo_xy=(int(xy[0]), int(xy[1])),
            logo_width_px=logo_w,
            logo_height_px=logo_h,
        )
        if plate.get("detected"):
            kind = plate.get("plate_kind") or "light"
            errors.append(
                f"{name}: {kind} plate/card under factory logo "
                f"(ratio={plate.get('plate_ratio')}, luma={plate.get('mean_luma')})"
            )

    for name in IMAGE_NAMES:
        if name == "cover.png" or name in inline_files:
            continue
        live = cover_dir / name
        if not live.is_file():
            continue
        result = detect_drawn_lockup_in_image(live)
        if result["detected"]:
            errors.append(
                f"{name}: forbidden drawn logo on panel without factory paste "
                f"(score={result['score']})"
            )

    return errors


PHONE_PILL_LUMA_MIN = 228.0
PHONE_PILL_STD_MAX = 14.0
PHONE_PILL_MIN_AREA_RATIO = 0.0045
PHONE_PILL_MIN_ASPECT = 2.2
CAT_ZONE_WIDTH_FRAC = 0.40
CAT_ZONE_HEIGHT_FRAC = 0.45
HEADLINE_BAND_HEIGHT_FRAC = 0.36


def _rects_intersect(a: tuple[int, int, int, int], b: tuple[int, int, int, int]) -> bool:
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    return ax0 < bx1 and ax1 > bx0 and ay0 < by1 and ay1 > by0


def detect_phone_pill_post_composite(image_path: Path) -> dict[str, Any]:
    """FAIL: opaque white/gray pill/button pasted over finished cover (factory legacy)."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    band_y0 = int(h * 0.68)
    band = arr[band_y0:h, :]
    if band.size == 0:
        return {"detected": False, "reason": "empty_bottom_band"}

    gray = band.mean(axis=2)
    rect = _largest_low_variance_rect(
        gray, luma_min=PHONE_PILL_LUMA_MIN, std_max=PHONE_PILL_STD_MAX
    )
    if not rect.get("found"):
        return {"detected": False, "reason": "no_uniform_block"}

    x0, y0, x1, y1 = rect["bbox"]
    block_w = max(1, x1 - x0)
    block_h = max(1, y1 - y0)
    aspect = block_w / block_h
    area_ratio = int(rect.get("area") or 0) / max(w * h, 1)
    detected = (
        aspect >= PHONE_PILL_MIN_ASPECT
        and area_ratio >= PHONE_PILL_MIN_AREA_RATIO
        and float(rect.get("mean") or 0.0) >= PHONE_PILL_LUMA_MIN
        and float(rect.get("std") or 0.0) <= PHONE_PILL_STD_MAX
    )
    global_bbox = (x0, band_y0 + y0, x1, band_y0 + y1)
    return {
        "detected": detected,
        "bbox": global_bbox,
        "aspect": round(aspect, 2),
        "area_ratio": round(area_ratio, 4),
        "mean_luma": round(float(rect.get("mean") or 0.0), 2),
        "std_luma": round(float(rect.get("std") or 0.0), 2),
    }


def detect_logo_overlaps_protected_zones(
    image_path: Path,
    *,
    logo_xy: tuple[int, int],
    logo_width_px: int,
    logo_height_px: int,
) -> dict[str, Any]:
    """FAIL if pasted logo intersects cat/meme bottom-left or headline band."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    x, y = logo_xy
    logo_box = (x, y, min(w, x + logo_width_px), min(h, y + logo_height_px))
    cat_zone = (0, int(h * (1.0 - CAT_ZONE_HEIGHT_FRAC)), int(w * CAT_ZONE_WIDTH_FRAC), h)
    headline_band = (0, 0, int(w * 0.82), int(h * HEADLINE_BAND_HEIGHT_FRAC))
    overlaps_cat = _rects_intersect(logo_box, cat_zone)
    overlaps_headline = _rects_intersect(logo_box, headline_band)
    return {
        "overlap": overlaps_cat or overlaps_headline,
        "overlaps_cat_zone": overlaps_cat,
        "overlaps_headline_band": overlaps_headline,
        "logo_box": logo_box,
        "cat_zone": cat_zone,
        "headline_band": headline_band,
    }


def detect_phone_pill_overlaps_cat_zone(image_path: Path) -> dict[str, Any]:
    pill = detect_phone_pill_post_composite(image_path)
    if not pill.get("detected"):
        return {"overlap": False, "pill": pill}
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    cat_zone = (0, int(h * (1.0 - CAT_ZONE_HEIGHT_FRAC)), int(w * CAT_ZONE_WIDTH_FRAC), h)
    bbox = pill.get("bbox") or (0, 0, 0, 0)
    overlap = _rects_intersect(tuple(bbox), cat_zone)
    return {"overlap": overlap, "pill": pill, "cat_zone": cat_zone}


def validate_cover_phone_and_overlap_gates(article_dir: Path, root: Path) -> list[str]:
    """Python gates: no post-composite phone pill; logo not over cat/headline zones."""
    errors: list[str] = []
    from excalibur_blog_brand_logo_composite import (
        load_tenant_logo_config,
        uses_brand_logo_paste,
    )

    cfg = load_tenant_logo_config(root)
    if not uses_brand_logo_paste(cfg):
        return errors

    cover_path = article_dir / "cover" / "cover.png"
    if not cover_path.is_file():
        return errors

    pill = detect_phone_pill_post_composite(cover_path)
    if pill.get("detected"):
        errors.append(
            "cover.png: post-composite phone pill/button detected "
            f"(aspect={pill.get('aspect')}, luma={pill.get('mean_luma')}) — regenerate with in-scene phone"
        )
    pill_overlap = detect_phone_pill_overlaps_cat_zone(cover_path)
    if pill_overlap.get("overlap"):
        errors.append("cover.png: phone pill overlaps cat/meme bottom-left zone")

    stamp_path = article_dir / "cover" / "logo-composite-stamp.json"
    if not stamp_path.is_file():
        return errors
    try:
        stamp = json.loads(stamp_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return errors
    placement = stamp.get("cover_logo_placement") or {}
    xy = placement.get("logo_xy") or []
    logo_w = int(placement.get("logo_width_px") or 0)
    logo_h = int(placement.get("logo_height_px") or max(1, int(logo_w * 1.6)))
    if len(xy) == 2 and logo_w > 0:
        overlap = detect_logo_overlaps_protected_zones(
            cover_path,
            logo_xy=(int(xy[0]), int(xy[1])),
            logo_width_px=logo_w,
            logo_height_px=logo_h,
        )
        if overlap.get("overlaps_cat_zone"):
            errors.append("cover.png: factory logo overlaps cat/meme bottom-left zone")
        if overlap.get("overlaps_headline_band"):
            errors.append("cover.png: factory logo overlaps headline band")

    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--image", help="Single image path for drawn-lockup detect")
    ap.add_argument("--article-dir", help="Validate article pre/post composite logo gates")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    root = project_root()

    if args.image:
        path = Path(args.image)
        if not path.is_absolute():
            path = root / path
        result = detect_drawn_lockup_in_image(path)
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            status = "DRAWN" if result["detected"] else "OK"
            print(f"{status}: {path} score={result['score']}")
        return 1 if result["detected"] else 0

    if args.article_dir:
        article_dir = Path(args.article_dir)
        if not article_dir.is_absolute():
            article_dir = root / article_dir
        errors = validate_article_logo_gates_slim(article_dir, root)
        if errors:
            print("FAIL LOGO GATE:", "; ".join(errors), file=sys.stderr)
            return 1
        print("OK logo paste gates (slim)")
        return 0

    ap.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
