"""Tests for type_meme_sticker_v3 cover gates — scene no-meme FAIL, type+meme+phone PASS."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


def _draw_type_poster_v3(path: Path) -> None:
    """Synthetic v3 PASS poster: headline band + meme zone + large phone sticker."""
    img = Image.new("RGB", (1200, 675), (248, 245, 238))
    draw = ImageDraw.Draw(img)
    # Global subtle paper texture (incl. top-right logo pad)
    for x in range(0, 1200, 5):
        for y in range(0, 675, 5):
            base = img.getpixel((x, y))
            img.putpixel((x, y), tuple(max(0, min(255, c + ((x * 13 + y * 7) % 11) - 5)) for c in base))
    # Headline typography band (dark blocks with edge texture)
    draw.rectangle((48, 36, 900, 210), fill=(20, 24, 32))
    for x in range(70, 880, 14):
        draw.rectangle((x, 60, x + 8, 95), fill=(235, 228, 215))
        draw.rectangle((x, 110, x + 10, 145), fill=(200, 175, 140))
    for y in range(50, 200, 11):
        draw.line((60, y, 880, y), fill=(35, 40, 50), width=1)
    # Meme sticker zone bottom-left (high contrast cutout)
    for x in range(40, 280, 3):
        for y in range(480, 640, 3):
            img.putpixel((x, y), (30 + (x % 40), 25 + (y % 35), 20 + ((x + y) % 30)))
    draw.ellipse((60, 500, 250, 620), fill=(90, 70, 55), outline=(10, 10, 10), width=4)
    # Large phone sticker mid-right (saturated blue — not pill/beige)
    draw.rounded_rectangle((780, 420, 1120, 540), radius=18, fill=(30, 110, 210), outline=(255, 255, 255), width=5)
    draw.rectangle((820, 460, 1080, 505), fill=(255, 255, 255))
    # Logo pad zone: decorative hatch (high local variance — not a blank plate)
    for x in range(1040, 1195):
        for y in range(8, 178):
            tone = 205 + ((x * 17 + y * 23) % 35)
            img.putpixel((x, y), (tone, tone - 18, tone - 32))
    img.save(path)


def _draw_people_scene_no_meme(path: Path) -> None:
    """Synthetic scene_poster_v2-style FAIL: people tones, no meme, no headline, no phone sticker."""
    img = Image.new("RGB", (1200, 675), (185, 175, 160))
    draw = ImageDraw.Draw(img)
    # Doorway / people flesh tones in center
    draw.rectangle((200, 120, 1000, 620), fill=(205, 175, 145))
    for x in range(280, 520, 8):
        for y in range(180, 580, 8):
            img.putpixel((x, y), (210 + (x % 25), 150 + (y % 20), 120 + ((x + y) % 18)))
    for x in range(620, 920, 8):
        for y in range(200, 600, 8):
            img.putpixel((x, y), (200 + (x % 22), 160 + (y % 18), 130 + ((x + y) % 16)))
    # Tiny in-scene phone text only
    draw.text((720, 520), "+7 993 574-83-22", fill=(30, 30, 30))
    img.save(path)


class TypeMemeStickerCoverGateTest(unittest.TestCase):
    def test_canon_slice4_locked(self) -> None:
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        self.assertEqual(canon["canon_id"], "dobry_dom_one_2k_slice4_v1")
        self.assertEqual((canon.get("pipeline") or {}).get("total_images"), 4)

    def test_tenant_cover_wow_rules_slice4(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        wow = tenant.get("cover_wow_rules") or {}
        self.assertEqual(wow.get("canon_id"), "dobry_dom_one_2k_slice4_v1")
        self.assertEqual(wow.get("cover_generation_mode"), "story_collage_16_9")
        self.assertFalse(wow.get("require_cover_meme_sticker"))
        self.assertTrue(wow.get("require_display_headline"))
        self.assertTrue(wow.get("require_large_phone_sticker"))
        self.assertTrue(wow.get("forbid_people_heavy_cover"))
        self.assertTrue(wow.get("vip_disabled"))

    def test_collage_gate_fails_split_white_panel(self) -> None:
        from excalibur_blog_cover_collage_gate import (
            detect_split_white_collage,
            validate_cover_type_meme_sticker_gates,
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
            errors = validate_cover_type_meme_sticker_gates(path)
            self.assertTrue(errors)

    def test_collage_gate_fails_people_scene_no_meme(self) -> None:
        from excalibur_blog_cover_collage_gate import validate_cover_type_meme_sticker_gates

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "scene.png"
            _draw_people_scene_no_meme(path)
            errors = validate_cover_type_meme_sticker_gates(path)
            self.assertTrue(errors)
            joined = " ".join(errors)
            self.assertIn("meme", joined.lower())
            self.assertTrue(
                "people-heavy" in joined or "headline" in joined or "phone sticker" in joined,
                joined,
            )

    def test_collage_gate_passes_type_meme_phone_sticker(self) -> None:
        from excalibur_blog_cover_collage_gate import detect_type_meme_sticker_pass

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "poster.png"
            _draw_type_poster_v3(path)
            heuristic = detect_type_meme_sticker_pass(path)
            self.assertTrue(heuristic.get("pass"), heuristic)
            self.assertTrue(heuristic["headline"].get("detected"), heuristic)
            self.assertGreaterEqual(heuristic["meme_zones"].get("count", 0), 1, heuristic)
            self.assertTrue(heuristic["phone_sticker"].get("detected"), heuristic)
            self.assertFalse(heuristic["people_heavy"].get("detected"), heuristic)

    def test_slice4_prompt_requires_grid(self) -> None:
        from excalibur_blog_cover_quad_prompt import build_one_2k_slice4_grid_prompt
        from excalibur_blog_meme_cat_gate import load_meme_catalog

        catalog = load_meme_catalog(ROOT)
        style = json.loads((ROOT / "memory/cover/quad-style-dobry-dom.json").read_text(encoding="utf-8"))
        design = json.loads((ROOT / "memory/cover/cover-design-code.json").read_text(encoding="utf-8"))
        manifest = {"cover_hook": "У двери — доплата за третьего", "cover_scene": "доплата за третьего гостя"}
        prompt = build_one_2k_slice4_grid_prompt(manifest, style, design, root=ROOT)
        lowered = prompt.casefold()
        self.assertIn("2×2", prompt)
        self.assertIn("993", prompt)
        self.assertIn("native aspect", lowered)

    def test_quad_slots_slice4_spec(self) -> None:
        from excalibur_blog_quad_slots import (
            SLICE4_CANVAS_SPEC,
            all_canvas_specs,
            uses_one_2k_slice4,
        )

        self.assertTrue(uses_one_2k_slice4(ROOT))
        specs = all_canvas_specs(3)
        self.assertEqual(len(specs), 1)
        self.assertTrue(specs[0].get("slice4_grid"))
        self.assertEqual(SLICE4_CANVAS_SPEC["canvas_file"], "cover/canvas-slice4.png")

    def test_cover_qa_gate_includes_type_meme_sticker_checks(self) -> None:
        gate_src = (ROOT / "scripts/excalibur_blog_cover_qa_gate.py").read_text(encoding="utf-8")
        for key in (
            "type_meme_sticker_editorial",
            "require_cover_meme_sticker",
            "require_display_headline",
            "require_large_phone_sticker",
            "forbid_people_heavy_cover",
            "forbid_split_white_collage",
            "validate_cover_type_meme_sticker_gates",
        ):
            self.assertIn(key, gate_src)

    def test_style_fallback_never_pink_cat_for_v3(self) -> None:
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

    def test_collage_gate_fails_metallic_gold(self) -> None:
        from excalibur_blog_cover_collage_gate import detect_metallic_gold_dominance

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "gold.png"
            img = Image.new("RGB", (1200, 675), (245, 240, 230))
            draw = ImageDraw.Draw(img)
            draw.rectangle((80, 40, 700, 220), fill=(218, 165, 32))
            for x in range(90, 680, 12):
                draw.rectangle((x, 60, x + 8, 100), fill=(255, 215, 0))
            img.save(path)
            result = detect_metallic_gold_dominance(path)
            self.assertTrue(result.get("detected"), result)

    def test_collage_gate_fails_dark_leather(self) -> None:
        from excalibur_blog_cover_collage_gate import detect_dark_leather_dominance

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "leather.png"
            img = Image.new("RGB", (1200, 675), (45, 30, 20))
            draw = ImageDraw.Draw(img)
            draw.rectangle((0, 0, 1200, 675), fill=(55, 35, 22))
            img.save(path)
            result = detect_dark_leather_dominance(path)
            self.assertTrue(result.get("detected"), result)

    def test_two_beat_headline_in_prompt(self) -> None:
        from excalibur_blog_cover_quad_prompt import build_one_2k_slice4_grid_prompt, build_case_cover_context
        from excalibur_blog_meme_cat_gate import load_meme_catalog

        manifest = {
            "cover_headline_line1": "в чате: можно с лапой",
            "cover_headline_line2": "у двери: +3000 ₽",
            "cover_hook": "После заселения — доплата 3000 за лапу",
        }
        case = build_case_cover_context(manifest)
        self.assertEqual(case["headline_line1"], "в чате: можно с лапой")
        self.assertEqual(case["headline_line2"], "у двери: +3000 ₽")
        catalog = load_meme_catalog(ROOT)
        style = json.loads((ROOT / "memory/cover/quad-style-dobry-dom.json").read_text(encoding="utf-8"))
        design = json.loads((ROOT / "memory/cover/cover-design-code.json").read_text(encoding="utf-8"))
        prompt = build_one_2k_slice4_grid_prompt(manifest, style, design, root=ROOT)
        self.assertIn("2×2", prompt)
        self.assertIn("в чате: можно с лапой", prompt)

        contract = (ROOT / "shared/blog-cover-quad-canvas-contract.md").read_text(encoding="utf-8")
        self.assertIn("dobry_dom_one_2k_slice4_v1", contract)
        self.assertIn("brand_logo_composite", contract)

    def test_live_lapoy_fixture_fails_type_meme_gates(self) -> None:
        """Regression: shipped people-scene lapoy cover must FAIL all v3 gates."""
        fixture = ROOT / "tests/fixtures/lapoy-live-cover-bad.png"
        self.assertTrue(fixture.is_file(), fixture)
        from excalibur_blog_cover_collage_gate import validate_cover_type_meme_sticker_gates
        from excalibur_blog_drawn_logo_gate import detect_white_plate_in_pad

        errors = validate_cover_type_meme_sticker_gates(fixture)
        self.assertTrue(errors)
        joined = " ".join(errors).lower()
        self.assertIn("people-heavy", joined)
        self.assertTrue(
            "meme" in joined or "glyph" in joined or "trade offer" in joined or "drake" in joined,
            joined,
        )
        plate = detect_white_plate_in_pad(fixture)
        self.assertTrue(plate.get("detected"), plate)

    def test_cream_tr_plate_fails_detect(self) -> None:
        from excalibur_blog_drawn_logo_gate import detect_white_plate_in_pad

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "cream-tr.png"
            img = Image.new("RGB", (1200, 675), (100, 110, 120))
            draw = ImageDraw.Draw(img)
            x0 = 1200 - 200
            draw.rectangle((x0, 12, 1190, 140), fill=(225, 222, 215))
            img.save(path)
            result = detect_white_plate_in_pad(path)
            self.assertTrue(result.get("detected"), result)
            self.assertGreaterEqual(float(result.get("plate_mean_luma") or 0), 200.0)


if __name__ == "__main__":
    unittest.main()
