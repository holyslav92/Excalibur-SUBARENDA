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

    def test_cover_canon_logo_lockup_mode(self) -> None:
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        self.assertTrue(canon["logo_lockup"]["required"])
        self.assertEqual(canon["identity_lock"]["status"], "DISABLED")
        logo_path = ROOT / canon["logo_lockup"]["asset"]
        self.assertTrue(logo_path.is_file(), str(logo_path))

    def test_cover_qa_doctor_logo_lockup(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/excalibur_blog_cover_qa_gate.py"), "--doctor"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)
        self.assertIn("logo lockup", proc.stdout.lower())

    def test_identity_real_check_logo_mode(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/excalibur_blog_identity_real.py"), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)
        self.assertIn("logo lockup", proc.stdout.lower())


if __name__ == "__main__":
    unittest.main()
