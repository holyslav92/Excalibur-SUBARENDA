"""Tests for dobry_dom_dzen_story_collage_v2 — full Grsai cover + anti-collage gates."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
FIXTURES = ROOT / "tests" / "fixtures"


def _draw_parking_collage_bad(path: Path) -> None:
    """Regression fixture: model headline stacked on Trade Offer + magnified glyph crops."""
    w, h = 1200, 675
    img = Image.new("RGB", (w, h), (248, 245, 238))
    draw = ImageDraw.Draw(img)
    draw.rectangle((20, 250, 300, 400), fill=(215, 178, 142))
    draw.rectangle((20, 410, 300, 610), fill=(120, 85, 65))
    draw.line((310, 240, 310, 620), fill=(10, 10, 10), width=6)
    draw.rectangle((330, 30, 950, 105), fill=(12, 14, 18))
    for x in range(350, 920, 14):
        draw.rectangle((x, 50, x + 10, 88), fill=(230, 220, 205))
    draw.rectangle((350, 85, 960, 200), fill=(14, 16, 22))
    for x in range(370, 940, 16):
        draw.rectangle((x, 145, x + 12, 175), fill=(195, 170, 135))
    draw.rectangle((480, 320, 860, 640), fill=(10, 12, 16))
    draw.rectangle((500, 340, 840, 620), fill=(235, 228, 218))
    draw.rectangle((520, 360, 780, 600), fill=(8, 10, 14))
    draw.rounded_rectangle((760, 400, 1140, 560), radius=18, fill=(28, 105, 200), outline=(255, 255, 255), width=5)
    draw.rectangle((800, 450, 1100, 510), fill=(255, 255, 255))
    img.save(path)


def _ensure_fixtures() -> None:
    FIXTURES.mkdir(parents=True, exist_ok=True)
    bad = FIXTURES / "parking-shlagbaum-collage-bad.png"
    if not bad.is_file():
        _draw_parking_collage_bad(bad)


class SceneCompositeCanonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _ensure_fixtures()

    def test_canon_v2_locked(self) -> None:
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        self.assertEqual(canon["canon_id"], "dobry_dom_dzen_story_collage_v2")
        rules = canon.get("dzen_story_collage_rules") or {}
        anti = rules.get("anti_collage_gates") or []
        self.assertIn("forbid_overlapping_text_blocks", anti)
        self.assertNotIn("poster_composite_stamp_pass", anti)

    def test_tenant_cover_wow_rules_full_grsai(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        wow = tenant.get("cover_wow_rules") or {}
        self.assertEqual(wow.get("canon_id"), "dobry_dom_dzen_story_collage_v2")
        self.assertFalse(wow.get("forbid_model_typography_in_generation"))
        self.assertTrue(wow.get("forbid_overlapping_text_blocks"))
        self.assertTrue(wow.get("forbid_giant_cropped_glyph"))
        self.assertTrue(wow.get("forbid_model_drawn_meme_template"))

    def test_full_grsai_prompt_requires_type_phone_logo(self) -> None:
        from excalibur_blog_cover_quad_prompt import build_standalone_cover_prompt
        from excalibur_blog_meme_cat_gate import load_meme_catalog

        catalog = load_meme_catalog(ROOT)
        style = json.loads((ROOT / "memory/cover/quad-style-dobry-dom.json").read_text(encoding="utf-8"))
        design = json.loads((ROOT / "memory/cover/cover-design-code.json").read_text(encoding="utf-8"))
        manifest = {"cover_hook": "Парковка бесплатно — у шлагбаума попросили 800 ₽"}
        prompt = build_standalone_cover_prompt(manifest, style, design, meme_catalog=catalog, root=ROOT)
        lowered = prompt.casefold()
        self.assertIn("story collage", lowered)
        self.assertIn("cyrillic", lowered)
        self.assertIn("993", prompt)
        self.assertIn("добрый дом", lowered)
        self.assertNotIn("zero cyrillic", lowered)
        self.assertIn("no poster composite", lowered)
        self.assertIn("no logo png paste", lowered)

    def test_quad_slots_scene_composite(self) -> None:
        from excalibur_blog_quad_slots import uses_dzen_story_collage_v1, uses_full_grsai_cover

        self.assertTrue(uses_dzen_story_collage_v1(ROOT))
        self.assertTrue(uses_full_grsai_cover(ROOT))


class SceneCompositeAntiCollageGateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _ensure_fixtures()

    def test_parking_fixture_fails_anti_collage_gates(self) -> None:
        from excalibur_blog_cover_collage_gate import validate_cover_anti_collage_gates

        fixture = FIXTURES / "parking-shlagbaum-collage-bad.png"
        errors = validate_cover_anti_collage_gates(fixture)
        self.assertTrue(errors)

    def test_cover_qa_gate_includes_anti_collage_not_poster_stamp(self) -> None:
        gate_src = (ROOT / "scripts/excalibur_blog_cover_qa_gate.py").read_text(encoding="utf-8")
        for key in (
            "forbid_overlapping_text_blocks",
            "forbid_giant_cropped_glyph",
            "forbid_model_drawn_meme_template",
            "validate_cover_anti_collage_gates",
            "FULL_GRSAI_COVER_CHECKS",
            "validate_full_grsai_cover_gates",
        ):
            self.assertIn(key, gate_src)
        full_grsai_block = gate_src.split("FULL_GRSAI_COVER_CHECKS", 1)[1].split("LOGO_REFERENCE_CHECKS", 1)[0]
        self.assertNotIn("poster_composite_stamp_pass", full_grsai_block)


class StandaloneApplyTest(unittest.TestCase):
    def test_standalone_apply_resize_only_report(self) -> None:
        from excalibur_blog_cover_standalone_apply import apply_standalone_cover

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            article = root / "article"
            cover = article / "cover"
            cover.mkdir(parents=True)
            img = Image.new("RGB", (2048, 1152), (240, 235, 228))
            img.save(cover / "cover-canvas.png")
            report = apply_standalone_cover(article, root, skip_pad_clear=True)
            self.assertEqual(report.get("logo_paste"), "in_generation_not_factory_paste")
            self.assertTrue((cover / "cover.png").is_file())


if __name__ == "__main__":
    unittest.main()
