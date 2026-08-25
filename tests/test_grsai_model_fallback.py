#!/usr/bin/env python3
"""Grsai model policy: PRIMARY_MODEL_ID only, vip permanently disabled."""

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
    VIP_DISABLED,
    create_draw_payload,
    ensure_2k_canvas,
    generate_image_with_model_fallback,
    is_2k_request_rejected,
    is_vip_model,
    primary_model,
    vip_fallback_model,
)


def _png_bytes(width: int, height: int) -> bytes:
    from PIL import Image

    buf = io.BytesIO()
    Image.new("RGB", (width, height), color=(200, 180, 160)).save(buf, format="PNG")
    return buf.getvalue()


VIP_MODEL = PRIMARY_MODEL_ID + "-vip"


class GrsaiModelFallbackTests(unittest.TestCase):
    def test_vip_disabled_flag(self) -> None:
        self.assertTrue(VIP_DISABLED)

    def test_primary_default(self) -> None:
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("GRSAI_IMAGE_MODEL", None)
            self.assertEqual(primary_model(), PRIMARY_MODEL_ID)

    def test_forbid_vip_as_primary_env(self) -> None:
        with patch.dict(os.environ, {"GRSAI_IMAGE_MODEL": VIP_MODEL}):
            with self.assertRaises(GrsaiApiError):
                primary_model()

    def test_vip_fallback_raises(self) -> None:
        with self.assertRaises(GrsaiApiError) as ctx:
            vip_fallback_model(PRIMARY_MODEL_ID)
        self.assertIn("vip_disabled", str(ctx.exception))

    def test_is_vip_model_detects_suffix(self) -> None:
        self.assertTrue(is_vip_model(VIP_MODEL))
        self.assertFalse(is_vip_model(PRIMARY_MODEL_ID))

    def test_primary_success_no_vip(self) -> None:
        native_2k = _png_bytes(2048, 1152)

        def fake_generate(*, model: str, **kwargs):  # noqa: ANN003
            self.assertEqual(model, PRIMARY_MODEL_ID)
            self.assertNotIn("-vip", model)
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
        self.assertTrue(meta["vip_disabled"])
        self.assertIsNone(meta["vip_trigger"])
        self.assertEqual(data, native_2k)

    def test_explicit_size_retry_on_undersized(self) -> None:
        calls: list[tuple[str, bool]] = []

        def fake_generate(*, model: str, explicit_size: bool = False, **kwargs):  # noqa: ANN003
            calls.append((model, explicit_size))
            self.assertEqual(model, PRIMARY_MODEL_ID)
            if not explicit_size:
                raise Grsai2KNotMetError(
                    "undersized 1672x941",
                    native_size=(1672, 941),
                    image_bytes=_png_bytes(1672, 941),
                )
            return _png_bytes(2048, 1152), {
                "host": "grsaiapi.com",
                "model": model,
                "delivery": "native_2k",
            }

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
        self.assertEqual(len(calls), 2)
        self.assertFalse(calls[0][1])
        self.assertTrue(calls[1][1])
        self.assertEqual(meta["model_succeeded"], PRIMARY_MODEL_ID)
        self.assertFalse(meta["used_vip_fallback"])
        self.assertTrue(meta["vip_disabled"])
        self.assertNotIn("-vip", meta["model_succeeded"])

    def test_ship_native_when_retry_still_undersized(self) -> None:
        undersized = _png_bytes(1672, 941)
        calls: list[str] = []

        def fake_generate(*, model: str, **kwargs):  # noqa: ANN003
            calls.append(model)
            self.assertEqual(model, PRIMARY_MODEL_ID)
            raise Grsai2KNotMetError(
                "undersized 1672x941",
                native_size=(1672, 941),
                image_bytes=undersized,
            )

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
        self.assertEqual(len(calls), 2)
        self.assertTrue(all(m == PRIMARY_MODEL_ID for m in calls))
        self.assertEqual(meta["model_succeeded"], PRIMARY_MODEL_ID)
        self.assertEqual(meta["delivery"], "native_undersized_vip_disabled")
        self.assertTrue(meta["vip_disabled"])
        self.assertEqual(meta["shipped_native"], "1672x941")
        self.assertEqual(data, undersized)

    def test_api_failure_no_vip(self) -> None:
        calls: list[str] = []

        def fake_generate(*, model: str, **kwargs):  # noqa: ANN003
            calls.append(model)
            raise GrsaiApiError("timeout on all hosts")

        with patch(
            "excalibur_blog_grsai_gpt_image2_api.generate_image",
            side_effect=fake_generate,
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
        self.assertEqual(calls, [PRIMARY_MODEL_ID])
        self.assertNotIn(VIP_MODEL, calls)

    def test_vip_payload_forbidden(self) -> None:
        with self.assertRaises(GrsaiApiError):
            create_draw_payload(
                prompt="probe",
                model=VIP_MODEL,
                aspect_ratio="16:9",
                quality="high",
            )

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

    def test_explicit_size_payload(self) -> None:
        payload = create_draw_payload(
            prompt="probe",
            model=PRIMARY_MODEL_ID,
            aspect_ratio="16:9",
            quality="high",
            explicit_size=True,
        )
        self.assertIn("size", payload)
        self.assertNotIn("aspectRatio", payload)
        self.assertEqual(payload["size"], "2048x1152")

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

    def test_ensure_2k_accept_undersized(self) -> None:
        raw = _png_bytes(1672, 941)
        out, meta = ensure_2k_canvas(raw, model=PRIMARY_MODEL_ID, accept_undersized=True)
        self.assertEqual(out, raw)
        self.assertEqual(meta["delivery"], "native_undersized_vip_disabled")
        self.assertTrue(meta["vip_disabled"])
        self.assertEqual(meta["shipped_native"], "1672x941")


if __name__ == "__main__":
    unittest.main()
