"""memory/topics/ must stay deleted; research_start uses --title."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class NoTopicsPoolTest(unittest.TestCase):
    def test_topics_dir_absent(self) -> None:
        self.assertFalse((ROOT / "memory/topics").exists())

    def test_purge_script_removes_resurrected_dir(self) -> None:
        from excalibur_blog_slim_blog_topics import purge_topics_dir

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            topics = root / "memory" / "topics"
            topics.mkdir(parents=True)
            (topics / "blog-topics.md").write_text(
                "## B999 — junk\n- **priority:** P0\n",
                encoding="utf-8",
            )
            stats = purge_topics_dir(root)
            self.assertEqual(stats["removed"], 1)
            self.assertFalse(topics.exists())

    def test_research_start_title_override(self) -> None:
        from excalibur_blog_research_start import parse_topic_card

        topic = parse_topic_card("B999", title_override="Make agent MCP для бизнеса")
        self.assertEqual(topic["topic_id"], "B999")
        self.assertEqual(topic["title"], "Make agent MCP для бизнеса")
        self.assertTrue(topic["slug"])

    def test_research_start_requires_title_without_topics_pool(self) -> None:
        from excalibur_blog_research_start import parse_topic_card

        with self.assertRaises(ValueError) as ctx:
            parse_topic_card("B03")
        self.assertIn("--title", str(ctx.exception))

    def test_memory_junk_removed(self) -> None:
        self.assertFalse((ROOT / "memory/topics").exists())
        self.assertFalse((ROOT / "memory/brief/maya-pro-deep-research.md").exists())
        self.assertFalse((ROOT / "memory/brief/editorial-policy.json").exists())
        self.assertFalse((ROOT / "memory/writer-critic-feedback.json").exists())
        self.assertFalse((ROOT / "memory/content-experiments.json").exists())
        self.assertTrue((ROOT / "memory/brief/site-brief.md").is_file())


if __name__ == "__main__":
    unittest.main()
