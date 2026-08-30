#!/usr/bin/env python3
"""Flag stale Writer/Sol artifacts when human-first inputs are newer."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

WATCHED = (
    "shared/SOUL.md",
    "shared/soul-examples/SOURCE.md",
    "shared/soul-examples/post-to-article.md",
    "shared/soul-examples/good-outputs.md",
    "shared/soul-examples/bad-outputs.md",
    "shared/article-style.md",
    "shared/writer-master-prompt.md",
    "shared/pipeline-canon.json",
    "agents/excalibur-blog-writer.md",
    "agents/excalibur-blog-sol.md",
    "skills/writer-excalibur-blog/SKILL.md",
    "skills/sol-excalibur-blog/SKILL.md",
    "scripts/excalibur_blog_pipeline_canon.py",
    "scripts/excalibur_blog_opening_meta_gate.py",
    "scripts/excalibur_blog_case_delivery_gate.py",
)

QA_ARTIFACTS = ("schema-gate.json",)
WRITER_DRAFT = "drafts/writer.html"
SOL_ARTIFACTS = ("drafts/variant-a.html", "article.html")
WRITER_ROOT_INPUTS = (
    "shared/writer-master-prompt.md",
    "agents/excalibur-blog-writer.md",
    "skills/writer-excalibur-blog/SKILL.md",
)
SOL_ROOT_INPUTS = (
    "shared/SOUL.md",
    "shared/soul-examples/SOURCE.md",
    "shared/soul-examples/post-to-article.md",
    "shared/soul-examples/good-outputs.md",
    "shared/soul-examples/bad-outputs.md",
    "shared/article-style.md",
    "agents/excalibur-blog-sol.md",
    "skills/sol-excalibur-blog/SKILL.md",
)
WRITER_ARTICLE_INPUTS = ("research-notes.md", "title-brief.json")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article-dir", required=True)
    parser.add_argument("--root", default=".")
    parser.add_argument("-o", "--output", default="freshness-report.json")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    article_dir = (
        root / args.article_dir
        if not Path(args.article_dir).is_absolute()
        else Path(args.article_dir)
    )

    contract_mtimes: dict[str, float] = {}
    missing_contracts: list[str] = []
    for rel in WATCHED:
        path = root / rel
        if not path.is_file():
            missing_contracts.append(rel)
            continue
        contract_mtimes[rel] = path.stat().st_mtime

    newest_contract = max(contract_mtimes.values()) if contract_mtimes else 0.0
    fingerprint_src = "|".join(
        f"{key}:{int(value)}" for key, value in sorted(contract_mtimes.items())
    )
    fingerprint = hashlib.sha256(fingerprint_src.encode()).hexdigest()[:16]

    must_rerun: list[str] = []
    checked: list[str] = []
    for name in QA_ARTIFACTS:
        path = article_dir / name
        if not path.is_file():
            continue
        checked.append(name)
        if path.stat().st_mtime < newest_contract:
            must_rerun.append(name)

    writer_input_mtimes = [
        (root / rel).stat().st_mtime
        for rel in WRITER_ROOT_INPUTS
        if (root / rel).is_file()
    ]
    writer_input_mtimes.extend(
        (article_dir / rel).stat().st_mtime
        for rel in WRITER_ARTICLE_INPUTS
        if (article_dir / rel).is_file()
    )
    newest_writer_input = max(writer_input_mtimes) if writer_input_mtimes else 0.0

    writer_draft = article_dir / WRITER_DRAFT
    if not writer_draft.is_file():
        must_rerun.append(f"{WRITER_DRAFT} missing")
    else:
        checked.append(WRITER_DRAFT)
        if writer_draft.stat().st_mtime < newest_writer_input:
            must_rerun.append(WRITER_DRAFT)

    sol_input_mtimes = [
        (root / rel).stat().st_mtime
        for rel in SOL_ROOT_INPUTS
        if (root / rel).is_file()
    ]
    if writer_draft.is_file():
        sol_input_mtimes.append(writer_draft.stat().st_mtime)
    for rel in ("title-brief.json", "research-notes.md"):
        p = article_dir / rel
        if p.is_file():
            sol_input_mtimes.append(p.stat().st_mtime)
    newest_sol_input = max(sol_input_mtimes) if sol_input_mtimes else 0.0

    for name in SOL_ARTIFACTS:
        path = article_dir / name
        if not path.is_file():
            if name == "article.html":
                must_rerun.append("article.html missing")
            continue
        checked.append(name)
        if path.stat().st_mtime < newest_sol_input:
            must_rerun.append(name)

    status = "PASS" if not must_rerun else "STALE"
    report = {
        "gate": "contract-freshness",
        "status": status,
        "contracts_fingerprint": fingerprint,
        "newest_contract_mtime": newest_contract,
        "missing_contracts": missing_contracts,
        "checked": checked,
        "must_rerun": must_rerun,
    }
    out = article_dir / Path(args.output).name
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
