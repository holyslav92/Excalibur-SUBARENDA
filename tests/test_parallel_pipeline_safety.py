"""Tests for idempotent handoff fragment merge."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ParallelPipelineSafetyTest(unittest.TestCase):
    def test_handoff_merge_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            handoff = root / "handoff.md"
            handoff.write_text("# handoff\n", encoding="utf-8")
            fragments = root / "fragments"
            fragments.mkdir()
            for role, marker in (("cover", "COVER"), ("schema", "SCHEMA")):
                (fragments / f"{role}.md").write_text(
                    f"---\nrole: excalibur-blog-{role}\nstatus: PASS\n"
                    "completed_at: 2026-07-20T00:00:00Z\nincident_report: none\n---\n"
                    f"=== EXCALIBUR BLOG {marker} ===\n",
                    encoding="utf-8",
                )
            cmd = [
                sys.executable, str(ROOT / "scripts/excalibur_blog_handoff_merge.py"),
                "--handoff", str(handoff), "--fragments-dir", str(fragments),
                "--wave", "cover,schema",
            ]
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            subprocess.run(cmd, check=True, capture_output=True, text=True)
            text = handoff.read_text(encoding="utf-8")
            self.assertEqual(text.count("=== EXCALIBUR BLOG COVER ==="), 1)
            self.assertEqual(text.count("=== EXCALIBUR BLOG SCHEMA ==="), 1)


if __name__ == "__main__":
    unittest.main()
