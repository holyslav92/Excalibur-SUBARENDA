"""Cross-link QA gate tests."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_crosslink_qa_gate import (  # noqa: E402
    anchor_matches_catalog_title,
    extract_article_links,
)

CATALOG_SLUGS = [
    ("beskontaktnoe-zaselenie-posutochno-tyumen", "Бесконтактное заселение посуточно в Тюмени"),
    ("perevel-zalog-za-posutochnuyu", "Перевёл залог за посуточную"),
    ("chto-vhodit-v-stoimost", "Что входит в стоимость квартиры посуточно"),
    ("pravila-prozhivaniya", "Правила проживания в отеле"),
]


def _build_catalog() -> dict:
    posts = []
    slug_index = {}
    for slug, title in CATALOG_SLUGS:
        href = f"/blog/{slug}/"
        row = {"slug": slug, "title": title, "href": href}
        posts.append(row)
        slug_index[slug] = dict(row)
    return {"posts": posts, "slug_index": slug_index}


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
        self._catalog_backup = None
        catalog_path = ROOT / "memory/live-catalog.json"
        if catalog_path.is_file():
            self._catalog_backup = catalog_path.read_text(encoding="utf-8")
        catalog_path.write_text(
            json.dumps(_build_catalog(), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        shutil.rmtree(self.article_dir, ignore_errors=True)
        catalog_path = ROOT / "memory/live-catalog.json"
        if self._catalog_backup is not None:
            catalog_path.write_text(self._catalog_backup, encoding="utf-8")
        elif catalog_path.is_file():
            catalog_path.unlink()

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

    def _three_link_html(self) -> str:
        return (
            "<p>Про "
            '<a href="/blog/beskontaktnoe-zaselenie-posutochno-tyumen/">бесконтактное заселение</a>, '
            '<a href="/blog/perevel-zalog-za-posutochnuyu/">залог при посуточной</a> и '
            '<a href="/blog/chto-vhodit-v-stoimost/">что входит в стоимость</a>.</p>\n'
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

    def test_fail_when_only_one_xlink(self) -> None:
        (self.article_dir / "article.html").write_text(
            '<p>Про <a href="/blog/beskontaktnoe-zaselenie-posutochno-tyumen/">бесконтактное заселение</a>.</p>\n',
            encoding="utf-8",
        )
        proc = self._run_gate()
        self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "crosslink-qa-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any("xlink quota" in err for err in report["errors"]))
        self.assertGreaterEqual(report.get("outbound_required_min", 0), 3)

    def test_pass_on_three_catalog_matching_hrefs(self) -> None:
        (self.article_dir / "article.html").write_text(self._three_link_html(), encoding="utf-8")
        proc = self._run_gate()
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "crosslink-qa-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "PASS")
        self.assertGreaterEqual(len(report.get("outbound_unique_slugs") or []), 3)

    def test_extract_anchor_only_inside_a_tag(self) -> None:
        """Regression B04: prose before/after <a> must not pollute anchor for title match."""
        html = (
            "<p>Про залог см. "
            '<a href="/blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/">'
            "«Снял квартиру посуточно. Залог не вернули — нашли скол на плите»"
            "</a> и дальше текст.</p>\n"
        )
        links = extract_article_links(html)
        self.assertEqual(len(links), 1)
        anchor = links[0]["anchor"]
        self.assertIn("Залог не вернули", anchor)
        self.assertNotIn("Про залог", anchor)
        self.assertNotIn("дальше текст", anchor)
        catalog_title = "Снял квартиру посуточно. Залог не вернули — нашли скол на плите"
        self.assertTrue(anchor_matches_catalog_title(anchor, catalog_title))


if __name__ == "__main__":
    unittest.main()
