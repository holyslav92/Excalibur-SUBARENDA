"""Tests for dobry_dom_dzen_story_collage_v2 — full Grsai editorial cover IN one generation."""
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


def _draw_story_barrier_scene(path: Path, size: tuple[int, int] = (1200, 675)) -> None:
    """Theme-derived parking/barrier scene — NOT empty hallway."""
    img = Image.new("RGB", size, (235, 228, 218))
    draw = ImageDraw.Draw(img)
    draw.rectangle((700, 180, 1150, 620), fill=(180, 175, 168))
    draw.rectangle((720, 200, 1120, 380), fill=(90, 95, 100))
    draw.rectangle((750, 400, 1050, 480), fill=(220, 60, 50))
    for x in range(40, 520, 8):
        for y in range(80, 580, 8):
            tone = 210 + ((x * 9 + y * 5) % 30)
            img.putpixel((x, y), (tone, tone - 5, tone - 12))
    draw.rectangle((size[0] - 180, 10, size[0] - 20, 150), fill=(225, 218, 205))
    img.save(path)


def _ensure_fixtures() -> None:
    FIXTURES.mkdir(parents=True, exist_ok=True)
    barrier = FIXTURES / "parking-barrier-story-scene.png"
    if not barrier.is_file():
        _draw_story_barrier_scene(barrier)


class DzenStoryCollageCanonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _ensure_fixtures()

    def test_canon_dzen_story_collage_v2_locked(self) -> None:
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        self.assertEqual(canon["canon_id"], "dobry_dom_dzen_story_collage_v2")
        self.assertEqual(canon.get("replaces"), "dobry_dom_dzen_story_collage_v1")
        rules = canon.get("dzen_story_collage_rules") or {}
        must = " ".join(rules.get("generation_must") or []).casefold()
        self.assertIn("cyrillic", must)
        self.assertIn("phone", must)
        self.assertIn("добрый дом", must)
        factory = rules.get("factory_post_process") or []
        joined_factory = " ".join(factory).casefold()
        self.assertNotIn("poster_composite", joined_factory)
        self.assertNotIn("brand_logo_composite", joined_factory)

    def test_tenant_cover_wow_rules_full_grsai(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        wow = tenant.get("cover_wow_rules") or {}
        self.assertEqual(wow.get("canon_id"), "dobry_dom_dzen_story_collage_v2")
        self.assertEqual(wow.get("cover_generation_mode"), "story_collage_16_9")
        self.assertFalse(wow.get("forbid_model_typography_in_generation"))
        self.assertFalse(wow.get("forbid_model_phone_in_generation"))
        self.assertTrue(wow.get("cover_phone_large_sticker_generation"))
        self.assertFalse(wow.get("cover_phone_factory_post_composite"))
        self.assertTrue(wow.get("forbid_factory_poster_composite"))
        self.assertTrue(wow.get("forbid_factory_logo_paste_on_cover"))

    def test_empty_hallway_not_required_layout(self) -> None:
        from excalibur_blog_cover_quad_prompt import build_standalone_cover_prompt
        from excalibur_blog_meme_cat_gate import load_meme_catalog

        catalog = load_meme_catalog(ROOT)
        style = json.loads((ROOT / "memory/cover/quad-style-dobry-dom.json").read_text(encoding="utf-8"))
        design = json.loads((ROOT / "memory/cover/cover-design-code.json").read_text(encoding="utf-8"))
        manifest = {
            "cover_hook": "Парковка бесплатно — у шлагбаума попросили 800 ₽",
            "cover_figure": "шлагбаум, парковочный талон, барьер",
            "cover_scene": "парковка у подъезда, шлагбаум, талон",
        }
        prompt = build_standalone_cover_prompt(manifest, style, design, meme_catalog=catalog, root=ROOT)
        lowered = prompt.casefold()
        self.assertIn("story collage", lowered)
        self.assertIn("never default empty hallway", lowered)
        self.assertNotIn("zero cyrillic", lowered)

    def test_hero_must_be_theme_derived(self) -> None:
        from excalibur_blog_cover_quad_prompt import build_dzen_story_collage_cover_prompt

        style = json.loads((ROOT / "memory/cover/quad-style-dobry-dom.json").read_text(encoding="utf-8"))
        design = json.loads((ROOT / "memory/cover/cover-design-code.json").read_text(encoding="utf-8"))
        manifest = {
            "cover_figure": "Wi-Fi роутер, ноутбук с созвоном",
            "cover_scene": "рабочий стол в квартире посуточно",
        }
        prompt = build_dzen_story_collage_cover_prompt(manifest, style, design, root=ROOT)
        self.assertIn("Wi-Fi роутер", prompt)
        self.assertIn("рабочий стол", prompt)
        self.assertIn("NEVER default empty hallway", prompt)

    def test_type_phone_logo_in_generation_prompt(self) -> None:
        from excalibur_blog_cover_quad_prompt import build_standalone_cover_prompt
        from excalibur_blog_meme_cat_gate import load_meme_catalog

        catalog = load_meme_catalog(ROOT)
        style = json.loads((ROOT / "memory/cover/quad-style-dobry-dom.json").read_text(encoding="utf-8"))
        design = json.loads((ROOT / "memory/cover/cover-design-code.json").read_text(encoding="utf-8"))
        manifest = {
            "cover_headline_line1": "в чате: парковка бесплатно",
            "cover_headline_line2": "у шлагбаума: +800 ₽",
            "cover_hook_highlight": "800",
            "cover_quote": "Талон не спас",
        }
        prompt = build_standalone_cover_prompt(manifest, style, design, meme_catalog=catalog, root=ROOT)
        self.assertIn("в чате: парковка бесплатно", prompt)
        self.assertIn("у шлагбаума: +800 ₽", prompt)
        self.assertIn("993", prompt)
        self.assertIn("Добрый дом", prompt)
        self.assertIn("no logo png paste", prompt.casefold())
        self.assertIn("no poster composite", prompt.casefold())

    def test_apply_script_resize_only(self) -> None:
        batch_path = ROOT / "memory/blog/articles/B01-beskontaktnoe-zaselenie-posutochno-tyumen/cover/cover-mcp-batch.json"
        if batch_path.is_file():
            batch = json.loads(batch_path.read_text(encoding="utf-8"))
            apply = str((batch.get("preferred_image_flow") or {}).get("apply_script") or "")
            self.assertIn("cover_standalone_apply", apply)
            self.assertNotIn("poster_composite", apply)

    def test_quad_slots_dzen_story_collage(self) -> None:
        from excalibur_blog_quad_slots import uses_dzen_story_collage_v1, uses_full_grsai_cover, uses_type_meme_sticker_v3

        self.assertTrue(uses_dzen_story_collage_v1(ROOT))
        self.assertTrue(uses_full_grsai_cover(ROOT))
        self.assertTrue(uses_type_meme_sticker_v3(ROOT))

    def test_brand_logo_paste_disabled_for_full_grsai(self) -> None:
        from excalibur_blog_brand_logo_composite import load_tenant_logo_config, uses_brand_logo_paste

        cfg = load_tenant_logo_config(ROOT)
        self.assertFalse(uses_brand_logo_paste(cfg))


if __name__ == "__main__":
    unittest.main()
