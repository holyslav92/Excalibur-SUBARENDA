#!/usr/bin/env python3
"""Scout wound saturation gate — dobry_dom_voice_reset_v1."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from excalibur_blog_editorial_anti_clone import (  # noqa: E402
    EDITORIAL_CANON_ID,
    check_scout_wound_not_saturated,
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--handoff",
        type=Path,
        default=Path(".cursor/excalibur-blog-handoff.md"),
        help="Scout handoff markdown",
    )
    ap.add_argument("-o", "--output", type=Path, default=Path("scout-wound-gate.json"))
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    handoff_path = args.handoff if args.handoff.is_absolute() else root / args.handoff
    if not handoff_path.is_file():
        print(f"BLOCKER: handoff not found: {handoff_path}", file=sys.stderr)
        return 2
    text = handoff_path.read_text(encoding="utf-8")
    errors = check_scout_wound_not_saturated(text, root=root)
    report = {
        "gate": "scout-wound",
        "status": "PASS" if not errors else "BLOCK",
        "editorial_canon": EDITORIAL_CANON_ID,
        "handoff": str(handoff_path),
        "errors": errors,
    }
    out = args.output if args.output.is_absolute() else root / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
