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
                        "date": "2026-08-17",
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
        self.assertTrue(wow.get("forbid_wordpress_ui_in_art"))
        self.assertTrue(wow.get("no_element_overlap"))
        self.assertTrue(wow.get("wow_poster_magazine_typography"))
        self.assertEqual(wow.get("inline_logo_count_min"), 2)
        self.assertEqual(wow.get("inline_logo_count_max"), 3)
        self.assertIn("Excalibur-SUBARENDA", wow.get("tenant_scope", ""))

    def test_visual_notes_dobry_dom(self) -> None:
        notes = json.loads(
            (ROOT / "memory/cover/visual-notes-dobry-dom.json").read_text(encoding="utf-8")
        )
        rules = notes.get("wow_cover_rules") or {}
        self.assertTrue(rules.get("forbid_wordpress_ui_in_art", {}).get("required"))
        self.assertTrue(rules.get("no_element_overlap", {}).get("required"))
        self.assertTrue(rules.get("wow_poster", {}).get("required"))

    def test_cover_qa_gate_requires_wow_checks(self) -> None:
        gate_src = (ROOT / "scripts/excalibur_blog_cover_qa_gate.py").read_text(encoding="utf-8")
        for key in (
            "forbid_wordpress_ui_in_art",
            "no_element_overlap",
            "wow_poster_magazine_typography",
        ):
            self.assertIn(key, gate_src)

    def test_quad_prompt_bans_wordpress_ui(self) -> None:
        prompt_src = (ROOT / "scripts/excalibur_blog_cover_quad_prompt.py").read_text(encoding="utf-8")
        self.assertIn("WOW_POSTER_BAN", prompt_src)
        self.assertIn("WordPress", prompt_src)

    def test_canvas_contract_dobry_dom_not_rieltor(self) -> None:
        contract = (ROOT / "shared/blog-cover-quad-canvas-contract.md").read_text(encoding="utf-8")
        self.assertIn("Добрый дом", contract)
        self.assertIn("WOW cover rules", contract)
        self.assertNotIn("The Риэлтор / tymenrieltor.ru", contract.split("NEVER")[0])


if __name__ == "__main__":
    unittest.main()
