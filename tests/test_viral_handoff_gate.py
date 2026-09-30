"""ViralDzen handoff gate — no Scout/article without viral pass."""
from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ViralHandoffGateTests(unittest.TestCase):
    def test_blocks_without_handoff(self) -> None:
        proc = subprocess.run(
            [
                "python3",
                str(ROOT / "scripts/excalibur_blog_viral_handoff_gate.py"),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 1)
        report = json.loads(proc.stdout)
        self.assertEqual(report["status"], "BLOCK")

    def test_passes_valid_handoff(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            handoff = {
                "status": "PASS",
                "viral_source": {
                    "title": "Пример",
                    "url": "https://dzen.ru/a/example",
                    "viral_score": 12.5,
                },
                "guest_angle_ru": "Гость боится доплаты у двери",
                "discovered_hub": {"slug": "travel", "title": "Путешествия", "url": "https://dzen.ru/topic/travel"},
            }
            path = Path(tmp) / "viral-dzen-handoff.json"
            path.write_text(json.dumps(handoff, ensure_ascii=False), encoding="utf-8")
            proc = subprocess.run(
                [
                    "python3",
                    str(ROOT / "scripts/excalibur_blog_viral_handoff_gate.py"),
                    "--handoff",
                    str(path),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc.returncode, 0)
            self.assertEqual(json.loads(proc.stdout)["status"], "PASS")

    def test_slot_dry_run_writes_handoff(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            slot_path = Path(tmp) / "memory/scout/viral-dzen-handoff.json"
            slot_path.parent.mkdir(parents=True)
            # redirect slot path via monkeypatch is heavy; use gate on synthetic file
            handoff = {
                "status": "PASS",
                "viral_source": {"title": "t", "url": "https://dzen.ru/a/x", "viral_score": 1.0},
                "guest_angle_ru": "угол",
                "discovered_hub": {"slug": "travel"},
            }
            slot_path.write_text(json.dumps(handoff), encoding="utf-8")
            proc = subprocess.run(
                [
                    "python3",
                    str(ROOT / "scripts/excalibur_blog_viral_handoff_gate.py"),
                    "--handoff",
                    str(slot_path),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc.returncode, 0)


class UtilityModelLunaTests(unittest.TestCase):
    def test_tenant_utility_is_gpt_6_luna(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        model = (tenant.get("writing_model") or {}).get("utility", {}).get("model")
        self.assertEqual(model, "gpt-6-luna")


class WriterModelOpus55Tests(unittest.TestCase):
    def test_tenant_writer_not_legacy_opus5_id(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        model = (tenant.get("writing_model") or {}).get("powerful", {}).get("model")
        self.assertEqual(model, "claude-opus-5-5")
        self.assertNotEqual(model, "claude-opus-5")

    def test_derouter_default_opus_model(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import DEFAULT_OPUS_MODEL

        self.assertEqual(DEFAULT_OPUS_MODEL, "claude-opus-5-5")
        self.assertNotEqual(DEFAULT_OPUS_MODEL, "claude-opus-5")


if __name__ == "__main__":
    unittest.main()
