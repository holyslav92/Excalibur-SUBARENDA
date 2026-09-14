"""Community CTA gate punycode equivalence (INC B21)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_community_cta_gate import link_in_html


class CommunityCtaPunycodeTests(unittest.TestCase):
    def test_link_in_html_accepts_punycode_href_for_cyrillic_cta(self) -> None:
        html = (
            '<p>Бронирование: <a href="https://xn----72-5cdbdlmuas0ap0k.xn--p1ai/booking/">'
            "https://добрыйдом-72.рф/booking/</a></p>"
        )
        cta = "https://добрыйдом-72.рф/booking/"
        self.assertTrue(link_in_html(html, cta))

    def test_link_in_html_accepts_non_roundtrip_punycode_variant(self) -> None:
        """Sol may emit punycode that does not IDNA round-trip to Cyrillic host."""
        html = '<a href="https://xn----72-5cdbdlmuas0ap0k.xn--p1ai/">site</a>'
        cta = "https://добрыйдом-72.рф/"
        self.assertTrue(link_in_html(html, cta))


if __name__ == "__main__":
    unittest.main()
