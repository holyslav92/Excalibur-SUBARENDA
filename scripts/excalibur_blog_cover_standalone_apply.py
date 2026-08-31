#!/usr/bin/env python3
"""Apply standalone cover canvas (2048×1152) → cover.png + logo composite."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEFAULT_OUTPUT_SIZE = (1200, 675)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def apply_standalone_cover(
    article_dir: Path,
    root: Path,
    *,
    source_name: str = "cover-canvas.png",
    output_size: tuple[int, int] = DEFAULT_OUTPUT_SIZE,
) -> dict:
    try:
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError("install Pillow") from exc

    cover_dir = article_dir / "cover"
    source = cover_dir / source_name
    if not source.is_file():
        raise FileNotFoundError(f"missing {source}")

    out_path = cover_dir / "cover.png"
    with Image.open(source) as img:
        rgb = img.convert("RGBA")
        if output_size:
            rgb = rgb.resize(output_size, Image.Resampling.LANCZOS)
        rgb.save(out_path, format="PNG", optimize=True)
        src_size = img.size
        out_size = rgb.size

    from excalibur_blog_brand_logo_composite import (
        composite_logo_onto_image,
        load_tenant_logo_config,
        uses_brand_logo_paste,
    )

    cfg = load_tenant_logo_config(root)
    if uses_brand_logo_paste(cfg):
        logo_path = root / str(cfg["logo_rel"])
        composite_logo_onto_image(
            out_path,
            logo_path,
            max_width_fraction=float(cfg.get("max_width_fraction") or 0.10),
            margin_px=int(cfg.get("margin_px") or 20),
            phone_display=str(cfg.get("phone_display") or ""),
            add_phone=False,
            adaptive_corner=False,
            fixed_corner=str(cfg.get("logo_corner") or "top_right"),
            paste_logo=True,
        )

    report = {
        "source": str(source.relative_to(article_dir)),
        "output": "cover/cover.png",
        "source_size_px": list(src_size),
        "output_size_px": list(out_size),
        "mode": "standalone_16_9",
    }
    report_path = cover_dir / "cover-standalone-apply.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description="Apply standalone cover canvas to cover.png")
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--source", default="cover-canvas.png")
    ap.add_argument("--output-size", default="1200x675")
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
        )
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL standalone cover apply: {exc}", file=sys.stderr)
        return 1
    print(f"OK standalone cover → cover.png {report['output_size_px']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
