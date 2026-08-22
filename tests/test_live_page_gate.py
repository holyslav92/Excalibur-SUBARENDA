"""Tests for Dobry Dom / default-WP theme live-page gate fallbacks."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_live_page_gate import inspect  # noqa: E402


FIXTURE = ROOT / "tests" / "fixtures" / "dobry-dom-live-post.html"
SCHEMA = ROOT / "memory/blog/articles/B03-pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti/schema.jsonld"


class LivePageGateDobryDomTest(unittest.TestCase):
  def test_entry_content_and_wp_post_image_pass_with_publish_schema(self) -> None:
    html = FIXTURE.read_text(encoding="utf-8")
    schema_raw = SCHEMA.read_text(encoding="utf-8")
    schema = json.loads(schema_raw.replace("{{SITE_BASE}}", "https://example.com"))
    errors = inspect(
      html,
      expected_slug="pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti",
      expected_permalink="https://example.com/blog/pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti/",
      expected_schema_jsonld=json.dumps(schema, ensure_ascii=False),
      verify_media=False,
    )
    self.assertEqual(errors, [], errors)

  def test_blog_permalink_equivalent_to_schema_root_path(self) -> None:
    from excalibur_blog_live_page_gate import _permalink_paths_equivalent

    self.assertTrue(
      _permalink_paths_equivalent(
        "https://example.com/blog/foo/",
        "https://example.com/foo/",
      )
    )


if __name__ == "__main__":
  unittest.main()
