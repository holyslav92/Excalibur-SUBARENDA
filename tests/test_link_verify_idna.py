"""Tests for IDN / Cyrillic URL handling in link_verify (INC-20260826-1257)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class LinkVerifyIdnaTest(unittest.TestCase):
    def test_normalize_url_for_http_punycode_host(self) -> None:
        from excalibur_blog_site_base import normalize_url_for_http

        url = normalize_url_for_http("https://добрыйдом-72.рф/booking/")
        self.assertIn("xn--", url)
        self.assertNotIn("д", url)
        self.assertTrue(url.endswith("/booking/"))

    def test_normalize_url_for_http_passthrough_ascii(self) -> None:
        from excalibur_blog_site_base import normalize_url_for_http

        url = normalize_url_for_http("https://example.com/path")
        self.assertEqual(url, "https://example.com/path")

    def test_check_url_cyrillic_host_no_unicode_encode_error(self) -> None:
        from excalibur_blog_link_verify import check_url

        result = check_url("https://добрыйдом-72.рф/", timeout=15.0, user_agent="ExcaliburTest/1.0")
        self.assertNotIn("UnicodeEncodeError", str(result.get("error") or ""))
        self.assertTrue(result.get("ok"), result)


if __name__ == "__main__":
    unittest.main()
