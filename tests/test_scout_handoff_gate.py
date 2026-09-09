"""Scout handoff validation — wp_category_slugs and angle_rotation gates."""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_wordstat_gate import (
    handoff_has_angle_rotation,
    handoff_has_valid_wp_categories,
)


MINIMAL_HANDOFF = """# Scout handoff B99
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: test_hook | original: «тест»
wordstat_rework: probe «квартира посуточно тюмень» 3552 → final P0 «квартиры посуточно тюмень» 3552
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 3552
angle_rotation: checked last N=3 | burn-at-door skip: no | reason: new zalog angle
wp_category_slugs: posutochnaya-arenda, zalog-i-vyiezd
"""


class ScoutHandoffGateTest(unittest.TestCase):
    def test_valid_wp_category_slugs(self) -> None:
        ok, _ = handoff_has_valid_wp_categories(MINIMAL_HANDOFF, ROOT)
        self.assertTrue(ok)

    def test_rejects_abbreviated_wp_category_slugs(self) -> None:
        bad = MINIMAL_HANDOFF.replace(
            "wp_category_slugs: posutochnaya-arenda, zalog-i-vyiezd",
            "wp_category_slugs: posutochno, zalog",
        )
        ok, reason = handoff_has_valid_wp_categories(bad, ROOT)
        self.assertFalse(ok)
        self.assertIn("unknown wp_category_slugs", reason)

    def test_requires_angle_rotation(self) -> None:
        ok, _ = handoff_has_angle_rotation(MINIMAL_HANDOFF)
        self.assertTrue(ok)
        bad = MINIMAL_HANDOFF.replace(
            "angle_rotation: checked last N=3 | burn-at-door skip: no | reason: new zalog angle\n",
            "",
        )
        ok, reason = handoff_has_angle_rotation(bad)
        self.assertFalse(ok)
        self.assertIn("angle_rotation", reason)


if __name__ == "__main__":
    unittest.main()
