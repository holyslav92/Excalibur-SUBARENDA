#!/usr/bin/env python3
"""Pad-clear top-right logo zone on cover panels when AI drew a lockup before factory paste."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _default_logo_panels(cover_dir: Path) -> list[str]:
    names = ["cover.png", "inline-01.png", "inline-03.png", "inline-07.png"]
    return [n for n in names if (cover_dir / n).is_file()]


def clear_panel_logo_pad(panel_path: Path) -> int:
    from excalibur_blog_live_plate_remove_relogo import clear_logo_pad, np_array_rgb_from_pil
    from PIL import Image
    import numpy as np

    img = Image.open(panel_path).convert("RGBA")
    rgb = np_array_rgb_from_pil(img)
    passes = clear_logo_pad(rgb, initial_full_wipe=True)
    Image.fromarray(np.asarray(rgb)).convert("RGBA").save(panel_path)
    return passes


def run_pad_clear(article_dir: Path, panels: list[str], *, remove_pre_composite: bool) -> list[str]:
    cover_dir = article_dir / "cover"
    if not cover_dir.is_dir():
        raise RuntimeError(f"cover dir missing: {cover_dir}")

    cleared: list[str] = []
    for name in panels:
        path = cover_dir / name
        if not path.is_file():
            print(f"WARN skip missing panel: {name}", file=sys.stderr)
            continue
        if name == "cover.png":
            pre_cover = cover_dir / "pre-composite" / "cover.png"
            if pre_cover.is_file():
                shutil.copy2(pre_cover, path)
        passes = clear_panel_logo_pad(path)
        cleared.append(name)
        print(f"OK pad-clear {name} passes={passes}", flush=True)

    if remove_pre_composite and "cover.png" in panels:
        pre = cover_dir / "pre-composite"
        if pre.is_dir():
            shutil.rmtree(pre)

    return cleared


def detect_drawn_lockup_panels(article_dir: Path, root: Path) -> list[str]:
    """Match slim drawn_logo_gate: pre-composite cover + unpasted inline panels only."""
    from excalibur_blog_brand_logo_composite import (
        IMAGE_NAMES,
        load_tenant_logo_config,
        resolve_inline_logo_slots,
        uses_brand_logo_paste,
    )
    from excalibur_blog_drawn_logo_gate import detect_drawn_lockup_in_image

    if not uses_brand_logo_paste(load_tenant_logo_config(root)):
        return []

    cover_dir = article_dir / "cover"
    bad: list[str] = []

    pre_cover = cover_dir / "pre-composite" / "cover.png"
    if pre_cover.is_file():
        result = detect_drawn_lockup_in_image(pre_cover)
        if result.get("detected"):
            bad.append("cover.png")
    elif (cover_dir / "cover.png").is_file():
        result = detect_drawn_lockup_in_image(cover_dir / "cover.png")
        if result.get("detected"):
            bad.append("cover.png")

    inline_with_logo = set(resolve_inline_logo_slots(article_dir, load_tenant_logo_config(root)))
    for name in IMAGE_NAMES:
        if name == "cover.png" or name in inline_with_logo:
            continue
        path = cover_dir / name
        if not path.is_file():
            continue
        if detect_drawn_lockup_in_image(path).get("detected"):
            bad.append(name)

    return bad


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True, help="memory/blog/articles/<topic>-<slug>")
    ap.add_argument(
        "--panels",
        nargs="*",
        default=None,
        help="Panel filenames under cover/ (default: cover + inline 01/03/07 if present)",
    )
    ap.add_argument(
        "--auto-detect",
        action="store_true",
        help="Only pad-clear panels with detected AI-drawn lockup",
    )
    ap.add_argument(
        "--remove-pre-composite",
        action="store_true",
        default=True,
        help="Remove cover/pre-composite before clearing (default: true)",
    )
    ap.add_argument(
        "--no-remove-pre-composite",
        action="store_false",
        dest="remove_pre_composite",
        help="Keep pre-composite snapshots",
    )
    ap.add_argument(
        "--recomposite",
        action="store_true",
        help="Run brand_logo_composite --after-pad-clear after pad-clear",
    )
    args = ap.parse_args()

    root = project_root()
    rel = Path(args.article_dir)
    article_dir = rel if rel.is_absolute() else root / rel
    cover_dir = article_dir / "cover"

    if args.panels:
        panels = list(args.panels)
    else:
        panels = _default_logo_panels(cover_dir)

    if args.auto_detect:
        panels = detect_drawn_lockup_panels(article_dir, root)
        if not panels:
            print("OK no drawn lockup detected — pad-clear skipped")
            return 0
        print(f"auto-detect panels: {panels}", flush=True)

    if not panels:
        print("WARN no panels to pad-clear", file=sys.stderr)
        return 1

    cleared = run_pad_clear(
        article_dir,
        panels,
        remove_pre_composite=bool(args.remove_pre_composite),
    )
    if not cleared:
        return 1

    if args.recomposite:
        import subprocess

        cmd = [
            sys.executable,
            str(root / "scripts" / "excalibur_blog_brand_logo_composite.py"),
            "--article-dir",
            str(rel),
            "--after-pad-clear",
        ]
        print("+", " ".join(cmd), flush=True)
        proc = subprocess.run(
            cmd,
            cwd=root,
            env={**os.environ, "PYTHONPATH": str(root / "scripts")},
        )
        return proc.returncode

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
