"""Theme contract deploy path probing (INC B21)."""
from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_theme_contract_deploy import theme_dir_candidates


class ThemeContractDeployTests(unittest.TestCase):
    def test_theme_dir_candidates_default_slugs(self) -> None:
        with mock.patch.dict(os.environ, {}, clear=True):
            slugs = theme_dir_candidates()
        self.assertEqual(slugs, ["kov4eg-mcp-theme", "theme"])

    def test_theme_dir_candidates_env_override_first(self) -> None:
        with mock.patch.dict(os.environ, {"WP_THEME_SLUG": "custom-theme"}, clear=False):
            slugs = theme_dir_candidates()
        self.assertEqual(slugs[0], "custom-theme")
        self.assertIn("theme", slugs)


if __name__ == "__main__":
    unittest.main()
