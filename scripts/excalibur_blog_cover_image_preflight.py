#!/usr/bin/env python3
"""Preflight Cover image providers before quad batch generation.

Reads (or optionally refreshes) memory/blog/derouter-image-base-probe.json and
fails fast when Derouter image generation is discontinued on all bases and Kie
is missing or known insufficient — avoids wasting Cover-scene / quad-prompt work.

See shared/derouter-gpt-image-api-contract.md.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROBE_REPORT = "memory/blog/derouter-image-base-probe.json"
DEFAULT_MAX_AGE_HOURS = 6


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return ROOT


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_probe_time(raw: str) -> datetime | None:
    text = str(raw or "").strip()
    if not text:
        return None
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None


def probe_is_stale(report: dict[str, Any], *, max_age_hours: float) -> bool:
    probed = parse_probe_time(str(report.get("probed_at") or ""))
    if probed is None:
        return True
    age = datetime.now(timezone.utc) - probed.astimezone(timezone.utc)
    return age.total_seconds() > max(0.0, max_age_hours) * 3600


def analyze_probe(report: dict[str, Any]) -> dict[str, Any]:
    results = report.get("results")
    if not isinstance(results, list):
        results = []
    winner = report.get("winner")
    errors = [str(r.get("error") or "") for r in results if isinstance(r, dict)]
    all_discontinued = bool(results) and not winner and all(
        "discontinued" in err.lower() for err in errors
    )
    return {
        "winner": winner,
        "results_count": len(results),
        "all_discontinued": all_discontinued,
        "probed_at": report.get("probed_at"),
    }


def run_probe(root: Path, *, report_rel: str) -> int:
    script = root / "scripts" / "excalibur_blog_derouter_image_base_probe.py"
    cmd = [sys.executable, str(script), "--report", report_rel]
    proc = subprocess.run(cmd, cwd=str(root))
    return proc.returncode


def kie_credits_known_insufficient(article_dir: Path | None) -> bool:
    if article_dir is None:
        return False
    blocker = article_dir / "cover" / "cover-blocker.json"
    if not blocker.is_file():
        return False
    try:
        data = load_json(blocker)
    except json.JSONDecodeError:
        return False
    for item in data.get("blockers") or []:
        if not isinstance(item, dict):
            continue
        detail = str(item.get("detail") or "").lower()
        code = str(item.get("code") or "").lower()
        if "402" in detail or "credits insufficient" in detail or "kie" in code and "402" in detail:
            return True
    return False


def build_blocker_payload(
    *,
    topic_id: str,
    article_dir: Path,
    analysis: dict[str, Any],
    kie_key_set: bool,
    kie_credits_bad: bool,
) -> dict[str, Any]:
    blockers: list[dict[str, str]] = []
    if analysis.get("all_discontinued"):
        blockers.append(
            {
                "code": "DEROUTER IMAGE BLOCKER",
                "detail": (
                    "DEROUTER_IMAGE_MODEL image generation discontinued on all Derouter bases "
                    "(see memory/blog/derouter-image-base-probe.json)"
                ),
            }
        )
    if not kie_key_set:
        blockers.append(
            {
                "code": "KIE API BLOCKER",
                "detail": "KIE_API_KEY missing — no Kie fallback while Derouter image is down",
            }
        )
    elif kie_credits_bad:
        blockers.append(
            {
                "code": "KIE CREDITS BLOCKER",
                "detail": "Kie fallback createTask HTTP 402 — credits insufficient",
            }
        )

    remediation_parts = []
    if analysis.get("all_discontinued"):
        remediation_parts.append(
            "Set a working DEROUTER_IMAGE_MODEL (GET /v1/models) or DEROUTER_IMAGE_API_BASE per "
            "shared/derouter-gpt-image-api-contract.md"
        )
    if not kie_key_set or kie_credits_bad:
        remediation_parts.append("Top up Kie credits or set KIE_API_KEY in Cloud Secrets")

    return {
        "status": "BLOCKER",
        "topic_id": topic_id,
        "article_dir": str(article_dir.relative_to(project_root()))
        if article_dir.is_relative_to(project_root())
        else str(article_dir),
        "blockers": blockers,
        "preflight": {
            "probed_at": analysis.get("probed_at"),
            "derouter_winner": analysis.get("winner"),
            "all_discontinued": analysis.get("all_discontinued"),
            "kie_key_set": kie_key_set,
            "kie_credits_known_insufficient": kie_credits_bad,
        },
        "remediation": "; ".join(remediation_parts) or "Run derouter image base probe and fix providers",
    }


def is_cover_image_blocked(
    analysis: dict[str, Any],
    *,
    kie_key_set: bool,
    kie_credits_bad: bool,
) -> bool:
    if analysis.get("winner"):
        return False
    if not analysis.get("all_discontinued"):
        return False
    if not kie_key_set:
        return True
    return kie_credits_bad


def main() -> int:
    ap = argparse.ArgumentParser(description="Preflight Cover image API providers")
    ap.add_argument("--article-dir", help="Optional article dir for cover-blocker.json")
    ap.add_argument("--topic-id", default="", help="Topic id for blocker payload (e.g. B03)")
    ap.add_argument("--probe-report", default=DEFAULT_PROBE_REPORT)
    ap.add_argument("--max-age-hours", type=float, default=DEFAULT_MAX_AGE_HOURS)
    ap.add_argument("--probe", action="store_true", help="Run live Derouter base probe first")
    ap.add_argument(
        "--write-blocker",
        action="store_true",
        help="Write cover/cover-blocker.json when blocked (requires --article-dir)",
    )
    args = ap.parse_args()

    root = project_root()
    report_path = Path(args.probe_report)
    if not report_path.is_absolute():
        report_path = root / report_path

    if args.probe or not report_path.is_file():
        rc = run_probe(root, report_rel=args.probe_report)
        if rc not in {0, 2}:
            print("COVER IMAGE PREFLIGHT BLOCKER: derouter image probe failed to run", file=sys.stderr)
            return 1

    if not report_path.is_file():
        print(
            "COVER IMAGE PREFLIGHT BLOCKER: probe report missing — run "
            "scripts/excalibur_blog_derouter_image_base_probe.py",
            file=sys.stderr,
        )
        return 1

    try:
        report = load_json(report_path)
    except json.JSONDecodeError as exc:
        print(f"COVER IMAGE PREFLIGHT BLOCKER: invalid probe JSON: {exc}", file=sys.stderr)
        return 1

    if probe_is_stale(report, max_age_hours=float(args.max_age_hours)) and not args.probe:
        print(
            f"WARN probe report older than {args.max_age_hours}h — rerun with --probe before Cover",
            flush=True,
        )

    analysis = analyze_probe(report)
    kie_key_set = bool(os.environ.get("KIE_API_KEY", "").strip())

    article_dir: Path | None = None
    if args.article_dir:
        article_dir = Path(args.article_dir)
        if not article_dir.is_absolute():
            article_dir = root / article_dir

    kie_credits_bad = kie_credits_known_insufficient(article_dir)
    blocked = is_cover_image_blocked(
        analysis, kie_key_set=kie_key_set, kie_credits_bad=kie_credits_bad
    )

    if analysis.get("winner"):
        print(f"OK derouter image base: {analysis['winner']}")
        return 0

    if analysis.get("all_discontinued"):
        print("WARN Derouter image discontinued on all probed bases", flush=True)
        if kie_key_set and not kie_credits_bad:
            print("OK Kie fallback available (credits not pre-checked) — Cover may proceed via Kie")
            return 0

    if blocked:
        print("COVER IMAGE PREFLIGHT BLOCKER", file=sys.stderr)
        if args.write_blocker and article_dir is not None:
            topic_id = args.topic_id.strip() or "n/a"
            payload = build_blocker_payload(
                topic_id=topic_id,
                article_dir=article_dir,
                analysis=analysis,
                kie_key_set=kie_key_set,
                kie_credits_bad=kie_credits_bad,
            )
            out = article_dir / "cover" / "cover-blocker.json"
            save_json(out, payload)
            print(f"Wrote {out}", flush=True)
        return 2

    if not analysis.get("results_count"):
        print("COVER IMAGE PREFLIGHT BLOCKER: empty probe results", file=sys.stderr)
        return 2

    print("WARN no Derouter winner — investigate probe report before Cover")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
