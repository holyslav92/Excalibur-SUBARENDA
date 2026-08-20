#!/usr/bin/env python3
"""Remove resurrected memory/topics/ junk. Topics pool is deleted permanently.

Scout must not write blog-topics.md. New topics go via:
  research_start.py --topic-id B111 --title "short title"
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def purge_topics_dir(root: Path, *, dry_run: bool = False) -> dict[str, int]:
    path = root / "memory" / "topics"
    if not path.exists():
        return {"existed": 0, "removed": 0}
    file_count = sum(1 for p in path.rglob("*") if p.is_file())
    if not dry_run:
        shutil.rmtree(path)
    return {"existed": 1, "removed": 1, "files": file_count}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    stats = purge_topics_dir(project_root(), dry_run=args.dry_run)
    print(
        f"OK topics_dir_existed={stats.get('existed', 0)} "
        f"removed={stats.get('removed', 0)} "
        f"files={stats.get('files', 0)} "
        f"dry_run={args.dry_run}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
