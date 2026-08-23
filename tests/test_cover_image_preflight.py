"""Tests for Cover image preflight and Kie credits blocker."""
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CoverImagePreflightTests(unittest.TestCase):
    def test_analyze_probe_discontinued(self) -> None:
        from scripts.excalibur_blog_cover_image_preflight import analyze_probe

        report = {
            "winner": None,
            "results": [
                {"ok": False, "error": "model foo discontinued on platform"},
                {"ok": False, "error": "discontinued"},
            ],
        }
        analysis = analyze_probe(report)
        self.assertTrue(analysis["all_discontinued"])
        self.assertIsNone(analysis["winner"])

    def test_blocked_when_discontinued_and_no_kie(self) -> None:
        from scripts.excalibur_blog_cover_image_preflight import is_cover_image_blocked

        analysis = {"winner": None, "all_discontinued": True}
        self.assertTrue(
            is_cover_image_blocked(analysis, kie_key_set=False, kie_credits_bad=False)
        )

    def test_not_blocked_when_kie_available(self) -> None:
        from scripts.excalibur_blog_cover_image_preflight import is_cover_image_blocked

        analysis = {"winner": None, "all_discontinued": True}
        self.assertFalse(
            is_cover_image_blocked(analysis, kie_key_set=True, kie_credits_bad=False)
        )

    def test_blocked_when_kie_credits_known_bad(self) -> None:
        from scripts.excalibur_blog_cover_image_preflight import is_cover_image_blocked

        analysis = {"winner": None, "all_discontinued": True}
        self.assertTrue(
            is_cover_image_blocked(analysis, kie_key_set=True, kie_credits_bad=True)
        )

    def test_kie_credits_from_cover_blocker(self) -> None:
        from scripts.excalibur_blog_cover_image_preflight import kie_credits_known_insufficient

        with tempfile.TemporaryDirectory() as tmp:
            article = Path(tmp)
            cover = article / "cover"
            cover.mkdir()
            (cover / "cover-blocker.json").write_text(
                json.dumps(
                    {
                        "blockers": [
                            {
                                "code": "KIE API BLOCKER",
                                "detail": "Kie fallback createTask HTTP 402 — Credits insufficient",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            self.assertTrue(kie_credits_known_insufficient(article))


class KieCreditsBlockerTests(unittest.TestCase):
    def test_is_kie_credits_error(self) -> None:
        import sys

        scripts = str(ROOT / "scripts")
        if scripts not in sys.path:
            sys.path.insert(0, scripts)
        from excalibur_blog_kie_gpt_image2_api import is_kie_credits_error

        self.assertTrue(is_kie_credits_error(402, '{"msg":"Credits insufficient"}'))
        self.assertTrue(is_kie_credits_error(400, "Credits insufficient for task"))
        self.assertFalse(is_kie_credits_error(500, "internal error"))


if __name__ == "__main__":
    unittest.main()
