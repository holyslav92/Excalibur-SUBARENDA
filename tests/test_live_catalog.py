"""Live blog catalog crawl helpers."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_live_catalog import (  # noqa: E402
    MAX_LISTING_PAGES,
    catalog_ledger_gaps,
    fetch_live_catalog,
    merge_catalog_entries,
)


class LiveCatalogTests(unittest.TestCase):
    def test_max_listing_pages_covers_b43_incident(self) -> None:
        self.assertGreaterEqual(MAX_LISTING_PAGES, 24)

    def test_catalog_ledger_gaps(self) -> None:
        catalog = {"slug_index": {"alpha": {"slug": "alpha"}}}
        self.assertEqual(catalog_ledger_gaps(catalog, {"alpha"}), [])
        self.assertEqual(catalog_ledger_gaps(catalog, {"alpha", "beta"}), ["beta"])

    def test_fetch_stops_early_when_ensure_slugs_satisfied(self) -> None:
        page1 = [
            {"slug": "one", "title": "One", "href": "/blog/one/"},
            {"slug": "two", "title": "Two", "href": "/blog/two/"},
        ]

        def fake_fetch(_base: str, page: int) -> str:
            if page == 1:
                return "<html></html>"
            raise AssertionError(f"unexpected page {page}")

        with patch("excalibur_blog_live_catalog.fetch_listing_page", side_effect=fake_fetch):
            with patch("excalibur_blog_live_catalog.parse_listing_html", return_value=page1):
                catalog = fetch_live_catalog(
                    "https://example.test",
                    max_pages=24,
                    ensure_slugs={"one", "two"},
                )
        self.assertEqual(catalog["pages_fetched"], 1)
        self.assertEqual(catalog["ledger_slugs_missing"], [])
        self.assertEqual(catalog["count"], 2)

    def test_fetch_reports_missing_ledger_after_cap(self) -> None:
        entries = [{"slug": "only", "title": "Only", "href": "/blog/only/"}]

        with patch("excalibur_blog_live_catalog.fetch_listing_page", return_value="<html></html>"):
            with patch("excalibur_blog_live_catalog.parse_listing_html", return_value=entries):
                catalog = fetch_live_catalog(
                    "https://example.test",
                    max_pages=1,
                    ensure_slugs={"only", "missing-slug"},
                )
        self.assertEqual(catalog["ledger_slugs_missing"], ["missing-slug"])

    def test_merge_catalog_keeps_longer_title(self) -> None:
        merged = merge_catalog_entries(
            [
                {"slug": "x", "title": "Short", "href": "/blog/x/"},
                {"slug": "x", "title": "Much longer catalog title", "href": "/blog/x/"},
            ]
        )
        self.assertEqual(merged["x"]["title"], "Much longer catalog title")


if __name__ == "__main__":
    unittest.main()
