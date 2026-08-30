"""SITE_BASE /blog/ xlink helpers."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_site_base import (
    SITE_BASE_PLACEHOLDER,
    canonical_blog_xlink_href,
    expand_blog_xlinks_in_html,
    is_root_relative_blog_href,
)


class SiteBaseXlinkTests(unittest.TestCase):
    def test_canonical_blog_xlink_href(self) -> None:
        self.assertEqual(
            canonical_blog_xlink_href("foo-bar"),
            f"{SITE_BASE_PLACEHOLDER}/blog/foo-bar/",
        )

    def test_is_root_relative_blog_href(self) -> None:
        self.assertTrue(is_root_relative_blog_href("/blog/foo/"))
        self.assertTrue(is_root_relative_blog_href("/blog"))
        self.assertFalse(is_root_relative_blog_href(f"{SITE_BASE_PLACEHOLDER}/blog/foo/"))
        self.assertFalse(is_root_relative_blog_href("https://example.test/blog/foo/"))

    def test_expand_blog_xlinks_in_html(self) -> None:
        html = (
            '<p><a href="/blog/foo/">rel</a> '
            f'<a href="{SITE_BASE_PLACEHOLDER}/blog/bar/">placeholder</a></p>'
        )
        out = expand_blog_xlinks_in_html(html, "https://добрыйдом-72.рф")
        self.assertIn('href="https://добрыйдом-72.рф/blog/foo/"', out)
        self.assertIn('href="https://добрыйдом-72.рф/blog/bar/"', out)
        self.assertNotIn('href="/blog/', out)


if __name__ == "__main__":
    unittest.main()
