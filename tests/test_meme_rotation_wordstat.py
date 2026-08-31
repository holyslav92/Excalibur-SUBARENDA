"""Tests for meme rotation and Wordstat seed canon."""
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class MemeRotationTest(unittest.TestCase):
    def test_meme_catalog_has_sixty_plus_tagged(self) -> None:
        catalog = json.loads((ROOT / "memory/cover/meme-top100.json").read_text(encoding="utf-8"))
        usable = [e for e in catalog.get("entries") or [] if e.get("category") != "banned"]
        self.assertGreaterEqual(len(usable), 60)
        for entry in usable:
            self.assertTrue(entry.get("tags"), f"missing tags: {entry.get('id')}")

    def test_meme_rotate_doctor(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/excalibur_blog_meme_rotate.py"), "doctor"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)

    def test_lapoy_skips_burned_harold_and_roll_safe(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_meme_cat_gate import load_meme_catalog  # noqa: PLC0415
        from excalibur_blog_meme_rotate import pick_cover_meme  # noqa: PLC0415

        catalog = load_meme_catalog(ROOT)
        manifest = {
            "topic_id": "LIVE-lapoy",
            "slug": "razreshili-s-lapoy-doplatu-nazvali-posle-zaseleniya",
            "cover_hook": "После заселения — доплата 3000 за лапу",
            "cover_motifs": {
                "joke": "разрешили с лапой — после заселения назвали доплату",
                "prop_set": "лапа, доплата 3000, чек",
            },
            "slots": {
                "cover": {
                    "meme_id": "hide_the_pain_harold",
                    "sticky": "3000 ₽ за лапу?",
                }
            },
        }
        picked = pick_cover_meme(manifest, catalog, ROOT)
        self.assertNotIn(
            picked.get("id"),
            {"hide_the_pain_harold", "roll_safe"},
            picked,
        )
        self.assertIn("pets", picked.get("topic_tags") or [])

    def test_recent_window_skips_last_eight(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_meme_cat_gate import load_meme_catalog  # noqa: PLC0415
        from excalibur_blog_meme_rotate import pick_cover_meme, recent_used_ids, load_meme_used  # noqa: PLC0415

        used = load_meme_used(ROOT)
        recent = recent_used_ids(used, window=8)
        self.assertGreaterEqual(len(recent), 1)
        catalog = load_meme_catalog(ROOT)
        manifest = {
            "topic_id": "B99-new",
            "cover_hook": "Залог не вернули после уборки",
            "cover_motifs": {"joke": "сказали после уборки", "prop_set": "залог, уборка"},
        }
        picked = pick_cover_meme(manifest, catalog, ROOT)
        self.assertNotIn(str(picked.get("id") or "").casefold(), recent)

    def test_globally_excluded_never_picked(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_meme_cat_gate import load_meme_catalog  # noqa: PLC0415
        from excalibur_blog_meme_rotate import pick_cover_meme  # noqa: PLC0415

        catalog = load_meme_catalog(ROOT)
        manifest = {"topic_id": "B99", "cover_hook": "тест"}
        picked = pick_cover_meme(manifest, catalog, ROOT)
        self.assertNotIn(
            picked.get("id"),
            {"hide_the_pain_harold", "roll_safe"},
            picked,
        )

    def test_design_code_tender_light_locked(self) -> None:
        design = json.loads((ROOT / "memory/cover/cover-design-code.json").read_text(encoding="utf-8"))
        canon = design.get("tender_light_canon") or {}
        self.assertEqual(design.get("design_code_id"), "dobry_dom_tender_light_v1")
        self.assertIn("terracotta_matte_rgb", canon.get("palette") or {})
        forbidden = canon.get("forbidden_palette") or []
        self.assertIn("metallic gold", forbidden)
        self.assertIn("dark leather", forbidden)
        excluded = (canon.get("meme") or {}).get("globally_excluded_ids") or []
        self.assertIn("hide_the_pain_harold", excluded)


class WordstatSeedCanonTest(unittest.TestCase):
    def test_wordstat_geo_seeds_locked(self) -> None:
        geo = json.loads((ROOT / "memory/cover/wordstat-geo.json").read_text(encoding="utf-8"))
        head = {p["phrase"]: p["volume"] for p in geo["head_rf_seeds"]["phrases"]}
        self.assertEqual(head["квартира посуточно"], 1212722)
        self.assertEqual(head["снять квартиру посуточно"], 775383)
        tyumen = {p["phrase"]: p["volume"] for p in geo["tyumen_geo_seeds"]["phrases"]}
        self.assertEqual(tyumen["квартиры посуточно тюмень"], 12242)
        banned = [b["phrase"].casefold() for b in geo.get("banned_weak_clusters") or []]
        self.assertIn("посуточная аренда тюмень", banned)
        rules = geo.get("writer_title_schema_rules") or {}
        self.assertEqual(rules.get("geo_ai", {}).get("phone"), "+7 (993) 574-83-22")


if __name__ == "__main__":
    unittest.main()
