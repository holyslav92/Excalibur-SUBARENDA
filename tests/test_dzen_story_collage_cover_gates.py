"""Tests for dobry_dom_gen_only_human_v1 — photoreal generate-only + logo paste cover only."""
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
    img = Image.new("RGB", size, (235, 228, 218))
    draw = ImageDraw.Draw(img)
    draw.rectangle((700, 180, 1150, 620), fill=(180, 175, 168))
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

    def test_canon_slice4_v1_locked(self) -> None:
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        self.assertEqual(canon["canon_id"], "dobry_dom_gen_only_human_v1")
        rules = canon.get("gen_only_rules") or {}
        phil = str(rules.get("philosophy") or "").casefold()
        self.assertIn("photoreal", phil)
        self.assertIn("native aspect", phil)

    def test_tenant_cover_wow_rules_gen_only(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        wow = tenant.get("cover_wow_rules") or {}
        img = tenant.get("image_generation") or {}
        self.assertEqual(wow.get("canon_id"), "dobry_dom_gen_only_human_v1")
        self.assertEqual(wow.get("logo_mode"), "factory_paste_cover_only")
        self.assertTrue(wow.get("forbid_logo_reference_in_generation"))
        self.assertTrue(img.get("logo_never_as_generation_reference"))
        self.assertFalse(img.get("logo_required_as_generation_reference"))
        self.assertFalse(wow.get("forbid_factory_logo_paste_on_cover"))
        self.assertTrue(wow.get("forbid_ai_drawn_logo"))

    def test_type_in_generation_logo_native_aspect_not_square(self) -> None:
        from excalibur_blog_cover_quad_prompt import build_one_2k_slice4_grid_prompt

        style = json.loads((ROOT / "memory/cover/quad-style-dobry-dom.json").read_text(encoding="utf-8"))
        design = json.loads((ROOT / "memory/cover/cover-design-code.json").read_text(encoding="utf-8"))
        manifest = {
            "cover_headline_line1": "в чате: парковка бесплатно",
            "cover_headline_line2": "у шлагбаума: +800 ₽",
        }
        prompt = build_one_2k_slice4_grid_prompt(manifest, style, design, root=ROOT)
        lowered = prompt.casefold()
        self.assertIn("native aspect", lowered)
        self.assertIn("not square", lowered)
        self.assertIn("cropped-img_7143", lowered)

    def test_poster_composite_script_blocked(self) -> None:
        import subprocess

        proc = subprocess.run(
            [sys.executable, "scripts/excalibur_blog_cover_poster_composite.py", "--article-dir", "."],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 1)
        self.assertIn("BLOCKER", proc.stderr)

    def test_cover_batch_apply_script_includes_logo_composite(self) -> None:
        from excalibur_blog_brand_logo_composite import load_tenant_logo_config, uses_brand_logo_paste
        from excalibur_blog_identity_real import tenant_uses_logo_reference_in_generation

        cfg = load_tenant_logo_config(ROOT)
        self.assertTrue(uses_brand_logo_paste(cfg))
        self.assertFalse(tenant_uses_logo_reference_in_generation(ROOT))

    def test_quad_slots_one_2k_slice4(self) -> None:
        from excalibur_blog_quad_slots import uses_one_2k_slice4, uses_full_grsai_cover

        self.assertTrue(uses_one_2k_slice4(ROOT))
        self.assertTrue(uses_full_grsai_cover(ROOT))


if __name__ == "__main__":
    unittest.main()
