#!/usr/bin/env python3
"""Emergency live fix: remove gray/white logo plate + re-paste official alpha logo."""

from __future__ import annotations

import json
import os
import sys
from io import BytesIO
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_brand_logo_composite import (  # noqa: E402
    DEFAULT_PHONE_DISPLAY,
    composite_logo_onto_image,
)
from excalibur_blog_drawn_logo_gate import (  # noqa: E402
    GRAY_PLATE_LUMA_MIN,
    GRAY_PLATE_STD_MAX,
    PAD_HEIGHT_FRACTION,
    PAD_WIDTH_FRACTION,
    WHITE_PLATE_LUMA_MIN,
    WHITE_PLATE_STD_MAX,
    _largest_low_variance_rect,
    _pad_box,
    detect_white_plate_in_pad,
    detect_white_plate_under_logo,
)

# Чуть шире стандартного pad — снимаем подложку + старый lockup целиком.
CLEAR_PAD_W_FRAC = 0.18
CLEAR_PAD_H_FRAC = 0.34
FEATHER_PX = 28

PUBLIC = os.environ.get("PUBLIC_SITE_URL", "").rstrip("/")
LOGO = ROOT / "memory/cover/assets/brand/logo-dobry-dom.png"

ARTICLES = [
    {
        "slug": "dogovor-arendy-pravila-prozhivaniya-posutochno",
        "cover_remote": "dogovor-arendy-pravila-prozhivaniya-posutochno-cover-1.png",
        "inline_remote": "dogovor-arendy-pravila-prozhivaniya-posutochno-inline-{n:02d}-1.png",
    },
    {
        "slug": "otmena-bronirovaniya-posutochno-vozvrat-predoplaty",
        "cover_remote": "otmena-bronirovaniya-posutochno-vozvrat-predoplaty-cover.png",
        "inline_remote": "otmena-bronirovaniya-posutochno-vozvrat-predoplaty-inline-{n:02d}.png",
    },
    {
        "slug": "pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti",
        "cover_remote": "pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti-cover.png",
        "inline_remote": "pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti-inline-{n:02d}.png",
    },
]


def download(url: str) -> bytes:
    with urlopen(url, timeout=120) as resp:
        return resp.read()


def np_array_rgb_from_pil(img):
    import numpy as np

    return np.array(img.convert("RGB"))


def _find_plate_bbox_local(pad_rgb) -> tuple[int, int, int, int] | None:
    """Найти bbox подложки (white/gray/cream) внутри pad для точечного снятия."""
    import numpy as np

    gray = pad_rgb.mean(axis=2)
    best: dict | None = None
    for luma_min, std_max in [
        (WHITE_PLATE_LUMA_MIN - 5, WHITE_PLATE_STD_MAX + 4),
        (200.0, 24.0),
        (GRAY_PLATE_LUMA_MIN, GRAY_PLATE_STD_MAX + 4),
        (120.0, 30.0),
    ]:
        rect = _largest_low_variance_rect(gray, luma_min=luma_min, std_max=std_max)
        if not rect.get("found"):
            continue
        area = int(rect.get("area") or 0)
        if area < 400:
            continue
        if best is None or area > int(best.get("area") or 0):
            best = rect
    if not best:
        return None
    bx0, by0, bx1, by1 = best["bbox"]
    # Небольшой margin — убрать антиалиас подложки.
    return max(0, bx0 - 3), max(0, by0 - 3), bx1 + 3, by1 + 3


def _texture_fill(shape: tuple[int, int], donors: list) -> "np.ndarray":
    """Сшить текстуру из доноров + лёгкий шум."""
    from PIL import Image
    import numpy as np

    h, w = shape
    patches: list[np.ndarray] = []
    for donor in donors:
        if donor is None or donor.size < 100:
            continue
        patches.append(
            np.array(
                Image.fromarray(donor).resize((w, h), Image.Resampling.LANCZOS),
                dtype=np.float32,
            )
        )
    if not patches:
        return np.zeros((h, w, 3), dtype=np.float32)
    filled = np.mean(np.stack(patches, axis=0), axis=0)
    rng = np.random.default_rng(11)
    filled += rng.normal(0, 8.0, filled.shape)
    return filled


