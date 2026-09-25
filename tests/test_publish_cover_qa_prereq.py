"""Publish preflight must run cover QA gate script (not JSON alone)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class PublishCoverQaPrereqTest(unittest.TestCase):
    def test_wp_publish_preflight_invokes_cover_qa_gate(self) -> None:
        src = (ROOT / "scripts/excalibur_blog_wp_publish.py").read_text(encoding="utf-8")
        self.assertIn("excalibur_blog_cover_qa_gate.py", src)
        self.assertIn("cover-qa-gate failed", src)


if __name__ == "__main__":
    unittest.main()
