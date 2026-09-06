"""Tests for publish slug resolution (title-brief vs article-dir suffix)."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublishSlugResolutionTests(unittest.TestCase):
    def test_title_brief_slug_wins_over_dir_suffix(self) -> None:
        from scripts.excalibur_blog_article_meta_index import resolve_publish_slug

        with tempfile.TemporaryDirectory() as tmp:
            article_dir = Path(tmp) / "B12-kvartira-posutochno-tihij-centr-strojka-za-oknom-tyumen"
            article_dir.mkdir()
            (article_dir / "title-brief.json").write_text(
                json.dumps(
                    {
                        "topic_id": "B12",
                        "slug": "napisali-tihij-centr-v-6-30-za-oknom-kran",
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                resolve_publish_slug(article_dir),
                "napisali-tihij-centr-v-6-30-za-oknom-kran",
            )

    def test_meta_slug_wins_over_title_brief(self) -> None:
        from scripts.excalibur_blog_article_meta_index import resolve_publish_slug

        with tempfile.TemporaryDirectory() as tmp:
            article_dir = Path(tmp) / "B12-dir-slug"
            article_dir.mkdir()
            (article_dir / "title-brief.json").write_text(
                json.dumps({"slug": "from-title"}),
                encoding="utf-8",
            )
            (article_dir / "article.meta.json").write_text(
                json.dumps({"slug": "from-meta"}),
                encoding="utf-8",
            )
            self.assertEqual(resolve_publish_slug(article_dir), "from-meta")


if __name__ == "__main__":
    unittest.main()
