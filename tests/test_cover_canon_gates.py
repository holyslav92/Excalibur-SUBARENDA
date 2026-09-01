"""Tests for cover motif anti-repeat and Wordstat gates."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SCOUT_HANDOFF_BASE = "\n".join(
    [
        "=== SCOUT ===",
        "klyshin_hook: deposit_return | original: «уборка залог» | angle: выезд",
        "wordstat_rework: probe «залог аренда» 120 → final «залог» 890",
        "wordstat_preflight: mcp-kv wordstat_get_user_info OK",
    ]
)


class CoverMotifGateTest(unittest.TestCase):
    def test_doctor_on_repo_log(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/excalibur_blog_cover_motif_gate.py"), "doctor"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)

    def test_collision_detected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "memory/cover").mkdir(parents=True)
            (root / "memory/cover/cover-canon.json").write_text("{}", encoding="utf-8")
            log = {
                "schema_version": 1,
                "window_days": 14,
                "entries": [
                    {
                        "date": "2026-08-28",
                        "topic_id": "B100",
                        "motifs": {"location": "лестничная клетка подъезда"},
                    }
                ],
            }
            (root / "memory/cover/used-motifs.json").write_text(
                json.dumps(log, ensure_ascii=False), encoding="utf-8"
            )
            env = {"EXCALIBUR_PROJECT_ROOT": str(root)}
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts/excalibur_blog_cover_motif_gate.py"),
                    "check",
                    "--topic-id",
                    "B101",
                    "--location",
                    "лестничная клетка подъезда",
                ],
                cwd=ROOT,
                env={**dict(**{k: v for k, v in __import__("os").environ.items()}), **env},
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 1, proc.stdout)
            self.assertIn("COLLISION", proc.stderr)


class WordstatGateTest(unittest.TestCase):
    def test_geo_doctor(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/excalibur_blog_wordstat_gate.py"), "doctor"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)

    def test_handoff_rejects_skip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            handoff = Path(tmp) / "handoff.md"
            handoff.write_text(
                SCOUT_HANDOFF_BASE + "\nwordstat: skip\n",
                encoding="utf-8",
            )
            env = {"EXCALIBUR_PROJECT_ROOT": str(tmp)}
            (Path(tmp) / "memory/cover").mkdir(parents=True)
            geo_src = ROOT / "memory/cover/wordstat-geo.json"
            (Path(tmp) / "memory/cover/wordstat-geo.json").write_text(
                geo_src.read_text(encoding="utf-8"), encoding="utf-8"
            )
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts/excalibur_blog_wordstat_gate.py"),
                    "handoff",
                    "--handoff",
                    str(handoff),
                ],
                cwd=ROOT,
                env={**dict(**{k: v for k, v in __import__("os").environ.items()}), **env},
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 1)
            self.assertIn("skip", proc.stderr.lower())

    def test_handoff_rejects_brand_vanity_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "memory/cover").mkdir(parents=True)
            geo_src = ROOT / "memory/cover/wordstat-geo.json"
            (root / "memory/cover/wordstat-geo.json").write_text(
                geo_src.read_text(encoding="utf-8"), encoding="utf-8"
            )
            handoff = root / "handoff.md"
            handoff.write_text(
                SCOUT_HANDOFF_BASE + "\n"
                + "wordstat: mcp_kv live | regions 55,11176 | «добрый дом тюмень» 47\n",
                encoding="utf-8",
            )
            env = {"EXCALIBUR_PROJECT_ROOT": str(root)}
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts/excalibur_blog_wordstat_gate.py"),
                    "handoff",
                    "--handoff",
                    str(handoff),
                ],
                cwd=ROOT,
                env={**dict(**{k: v for k, v in __import__("os").environ.items()}), **env},
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 1)
            self.assertIn("buyer", proc.stderr.lower())

    def test_handoff_accepts_mcp_kv_buyer_p0(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "memory/cover").mkdir(parents=True)
            geo_src = ROOT / "memory/cover/wordstat-geo.json"
            (root / "memory/cover/wordstat-geo.json").write_text(
                geo_src.read_text(encoding="utf-8"), encoding="utf-8"
            )
            handoff = root / "handoff.md"
            handoff.write_text(
                SCOUT_HANDOFF_BASE + "\n"
                + "wordstat: mcp_kv live | regions 55,11176 vs RU 225 | P0 «квартиры посуточно тюмень» 2306\n",
                encoding="utf-8",
            )
            env = {"EXCALIBUR_PROJECT_ROOT": str(root)}
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts/excalibur_blog_wordstat_gate.py"),
                    "handoff",
                    "--handoff",
                    str(handoff),
                ],
                cwd=ROOT,
                env={**dict(**{k: v for k, v in __import__("os").environ.items()}), **env},
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_scout_skill_hard_gate(self) -> None:
        s = (ROOT / "skills/scout-excalibur-blog/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("HARD GATE", s)
        self.assertIn("MCP-KV", s)
        self.assertIn("wordstat_get_user_info", s)
        self.assertIn("добрый дом", s.lower())
        self.assertNotIn("mcp-yandex-wordstat", s.lower())

    def test_cover_canon_rejects_daypart(self) -> None:
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        self.assertTrue(canon["forbidden_daypart_formula"]["never_use"])

    def test_wow_cover_rules_locked_in_tenant(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        wow = tenant.get("cover_wow_rules") or {}
        self.assertEqual(wow.get("cover_qa_mode"), "slim")
        self.assertEqual(wow.get("canon_id"), "dobry_dom_scene_composite_v1")
        self.assertEqual(wow.get("cover_generation_mode"), "scene_only_16_9")
        self.assertEqual(wow.get("logo_mode"), "brand_logo_paste")
        self.assertTrue(wow.get("forbid_logo_reference_in_generation"))
        self.assertTrue(wow.get("cover_phone_factory_post_composite"))
        self.assertFalse(wow.get("cover_phone_large_sticker_generation"))
        self.assertTrue(wow.get("require_cover_meme_sticker"))
        self.assertTrue(wow.get("vip_disabled"))
        self.assertEqual(wow.get("max_generation_attempts_per_canvas"), 2)
        self.assertTrue(wow.get("paste_and_ship_on_exhaust"))
        self.assertTrue(wow.get("forbid_wordpress_ui_in_art"))
        self.assertEqual(wow.get("inline_logo_count_min"), 0)
        self.assertEqual(wow.get("inline_logo_count_max"), 0)
        self.assertIn("Excalibur-SUBARENDA", wow.get("tenant_scope", ""))
        self.assertEqual(tenant.get("cover_mode"), "brand_logo_paste")
        img = tenant.get("image_generation") or {}
        self.assertTrue(img.get("logo_never_as_generation_reference"))
        self.assertTrue(wow.get("cover_phone_factory_post_composite"))

    def test_visual_notes_dobry_dom(self) -> None:
        notes = json.loads(
            (ROOT / "memory/cover/visual-notes-dobry-dom.json").read_text(encoding="utf-8")
        )
        brand = notes.get("brand_lock") or {}
        self.assertTrue(brand.get("forbid_ai_drawn_lockup"))
        self.assertTrue(brand.get("forbid_logo_plate"))
        self.assertEqual(notes.get("generation_policy", {}).get("max_attempts_per_canvas"), 2)

    def test_cover_qa_gate_slim_checks(self) -> None:
        gate_src = (ROOT / "scripts/excalibur_blog_cover_qa_gate.py").read_text(encoding="utf-8")
        for key in (
            "forbid_wordpress_ui_in_art",
            "forbid_ai_drawn_logo_cover",
            "logo_composite_stamp_pass",
            "no_logo_plate_cover",
            "inline_no_logo_on_inlines",
            "cover_phone_993_large_sticker",
            "forbid_phone_pill_post_composite",
            "forbid_logo_overlaps_headline_phone",
            "validate_cover_phone_and_overlap_gates",
            "validate_cover_type_meme_sticker_gates",
            "forbid_split_white_collage",
            "forbid_overlapping_text_blocks",
            "poster_composite_stamp_pass",
        ):
            self.assertIn(key, gate_src)
        for removed in (
            "wow_poster_magazine_typography",
            "official_logo_pixels_only",
            "august_no_winter_hero",
            "inline_utility_all_7",
        ):
            self.assertNotIn(removed, gate_src)

    def test_quad_prompt_bans_wordpress_ui(self) -> None:
        prompt_src = (ROOT / "scripts/excalibur_blog_cover_quad_prompt.py").read_text(encoding="utf-8")
        self.assertIn("WOW_POSTER_BAN", prompt_src)
        self.assertIn("WordPress", prompt_src)
        self.assertIn("CAT_MEME_QUOTA_RULE", prompt_src)

    def test_cover_canon_tender_light_v1(self) -> None:
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        self.assertEqual(canon["canon_id"], "dobry_dom_scene_composite_v1")
        phone = canon["wow_cover_rules"]["no_element_overlap"]["cover_phone"]
        self.assertEqual(phone.get("mode"), "kitchen_tablo_factory_drawn")
        self.assertTrue(phone.get("factory_post_composite"))
        meme = canon.get("meme_system") or {}
        self.assertIn("REQUIRED", str(meme.get("cover", "")))

    def test_meme_top100_cat_quota(self) -> None:
        catalog = json.loads((ROOT / "memory/cover/meme-top100.json").read_text(encoding="utf-8"))
        quota = (catalog.get("usage_rules") or {}).get("cat_meme_quota") or {}
        self.assertEqual(quota.get("max_slots_per_article"), 1)

    def test_meme_cat_gate_detects_two_cats(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_meme_cat_gate import (  # noqa: PLC0415
            load_meme_catalog,
            validate_max_one_cat_meme,
        )

        catalog = load_meme_catalog(ROOT)
        manifest = {
            "cover_motifs": {"meme": "tiny cat sticker bottom-left"},
            "slots": {
                "cover": {"scene_hint": "poster"},
                "inline_7": {"scene_hint": "small cat sticker bottom-left only"},
            },
        }
        errors = validate_max_one_cat_meme(manifest, catalog)
        self.assertTrue(errors)
        self.assertIn("cat-meme quota exceeded", errors[0])

    def test_meme_cat_gate_allows_one_cat(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_meme_cat_gate import (  # noqa: PLC0415
            load_meme_catalog,
            validate_max_one_cat_meme,
        )

        catalog = load_meme_catalog(ROOT)
        manifest = {
            "cover_motifs": {"meme": "tiny cat sticker bottom-left"},
            "slots": {
                "cover": {"scene_hint": "poster"},
                "inline_7": {"scene_hint": "checklist board", "meme_sticker": True},
            },
        }
        errors = validate_max_one_cat_meme(manifest, catalog)
        self.assertEqual(errors, [])

    def test_motif_gate_cat_family_collision(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "memory/cover").mkdir(parents=True)
            (root / "memory/cover/cover-canon.json").write_text("{}", encoding="utf-8")
            catalog_src = ROOT / "memory/cover/meme-top100.json"
            (root / "memory/cover/meme-top100.json").write_text(
                catalog_src.read_text(encoding="utf-8"), encoding="utf-8"
            )
            log = {
                "schema_version": 1,
                "window_days": 14,
                "entries": [
                    {
                        "date": "2026-08-28",
                        "topic_id": "B100",
                        "motifs": {"meme": "grumpy cat sticker"},
                    }
                ],
            }
            (root / "memory/cover/used-motifs.json").write_text(
                json.dumps(log, ensure_ascii=False), encoding="utf-8"
            )
            env = {"EXCALIBUR_PROJECT_ROOT": str(root)}
            proc = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts/excalibur_blog_cover_motif_gate.py"),
                    "check",
                    "--topic-id",
                    "B101",
                    "--meme",
                    "smudge cat bottom-left",
                ],
                cwd=ROOT,
                env={**dict(**{k: v for k, v in __import__("os").environ.items()}), **env},
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 1, proc.stdout)
            self.assertIn("COLLISION", proc.stderr)

    def test_cover_qa_gate_requires_cat_quota_check(self) -> None:
        gate_src = (ROOT / "scripts/excalibur_blog_cover_qa_gate.py").read_text(encoding="utf-8")
        self.assertIn("max_one_cat_meme_slot", gate_src)
        self.assertIn("validate_max_one_cat_meme", gate_src)

    def test_canvas_contract_dobry_dom_not_rieltor(self) -> None:
        contract = (ROOT / "shared/blog-cover-quad-canvas-contract.md").read_text(encoding="utf-8")
        self.assertIn("Добрый дом", contract)
        self.assertIn("Brand lock", contract)
        self.assertNotIn("The Риэлтор / tymenrieltor.ru", contract.split("NEVER")[0])


if __name__ == "__main__":
    unittest.main()
