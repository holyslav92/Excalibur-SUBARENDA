#!/usr/bin/env python3
"""Hard gate: ViralDzen angle must not repeat recent live wounds / H1 shapes."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from excalibur_blog_viral_topic_repeat import check_topic_repeat, probe_text_from_article_dir

HANDOFF_NAME = "viral-dzen-handoff.json"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", type=Path, required=True)
    ap.add_argument("--text", default="", help="Optional probe override")
    ap.add_argument("-o", "--output", type=Path, default=None)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    ad = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    handoff_path = ad / HANDOFF_NAME
    errors: list[str] = []
    if not handoff_path.is_file():
        errors.append(f"{HANDOFF_NAME} missing in article dir")
    probe = args.text.strip() or probe_text_from_article_dir(root, ad)
    errors.extend(check_topic_repeat(root, probe, article_dir=ad))
    report = {
        "gate": "viral-topic-repeat",
        "status": "PASS" if not errors else "BLOCK",
        "article_dir": str(ad.relative_to(root) if ad.is_relative_to(root) else ad),
        "errors": errors,
    }
    out = args.output or ad / "viral-topic-repeat-gate.json"
    out_path = out if out.is_absolute() else root / out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
