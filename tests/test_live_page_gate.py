"""Tests for live-page gate theme parity helpers."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_live_page_gate import (  # noqa: E402
    _extract_article_body,
    _extract_featured_block,
    _permalink_paths_equivalent,
    inspect,
)


class LivePageGateHelpersTest(unittest.TestCase):
    def test_permalink_blog_prefix_equivalent(self) -> None:
        left = "https://example.com/blog/my-slug/"
        right = "https://example.com/my-slug/"
        self.assertTrue(_permalink_paths_equivalent(left, right))

    def test_permalink_exact_match(self) -> None:
        url = "https://example.com/blog/foo/"
        self.assertTrue(_permalink_paths_equivalent(url, url))

    def test_extract_entry_content(self) -> None:
        html = '<div id="article-content"><p>probe text</p></div>'
        match = _extract_article_body(html)
        self.assertIsNotNone(match)
        self.assertIn("probe text", match.group(1))

    def test_extract_articles_typical_content(self) -> None:
        html = '<div class="articles-typical__content"><p>tyumen probe</p></div>'
        match = _extract_article_body(html)
        self.assertIsNotNone(match)
        self.assertIn("tyumen probe", match.group(1))

    def test_extract_featured_typical_image(self) -> None:
        html = '<div class="articles-typical__image"><img src="x.png" alt="cover"></div>'
        match = _extract_featured_block(html)
        self.assertIsNotNone(match)
        self.assertIn("cover", match.group(1))

    def test_expected_schema_jsonld_faq_parity(self) -> None:
        html = """
        <html><head><title>Test</title></head><body>
        <h2>Частые вопросы</h2>
        <h3>Вопрос?</h3><p>Ответ.</p>
        <div class="articles-typical__content"><img src="https://cdn/x.png" alt="ok"></div>
        <div class="articles-typical__image"><img src="https://cdn/y.png" alt="feat"></div>
        </body></html>
        """
        schema = json.dumps(
            {
                "@type": "BlogPosting",
                "url": "https://example.com/my-slug/",
                "mainEntity": {
                    "@type": "FAQPage",
                    "mainEntity": [
                        {
                            "@type": "Question",
                            "name": "Вопрос?",
                            "acceptedAnswer": {"@type": "Answer", "text": "Ответ."},
                        }
                    ],
                },
            },
            ensure_ascii=False,
        )
        errors = inspect(
            html,
            expected_slug="my-slug",
            expected_permalink="https://example.com/blog/my-slug/",
            expected_schema_jsonld=schema,
            verify_media=False,
        )
        jsonld_errors = [e for e in errors if "JSON-LD" in e or "jsonld" in e.lower()]
        self.assertEqual(jsonld_errors, [], errors)


if __name__ == "__main__":
    unittest.main()
