#!/usr/bin/env python3
"""Enforce the current human-first article pipeline at publication time."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

from excalibur_blog_article_meta_index import resolve_publish_slug


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_canon(root: Path) -> dict[str, Any]:
    path = root / "shared" / "pipeline-canon.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not str(data.get("version") or "").strip():
        raise ValueError("shared/pipeline-canon.json must contain version")
    return data


def load_json(path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def _plain(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    return re.sub(r"\s+", " ", text).strip()


def _first_sentences(text: str, max_chars: int = 220) -> str:
    """Truncate plain text. Do NOT use body opening as WP/RSS excerpt.

    Cloning the lead into post_excerpt makes Dzen/RSSLint show the same
    lines twice (RSS <description> + <content:encoded>). Prefer H1 for
    auto description / excerpt fallbacks (INC-20260805-2240).
    """
    plain = _plain(text)
    if not plain:
        return ""
    if len(plain) <= max_chars:
        return plain
    cut = plain[: max_chars - 1]
    if " " in cut:
        cut = cut.rsplit(" ", 1)[0]
    return cut.rstrip(".,;:") + "…"


def description_clones_opening(description: str, body_html: str, *, min_chars: int = 48) -> bool:
    """True when meta/excerpt is a truncated copy of the article opening."""
    desc = _plain(description).rstrip("…").rstrip(".,;:").strip()
    body = _plain(body_html)
    if len(desc) < min_chars or not body:
        return False
    probe = desc[: min(len(desc), 80)]
    return body.startswith(probe)


def validate_article_canon(article_dir: Path, root: Path) -> list[str]:
    """Return blockers when an article comes from an old or hybrid pipeline."""
    canon = load_canon(root)
    expected = str(canon["version"])
    errors: list[str] = []

    meta = load_json(article_dir / "article.meta.json")
    if not meta:
        return ["article.meta.json missing/invalid for pipeline canon"]
    if meta.get("pipeline_canon") != expected:
        errors.append(
            "article.meta.json pipeline_canon="
            f"{meta.get('pipeline_canon')!r} (need {expected!r})"
        )
    if meta.get("editorial_swarm") is not False:
        errors.append("article.meta.json editorial_swarm=false required")

    for name in canon.get("forbidden_article_files") or []:
        if (article_dir / str(name)).exists():
            errors.append(f"legacy pipeline artifact forbidden: {name}")

    html_path = article_dir / "article.html"
    if html_path.is_file():
        body = html_path.read_text(encoding="utf-8").lower()
        for marker in canon.get("forbidden_body_markers") or []:
            if re.search(rf"\b{re.escape(str(marker))}\b", body):
                errors.append(f"service English marker forbidden in article.html: {marker}")

    title_blob = " ".join(
        str(meta.get(key) or "")
        for key in ("title", "h1", "description", "cover_hook")
    ).lower()
    for marker in canon.get("forbidden_title_markers") or []:
        if str(marker).lower() in title_blob:
            errors.append(f"SEO title marker forbidden in meta: {marker}")

    return errors


def stamp_article(article_dir: Path, root: Path) -> None:
    """Stamp canon flags + fill thin meta from Writer HTML / title-brief.

    Does not rewrite article.html prose.
    """
    canon = load_canon(root)
    meta_path = article_dir / "article.meta.json"
    meta = load_json(meta_path) or {}
    title_brief = load_json(article_dir / "title-brief.json") or {}
    research_ctx = load_json(article_dir / "research-context.json") or {}
    html_path = article_dir / "article.html"
    body = html_path.read_text(encoding="utf-8") if html_path.is_file() else ""

    h1 = str(
        title_brief.get("h1") or title_brief.get("title") or meta.get("h1") or ""
    ).strip()
    slug = str(meta.get("slug") or title_brief.get("slug") or resolve_publish_slug(article_dir)).strip().strip("/")
    topic_id = str(
        meta.get("topic_id")
        or title_brief.get("topic_id")
        or article_dir.name.split("-", 1)[0]
    )
    # Auto description must NOT clone the opening paragraphs: WP maps it to
    # post_excerpt → RSS <description>, and Dzen shows description + body.
    existing_desc = str(meta.get("description") or "").strip()
    if existing_desc and description_clones_opening(existing_desc, body):
        description = h1 or existing_desc
    else:
        description = existing_desc or h1 or ""

    if h1:
        meta.setdefault("title", h1)
        meta["h1"] = h1
    meta.setdefault("slug", slug)
    meta.setdefault("topic_id", topic_id)
    # author_id from tenant-config when meta omits it
    if not meta.get("author_id"):
        tenant = load_json(project_root() / "shared/tenant-config.json") or {}
        tenant_author = str(tenant.get("author_id") or "").strip()
        if tenant_author:
            meta["author_id"] = tenant_author
    meta.setdefault("article_mode", meta.get("article_mode") or "B")
    if description:
        meta["description"] = description
    meta.setdefault("meta_ab", {})
    if isinstance(meta["meta_ab"], dict):
        if h1:
            meta["meta_ab"].setdefault("title_seo", h1)
            meta["meta_ab"].setdefault("title_ctr", h1)
            meta["meta_ab"].setdefault("title_aeo", h1)
        if description:
            # Force-replace SEO desc copies that clone the opening (Dzen RSS).
            for key in ("description_seo", "description_ctr", "description_aeo"):
                cur = str(meta["meta_ab"].get(key) or "").strip()
                if not cur or description_clones_opening(cur, body):
                    meta["meta_ab"][key] = description
                else:
                    meta["meta_ab"].setdefault(key, description)
    meta.setdefault(
        "theme_blocks",
        {"faq": "skip", "quiz": "skip", "side_stickers": "skip"},
    )
    if isinstance(meta["theme_blocks"], dict):
        for key in ("faq", "quiz", "side_stickers"):
            meta["theme_blocks"].setdefault(key, "skip")
    meta.setdefault(
        "date",
        str(research_ctx.get("today_iso") or meta.get("date") or date.today().isoformat()),
    )
    meta["pipeline_canon"] = canon["version"]
    meta["editorial_swarm"] = False

    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Keep draft mirror if Writer only wrote article.html
    draft = article_dir / "drafts" / "variant-a.html"
    if body and not draft.is_file():
        draft.parent.mkdir(parents=True, exist_ok=True)
        draft.write_text(body, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article-dir", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=project_root())
    parser.add_argument("--stamp", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    article_dir = args.article_dir.resolve()

    if args.stamp:
        stamp_article(article_dir, root)
    errors = validate_article_canon(article_dir, root)
    payload = {
        "gate": "pipeline-canon",
        "status": "PASS" if not errors else "BLOCK",
        "version": load_canon(root)["version"],
        "errors": errors,
    }
    print(json.dumps(payload, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
