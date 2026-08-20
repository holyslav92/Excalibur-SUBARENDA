#!/usr/bin/env python3
"""Gate: tariff/commission claims about known entities need official source verification."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_entities(root: Path) -> list[dict[str, Any]]:
    path = root / "shared/research-official-entities.json"
    if not path.is_file():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data.get("entities") or [])


def _normalize(text: str) -> str:
    return (text or "").lower().replace("ё", "е")


def entity_mentioned(text: str, entity: dict[str, Any]) -> bool:
    norm = _normalize(text)
    for alias in entity.get("aliases") or []:
        if _normalize(str(alias)) in norm:
            return True
    return False


def has_tariff_signal(text: str, entity: dict[str, Any]) -> bool:
    norm = _normalize(text)
    keywords = entity.get("tariff_keywords") or []
    return any(_normalize(str(k)) in norm for k in keywords)


def has_entity_tariff_claim_line(line: str, entity: dict[str, Any]) -> bool:
    if not entity_mentioned(line, entity):
        return False
    norm = _normalize(line)
    if "wordstat" in norm or "показ" in norm or "partial" in norm:
        return False
    if not has_tariff_signal(line, entity):
        return False
    # Конкретная сумма/процент (не любая цифра в строке).
    if not re.search(r"(₽|\d+\s*000|\d+[,.]\d+\s*%|0,\d+%|\d+\s*400)", line):
        return False
    if "вилка" in norm or "обзор" in norm:
        return False
    return True


def detect_required_entities(notes: str, entities: list[dict[str, Any]]) -> list[str]:
    required: list[str] = []
    lines = notes.splitlines()
    for entity in entities:
        eid = str(entity.get("id") or "")
        if not eid:
            continue
        if any(has_entity_tariff_claim_line(line, entity) for line in lines):
            required.append(eid)
    return required


def parse_source_table(notes: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    in_table = False
    for line in notes.splitlines():
        if line.strip().startswith("## source_table"):
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        if not in_table or not line.startswith("|"):
            continue
        if line.startswith("|----") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0].lower() == "id":
            continue
        rows.append(
            {
                "id": cells[0],
                "title": cells[1] if len(cells) > 1 else "",
                "url": cells[2] if len(cells) > 2 else "",
                "type": cells[3].lower() if len(cells) > 3 else "",
            }
        )
    return rows


def has_official_section(notes: str) -> bool:
    return "## official_verifications" in notes


def official_urls_for_entity(source_rows: list[dict[str, str]], entity: dict[str, Any]) -> list[str]:
    domains = {_normalize(d) for d in (entity.get("official_domains") or [])}
    urls: list[str] = []
    for row in source_rows:
        if row.get("type") != "official":
            continue
        host = _normalize(urlparse(row.get("url") or "").netloc)
        if host in domains or any(host.endswith("." + d) for d in domains):
            urls.append(row.get("url") or "")
    return urls


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article-dir", required=True)
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("-o", "--output", default="research-official-gate.json")
    args = parser.parse_args()

    root = args.root or project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    notes_path = article_dir / "research-notes.md"
    report_path = article_dir / "research-agent-report.json"
    errors: list[str] = []
    warnings: list[str] = []
    entities_checked: list[str] = []
    required_entities: list[str] = []

    notes = notes_path.read_text(encoding="utf-8") if notes_path.is_file() else ""
    if not notes:
        errors.append("research-notes.md missing")

    entities = load_entities(root)
    source_rows = parse_source_table(notes)

    required_entities = detect_required_entities(notes, entities)
    entities_checked = list(required_entities)

    for entity in entities:
        eid = str(entity.get("id") or "")
        if eid not in required_entities:
            continue
        official_urls = official_urls_for_entity(source_rows, entity)
        if not official_urls:
            errors.append(
                f"{eid}: tariff-like claim detected but no official source in source_table"
            )
        if not has_official_section(notes):
            errors.append(
                f"{eid}: missing ## official_verifications section in research-notes.md"
            )
        else:
            section = notes.split("## official_verifications", 1)[-1].split("##", 1)[0]
            if not entity_mentioned(section, entity):
                errors.append(
                    f"{eid}: official_verifications section exists but no row for this entity"
                )

    report_audit: dict[str, Any] = {}
    if report_path.is_file():
        try:
            report = json.loads(report_path.read_text(encoding="utf-8"))
            report_audit = report.get("official_source_audit") or {}
            if required_entities and str(report_audit.get("status") or "").upper() == "BLOCK":
                errors.append("research-agent-report.json official_source_audit.status=BLOCK")
        except json.JSONDecodeError:
            warnings.append("research-agent-report.json invalid JSON")

    if required_entities and not report_audit:
        warnings.append(
            "research-agent-report.json missing official_source_audit block (recommended)"
        )

    status = "PASS" if not errors else "BLOCK"
    out = {
        "gate": "research-official",
        "status": status,
        "required_entities": required_entities,
        "entities_checked": entities_checked,
        "has_official_verifications_section": has_official_section(notes),
        "errors": errors,
        "warnings": warnings,
    }
    out_path = article_dir / args.output
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    if errors:
        for err in errors:
            print(f"BLOCKER: {err}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
