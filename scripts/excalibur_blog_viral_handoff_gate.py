#!/usr/bin/env python3
"""BLOCK slot if ViralDzen handoff missing — no silent Scout without viral pass."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HANDOFF_NAME = "viral-dzen-handoff.json"
SLOT_DEFAULT = Path("memory/scout/viral-dzen-handoff.json")
MAX_HANDOFF_AGE_HOURS = 36


def _load_handoff(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"status": "BLOCK", "errors": [f"invalid JSON: {exc}"]}
    if not isinstance(data, dict):
        return {"status": "BLOCK", "errors": ["handoff must be a JSON object"]}
    return data


def check_handoff(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("status") != "PASS":
        errors.append("status must be PASS (ViralDzen slot must complete before Scout)")
    src = data.get("viral_source")
    if not isinstance(src, dict):
        errors.append("missing viral_source object")
    else:
        if not str(src.get("title") or "").strip():
            errors.append("viral_source.title empty")
        if not str(src.get("url") or "").strip().startswith("http"):
            errors.append("viral_source.url must be http(s)")
        if src.get("viral_score") is None:
            errors.append("viral_source.viral_score missing")
    if not str(data.get("guest_angle_ru") or "").strip():
        errors.append("guest_angle_ru empty")
    hub = data.get("discovered_hub")
    if not isinstance(hub, dict) or not str(hub.get("slug") or "").strip():
        errors.append("discovered_hub.slug missing (must be real Dzen topic slug from ViralDzen)")
    issued = str(data.get("issued_at") or "").strip()
    if not issued:
        errors.append("issued_at missing (re-run scripts/excalibur_blog_viraldzen_slot.py)")
    else:
        try:
            ts = datetime.fromisoformat(issued.replace("Z", "+00:00"))
            if ts.tzinfo is None:
                ts = ts.replace(tzinfo=timezone.utc)
            age_h = (datetime.now(timezone.utc) - ts.astimezone(timezone.utc)).total_seconds() / 3600
            if age_h > MAX_HANDOFF_AGE_HOURS:
                errors.append(f"issued_at stale ({age_h:.1f}h > {MAX_HANDOFF_AGE_HOURS}h)")
        except ValueError:
            errors.append("issued_at not valid ISO-8601")
    if not str(data.get("handoff_id") or "").strip():
        errors.append("handoff_id missing")
    return errors


def check_handoff_for_publish(root: Path, article_dir: Path) -> list[str]:
    """Publish path: handoff must live in article dir and match article.meta binding."""
    ad = article_dir if article_dir.is_absolute() else root / article_dir
    handoff_path = ad / HANDOFF_NAME
    errors: list[str] = []
    if not handoff_path.is_file():
        errors.append(
            f"VIRALDZEN BLOCKER: {HANDOFF_NAME} missing in article dir "
            "(ViralDzen slot must run before Scout/research_start)"
        )
        return errors
    data = _load_handoff(handoff_path)
    errors.extend(check_handoff(data))
    meta_path = ad / "article.meta.json"
    if not meta_path.is_file():
        errors.append("article.meta.json missing (viral handoff binding)")
        return errors
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        errors.append("article.meta.json invalid")
        return errors
    if str(meta.get("viral_handoff_id") or "") != str(data.get("handoff_id") or ""):
        errors.append("viral_handoff_id mismatch between article.meta and viral-dzen-handoff.json")
    if str(meta.get("viral_handoff_issued_at") or "") != str(data.get("issued_at") or ""):
        errors.append("viral_handoff_issued_at mismatch between article.meta and handoff")
    return errors


def resolve_handoff_path(
    *,
    root: Path,
    article_dir: Path | None,
    explicit: Path | None,
) -> Path | None:
    if explicit is not None:
        p = explicit if explicit.is_absolute() else root / explicit
        return p if p.is_file() else None
    if article_dir is not None:
        ad = article_dir if article_dir.is_absolute() else root / article_dir
        candidate = ad / HANDOFF_NAME
        if candidate.is_file():
            return candidate
    slot = root / SLOT_DEFAULT
    return slot if slot.is_file() else None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", type=Path, default=None)
    ap.add_argument("--handoff", type=Path, default=None)
    ap.add_argument("-o", "--output", type=Path, default=None)
    ap.add_argument(
        "--publish",
        action="store_true",
        help="Publish binding: require handoff in --article-dir + article.meta stamp",
    )
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    data: dict[str, Any] = {}
    handoff_path: Path | None = None
    if args.publish:
        if not args.article_dir:
            errors.append("--publish requires --article-dir")
        else:
            ad = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
            handoff_path = ad / HANDOFF_NAME
            errors.extend(check_handoff_for_publish(root, ad))
    else:
        handoff_path = resolve_handoff_path(
            root=root, article_dir=args.article_dir, explicit=args.handoff
        )
        if handoff_path is None:
            errors.append(
                f"VIRALDZEN BLOCKER: no {HANDOFF_NAME} "
                f"(run scripts/excalibur_blog_viraldzen_slot.py first)"
            )
        else:
            data = _load_handoff(handoff_path)
            errors.extend(check_handoff(data))

    report = {
        "gate": "viral-handoff",
        "status": "PASS" if not errors else "BLOCK",
        "handoff": str(handoff_path) if handoff_path else None,
        "errors": errors,
    }
    out = args.output
    if out is None and args.article_dir:
        ad = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
        out = ad / "viral-handoff-gate.json"
    if out is not None:
        out_path = out if out.is_absolute() else root / out
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
