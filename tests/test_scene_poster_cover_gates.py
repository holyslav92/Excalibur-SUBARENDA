"""Tests for scene_poster_v2 cover gates — collage FAIL, scene PASS."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class ScenePosterCoverGateTest(unittest.TestCase):
    def test_canon_scene_poster_v2_locked(self) -> None:
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        self.assertEqual(canon["canon_id"], "dobry_dom_scene_poster_v2")
        phone = canon["wow_cover_rules"]["no_element_overlap"]["cover_phone"]
        self.assertFalse(phone["post_composite_bottom_left"])
        self.assertTrue(phone["in_scene_only"])
        self.assertEqual(canon["cover_generation"]["mode"], "standalone_16_9")

    def test_tenant_cover_wow_rules_scene_poster_v2(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        wow = tenant.get("cover_wow_rules") or {}
        self.assertEqual(wow.get("canon_id"), "dobry_dom_scene_poster_v2")
        self.assertEqual(wow.get("cover_generation_mode"), "standalone_16_9")
        self.assertTrue(wow.get("forbid_cover_meme_collage"))
        self.assertTrue(wow.get("vip_disabled"))

    def test_collage_gate_fails_split_white_panel(self) -> None:
        from excalibur_blog_cover_collage_gate import (
            detect_split_white_collage,
            validate_cover_scene_poster_gates,
        )

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "collage.png"
            img = Image.new("RGB", (1200, 675), (255, 255, 255))
            draw = ImageDraw.Draw(img)
            for x in range(480, 1200):
                for y in range(675):
                    img.putpixel((x, y), (80 + (x % 90), 70 + (y % 80), 60 + ((x + y) % 70)))
            draw.rectangle((0, 0, 450, 675), fill=(252, 252, 252))
            img.save(path)
            split = detect_split_white_collage(path)
            self.assertTrue(split.get("detected"), split)
            errors = validate_cover_scene_poster_gates(path)
            self.assertTrue(errors)

    def test_collage_gate_passes_full_bleed_scene(self) -> None:
        from excalibur_blog_cover_collage_gate import validate_cover_scene_poster_gates

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scene.png"
            img = Image.new("RGB", (1200, 675), (185, 175, 160))
            draw = ImageDraw.Draw(img)
            draw.rectangle((60, 90, 540, 620), fill=(95, 82, 72))
            draw.rectangle((620, 140, 860, 640), fill=(205, 198, 188))
            for x in range(700, 1100, 12):
                for y in range(180, 600, 12):
                    img.putpixel((x, y), (160 + (x % 35), 140 + (y % 28), 120 + ((x + y) % 22)))
            for x in range(980, 1180, 6):
                for y in range(20, 200, 6):
                    img.putpixel((x, y), (228 + (x % 5), 222 + (y % 4), 215 + ((x + y) % 3)))
            draw.text((720, 520), "+7 993 574-83-22", fill=(30, 30, 30))
            img.save(path)
            errors = validate_cover_scene_poster_gates(path)
            self.assertEqual(errors, [], errors)

    def test_quad_slots_standalone_cover_spec(self) -> None:
        from excalibur_blog_quad_slots import (
            STANDALONE_COVER_SPEC,
            all_canvas_specs,
            uses_scene_poster_v2,
        )

        self.assertTrue(uses_scene_poster_v2(ROOT))
        specs = all_canvas_specs(7)
        self.assertEqual(specs[0]["standalone_cover"], True)
        self.assertEqual(STANDALONE_COVER_SPEC["canvas_file"], "cover/cover-canvas.png")

    def test_cover_qa_gate_includes_scene_poster_checks(self) -> None:
        gate_src = (ROOT / "scripts/excalibur_blog_cover_qa_gate.py").read_text(encoding="utf-8")
        for key in (
            "scene_poster_editorial",
            "forbid_cover_meme_collage",
            "forbid_split_white_collage",
            "validate_cover_scene_poster_gates",
        ):
            self.assertIn(key, gate_src)

    def test_style_fallback_never_pink_cat_for_scene_v2(self) -> None:
        from excalibur_blog_cover_quad_prompt import (
            DEFAULT_STYLE_DOBRY_DOM,
            resolve_style_file,
        )

        self.assertEqual(resolve_style_file({}, ROOT), DEFAULT_STYLE_DOBRY_DOM)
        self.assertNotIn("pink-cat", resolve_style_file({}, ROOT))

    def test_collage_gate_fails_empty_stock(self) -> None:
        from excalibur_blog_cover_collage_gate import detect_empty_stock_room

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "empty.png"
            img = Image.new("RGB", (1200, 675), (210, 210, 208))
            img.save(path)
            result = detect_empty_stock_room(path)
            self.assertTrue(result.get("detected"), result)

    def test_collage_gate_fails_yellow_sticky_soup(self) -> None:
        from excalibur_blog_cover_collage_gate import detect_yellow_sticky_soup

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sticky.png"
            img = Image.new("RGB", (1200, 675), (245, 245, 240))
            draw = ImageDraw.Draw(img)
            for box in ((40, 40, 220, 140), (900, 80, 1100, 200), (200, 500, 420, 620)):
                draw.rectangle(box, fill=(255, 235, 80))
            img.save(path)
            result = detect_yellow_sticky_soup(path)
            self.assertTrue(result.get("detected"), result)

    def test_contract_scene_poster_v2(self) -> None:
        contract = (ROOT / "shared/blog-cover-quad-canvas-contract.md").read_text(encoding="utf-8")
        self.assertIn("scene_poster_v2", contract)
        self.assertIn("standalone", contract.lower())
        self.assertIn("cover-canvas.png", contract)


if __name__ == "__main__":
    unittest.main()
