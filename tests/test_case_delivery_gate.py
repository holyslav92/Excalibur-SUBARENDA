"""HARD gate: CASE delivery blocks how-to H1 and thin openings."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.excalibur_blog_case_delivery_gate import (
    check_h1,
    check_opening_body,
    check_article_dir,
)

ROOT = Path(__file__).resolve().parents[1]

DENSE_OPENING = (
    "<p>26 августа, Тюмень, 23:40. Код из приложения сработал, дверь открылась — "
    "но из крана льётся ледяная вода. В чате хост отвечает в 00:12: «Утром будет, "
    "бойлер выключили ночью». Вы стоите с мокрыми руками, завтра встреча в 9:00 — "
    "а «утром» в их голове наступает после вашего выезда. Обещание было. "
    "И оно не соврало — просто про их утро, не про ваше — доплата 800 ₽ в переписке не светилась.</p>"
    "<p>Я хост посуточной в Тюмени. Это «Добрый дом».</p>"
)


class CaseDeliveryGateTest(unittest.TestCase):
    def test_script_exists(self) -> None:
        self.assertTrue((ROOT / "scripts/excalibur_blog_case_delivery_gate.py").is_file())

    def test_blocks_how_to_h1(self) -> None:
        errors = check_h1("Как снять квартиру посуточно в Тюмени: 7 шагов")
        self.assertTrue(errors)
        joined = " ".join(errors).lower()
        self.assertTrue("how-to" in joined or "как снять" in joined)

    def test_blocks_topic_label_h1(self) -> None:
        errors = check_h1("О проверке квартиры перед заселением")
        self.assertTrue(any("topic label" in e for e in errors))

    def test_passes_two_beat_case_h1(self) -> None:
        errors = check_h1(
            "Хозяин сказал «всё включено». В такси доплатили 2 400 ₽"
        )
        self.assertEqual(errors, [], errors)

    def test_blocks_h1_without_two_beats(self) -> None:
        errors = check_h1("Залог при посуточной аренде")
        self.assertTrue(any("two-beat" in e for e in errors))

    def test_blocks_chopped_opening(self) -> None:
        chopped = (
            "<p>02:14.</p><p>Тюмень.</p><p>Сын рядом.</p>"
            "<p>Код есть.</p><p>Дверь закрыта.</p><p>Хост молчит.</p>"
            "<p>Вы стоите.</p><p>С чемоданом.</p>"
        )
        errors = check_opening_body(chopped, label="test")
        self.assertTrue(any("chopped" in e for e in errors))

    def test_passes_dense_case_opening(self) -> None:
        errors = check_opening_body(DENSE_OPENING, label="test")
        self.assertEqual(errors, [], errors)

    def test_title_stage_blocks_skeleton(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            (d / "title-brief.json").write_text(
                json.dumps(
                    {"h1": "5 вопросов хозяину до перевода предоплаты", "verdict": "PASS"},
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            report = check_article_dir(d, stage="title")
            self.assertEqual(report["status"], "BLOCK")

    def test_writer_stage_needs_case_elements(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            drafts = d / "drafts"
            drafts.mkdir()
            (drafts / "writer.html").write_text(
                "<p>Разберём, что проверить при заселении в квартиру посуточно.</p>",
                encoding="utf-8",
            )
            report = check_article_dir(d, stage="writer")
            self.assertEqual(report["status"], "BLOCK")


if __name__ == "__main__":
    unittest.main()
