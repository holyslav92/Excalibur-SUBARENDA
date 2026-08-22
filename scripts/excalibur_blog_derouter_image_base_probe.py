#!/usr/bin/env python3
"""Probe Derouter image API bases; log status + short error (never print API key)."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_derouter_gpt_image2_api import (  # noqa: E402
    DEFAULT_IMAGE_API_BASE_CANDIDATES,
    DEFAULT_SIZE_2K_16_9,
    DerouterApiError,
    call_generations,
    default_model,
    image_api_base_candidates,
    parse_image_response,
)


def probe_one(*, base: str, api_key: str, model: str, size: str, timeout: int) -> dict:
    host = base.split("//", 1)[-1].split("/", 1)[0]
    try:
        parsed = call_generations(
            base_url=base,
            api_key=api_key,
            model=model,
            prompt="tiny probe: bright collage, empty top-right pad, no logo, no text",
            size=size,
            quality="auto",
            timeout=timeout,
        )
        image_bytes = parse_image_response(parsed)
        return {
            "base": base,
            "host": host,
            "status": 200,
            "ok": True,
            "bytes": len(image_bytes),
            "error": "",
        }
    except DerouterApiError as exc:
        msg = str(exc)
        status = 400
        if "HTTP " in msg:
            try:
                status = int(msg.split("HTTP ", 1)[1].split(":", 1)[0])
            except ValueError:
                status = 400
        return {
            "base": base,
            "host": host,
            "status": status,
            "ok": False,
            "bytes": 0,
            "error": msg[:500],
        }


def main() -> int:
    ap = argparse.ArgumentParser(description="Probe Derouter image API base URLs")
    ap.add_argument("--size", default=os.environ.get("DEROUTER_IMAGE_SIZE", DEFAULT_SIZE_2K_16_9))
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument(
        "--report",
        default="memory/blog/derouter-image-base-probe.json",
        help="write JSON report (relative to repo root)",
    )
    args = ap.parse_args()

    api_key = os.environ.get("DEROUTER_API_KEY", "").strip()
    if not api_key:
        print("DEROUTER_API_KEY missing", file=sys.stderr)
        return 1

    try:
        model = default_model()
    except DerouterApiError as exc:
        print(f"DEROUTER IMAGE MODEL missing: {exc}", file=sys.stderr)
        return 1

    bases = image_api_base_candidates()
    results = [
        probe_one(base=base, api_key=api_key, model=model, size=args.size, timeout=args.timeout)
        for base in bases
    ]
    winner = next((r for r in results if r.get("ok")), None)
    report = {
        "probed_at": datetime.now(timezone.utc).isoformat(),
        "model_env": "DEROUTER_IMAGE_MODEL",
        "size": args.size,
        "candidates_default": DEFAULT_IMAGE_API_BASE_CANDIDATES,
        "candidates_effective": bases,
        "winner": winner["base"] if winner else None,
        "results": results,
    }
    out = ROOT / args.report
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for row in results:
        mark = "OK" if row.get("ok") else f"HTTP {row.get('status')}"
        err = (row.get("error") or "")[:120]
        print(f"{mark:8} {row['host']:28} {err}")

    if winner:
        print(f"\nWINNER: {winner['base']} ({winner['bytes']} bytes)")
        return 0
    print("\nNO working image base found.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
