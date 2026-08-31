"""Normalize committed article HTML site URLs (INC-20260831)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_site_base import (  # noqa: E402
    SITE_BASE_PLACEHOLDER,
    find_punycode_href_hits,
    normalize_committed_html_site_urls,
    redact_site_base,
)


PUNY_SAMPLE = (
    '<a href="https://xn----7sbabcgi5aqbrdkdcgs2f.xn--p1ai/blog/foo/">link</a>'
)
UNICODE_SAMPLE = (
    '<a href="https://добрыйдом-72.рф/blog/bar/">link</a>'
)


class SiteBaseNormalizeTests(unittest.TestCase):
    def test_normalize_punycode_href_without_env(self) -> None:
        out = normalize_committed_html_site_urls(PUNY_SAMPLE)
        self.assertIn(f'href="{SITE_BASE_PLACEHOLDER}/blog/foo/"', out)
        self.assertEqual(find_punycode_href_hits(out), [])

    def test_redact_unicode_with_public_base(self) -> None:
        out = redact_site_base(
            UNICODE_SAMPLE,
            "https://добрыйдом-72.рф",
        )
        self.assertIn(f'href="{SITE_BASE_PLACEHOLDER}/blog/bar/"', out)

    def test_redact_punycode_with_unicode_public_base(self) -> None:
        """IDNA punycode from unicode host may differ from Derouter-emitted xn-- href."""
        out = redact_site_base(
            PUNY_SAMPLE,
            "https://добрыйдом-72.рф",
        )
        # Wrong/alternate punycode survives redact alone — normalize fixes it.
        self.assertIn("xn--", out)
        fixed = normalize_committed_html_site_urls(out)
        self.assertIn(f'href="{SITE_BASE_PLACEHOLDER}/blog/foo/"', fixed)
        self.assertEqual(find_punycode_href_hits(fixed), [])

    def test_root_relative_blog_href(self) -> None:
        html = '<a href="/blog/baz/">rel</a>'
        out = normalize_committed_html_site_urls(html)
        self.assertIn(f'href="{SITE_BASE_PLACEHOLDER}/blog/baz/"', out)


if __name__ == "__main__":
    unittest.main()
