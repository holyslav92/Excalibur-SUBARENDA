"""Tests for dobry_dom_scene_composite_v1 — scene-only gen + factory poster composite + anti-collage gates."""
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


def _draw_empty_hallway(path: Path, size: tuple[int, int] = (1200, 675)) -> None:
    img = Image.new("RGB", size, (245, 240, 232))
    draw = ImageDraw.Draw(img)
    for x in range(0, size[0], 6):
        for y in range(0, size[1], 6):
            tone = 238 + ((x * 11 + y * 7) % 12)
            img.putpixel((x, y), (tone, tone - 8, tone - 16))
    draw.rectangle((size[0] - 180, 10, size[0] - 20, 150), fill=(230, 222, 210))
    draw.rectangle((40, size[1] - 120, 180, size[1] - 40), fill=(210, 195, 175))
    img.save(path)


def _draw_parking_collage_bad(path: Path) -> None:
    """Regression fixture: model headline stacked on Trade Offer + magnified glyph crops."""
    w, h = 1200, 675
    img = Image.new("RGB", (w, h), (248, 245, 238))
    draw = ImageDraw.Draw(img)
    # Trade Offer left two-panel meme (skin tones) — strong vertical split
    draw.rectangle((20, 250, 300, 400), fill=(215, 178, 142))
    draw.rectangle((20, 410, 300, 610), fill=(120, 85, 65))
    draw.line((310, 240, 310, 620), fill=(10, 10, 10), width=6)
    # Overlapping headline bands (gap between so they stay separate blobs)
    draw.rectangle((330, 30, 950, 105), fill=(12, 14, 18))
    for x in range(350, 920, 14):
        draw.rectangle((x, 50, x + 10, 88), fill=(230, 220, 205))
    draw.rectangle((350, 85, 960, 200), fill=(14, 16, 22))
    for x in range(370, 940, 16):
        draw.rectangle((x, 145, x + 12, 175), fill=(195, 170, 135))
    # Magnified letter crop blob >12% canvas
    draw.rectangle((480, 320, 860, 640), fill=(10, 12, 16))
    draw.rectangle((500, 340, 840, 620), fill=(235, 228, 218))
    draw.rectangle((520, 360, 780, 600), fill=(8, 10, 14))
    # Phone tablo overlap zone
    draw.rounded_rectangle((760, 400, 1140, 560), radius=18, fill=(28, 105, 200), outline=(255, 255, 255), width=5)
    draw.rectangle((800, 450, 1100, 510), fill=(255, 255, 255))
    img.save(path)


def _ensure_fixtures() -> None:
    FIXTURES.mkdir(parents=True, exist_ok=True)
    bad = FIXTURES / "parking-shlagbaum-collage-bad.png"
    if not bad.is_file():
        _draw_parking_collage_bad(bad)
    scene = FIXTURES / "scene-only-hallway-good.png"
    if not scene.is_file():
        _draw_empty_hallway(scene)
    meme_dir = ROOT / "memory/cover/memes"
    meme_dir.mkdir(parents=True, exist_ok=True)
    meme = meme_dir / "trade_offer.png"
    if not meme.is_file():
        m = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
        d = ImageDraw.Draw(m)
        d.rectangle((10, 10, 190, 95), fill=(210, 175, 140, 255))
        d.rectangle((10, 105, 190, 190), fill=(195, 160, 125, 255))
        m.save(meme)


class SceneCompositeCanonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _ensure_fixtures()

    def test_canon_scene_composite_v1_locked(self) -> None:
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        self.assertEqual(canon["canon_id"], "dobry_dom_scene_composite_v1")
        rules = canon.get("scene_composite_rules") or {}
        self.assertIn("factory_post_process", rules)
        self.assertIn("forbid_overlapping_text_blocks", rules.get("anti_collage_gates", []))

    def test_tenant_cover_wow_rules_scene_composite(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        wow = tenant.get("cover_wow_rules") or {}
        self.assertEqual(wow.get("canon_id"), "dobry_dom_scene_composite_v1")
        self.assertTrue(wow.get("forbid_model_typography_in_generation"))
        self.assertTrue(wow.get("forbid_overlapping_text_blocks"))
        self.assertTrue(wow.get("forbid_giant_cropped_glyph"))
        self.assertTrue(wow.get("forbid_model_drawn_meme_template"))

    def test_scene_only_prompt_has_no_cyrillic_meme_phone(self) -> None:
        from excalibur_blog_cover_quad_prompt import build_standalone_cover_prompt
        from excalibur_blog_meme_cat_gate import load_meme_catalog

        catalog = load_meme_catalog(ROOT)
        style = json.loads((ROOT / "memory/cover/quad-style-dobry-dom.json").read_text(encoding="utf-8"))
        design = json.loads((ROOT / "memory/cover/cover-design-code.json").read_text(encoding="utf-8"))
        manifest = {"cover_hook": "Парковка бесплатно — у шлагбаума попросили 800 ₽"}
        prompt = build_standalone_cover_prompt(manifest, style, design, meme_catalog=catalog, root=ROOT)
        lowered = prompt.casefold()
        self.assertIn("empty", lowered)
        self.assertIn("zero cyrillic", lowered)
        self.assertIn("zero digits", lowered)
        self.assertIn("zero meme", lowered)
        self.assertIn("zero phone", lowered)
        self.assertIn("trade offer", lowered)
        self.assertNotIn("exactly one catalog meme die-cut", lowered)
        self.assertNotIn("exactly one catalog meme die-cut", lowered)

    def test_quad_slots_scene_composite(self) -> None:
        from excalibur_blog_quad_slots import uses_scene_composite_v1, uses_type_meme_sticker_v3

        self.assertTrue(uses_scene_composite_v1(ROOT))
        self.assertTrue(uses_type_meme_sticker_v3(ROOT))


class SceneCompositeAntiCollageGateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _ensure_fixtures()

    def test_parking_fixture_fails_anti_collage_gates(self) -> None:
        from excalibur_blog_cover_collage_gate import validate_cover_anti_collage_gates

        fixture = FIXTURES / "parking-shlagbaum-collage-bad.png"
        errors = validate_cover_anti_collage_gates(fixture)
        self.assertTrue(errors)
        joined = " ".join(errors).lower()
        self.assertTrue(
            "overlapping text" in joined or "trade offer" in joined or "glyph" in joined,
            joined,
        )

    def test_detect_overlapping_text_blocks(self) -> None:
        from excalibur_blog_cover_collage_gate import (
            detect_overlapping_text_blocks,
            detect_stacked_type_layers,
            validate_cover_anti_collage_gates,
        )

        fixture = FIXTURES / "parking-shlagbaum-collage-bad.png"
        stacked = detect_stacked_type_layers(fixture)
        overlap = detect_overlapping_text_blocks(fixture)
        anti = validate_cover_anti_collage_gates(fixture)
        self.assertTrue(
            stacked.get("detected") or overlap.get("detected") or bool(anti),
            {"stacked": stacked, "overlap": overlap, "anti": anti},
        )

    def test_detect_giant_cropped_glyph(self) -> None:
        from excalibur_blog_cover_collage_gate import detect_giant_cropped_glyph

        result = detect_giant_cropped_glyph(FIXTURES / "parking-shlagbaum-collage-bad.png")
        self.assertTrue(result.get("detected"), result)

    def test_detect_trade_offer_template(self) -> None:
        from excalibur_blog_cover_collage_gate import detect_model_drawn_trade_offer_template

        result = detect_model_drawn_trade_offer_template(FIXTURES / "parking-shlagbaum-collage-bad.png")
        self.assertTrue(result.get("detected"), result)

    def test_empty_scene_passes_scene_only_gate(self) -> None:
        from excalibur_blog_cover_collage_gate import validate_scene_only_canvas

        errors = validate_scene_only_canvas(FIXTURES / "scene-only-hallway-good.png")
        self.assertEqual(errors, [])

    def test_collage_bad_fails_scene_only_gate(self) -> None:
        from excalibur_blog_cover_collage_gate import validate_scene_only_canvas

        errors = validate_scene_only_canvas(FIXTURES / "parking-shlagbaum-collage-bad.png")
        self.assertTrue(errors)

    def test_cover_qa_gate_includes_anti_collage_checks(self) -> None:
        gate_src = (ROOT / "scripts/excalibur_blog_cover_qa_gate.py").read_text(encoding="utf-8")
        for key in (
            "forbid_overlapping_text_blocks",
            "forbid_giant_cropped_glyph",
            "forbid_model_drawn_meme_template",
            "poster_composite_stamp_pass",
            "validate_cover_anti_collage_gates",
            "poster-composite-stamp.json",
        ):
            self.assertIn(key, gate_src)


class PosterCompositeScriptTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        _ensure_fixtures()

    def test_poster_composite_produces_cover_and_stamp(self) -> None:
        from excalibur_blog_cover_poster_composite import composite_poster_cover

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            article = root / "article"
            cover = article / "cover"
            cover.mkdir(parents=True)
            (root / "memory/cover").mkdir(parents=True)
            (root / "shared").mkdir(parents=True)
            tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
            (root / "shared/tenant-config.json").write_text(
                json.dumps(tenant, ensure_ascii=False), encoding="utf-8"
            )
            for rel in (
                "memory/cover/meme-top100.json",
                "memory/cover/meme-used.json",
                "memory/cover/cover-canon.json",
            ):
                src = ROOT / rel
                dst = root / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            meme_src = ROOT / "memory/cover/memes/trade_offer.png"
            meme_dst = root / "memory/cover/memes/trade_offer.png"
            meme_dst.parent.mkdir(parents=True, exist_ok=True)
            meme_dst.write_bytes(meme_src.read_bytes())
            for rel in ("Cormorant-SemiBoldItalic.ttf", "Onest-ExtraBold.ttf"):
                font_src = ROOT / "memory/cover/assets/fonts" / rel
                font_dst = root / "memory/cover/assets/fonts" / rel
                font_dst.parent.mkdir(parents=True, exist_ok=True)
                font_dst.write_bytes(font_src.read_bytes())
            _draw_empty_hallway(cover / "cover-canvas.png")
            manifest = {
                "cover_headline_line1": "в чате: парковка бесплатно",
                "cover_headline_line2": "у шлагбаума: +800 ₽",
                "cover_phone_cta": "+7 (993) 574-83-22",
                "slots": {"cover": {"meme_id": "trade_offer"}},
            }
            (cover / "quad-manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False), encoding="utf-8"
            )
            stamp = composite_poster_cover(article, root)
            self.assertEqual(stamp.get("status"), "PASS")
            self.assertEqual(stamp["meme"]["id"], "trade_offer")
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
