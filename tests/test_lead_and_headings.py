"""Guard Writer meaning draft + Sol final (no second-author rewrite beyond Sol)."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GONE = (
    "skills/excalibur-geo-qa/SKILL.md",
    "skills/article-editor-excalibur-blog/SKILL.md",
    "skills/lead-excalibur-blog/SKILL.md",
    "skills/hook-excalibur-blog/SKILL.md",
    "agents/excalibur-blog-geo-qa.md",
    "agents/excalibur-blog-article-editor.md",
    "agents/excalibur-blog-lead.md",
    "agents/excalibur-blog-hook.md",
)


class WriterFinalTest(unittest.TestCase):
    def test_master_prompt_forbids_term_dump_opening(self) -> None:
        p = (ROOT / "shared/writer-master-prompt.md").read_text(encoding="utf-8")
        low = p.lower()
        self.assertIn("термин-дамп", low)
        self.assertIn("открытие", low)
        self.assertIn("drafts/writer.html", p)
        self.assertIn("Sol", p)

    def test_removed_skills_and_agents_absent(self) -> None:
        for rel in GONE:
            self.assertFalse((ROOT / rel).exists(), rel)

    def test_writer_hands_off_to_sol(self) -> None:
        a = (ROOT / "agents/excalibur-blog-writer.md").read_text(encoding="utf-8")
        self.assertIn("article.html", a)
        self.assertTrue("SOUL" in a or "слог" in a.lower() or "Sol" in a)
        self.assertIn("drafts/writer.html", a)

    def test_research_notes_not_prose_template(self) -> None:
        r = (ROOT / "skills/excalibur-research/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("не пиши готовые h2", r.lower())


if __name__ == "__main__":
    unittest.main()
