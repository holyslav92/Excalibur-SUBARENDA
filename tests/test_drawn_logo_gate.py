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

    def test_cover_qa_gate_requires_drawn_logo_checks(self) -> None:
        gate_src = (ROOT / "scripts/excalibur_blog_cover_qa_gate.py").read_text(encoding="utf-8")
        for key in (
            "forbid_ai_drawn_logo_pre_composite",
            "official_logo_pixels_only",
            "logo_no_text_overlap",
            "validate_article_logo_gates",
        ):
            self.assertIn(key, gate_src)

    def test_quad_prompt_hard_bans_drawn_lockup(self) -> None:
        src = (ROOT / "scripts/excalibur_blog_cover_quad_prompt.py").read_text(encoding="utf-8")
        self.assertIn("LOGO_DRAW_HARD_BAN", src)
        self.assertIn("curtains+red flower", src)
        self.assertIn("dashed logo frame", src)

    def test_tenant_image_generation_forbids_drawn_logo(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        img = tenant.get("image_generation") or {}
        forbids = " ".join(img.get("forbid_in_generation") or []).lower()
        self.assertIn("добрый дом", forbids)
        self.assertIn("logo-dobry-dom.png", img.get("logo_factory_paste_only", ""))


if __name__ == "__main__":
    unittest.main()
