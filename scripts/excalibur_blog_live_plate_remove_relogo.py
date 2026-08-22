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
FEATHER_PX = 32
MAX_CLEAR_PASSES = 5
SENSITIVE_MIN_PAD_RATIO = 0.06
SENSITIVE_MIN_AREA = 800

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


def _find_plate_bbox_local(pad_rgb, *, min_area: int = 400) -> tuple[int, int, int, int] | None:
    """Найти bbox подложки (white/gray/cream) внутри pad для точечного снятия."""
    gray = pad_rgb.mean(axis=2)
    best: dict | None = None
    for luma_min, std_max in [
        (WHITE_PLATE_LUMA_MIN - 8, WHITE_PLATE_STD_MAX + 6),
        (200.0, 26.0),
        (GRAY_PLATE_LUMA_MIN, GRAY_PLATE_STD_MAX + 6),
        (115.0, 32.0),
        (100.0, 36.0),
    ]:
        rect = _largest_low_variance_rect(gray, luma_min=luma_min, std_max=std_max)
        if not rect.get("found"):
            continue
        area = int(rect.get("area") or 0)
        if area < min_area:
            continue
        if best is None or area > int(best.get("area") or 0):
            best = rect
    if not best:
        return None
    bx0, by0, bx1, by1 = best["bbox"]
    return max(0, bx0 - 6), max(0, by0 - 6), min(pad_rgb.shape[1], bx1 + 6), min(pad_rgb.shape[0], by1 + 6)


def _uniform_top_right_plate(pad_rgb) -> bool:
    """Пустая серая/белая карточка в углу pad без логотипа."""
    gray = pad_rgb.mean(axis=2)
    ph, pw = gray.shape
    if ph < 12 or pw < 12:
        return False
    tr = gray[0 : max(8, int(ph * 0.62)), max(0, int(pw * 0.28)) :]
    if tr.size < 64:
        return False
    return float(tr.std()) < 24.0 and 112.0 < float(tr.mean()) < 248.0


def detect_plate_sensitive(rgb_arr) -> dict:
    """Чувствительнее production gate — ловит пустые серые plates на inline 02/04/05/06."""
    import numpy as np

    h, w = rgb_arr.shape[:2]
    px0, py0, pad_w, pad_h = _pad_box(
        w, h, pad_w_frac=CLEAR_PAD_W_FRAC, pad_h_frac=CLEAR_PAD_H_FRAC
    )
    pad = rgb_arr[py0 : py0 + pad_h, px0 : px0 + pad_w]
    if pad.size == 0:
        return {"detected": False, "reason": "empty_pad"}

    pad_area = max(pad_w * pad_h, 1)
    min_area = max(SENSITIVE_MIN_AREA, int(pad_area * SENSITIVE_MIN_PAD_RATIO))
    gray = pad.mean(axis=2)

    for luma_min, std_max, kind in [
        (WHITE_PLATE_LUMA_MIN - 10, WHITE_PLATE_STD_MAX + 8, "white"),
        (200.0, 28.0, "light"),
        (GRAY_PLATE_LUMA_MIN, GRAY_PLATE_STD_MAX + 8, "gray"),
        (110.0, 34.0, "cream"),
    ]:
        rect = _largest_low_variance_rect(gray, luma_min=luma_min, std_max=std_max)
        area = int(rect.get("area") or 0)
        if rect.get("found") and area >= min_area:
            return {
                "detected": True,
                "plate_kind": kind,
                "plate_area": area,
                "min_area": min_area,
                "plate_bbox_local": rect.get("bbox"),
                "plate_mean_luma": round(float(rect.get("mean") or 0.0), 2),
            }

    if _uniform_top_right_plate(pad):
        tr = gray[0 : max(8, int(pad_h * 0.62)), max(0, int(pad_w * 0.28)) :]
        return {
            "detected": True,
            "plate_kind": "uniform_corner",
            "plate_area": int(tr.size),
            "min_area": min_area,
            "corner_mean": round(float(tr.mean()), 2),
            "corner_std": round(float(tr.std()), 2),
        }
    return {"detected": False, "min_area": min_area}


def _pad_donor_strips(rgb_arr, px0: int, py0: int, pad_w: int, pad_h: int) -> list:
    """Образцы фона слева/снизу от pad — без watermark-зоны."""
    h, w = rgb_arr.shape[:2]
    donors: list = []
    left_w = min(160, px0 - 8)
    if left_w > 24:
        donors.append(rgb_arr[py0 : py0 + pad_h, px0 - left_w : px0 - 4])
    below_h = min(120, h - (py0 + pad_h) - 4)
    if below_h > 24:
        donors.append(rgb_arr[py0 + pad_h + 4 : py0 + pad_h + 4 + below_h, px0 : px0 + pad_w])
    mid_y0 = py0 + pad_h // 5
    mid_y1 = py0 + pad_h - pad_h // 5
    far_left = max(0, px0 - min(280, px0))
    if px0 - far_left > 48:
        donors.append(rgb_arr[mid_y0:mid_y1, far_left : max(far_left + 8, px0 - 24)])
    return donors


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


