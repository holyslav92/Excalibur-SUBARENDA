"""Tests for Dzen RSS factory contract."""

from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DzenRssContractTest(unittest.TestCase):
    def test_mu_plugin_present(self) -> None:
        path = ROOT / "factory/wp-mu-plugins/excalibur-dzen-rss.php"
        text = path.read_text(encoding="utf-8")
        self.assertIn("format-article", text)
        self.assertIn("native-no", text)
        self.assertIn("yzen_thumb_imgurl", text)

    def test_wp_dzen_rss_module(self) -> None:
        from excalibur_blog_wp_dzen_rss import (
            DZEN_FORBIDDEN_PLATFORM,
            DZEN_FORMAT_CATEGORY,
            DZEN_PLATFORM_NATIVE_YES,
            default_yzen_options,
            post_dzen_meta_values,
        )

        opts = default_yzen_options("https://example.com")
        self.assertEqual(opts["yztypeplatform"], DZEN_PLATFORM_NATIVE_YES)
        self.assertEqual(opts["yzselectthumb"], "full")
        self.assertNotEqual(opts["yztypeplatform"], DZEN_FORBIDDEN_PLATFORM)

        meta = post_dzen_meta_values()
        self.assertEqual(meta["yztypeplatform_meta_value"], DZEN_PLATFORM_NATIVE_YES)
        self.assertEqual(DZEN_FORMAT_CATEGORY, "format-article")

    def test_dzen_rss_contract_doc(self) -> None:
        text = (ROOT / "shared/dzen-rss-contract.md").read_text(encoding="utf-8")
        self.assertIn("native-no", text)
        self.assertIn("format-article", text)
        self.assertIn("excalibur-dzen-rss.php", text)

    def test_publish_imports_dzen_helpers(self) -> None:
        publish = (ROOT / "scripts/excalibur_blog_wp_publish.py").read_text(encoding="utf-8")
        self.assertIn("excalibur_blog_wp_dzen_rss", publish)
        self.assertIn("dzen_meta_php_snippet", publish)
        self.assertIn("deploy_dzen_mu_plugin", publish)


if __name__ == "__main__":
    unittest.main()
