"""WP categories + interlink gate tests."""
from __future__ import annotations

import json
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class WpCategoriesInterlinkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.article_dir = ROOT / "memory/blog/articles/_gate_fixture_categories_interlink"
        if self.article_dir.exists():
            shutil.rmtree(self.article_dir)
        self.article_dir.mkdir(parents=True)
        (self.article_dir / "article.meta.json").write_text(
            json.dumps(
                {
                    "slug": "fixture-slug",
                    "topic_id": "B02",
                    "title": "Fixture",
                    "theme_blocks": {"faq": "skip", "quiz": "skip", "side_stickers": "skip"},
                },
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.article_dir, ignore_errors=True)

    def test_wp_categories_resolve_b02_defaults(self) -> None:
        proc = subprocess.run(
            [
                "python3",
                str(ROOT / "scripts/excalibur_blog_wp_categories.py"),
                "--article-dir",
                str(self.article_dir.relative_to(ROOT)),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "wp-categories-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "PASS")
        self.assertIn(101, report["category_ids"])
        self.assertIn("posutochnaya-arenda", report["category_slugs"])

    def test_interlink_gate_pass_with_outbound(self) -> None:
        (self.article_dir / "article.html").write_text(
            '<p>См. <a href="/blog/vtorichka-i-riski/rosfinmonitoring-sdelka-nedvizhimost-cheklis-tyumen-2026/">чеклист</a>.</p>\n',
            encoding="utf-8",
        )
        proc = subprocess.run(
            [
                "python3",
                str(ROOT / "scripts/excalibur_blog_interlinker.py"),
                "--article-dir",
                str(self.article_dir.relative_to(ROOT)),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "interlink-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "PASS")
        self.assertGreaterEqual(len(report["outbound_found"]), 1)

    def test_ledger_upsert_dedupes_legacy_row(self) -> None:
        import sys

        sys.path.insert(0, str(ROOT / "scripts"))
        from excalibur_blog_wp_publish import upsert_publish_ledger

        ledger_path = ROOT / "shared/published-articles.md"
        backup = ledger_path.read_text(encoding="utf-8")
        try:
            ledger_path.write_text(
                "# ledger\n\n"
                "| topic_id | slug | status | url |\n"
                "|----------|------|--------|-----|\n"
                "| B02 | old-slug | published | /blog/bez-rubriki/old-slug/ |\n",
                encoding="utf-8",
            )
            upsert_publish_ledger(
                ROOT,
                {"topic_id": "B02", "slug": "new-slug"},
                "https://example.com/blog/vtorichka-i-riski/new-slug/",
            )
            text = ledger_path.read_text(encoding="utf-8")
            self.assertEqual(text.count("B02"), 1)
            self.assertIn("/blog/vtorichka-i-riski/new-slug/", text)
            self.assertNotIn("bez-rubriki", text)
        finally:
            ledger_path.write_text(backup, encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
