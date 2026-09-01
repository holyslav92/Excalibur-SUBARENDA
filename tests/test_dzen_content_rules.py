"""Guard Dzen content rules wiring into style/gates."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DzenContentRulesTest(unittest.TestCase):
    def test_dzen_rules_file_present(self) -> None:
        text = (ROOT / "shared/dzen-content-rules.md").read_text(encoding="utf-8")
        low = text.lower()
        self.assertIn("ненормативн", low)
        self.assertIn("кликбейт", low)
        self.assertIn("комментар", low)
        self.assertIn("dzen.ru/help", low)

    def test_article_style_bans_mat_for_dzen(self) -> None:
        style = (ROOT / "shared/article-style.md").read_text(encoding="utf-8")
        self.assertIn("dzen-content-rules.md", style)
        self.assertIn("мат запрещён", style.lower())

    def test_dzen_rules_applied_to_writer_pipeline(self) -> None:
        text = (ROOT / "shared/dzen-content-rules.md").read_text(encoding="utf-8")
        self.assertIn("Title / Writer", text)
        self.assertNotIn("GEO QA", text)

    def test_doctor_requires_dzen_rules(self) -> None:
        doc = (ROOT / "scripts/excalibur_blog_doctor.py").read_text(encoding="utf-8")
        self.assertIn("shared/dzen-content-rules.md", doc)

    def test_dzen_feed_patterns_in_style_and_soul(self) -> None:
        style = (ROOT / "shared/article-style.md").read_text(encoding="utf-8").lower()
        soul = (ROOT / "shared/SOUL.md").read_text(encoding="utf-8").lower()
        scout = (ROOT / "skills/scout-excalibur-blog/SKILL.md").read_text(encoding="utf-8").lower()
        title = (ROOT / "skills/title-excalibur-blog/SKILL.md").read_text(encoding="utf-8").lower()
        writer = (ROOT / "skills/writer-excalibur-blog/SKILL.md").read_text(encoding="utf-8").lower()
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))

        for blob in (style, soul):
            self.assertIn("5 вопросов", blob)
            self.assertIn("залог 5 000", blob)
            self.assertIn("посуточно или отель", blob)

        for blob in (scout, title, writer):
            self.assertTrue("dzen_pattern" in blob or "dzen pattern" in blob)

        self.assertIn("поверхность дистрибуции", style)
        self.assertIn("tg/max", style)
        self.assertIn("writing_patterns_ref", tenant["dzen_publish"])
        self.assertEqual(len(tenant["dzen_publish"]["patterns"]), 5)
        self.assertGreaterEqual(len(tenant["dzen_publish"]["headline_shapes_example"]), 3)


if __name__ == "__main__":
    unittest.main()
