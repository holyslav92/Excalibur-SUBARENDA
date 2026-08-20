#!/usr/bin/env python3
"""Wordstat MCP-KV gate + Scout handoff validation for Excalibur BLOG."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


PARTIAL_RE = re.compile(r"wordstat\s*:\s*.*partial", re.IGNORECASE)
SKIP_RE = re.compile(r"wordstat\s*:\s*.*\bskip\b", re.IGNORECASE)
INVENTED_RE = re.compile(r"\b(approx|~|около|примерно|invented|выдум)\b", re.IGNORECASE)
FREQ_RE = re.compile(r"\d[\d\s]*")
MCP_KV_RE = re.compile(r"mcp[-_]?kv", re.IGNORECASE)


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_geo(root: Path) -> dict:
    return load_json(root / "memory/cover/wordstat-geo.json")


def wordstat_env_fallback_configured() -> bool:
    """Optional direct Yandex API env — secondary to MCP-KV in Cloud."""
    env = os.environ
    if env.get("WORDSTAT_API_KEY") and env.get("WORDSTAT_FOLDER_ID"):
        return True
    if env.get("YANDEX_SEARCH_API_KEY") and env.get("YANDEX_FOLDER_ID"):
        return True
    return bool(env.get("MCP_KV_TOKEN"))


def parse_handoff_field(handoff_text: str, key: str) -> str:
    prefix = f"{key}:"
    for line in handoff_text.splitlines():
        if line.strip().lower().startswith(prefix.lower()):
            return line.split(":", 1)[1].strip()
    return ""


def parse_handoff_wordstat(handoff_text: str) -> str:
    return parse_handoff_field(handoff_text, "wordstat")


def has_mcp_kv_marker(handoff_text: str, wordstat_value: str) -> bool:
    preflight = parse_handoff_field(handoff_text, "wordstat_preflight").casefold()
    if "wordstat_get_user_info" in preflight and "ok" in preflight:
        return True
    if MCP_KV_RE.search(wordstat_value):
        return True
    if MCP_KV_RE.search(handoff_text):
        return True
    return False


def has_buyer_p0_phrase(value: str, geo: dict) -> bool:
    low = value.casefold()
    for seed in geo.get("p0_buyer_seed_phrases") or []:
        if str(seed).casefold() in low:
            return True
    return False


def is_brand_vanity_only(value: str, geo: dict) -> bool:
    low = value.casefold()
    buyer = has_buyer_p0_phrase(value, geo)
    if buyer:
        return False
    for vanity in geo.get("brand_vanity_queries_not_p0") or []:
        if str(vanity).casefold() in low:
            return True
    if "риэлтор" in low and "тюмен" in low:
        return True
    return False


def handoff_has_klyshin_hook(handoff_text: str) -> tuple[bool, str]:
    value = parse_handoff_field(handoff_text, "klyshin_hook")
    if not value:
        return False, "klyshin_hook field missing in handoff (required: original Klyshin hook id/angle)"
    if "original" not in value.casefold() and "|" not in value:
        return False, "klyshin_hook must log original hook (e.g. klyshin_hook: <id> | original: «…»)"
    return True, value


def handoff_has_rework_log(handoff_text: str) -> tuple[bool, str]:
    value = parse_handoff_field(handoff_text, "wordstat_rework")
    if not value:
        return False, "wordstat_rework field missing (log probe → rework → final P0 cluster)"
    if not FREQ_RE.search(value):
        return False, "wordstat_rework must include numeric frequencies from MCP-KV probes"
    return True, value


def handoff_has_live_wordstat(handoff_text: str, geo: dict) -> tuple[bool, str]:
    value = parse_handoff_wordstat(handoff_text)
    if not value:
        return False, "wordstat field missing in handoff"
    if SKIP_RE.search(f"wordstat: {value}"):
        return False, "wordstat: skip is forbidden for Scout"
    if PARTIAL_RE.search(f"wordstat: {value}"):
        return False, "wordstat PARTIAL is forbidden — need live MCP-KV top phrases + frequencies"
    if INVENTED_RE.search(value):
        return False, "wordstat handoff must not contain approx/invented markers"
    if not FREQ_RE.search(value):
        return False, "wordstat handoff must include numeric frequencies from MCP-KV"
    if not has_mcp_kv_marker(handoff_text, value):
        return False, "handoff must cite mcp_kv live pull (wordstat_preflight or mcp_kv in wordstat line)"
    low = value.casefold()
    required_ids = [str(x) for x in (geo.get("scout_required_region_ids") or [])]
    if not any(rid in value for rid in required_ids) and "тюмен" not in low:
        return False, "wordstat handoff must show Tyumen region ids from wordstat-geo.json"
    if is_brand_vanity_only(value, geo):
        return False, (
            "P0 topic must come from buyer-demand queries (купить квартиру / новостройки / "
            "ипотека / ЕГРН…), not brand vanity «риэлтор тюмень» only"
        )
    if not has_buyer_p0_phrase(value, geo):
        return False, "wordstat handoff must include at least one P0 buyer seed phrase with frequency"
    return True, value


def cmd_config(root: Path) -> int:
    geo = load_geo(root)
    ids = geo.get("scout_required_region_ids") or []
    print("OK wordstat primary path: MCP-KV (server MCP-KV)")
    print(f"OK tools: {', '.join(geo.get('mcp_tools') or [])}")
    print(f"OK tenant regions: {ids} (compare RU {geo.get('russia_region_id')})")
    print("NOTE Scout preflight: CallMcpTool wordstat_get_user_info — FAIL if tool missing")
    print("NOTE Scout canon: Klyshin hook → Wordstat probe → rework for demand (not skip-if-weak)")
    print("NOTE handoff fields: klyshin_hook (original) + wordstat_rework + wordstat (final P0)")
    rework = geo.get("rework_vocabulary") or []
    if rework:
        print(f"NOTE rework vocabulary: {', '.join(str(x) for x in rework[:8])}…")
    if wordstat_env_fallback_configured():
        print("OK optional env fallback present (MCP_KV_TOKEN or Yandex API keys)")
    else:
        print("NOTE no Wordstat env in shell — expected when MCP-KV wired in Cloud Automation Tools")
    return 0


def cmd_handoff(root: Path, args: argparse.Namespace) -> int:
    handoff_path = Path(args.handoff)
    if not handoff_path.is_absolute():
        handoff_path = root / handoff_path
    if not handoff_path.is_file():
        print(f"FAIL handoff not found: {handoff_path}", file=sys.stderr)
        return 1

    geo = load_geo(root)
    text = handoff_path.read_text(encoding="utf-8")
    ok_klyshin, reason_k = handoff_has_klyshin_hook(text)
    if not ok_klyshin:
        print(f"FAIL SCOUT WORDSTAT GATE: {reason_k}", file=sys.stderr)
        return 1
    ok_rework, reason_r = handoff_has_rework_log(text)
    if not ok_rework:
        print(f"FAIL SCOUT WORDSTAT GATE: {reason_r}", file=sys.stderr)
        return 1
    ok_handoff, reason = handoff_has_live_wordstat(text, geo)
    if not ok_handoff:
        print(f"FAIL SCOUT WORDSTAT GATE: {reason}", file=sys.stderr)
        return 1

    ids = geo.get("scout_required_region_ids") or []
    print(f"OK scout wordstat handoff (mcp_kv live, klyshin+rework log); region_ids={ids}")
    return 0


def cmd_doctor(root: Path) -> int:
    geo_path = root / "memory/cover/wordstat-geo.json"
    if not geo_path.is_file():
        print("FAIL wordstat-geo.json missing", file=sys.stderr)
        return 1
    geo = load_geo(root)
    if geo.get("primary_source") != "mcp-kv":
        print("FAIL wordstat-geo primary_source must be mcp-kv", file=sys.stderr)
        return 1
    ids = geo.get("scout_required_region_ids") or []
    if 55 not in ids or 11176 not in ids:
        print("FAIL wordstat-geo must include Tyumen city 55 and oblast 11176", file=sys.stderr)
        return 1
    if not geo.get("region_ids_verified_via"):
        print("FAIL wordstat-geo missing region_ids_verified_via", file=sys.stderr)
        return 1
    if not geo.get("p0_buyer_seed_phrases"):
        print("FAIL wordstat-geo missing p0_buyer_seed_phrases", file=sys.stderr)
        return 1
    if geo.get("russia_region_id") != 225:
        print("FAIL wordstat-geo russia_region_id must be 225", file=sys.stderr)
        return 1
    print("OK wordstat-geo canon (MCP-KV primary)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Wordstat MCP-KV gate and Scout handoff validation")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("config", help="Print Wordstat MCP-KV path expectations for Scout")
    handoff = sub.add_parser("handoff", help="Validate Scout handoff wordstat field")
    handoff.add_argument("--handoff", default=".cursor/excalibur-blog-handoff.md")
    sub.add_parser("doctor", help="Validate wordstat-geo canon")
    args = parser.parse_args()
    root = project_root()
    if args.command == "config":
        return cmd_config(root)
    if args.command == "handoff":
        return cmd_handoff(root, args)
    if args.command == "doctor":
        return cmd_doctor(root)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
