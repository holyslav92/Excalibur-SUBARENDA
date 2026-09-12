#!/usr/bin/env python3
"""Pad-clear TR zone on no-logo inline panels before drawn_logo_gate / Cover-QA retry."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from excalibur_blog_brand_logo_composite import (
    PRE_COMPOSITE_DIRNAME,
    invalidate_pre_composite_panel,
    load_tenant_logo_config,
    resolve_inline_logo_slots,
)
from excalibur_blog_cover_standalone_apply import pad_clear_top_right_scene_clone
from excalibur_blog_quad_slots import INLINE_FILES, active_inline_keys, inline_count_from_manifest


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def no_logo_inline_files(article_dir: Path, root: Path) -> list[Path]:
    manifest_path = article_dir / "cover" / "quad-manifest.json"
    if not manifest_path.is_file():
        return []
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    inline_count = inline_count_from_manifest(manifest)
    cfg = load_tenant_logo_config(root)
    logo_files = set(resolve_inline_logo_slots(article_dir, cfg))
    cover_dir = article_dir / "cover"
    files: list[Path] = []
    for key in active_inline_keys(inline_count):
        rel = INLINE_FILES.get(key)
        if not rel or rel in logo_files:
            continue
        path = cover_dir / rel
        if path.is_file():
            files.append(path)
    return files


def pad_clear_no_logo_inlines(article_dir: Path, root: Path) -> dict:
    cleared: list[dict] = []
    pre_dir = article_dir / "cover" / PRE_COMPOSITE_DIRNAME
    for path in no_logo_inline_files(article_dir, root):
        passes = pad_clear_top_right_scene_clone(path)
        pre_invalidated = invalidate_pre_composite_panel(pre_dir, path.name)
        cleared.append(
            {
                "file": str(path.relative_to(article_dir)),
                "pad_clear_passes": passes,
                "pre_composite_invalidated": pre_invalidated,
            }
        )
    return {
        "article_dir": str(article_dir),
        "panels_cleared": cleared,
        "count": len(cleared),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    args = ap.parse_args()
    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    if not article_dir.is_dir():
        print(f"BLOCKER missing article dir: {article_dir}", file=sys.stderr)
        return 1
    report = pad_clear_no_logo_inlines(article_dir, root)
    out = article_dir / "cover" / "inline-pad-clear-report.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"OK inline pad-clear count={report['count']} "
        f"files={[x['file'] for x in report['panels_cleared']]}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