def _feather_blend_region(
    rgb_arr,
    x0: int,
    y0: int,
    x1: int,
    y1: int,
    fill_patch,
    *,
    feather: int = FEATHER_PX,
) -> None:
    """Заменить прямоугольник с мягкими краями — без «карточки»."""
    import numpy as np

    region_h, region_w = y1 - y0, x1 - x0
    if region_h < 2 or region_w < 2:
        return
    orig = rgb_arr[y0:y1, x0:x1].astype(np.float32)
    region_h, region_w = orig.shape[0], orig.shape[1]
    mask = np.ones((region_h, region_w), dtype=np.float32)
    f = min(feather, region_h // 3, region_w // 3, 40)
    for d in range(f):
        t = (d + 1) / f
        mask[d, :] = np.minimum(mask[d, :], t)
        mask[region_h - 1 - d, :] = np.minimum(mask[region_h - 1 - d, :], t)
        mask[:, d] = np.minimum(mask[:, d], t)
        mask[:, region_w - 1 - d] = np.minimum(mask[:, region_w - 1 - d], t)
    mask = mask[..., None]
    new = fill_patch.astype(np.float32)
    if new.shape[:2] != orig.shape[:2]:
        from PIL import Image

        new = np.array(
            Image.fromarray(np.clip(new, 0, 255).astype(np.uint8)).resize(
                (region_w, region_h), Image.Resampling.LANCZOS
            ),
            dtype=np.float32,
        )
    blended = new * mask + orig * (1.0 - mask)
    rgb_arr[y0:y1, x0:x1] = np.clip(blended, 0, 255).astype(np.uint8)


def clear_logo_pad(rgb_arr) -> None:
    """Снять plate + старый lockup: inpaint только pad, без donor-пятна."""
    import cv2
    import numpy as np

    h, w = rgb_arr.shape[:2]
    px0, py0, pad_w, pad_h = _pad_box(
        w, h, pad_w_frac=CLEAR_PAD_W_FRAC, pad_h_frac=CLEAR_PAD_H_FRAC
    )

    pad = rgb_arr[py0 : py0 + pad_h, px0 : px0 + pad_w]
    gray_pad = pad.mean(axis=2)
    plate_local = _find_plate_bbox_local(pad)

    mask = np.zeros((h, w), dtype=np.uint8)
    if plate_local:
        lx0, ly0, lx1, ly1 = plate_local
        mask[py0 + ly0 : py0 + ly1, px0 + lx0 : px0 + lx1] = 255
    else:
        mask[py0 : py0 + pad_h, px0 : px0 + pad_w] = 255

    # Добавить светлые пиксели подложки в маску.
    light = gray_pad > 200.0
    pad_mask = np.zeros((pad_h, pad_w), dtype=np.uint8)
    pad_mask[light] = 255
    mask[py0 : py0 + pad_h, px0 : px0 + pad_w] = np.maximum(
        mask[py0 : py0 + pad_h, px0 : px0 + pad_w], pad_mask
    )

    bgr = cv2.cvtColor(rgb_arr, cv2.COLOR_RGB2BGR)
    inpainted = cv2.inpaint(bgr, mask, inpaintRadius=9, flags=cv2.INPAINT_TELEA)
    rgb_arr[:] = cv2.cvtColor(inpainted, cv2.COLOR_BGR2RGB)


def fix_image(data: bytes, *, add_phone: bool, paste_logo: bool, logo_fraction: float = 0.10) -> tuple[bytes, dict]:
    from PIL import Image

    img = Image.open(BytesIO(data)).convert("RGBA")
    rgb = np_array_rgb_from_pil(img)
    clear_logo_pad(rgb)
    tmp = Path("/tmp/live-fix-panel.png")
    Image.fromarray(rgb).convert("RGBA").save(tmp)

    placement: dict = {}
    if paste_logo:
        placement = composite_logo_onto_image(
            tmp,
            LOGO,
            max_width_fraction=logo_fraction,
            paste_logo=True,
            add_phone=add_phone,
            phone_display=DEFAULT_PHONE_DISPLAY,
            pre_snapshot_dir=None,
            block_drawn_lockup=False,
        )
    elif add_phone:
        placement = composite_logo_onto_image(
            tmp,
            LOGO,
            paste_logo=False,
            add_phone=True,
            phone_display=DEFAULT_PHONE_DISPLAY,
            pre_snapshot_dir=None,
            block_drawn_lockup=False,
        )

    out_img = Image.open(tmp).convert("RGBA")
    out = BytesIO()
    out_img.save(out, format="PNG")

    verify: dict = {"pad_plate": detect_white_plate_in_pad(tmp)}
    if paste_logo and placement.get("logo_xy"):
        xy = placement["logo_xy"]
        verify["under_logo"] = detect_white_plate_under_logo(
            tmp,
            LOGO,
            logo_xy=(xy[0], xy[1]),
            logo_width_px=int(placement.get("logo_width_px") or 0),
            logo_height_px=int(placement.get("logo_height_px") or 0),
        )
    return out.getvalue(), verify


def upload_sftp(spec: dict, cover_dir: Path) -> list[str]:
    import paramiko
    from excalibur_blog_wp_publish import load_env, project_root, sftp_remote_path, sftp_root_candidates, _ssh_creds, is_missing_remote_path_error

    env = load_env(project_root())
    host, port, user, password = _ssh_creds(env)
    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    remote_dir = "wp-content/uploads/2026/08"
    urls: list[str] = []
    mapping = [("cover.png", spec["cover_remote"])]
    for n in range(1, 8):
        mapping.append((f"inline-{n:02d}.png", spec["inline_remote"].format(n=n)))

    try:
        for local_name, remote_name in mapping:
            data = (cover_dir / local_name).read_bytes()
            remote_path = f"{remote_dir}/{remote_name}"
            uploaded = False
            for root_candidate in sftp_root_candidates(env):
                full = sftp_remote_path(env, remote_path, root_candidate)
                try:
                    with sftp.open(full, "wb") as handle:
                        handle.write(data)
                    print(f"SFTP upload OK: {full} ({len(data)} bytes)")
                    uploaded = True
                    break
                except OSError as exc:
                    if is_missing_remote_path_error(exc):
                        continue
                    raise
            if not uploaded:
                raise RuntimeError(f"SFTP upload failed for {remote_path}")
            if PUBLIC:
                urls.append(f"{PUBLIC}/{remote_dir}/{remote_name}")
    finally:
        sftp.close()
        transport.close()
    return urls


def process_article(spec: dict) -> list[str]:
    base = f"{PUBLIC}/wp-content/uploads/2026/08"
    out_dir = ROOT / "memory/blog/articles" / f"LIVE-fix-{spec['slug']}" / "cover"
    out_dir.mkdir(parents=True, exist_ok=True)

    mapping = [("cover.png", spec["cover_remote"], True, True)]
    for n in range(1, 8):
        paste = n in (1, 3, 7)
        mapping.append((f"inline-{n:02d}.png", spec["inline_remote"].format(n=n), False, paste))

    for local, remote, phone, paste in mapping:
        src = f"{base}/{remote}"
        print(f"fix {remote} ...", flush=True)
        raw = download(src)
        fixed, verify = fix_image(raw, add_phone=phone, paste_logo=paste)
        if verify.get("pad_plate", {}).get("detected"):
            print(f"WARN pad plate: {remote} {verify['pad_plate']}", flush=True)
        under = verify.get("under_logo") or {}
        if under.get("detected"):
            print(f"WARN under-logo plate: {remote} {under}", flush=True)
        (out_dir / local).write_bytes(fixed)

    urls = upload_sftp(spec, out_dir)
    cb = int.from_bytes(os.urandom(4), "big")
    return [f"{u}?cb={cb}" for u in urls]


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", help="process single slug")
    args = ap.parse_args()

    if not PUBLIC:
        print("PUBLIC_SITE_URL missing", file=sys.stderr)
        return 1
    if not LOGO.is_file():
        print("logo missing", file=sys.stderr)
        return 1
    report: dict[str, list[str]] = {}
    specs = [s for s in ARTICLES if not args.slug or s["slug"] == args.slug]
    for spec in specs:
        print(f"\n=== FIX {spec['slug']} ===", flush=True)
        report[spec["slug"]] = process_article(spec)
    out = ROOT / "memory/blog/live-plate-fix-aug22-report.json"
    existing = {}
    if out.is_file():
        try:
            existing = json.loads(out.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = {}
    existing.update(report)
    out.write_text(json.dumps(existing, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
