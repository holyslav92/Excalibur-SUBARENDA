"""Tests for live Dzen bump spec builder (inline slots vs H2 sections)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_live_cover_regen_aug22 import (  # noqa: E402
    count_inline_images,
    pad_h2s_for_inline_slots,
)
from excalibur_blog_wp_intermediate_refresh import (  # noqa: E402
    uploads_prefix_from_media,
    zen_upload_pattern,
)


B33_FRAGMENT = """
<h2>Что произошло с оплатой</h2>
<figure data-slot="inline_3"><img src="/wp-content/uploads/2026/09/foo-inline-03.png"></figure>
<figure data-slot="inline_2"><img src="/wp-content/uploads/2026/09/foo-inline-02.png"></figure>
<figure data-slot="inline_1"><img src="/wp-content/uploads/2026/09/foo-inline-01.png"></figure>
<h2>Почему хозяин предлагает оплатить напрямую</h2>
<figure data-slot="inline_5"></figure>
<figure data-slot="inline_4"></figure>
<h2>Что проверить до перевода</h2>
<figure data-slot="inline_6"></figure>
<h2>Мой вывод как практика</h2>
<figure data-slot="inline_7"></figure>
"""


class DzenBuildSpecTest(unittest.TestCase):
    def test_count_inline_images_from_data_slots(self) -> None:
        self.assertEqual(count_inline_images(B33_FRAGMENT), 7)

    def test_pad_h2s_when_fewer_sections_than_inlines(self) -> None:
        h2s = ["A", "B", "C", "D"]
        padded = pad_h2s_for_inline_slots(h2s, 7, "fallback")
        self.assertEqual(len(padded), 7)
        self.assertEqual(padded[:4], h2s)

    def test_uploads_prefix_from_media_source_url(self) -> None:
        media = [{"source_url": "https://example.com/wp-content/uploads/2026/09/cover.png"}]
        self.assertEqual(
            uploads_prefix_from_media(media),
            "wp-content/uploads/2026/09/",
        )

    def test_zen_upload_pattern_matches_month(self) -> None:
        zen_re = zen_upload_pattern("wp-content/uploads/2026/09/")
        block = '<enclosure url="https://x/wp-content/uploads/2026/09/slug-inline-01-1024x576.png"/>'
        self.assertEqual(zen_re.findall(block), ["slug-inline-01-1024x576.png"])


if __name__ == "__main__":
    unittest.main()
