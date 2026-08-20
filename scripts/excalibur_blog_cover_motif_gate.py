#!/usr/bin/env python3
"""Anti-repeat gate for cover motifs (rolling 14-day window)."""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalize_token(value: str) -> str:
    return " ".join(str(value or "").casefold().split())


def parse_entry_date(raw: str) -> date | None:
    text = str(raw or "").strip()
    if not text:
        return None
    try:
        if "T" in text:
            return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
        return date.fromisoformat(text[:10])
    except ValueError:
        return None


def prune_entries(entries: list[dict], *, window_days: int, today: date) -> list[dict]:
    cutoff = today - timedelta(days=window_days - 1)
    kept: list[dict] = []
    for entry in entries:
        entry_date = parse_entry_date(str(entry.get("date") or ""))
        if entry_date is None or entry_date >= cutoff:
            kept.append(entry)
    return kept


def motif_payload_from_args(args: argparse.Namespace) -> dict[str, str]:
    fields = ("composition", "location", "meme", "prop_set", "sticker_set", "joke")
    payload: dict[str, str] = {}
    for field in fields:
        value = normalize_token(getattr(args, field, "") or "")
        if value:
            payload[field] = value
    return payload


def find_collisions(
    motifs: dict[str, str],
    entries: list[dict],
    *,
    topic_id: str,
) -> list[dict]:
    hits: list[dict] = []
    topic_norm = normalize_token(topic_id)
    for entry in entries:
        if normalize_token(str(entry.get("topic_id") or "")) == topic_norm:
            continue
        prior = entry.get("motifs") or {}
        for field, value in motifs.items():
            prior_value = normalize_token(str(prior.get(field) or ""))
            if prior_value and prior_value == value:
                hits.append(
                    {
                        "field": field,
                        "value": value,
                        "prior_topic_id": entry.get("topic_id"),
                        "prior_date": entry.get("date"),
                    }
                )
    return hits


def cmd_check(root: Path, args: argparse.Namespace) -> int:
    log_path = root / "memory/cover/used-motifs.json"
    canon_path = root / "memory/cover/cover-canon.json"
    if not log_path.is_file():
        print(f"FAIL used-motifs log missing: {log_path}", file=sys.stderr)
        return 1
    if not canon_path.is_file():
        print(f"FAIL cover-canon missing: {canon_path}", file=sys.stderr)
        return 1

    data = load_json(log_path)
    window_days = int(data.get("window_days") or 14)
    today = date.today()
    entries = prune_entries(list(data.get("entries") or []), window_days=window_days, today=today)
    motifs = motif_payload_from_args(args)
    if not motifs:
        print("FAIL motif gate: pass at least one --composition/--location/--meme/--prop-set/--sticker-set/--joke", file=sys.stderr)
        return 1

    collisions = find_collisions(motifs, entries, topic_id=args.topic_id or "")
    if collisions:
        print("FAIL COVER MOTIF COLLISION (14-day anti-repeat):", file=sys.stderr)
        for hit in collisions:
            print(
                f"  - {hit['field']}={hit['value']!r} repeats {hit['prior_topic_id']} ({hit['prior_date']})",
                file=sys.stderr,
            )
        return 1

    print(f"OK motif gate topic_id={args.topic_id} fields={','.join(motifs)} window={window_days}d")
    return 0


def cmd_record(root: Path, args: argparse.Namespace) -> int:
    log_path = root / "memory/cover/used-motifs.json"
    data = load_json(log_path) if log_path.is_file() else {"schema_version": 1, "window_days": 14, "entries": []}
    window_days = int(data.get("window_days") or 14)
    today = date.today()
    motifs = motif_payload_from_args(args)
    if not motifs:
        print("FAIL motif record: empty motifs", file=sys.stderr)
        return 1

    entries = prune_entries(list(data.get("entries") or []), window_days=window_days, today=today)
    topic_id = str(args.topic_id or "").strip()
    entries = [e for e in entries if normalize_token(str(e.get("topic_id") or "")) != normalize_token(topic_id)]
    entries.append(
        {
            "date": datetime.now(timezone.utc).date().isoformat(),
            "topic_id": topic_id,
            "slug": str(args.slug or "").strip(),
            "motifs": motifs,
        }
    )
    data["entries"] = entries
    save_json(log_path, data)
    print(f"OK motif recorded topic_id={topic_id} entries={len(entries)}")
    return 0


def cmd_doctor(root: Path) -> int:
    log_path = root / "memory/cover/used-motifs.json"
    canon_path = root / "memory/cover/cover-canon.json"
    ok = True
    for path in (log_path, canon_path):
        if not path.is_file():
            print(f"FAIL missing {path.relative_to(root)}", file=sys.stderr)
            ok = False
    if not ok:
        return 1
    data = load_json(log_path)
    if int(data.get("window_days") or 0) != 14:
        print("FAIL used-motifs window_days must be 14", file=sys.stderr)
        return 1
    if not isinstance(data.get("entries"), list):
        print("FAIL used-motifs entries must be a list", file=sys.stderr)
        return 1
    print("OK cover motif log schema")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Cover motif anti-repeat gate (14 days)")
    sub = parser.add_subparsers(dest="command", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--topic-id", default="")
    common.add_argument("--slug", default="")
    common.add_argument("--composition", default="")
    common.add_argument("--location", default="")
    common.add_argument("--meme", default="")
    common.add_argument("--prop-set", dest="prop_set", default="")
    common.add_argument("--sticker-set", dest="sticker_set", default="")
    common.add_argument("--joke", default="")

    sub.add_parser("check", parents=[common], help="Reject collisions before generate")
    sub.add_parser("record", parents=[common], help="Append motifs after successful cover")
    sub.add_parser("doctor", help="Validate log schema")

    args = parser.parse_args()
    root = project_root()
    if args.command == "doctor":
        return cmd_doctor(root)
    if args.command == "check":
        return cmd_check(root, args)
    if args.command == "record":
        return cmd_record(root, args)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
