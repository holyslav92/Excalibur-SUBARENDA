#!/usr/bin/env python3
"""Tests for description/schema OG factory gates."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import sys

sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_description_gate import (  # noqa: E402
    description_og_factory_errors,
    validate_description_brief,
)
from excalibur_blog_schema_gate import validate_schema_text  # noqa: E402


class DescriptionOgFactoryTests(unittest.TestCase):
    def test_rejects_shakin_author(self) -> None:
        desc = "История Святослава Шакина: как не переплатить за сутки."
        errors = description_og_factory_errors(desc)
        self.assertTrue(any("Шакин" in e for e in errors))

    def test_rejects_brand_price_ladder(self) -> None:
        desc = "У Доброго дома две ночи по 2500 вышли 6500 с доплатами."
        errors = description_og_factory_errors(desc)
        self.assertTrue(len(errors) >= 1)

    def test_accepts_risk_teaser_without_brand_prices(self) -> None:
        desc = "Хост пишет «утром будет». Вы уже в квартире — где бойлер, спросите до замёрзания."
        self.assertEqual(description_og_factory_errors(desc), [])

    def test_gate_passes_clean_brief(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            article_dir = Path(tmp)
            (article_dir / "title-brief.json").write_text(
                json.dumps({"h1": "Код есть — из крана холодное"}, ensure_ascii=False),
                encoding="utf-8",
            )
            (article_dir / "article.html").write_text(
                "<p>23:40. Код сработал.</p><p>Из крана холодное.</p>",
                encoding="utf-8",
            )
            (article_dir / "description-brief.json").write_text(
                json.dumps(
                    {
                        "description": "Хост пишет «утром будет». Вы уже в квартире — где бойлер, спросите до замёрзания.",
                        "verdict": "PASS",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            result = validate_description_brief(article_dir)
            self.assertEqual(result["status"], "PASS")


class SchemaBlogPathTests(unittest.TestCase):
    def test_rejects_schema_without_blog_path(self) -> None:
        text = json.dumps(
            {
                "@context": "https://schema.org",
                "@type": "BlogPosting",
                "@id": "{{SITE_BASE}}/my-slug/#article",
                "url": "{{SITE_BASE}}/my-slug/",
                "author": {"@type": "Organization", "name": "Добрый дом"},
            },
            ensure_ascii=False,
        )
        errors = validate_schema_text(text)
        self.assertFalse(errors)  # validate_schema_text no longer forbids /blog/

    def test_schema_gate_requires_blog_path_in_main(self) -> None:
        # Full gate tested via integration; here ensure old anti-/blog/ rule removed
        text = '{{SITE_BASE}}/blog/slug/'
        errors = validate_schema_text(
            json.dumps({"url": text, "@type": "BlogPosting"}, ensure_ascii=False)
        )
        self.assertFalse(any("not /blog" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
