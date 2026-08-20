"""Unit tests for Derouter role→tier model resolution."""
from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]


class DerouterResolveModelTests(unittest.TestCase):
    def test_powerful_role_requires_opus_family(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import resolve_model

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shared").mkdir()
            (root / "shared" / "tenant-config.json").write_text(
                json.dumps(
                    {
                        "writing_model": {
                            "powerful": {
                                "model": "claude-opus-5",
                                "model_env": "DEROUTER_OPUS_MODEL",
                                "roles": ["writer", "sol", "title", "scout"],
                            },
                            "utility": {
                                "model": "gpt-5.6-terra",
                                "model_env": "DEROUTER_TERRA_MODEL",
                                "roles": ["research", "description", "cover-text", "schema", "cover-scene"],
                            },
                        }
                    }
                ),
                encoding="utf-8",
            )
            model, tier = resolve_model("writer", None, root)
            self.assertEqual(tier, "powerful")
            self.assertEqual(model, "claude-opus-5")

            model, tier = resolve_model("research", None, root)
            self.assertEqual(tier, "utility")
            self.assertEqual(model, "gpt-5.6-terra")

    def test_legacy_text_model_does_not_override_powerful_to_non_opus(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import resolve_model

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shared").mkdir()
            (root / "shared" / "tenant-config.json").write_text(
                json.dumps(
                    {
                        "writing_model": {
                            "powerful": {"model": "claude-opus-5", "roles": ["writer"]},
                            "utility": {"model": "gpt-5.6-terra", "roles": ["research"]},
                        }
                    }
                ),
                encoding="utf-8",
            )
            with mock.patch.dict(os.environ, {"DEROUTER_TEXT_MODEL": "gpt-5.6-terra"}, clear=False):
                model, tier = resolve_model("writer", None, root)
                self.assertEqual(tier, "powerful")
                self.assertIn("opus", model.lower())


if __name__ == "__main__":
    unittest.main()
