#!/usr/bin/env python3
"""Factory poster composite — scene-only canvas + typography + meme paste + phone tablo.

HARD RULE (dobry_dom_scene_composite_v1):
- Grsai generates ONLY empty tender-light hallway (no Cyrillic, digits, meme, logo, phone).
- This script draws headline (Cormorant SemiBold Italic + Onest ~860), pastes ONE catalog meme PNG,
  draws kitchen-tablo phone +7 (993) 574-83-22.
- Official alpha logo is applied AFTER by excalibur_blog_brand_logo_composite.py.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_OUTPUT_SIZE = (1200, 675)
TERRACOTTA_RGB = (158, 74, 54)
CHARCOAL_RGB = (33, 29, 26)
PHONE_BOARD_RGB = (232, 226, 214)
PHONE_BOARD_BORDER = (180, 168, 150)
PHONE_CAPTION_RGB = (90, 82, 74)
FONT_DIR_REL = "memory/cover/assets/fonts"
CORMORANT_REL = f"{FONT_DIR_REL}/Cormorant-SemiBoldItalic.ttf"
ONEST_REL = f"{FONT_DIR_REL}/Onest-ExtraBold.ttf"
MEME_ASSETS_DIR = "memory/cover/memes"
DEFAULT_PHONE = "+7 (993) 574-83-22"
PHONE_CAPTION = "добрый дом • тюмень"


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_font(root: Path, rel: str, size: int, *, fallback: str):
    from PIL import ImageFont

    path = root / rel
    if path.is_file():
        try:
            return ImageFont.truetype(str(path), size=size)
        except OSError:
            pass
    fallback_paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    for fb in fallback_paths:
        if Path(fb).is_file():
            try:
                return ImageFont.truetype(fb, size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def wrap_text(draw, text: str, font, max_width: int) -> list[str]:
    words = text.split()
    if not words:
        return []
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        trial = f"{current} {word}"
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def resolve_headline_lines(manifest: dict) -> tuple[str, str]:
    motifs = manifest.get("cover_motifs") or {}
    line1 = str(manifest.get("cover_headline_line1") or motifs.get("headline_line1") or "").strip()
    line2 = str(manifest.get("cover_headline_line2") or motifs.get("headline_line2") or "").strip()
    hook = str(manifest.get("cover_hook") or "").strip()
    if not line1 and hook:
        if " — " in hook:
            line1, _, line2 = [x.strip() for x in hook.partition(" — ")]
        elif ". " in hook:
            parts = hook.split(". ", 1)
            line1 = parts[0].strip()
            line2 = parts[1].strip() if len(parts) > 1 else ""
        else:
            line1 = hook
    if not line2:
        line2 = str(manifest.get("cover_hook_highlight") or "").strip()
    return line1, line2


def resolve_meme_asset(root: Path, manifest: dict) -> tuple[str, str, Path | None]:
    from excalibur_blog_meme_rotate import pick_cover_meme, load_meme_catalog

    catalog = load_meme_catalog(root)
    picked = pick_cover_meme(manifest, catalog, root)
    meme_id = str(picked.get("id") or "").strip()
    asset_rel = str(picked.get("asset") or "").strip()
    if asset_rel:
        asset_path = root / asset_rel
        if asset_path.is_file():
            return meme_id, str(picked.get("name_ru") or meme_id), asset_path
    fallback = root / MEME_ASSETS_DIR / f"{meme_id}.png"
    if fallback.is_file():
        return meme_id, str(picked.get("name_ru") or meme_id), fallback
    return meme_id, str(picked.get("name_ru") or meme_id), None


def draw_headline_block(draw, line1: str, line2: str, *, width: int, root: Path) -> tuple[int, int, int, int]:
    margin_x = int(width * 0.06)
    max_w = int(width * 0.72)
    y = int(675 * 0.05)
    font_l1 = load_font(root, CORMORANT_REL, 54, fallback="serif")
    font_l2 = load_font(root, ONEST_REL, 42, fallback="sans")

    bbox_top = y
    # Dark backing band so headline reads as display type (QA heuristic + Dzen thumb)
    band_bottom = y + int(font_l1.size * 2.6)
    draw.rectangle((margin_x - 8, bbox_top - 6, margin_x + max_w + 8, band_bottom), fill=(18, 20, 24, 180))
    for line, font, color in ((line1, font_l1, TERRACOTTA_RGB), (line2.lower(), font_l2, (235, 228, 215))):
        if not line:
            continue
        for wrapped in wrap_text(draw, line, font, max_w):
            draw.text((margin_x, y), wrapped, fill=color, font=font)
            y += int(font.size * 1.15)
    bbox_bottom = y
    return margin_x, bbox_top, margin_x + max_w, bbox_bottom


def paste_meme_sticker(base, meme_path: Path, *, width: int, height: int):
    from PIL import Image, ImageOps

    max_w = int(width * 0.22)
    max_h = int(height * 0.28)
    with Image.open(meme_path) as meme_img:
        meme = meme_img.convert("RGBA")
    meme = ImageOps.contain(meme, (max_w, max_h), Image.Resampling.LANCZOS)
    x = int(width * 0.04)
    y = height - meme.height - int(height * 0.06)
    base.alpha_composite(meme, (x, y))
    return (x, y, x + meme.width, y + meme.height)


def draw_phone_tablo(draw, phone: str, *, width: int, height: int, root: Path) -> tuple[int, int, int, int]:
    board_w = int(width * 0.34)
    board_h = int(height * 0.16)
    x0 = width - board_w - int(width * 0.06)
    y0 = int(height * 0.58)
    x1 = x0 + board_w
    y1 = y0 + board_h
    draw.rounded_rectangle((x0, y0, x1, y1), radius=14, fill=PHONE_BOARD_RGB, outline=PHONE_BOARD_BORDER, width=3)
    phone_font = load_font(root, ONEST_REL, 30, fallback="sans")
    caption_font = load_font(root, CORMORANT_REL, 16, fallback="serif")
    phone_w = draw.textlength(phone, font=phone_font)
    draw.text((x0 + (board_w - phone_w) / 2, y0 + board_h * 0.22), phone, fill=CHARCOAL_RGB, font=phone_font)
    cap_w = draw.textlength(PHONE_CAPTION, font=caption_font)
    draw.text(
        (x0 + (board_w - cap_w) / 2, y0 + board_h * 0.62),
        PHONE_CAPTION,
        fill=PHONE_CAPTION_RGB,
        font=caption_font,
    )
    return (int(x0), int(y0), int(x1), int(y1))


def composite_poster_cover(
    article_dir: Path,
    root: Path,
    *,
    source_name: str = "cover-canvas.png",
    output_size: tuple[int, int] = DEFAULT_OUTPUT_SIZE,
) -> dict[str, Any]:
    from PIL import Image, ImageDraw

    cover_dir = article_dir / "cover"
    source = cover_dir / source_name
    if not source.is_file():
        raise FileNotFoundError(f"missing {source}")

    manifest_path = cover_dir / "quad-manifest.json"
    manifest = load_json(manifest_path) if manifest_path.is_file() else {}
    line1, line2 = resolve_headline_lines(manifest)
    if not line1:
        raise ValueError("cover headline line1 missing in quad-manifest — set cover_headline_line1/cover_hook")

    phone = str(manifest.get("cover_phone_cta") or DEFAULT_PHONE).strip()
    meme_id, meme_name, meme_path = resolve_meme_asset(root, manifest)
    if meme_path is None:
        raise FileNotFoundError(
            f"catalog meme asset missing for id={meme_id!r} — add memory/cover/memes/{meme_id}.png"
        )

    try:
        from excalibur_blog_cover_collage_gate import validate_scene_only_canvas

        scene_errors = validate_scene_only_canvas(source)
        if scene_errors:
            raise RuntimeError(f"scene-only canvas BLOCKER: {'; '.join(scene_errors)}")
    except ImportError:
        pass

    with Image.open(source) as scene_img:
        base = scene_img.convert("RGBA").resize(output_size, Image.Resampling.LANCZOS)

    draw = ImageDraw.Draw(base)
    w, h = base.size
    headline_bbox = draw_headline_block(draw, line1, line2, width=w, root=root)
    meme_bbox = paste_meme_sticker(base, meme_path, width=w, height=h)
    draw = ImageDraw.Draw(base)
    phone_bbox = draw_phone_tablo(draw, phone, width=w, height=h, root=root)

    out_path = cover_dir / "cover.png"
    base.convert("RGB").save(out_path, format="PNG", optimize=True)

    stamp = {
        "status": "PASS",
        "mode": "scene_composite_v1",
        "agent": "excalibur-blog-cover",
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "source_scene": str(source.relative_to(article_dir)),
        "output": "cover/cover.png",
        "headline": {"line1": line1, "line2": line2, "bbox": list(headline_bbox)},
        "meme": {"id": meme_id, "name_ru": meme_name, "asset": str(meme_path.relative_to(root)), "bbox": list(meme_bbox)},
        "phone": {"display": phone, "bbox": list(phone_bbox)},
        "fonts": {"line1": CORMORANT_REL, "line2": ONEST_REL},
        "logo_paste": "deferred_to_brand_logo_composite",
    }
    stamp_path = cover_dir / "poster-composite-stamp.json"
    stamp_path.write_text(json.dumps(stamp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return stamp


def main() -> int:
    ap = argparse.ArgumentParser(description="Factory poster composite for scene-only cover canvas")
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
        stamp = composite_poster_cover(article_dir, root, source_name=args.source, output_size=output_size)
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL poster composite: {exc}", file=sys.stderr)
        return 1
    print(f"OK poster composite meme={stamp['meme']['id']} → cover.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
