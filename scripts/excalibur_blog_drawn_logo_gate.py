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
WHITE_PLATE_LUMA_MIN = 235.0
WHITE_PLATE_STD_MAX = 16.0
WHITE_PLATE_MIN_AREA_RATIO = 1.12
WHITE_PLATE_RING_PX = 12


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


def detect_white_plate_in_pad(
    image_path: Path,
    *,
    pad_w_frac: float = PAD_WIDTH_FRACTION,
    pad_h_frac: float = PAD_HEIGHT_FRACTION,
) -> dict[str, Any]:
    """FAIL helper: AI generation drew a white card/plate in the logo pad."""
    arr = np_array_rgb(image_path)
    h, w = arr.shape[:2]
    x0, y0, pad_w, pad_h = _pad_box(w, h, pad_w_frac=pad_w_frac, pad_h_frac=pad_h_frac)
    pad = arr[y0 : y0 + pad_h, x0 : x0 + pad_w]
    if pad.size == 0:
        return {"detected": False, "reason": "empty_pad"}

    gray = pad.mean(axis=2)
    global_mean = float(arr.mean())
    rect = _largest_low_variance_rect(
        gray, luma_min=WHITE_PLATE_LUMA_MIN, std_max=WHITE_PLATE_STD_MAX
    )
    pad_area = int(pad_w * pad_h)
    min_area = max(900, int(pad_area * 0.18))
    plate_mean = float(rect.get("mean") or 0.0)
    plate_std = float(rect.get("std") or 0.0)
    brighter_than_scene = plate_mean >= max(WHITE_PLATE_LUMA_MIN, global_mean + 12.0)
    detected = (
        bool(rect.get("found"))
        and int(rect.get("area") or 0) >= min_area
        and brighter_than_scene
        and plate_std <= WHITE_PLATE_STD_MAX
    )
    return {
        "detected": detected,
        "pad_box": [x0, y0, pad_w, pad_h],
        "plate_area": int(rect.get("area") or 0),
        "plate_mean_luma": round(float(rect.get("mean") or 0.0), 2),
        "plate_std": round(float(rect.get("std") or 0.0), 2),
        "plate_bbox_local": rect.get("bbox"),
        "min_area": min_area,
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
    rect = _largest_low_variance_rect(
        gray, luma_min=WHITE_PLATE_LUMA_MIN, std_max=WHITE_PLATE_STD_MAX
    )
    plate_area = int(rect.get("area") or 0)
    plate_ratio = plate_area / max(glyph_bbox_area, 1)
    # Uniform near-white under transparent logo margins = backing plate on a non-white scene.
    backing_under_glyphs = (
        low_var_white
        and white_frac >= 0.45
        and mean_luma >= WHITE_PLATE_LUMA_MIN
        and std_luma <= 8.0
    )
    detected = backing_under_glyphs or (
        low_var_white and plate_ratio >= WHITE_PLATE_MIN_AREA_RATIO
    )
    return {
        "detected": detected,
        "mean_luma": round(mean_luma, 2),
        "std_luma": round(std_luma, 2),
        "glyph_bbox_area": glyph_bbox_area,
        "plate_area": plate_area,
        "plate_ratio": round(plate_ratio, 3),
        "plate_bbox_local": rect.get("bbox"),
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
            errors.append(
                f"pre-composite {name}: white logo plate/card in generation pad "
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
            errors.append(
                f"{name}: white plate/card under factory logo "
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
        errors = validate_article_logo_gates(article_dir, root)
        if errors:
            print("FAIL LOGO GATE:", "; ".join(errors), file=sys.stderr)
            return 1
        print("OK logo paste gates")
        return 0

    ap.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
