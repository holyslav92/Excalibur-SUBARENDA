"""Tests for WordPress-style intermediate image resize."""
from __future__ import annotations

import io
import sys
import unittest
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_wp_intermediate_refresh import (  # noqa: E402
    full_name_from_intermediate,
    is_intermediate_name,
    resize_wp_image,
    uploads_prefix_from_source_url,
    wp_constrain_dimensions,
    zen_upload_names,
)


class WpIntermediateRefreshTest(unittest.TestCase):
    def test_constrain_16_9(self) -> None:
        self.assertEqual(wp_constrain_dimensions(1200, 675, 1024, 576), (1024, 576))

    def test_resize_large_matches_box(self) -> None:
        img = Image.new("RGB", (1200, 675), color=(10, 20, 30))
        out = resize_wp_image(img, 1024, 576, crop=False)
        self.assertEqual(out.size, (1024, 576))

    def test_thumbnail_center_crop(self) -> None:
        img = Image.new("RGB", (1200, 675), color=(255, 0, 0))
        out = resize_wp_image(img, 150, 150, crop=True)
        self.assertEqual(out.size, (150, 150))

    def test_intermediate_name_parse(self) -> None:
        name = "dogovor-arendy-pravila-prozhivaniya-posutochno-cover-1-1024x576.png"
        self.assertTrue(is_intermediate_name(name))
        self.assertEqual(
            full_name_from_intermediate(name),
            "dogovor-arendy-pravila-prozhivaniya-posutochno-cover-1.png",
        )

    def test_uploads_prefix_from_2026_09_source_url(self) -> None:
        url = (
            "https://example.test/wp-content/uploads/2026/09/"
            "posutochno-tyumen-pyatyj-etazh-lift-chemodan-cover.png"
        )
        self.assertEqual(
            uploads_prefix_from_source_url(url),
            "wp-content/uploads/2026/09/",
        )

    def test_zen_upload_names_parses_year_month(self) -> None:
        feed = """
        <item>
          <enclosure url="https://example.test/wp-content/uploads/2026/09/slug-cover-1024x576.png"/>
        </item>
        """
        with unittest.mock.patch(
            "excalibur_blog_wp_intermediate_refresh.zen_feed_block",
            return_value=feed,
        ):
            pairs = zen_upload_names("https://example.test", "slug")
        self.assertEqual(
            pairs,
            [("wp-content/uploads/2026/09/", "slug-cover-1024x576.png")],
        )


if __name__ == "__main__":
    unittest.main()
