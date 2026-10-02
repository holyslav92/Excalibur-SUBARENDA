#!/usr/bin/env python3
"""Эфемерный референс стиля обложки из Pexels (один на статью).

Ищет landscape editorial/magazine cover по теме статьи, пишет
``cover/pexels-design-ref.json``. URL используется в Grsai ``urls[]`` только
на время генерации; после успешного draw ссылка не хранится в batch —
остаётся только логотип в настройках тенанта.
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_API_KEY_ENV = "PEXELS_API_KEY"
SEARCH_URL = "https://api.pexels.com/v1/search"
USED_REFS_REL = "memory/cover/used-pexels-refs.json"
DEFAULT_ORIENTATION = "landscape"
DEFAULT_PER_PAGE = 20


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path, default: Any = None) -> Any:
    if not path.is_file():
        return default if default is not None else {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def pexels_search(
    query: str,
    api_key: str,
    *,
    orientation: str = DEFAULT_ORIENTATION,
    per_page: int = DEFAULT_PER_PAGE,
    page: int = 1,
) -> dict[str, Any]:
    params = urllib.parse.urlencode(
        {
            "query": query,
            "orientation": orientation,
            "per_page": max(1, min(80, int(per_page))),
            "page": max(1, int(page)),
        }
    )
    url = f"{SEARCH_URL}?{params}"
    request = urllib.request.Request(
        url,
        headers={"Authorization": api_key, "User-Agent": "ExcaliburBlogPexels/1.0"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        err = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Pexels HTTP {exc.code}: {err[:400]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Pexels network error: {exc.reason}") from exc
    parsed = json.loads(body)
    if not isinstance(parsed, dict):
        raise RuntimeError("Pexels returned non-object JSON")
    return parsed


def best_photo_url(photo: dict[str, Any]) -> str:
    src = photo.get("src") or {}
    if not isinstance(src, dict):
        return ""
    for key in ("large2x", "large", "original", "medium"):
        url = str(src.get(key) or "").strip()
        if url.startswith("http"):
            return url
    return ""


def build_query_from_article(article_dir: Path) -> str:
    """Собрать запрос: editorial poster + тема из manifest/cover-text."""
    for rel in ("cover/quad-manifest.json", "cover/cover-text.json", "title-brief.json"):
        path = article_dir / rel
        if not path.is_file():
            continue
        try:
            data = load_json(path)
        except json.JSONDecodeError:
            continue
        parts: list[str] = []
        for key in ("cover_hook", "hook", "h1", "title"):
            val = str(data.get(key) or "").strip()
            if val:
                parts.append(val)
                break
        topic = " ".join(parts)[:80].strip()
        base = "editorial magazine cover typography layout bright"
        if topic:
            return f"{base} apartment rental {topic}"
        return base
    return "editorial magazine cover typography bright modern"


def pick_photo(
    photos: list[dict[str, Any]],
    *,
    used_ids: set[int],
    seed: int | None = None,
) -> dict[str, Any] | None:
    candidates = [p for p in photos if isinstance(p, dict) and int(p.get("id") or 0) not in used_ids]
    pool = candidates or [p for p in photos if isinstance(p, dict)]
    if not pool:
        return None
    rng = random.Random(seed)
    return rng.choice(pool)


def record_used_photo(root: Path, photo_id: int, query: str, url: str) -> None:
    path = root / USED_REFS_REL
    data = load_json(path, {"photos": []})
    photos = data.get("photos")
    if not isinstance(photos, list):
        photos = []
    entry = {
        "id": photo_id,
        "query": query,
        "url": url,
        "used_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    photos = [p for p in photos if not (isinstance(p, dict) and p.get("id") == photo_id)]
    photos.insert(0, entry)
    data["photos"] = photos[:200]
    save_json(path, data)


def resolve_pexels_ref(article_dir: Path, root: Path, query: str) -> dict[str, Any]:
    api_key = os.environ.get(DEFAULT_API_KEY_ENV, "").strip()
    if not api_key:
        raise RuntimeError(
            f"{DEFAULT_API_KEY_ENV} missing — set Pexels API key in Cloud Secrets"
        )
    used_data = load_json(root / USED_REFS_REL, {"photos": []})
    used_ids = {
        int(p.get("id"))
        for p in (used_data.get("photos") or [])
        if isinstance(p, dict) and p.get("id")
    }
    search_query = query.strip() or build_query_from_article(article_dir)
    result = pexels_search(search_query, api_key)
    photos = result.get("photos") or []
    if not isinstance(photos, list) or not photos:
        raise RuntimeError(f"Pexels: no photos for query={search_query!r}")
    seed = hash(str(article_dir.name)) & 0xFFFFFFFF
    photo = pick_photo(photos, used_ids=used_ids, seed=seed)
    if not photo:
        raise RuntimeError("Pexels: could not pick photo")
    url = best_photo_url(photo)
    if not url:
        raise RuntimeError("Pexels: photo missing src URL")
    photo_id = int(photo.get("id") or 0)
    record_used_photo(root, photo_id, search_query, url)
    photographer = str(photo.get("photographer") or "").strip()
    return {
        "status": "PASS",
        "source": "pexels",
        "query": search_query,
        "photo_id": photo_id,
        "url": url,
        "photographer": photographer,
        "orientation": DEFAULT_ORIENTATION,
        "role": "ephemeral_style_reference",
        "note": "Use in Grsai urls[0] for layout/style only; remove from batch after generation",
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--query", default="", help="Pexels search query (default: from article)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir
    if not article_dir.is_dir():
        print(f"BLOCKER: article dir missing: {article_dir}", file=sys.stderr)
        return 1
    try:
        ref = resolve_pexels_ref(article_dir, root, args.query)
    except RuntimeError as exc:
        print(f"BLOCKER: {exc}", file=sys.stderr)
        return 1
    out_path = article_dir / "cover" / "pexels-design-ref.json"
    if args.dry_run:
        preview = {**ref, "would_write": str(out_path.relative_to(root))}
        print(json.dumps(preview, ensure_ascii=False, indent=2))
        return 0
    save_json(out_path, ref)
    print(f"OK pexels-design-ref photo_id={ref['photo_id']} url={ref['url'][:80]}...")
    print(f"OK wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
