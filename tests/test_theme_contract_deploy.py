"""Theme contract deploy path probing (INC B21)."""
from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_theme_contract_deploy import (
    faq_skip_guard_applied,
    patch_functions,
    patch_single,
    single_needs_excalibur_guards,
    theme_dir_candidates,
    theme_has_legacy_faq_hook,
)


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


    def test_patch_functions_skip_when_no_legacy_faq_hook(self) -> None:
        """INC B32: refactored theme has schema hook only — no FAQ bounds error."""
        text = (
            "<?php\n"
            "function excalibur_blog_output_schema_jsonld() {}\n"
            "add_action( 'wp_head', 'excalibur_blog_output_schema_jsonld', 20 );\n"
        )
        self.assertFalse(theme_has_legacy_faq_hook(text))
        patched = patch_functions(text)
        self.assertEqual(patched, text)

    def test_patch_single_skip_modern_layout(self) -> None:
        modern = "<?php\n the_content();\n"
        self.assertFalse(single_needs_excalibur_guards(modern))
        self.assertEqual(patch_single(modern), modern)

    def test_faq_skip_guard_detects_applied_patch(self) -> None:
        legacy = (
            "function custom_theme_add_faq_to_single() {\n"
            "if ( is_single() && 'post' === get_post_type() "
            "&& ! ( '1' === get_post_meta( get_the_ID(), "
            "'_excalibur_blog_skip_theme_faq', true ) "
            "&& '1' === get_post_meta( get_the_ID(), "
            "'_excalibur_blog_skip_engagement_quiz', true ) ) ) {\n"
            "}\n"
        )
        self.assertTrue(faq_skip_guard_applied(legacy))


if __name__ == "__main__":
    unittest.main()
