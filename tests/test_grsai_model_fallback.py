#!/usr/bin/env python3
"""Grsai model policy: non-vip 2K first, vip on 2K fail or API fail."""

from __future__ import annotations

import io
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_grsai_gpt_image2_api import (  # noqa: E402
    Grsai2KNotMetError,
    GrsaiApiError,
    MIN_LONG_SIDE_2K,
    NATIVE_2K_CLASS_MIN_LONG_SIDE,
    PRIMARY_MODEL_ID,
    VIP_FALLBACK_MODEL_ID,
    create_draw_payload,
    economy_skip_primary,
    ensure_2k_canvas,
    generate_image_vip_economy,
    generate_image_with_model_fallback,
    is_2k_request_rejected,
    primary_model,
    vip_fallback_model,
)


def _png_bytes(width: int, height: int) -> bytes:
    from PIL import Image

    buf = io.BytesIO()
    Image.new("RGB", (width, height), color=(200, 180, 160)).save(buf, format="PNG")
    return buf.getvalue()


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

    def test_primary_success_no_vip(self) -> None:
        native_2k = _png_bytes(2048, 1152)

        def fake_generate(*, model: str, **kwargs):  # noqa: ANN003
            self.assertEqual(model, PRIMARY_MODEL_ID)
            return native_2k, {
                "host": "grsaiapi.com",
                "model": model,
                "native_long_side": 2048,
                "delivery": "native_2k",
            }

        with patch(
            "excalibur_blog_grsai_gpt_image2_api.generate_image",
            side_effect=fake_generate,
        ):
            data, meta = generate_image_with_model_fallback(
                image_input={"prompt": "probe", "resolution": "2K"},
                api_key="test-key",
                quality="high",
                poll_interval=1,
                max_wait=10,
                timeout=5,
            )
        self.assertEqual(meta["model_succeeded"], PRIMARY_MODEL_ID)
        self.assertFalse(meta["used_vip_fallback"])
        self.assertIsNone(meta["vip_trigger"])
        self.assertEqual(data, native_2k)

    def test_vip_on_2k_not_met(self) -> None:
        calls: list[str] = []

        def fake_generate(*, model: str, **kwargs):  # noqa: ANN003
            calls.append(model)
            if model == PRIMARY_MODEL_ID:
                raise Grsai2KNotMetError("undersized 1672x941", native_size=(1672, 941))
            return _png_bytes(2048, 1152), {"host": "grsaiapi.com", "model": model}

        with patch(
            "excalibur_blog_grsai_gpt_image2_api.generate_image",
            side_effect=fake_generate,
        ):
            _data, meta = generate_image_with_model_fallback(
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
        self.assertEqual(meta["vip_trigger"], "2k_not_possible_on_primary")

    def test_vip_on_api_failure(self) -> None:
        calls: list[str] = []

        def fake_generate(*, model: str, **kwargs):  # noqa: ANN003
            calls.append(model)
            if model == PRIMARY_MODEL_ID:
                raise GrsaiApiError("timeout on all hosts")
            return _png_bytes(2048, 1152), {"host": "grsaiapi.com", "model": model}

        with patch(
            "excalibur_blog_grsai_gpt_image2_api.generate_image",
            side_effect=fake_generate,
        ):
            _data, meta = generate_image_with_model_fallback(
                image_input={"prompt": "probe"},
                api_key="test-key",
                quality="high",
                poll_interval=1,
                max_wait=10,
                timeout=5,
            )
        self.assertEqual(calls, [PRIMARY_MODEL_ID, VIP_FALLBACK_MODEL_ID])
        self.assertEqual(meta["vip_trigger"], "api_failure")

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
        payload = create_draw_payload(
            prompt="probe",
            model=VIP_FALLBACK_MODEL_ID,
            aspect_ratio="16:9",
            quality="high",
        )
        self.assertIn("size", payload)
        self.assertNotIn("aspectRatio", payload)
        self.assertEqual(payload["size"], "2048x1152")

    def test_primary_payload_requests_2k(self) -> None:
        payload = create_draw_payload(
            prompt="probe",
            model=PRIMARY_MODEL_ID,
            aspect_ratio="16:9",
            quality="high",
            resolution="2K",
        )
        self.assertEqual(payload.get("aspectRatio"), "16:9")
        self.assertEqual(payload.get("resolution"), "2K")
        self.assertNotIn("size", payload)

    def test_is_2k_request_rejected(self) -> None:
        self.assertTrue(is_2k_request_rejected(GrsaiApiError("HTTP 400: invalid size parameter")))
        self.assertFalse(is_2k_request_rejected(GrsaiApiError("HTTP 500: internal error")))

    def test_ensure_2k_native_pass(self) -> None:
        raw = _png_bytes(2048, 1152)
        out, meta = ensure_2k_canvas(raw, model=PRIMARY_MODEL_ID)
        self.assertEqual(out, raw)
        self.assertEqual(meta["delivery"], "native_2k")
        self.assertEqual(meta["native_long_side"], 2048)

    def test_ensure_2k_class_upscale(self) -> None:
        raw = _png_bytes(1920, 1080)
        out, meta = ensure_2k_canvas(raw, model=PRIMARY_MODEL_ID)
        self.assertEqual(meta["delivery"], "upscaled_2k_class")
        from PIL import Image

        with Image.open(io.BytesIO(out)) as img:
            self.assertEqual(img.size, (2048, 1152))

    def test_ensure_2k_undersized_raises(self) -> None:
        raw = _png_bytes(1672, 941)
        with self.assertRaises(Grsai2KNotMetError) as ctx:
            ensure_2k_canvas(raw, model=PRIMARY_MODEL_ID)
        self.assertEqual(ctx.exception.native_size, (1672, 941))
        self.assertLess(1672, NATIVE_2K_CLASS_MIN_LONG_SIDE)
        self.assertLess(1672, MIN_LONG_SIDE_2K)

    def test_economy_skip_primary_16_9(self) -> None:
        with patch.dict(
            os.environ,
            {"GRSAI_VIP_ECONOMY": "1", "GRSAI_FORBID_VIP": ""},
            clear=False,
        ):
            os.environ.pop("GRSAI_FORBID_VIP", None)
            self.assertTrue(economy_skip_primary({"aspect_ratio": "16:9"}))
            self.assertFalse(economy_skip_primary({"aspect_ratio": "1:1"}))

    def test_vip_economy_single_call(self) -> None:
        calls: list[str] = []

        def fake_generate(*, model: str, **kwargs):  # noqa: ANN003
            calls.append(model)
            return _png_bytes(2048, 1152), {"host": "grsaiapi.com", "model": model, "delivery": "native_2k"}

        with patch.dict(os.environ, {"GRSAI_VIP_ECONOMY": "1"}, clear=False):
            with patch(
                "excalibur_blog_grsai_gpt_image2_api.generate_image",
                side_effect=fake_generate,
            ):
                _data, meta = generate_image_vip_economy(
                    image_input={"prompt": "probe", "aspect_ratio": "16:9"},
                    api_key="test-key",
                    quality="high",
                    poll_interval=1,
                    max_wait=10,
                    timeout=5,
                )
        self.assertEqual(calls, [VIP_FALLBACK_MODEL_ID])
        self.assertEqual(meta["model_succeeded"], VIP_FALLBACK_MODEL_ID)
        self.assertTrue(meta["used_vip_fallback"])
        self.assertEqual(meta["vip_trigger"], "economy_skip_primary_16_9")


if __name__ == "__main__":
    unittest.main()
