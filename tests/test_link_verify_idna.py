"""Tests for Cyrillic host IDNA encoding in link-verify (INC-20260828 link-verify)."""
from __future__ import annotations

import unittest

ROOT = __import__("pathlib").Path(__file__).resolve().parents[1]
import sys

sys.path.insert(0, str(ROOT / "scripts"))


class LinkVerifyIdnaTests(unittest.TestCase):
    def test_encode_cyrillic_host_to_punycode(self) -> None:
        from excalibur_blog_link_verify import encode_idna_url

        url = "https://добрыйдом-72.рф/blog/test/"
        encoded = encode_idna_url(url)
        self.assertTrue(encoded.isascii(), encoded)
        self.assertIn("xn--", encoded)
        self.assertIn("/blog/test/", encoded)

    def test_ascii_url_unchanged(self) -> None:
        from excalibur_blog_link_verify import encode_idna_url

        url = "https://example.com/path"
        self.assertEqual(encode_idna_url(url), url)


if __name__ == "__main__":
    unittest.main()
