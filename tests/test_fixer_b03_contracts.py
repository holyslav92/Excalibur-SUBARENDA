"""Durable fixes from B03 fixer loop (schema output, GRSAI base, interlink catalog)."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class GrsaiApiBaseTests(unittest.TestCase):
    def test_grsai_host_uses_v1_not_openai_v1(self) -> None:
        from excalibur_blog_derouter_gpt_image2_api import normalize_api_base

        grsai_host = "grsai" + "api.com"
        self.assertEqual(
            normalize_api_base(f"https://{grsai_host}"),
            f"https://{grsai_host}/v1",
        )
        self.assertEqual(
            normalize_api_base(f"https://{grsai_host}/v1"),
            f"https://{grsai_host}/v1",
        )
        self.assertEqual(
            normalize_api_base("https://api-direct.derouter.ai/openai/v1"),
            "https://api-direct.derouter.ai/openai/v1",
        )


class DerouterOutputPathTests(unittest.TestCase):
    def test_bare_schema_output_under_article_dir(self) -> None:
        from excalibur_repo_paths import resolve_article_output

        root = ROOT
        article = root / "memory/blog/articles/B03-example"
        out = resolve_article_output(
            "schema.jsonld",
            article_dir=article,
            root=root,
            default_name="schema.jsonld",
        )
        self.assertEqual(out, article / "schema.jsonld")


class InterlinkCatalogMergeTests(unittest.TestCase):
    def test_live_catalog_slugs_merge_when_cache_present(self) -> None:
        from excalibur_blog_interlink_lib import all_interlink_candidates

        catalog_path = ROOT / "memory/live-catalog.json"
        if not catalog_path.is_file():
            self.skipTest("memory/live-catalog.json missing in this checkout")
        candidates = all_interlink_candidates(ROOT, exclude_topic_id="B99")
        sources = {str(c.get("source")) for c in candidates}
        self.assertIn("ledger", sources)
        if json.loads(catalog_path.read_text(encoding="utf-8")).get("count", 0) > 2:
            self.assertIn("live_catalog", sources)
        titled = [c for c in candidates if c.get("title") and c["title"] != c.get("slug")]
        self.assertTrue(len(titled) >= 1 or len(candidates) <= 2)


if __name__ == "__main__":
    unittest.main()
