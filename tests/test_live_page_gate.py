"""Tests for live page gate selectors and schema URL parity."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_live_page_gate import inspect  # noqa: E402


def _fixture_html(*, with_schema: bool = True) -> str:
    schema = ""
    if with_schema:
        schema = """
<script type="application/ld+json">{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "url": "https://example.com/dogovor-arendy/",
  "mainEntity": {
    "@type": "FAQPage",
    "mainEntity": [{
      "@type": "Question",
      "name": "Вопрос?",
      "acceptedAnswer": {"@type": "Answer", "text": "Ответ."}
    }]
  }
}</script>"""
    return f"""<!doctype html>
<html><head>
<link rel="canonical" href="https://example.com/blog/dogovor-arendy/" />
<title>Заголовок статьи</title>
{schema}
</head><body>
<section class="articles-typical">
  <div class="articles-typical__image post-thumbnail">
    <img src="https://example.com/cover.png" alt="Обложка" class="wp-post-image" />
  </div>
  <div id="article-content" class="articles-typical__content">
    <p>Первый абзац статьи для body probe.</p>
    <h2>Частые вопросы</h2>
    <h3>Вопрос?</h3>
    <p>Ответ.</p>
  </div>
</section>
</body></html>"""


class LivePageGateTest(unittest.TestCase):
    def test_dobry_dom_theme_selectors_pass(self) -> None:
        errors = inspect(
            _fixture_html(),
            expected_slug="dogovor-arendy",
            expected_permalink="https://example.com/blog/dogovor-arendy/",
            body_probe="Первый абзац статьи",
        )
        self.assertEqual(errors, [])

    def test_blogposting_slug_match_without_blog_prefix(self) -> None:
        errors = inspect(
            _fixture_html(),
            expected_slug="dogovor-arendy",
            expected_permalink="https://example.com/blog/dogovor-arendy/",
        )
        self.assertNotIn("live BlogPosting JSON-LD URL does not exactly match permalink", errors)

    def test_missing_schema_blocks_faq_jsonld(self) -> None:
        errors = inspect(
            _fixture_html(with_schema=False),
            expected_slug="dogovor-arendy",
            expected_permalink="https://example.com/blog/dogovor-arendy/",
        )
        self.assertTrue(any("FAQPage JSON-LD count" in err for err in errors))


if __name__ == "__main__":
    unittest.main()
