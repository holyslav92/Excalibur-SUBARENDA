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

    with Image.open(image_path) as base_img:
        base = base_img.convert("RGBA")
    with Image.open(logo_path) as logo_img:
        logo = logo_img.convert("RGBA")

    x, y = logo_xy
    if logo_width_px <= 0:
        return {"ok": False, "reason": "logo_width_px missing"}

    scale = logo_width_px / max(logo.width, 1)
    target_h = logo_height_px or max(1, int(logo.height * scale))
    logo_resized = logo.resize((logo_width_px, target_h), Image.Resampling.LANCZOS)

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