def _inpaint_plate_bbox(rgb_arr, px0: int, py0: int, lx0: int, ly0: int, lx1: int, ly1: int, *, passes: int = 3) -> None:
    """Inpaint только bbox подложки — не трогаем остальной pad/scene."""
    import cv2
    import numpy as np

    h, w = rgb_arr.shape[:2]
    gx0 = max(0, px0 + lx0 - 4)
    gy0 = max(0, py0 + ly0 - 4)
    gx1 = min(w, px0 + lx1 + 4)
    gy1 = min(h, py0 + ly1 + 4)
    if gx1 - gx0 < 6 or gy1 - gy0 < 6:
        return
    for _ in range(passes):
        mask = np.zeros((h, w), dtype=np.uint8)
        mask[gy0:gy1, gx0:gx1] = 255
        bgr = cv2.cvtColor(rgb_arr, cv2.COLOR_RGB2BGR)
        inpainted = cv2.inpaint(bgr, mask, inpaintRadius=13, flags=cv2.INPAINT_NS)
        rgb_arr[:] = cv2.cvtColor(inpainted, cv2.COLOR_BGR2RGB)


def _inpaint_mask_region(rgb_arr, x0: int, y0: int, x1: int, y1: int) -> None:
    """Точечный inpaint для остатков после bbox-проходов."""
    import cv2
    import numpy as np

    h, w = rgb_arr.shape[:2]
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(w, x1), min(h, y1)
    if x1 - x0 < 4 or y1 - y0 < 4:
        return
    mask = np.zeros((h, w), dtype=np.uint8)
    mask[y0:y1, x0:x1] = 255
    bgr = cv2.cvtColor(rgb_arr, cv2.COLOR_RGB2BGR)
    inpainted = cv2.inpaint(bgr, mask, inpaintRadius=9, flags=cv2.INPAINT_NS)
    rgb_arr[:] = cv2.cvtColor(inpainted, cv2.COLOR_BGR2RGB)


def clear_logo_pad(rgb_arr, *, initial_full_wipe: bool = False) -> int:
    """Снять white/gray plate + старый lockup: bbox inpaint, без белой заливки всего pad."""
    passes = 0
    h, w = rgb_arr.shape[:2]
    px0, py0, pad_w, pad_h = _pad_box(
        w, h, pad_w_frac=CLEAR_PAD_W_FRAC, pad_h_frac=CLEAR_PAD_H_FRAC
    )
    pad_area = max(pad_w * pad_h, 1)

    if initial_full_wipe:
        _inpaint_mask_region(rgb_arr, px0, py0, px0 + pad_w, py0 + pad_h)
        passes += 1

    for _ in range(MAX_CLEAR_PASSES):
        pad = rgb_arr[py0 : py0 + pad_h, px0 : px0 + pad_w]
        plate_local = _find_plate_bbox_local(pad, min_area=900)
        gate_before = detect_white_plate_in_pad_from_arr(rgb_arr)
        if not gate_before.get("detected") and not plate_local:
            break

        if plate_local:
            lx0, ly0, lx1, ly1 = plate_local
            plate_area = max(1, (lx1 - lx0) * (ly1 - ly0))
            # Почти весь pad — plate: inpaint весь pad, иначе только bbox.
            if plate_area >= int(pad_area * 0.72):
                _inpaint_mask_region(rgb_arr, px0, py0, px0 + pad_w, py0 + pad_h)
            else:
                _inpaint_plate_bbox(rgb_arr, px0, py0, lx0, ly0, lx1, ly1, passes=2)
        elif gate_before.get("detected"):
            bbox = gate_before.get("plate_bbox_local")
            if bbox:
                lx0, ly0, lx1, ly1 = bbox
                _inpaint_plate_bbox(rgb_arr, px0, py0, lx0, ly0, lx1, ly1, passes=2)
            else:
                _inpaint_mask_region(rgb_arr, px0, py0, px0 + pad_w, py0 + pad_h)
        else:
            break
        passes += 1

    return passes


def detect_white_plate_in_pad_from_arr(rgb_arr) -> dict:
    """Обёртка gate без temp-файла."""
    from PIL import Image
    import uuid

    tmp = Path(f"/tmp/pad-gate-{uuid.uuid4().hex}.png")
    Image.fromarray(rgb_arr).save(tmp)
    try:
        return detect_white_plate_in_pad(tmp)
    finally:
        tmp.unlink(missing_ok=True)


