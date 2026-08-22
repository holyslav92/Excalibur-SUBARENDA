#!/usr/bin/env python3
"""Grsai model policy: primary tier first, one vip per sheet."""

from __future__ import annotations

import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_grsai_gpt_image2_api import (  # noqa: E402
    GrsaiApiError,
    PRIMARY_MODEL_ID,
    VIP_FALLBACK_MODEL_ID,
    generate_image_with_model_fallback,
    primary_model,
    vip_fallback_model,
)


class GrsaiModelFallbackTests(unittest.TestCase):
    def test_primary_default(self) -> None:
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("GRSAI_IMAGE_MODEL", None)
            self.assertEqual(primary_model(), PRIMARY_MODEL_ID)

    def test_forbid_vip_as_primary_env(self) -> None:
        with patch.dict(os.environ, {"GRSAI_IMAGE_MODEL": VIP_FALLBACK_MODEL_ID}):
            with self.assertRaises(GrsaiApiError):
                primary_model()

    def test_vip_fallback_id(self) -> None:
        self.assertEqual(vip_fallback_model(PRIMARY_MODEL_ID), VIP_FALLBACK_MODEL_ID)

    def test_primary_then_vip_on_failure(self) -> None:
        calls: list[str] = []

        def fake_generate(*, model: str, **kwargs):  # noqa: ANN003
            calls.append(model)
            if model == PRIMARY_MODEL_ID:
                raise GrsaiApiError("simulated primary fail")
            return b"png", {"host": "grsaiapi.com", "model": model}

        with patch(
            "excalibur_blog_grsai_gpt_image2_api.generate_image",
            side_effect=fake_generate,
        ):
            data, meta = generate_image_with_model_fallback(
                image_input={"prompt": "probe"},
                api_key="test-key",
                quality="high",
                poll_interval=1,
                max_wait=10,
                timeout=5,
            )
        self.assertEqual(calls, [PRIMARY_MODEL_ID, VIP_FALLBACK_MODEL_ID])
        self.assertEqual(meta["model_succeeded"], VIP_FALLBACK_MODEL_ID)
        self.assertTrue(meta["used_vip_fallback"])
        self.assertEqual(data, b"png")

    def test_no_second_vip(self) -> None:
        def always_fail(*, model: str, **kwargs):  # noqa: ANN003
            raise GrsaiApiError(f"fail {model}")

        with patch(
            "excalibur_blog_grsai_gpt_image2_api.generate_image",
            side_effect=always_fail,
        ):
            with self.assertRaises(GrsaiApiError):
                generate_image_with_model_fallback(
                    image_input={"prompt": "probe"},
                    api_key="test-key",
                    quality="high",
                    poll_interval=1,
                    max_wait=10,
                    timeout=5,
                )


    def test_vip_payload_uses_pixel_size(self) -> None:
        from excalibur_blog_grsai_gpt_image2_api import create_draw_payload

        payload = create_draw_payload(
            prompt="probe",
            model=VIP_FALLBACK_MODEL_ID,
            aspect_ratio="16:9",
            quality="high",
        )
        self.assertIn("size", payload)
        self.assertNotIn("aspectRatio", payload)
        self.assertEqual(payload["size"], "2048x1152")

    def test_primary_payload_uses_aspect_ratio(self) -> None:
        from excalibur_blog_grsai_gpt_image2_api import create_draw_payload

        payload = create_draw_payload(
            prompt="probe",
            model=PRIMARY_MODEL_ID,
            aspect_ratio="16:9",
            quality="high",
        )
        self.assertEqual(payload.get("aspectRatio"), "16:9")
        self.assertNotIn("size", payload)


if __name__ == "__main__":
    unittest.main()
