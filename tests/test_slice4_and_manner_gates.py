"""Tests for klyshin_manner_dobry_dom_v1 + dobry_dom_one_2k_slice4_v1 locks."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_case_delivery_gate import (  # noqa: E402
    MANNER_CANON_ID,
    WORD_COUNT_HARD_MAX,
    check_manner_stamps,
    check_word_count,
    check_article_dir,
)
from excalibur_blog_quad_slots import ONE_2K_SLICE4_CANON_ID, uses_one_2k_slice4  # noqa: E402
from excalibur_blog_brand_logo_composite import prepare_logo_rgba  # noqa: E402

LOGO = ROOT / "memory/cover/assets/brand/logo-dobry-dom.png"

GOOD_ARTICLE = (
    "<p>«Парковка бесплатно» — в чате так и написали. У шлагбаума попросили 800 ₽. "
    "Вы уже в машине, ребёнок спит.</p>"
    "<p>Я хост посуточной в Тюмени. Это «Добрый дом».</p>"
    "<h2>Где ловят</h2><p>На словах «бесплатно» без номера места и без скрина шлагбаума.</p>"
    "<h2>Мой вывод как практика</h2><p>Сначала место на карте, потом перевод. Не наоборот.</p>"
    "<h2>Что спросить до оплаты</h2><ul><li>Номер парковочного места</li><li>Скрин шлагбаума</li></ul>"
    + "<p>Залог 5 000 — норм или перебор? Ответ в Telegram.</p>" * 3
)


class KlyshinMannerGateTest(unittest.TestCase):
    def test_manner_canon_in_pipeline(self) -> None:
        canon = json.loads((ROOT / "shared/pipeline-canon.json").read_text(encoding="utf-8"))
        self.assertEqual(canon.get("editorial_manner_canon"), MANNER_CANON_ID)
        self.assertEqual(canon.get("cover_pipeline_canon"), ONE_2K_SLICE4_CANON_ID)
        self.assertEqual(canon["opening_rules"].get("word_count_target"), "700-1100")

    def test_article_style_names_manner_canon(self) -> None:
        style = (ROOT / "shared/article-style.md").read_text(encoding="utf-8")
        self.assertIn(MANNER_CANON_ID, style)
        self.assertIn("700–1100", style)
        self.assertIn("Мой вывод как практика", style)
        self.assertNotIn("1100–1800", style)

    def test_bans_nash_vyvod_stamp(self) -> None:
        html = "<p>Наш вывод простой. Хороший хост — тот, кто говорит цифры заранее.</p>"
        errors = check_manner_stamps(html, label="test")
        self.assertTrue(errors)

    def test_bans_repeat_net_tak_ne_zaselyaem(self) -> None:
        html = (
            "<p>Нет. Так не заселяем.</p><p>Снова: нет. Так не заселяем.</p>"
        )
        errors = check_manner_stamps(html, label="test")
        self.assertTrue(errors)

    def test_word_count_hard_max_1300(self) -> None:
        long_html = "<p>" + "слово " * 1400 + "</p>"
        errors = check_word_count(long_html, label="test")
        self.assertTrue(any(str(WORD_COUNT_HARD_MAX) in e for e in errors))

    def test_article_style_forbids_old_length(self) -> None:
        prompt = (ROOT / "shared/writer-master-prompt.md").read_text(encoding="utf-8")
        self.assertIn("700–1100", prompt)
        self.assertNotIn("1100–1800", prompt)


class Slice4CanonTest(unittest.TestCase):
    def test_slice4_canon_active(self) -> None:
        self.assertTrue(uses_one_2k_slice4(ROOT))
        canon = json.loads((ROOT / "memory/cover/cover-canon.json").read_text(encoding="utf-8"))
        self.assertEqual(canon["canon_id"], ONE_2K_SLICE4_CANON_ID)

    def test_tenant_slice4_config(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        self.assertEqual(tenant.get("cover_mode"), "one_2k_slice4")
        self.assertEqual(tenant.get("inline_image_count"), 3)
        img = tenant.get("image_generation") or {}
        self.assertEqual(img.get("total_images"), 4)
        self.assertEqual(img.get("canvases_per_article"), 1)
        wow = tenant.get("cover_wow_rules") or {}
        self.assertEqual(wow.get("canon_id"), ONE_2K_SLICE4_CANON_ID)
        self.assertIn("native aspect", wow.get("philosophy", "").casefold())

    def test_slice4_doctor(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/excalibur_blog_slice4_gate.py"), "--doctor"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)

    def test_slice4_blocks_second_batch(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            cover = d / "cover"
            cover.mkdir()
            (cover / "slice4-mcp-batch.json").write_text("{}", encoding="utf-8")
            (cover / "quad-mcp-batch-02.json").write_text("{}", encoding="utf-8")
            from excalibur_blog_slice4_gate import check_article_dir as slice4_check  # noqa: PLC0415

            report = slice4_check(d, root=ROOT)
            self.assertEqual(report["status"], "BLOCK")
            self.assertTrue(any("quad-mcp-batch-02" in e for e in report["errors"]))

    def test_logo_paste_keeps_native_aspect_not_square(self) -> None:
        self.assertTrue(LOGO.is_file(), "official logo missing")
        from PIL import Image

        with Image.open(LOGO) as raw:
            full_w, full_h = raw.size
        cropped = prepare_logo_rgba(LOGO, 120)
        self.assertLess(cropped.width, full_w)
        ratio = cropped.width / max(cropped.height, 1)
        self.assertGreater(ratio, 1.1, "logo should stay wide (not square crop)")

    def test_slice4_prompt_mentions_grid(self) -> None:
        from excalibur_blog_cover_quad_prompt import build_one_2k_slice4_grid_prompt  # noqa: PLC0415

        manifest = {
            "cover_headline_line1": "в чате: парковка бесплатно",
            "cover_headline_line2": "у шлагбаума: +800 ₽",
            "slots": {
                "inline_1": {"h2_anchor": "Где ловят", "scene_hint": "шлагбаум"},
            },
        }
        style = json.loads((ROOT / "memory/cover/quad-style-dobry-dom.json").read_text(encoding="utf-8"))
        design = json.loads((ROOT / "memory/cover/cover-design-code.json").read_text(encoding="utf-8"))
        prompt = build_one_2k_slice4_grid_prompt(manifest, style, design, root=ROOT)
        low = prompt.casefold()
        self.assertIn("2×2", prompt)
        self.assertIn("native aspect", low)
        self.assertIn("not square", low)


if __name__ == "__main__":
    unittest.main()
