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
    canonicalize_tenant_site_hrefs_in_html,
    expand_blog_xlinks_in_html,
    href_host_variants,
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

    def test_href_host_variants_unicode_and_punycode(self) -> None:
        cyrillic = "https://добрыйдом-72.рф/booking/"
        variants = href_host_variants(cyrillic)
        self.assertIn("добрыйдом-72.рф", variants)
        self.assertTrue(any(v.startswith("xn--") for v in variants))

    def test_canonicalize_tenant_site_hrefs_in_html(self) -> None:
        tenant = {
            "cta_channels": {
                "site": "https://добрыйдом-72.рф/",
                "booking": "https://добрыйдом-72.рф/booking/",
            }
        }
        html = (
            '<p>Бронирование: <a href="https://xn----72-5cdbdlmuas0ap0k.xn--p1ai/booking/">'
            "https://добрыйдом-72.рф/booking/</a></p>"
        )
        fixed, changes = canonicalize_tenant_site_hrefs_in_html(html, tenant)
        self.assertEqual(len(changes), 1)
        self.assertIn('href="https://добрыйдом-72.рф/booking/"', fixed)
        self.assertNotIn("xn----72", fixed)


if __name__ == "__main__":
    unittest.main()
