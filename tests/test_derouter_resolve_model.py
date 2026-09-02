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
            self.assertIn("terra", model.lower(), role)

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
                                "model": "gpt-5.6-terra",
                                "model_env": "DEROUTER_TERRA_MODEL",
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
            self.assertEqual(model, "gpt-5.6-terra")

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


class OneShotOwnerOverrideTests(unittest.TestCase):
    def test_one_shot_bypasses_family_check_but_not_defaults(self) -> None:
        from scripts.excalibur_blog_derouter_opus_chat import (
            DerouterChatError,
            resolve_model,
        )

        # Разовый override: точный id без проверки семейства tier
        model, tier = resolve_model("writer", "claude-fable-5-1", ROOT, one_shot=True)
        self.assertEqual((model, tier), ("claude-fable-5-1", "powerful"))
        model, tier = resolve_model("sol", "claude-fable-5-1", ROOT, one_shot=True)
        self.assertEqual((model, tier), ("claude-fable-5-1", "utility"))

        # Без флага тот же id по-прежнему блокируется — дефолт не изменился
        with self.assertRaises(DerouterChatError):
            resolve_model("writer", "claude-fable-5-1", ROOT)
        with self.assertRaises(DerouterChatError):
            resolve_model("writer", "", ROOT, one_shot=True)

    def test_one_shot_disables_alias_fallback(self) -> None:
        from scripts import excalibur_blog_derouter_opus_chat as mod

        seen: list[str] = []

        def fake_chat(*, system_prompt, user_prompt, model, timeout, max_retries):
            seen.append(model)
            raise mod.DerouterChatError("model not found", status=404)

        with mock.patch.object(mod, "call_derouter_chat", fake_chat):
            with self.assertRaises(mod.DerouterChatError):
                mod.call_derouter_with_aliases(
                    system_prompt="s",
                    user_prompt="u",
                    tier="powerful",
                    model="claude-fable-5-1",
                    timeout=10,
                    max_retries=0,
                    exact_model_only=True,
                )
        self.assertEqual(seen, ["claude-fable-5-1"])


class TenantWritingModelRoutingTests(unittest.TestCase):
    def test_tenant_config_opus_writer_only(self) -> None:
        tenant = json.loads((ROOT / "shared/tenant-config.json").read_text(encoding="utf-8"))
        writing = tenant.get("writing_model") or {}
        powerful_roles = set((writing.get("powerful") or {}).get("roles") or [])
        utility_roles = set((writing.get("utility") or {}).get("roles") or [])

        self.assertEqual(powerful_roles, {"writer"})
        self.assertEqual(writing.get("canon_note"), "Opus 5 = Writer only; everything else Terra")
        self.assertFalse(powerful_roles.intersection({"scout", "title", "sol"}))
        self.assertTrue(set(NON_WRITER_TEXT_ROLES).issubset(utility_roles))


if __name__ == "__main__":
    unittest.main()
