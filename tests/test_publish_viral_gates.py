"""Publish path must block without ViralDzen handoff (B40-class Klyshin-only slots)."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublishViralGateTests(unittest.TestCase):
    def test_publish_prerequisites_block_without_viral_handoff(self) -> None:
        from scripts.excalibur_blog_wp_publish import check_publish_prerequisites

        article = ROOT / "memory/blog/articles/B34-bez-zaloga-v-filtre-zalog-u-dveri"
        if not article.is_dir():
            self.skipTest("fixture article dir missing")
        blockers = check_publish_prerequisites(
            article,
            require_scorecard_gate=False,
            require_freshness_gate=False,
            require_swarm_gates=False,
        )
        viral_block = [b for b in blockers if "viral" in b.lower()]
        self.assertTrue(
            viral_block,
            f"expected viral blocker without handoff; got {blockers[:8]}",
        )

    def test_b33_angle_blocked_by_repeat_gate(self) -> None:
        from excalibur_blog_viral_topic_repeat import check_topic_repeat

        probe = (
            "Гость оплатил бронь на Авито. В чате просят второй перевод предоплаты на карту. "
            "Тюмень посуточно."
        )
        errors = check_topic_repeat(ROOT, probe)
        self.assertTrue(errors, errors)

    def test_b45_rules_angle_passes_door_bags_combo_fails(self) -> None:
        from excalibur_blog_viral_topic_repeat import check_topic_repeat

        ad = ROOT / "memory/blog/articles/B45-posutochno-pravila-posle-perevoda-shtraf-za-musor-na-vyezde"
        if not (ad / "viral-dzen-handoff.json").is_file():
            self.skipTest("B45 fixture missing")
        from excalibur_blog_viral_topic_repeat import probe_text_from_article_dir

        probe_ok = probe_text_from_article_dir(ROOT, ad)
        self.assertFalse(
            check_topic_repeat(ROOT, probe_ok, article_dir=ad),
            "B45 post-fix handoff+title+opening should PASS repeat gate",
        )
        bad = "У двери гость с чемоданами и пакетами — доплата 3800 за мусор на выезде"
        self.assertTrue(
            check_topic_repeat(ROOT, bad),
            "door_beat+bags combo should FAIL when saturated in last 12 live",
        )

    def test_handoff_publish_binding_requires_meta(self) -> None:
        from scripts.excalibur_blog_viral_handoff_gate import check_handoff_for_publish

        with tempfile.TemporaryDirectory() as tmp:
            ad = Path(tmp) / "art"
            ad.mkdir()
            handoff = {
                "status": "PASS",
                "handoff_id": "test-id",
                "issued_at": "2026-10-01T03:00:00+00:00",
                "viral_source": {"title": "t", "url": "https://dzen.ru/a/x", "viral_score": 1.0},
                "guest_angle_ru": "угол",
                "discovered_hub": {"slug": "travel"},
            }
            (ad / "viral-dzen-handoff.json").write_text(json.dumps(handoff), encoding="utf-8")
            (ad / "article.meta.json").write_text("{}", encoding="utf-8")
            errors = check_handoff_for_publish(ROOT, ad)
            self.assertTrue(any("mismatch" in e for e in errors))


class AutomationYamlTests(unittest.TestCase):
    def test_dobry_dom_automation_yaml_parses(self) -> None:
        try:
            import yaml
        except ImportError:
            self.skipTest("PyYAML not installed")
        path = ROOT / ".cursor/automations/dobry-dom-3x.yml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        instructions = str(data.get("instructions") or "")
        self.assertIn("ViralDzen", instructions)
        self.assertTrue(instructions.strip().lower().startswith("step 0"))


if __name__ == "__main__":
    unittest.main()
