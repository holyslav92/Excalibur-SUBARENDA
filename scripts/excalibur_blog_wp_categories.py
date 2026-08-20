#!/usr/bin/env python3
"""Resolve WordPress category IDs for Excalibur BLOG publish."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_registry(root: Path | None = None) -> dict[str, Any]:
    root = root or project_root()
    path = root / "shared/wp-blog-categories.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_tenant(root: Path) -> dict[str, Any]:
    path = root / "shared/tenant-config.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def slug_to_wp_id(registry: dict[str, Any], slug: str) -> int | None:
    categories = registry.get("categories") or {}
    entry = categories.get(slug) or {}
    wp_id = entry.get("wp_id")
    return int(wp_id) if wp_id else None


def resolve_category_slugs(root: Path, article_dir: Path) -> list[str]:
    registry = load_registry(root)
    meta_path = article_dir / "article.meta.json"
    meta: dict[str, Any] = {}
    if meta_path.is_file():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))

    explicit = meta.get("wp_category_slugs") or meta.get("category_slugs") or []
    slugs: list[str] = []
    if isinstance(explicit, str):
        explicit = [explicit]
    if isinstance(explicit, list):
        slugs = [str(item).strip() for item in explicit if str(item).strip()]

    if not slugs:
        topic_id = str(meta.get("topic_id") or "").upper()
        defaults = registry.get("topic_defaults") or {}
        topic_slugs = defaults.get(topic_id) or defaults.get(topic_id.lower()) or []
        if isinstance(topic_slugs, list):
            slugs = [str(item).strip() for item in topic_slugs if str(item).strip()]

    if not slugs:
        default_slug = str(registry.get("default_primary_slug") or "").strip()
        if default_slug:
            slugs = [default_slug]

    # Уникальные slug в порядке приоритета.
    seen: set[str] = set()
    ordered: list[str] = []
    for slug in slugs:
        if slug not in seen:
            seen.add(slug)
            ordered.append(slug)
    return ordered


def resolve_category_ids(root: Path, article_dir: Path) -> tuple[list[int], list[str]]:
    registry = load_registry(root)
    slugs = resolve_category_slugs(root, article_dir)
    ids: list[int] = []
    for slug in slugs:
        wp_id = slug_to_wp_id(registry, slug)
        if wp_id:
            ids.append(wp_id)
    # Уникальные ID, порядок сохраняем.
    seen_ids: set[int] = set()
    unique_ids: list[int] = []
    for wp_id in ids:
        if wp_id not in seen_ids:
            seen_ids.add(wp_id)
            unique_ids.append(wp_id)
    return unique_ids, slugs


def category_gate_errors(root: Path, article_dir: Path) -> list[str]:
    tenant = load_tenant(root)
    registry = load_registry(root)
    required = bool(tenant.get("wp_categories_required", True))
    if registry.get("forbid_uncategorized") is False and not required:
        return []

    category_ids, slugs = resolve_category_ids(root, article_dir)
    errors: list[str] = []
    if not category_ids:
        errors.append(
            "wp categories missing: set article.meta.json wp_category_slugs "
            "or shared/wp-blog-categories.json topic_defaults"
        )
        return errors

    uncategorized_id = int(registry.get("uncategorized_wp_id") or 1)
    if registry.get("forbid_uncategorized", True) and category_ids == [uncategorized_id]:
        errors.append("wp category is only 'Без рубрики' (bez-rubriki); assign a real rubric")

    known = set((registry.get("categories") or {}).keys())
    for slug in slugs:
        if slug not in known:
            errors.append(f"unknown wp_category_slug: {slug}")

    return errors


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article-dir", required=True)
    parser.add_argument("--root", type=Path, default=None)
    args = parser.parse_args()

    root = args.root or project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    ids, slugs = resolve_category_ids(root, article_dir)
    errors = category_gate_errors(root, article_dir)
    report = {
        "category_ids": ids,
        "category_slugs": slugs,
        "errors": errors,
        "status": "PASS" if not errors else "BLOCK",
    }
    out_path = article_dir / "wp-categories-gate.json"
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
