#!/usr/bin/env python3
"""Apply standalone cover canvas (2048×1152) → cover.png + pad-clear + logo composite."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

DEFAULT_OUTPUT_SIZE = (1200, 675)
PRE_COMPOSITE_DIRNAME = "pre-composite"


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def pad_clear_top_right_scene_clone(image_path: Path) -> int:
    """Снять light plate в TR pad — inpaint bbox + texture clone, без белой заливки."""
    from excalibur_blog_drawn_logo_gate import (
        detect_white_plate_in_pad,
        _pad_box,
        PAD_WIDTH_FRACTION,
        PAD_HEIGHT_FRACTION,
    )
    from excalibur_blog_live_plate_remove_relogo import (
        clear_logo_pad,
        np_array_rgb_from_pil,
        _find_plate_bbox_local,
        _pad_donor_strips,
        _texture_fill,
        _feather_blend_region,
        CLEAR_PAD_W_FRAC,
        CLEAR_PAD_H_FRAC,
    )
    from PIL import Image
    import numpy as np

    img = Image.open(image_path).convert("RGBA")
    rgb_arr = np_array_rgb_from_pil(img)
    passes = clear_logo_pad(rgb_arr, initial_full_wipe=False)
    Image.fromarray(rgb_arr).convert("RGBA").save(image_path, format="PNG", optimize=True)

    plate = detect_white_plate_in_pad(image_path)
    if plate.get("detected") and float(plate.get("pad_ratio") or 0) >= 0.06:
        rgb_arr = np_array_rgb_from_pil(Image.open(image_path).convert("RGBA"))
        h, w = rgb_arr.shape[:2]
        px0, py0, pw, ph = _pad_box(
            w, h, pad_w_frac=CLEAR_PAD_W_FRAC, pad_h_frac=CLEAR_PAD_H_FRAC
        )
        pad = rgb_arr[py0 : py0 + ph, px0 : px0 + pw]
        bbox = _find_plate_bbox_local(pad, min_area=400)
        if bbox:
            lx0, ly0, lx1, ly1 = bbox
            gx0, gy0 = px0 + lx0, py0 + ly0
            gx1, gy1 = px0 + lx1, py0 + ly1
            donors = _pad_donor_strips(rgb_arr, px0, py0, pw, ph)
            fill = _texture_fill((gy1 - gy0, gx1 - gx0), donors)
            _feather_blend_region(rgb_arr, gx0, gy0, gx1, gy1, fill, feather=28)
            passes += 1
        else:
            donors = _pad_donor_strips(rgb_arr, px0, py0, pw, ph)
            fill = _texture_fill((ph, pw), donors)
            _feather_blend_region(rgb_arr, px0, py0, px0 + pw, py0 + ph, fill, feather=40)
            passes += 1
        Image.fromarray(np.clip(rgb_arr, 0, 255).astype(np.uint8)).convert("RGBA").save(
            image_path, format="PNG", optimize=True
        )
    return passes


def apply_standalone_cover(
    article_dir: Path,
    root: Path,
    *,
    source_name: str = "cover-canvas.png",
    output_size: tuple[int, int] = DEFAULT_OUTPUT_SIZE,
    skip_pad_clear: bool = False,
) -> dict:
    try:
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError("install Pillow") from exc

    cover_dir = article_dir / "cover"
    source = cover_dir / source_name
    if not source.is_file():
        raise FileNotFoundError(f"missing {source}")

    pad_clear_passes = 0
    if not skip_pad_clear:
        pad_clear_passes = pad_clear_top_right_scene_clone(source)

    out_path = cover_dir / "cover.png"
    pre_dir = cover_dir / PRE_COMPOSITE_DIRNAME
    pre_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(source) as img:
        rgb = img.convert("RGBA")
        if output_size:
            rgb = rgb.resize(output_size, Image.Resampling.LANCZOS)
        rgb.save(out_path, format="PNG", optimize=True)
        src_size = img.size
        out_size = rgb.size

    shutil.copy2(out_path, pre_dir / "cover.png")
    if not skip_pad_clear:
        pad_clear_passes += pad_clear_top_right_scene_clone(out_path)

    from excalibur_blog_drawn_logo_gate import detect_white_plate_in_pad

    plate_after_clear = detect_white_plate_in_pad(out_path)
    if plate_after_clear.get("detected") and float(plate_after_clear.get("pad_ratio") or 0) >= 0.12:
        raise RuntimeError(f"BLOCKER TR plate after pad-clear: {plate_after_clear}")

    report = {
        "source": str(source.relative_to(article_dir)),
        "output": "cover/cover.png",
        "source_size_px": list(src_size),
        "output_size_px": list(out_size),
        "mode": "standalone_16_9",
        "pad_clear_passes": pad_clear_passes,
        "pad_clear_method": "inpaint_bbox_plus_texture_clone_not_white_fill",
        "logo_paste": "deferred_to_brand_logo_composite",
    }
    report_path = cover_dir / "cover-standalone-apply.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description="Apply standalone cover canvas to cover.png")
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--source", default="cover-canvas.png")
    ap.add_argument("--output-size", default="1200x675")
    ap.add_argument("--skip-pad-clear", action="store_true")
    args = ap.parse_args()
    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    try:
        w, h = (int(x) for x in args.output_size.lower().split("x", 1))
        output_size = (w, h)
    except (ValueError, TypeError):
        print("FAIL invalid --output-size", file=sys.stderr)
        return 1
    try:
        report = apply_standalone_cover(
            article_dir,
            root,
            source_name=args.source,
            output_size=output_size,
            skip_pad_clear=bool(args.skip_pad_clear),
        )
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL standalone cover apply: {exc}", file=sys.stderr)
        return 1
    print(f"OK standalone cover → cover.png {report['output_size_px']} pad_clear={report.get('pad_clear_passes')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