def fix_image(
    data: bytes,
    *,
    add_phone: bool,
    paste_logo: bool,
    logo_fraction: float = 0.10,
    strict: bool = False,
) -> tuple[bytes, dict]:
    from PIL import Image

    import uuid

    img = Image.open(BytesIO(data)).convert("RGBA")
    rgb = np_array_rgb_from_pil(img)
    clear_passes = clear_logo_pad(rgb, initial_full_wipe=bool(paste_logo or add_phone))
    tmp = Path(f"/tmp/live-fix-panel-{uuid.uuid4().hex}.png")
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

    rgb_after = np_array_rgb_from_pil(out_img)
    verify: dict = {
        "clear_passes": clear_passes,
        "pad_plate": detect_white_plate_in_pad(tmp),
        "pad_plate_sensitive": detect_plate_sensitive(rgb_after),
    }
    if paste_logo and placement.get("logo_xy"):
        xy = placement["logo_xy"]
        verify["under_logo"] = detect_white_plate_under_logo(
            tmp,
            LOGO,
            logo_xy=(xy[0], xy[1]),
            logo_width_px=int(placement.get("logo_width_px") or 0),
            logo_height_px=int(placement.get("logo_height_px") or 0),
        )
    if strict:
        if verify["pad_plate"].get("detected") or verify["pad_plate_sensitive"].get("detected"):
            raise RuntimeError(f"plate remains after fix: {verify}")
        under = verify.get("under_logo") or {}
        if under.get("detected"):
            raise RuntimeError(f"under-logo plate after fix: {under}")
    try:
        tmp.unlink(missing_ok=True)
    except OSError:
        pass
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


def process_article(spec: dict, *, strict: bool = False) -> list[str]:
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
        fixed, verify = fix_image(raw, add_phone=phone, paste_logo=paste, strict=strict)
        for key in ("pad_plate", "pad_plate_sensitive"):
            if verify.get(key, {}).get("detected"):
                print(f"WARN {key}: {remote} {verify[key]}", flush=True)
        under = verify.get("under_logo") or {}
        if under.get("detected"):
            print(f"WARN under-logo plate: {remote} {under}", flush=True)
        (out_dir / local).write_bytes(fixed)

    urls = upload_sftp(spec, out_dir)
    cb = int.from_bytes(os.urandom(4), "big")
    return [f"{u}?cb={cb}" for u in urls]


def main() -> int:
    import argparse
    from concurrent.futures import ThreadPoolExecutor, as_completed

    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", help="process single slug")
    ap.add_argument("--workers", type=int, default=3, help="parallel articles (default 3)")
    ap.add_argument("--strict", action="store_true", help="abort on any remaining plate")
    ap.add_argument(
        "--optional",
        action="store_true",
        help="also fix sem-utra + subarenda white corner plates",
    )
    args = ap.parse_args()

    if not PUBLIC:
        print("PUBLIC_SITE_URL missing", file=sys.stderr)
        return 1
    if not LOGO.is_file():
        print("logo missing", file=sys.stderr)
        return 1
    report: dict[str, list[str]] = {}
    optional_articles = [
        {
            "slug": "priehal-v-sem-utra-kvartiru-dali-tolko-v-dva-chto-delat-do-zaseleniya",
            "cover_remote": "priehal-v-sem-utra-kvartiru-dali-tolko-v-dva-chto-delat-do-zaseleniya-cover.png",
            "inline_remote": "priehal-v-sem-utra-kvartiru-dali-tolko-v-dva-chto-delat-do-zaseleniya-inline-{n:02d}.png",
        },
        {
            "slug": "zabroniroval-posutochno-vyyasnilos-kvartira-v-subarende",
            "cover_remote": "zabroniroval-posutochno-vyyasnilos-kvartira-v-subarende-cover-2.png",
            "inline_remote": "zabroniroval-posutochno-vyyasnilos-kvartira-v-subarende-inline-{n:02d}.png",
        },
    ]
    pool_articles = list(ARTICLES)
    if args.optional:
        pool_articles.extend(optional_articles)
    specs = [s for s in pool_articles if not args.slug or s["slug"] == args.slug]
    workers = max(1, min(int(args.workers), len(specs)))

    def _run(spec: dict) -> tuple[str, list[str]]:
        print(f"\n=== FIX {spec['slug']} ===", flush=True)
        return spec["slug"], process_article(spec, strict=bool(args.strict))

    if workers == 1 or len(specs) == 1:
        for spec in specs:
            slug, urls = _run(spec)
            report[slug] = urls
    else:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = [pool.submit(_run, spec) for spec in specs]
            for fut in as_completed(futures):
                slug, urls = fut.result()
                report[slug] = urls
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
