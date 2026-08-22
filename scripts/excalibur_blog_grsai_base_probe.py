#!/usr/bin/env python3
"""Проба Grsai draw API (global + china fallback); лог без ключа."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_grsai_gpt_image2_api import (  # noqa: E402
    FALLBACK_BASE,
    PRIMARY_BASE,
    GrsaiApiError,
    api_base_candidates,
    create_task,
    default_model,
    download_image,
    poll_result,
    upscale_canvas_if_needed,
)


def probe_one(*, base: str, api_key: str, model: str, timeout: int, max_wait: int) -> dict:
    host = base.split("//", 1)[-1].split("/", 1)[0]
    try:
        task_id = create_task(
            base_url=base,
            api_key=api_key,
            model=model,
            prompt="tiny probe: bright collage, empty top-right pad, no logo, no text",
            aspect_ratio="16:9",
            quality="high",
            images=None,
            timeout=timeout,
        )
        image_url = poll_result(
            base_url=base,
            api_key=api_key,
            task_id=task_id,
            poll_interval=5,
            max_wait=max_wait,
            timeout=timeout,
        )
        raw = download_image(image_url, timeout=timeout)
        image_bytes = upscale_canvas_if_needed(raw)
        return {
            "base": base,
            "host": host,
            "status": 200,
            "ok": True,
            "task_id": task_id,
            "bytes": len(image_bytes),
            "error": "",
        }
    except GrsaiApiError as exc:
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
            "task_id": "",
            "bytes": 0,
            "error": msg[:500],
        }


def main() -> int:
    ap = argparse.ArgumentParser(description="Probe Grsai draw API base URLs")
    ap.add_argument("--model", default=os.environ.get("GRSAI_IMAGE_MODEL", ""))
    ap.add_argument("--timeout", type=int, default=120)
    ap.add_argument("--max-wait", type=int, default=300)
    ap.add_argument(
        "--report",
        default="memory/blog/grsai-image-base-probe.json",
        help="write JSON report (relative to repo root)",
    )
    args = ap.parse_args()

    api_key = os.environ.get("GRSAI_API_KEY", "").strip()
    if not api_key:
        print("GRSAI_API_KEY missing", file=sys.stderr)
        return 1

    model = str(args.model or default_model()).strip()
    bases = api_base_candidates(primary=PRIMARY_BASE, fallback=FALLBACK_BASE)
    results = [
        probe_one(base=base, api_key=api_key, model=model, timeout=args.timeout, max_wait=args.max_wait)
        for base in bases
    ]
    winner = next((r for r in results if r.get("ok")), None)
    report = {
        "probed_at": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "api": "POST /v1/draw/completions + POST /v1/draw/result",
        "webhook": "-1",
        "candidates_default": [PRIMARY_BASE, FALLBACK_BASE],
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
    print("\nNO working Grsai base found.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
