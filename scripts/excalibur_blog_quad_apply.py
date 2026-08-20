#!/usr/bin/env python3
"""Download ONE quad canvas URL, save canvas-quad.png, run split + optional inject.

``--inject-html`` delegates to ``excalibur_blog_cover_quad_split.py``, which
re-validates each existing ``data-slot`` figure against manifest ``h2_anchor``
(and src/alt). Wrong-H2 / stale figures are moved/rewritten — never silent skip.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from asset_download import download_url_bytes  # noqa: E402


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--url", default="", help="MCP result URL (or read result json)")
    ap.add_argument("--canvas-index", type=int, default=1, help="Canvas index 1 or 2 (longform)")
    ap.add_argument("--inject-html", action="store_true")
    ap.add_argument("--output-size", default="1200x675")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    cover_dir = article_dir / "cover"
    cover_dir.mkdir(parents=True, exist_ok=True)

    url = args.url.strip()
    local_path: Path | None = None
    result_name = f"quad-mcp-result-{args.canvas_index:02d}.json"
    legacy_result_name = "quad-mcp-result.json" if args.canvas_index == 1 else ""
    if not url:
        candidates = [cover_dir / result_name]
        if legacy_result_name:
            candidates.append(cover_dir / legacy_result_name)
        for result_path in candidates:
            if result_path.is_file():
                result_data = json.loads(result_path.read_text(encoding="utf-8"))
                url = (result_data.get("url") or "").strip()
                local_rel = (result_data.get("local_path") or "").strip()
                if local_rel:
                    local_path = Path(local_rel)
                    if not local_path.is_absolute():
                        local_path = article_dir / local_path
                if url or local_path:
                    break
    if not url and not local_path:
        print(f"❌ QUAD APPLY BLOCKER: pass --url or cover/{result_name}", file=sys.stderr)
        return 1

    manifest_path = cover_dir / "quad-manifest.json"
    canvas_file = f"canvas-quad-{args.canvas_index:02d}.png"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for spec in manifest.get("canvases") or []:
            if spec.get("index") == args.canvas_index:
                canvas_file = Path(str(spec.get("canvas_file", canvas_file))).name
                break

    canvas_path = cover_dir / canvas_file
    if local_path and local_path.is_file():
        data = local_path.read_bytes()
    else:
        data, _evidence = download_url_bytes(url)
    canvas_path.write_bytes(data)
    print(f"OK canvas={canvas_path}")

    result_json = cover_dir / result_name
    result_out: dict[str, str] = {}
    if url:
        result_out["url"] = url
    if local_path and local_path.is_file():
        rel = local_path
        if rel.is_relative_to(article_dir):
            rel = rel.relative_to(article_dir)
        result_out["local_path"] = str(rel)
    result_json.write_text(json.dumps(result_out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    cmd = [
        sys.executable,
        str(root / "scripts" / "excalibur_blog_cover_quad_split.py"),
        "--article-dir",
        str(article_dir),
        "--manifest",
        "cover/quad-manifest.json",
        "--canvas-index",
        str(args.canvas_index),
        "--output-size",
        args.output_size,
    ]
    if args.inject_html:
        cmd.append("--inject-html")
    proc = subprocess.run(cmd, cwd=str(root))
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
