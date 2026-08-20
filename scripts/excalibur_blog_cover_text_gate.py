#!/usr/bin/env python3
"""Validate cover/cover-text.json — exact Russian inscriptions for the quad cover.

The image model must render ONLY these strings. This gate enforces:
- hook 2-8 words, Cyrillic, highlight word inside hook;
- sticky <=5 words;
- labels 2-6 per inline panel, each <=4 words;
- no Latin letters except whitelisted brands (Cursor, Make, MCP, AI, ...).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from excalibur_blog_quad_slots import INLINE_SLOT_KEYS, active_inline_keys, inline_count_from_tenant

BRAND_WHITELIST = {
    "cursor", "make", "mcp", "ai", "openai", "google", "microsoft", "nvidia",
    "meta", "claude", "grok", "qwen", "gmail", "sheets", "deepmind", "hugging",
    "face", "n8n", "llm", "vps", "api", "ui", "x", "rsc", "hark",
}

CYRILLIC_RE = re.compile(r"[А-Яа-яЁё]")
LATIN_WORD_RE = re.compile(r"[A-Za-z]+")


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _latin_violations(text: str) -> list[str]:
    out: list[str] = []
    for word in LATIN_WORD_RE.findall(text or ""):
        if word.lower() in BRAND_WHITELIST:
            continue
        if len(word) <= 2:  # single letters / acronyms like «C2» fragments
            continue
        out.append(word)
    return out


def _check_text(errors: list[str], errors_out: list[str], field: str, value: str,
                *, min_words: int, max_words: int, max_chars: int) -> None:
    value = (value or "").strip()
    if not value:
        errors.append(f"{field} empty")
        errors_out.append(field)
        return
    words = value.split()
    if not (min_words <= len(words) <= max_words):
        errors.append(f"{field}: {len(words)} words, need {min_words}-{max_words}")
    if len(value) > max_chars:
        errors.append(f"{field}: {len(value)} chars > {max_chars}")
    bad = _latin_violations(value)
    if bad:
        errors.append(f"{field}: Latin words not in brand whitelist: {bad}")
    elif not CYRILLIC_RE.search(value) and not LATIN_WORD_RE.findall(value):
        errors.append(f"{field}: empty of readable text — write Russian")


def validate_cover_text(data: dict, inline_count: int = 7) -> dict:
    errors: list[str] = []
    error_fields: list[str] = []

    hook = str(data.get("hook") or "").strip()
    _check_text(errors, error_fields, "hook", hook, min_words=2, max_words=8, max_chars=64)

    highlight = str(data.get("highlight") or "").strip()
    if not highlight:
        errors.append("highlight empty")
    elif highlight.casefold() not in hook.casefold():
        errors.append(f"highlight {highlight!r} is not a word inside hook {hook!r}")

    sticky = str(data.get("sticky") or "").strip()
    if sticky:
        _check_text(errors, error_fields, "sticky", sticky, min_words=1, max_words=5, max_chars=32)

    labels = data.get("inline_labels") or {}
    for key in active_inline_keys(inline_count):
        panel_labels = labels.get(key) or []
        if not isinstance(panel_labels, list) or not (2 <= len(panel_labels) <= 6):
            errors.append(f"{key}: labels must be 2-6 short strings, got {panel_labels!r}")
            continue
        for lbl in panel_labels:
            _check_text(errors, error_fields, f"{key}.label", str(lbl),
                        min_words=1, max_words=4, max_chars=28)

    return {
        "status": "PASS" if not errors else "BLOCK",
        "errors": errors,
        "error_fields": sorted(set(error_fields)),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("-o", "--output", default="cover-text-gate.json",
                    help="Bare filename written inside article_dir")
    args = ap.parse_args()
    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    text_path = article_dir / "cover" / "cover-text.json"
    if not text_path.is_file():
        print(f"❌ COVER TEXT BLOCKER: {text_path} missing — Cover-text agent must write it",
              file=sys.stderr)
        return 1

    try:
        data = json.loads(text_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"❌ COVER TEXT BLOCKER: bad JSON: {exc}", file=sys.stderr)
        return 1

    tenant_path = root / "shared/tenant-config.json"
    tenant = json.loads(tenant_path.read_text(encoding="utf-8")) if tenant_path.is_file() else {}
    inline_count = inline_count_from_tenant(tenant)

    verdict = validate_cover_text(data, inline_count=inline_count)
    out_name = Path(args.output).name
    out_path = article_dir / out_name
    out_path.write_text(json.dumps(verdict, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
    print(f"OK gate={out_path} status={verdict['status']}")
    for err in verdict["errors"]:
        print(f"  - {err}")
    return 0 if verdict["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
