"""Cross-link QA gate tests."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CATALOG_SLUGS = [
    ("beskontaktnoe-zaselenie-posutochno-tyumen", "Бесконтактное заселение посуточно в Тюмени"),
    ("perevel-zalog-za-posutochnuyu", "Перевёл залог за посуточную"),
    ("chto-vhodit-v-stoimost", "Что входит в стоимость квартиры посуточно"),
    ("pravila-prozhivaniya", "Правила проживания в отеле"),
]

SITE_BASE = "{{SITE_BASE}}"


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

    def _three_link_html(self, *, absolute: bool = True) -> str:
        prefix = f"{SITE_BASE}" if absolute else ""
        return (
            "<p>Про "
            f'<a href="{prefix}/blog/beskontaktnoe-zaselenie-posutochno-tyumen/">бесконтактное заселение</a>, '
            f'<a href="{prefix}/blog/perevel-zalog-za-posutochnuyu/">залог при посуточной</a> и '
            f'<a href="{prefix}/blog/chto-vhodit-v-stoimost/">что входит в стоимость</a>.</p>\n'
        )

    def test_fail_on_invented_slug(self) -> None:
        (self.article_dir / "article.html").write_text(
            f'<p>См. <a href="{SITE_BASE}/blog/this-slug-does-not-exist-live/">бесконтактное заселение</a>.</p>\n',
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
            f'<p>Про <a href="{SITE_BASE}/blog/beskontaktnoe-zaselenie-posutochno-tyumen/">бесконтактное заселение</a>.</p>\n',
            encoding="utf-8",
        )
        proc = self._run_gate()
        self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "crosslink-qa-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any("xlink quota" in err for err in report["errors"]))
        self.assertGreaterEqual(report.get("outbound_required_min", 0), 3)

    def test_fail_on_root_relative_blog_hrefs(self) -> None:
        """Relative /blog/ must FAIL even when concatenated URL would HTTP 200 on-site."""
        (self.article_dir / "article.html").write_text(self._three_link_html(absolute=False), encoding="utf-8")
        proc = self._run_gate()
        self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "crosslink-qa-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(
            any("Dzen-unsafe root-relative" in err for err in report["errors"]),
            report["errors"],
        )

    def test_fail_on_root_relative_even_when_http_200(self) -> None:
        from excalibur_blog_crosslink_qa_gate import validate_article_crosslinks

        html = self._three_link_html(absolute=False)
        catalog = _build_catalog()
        tenant: dict = {}
        with patch(
            "excalibur_blog_crosslink_qa_gate.check_url_with_connection_reset_retry",
            return_value={"ok": True, "status": 200},
        ):
            report = validate_article_crosslinks(
                html,
                catalog=catalog,
                site_base="https://example.test",
                tenant=tenant,
                skip_http=False,
                current_slug="fixture-crosslink",
            )
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any("Dzen-unsafe root-relative" in err for err in report["errors"]))

    def test_pass_on_three_catalog_matching_hrefs(self) -> None:
        (self.article_dir / "article.html").write_text(self._three_link_html(absolute=True), encoding="utf-8")
        proc = self._run_gate()
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "crosslink-qa-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "PASS")
        self.assertGreaterEqual(len(report.get("outbound_unique_slugs") or []), 3)


if __name__ == "__main__":
    unittest.main()
