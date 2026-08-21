"""Cross-link QA gate tests."""
from __future__ import annotations

import json
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CrosslinkQaGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.article_dir = ROOT / "memory/blog/articles/_gate_fixture_crosslink_qa"
        if self.article_dir.exists():
            shutil.rmtree(self.article_dir)
        self.article_dir.mkdir(parents=True)
        (self.article_dir / "article.meta.json").write_text(
            json.dumps(
                {
                    "slug": "fixture-crosslink",
                    "topic_id": "B99",
                    "title": "Fixture crosslink",
                    "theme_blocks": {"faq": "skip", "quiz": "skip", "side_stickers": "skip"},
                },
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )
        catalog = {
            "posts": [
                {
                    "slug": "beskontaktnoe-zaselenie-posutochno-tyumen",
                    "title": "Бесконтактное заселение посуточно в Тюмени",
                    "href": "/blog/beskontaktnoe-zaselenie-posutochno-tyumen/",
                }
            ],
            "slug_index": {
                "beskontaktnoe-zaselenie-posutochno-tyumen": {
                    "slug": "beskontaktnoe-zaselenie-posutochno-tyumen",
                    "title": "Бесконтактное заселение посуточно в Тюмени",
                    "href": "/blog/beskontaktnoe-zaselenie-posutochno-tyumen/",
                }
            },
        }
        (ROOT / "memory/live-catalog.json").write_text(
            json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.article_dir, ignore_errors=True)

    def _run_gate(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                "python3",
                str(ROOT / "scripts/excalibur_blog_crosslink_qa_gate.py"),
                "--article-dir",
                str(self.article_dir.relative_to(ROOT)),
                "--use-cache",
                "--skip-http",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_fail_on_invented_slug(self) -> None:
        (self.article_dir / "article.html").write_text(
            '<p>См. <a href="/blog/this-slug-does-not-exist-live/">бесконтактное заселение</a>.</p>\n',
            encoding="utf-8",
        )
        proc = self._run_gate()
        self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "crosslink-qa-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any("invented" in err or "not in live catalog" in err for err in report["errors"]))

    def test_fail_on_mashed_plain_text(self) -> None:
        (self.article_dir / "article.html").write_text(
            "<p>В материале пробесконтактное заселение без ссылки.</p>\n",
            encoding="utf-8",
        )
        proc = self._run_gate()
        self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "crosslink-qa-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any("пробесконтакт" in err for err in report["errors"]))

    def test_pass_on_catalog_matching_href(self) -> None:
        (self.article_dir / "article.html").write_text(
            '<p>Про <a href="/blog/beskontaktnoe-zaselenie-posutochno-tyumen/">бесконтактное заселение</a>.</p>\n',
            encoding="utf-8",
        )
        proc = self._run_gate()
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "crosslink-qa-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
