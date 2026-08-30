"""Tests for AI-drawn logo detection and official PNG paste gates."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
LOGO = ROOT / "memory/cover/assets/brand/logo-dobry-dom.png"


class DrawnLogoGateTest(unittest.TestCase):
    def test_official_logo_not_detected_as_drawn_on_white_pad(self) -> None:
        from PIL import Image

        from excalibur_blog_drawn_logo_gate import detect_drawn_lockup_in_image

        with tempfile.TemporaryDirectory() as tmp:
            canvas = Path(tmp) / "white.png"
            Image.new("RGB", (1200, 675), (255, 255, 255)).save(canvas)
            result = detect_drawn_lockup_in_image(canvas)
            self.assertFalse(result["detected"], result)

    def test_composite_on_dark_scene_keeps_scene_pixels_no_white_plate(self) -> None:
        from PIL import Image
        import numpy as np

        from excalibur_blog_brand_logo_composite import composite_logo_onto_image
        from excalibur_blog_drawn_logo_gate import detect_white_plate_under_logo

        self.assertTrue(LOGO.is_file(), "official logo asset missing")
        with tempfile.TemporaryDirectory() as tmp:
            canvas = Path(tmp) / "dark.png"
            scene_color = (30, 60, 90)
            Image.new("RGB", (1200, 675), scene_color).save(canvas)
            placement = composite_logo_onto_image(
                canvas,
                LOGO,
                max_width_fraction=0.10,
                paste_logo=True,
                add_phone=False,
            )
            plate = detect_white_plate_under_logo(
                canvas,
                LOGO,
                logo_xy=(placement["logo_xy"][0], placement["logo_xy"][1]),
                logo_width_px=placement["logo_width_px"],
                logo_height_px=placement["logo_height_px"],
            )
            self.assertFalse(plate.get("detected"), plate)
            img = np.array(Image.open(canvas).convert("RGB"))
            x, y = placement["logo_xy"]
            ring = img[y - 8 : y + 8, x - 8 : x + 12]
            self.assertLess(float(ring.mean()), 200.0)

    def test_white_card_under_logo_region_fails_gate(self) -> None:
        from PIL import Image, ImageDraw

        from excalibur_blog_drawn_logo_gate import (
            detect_white_plate_in_pad,
            detect_white_plate_under_logo,
        )

        with tempfile.TemporaryDirectory() as tmp:
            canvas = Path(tmp) / "white-card.png"
            img = Image.new("RGB", (1200, 675), (180, 190, 200))
            draw = ImageDraw.Draw(img)
            x0 = 1200 - 220
            draw.rectangle((x0, 12, 1190, 190), fill=(252, 252, 252))
            img.save(canvas)
            pad = detect_white_plate_in_pad(canvas)
            self.assertTrue(pad.get("detected"), pad)

        with tempfile.TemporaryDirectory() as tmp:
            canvas = Path(tmp) / "plate-under-logo.png"
            img = Image.new("RGB", (1200, 675), (40, 80, 120))
            draw = ImageDraw.Draw(img)
            x0 = 1200 - 200
            draw.rectangle((x0, 10, 1190, 170), fill=(250, 250, 250))
            img.save(canvas)
            plate = detect_white_plate_under_logo(
                canvas,
                LOGO,
                logo_xy=(x0 + 10, 20),
                logo_width_px=120,
                logo_height_px=90,
            )
            self.assertTrue(plate.get("detected"), plate)

    def test_official_logo_pasted_region_matches_canonical(self) -> None:
        from PIL import Image

        from excalibur_blog_brand_logo_composite import composite_logo_onto_image
        from excalibur_blog_drawn_logo_gate import (
            detect_drawn_lockup_in_image,
            verify_official_logo_paste,
        )

        self.assertTrue(LOGO.is_file(), "official logo asset missing")
        with tempfile.TemporaryDirectory() as tmp:
            canvas = Path(tmp) / "cover.png"
            Image.new("RGBA", (1200, 675), (255, 255, 255, 255)).save(canvas)
            placement = composite_logo_onto_image(
                canvas,
                LOGO,
                max_width_fraction=0.10,
                paste_logo=True,
                add_phone=False,
            )
            xy = placement["logo_xy"]
            verify = verify_official_logo_paste(
                canvas,
                LOGO,
                logo_xy=(xy[0], xy[1]),
                logo_width_px=placement["logo_width_px"],
                logo_height_px=placement["logo_height_px"],
            )
            self.assertTrue(verify["ok"], verify)

    def test_simulated_drawn_lockup_detected_in_pad(self) -> None:
        from PIL import Image, ImageDraw

        from excalibur_blog_drawn_logo_gate import detect_drawn_lockup_in_image

        with tempfile.TemporaryDirectory() as tmp:
            canvas = Path(tmp) / "fake-lockup.png"
            img = Image.new("RGB", (1200, 675), (255, 255, 255))
            draw = ImageDraw.Draw(img)
            x0 = 1200 - 140
            draw.rectangle((x0, 10, 1190, 170), fill=(61, 139, 122))
            draw.rectangle((x0 + 8, 18, 1182, 162), outline=(120, 120, 120), width=2)
            draw.rectangle((x0 + 40, 30, x0 + 90, 80), fill=(180, 40, 40))
            draw.text((x0 + 12, 95), "Добрый дом", fill=(196, 92, 62))
            img.save(canvas)
            result = detect_drawn_lockup_in_image(canvas)
            self.assertTrue(result["detected"], result)

    def test_composite_creates_pre_composite_snapshot(self) -> None:
        from PIL import Image

        with tempfile.TemporaryDirectory() as tmp:
            tenant_root = Path(tmp) / "repo"
            article = tenant_root / "memory/blog/articles/test-logo"
            cover = article / "cover"
            cover.mkdir(parents=True)
            shutil.copytree(ROOT / "shared", tenant_root / "shared")
            shutil.copytree(ROOT / "memory/cover/assets", tenant_root / "memory/cover/assets")
            (tenant_root / "scripts").mkdir()
            for name in (
                "excalibur_blog_brand_logo_composite.py",
                "excalibur_blog_drawn_logo_gate.py",
            ):
                shutil.copy2(ROOT / "scripts" / name, tenant_root / "scripts" / name)
            manifest = {
                "logo_paste_inline_slots": ["inline_1", "inline_3", "inline_7"],
            }
            (cover / "quad-manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False), encoding="utf-8"
            )
            for name in (
                "cover.png",
                "inline-01.png",
                "inline-02.png",
                "inline-03.png",
                "inline-04.png",
                "inline-05.png",
                "inline-06.png",
                "inline-07.png",
            ):
                Image.new("RGBA", (1200, 675), (255, 255, 255, 255)).save(cover / name)
            env = {"EXCALIBUR_PROJECT_ROOT": str(tenant_root), **dict(__import__("os").environ)}
            proc = subprocess.run(
                [
                    sys.executable,
                    str(tenant_root / "scripts/excalibur_blog_brand_logo_composite.py"),
                    "--article-dir",
                    str(article),
                ],
                cwd=tenant_root,
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)
            pre = cover / "pre-composite/cover.png"
            self.assertTrue(pre.is_file(), "pre-composite snapshot missing")

    def test_composite_crops_logo_getbbox_not_full_square(self) -> None:
        from PIL import Image

        from excalibur_blog_brand_logo_composite import composite_logo_onto_image, prepare_logo_rgba

        with Image.open(LOGO) as raw:
            full_bbox = raw.size
        cropped = prepare_logo_rgba(LOGO, 120)
        self.assertLess(cropped.width, full_bbox[0])
        self.assertLess(cropped.height, full_bbox[1] * 0.5)

    def test_cover_qa_gate_requires_slim_drawn_logo_checks(self) -> None:
        gate_src = (ROOT / "scripts/excalibur_blog_cover_qa_gate.py").read_text(encoding="utf-8")
        for key in (
            "forbid_ai_drawn_logo_cover",
            "no_logo_plate_cover",
            "validate_article_logo_gates_slim",
        ):
            self.assertIn(key, gate_src)
        for removed in (
            "official_logo_pixels_only",
            "logo_no_text_overlap",
            "forbid_logo_white_plate",
        ):
            self.assertNotIn(removed, gate_src)

    def test_gray_card_in_logo_pad_fails_gate(self) -> None:
        from PIL import Image, ImageDraw

        from excalibur_blog_drawn_logo_gate import detect_white_plate_in_pad

        with tempfile.TemporaryDirectory() as tmp:
            canvas = Path(tmp) / "gray-card.png"
            img = Image.new("RGB", (1200, 675), (180, 190, 200))
            draw = ImageDraw.Draw(img)
            x0 = 1200 - 220
            draw.rectangle((x0, 12, 1190, 190), fill=(200, 205, 210))
            img.save(canvas)
            result = detect_white_plate_in_pad(canvas)
            self.assertTrue(result.get("detected"), result)
            self.assertEqual(result.get("plate_kind"), "gray")

    def test_prepare_logo_rgba_crops_getbbox_not_full_canvas(self) -> None:
        from excalibur_blog_brand_logo_composite import (
            LOGO_CROP_BBOX_CANON,
            LOGO_SOURCE_CANVAS_PX,
            prepare_logo_rgba,
        )
        from PIL import Image

        logo_path = ROOT / "memory/cover/assets/brand/logo-dobry-dom.png"
        self.assertTrue(logo_path.is_file(), logo_path)
        with Image.open(logo_path) as raw:
            self.assertEqual(raw.size, (LOGO_SOURCE_CANVAS_PX, LOGO_SOURCE_CANVAS_PX))
            self.assertEqual(raw.getbbox(), LOGO_CROP_BBOX_CANON)
            corner = raw.convert("RGBA").getpixel((0, 0))
            self.assertEqual(corner[3], 0, "corner must be transparent (alpha=0)")

        cropped = prepare_logo_rgba(logo_path, 120)
        self.assertLess(cropped.width, LOGO_SOURCE_CANVAS_PX - 4)
        self.assertLess(cropped.height, LOGO_SOURCE_CANVAS_PX - 4)

        src = (ROOT / "scripts/excalibur_blog_cover_quad_prompt.py").read_text(encoding="utf-8")
        self.assertIn("LOGO_DRAW_HARD_BAN", src)
        self.assertIn("LOGO_WHITE_PLATE_BAN", src)
        self.assertIn("curtains+red flower", src)
        self.assertIn("dashed logo frame", src)
        self.assertIn("white/gray", src)
        self.assertIn("cropped-img_7143.png", src)

    def test_phone_pill_post_composite_detected(self) -> None:
        from PIL import Image, ImageDraw

        from excalibur_blog_drawn_logo_gate import (
            detect_phone_pill_post_composite,
            detect_phone_pill_overlaps_cat_zone,
        )

        with tempfile.TemporaryDirectory() as tmp:
            canvas = Path(tmp) / "pill.png"
            img = Image.new("RGB", (1200, 675), (200, 210, 220))
            draw = ImageDraw.Draw(img)
            draw.rounded_rectangle((40, 610, 420, 660), radius=8, fill=(252, 252, 252), outline=(20, 24, 33), width=2)
            draw.text((55, 620), "+7 (993) 574-83-22", fill=(20, 24, 33))
            img.save(canvas)
            pill = detect_phone_pill_post_composite(canvas)
            self.assertTrue(pill.get("detected"), pill)

        with tempfile.TemporaryDirectory() as tmp:
            canvas = Path(tmp) / "pill-on-cat.png"
            img = Image.new("RGB", (1200, 675), (200, 210, 220))
            draw = ImageDraw.Draw(img)
            draw.rectangle((20, 520, 200, 660), fill=(120, 80, 60))
            draw.rounded_rectangle((30, 600, 360, 655), radius=8, fill=(250, 250, 250))
            img.save(canvas)
            overlap = detect_phone_pill_overlaps_cat_zone(canvas)
            self.assertTrue(overlap.get("overlap"), overlap)

    def test_phone_only_composite_flag_blocked(self) -> None:
        from excalibur_blog_brand_logo_composite import composite_article_images

        with tempfile.TemporaryDirectory() as tmp:
            tenant_root = Path(tmp) / "repo"
            article = tenant_root / "memory/blog/articles/test-phone"
            cover = article / "cover"
            cover.mkdir(parents=True)
            shutil.copytree(ROOT / "shared", tenant_root / "shared")
            shutil.copytree(ROOT / "memory/cover/assets", tenant_root / "memory/cover/assets")
            (tenant_root / "scripts").mkdir()
            shutil.copy2(
                ROOT / "scripts/excalibur_blog_brand_logo_composite.py",
                tenant_root / "scripts/excalibur_blog_brand_logo_composite.py",
            )
            from PIL import Image

            Image.new("RGBA", (1200, 675), (255, 255, 255, 255)).save(cover / "cover.png")
            with self.assertRaises(ValueError):
                composite_article_images(article, tenant_root, phone_only=True)

    def test_tenant_image_generation_forbids_drawn_logo(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        img = tenant.get("image_generation") or {}
        forbids = " ".join(img.get("forbid_in_generation") or []).lower()
        self.assertIn("добрый дом", forbids)
        self.assertIn("gray box", forbids)
        self.assertIn("white box", forbids)
        self.assertIn("phone pill", forbids)
        self.assertTrue(img.get("logo_never_as_generation_reference"))
        self.assertIn("logo-dobry-dom.png", img.get("logo_factory_paste_only", ""))

    def test_bright_window_pad_exempt_when_no_lockup_colors(self) -> None:
        from excalibur_blog_drawn_logo_gate import (
            detect_drawn_lockup_in_image,
            detect_white_plate_in_pad,
            is_bright_window_pad_false_positive,
        )

        cover = (
            ROOT
            / "memory/blog/articles/B03-kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki"
            / "cover/pre-composite/cover.png"
        )
        self.assertTrue(cover.is_file(), cover)
        lockup = detect_drawn_lockup_in_image(cover)
        plate = detect_white_plate_in_pad(cover)
        self.assertTrue(plate.get("detected"), plate)
        self.assertEqual(plate.get("plate_kind"), "white")
        self.assertFalse(lockup.get("detected"), lockup)
        self.assertTrue(
            is_bright_window_pad_false_positive(cover, lockup=lockup, plate=plate),
            plate,
        )

    def test_poster_split_flat_white_tr_pad_exempt(self) -> None:
        """WOW poster-split: flat white TR headline field is not an AI logo card (B04)."""
        from excalibur_blog_drawn_logo_gate import (
            detect_drawn_lockup_in_image,
            detect_white_plate_in_pad,
            is_bright_window_pad_false_positive,
        )

        cover = (
            ROOT
            / "memory/blog/articles/B04-poprosili-foto-pasporta-pri-zaselenii-posutochno-do-oplaty"
            / "cover/pre-composite/cover.png"
        )
        self.assertTrue(cover.is_file(), cover)
        lockup = detect_drawn_lockup_in_image(cover)
        plate = detect_white_plate_in_pad(cover)
        self.assertTrue(plate.get("detected"), plate)
        self.assertEqual(plate.get("plate_kind"), "white")
        self.assertFalse(lockup.get("detected"), lockup)
        self.assertLessEqual(float(plate.get("plate_std") or 99.0), 8.0, plate)
        self.assertLess(float(lockup.get("score") or 1.0), 0.30, lockup)
        self.assertTrue(
            is_bright_window_pad_false_positive(cover, lockup=lockup, plate=plate),
            plate,
        )


if __name__ == "__main__":
    unittest.main()
