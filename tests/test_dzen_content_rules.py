"""Guard Dzen content rules wiring into style/gates."""
from __future__ import annotations

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


if __name__ == "__main__":
    unittest.main()
