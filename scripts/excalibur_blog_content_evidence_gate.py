#!/usr/bin/env python3
"""Validate evidence-based editorial QA without subjective numeric ratings."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_EVIDENCE = (
    "research_notes",
    "writer_ready",
    "links",
    "html",
)
# Accept old evidence key from published articles.
LEGACY_EVIDENCE_ALIASES = {"writer_ready": ("editor",)}
REQUIRED_EDITORIAL_JUDGMENTS = (
    "utility",
    "human_voice",
    "standalone",
    "direct_plain_language",
)
FORBIDDEN_RATING_KEYS = {
    "score",
    "scores",
    "overall",
    "overall_score",
    "judge_score",
    "weighted_quality_score",
    "rating",
    "ratings",
    "quality_score",
    "score_delta",
    "weighted_quality",
}


def _load(path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def _status(data: dict[str, Any]) -> str:
    for key in ("status", "verdict"):
        value = str(data.get(key) or "").strip().upper()
        if value:
            return value
    return ""


def _rating_keys(value: Any, prefix: str = "") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            path = f"{prefix}.{key}" if prefix else str(key)
            if str(key).lower() in FORBIDDEN_RATING_KEYS:
                found.append(path)
            found.extend(_rating_keys(child, path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(_rating_keys(child, f"{prefix}[{index}]"))
    return found


def validate(article_dir: Path, data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schema_version") != 2:
        errors.append("schema_version must be 2")
    if str(data.get("qa_verdict") or "").upper() != "PASS":
        errors.append("qa_verdict must be PASS")
    rating_keys = _rating_keys(data)
    if rating_keys:
        errors.append(
            "numeric editorial ratings are forbidden in evidence report: "
            + ", ".join(rating_keys)
        )

    evidence = data.get("evidence")
    if not isinstance(evidence, dict):
        errors.append("evidence must be an object")
        evidence = {}
    for name in REQUIRED_EVIDENCE:
        item = evidence.get(name)
        if not isinstance(item, dict):
            for alias in LEGACY_EVIDENCE_ALIASES.get(name, ()):
                alt = evidence.get(alias)
                if isinstance(alt, dict):
                    item = alt
                    break
        if not isinstance(item, dict):
            errors.append(f"evidence.{name} required")
            continue
        if str(item.get("status") or "").upper() != "PASS":
            errors.append(f"evidence.{name}.status must be PASS")
        report_name = str(item.get("report") or "").strip()
        if not report_name or Path(report_name).name != report_name:
            errors.append(f"evidence.{name}.report must be a filename")
            continue
        report = _load(article_dir / report_name)
        if report is None and report_name == "writer-ready-gate.json":
            report = _load(article_dir / "editor-choice-gate.json")
        if report is None:
            errors.append(f"evidence.{name} report missing/invalid: {report_name}")
        elif _status(report) not in {"PASS", "OK"}:
            errors.append(f"evidence.{name} report is not PASS: {report_name}")

    judgments = data.get("editorial_judgments")
    if not isinstance(judgments, dict):
        errors.append("editorial_judgments must be an object")
        judgments = {}
    for name in REQUIRED_EDITORIAL_JUDGMENTS:
        item = judgments.get(name)
        if not isinstance(item, dict):
            errors.append(f"editorial_judgments.{name} required")
            continue
        if str(item.get("status") or "").upper() != "PASS":
            errors.append(f"editorial_judgments.{name}.status must be PASS")
        if item.get("decided_by") != "excalibur-blog-writer":
            errors.append(
                "editorial_judgments.%s.decided_by must be excalibur-blog-writer"
                % name
            )
        findings = item.get("evidence")
        if not isinstance(findings, list) or not any(str(x).strip() for x in findings):
            errors.append(f"editorial_judgments.{name}.evidence required")
        if name == "standalone":
            if item.get("standalone_without_other_articles") is not True:
                errors.append(
                    "editorial_judgments.standalone requires "
                    "standalone_without_other_articles=true"
                )
            prior = item.get("required_prior_articles")
            if not isinstance(prior, list) or prior:
                errors.append(
                    "editorial_judgments.standalone.required_prior_articles must be empty"
                )
        if name == "direct_plain_language":
            if item.get("reader_entry_visible") is not True:
                errors.append(
                    "editorial_judgments.direct_plain_language requires "
                    "reader_entry_visible=true"
                )

    for key in ("reader_pain_solved", "first_result_shown"):
        if not str(data.get(key) or "").strip():
            errors.append(f"{key} required")
    keep = [str(x).strip() for x in data.get("keep", []) if str(x).strip()]
    if not keep:
        errors.append("keep must contain evidence-backed item")
    if data.get("unresolved_blockers"):
        errors.append("unresolved_blockers must be empty")
    if data.get("scaffold") is True:
        errors.append("scaffold:true forbidden")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article-dir", required=True)
    parser.add_argument(
        "-o",
        "--output",
        default="content-evidence-report.json",
        help="Report filename to validate (default: content-evidence-report.json).",
    )
    args = parser.parse_args()
    article_dir = Path(args.article_dir).resolve()
    if not article_dir.is_dir():
        parser.error(f"article-dir missing: {article_dir}")

    report_path = article_dir / args.output
    # human-first-v2: report is optional/legacy. Missing file → SKIP (exit 0),
    # not BLOCK. Present-but-invalid still BLOCKs.
    if not report_path.is_file():
        result = {
            "gate": "content-evidence",
            "status": "SKIP",
            "errors": [],
            "notes": [
                "content-evidence-report.json absent; optional under "
                "pipeline_canon human-first-v2"
            ],
            "rating_mode": "forbidden",
        }
        gate_path = article_dir / "content-evidence-gate.json"
        gate_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(json.dumps(result, ensure_ascii=False))
        return 0

    data = _load(report_path)
    if data is None:
        errors = ["missing/invalid content-evidence-report.json"]
    else:
        errors = validate(article_dir, data)
    result = {
        "gate": "content-evidence",
        "status": "PASS" if not errors else "BLOCK",
        "errors": errors,
        "rating_mode": "forbidden",
    }
    gate_path = article_dir / "content-evidence-gate.json"
    gate_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
