"""Tests for Derouter --output path resolution under --article-dir."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DerouterOutputPathTests(unittest.TestCase):
    def test_bare_filename_resolves_under_article_dir(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import resolve_derouter_output_path

        article = "memory/blog/articles/B03-test-slug"
        out = resolve_derouter_output_path(
            "schema.jsonld",
            article_dir=article,
            root=ROOT,
        )
        self.assertEqual(
            out,
            (ROOT / article / "schema.jsonld").resolve(),
        )

    def test_repo_relative_output_not_nested_twice(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import resolve_derouter_output_path

        article = "memory/blog/articles/B03-test-slug"
        full = f"{article}/schema.jsonld"
        out = resolve_derouter_output_path(
            full,
            article_dir=article,
            root=ROOT,
        )
        self.assertEqual(out, (ROOT / full).resolve())

    def test_without_article_dir_relative_goes_to_repo_root(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import resolve_derouter_output_path

        out = resolve_derouter_output_path("schema.jsonld", article_dir=None, root=ROOT)
        self.assertEqual(out, ROOT / "schema.jsonld")

    def test_write_under_article_dir_on_disk(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import resolve_derouter_output_path

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            article = root / "memory/blog/articles/B99-slug"
            article.mkdir(parents=True)
            out = resolve_derouter_output_path(
                "schema.jsonld",
                article_dir=str(article.relative_to(root)),
                root=root,
            )
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text('{"@type":"BlogPosting"}\n', encoding="utf-8")
            self.assertTrue((article / "schema.jsonld").is_file())
            self.assertFalse((root / "schema.jsonld").is_file())


if __name__ == "__main__":
    unittest.main()
