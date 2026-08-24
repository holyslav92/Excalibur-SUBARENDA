"""Абсолютные href для Дзена: relative /blog/ не должен уезжать на dzen.ru."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_interlink_lib import permalink_path_for_slug  # noqa: E402
from excalibur_blog_live_xlink_fix import strip_legacy_category_blog_hrefs  # noqa: E402
from excalibur_blog_site_base import (  # noqa: E402
    absolutize_root_relative_hrefs,
    expand_site_base,
)


class AbsolutizeHrefsTests(unittest.TestCase):
    def test_blog_and_home_become_absolute(self) -> None:
        html = (
            '<p><a href="/blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/">'
            "залог</a> и <a href=\"/\">сайт</a></p>"
        )
        out = absolutize_root_relative_hrefs(html, "https://example.test")
        self.assertIn(
            'href="https://example.test/blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/"',
            out,
        )
        self.assertIn('href="https://example.test/"', out)
        self.assertNotIn('href="/blog/', out)

    def test_protocol_relative_and_external_unchanged(self) -> None:
        html = '<a href="//cdn.example/x">x</a> <a href="https://t.me/foo">tg</a>'
        out = absolutize_root_relative_hrefs(html, "https://example.test")
        self.assertEqual(html, out)

    def test_empty_base_keeps_relative(self) -> None:
        html = '<a href="/blog/foo/">foo</a>'
        self.assertEqual(html, absolutize_root_relative_hrefs(html, ""))

    def test_expand_then_absolutize_does_not_double_host(self) -> None:
        html = '<a href="{{SITE_BASE}}/blog/foo/">foo</a> <a href="/blog/bar/">bar</a>'
        expanded = expand_site_base(html, "https://example.test")
        out = absolutize_root_relative_hrefs(expanded, "https://example.test")
        self.assertEqual(out.count("https://example.test"), 2)
        self.assertIn('href="https://example.test/blog/foo/"', out)
        self.assertIn('href="https://example.test/blog/bar/"', out)

    def test_permalink_path_is_blog_slug_not_category(self) -> None:
        self.assertEqual(permalink_path_for_slug("my-slug"), "/blog/my-slug/")

    def test_strip_legacy_vtorichka_category(self) -> None:
        html = (
            '<a href="/blog/vtorichka-i-riski/rosfinmonitoring-sdelka-nedvizhimost-cheklis-tyumen-2026/">'
            "чеклист</a>"
            '<a href="https://example.test/blog/vtorichka-i-riski/skrytye-doplaty-pri-posutochnoj-arende-ot-hozyaina/">'
            "доплаты</a>"
        )
        out, changes = strip_legacy_category_blog_hrefs(html)
        self.assertEqual(len(changes), 2)
        self.assertIn("/blog/rosfinmonitoring-sdelka-nedvizhimost-cheklis-tyumen-2026/", out)
        self.assertIn(
            "https://example.test/blog/skrytye-doplaty-pri-posutochnoj-arende-ot-hozyaina/",
            out,
        )
        self.assertNotIn("vtorichka-i-riski", out)


if __name__ == "__main__":
    unittest.main()
