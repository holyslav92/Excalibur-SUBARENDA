#!/usr/bin/env python3
"""Factory poster composite — story collage canvas + typography + optional meme + phone bar.

HARD RULE (dobry_dom_dzen_story_collage_v1):
- Grsai generates photoreal story collage scene (theme-derived hero; no Cyrillic/digits/meme/logo/phone).
- This script draws Onest ~860 black headline + yellow/peach brush highlight on ONE keyword,
  ONE yellow sticky-note punch, phone bar +7 (993) 574-83-22, optional ONE catalog meme PNG paste.
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
CHARCOAL_RGB = (33, 29, 26)
BRUSH_RGB = (255, 210, 80)
STICKY_RGB = (255, 235, 80)
STICKY_BORDER = (220, 200, 60)
PHONE_BAR_RGB = (245, 240, 230)
PHONE_BAR_BORDER = (200, 190, 175)
PHONE_CAPTION_RGB = (90, 82, 74)
FONT_DIR_REL = "memory/cover/assets/fonts"
ONEST_REL = f"{FONT_DIR_REL}/Onest-ExtraBold.ttf"
MEME_ASSETS_DIR = "memory/cover/memes"
DEFAULT_PHONE = "+7 (993) 574-83-22"
FORBIDDEN_PHONE = "+7 922 001 65 05"
PHONE_CAPTION = "добрый дом • тюмень"
POSTER_MODE = "dzen_story_collage_v1"


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
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
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


def resolve_highlight_keyword(manifest: dict, line1: str, line2: str) -> str:
    kw = str(manifest.get("cover_hook_highlight") or "").strip()
    if kw:
        return kw
    for line in (line2, line1):
        for token in line.replace("—", " ").replace(":", " ").split():
            cleaned = token.strip("«»\"'.,!?")
            if len(cleaned) >= 3 and any(ch.isdigit() for ch in cleaned):
                return cleaned
            if len(cleaned) >= 4:
                return cleaned
    return ""


def resolve_sticky_text(manifest: dict) -> str:
    cover_slot = (manifest.get("slots") or {}).get("cover") or {}
    for key in ("sticky", "cover_quote", "meme_caption_ru"):
        val = str(cover_slot.get(key) or manifest.get(f"cover_{key}" if key != "sticky" else "cover_quote") or "").strip()
        if val:
            return val[:48]
    return ""


def resolve_meme_asset(root: Path, manifest: dict) -> tuple[str, str, Path | None]:
    from excalibur_blog_meme_rotate import pick_cover_meme, load_meme_catalog

    cover_slot = (manifest.get("slots") or {}).get("cover") or {}
    forced_id = str(cover_slot.get("meme_id") or manifest.get("cover_meme_id") or "").strip()
    if not forced_id and not manifest.get("cover_meme_required"):
        return "", "", None

    catalog = load_meme_catalog(root)
    picked = pick_cover_meme(manifest, catalog, root)
    meme_id = str(picked.get("id") or forced_id or "").strip()
    if not meme_id:
        return "", "", None
    asset_rel = str(picked.get("asset") or "").strip()
    if asset_rel:
        asset_path = root / asset_rel
        if asset_path.is_file():
            return meme_id, str(picked.get("name_ru") or meme_id), asset_path
    fallback = root / MEME_ASSETS_DIR / f"{meme_id}.png"
    if fallback.is_file():
        return meme_id, str(picked.get("name_ru") or meme_id), fallback
    return meme_id, str(picked.get("name_ru") or meme_id), None


def draw_brush_highlight(draw, x: int, y: int, width: int, height: int) -> None:
    pad = 4
    draw.rounded_rectangle(
        (x - pad, y + int(height * 0.55), x + width + pad, y + height + pad),
        radius=8,
        fill=BRUSH_RGB,
    )


def draw_headline_block(
    draw,
    line1: str,
    line2: str,
    *,
    width: int,
    root: Path,
    highlight_kw: str,
) -> tuple[int, int, int, int]:
    margin_x = int(width * 0.05)
    max_w = int(width * 0.55)
    y = int(675 * 0.06)
    font_l1 = load_font(root, ONEST_REL, 46, fallback="sans")
    font_l2 = load_font(root, ONEST_REL, 40, fallback="sans")
    font_kw = load_font(root, ONEST_REL, 40, fallback="sans")

    bbox_top = y
    for line, font in ((line1, font_l1), (line2, font_l2)):
        if not line:
            continue
        for wrapped in wrap_text(draw, line, font, max_w):
            if highlight_kw and highlight_kw.casefold() in wrapped.casefold():
                parts = wrapped.split(highlight_kw, 1)
                if len(parts) == 2:
                    before, after = parts
                    x_cursor = margin_x
                    if before:
                        draw.text((x_cursor, y), before, fill=CHARCOAL_RGB, font=font)
                        x_cursor += int(draw.textlength(before, font=font))
                    kw_w = int(draw.textlength(highlight_kw, font=font_kw))
                    bbox = draw.textbbox((x_cursor, y), highlight_kw, font=font_kw)
                    draw_brush_highlight(draw, x_cursor, bbox[1], kw_w, bbox[3] - bbox[1])
                    draw.text((x_cursor, y), highlight_kw, fill=CHARCOAL_RGB, font=font_kw)
                    if after:
                        draw.text((x_cursor + kw_w, y), after, fill=CHARCOAL_RGB, font=font)
                else:
                    draw.text((margin_x, y), wrapped, fill=CHARCOAL_RGB, font=font)
            else:
                draw.text((margin_x, y), wrapped, fill=CHARCOAL_RGB, font=font)
            y += int(font.size * 1.12)
    return margin_x, bbox_top, margin_x + max_w, y


def draw_sticky_note(draw, text: str, *, width: int, root: Path) -> tuple[int, int, int, int] | None:
    if not text:
        return None
    note_w = int(width * 0.28)
    note_h = int(width * 0.14)
    x0 = int(width * 0.04)
    y0 = int(675 * 0.02)
    x1 = x0 + note_w
    y1 = y0 + note_h
    draw.polygon(
        [(x0, y0), (x1, y0), (x1, y1 - 12), (x1 - 12, y1), (x0, y1)],
        fill=STICKY_RGB,
        outline=STICKY_BORDER,
    )
    font = load_font(root, ONEST_REL, 18, fallback="sans")
    inner_w = note_w - 16
    lines = wrap_text(draw, text, font, inner_w)[:3]
    ty = y0 + 10
    for ln in lines:
        draw.text((x0 + 8, ty), ln, fill=CHARCOAL_RGB, font=font)
        ty += int(font.size * 1.1)
    return (x0, y0, x1, y1)


def paste_meme_sticker(base, meme_path: Path, *, width: int, height: int):
    from PIL import Image, ImageOps

    max_w = int(width * 0.18)
    max_h = int(height * 0.22)
    with Image.open(meme_path) as meme_img:
        meme = meme_img.convert("RGBA")
    meme = ImageOps.contain(meme, (max_w, max_h), Image.Resampling.LANCZOS)
    x = int(width * 0.04)
    y = height - meme.height - int(height * 0.14)
    base.alpha_composite(meme, (x, y))
    return (x, y, x + meme.width, y + meme.height)


def draw_phone_bar(draw, phone: str, *, width: int, height: int, root: Path) -> tuple[int, int, int, int]:
    if FORBIDDEN_PHONE.replace(" ", "") in phone.replace(" ", ""):
        raise ValueError(f"forbidden realtor phone {phone!r} — use {DEFAULT_PHONE}")
    bar_h = int(height * 0.11)
    bar_w = int(width * 0.36)
    x0 = width - bar_w - int(width * 0.04)
    y0 = height - bar_h - int(height * 0.04)
    x1 = x0 + bar_w
    y1 = y0 + bar_h
    draw.rounded_rectangle((x0, y0, x1, y1), radius=10, fill=PHONE_BAR_RGB, outline=PHONE_BAR_BORDER, width=2)
    phone_font = load_font(root, ONEST_REL, 26, fallback="sans")
    caption_font = load_font(root, ONEST_REL, 13, fallback="sans")
    phone_w = draw.textlength(phone, font=phone_font)
    draw.text((x0 + (bar_w - phone_w) / 2, y0 + bar_h * 0.18), phone, fill=CHARCOAL_RGB, font=phone_font)
    cap_w = draw.textlength(PHONE_CAPTION, font=caption_font)
    draw.text(
        (x0 + (bar_w - cap_w) / 2, y0 + bar_h * 0.58),
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
    highlight_kw = resolve_highlight_keyword(manifest, line1, line2)
    sticky_text = resolve_sticky_text(manifest)
    meme_id, meme_name, meme_path = resolve_meme_asset(root, manifest)

    try:
        from excalibur_blog_cover_collage_gate import validate_story_scene_canvas

        scene_errors = validate_story_scene_canvas(source)
        if scene_errors:
            raise RuntimeError(f"story scene canvas BLOCKER: {'; '.join(scene_errors)}")
    except ImportError:
        pass

    with Image.open(source) as scene_img:
        base = scene_img.convert("RGBA").resize(output_size, Image.Resampling.LANCZOS)

    draw = ImageDraw.Draw(base)
    w, h = base.size
    sticky_bbox = draw_sticky_note(draw, sticky_text, width=w, root=root)
    headline_bbox = draw_headline_block(draw, line1, line2, width=w, root=root, highlight_kw=highlight_kw)
    meme_bbox: tuple[int, int, int, int] | None = None
    if meme_path is not None:
        meme_bbox = paste_meme_sticker(base, meme_path, width=w, height=h)
    draw = ImageDraw.Draw(base)
    phone_bbox = draw_phone_bar(draw, phone, width=w, height=h, root=root)

    out_path = cover_dir / "cover.png"
    base.convert("RGB").save(out_path, format="PNG", optimize=True)

    stamp: dict[str, Any] = {
        "status": "PASS",
        "mode": POSTER_MODE,
        "agent": "excalibur-blog-cover",
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "source_scene": str(source.relative_to(article_dir)),
        "output": "cover/cover.png",
        "headline": {
            "line1": line1,
            "line2": line2,
            "highlight_keyword": highlight_kw,
            "bbox": list(headline_bbox),
        },
        "sticky_note": {"text": sticky_text, "bbox": list(sticky_bbox) if sticky_bbox else None},
        "phone": {"display": phone, "bbox": list(phone_bbox)},
        "fonts": {"headline": ONEST_REL},
        "logo_paste": "deferred_to_brand_logo_composite",
    }
    if meme_id:
        stamp["meme"] = {
            "id": meme_id,
            "name_ru": meme_name,
            "asset": str(meme_path.relative_to(root)) if meme_path else None,
            "bbox": list(meme_bbox) if meme_bbox else None,
        }
    stamp_path = cover_dir / "poster-composite-stamp.json"
    stamp_path.write_text(json.dumps(stamp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return stamp


def main() -> int:
    print(
        "BLOCKER: excalibur_blog_cover_poster_composite.py disabled — "
        "dobry_dom_dzen_story_collage_v2 draws Cyrillic headline/sticky/phone IN Grsai generation; "
        "only brand_logo_composite may post-process (official logo paste pixel-faithful on cover).",
        file=sys.stderr,
    )
    return 1


def _legacy_main_disabled() -> int:
    ap = argparse.ArgumentParser(description="Factory poster composite for Dzen story collage cover canvas")
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
    meme_note = f" meme={stamp['meme']['id']}" if stamp.get("meme") else ""
    print(f"OK poster composite{meme_note} → cover.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
