#!/usr/bin/env python3
"""Paste canonical Dobry Dom brand PNG onto cover/inline panels (alpha composite).

NEVER ask image models to draw/restyle the logo — factory pastes cropped-img_7143.png 1:1.
Crop to non-transparent getbbox() before resize — never paste the full empty square.
Never draw white/card/plate backing under the lockup — alpha overlay only.
Cover phone is painted IN the scene during generation — NEVER post-composite pill overlay.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_LOGO_REL = "memory/cover/assets/brand/logo-dobry-dom.png"
PRE_COMPOSITE_DIRNAME = "pre-composite"
CANONICAL_SHA256 = "72e53ba966f0626cc6eaad0792e68b57c8da0ccd9265d6822fbc173fdb48b941"
LOGO_WIDTH_FRACTION_MIN = 0.08
LOGO_WIDTH_FRACTION_MAX = 0.12
LOGO_WIDTH_FRACTION_DEFAULT = 0.10
FIXED_LOGO_CORNER = "top_right"
INLINE_LOGO_COUNT_MIN = 0
INLINE_LOGO_COUNT_MAX = 0
DEFAULT_INLINE_LOGO_SLOTS: tuple[str, ...] = ()
DEFAULT_PHONE_DISPLAY = "+7 (993) 574-83-22"
DEFAULT_PHONE_TEL = "tel:+79935748322"
FORBIDDEN_PHONE_DIGITS = (
    "9220016505",
    "79220016505",
)
IMAGE_NAMES = (
    "cover.png",
    "inline-01.png",
    "inline-02.png",
    "inline-03.png",
    "inline-04.png",
    "inline-05.png",
    "inline-06.png",
    "inline-07.png",
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def normalize_phone_digits(value: str) -> str:
    return re.sub(r"\D", "", value or "")


def load_tenant_logo_config(root: Path) -> dict[str, Any]:
    cfg_path = root / "shared" / "tenant-config.json"
    if not cfg_path.is_file():
        return {}
    try:
        tenant = json.loads(cfg_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    channels = tenant.get("cta_channels") or {}
    hero_rel = (tenant.get("cover_files") or {}).get("hero") or "memory/cover/blog-hero.json"
    hero: dict[str, Any] = {}
    hero_path = root / hero_rel
    if hero_path.is_file():
        try:
            hero = json.loads(hero_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            hero = {}
    composite = hero.get("logo_composite") or tenant.get("logo_composite") or {}
    logo_rel = composite.get("logo_asset") or hero.get("reference_image") or DEFAULT_LOGO_REL
    phone_display = str(channels.get("phone_display") or DEFAULT_PHONE_DISPLAY).strip()
    phone_raw = str(channels.get("phone") or "+79935748322").strip()
    return {
        "cover_mode": tenant.get("cover_mode") or hero.get("cover_mode") or "",
        "logo_mode": tenant.get("logo_mode") or tenant.get("cover_mode") or hero.get("cover_mode") or "",
        "logo_rel": str(logo_rel),
        "logo_sha256": str(composite.get("canonical_sha256") or CANONICAL_SHA256),
        "max_width_fraction": float(
            composite.get("max_width_fraction") or LOGO_WIDTH_FRACTION_DEFAULT
        ),
        "min_width_fraction": float(
            composite.get("min_width_fraction") or LOGO_WIDTH_FRACTION_MIN
        ),
        "max_width_fraction_cap": float(
            composite.get("max_width_fraction_cap") or LOGO_WIDTH_FRACTION_MAX
        ),
        "margin_px": int(composite.get("margin_px") or 20),
        "logo_corner": str(composite.get("logo_corner") or FIXED_LOGO_CORNER).strip().casefold(),
        "inline_logo_count_min": int(composite.get("inline_logo_count_min") or INLINE_LOGO_COUNT_MIN),
        "inline_logo_count_max": int(composite.get("inline_logo_count_max") or INLINE_LOGO_COUNT_MAX),
        "inline_logo_slots_default": list(
            composite.get("inline_logo_slots_default") or list(DEFAULT_INLINE_LOGO_SLOTS)
        ),
        "phone_display": phone_display,
        "phone_tel": f"tel:+{normalize_phone_digits(phone_raw).lstrip('0')}" if phone_raw else DEFAULT_PHONE_TEL,
        "cover_phone_required": True,
    }


def uses_brand_logo_paste(cfg: dict[str, Any]) -> bool:
    mode = str(cfg.get("cover_mode") or "").strip().casefold()
    logo_mode = str(cfg.get("logo_mode") or mode).strip().casefold()
    if mode in {"full_grsai_cover", "grsai_full_cover"}:
        return False
    if logo_mode in {"drawn_in_generation", "full_grsai_cover"}:
        return False
    if logo_mode in {"reference_in_generation", "logo_reference_in_generation", "reference_in_gen"}:
        return False
    return mode in {"brand_logo_paste", "brand_logo_composite", "paste_png"}


def uses_logo_reference_in_generation(cfg: dict[str, Any]) -> bool:
    mode = str(cfg.get("logo_mode") or cfg.get("cover_mode") or "").strip().casefold()
    return mode in {"reference_in_generation", "logo_reference_in_generation", "reference_in_gen"}


def _load_font(size: int):
    from PIL import ImageFont

    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ):
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def _corner_busyness(rgb_arr, x0: int, y0: int, box_w: int, box_h: int) -> float:
    """Меньше = пустее участок (лучше для логотипа)."""
    import numpy as np

    patch = rgb_arr[y0 : y0 + box_h, x0 : x0 + box_w]
    if patch.size == 0:
        return float("inf")
    gray = patch.mean(axis=2)
    edge_y = float(np.abs(np.diff(gray, axis=0)).mean()) if gray.shape[0] > 1 else 0.0
    edge_x = float(np.abs(np.diff(gray, axis=1)).mean()) if gray.shape[1] > 1 else 0.0
    return edge_y + edge_x + float(gray.std()) * 0.35


def pick_logo_corner(
    base,
    logo_w: int,
    logo_h: int,
    *,
    margin_px: int,
) -> tuple[int, int, str]:
    """Выбрать угол с наименьшей «занятостью» — не клеить логотип поверх мема/стикера."""
    import numpy as np

    arr = np.array(base.convert("RGB"))
    h, w = arr.shape[:2]
    candidates: list[tuple[str, int, int]] = [
        ("top_left", margin_px, margin_px),
        ("top_right", max(margin_px, w - logo_w - margin_px), margin_px),
        ("bottom_left", margin_px, max(margin_px, h - logo_h - margin_px)),
        (
            "bottom_right",
            max(margin_px, w - logo_w - margin_px),
            max(margin_px, h - logo_h - margin_px),
        ),
    ]
    best_name = "top_left"
    best_x, best_y = margin_px, margin_px
    best_score = float("inf")
    for name, x0, y0 in candidates:
        score = _corner_busyness(arr, x0, y0, logo_w, logo_h)
        if score < best_score:
            best_score = score
            best_name = name
            best_x, best_y = x0, y0
    return best_x, best_y, best_name


def phone_anchor_for_logo_corner(logo_corner: str) -> str:
    """Телефон — в угол, диагонально противоположный логотипу (не перекрывать)."""
    return {
        "top_left": "bottom_right",
        "top_right": "bottom_left",
        "bottom_left": "top_right",
        "bottom_right": "top_left",
    }.get(logo_corner, "bottom_left")


def inline_file_for_slot(slot_key: str) -> str:
    if slot_key == "cover":
        return "cover.png"
    m = re.match(r"inline_(\d+)$", slot_key.strip())
    if m:
        return f"inline-{int(m.group(1)):02d}.png"
    return slot_key


def slot_key_for_inline_file(name: str) -> str:
    m = re.match(r"inline-(\d+)\.png$", name.strip())
    if m:
        return f"inline_{int(m.group(1))}"
    if name == "cover.png":
        return "cover"
    return name


def _inline_logo_bounds(cfg: dict[str, Any]) -> tuple[int, int]:
    lo_raw = cfg.get("inline_logo_count_min")
    hi_raw = cfg.get("inline_logo_count_max")
    lo = INLINE_LOGO_COUNT_MIN if lo_raw is None else int(lo_raw)
    hi = INLINE_LOGO_COUNT_MAX if hi_raw is None else int(hi_raw)
    return lo, hi


def resolve_inline_logo_slots(article_dir: Path, cfg: dict[str, Any]) -> list[str]:
    """Какие inline-файлы получают factory logo paste (factory lock: 0 — только cover)."""
    lo, hi = _inline_logo_bounds(cfg)
    if lo == 0 and hi == 0:
        return []

    manifest_path = article_dir / "cover" / "quad-manifest.json"
    manifest_slots: list[str] = []
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            raw = manifest.get("logo_paste_inline_slots") or manifest.get("inline_logo_slots")
            if isinstance(raw, list) and raw:
                manifest_slots = [str(x).strip() for x in raw if str(x).strip()]
        except json.JSONDecodeError:
            manifest_slots = []

    if manifest_slots:
        files = [inline_file_for_slot(k) if not k.endswith(".png") else k for k in manifest_slots]
    else:
        defaults = cfg.get("inline_logo_slots_default") or list(DEFAULT_INLINE_LOGO_SLOTS)
        files = [inline_file_for_slot(str(k)) for k in defaults]

    files = [f for f in files if f.startswith("inline-") and f.endswith(".png")]
    if len(files) < lo:
        raise ValueError(
            f"inline logo slots {len(files)} < factory min {lo} — set logo_paste_inline_slots in quad-manifest"
        )
    if len(files) > hi:
        files = files[:hi]
    return files


def fixed_logo_xy(base, logo_w: int, logo_h: int, *, margin_px: int, corner: str) -> tuple[int, int]:
    corner = (corner or FIXED_LOGO_CORNER).casefold()
    if corner == "top_right":
        return max(margin_px, base.width - logo_w - margin_px), margin_px
    if corner == "bottom_right":
        return max(margin_px, base.width - logo_w - margin_px), max(margin_px, base.height - logo_h - margin_px)
    if corner == "bottom_left":
        return margin_px, max(margin_px, base.height - logo_h - margin_px)
    return margin_px, margin_px


def draw_phone_on_cover(*_args, **_kwargs) -> None:
    """Запрещено: post-composite pill перекрывал мем/кота на обложке 1 сент."""
    raise ValueError(
        "cover phone post-composite pill is forbidden — paint +7 (993) 574-83-22 IN the scene during generation"
    )


LOGO_SOURCE_CANVAS_PX = 512
# cropped-img_7143.png opaque glyph bbox on 512² canvas (alpha-only outside).
LOGO_CROP_BBOX_CANON = (18, 90, 490, 413)


def assert_logo_paste_not_full_canvas(logo) -> None:
    """Блок: paste полного 512² квадрата с пустым padding = opaque card на сцене."""
    if logo.width >= LOGO_SOURCE_CANVAS_PX - 4 and logo.height >= LOGO_SOURCE_CANVAS_PX - 4:
        raise ValueError(
            f"logo paste is full {LOGO_SOURCE_CANVAS_PX}px canvas ({logo.width}x{logo.height}); "
            "call prepare_logo_rgba (getbbox crop) before alpha_composite"
        )


def prepare_logo_rgba(logo_path: Path, max_width_px: int):
    """Crop logo to opaque bbox, resize to target width — RGBA only, no white flatten."""
    from PIL import Image

    with Image.open(logo_path) as logo_img:
        logo = logo_img.convert("RGBA")
    bbox = logo.getbbox()
    if not bbox:
        raise ValueError(f"logo has no opaque pixels: {logo_path}")
    logo = logo.crop(bbox)
    assert_logo_paste_not_full_canvas(logo)
    max_w = max(32, int(max_width_px))
    if logo.width > max_w:
        scale = max_w / logo.width
        logo = logo.resize(
            (max_w, max(1, int(logo.height * scale))),
            Image.Resampling.LANCZOS,
        )
    return logo


def clamp_logo_fraction(value: float, cfg: dict[str, Any] | None = None) -> float:
    cfg = cfg or {}
    lo = float(cfg.get("min_width_fraction") or LOGO_WIDTH_FRACTION_MIN)
    hi = float(cfg.get("max_width_fraction_cap") or LOGO_WIDTH_FRACTION_MAX)
    target = float(cfg.get("max_width_fraction") or LOGO_WIDTH_FRACTION_DEFAULT)
    return max(lo, min(hi, target))


def snapshot_pre_composite(image_path: Path, pre_dir: Path) -> tuple[Path, bool]:
    """Сохранить копию до factory paste — для QA drawn-lockup gate."""
    pre_dir.mkdir(parents=True, exist_ok=True)
    dest = pre_dir / image_path.name
    if dest.is_file():
        return dest, False
    shutil.copy2(image_path, dest)
    return dest, True


def restore_or_snapshot_pre_composite(image_path: Path, pre_dir: Path) -> tuple[Path, bool]:
    """Вернуть generation-only panel: restore из pre-composite или создать snapshot."""
    pre_path, created = snapshot_pre_composite(image_path, pre_dir)
    if not created:
        shutil.copy2(pre_path, image_path)
    return pre_path, created


def assert_no_drawn_lockup_before_paste(image_path: Path) -> None:
    from excalibur_blog_drawn_logo_gate import detect_drawn_lockup_in_image

    result = detect_drawn_lockup_in_image(image_path)
    if result.get("detected"):
        reasons = ", ".join(result.get("reasons") or [])
        raise ValueError(
            f"AI-drawn lockup in {image_path.name} before factory paste "
            f"(score={result.get('score')}, {reasons}) — regenerate panel with empty top-right pad"
        )


def composite_logo_onto_image(
    image_path: Path,
    logo_path: Path,
    *,
    max_width_fraction: float = LOGO_WIDTH_FRACTION_DEFAULT,
    margin_px: int = 20,
    phone_display: str = "",
    add_phone: bool = False,
    adaptive_corner: bool = False,
    fixed_corner: str = FIXED_LOGO_CORNER,
    paste_logo: bool = True,
    pre_snapshot_dir: Path | None = None,
    block_drawn_lockup: bool = True,
) -> dict[str, Any]:
    from PIL import Image

    if pre_snapshot_dir is not None:
        pre_path, created = restore_or_snapshot_pre_composite(image_path, pre_snapshot_dir)
        if paste_logo and block_drawn_lockup and created:
            assert_no_drawn_lockup_before_paste(pre_path)

    with Image.open(image_path) as base_img:
        base = base_img.convert("RGBA")
        corner = str(fixed_corner or FIXED_LOGO_CORNER).casefold()
        phone_anchor = phone_anchor_for_logo_corner(corner)
        if paste_logo:
            max_w = max(32, int(base.width * max_width_fraction))
            logo = prepare_logo_rgba(logo_path, max_w)
            if adaptive_corner:
                x, y, corner = pick_logo_corner(base, logo.width, logo.height, margin_px=margin_px)
            else:
                x, y = fixed_logo_xy(
                    base, logo.width, logo.height, margin_px=margin_px, corner=corner
                )
            # Alpha-composite only — never paste with mask on RGB, never draw backing plate.
            base.alpha_composite(logo, (max(0, x), max(0, y)))
            logo_width_fraction = round(logo.width / max(base.width, 1), 4)
            logo_width_px = int(logo.width)
            logo_height_px = int(logo.height)
            logo_xy = [int(x), int(y)]
        else:
            logo_width_fraction = 0.0
            logo_width_px = 0
            logo_height_px = 0
            logo_xy = []
        if add_phone and phone_display:
            draw_phone_on_cover(base, phone_display, anchor=phone_anchor, margin_px=margin_px)
        base.save(image_path, format="PNG", optimize=True)
    return {
        "logo_corner": corner if paste_logo else "",
        "logo_xy": logo_xy,
        "logo_width_px": logo_width_px,
        "logo_height_px": logo_height_px,
        "logo_width_fraction": logo_width_fraction,
        "phone_anchor": phone_anchor if add_phone else "",
        "logo_pasted": bool(paste_logo),
    }


def composite_article_images(
    article_dir: Path,
    root: Path,
    *,
    force: bool = False,
    cover_only: bool = False,
    phone_only: bool = False,
    emergency: bool = False,
    after_pad_clear: bool = False,
) -> dict[str, Any]:
    cfg = load_tenant_logo_config(root)
    if phone_only:
        raise ValueError(
            "--phone-only forbidden: cover phone must be painted IN the scene during generation, "
            "never as post-composite pill overlay"
        )
    if not uses_brand_logo_paste(cfg) and not force and not emergency:
        return {"status": "SKIP", "reason": "cover_mode is not brand_logo_paste"}

    logo_path = root / cfg["logo_rel"]
    if not logo_path.is_file():
        raise FileNotFoundError(f"brand logo missing: {logo_path}")

    logo_sha = sha256_file(logo_path)
    expected = str(cfg.get("logo_sha256") or CANONICAL_SHA256)
    if logo_sha != expected:
        raise ValueError(
            f"brand logo sha256 mismatch: got {logo_sha}, expected {expected} ({logo_path})"
        )

    phone_display = str(cfg.get("phone_display") or DEFAULT_PHONE_DISPLAY)
    logo_fraction = clamp_logo_fraction(float(cfg.get("max_width_fraction") or LOGO_WIDTH_FRACTION_DEFAULT), cfg)
    logo_corner = str(cfg.get("logo_corner") or FIXED_LOGO_CORNER).casefold()
    inline_logo_files = resolve_inline_logo_slots(article_dir, cfg)
    cover_dir = article_dir / "cover"
    pre_composite_dir = cover_dir / PRE_COMPOSITE_DIRNAME
    composed: list[str] = []
    cover_placement: dict[str, Any] = {}
    panel_placements: dict[str, Any] = {}
    panel_skipped: dict[str, str] = {}
    targets = ("cover.png",) if cover_only else IMAGE_NAMES
    for name in targets:
        img_path = cover_dir / name
        if not img_path.is_file():
            raise FileNotFoundError(f"missing panel image: {img_path}")
        paste_logo = name == "cover.png" or name in inline_logo_files
        placement = composite_logo_onto_image(
            img_path,
            logo_path,
            max_width_fraction=logo_fraction,
            margin_px=int(cfg.get("margin_px") or 20),
            phone_display=phone_display,
            add_phone=False,
            adaptive_corner=False,
            fixed_corner=logo_corner,
            paste_logo=paste_logo,
            pre_snapshot_dir=pre_composite_dir,
            block_drawn_lockup=not after_pad_clear,
        )
        if name == "cover.png":
            cover_placement = placement
        elif paste_logo:
            panel_placements[name] = placement
        else:
            panel_skipped[name] = "no_factory_logo_by_rule"
        composed.append(f"cover/{name}")

    stamp = {
        "status": "PASS",
        "mode": "paste_png_alpha",
        "logo_path": cfg["logo_rel"],
        "logo_sha256": logo_sha,
        "logo_corner_fixed": logo_corner,
        "logo_width_fraction_target": logo_fraction,
        "logo_width_fraction_min": float(cfg.get("min_width_fraction") or LOGO_WIDTH_FRACTION_MIN),
        "logo_width_fraction_max": float(cfg.get("max_width_fraction_cap") or LOGO_WIDTH_FRACTION_MAX),
        "inline_logo_files": inline_logo_files,
        "inline_logo_count": len(inline_logo_files),
        "cover_phone_display": phone_display,
        "cover_phone_in_scene_generation": True,
        "cover_phone_post_composite": False,
        "forbid_logo_as_generation_reference": True,
        "cover_logo_placement": cover_placement,
        "panel_logo_placements": panel_placements,
        "panel_logo_skipped": panel_skipped,
        "images": composed,
        "composed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "forbid_ai_drawn_logo": True,
        "forbid_logo_white_plate": True,
        "logo_crop_getbbox": True,
        "forbid_multiple_logos_per_image": True,
        "adaptive_logo_corner_all_panels": False,
        "inline_phone_required": False,
        "pre_composite_dir": f"cover/{PRE_COMPOSITE_DIRNAME}",
    }
    stamp_path = cover_dir / "logo-composite-stamp.json"
    stamp_path.write_text(json.dumps(stamp, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return stamp


def validate_logo_stamp(article_dir: Path, root: Path) -> list[str]:
    errors: list[str] = []
    cfg = load_tenant_logo_config(root)
    if not uses_brand_logo_paste(cfg):
        return errors

    stamp_path = article_dir / "cover" / "logo-composite-stamp.json"
    if not stamp_path.is_file():
        errors.append("cover/logo-composite-stamp.json missing — run brand logo composite")
        return errors
    try:
        stamp = json.loads(stamp_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ["logo-composite-stamp.json invalid JSON"]

    if str(stamp.get("status") or "").upper() != "PASS":
        errors.append("logo-composite-stamp.json status != PASS")
    if str(stamp.get("logo_sha256") or "") != str(cfg.get("logo_sha256") or CANONICAL_SHA256):
        errors.append("logo-composite-stamp.json sha256 mismatch vs canonical logo")

    expected_phone = str(cfg.get("phone_display") or DEFAULT_PHONE_DISPLAY)
    if str(stamp.get("cover_phone_display") or "") != expected_phone:
        errors.append(f"logo-composite stamp phone must be {expected_phone!r}")
    if stamp.get("cover_phone_post_composite") is True:
        errors.append("logo-composite stamp must not set cover_phone_post_composite=true (phone in scene only)")
    if stamp.get("cover_phone_in_scene_generation") is False:
        errors.append("logo-composite stamp must set cover_phone_in_scene_generation=true")

    manifest_path = article_dir / "cover" / "quad-manifest.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            phone = str(manifest.get("cover_phone_cta") or "").strip()
            if phone != expected_phone:
                errors.append(
                    f"quad-manifest cover_phone_cta must be {expected_phone!r}, got {phone!r}"
                )
            for forbidden in FORBIDDEN_PHONE_DIGITS:
                if forbidden in normalize_phone_digits(phone):
                    errors.append("quad-manifest cover_phone_cta uses forbidden realtor number")
        except json.JSONDecodeError:
            errors.append("quad-manifest.json invalid JSON")

    for name in IMAGE_NAMES:
        if not (article_dir / "cover" / name).is_file():
            errors.append(f"missing composed image cover/{name}")

    lo = float(cfg.get("min_width_fraction") or LOGO_WIDTH_FRACTION_MIN)
    hi = float(cfg.get("max_width_fraction_cap") or LOGO_WIDTH_FRACTION_MAX)
    expected_corner = str(cfg.get("logo_corner") or FIXED_LOGO_CORNER).casefold()
    stamp_corner = str(stamp.get("logo_corner_fixed") or "").casefold()
    if stamp_corner != expected_corner:
        errors.append(f"logo corner must be fixed {expected_corner!r}, stamp has {stamp_corner!r}")

    inline_files = list(stamp.get("inline_logo_files") or [])
    inline_lo, inline_hi = _inline_logo_bounds(cfg)
    if not (inline_lo <= len(inline_files) <= inline_hi):
        errors.append(
            f"inline logo count {len(inline_files)} outside factory {inline_lo}–{inline_hi}"
        )

    cover_placement = stamp.get("cover_logo_placement") or {}
    if str(cover_placement.get("logo_corner") or "").casefold() != expected_corner:
        errors.append("cover logo must be top-right fixed corner")
    if not cover_placement.get("logo_pasted", True):
        errors.append("cover must have exactly one factory logo paste")

    panel_placements = stamp.get("panel_logo_placements") or {}
    panel_skipped = stamp.get("panel_logo_skipped") or {}
    expected_skipped = {
        f"inline-{i:02d}.png"
        for i in range(1, 8)
        if f"inline-{i:02d}.png" not in inline_files
    }
    if set(panel_skipped.keys()) != expected_skipped:
        errors.append(
            "panel_logo_skipped must list all inline panels without logo paste "
            f"(expected {sorted(expected_skipped)}, got {sorted(panel_skipped.keys())})"
        )
    for name, placement in panel_placements.items():
        if str(placement.get("logo_corner") or "").casefold() != expected_corner:
            errors.append(f"{name} logo must be top-right fixed corner")
        frac = placement.get("logo_width_fraction")
        if frac is None:
            errors.append(f"logo-composite stamp missing logo_width_fraction on {name}")
            continue
        try:
            frac_f = float(frac)
        except (TypeError, ValueError):
            errors.append(f"logo-composite stamp logo_width_fraction invalid on {name}")
            continue
        if frac_f < lo or frac_f > hi:
            errors.append(
                f"{name} logo width fraction {frac_f:.3f} outside factory lock {lo:.2f}–{hi:.2f}"
            )

    cover_frac = cover_placement.get("logo_width_fraction")
    try:
        cover_frac_f = float(cover_frac)
        if cover_frac_f < lo or cover_frac_f > hi:
            errors.append(
                f"cover logo width fraction {cover_frac_f:.3f} outside factory lock {lo:.2f}–{hi:.2f}"
            )
    except (TypeError, ValueError):
        errors.append("cover logo_width_fraction invalid")

    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--force", action="store_true", help="Composite even if cover_mode unset")
    ap.add_argument("--cover-only", action="store_true", help="Composite cover.png only")
    ap.add_argument(
        "--phone-only",
        action="store_true",
        help="Post-composite phone on cover only (reference_in_generation mode)",
    )
    ap.add_argument(
        "--emergency",
        action="store_true",
        help="Emergency alpha-paste pipeline even when logo_mode=reference_in_generation",
    )
    ap.add_argument(
        "--after-pad-clear",
        action="store_true",
        help="После pad-clear live regen: не блокировать на terracotta false-positive",
    )
    args = ap.parse_args()
    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    try:
        stamp = composite_article_images(
            article_dir,
            root,
            force=bool(args.force),
            cover_only=bool(args.cover_only),
            phone_only=bool(args.phone_only),
            emergency=bool(args.emergency),
            after_pad_clear=bool(args.after_pad_clear),
        )
    except (FileNotFoundError, ValueError) as exc:
        print(f"BLOCKER: {exc}", file=sys.stderr)
        return 1
    if stamp.get("status") == "SKIP":
        print(json.dumps(stamp, ensure_ascii=False))
        return 0
    print(json.dumps(stamp, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
