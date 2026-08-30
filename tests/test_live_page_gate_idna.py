"""Tests for Cyrillic host IDNA encoding in live-page gate (INC-20260830)."""
from __future__ import annotations

import unittest

ROOT = __import__("pathlib").Path(__file__).resolve().parents[1]
import sys

sys.path.insert(0, str(ROOT / "scripts"))


class LivePageGateIdnaTests(unittest.TestCase):
    def test_main_accepts_cyrillic_permalink_without_latin1_error(self) -> None:
        from excalibur_blog_link_verify import encode_idna_url

        url = "https://добрыйдом-72.рф/blog/test-slug/"
        encoded = encode_idna_url(url)
        self.assertTrue(encoded.isascii(), encoded)
        self.assertIn("xn--", encoded)

    def test_normalize_live_url_unicode_and_punycode_match(self) -> None:
        from excalibur_blog_link_verify import encode_idna_url
        from excalibur_blog_live_page_gate import _normalize_live_url

        unicode_url = "https://добрыйдом-72.рф/blog/foo/"
        puny = encode_idna_url(unicode_url)
        self.assertEqual(_normalize_live_url(unicode_url), _normalize_live_url(puny))


if __name__ == "__main__":
    unittest.main()
