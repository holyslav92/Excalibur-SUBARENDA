"""Tests for dobry_dom_dzen_story_collage_v1 — story scene + factory type overlay + anti-collage gates."""
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
    # Barrier arm + ticket booth tones (story props)
    draw.rectangle((700, 180, 1150, 620), fill=(180, 175, 168))
    draw.rectangle((720, 200, 1120, 380), fill=(90, 95, 100))
    draw.rectangle((750, 400, 1050, 480), fill=(220, 60, 50))
    # Blurred apartment window left
    for x in range(40, 520, 8):
        for y in range(80, 580, 8):
            tone = 210 + ((x * 9 + y * 5) % 30)
            img.putpixel((x, y), (tone, tone - 5, tone - 12))
    draw.rectangle((size[0] - 180, 10, size[0] - 20, 150), fill=(225, 218, 205))
    img.save(path)


def _draw_empty_hallway(path: Path, size: tuple[int, int] = (1200, 675)) -> None:
    img = Image.new("RGB", size, (245, 240, 232))
    draw = ImageDraw.Draw(img)
    for x in range(0, size[0], 6):
        for y in range(0, size[1], 6):
            tone = 238 + ((x * 11 + y * 7) % 12)
            img.putpixel((x, y), (tone, tone - 8, tone - 16))
    draw.rectangle((size[0] - 180, 10, size[0] - 20, 150), fill=(230, 222, 210))
    img.save(path)


def _ensure_fixtures() -> None:
    FIXTURES.mkdir(parents=True, exist_ok=True)
    barrier = FIXTURES / "parking-barrier-story-scene.png"
    if not barrier.is_file():
        _draw_story_barrier_scene(barrier)
    hallway = FIXTURES / "scene-only-hallway-good.png"
    if not hallway.is_file():
        _draw_empty_hallway(hallway)
    meme_dir = ROOT / "memory/cover/memes"
    meme_dir.mkdir(parents=True, exist_ok=True)
    meme = meme_dir / "roll_safe.png"
    if not meme.is_file():
        m = Image.new("RGBA", (180, 180), (0, 0, 0, 0))
        d = ImageDraw.Draw(m)
        d.ellipse((20, 20, 160, 160), fill=(120, 90, 70, 255))
        m.save(meme)


class DzenStoryCollageCanonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _ensure_fixtures()

    def test_canon_dzen_story_collage_v1_locked(self) -> None:
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        self.assertEqual(canon["canon_id"], "dobry_dom_dzen_story_collage_v1")
        self.assertEqual(canon.get("replaces"), "dobry_dom_scene_composite_v1")
        rules = canon.get("dzen_story_collage_rules") or {}
        must_not = " ".join(rules.get("generation_must_not") or []).casefold()
        self.assertIn("empty", must_not)
        self.assertIn("hallway", must_not)
        self.assertIn("blinking", must_not)

    def test_tenant_cover_wow_rules_dzen_story_collage(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        wow = tenant.get("cover_wow_rules") or {}
        self.assertEqual(wow.get("canon_id"), "dobry_dom_dzen_story_collage_v1")
        self.assertEqual(wow.get("cover_generation_mode"), "story_collage_16_9")
        self.assertTrue(wow.get("forbid_model_typography_in_generation"))
        self.assertFalse(wow.get("require_cover_meme_sticker"))

    def test_empty_hallway_not_required_layout(self) -> None:
        """(a) parking-empty-hallway+blinking-guy is NOT the required layout."""
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
        self.assertNotIn("empty scene only, not a poster", lowered.replace("story collage scene, not a type poster", ""))
        self.assertNotIn("people: zero — no guests", lowered)
        self.assertNotIn("blinking_white_guy", lowered)

    def test_hero_must_be_theme_derived(self) -> None:
        """(b) hero must be theme-derived from manifest case atoms."""
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

    def test_type_overlay_still_factory(self) -> None:
        """(c) type overlay still factory — zero Cyrillic in generation prompt."""
        from excalibur_blog_cover_quad_prompt import build_standalone_cover_prompt
        from excalibur_blog_meme_cat_gate import load_meme_catalog

        catalog = load_meme_catalog(ROOT)
        style = json.loads((ROOT / "memory/cover/quad-style-dobry-dom.json").read_text(encoding="utf-8"))
        design = json.loads((ROOT / "memory/cover/cover-design-code.json").read_text(encoding="utf-8"))
        manifest = {
            "cover_headline_line1": "в чате: парковка бесплатно",
            "cover_headline_line2": "у шлагбаума: +800 ₽",
            "cover_hook_highlight": "800",
        }
        prompt = build_standalone_cover_prompt(manifest, style, design, meme_catalog=catalog, root=ROOT)
        lowered = prompt.casefold()
        self.assertIn("zero cyrillic", lowered)
        self.assertIn("factory", lowered)
        self.assertNotIn("в чате: парковка бесплатно", prompt)

    def test_phone_993_only(self) -> None:
        """(d) phone 993 only — forbidden 922 in canon and poster composite."""
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        phone_rules = canon["wow_cover_rules"]["no_element_overlap"]["cover_phone"]
        self.assertEqual(phone_rules["display"], "+7 (993) 574-83-22")
        self.assertEqual(phone_rules.get("forbidden_phone"), "+7 922 001 65 05")
        from excalibur_blog_cover_poster_composite import draw_phone_bar, FORBIDDEN_PHONE

        with tempfile.TemporaryDirectory() as tmp:
            from PIL import Image, ImageDraw

            img = Image.new("RGBA", (1200, 675), (255, 255, 255, 255))
            draw = ImageDraw.Draw(img)
            with self.assertRaises(ValueError):
                draw_phone_bar(draw, FORBIDDEN_PHONE, width=1200, height=675, root=ROOT)

    def test_quad_slots_dzen_story_collage(self) -> None:
        from excalibur_blog_quad_slots import uses_dzen_story_collage_v1, uses_type_meme_sticker_v3

        self.assertTrue(uses_dzen_story_collage_v1(ROOT))
        self.assertTrue(uses_type_meme_sticker_v3(ROOT))

    def test_story_scene_passes_pre_composite_gate(self) -> None:
        from excalibur_blog_cover_collage_gate import validate_story_scene_canvas

        errors = validate_story_scene_canvas(FIXTURES / "parking-barrier-story-scene.png")
        self.assertEqual(errors, [])


class DzenStoryPosterCompositeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _ensure_fixtures()

    def test_poster_composite_onest_brush_sticky_phone(self) -> None:
        from excalibur_blog_cover_poster_composite import composite_poster_cover, POSTER_MODE

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            article = root / "article"
            cover = article / "cover"
            cover.mkdir(parents=True)
            for rel in (
                "memory/cover/meme-top100.json",
                "memory/cover/meme-used.json",
                "memory/cover/cover-canon.json",
            ):
                src = ROOT / rel
                dst = root / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            for rel in ("Onest-ExtraBold.ttf",):
                font_src = ROOT / "memory/cover/assets/fonts" / rel
                font_dst = root / "memory/cover/assets/fonts" / rel
                font_dst.parent.mkdir(parents=True, exist_ok=True)
                font_dst.write_bytes(font_src.read_bytes())
            _draw_story_barrier_scene(cover / "cover-canvas.png")
            manifest = {
                "cover_headline_line1": "в чате: парковка бесплатно",
                "cover_headline_line2": "у шлагбаума: +800 ₽",
                "cover_hook_highlight": "800",
                "cover_phone_cta": "+7 (993) 574-83-22",
                "cover_quote": "Талон не спас",
                "slots": {"cover": {"sticky": "Талон не спас"}},
            }
            (cover / "quad-manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False), encoding="utf-8"
            )
            stamp = composite_poster_cover(article, root)
            self.assertEqual(stamp.get("status"), "PASS")
            self.assertEqual(stamp.get("mode"), POSTER_MODE)
            self.assertEqual(stamp["phone"]["display"], "+7 (993) 574-83-22")
            self.assertTrue((cover / "cover.png").is_file())
            self.assertTrue((cover / "poster-composite-stamp.json").is_file())
            from excalibur_blog_cover_collage_gate import (
                detect_display_headline,
                detect_large_phone_sticker,
            )

            cover_path = cover / "cover.png"
            self.assertTrue(detect_display_headline(cover_path).get("detected"))
            self.assertTrue(detect_large_phone_sticker(cover_path).get("detected"))


if __name__ == "__main__":
    unittest.main()
