"""Unit tests for Derouter role→tier model resolution."""
from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]

NON_WRITER_TEXT_ROLES = (
    "scout",
    "title",
    "sol",
    "research",
    "description",
    "cover-text",
    "schema",
    "cover-scene",
)


class DerouterResolveModelTests(unittest.TestCase):
    def test_only_writer_on_powerful_tier(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import (
            POWERFUL_ROLES,
            UTILITY_ROLES,
            resolve_model,
        )

        self.assertEqual(POWERFUL_ROLES, frozenset({"writer"}))
        self.assertEqual(
            UTILITY_ROLES,
            frozenset(
                {
                    "scout",
                    "title",
                    "sol",
                    "research",
                    "description",
                    "cover-text",
                    "schema",
                    "cover-scene",
                    "viral-pick",
                }
            ),
        )

        model, tier = resolve_model("writer", None, ROOT)
        self.assertEqual(tier, "powerful")
        self.assertIn("opus", model.lower())

        for role in NON_WRITER_TEXT_ROLES:
            model, tier = resolve_model(role, None, ROOT)
            self.assertEqual(tier, "utility", role)
            self.assertNotIn("opus", model.lower(), role)
            self.assertEqual(model, "gpt-6-luna", role)

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
                                "roles": ["writer"],
                            },
                            "utility": {
                                "model": "gpt-6-luna",
                                "model_env": "DEROUTER_UTILITY_MODEL",
                                "roles": list(NON_WRITER_TEXT_ROLES),
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
            self.assertEqual(model, "gpt-6-luna")

    def test_validate_rejects_non_writer_on_opus_tier(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import (
            DerouterChatError,
            validate_writing_model_opus_writer_only,
        )

        with self.assertRaises(DerouterChatError):
            validate_writing_model_opus_writer_only(
                {"powerful": {"roles": ["writer", "sol", "title"]}, "utility": {"roles": ["scout"]}}
            )

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
                            "utility": {"model": "gpt-6-luna", "roles": ["research"]},
                        }
                    }
                ),
                encoding="utf-8",
            )
            with mock.patch.dict(os.environ, {"DEROUTER_TEXT_MODEL": "gpt-6-luna"}, clear=False):
                model, tier = resolve_model("writer", None, root)
                self.assertEqual(tier, "powerful")
                self.assertIn("opus", model.lower())

    def test_utility_rejects_legacy_terra_model(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import DerouterChatError, resolve_model

        with self.assertRaises(DerouterChatError):
            resolve_model("scout", "gpt-5.6-terra", ROOT)


class TenantWritingModelRoutingTests(unittest.TestCase):
    def test_tenant_config_opus_writer_only(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        writing = tenant.get("writing_model") or {}
        powerful_roles = set((writing.get("powerful") or {}).get("roles") or [])
        utility_roles = set((writing.get("utility") or {}).get("roles") or [])

        self.assertEqual(powerful_roles, {"writer"})
        self.assertIn("Opus 5.5", writing.get("canon_note") or "")
        self.assertFalse(powerful_roles.intersection({"scout", "title", "sol"}))
        self.assertTrue(set(NON_WRITER_TEXT_ROLES).issubset(utility_roles))


if __name__ == "__main__":
    unittest.main()
