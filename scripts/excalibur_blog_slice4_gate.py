#!/usr/bin/env python3
"""HARD gate: dobry_dom_gen_only_human_v1 — ONE Grsai 2K draw, PIL slice into 4 tiles.

Cover = tile[0] + factory logo paste only. Inlines = tiles[1..3]. No second canvas,
no standalone cover batch, no 8-frame pipeline, no overlay scripts.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from excalibur_blog_quad_slots import GEN_ONLY_HUMAN_CANON_ID, ONE_2K_SLICE4_CANON_ID, uses_gen_only_human, uses_one_2k_slice4

SLICE4_BATCH_NAMES = frozenset(
    {
        "slice4-mcp-batch.json",
        "quad-mcp-batch.json",
    }
)

FORBIDDEN_EXTRA_BATCHES = frozenset(
    {
        "cover-mcp-batch.json",
        "quad-mcp-batch-01.json",
        "quad-mcp-batch-02.json",
    }
)

FORBIDDEN_OVERLAY_STAMPS = (
    "poster-composite-stamp.json",
)

FORBIDDEN_RESULT_SUFFIXES = (
    "cover-mcp-result.json",
    "quad-mcp-result-01.json",
    "quad-mcp-result-02.json",
)

GRSAI_RESULT_RE = re.compile(r"grsai|draw-api|draw/completions", re.I)


def _load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def _grsai_draw_count(cover_dir: Path) -> int:
    count = 0
    for path in sorted(cover_dir.glob("*-mcp-result*.json")):
        data = _load_json(path)
        blob = json.dumps(data, ensure_ascii=False).casefold()
        if GRSAI_RESULT_RE.search(blob) or data.get("status") == "ok":
            count += 1
    return count


def _batch_files_present(cover_dir: Path) -> list[str]:
    names: list[str] = []
    for path in sorted(cover_dir.glob("*-mcp-batch*.json")):
        names.append(path.name)
    return names


def check_article_dir(article_dir: Path, *, root: Path | None = None) -> dict[str, Any]:
    root = root or Path(__file__).resolve().parents[1]
    errors: list[str] = []
    checks: list[str] = []

    if not uses_one_2k_slice4(root):
        return {
            "gate": "slice4",
            "status": "SKIP",
            "canon": GEN_ONLY_HUMAN_CANON_ID,
            "errors": [],
            "checks_run": ["canon_not_active"],
            "article_dir": str(article_dir),
        }

    cover_dir = article_dir / "cover"
    checks.append("slice4_canon_active")

    batch_names = _batch_files_present(cover_dir) if cover_dir.is_dir() else []
    if batch_names:
        checks.append("batch_files")
        allowed = [n for n in batch_names if n in SLICE4_BATCH_NAMES]
        forbidden = [n for n in batch_names if n in FORBIDDEN_EXTRA_BATCHES]
        if forbidden:
            errors.append(
                f"slice4: forbidden extra batch file(s): {', '.join(forbidden)} "
                "(ONE draw only — no cover-mcp / quad-mcp-batch-01|02)"
            )
        if len(allowed) > 1:
            errors.append(
                f"slice4: multiple allowed batches {allowed} — exactly ONE Grsai call per article"
            )
        if batch_names and not allowed and not forbidden:
            errors.append(f"slice4: unexpected batch file(s): {', '.join(batch_names)}")

    if cover_dir.is_dir():
        for name in FORBIDDEN_RESULT_SUFFIXES:
            if (cover_dir / name).is_file():
                errors.append(f"slice4: forbidden legacy result {name} (8-frame / standalone cover)")
        if uses_gen_only_human(root):
            checks.append("gen_only_no_overlay")
            for stamp in FORBIDDEN_OVERLAY_STAMPS:
                if (cover_dir / stamp).is_file():
                    errors.append(
                        f"slice4: forbidden overlay stamp {stamp} — gen_only_human allows slice + logo paste only"
                    )
        draw_count = _grsai_draw_count(cover_dir)
        checks.append("grsai_draw_count")
        if draw_count > 1:
            errors.append(
                f"slice4: {draw_count} Grsai completion result files — max 1 draw per article"
            )

    manifest_path = cover_dir / "quad-manifest.json"
    if manifest_path.is_file():
        checks.append("quad-manifest")
        manifest = _load_json(manifest_path)
        inline_count = int(manifest.get("inline_count") or 0)
        if inline_count not in (0, 3):
            errors.append(f"slice4: inline_count={inline_count} — must be 3")
        pipeline = str(manifest.get("pipeline") or "")
        if pipeline and "8" in pipeline and "slice4" not in pipeline.casefold():
            errors.append(f"slice4: legacy 8-frame pipeline marker in manifest: {pipeline}")

    registry_path = cover_dir / "cover-registry.json"
    if registry_path.is_file():
        checks.append("cover-registry")
        registry = _load_json(registry_path)
        assets = registry.get("assets") or []
        if isinstance(assets, list) and len(assets) > 4:
            errors.append(
                f"slice4: cover-registry lists {len(assets)} assets — max 4 (1 cover + 3 inlines)"
            )

    for extra_inline in range(4, 8):
        inline_path = cover_dir / f"inline-{extra_inline:02d}.png"
        if inline_path.is_file():
            errors.append(f"slice4: forbidden inline-{extra_inline:02d}.png (max 3 inlines)")

    tenant_path = root / "shared/tenant-config.json"
    if tenant_path.is_file():
        tenant = _load_json(tenant_path)
        img = tenant.get("image_generation") or {}
        checks.append("tenant_image_policy")
        if int(img.get("total_images") or 0) not in (0, 4):
            errors.append(
                f"tenant image_generation.total_images={img.get('total_images')} — must be 4"
            )
        if int(img.get("canvases_per_article") or 0) not in (0, 1):
            errors.append(
                f"tenant image_generation.canvases_per_article={img.get('canvases_per_article')} "
                "— must be 1"
            )
        if int(tenant.get("inline_image_count") or 0) not in (0, 3):
            errors.append(
                f"tenant inline_image_count={tenant.get('inline_image_count')} — must be 3"
            )

    status = "PASS" if not errors else "BLOCK"
    canon = GEN_ONLY_HUMAN_CANON_ID if uses_gen_only_human(root) else ONE_2K_SLICE4_CANON_ID
    return {
        "gate": "slice4",
        "status": status,
        "canon": canon,
        "checks_run": checks,
        "errors": errors,
        "article_dir": str(article_dir),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", type=Path, required=False)
    ap.add_argument("--doctor", action="store_true", help="Validate repo tenant/canon lock")
    ap.add_argument("-o", "--output", default="slice4-gate.json")
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]

    if args.doctor:
        errors: list[str] = []
        if not uses_one_2k_slice4(root):
            errors.append("slice4 canon not active in repo")
        canon_path = root / "memory/cover/cover-canon.json"
        if canon_path.is_file():
            canon = _load_json(canon_path)
            if canon.get("canon_id") != GEN_ONLY_HUMAN_CANON_ID:
                errors.append(f"cover-canon.json canon_id != {GEN_ONLY_HUMAN_CANON_ID}")
        tenant = _load_json(root / "shared/tenant-config.json")
        if tenant.get("cover_mode") not in {"one_2k_slice4", "gen_only_slice4"}:
            errors.append("tenant cover_mode must be gen_only_slice4")
        if errors:
            for err in errors:
                print(f"BLOCK: {err}", file=sys.stderr)
            return 1
        print(f"OK slice4 doctor — {GEN_ONLY_HUMAN_CANON_ID}")
        return 0

    article_dir = args.article_dir
    if not article_dir:
        print("BLOCKER: --article-dir required unless --doctor", file=sys.stderr)
        return 2
    article_dir = article_dir if article_dir.is_absolute() else root / article_dir
    if not article_dir.is_dir():
        print(f"BLOCKER: article-dir not found: {article_dir}", file=sys.stderr)
        return 2
    report = check_article_dir(article_dir, root=root)
    out_path = article_dir / Path(args.output).name
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] in {"PASS", "SKIP"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
