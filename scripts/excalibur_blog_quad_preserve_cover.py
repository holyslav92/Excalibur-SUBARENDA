#!/usr/bin/env python3
"""Restore approved cover quadrant after inline-only canvas-1 regen."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--backup-cover", required=True, help="Path to saved cover.png")
    ap.add_argument("--backup-canvas", required=True, help="Path to saved canvas-quad-01.png")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    cover_dir = article_dir / "cover"
    canvas_path = cover_dir / "canvas-quad-01.png"
    cover_path = cover_dir / "cover.png"
    backup_cover = Path(args.backup_cover)
    backup_canvas = Path(args.backup_canvas)

    for path in (backup_cover, backup_canvas, canvas_path):
        if not path.is_file():
            print(f"FAIL missing {path}", file=sys.stderr)
            return 1

    try:
        from PIL import Image
    except ImportError:
        print("FAIL Pillow required", file=sys.stderr)
        return 1

    canvas = Image.open(canvas_path).convert("RGBA")
    backup = Image.open(backup_canvas).convert("RGBA")
    w, h = canvas.size
    qw, qh = w // 2, h // 2
    cover_quadrant = backup.crop((0, 0, qw, qh))
    canvas.paste(cover_quadrant, (0, 0))
    canvas.save(canvas_path)
    shutil.copy2(backup_cover, cover_path)
    print(f"OK pasted approved cover quadrant onto {canvas_path}")
    print(f"OK restored {cover_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
