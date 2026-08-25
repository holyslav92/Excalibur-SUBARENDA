"""Single end-of-article full-funnel CTA gate tests."""
from __future__ import annotations

import json
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FUNNEL_BLOCK = (
    "<p>Если нужна квартира без сюрприза — подпишитесь на канал "
    '<a href="https://t.me/Dobriy_dom_72">Telegram</a>, '
    'напишите в <a href="https://max.ru/id660300569233_biz">MAX</a> '
    "или на сайте "
    '<a href="https://добрыйдом-72.рф/">добрыйдом-72.рф</a> '
    '<a href="https://добрыйдом-72.рф/booking/">бронь</a> — '
    'менеджер <a href="https://t.me/Dobriy_dom_Tyumen">@Dobriy_dom_Tyumen</a>, '
    'тел. <a href="tel:+79935748322">+7 (993) 574-83-22</a>.</p>\n'
)


class SingleFunnelGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.article_dir = ROOT / "memory/blog/articles/_gate_fixture_single_funnel"
        if self.article_dir.exists():
            shutil.rmtree(self.article_dir)
        self.article_dir.mkdir(parents=True)

    def tearDown(self) -> None:
        shutil.rmtree(self.article_dir, ignore_errors=True)

    def _run_gate(self, html: str) -> subprocess.CompletedProcess[str]:
        (self.article_dir / "article.html").write_text(html, encoding="utf-8")
        return subprocess.run(
            [
                "python3",
                str(ROOT / "scripts/excalibur_blog_community_cta_gate.py"),
                "--article-dir",
                str(self.article_dir.relative_to(ROOT)),
                "--root",
                str(ROOT),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_fail_no_funnel_at_end(self) -> None:
        opening = "<p>" + "Сцена заселения. " * 40 + "</p>\n"
        proc = self._run_gate(opening)
        self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "community-cta-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(
            any("end block missing" in err for err in report.get("funnel_errors") or report["errors"])
        )

    def test_fail_mid_article_funnel(self) -> None:
        opening = "<p>" + "Сцена заселения у двери. " * 30 + "</p>\n"
        middle = "<p>" + "Вердикт и moral. " * 20 + "</p>\n"
        end = "<p>" + "Финал после пользы. " * 15 + "</p>\n"
        proc = self._run_gate(opening + middle + FUNNEL_BLOCK + end + FUNNEL_BLOCK)
        self.assertNotEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "community-cta-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(
            any(
                "multiple full CTA" in err or "one block at end" in err
                for err in report.get("funnel_errors") or report["errors"]
            )
        )

    def test_pass_single_funnel_at_end(self) -> None:
        opening = "<p>" + "Сцена заселения у двери. " * 30 + "</p>\n"
        middle = "<p>" + "Вердикт и moral. " * 20 + "</p>\n"
        end = "<p>" + "Финал после пользы. " * 15 + "</p>\n"
        proc = self._run_gate(opening + middle + end + FUNNEL_BLOCK)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        report = json.loads((self.article_dir / "community-cta-gate.json").read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
