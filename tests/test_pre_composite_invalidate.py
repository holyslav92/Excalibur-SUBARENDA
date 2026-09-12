"""Regression: stale pre-composite must not restore over regenned panels (INC B17)."""
from __future__ import annotations

import shutil
import sys
import tempfile
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_brand_logo_composite import (  # noqa: E402
    PRE_COMPOSITE_DIRNAME,
    invalidate_pre_composite_panel,
    restore_or_snapshot_pre_composite,
    snapshot_pre_composite,
)


class PreCompositeInvalidateTest(unittest.TestCase):
    def test_invalidate_removes_stale_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            pre_dir = Path(tmp) / PRE_COMPOSITE_DIRNAME
            pre_dir.mkdir()
            stale = pre_dir / "inline-04.png"
            stale.write_bytes(b"stale")
            self.assertTrue(invalidate_pre_composite_panel(pre_dir, "inline-04.png"))
            self.assertFalse(stale.is_file())
            self.assertFalse(invalidate_pre_composite_panel(pre_dir, "inline-04.png"))

    def test_restore_skips_when_pre_composite_invalidated(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cover = Path(tmp) / "cover"
            pre_dir = cover / PRE_COMPOSITE_DIRNAME
            cover.mkdir()
            panel = cover / "inline-04.png"
            panel.write_bytes(b"fresh-regen")
            pre_dir.mkdir()
            (pre_dir / "inline-04.png").write_bytes(b"stale-art")
            time.sleep(0.02)
            panel.write_bytes(b"fresh-regen-v2")
            invalidate_pre_composite_panel(pre_dir, panel.name)
            _, created = restore_or_snapshot_pre_composite(panel, pre_dir)
            self.assertTrue(created)
            self.assertEqual(panel.read_bytes(), b"fresh-regen-v2")
            self.assertEqual((pre_dir / "inline-04.png").read_bytes(), b"fresh-regen-v2")

    def test_restore_generation_only_when_pre_exists(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cover = Path(tmp) / "cover"
            pre_dir = cover / PRE_COMPOSITE_DIRNAME
            cover.mkdir()
            panel = cover / "cover.png"
            panel.write_bytes(b"generation-only")
            pre_path, created = snapshot_pre_composite(panel, pre_dir)
            self.assertTrue(created)
            panel.write_bytes(b"with-factory-logo")
            _, created2 = restore_or_snapshot_pre_composite(panel, pre_dir)
            self.assertFalse(created2)
            self.assertEqual(panel.read_bytes(), b"generation-only")
            self.assertEqual(pre_path.read_bytes(), b"generation-only")


if __name__ == "__main__":
    unittest.main()
