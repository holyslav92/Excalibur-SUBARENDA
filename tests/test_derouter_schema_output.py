"""Schema role output validation for Derouter chat (INC B31)."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_derouter_opus_chat import (
    schema_derouter_output_errors,
    strip_jsonld_fences,
)  # noqa: E402


class DerouterSchemaOutputTests(unittest.TestCase):
    def test_valid_blogposting_json(self) -> None:
        text = '{"@type":"BlogPosting","headline":"Test"}'
        self.assertEqual(schema_derouter_output_errors(text), [])

    def test_valid_blogposting_in_graph(self) -> None:
        text = (
            '{"@graph":[{"@type":"BlogPosting","headline":"T"},'
            '{"@type":"FAQPage","mainEntity":[]}]}'
        )
        self.assertEqual(schema_derouter_output_errors(text), [])

    def test_meta_refusal_prose_rejected(self) -> None:
        text = (
            "Файл schema.jsonld должен быть создан через "
            "excalibur_blog_derouter_opus_chat.py --role schema."
        )
        errors = schema_derouter_output_errors(text)
        self.assertTrue(errors)
        self.assertIn("meta-refusal", errors[0])

    def test_non_json_rejected(self) -> None:
        errors = schema_derouter_output_errors("not json at all")
        self.assertTrue(errors)
        self.assertIn("not valid JSON", errors[0])

    def test_json_without_blogposting_rejected(self) -> None:
        errors = schema_derouter_output_errors('{"@type":"WebPage"}')
        self.assertEqual(errors, ["JSON lacks @type BlogPosting"])

    def test_strip_markdown_fences(self) -> None:
        wrapped = '```json\n{"@type":"BlogPosting"}\n```'
        self.assertEqual(strip_jsonld_fences(wrapped), '{"@type":"BlogPosting"}')
        self.assertEqual(schema_derouter_output_errors(wrapped), [])


if __name__ == "__main__":
    unittest.main()
