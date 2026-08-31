"""HARD gate: CASE delivery blocks how-to H1, duty-log openings, thin leads."""
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

SMOOTH_OPENING = (
    "<p>«Оплатили за двоих» — в чате бронь закрыта. У двери просят ещё 2 400 ₽ "
    "за третьего. Нет. Так не заселяем.</p>"
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

    def test_blocks_how_to_chto_nuzhno_znat(self) -> None:
        errors = check_h1("Что нужно знать перед посуточной арендой в Тюмени")
        self.assertTrue(errors)
        joined = " ".join(errors).lower()
        self.assertTrue("how-to" in joined or "что нужно" in joined)

    def test_blocks_h1_without_figure(self) -> None:
        errors = check_h1("Обещали парковку рядом. Шлагбаум не пустил")
        self.assertTrue(any("figure" in e or "цифра" in e for e in errors))

    def test_passes_h1_with_figure(self) -> None:
        errors = check_h1("«Парковка бесплатно». У шлагбаума попросили 500 ₽")
        self.assertEqual(errors, [], errors)

    def test_passes_two_beat_case_h1(self) -> None:
        errors = check_h1(
            "Хозяин сказал «всё включено». В такси доплатили 2 400 ₽"
        )
        self.assertEqual(errors, [], errors)

    def test_passes_h1_without_clock_oplatili(self) -> None:
        errors = check_h1("Оплатили за двоих. У двери попросили доплату за третьего")
        self.assertEqual(errors, [], errors)

    def test_passes_h1_without_clock_utrom(self) -> None:
        errors = check_h1("Перевёл 3 000 ₽ предоплаты. Утром квартиру уже сдали")
        self.assertEqual(errors, [], errors)

    def test_blocks_h1_with_clock(self) -> None:
        errors = check_h1("Звонок в 10:00. Заселился в 22:00 — у стола нет розетки")
        self.assertTrue(any("clock" in e.lower() for e in errors))

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

    def test_blocks_duty_log_saturday_stamp(self) -> None:
        opening = (
            "<p>Суббота, 23 августа 2026 года, 21:40. Тюмень, двор у подъезда. "
            "Гость с чемоданом.</p>"
        )
        errors = check_opening_body(opening, label="test")
        self.assertTrue(any("duty-log" in e for e in errors))

    def test_blocks_duty_log_august_clock(self) -> None:
        opening = (
            "<p>28 августа в 22:15 Марина искала квартиру в Тюмени.</p>"
        )
        errors = check_opening_body(opening, label="test")
        self.assertTrue(any("duty-log" in e for e in errors))

    def test_passes_smooth_holyslav_opening(self) -> None:
        errors = check_opening_body(SMOOTH_OPENING, label="test")
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
