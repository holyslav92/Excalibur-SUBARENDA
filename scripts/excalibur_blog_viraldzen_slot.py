#!/usr/bin/env python3
"""Slot step 0: ViralDzen collect + utility viral-angle pick (before Scout).

Fails loud on network/tool errors — no silent fallback to old topic picking.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from excalibur_blog_viral_topic_repeat import check_topic_repeat

ROOT = Path(__file__).resolve().parents[1]


def _load_config(root: Path) -> dict[str, Any]:
    path = root / "shared/viraldzen-slot-config.json"
    if not path.is_file():
        raise RuntimeError(f"missing config: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _import_viraldzen() -> Any:
    try:
        import viraldzen  # noqa: F401
    except ImportError as exc:
        raise RuntimeError(
            "VIRALDZEN BLOCKER: package viraldzen not installed. "
            "pip install 'git+https://github.com/Horosheff/ViralDzen.git'"
        ) from exc
    from viraldzen.collect import CollectConfig, collect
    from viraldzen.dzen import DzenApi
    from viraldzen.http import DzenClient
    from viraldzen.store import ItemStore
    from viraldzen.topics import apply_topic_filters, merge_official_topics

    return CollectConfig, collect, DzenApi, DzenClient, ItemStore, apply_topic_filters, merge_official_topics


def _discover_hubs(root: Path, cfg: dict[str, Any]) -> dict[str, Any]:
    CollectConfig, collect, DzenApi, DzenClient, ItemStore, apply_topic_filters, merge_official_topics = (
        _import_viraldzen()
    )
    hub_cfg = cfg.get("hub_pick") or {}
    seeds = list(cfg.get("topic_seeds_ru") or [])
    if not seeds:
        raise RuntimeError("VIRALDZEN BLOCKER: topic_seeds_ru empty in viraldzen-slot-config.json")

    delay = float((cfg.get("collect") or {}).get("delay_seconds", 0.7))
    client = DzenClient(delay_seconds=delay)
    client.warmup()
    api = DzenApi(client)

    groups = []
    for seed in seeds:
        found = api.search_official_topics(seed.strip(), pages=int(hub_cfg.get("topic_pages", 1)))
        groups.append(found)
    merged = merge_official_topics(groups)
    topics = apply_topic_filters(
        merged,
        min_subscribers=int(hub_cfg.get("min_subscribers", 0)),
        limit=int(hub_cfg.get("topics_per_seed", 8)) * max(len(seeds), 1),
        sort="subscribers",
    )
    if not topics:
        raise RuntimeError("VIRALDZEN BLOCKER: no official Dzen hubs discovered for configured seeds")

    keywords = [k.casefold() for k in (hub_cfg.get("prefer_slug_keywords") or [])]
    scored: list[tuple[int, Any]] = []
    for topic in topics:
        blob = f"{topic.slug} {topic.title}".casefold()
        kw_hits = sum(1 for k in keywords if k in blob)
        scored.append((kw_hits * 10_000_000 + int(topic.subscribers or 0), topic))
    scored.sort(key=lambda x: x[0], reverse=True)
    best = scored[0][1]
    return {
        "slug": best.slug,
        "title": best.title,
        "url": best.url,
        "subscribers": best.subscribers,
        "topic_id": best.topic_id,
        "discovered_from_seeds": seeds,
    }


def _collect_viral(root: Path, cfg: dict[str, Any], hub: dict[str, Any], out_dir: Path) -> list[dict[str, Any]]:
    coll = cfg.get("collect") or {}
    slug = str(hub["slug"])
    delay = float(coll.get("delay_seconds", 0.7))
    cmd = [
        sys.executable,
        "-m",
        "viraldzen",
        "collect",
        "--slug",
        slug,
        "--out-dir",
        str(out_dir),
        "--delay",
        str(delay),
        "--pages",
        str(int(coll.get("pages", 2))),
        "--top",
        str(int(coll.get("top_n", 20))),
        "--min-views",
        str(int(coll.get("min_views", 0))),
        "--no-content",
        "--no-images",
    ]
    proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True, timeout=900)
    if proc.returncode != 0:
        raise RuntimeError(
            f"VIRALDZEN BLOCKER: collect failed for slug={slug}\n"
            + (proc.stderr or proc.stdout or "")[:2500]
        )
    db_path = out_dir / "viral.sqlite"
    ItemStore = _import_viraldzen()[4]
    store = ItemStore(db_path)
    try:
        items = store.all_items()
    finally:
        store.close()
    if not items:
        raise RuntimeError(f"VIRALDZEN BLOCKER: collect returned 0 items for hub slug={slug}")
    def _item_field(item: Any, key: str, default: Any = "") -> Any:
        # viraldzen ItemStore.all_items() returns sqlite3.Row — доступ по ключу, не по атрибуту
        if isinstance(item, dict):
            return item.get(key, default)
        try:
            return item[key]
        except (KeyError, TypeError, IndexError):
            return getattr(item, key, default)

    rows: list[dict[str, Any]] = []
    for item in items[: int(coll.get("top_n", 20))]:
        rows.append(
            {
                "title": _item_field(item, "title"),
                "url": _item_field(item, "url"),
                "viral_score": float(_item_field(item, "viral_score") or 0),
                "views": int(_item_field(item, "views") or 0),
                "topic": _item_field(item, "topic"),
                "snippet": str(_item_field(item, "snippet") or "")[:280],
            }
        )
    rows.sort(key=lambda r: (r["viral_score"], r["views"]), reverse=True)
    return rows


def _pick_angle(root: Path, hub: dict[str, Any], candidates: list[dict[str, Any]], out_dir: Path) -> dict[str, Any]:
    user_path = out_dir / "viraldzen-angle-input.md"
    lines = [
        "# Viral candidates (titles only — do not copy text)",
        f"Hub slug: {hub['slug']} ({hub['title']})",
        "",
    ]
    for i, row in enumerate(candidates[:12], start=1):
        lines.append(
            f"{i}. score={row['viral_score']:.2f} views={row['views']} "
            f"title={row['title']!r} url={row['url']}"
        )
    user_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    angle_path = out_dir / "viral-angle-pick.json"
    cmd = [
        sys.executable,
        str(root / "scripts/excalibur_blog_derouter_opus_chat.py"),
        "--role",
        "viral-pick",
        "--system-file",
        str(root / "shared/viral-dzen-angle-system.md"),
        "--user-file",
        str(user_path),
        "--output",
        str(angle_path),
    ]
    proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True, timeout=600)
    if proc.returncode != 0:
        raise RuntimeError(
            "VIRALDZEN BLOCKER: Derouter viral-pick failed\n"
            + (proc.stderr or proc.stdout or "")[:2000]
        )
    if not angle_path.is_file():
        raise RuntimeError("VIRALDZEN BLOCKER: viral-angle-pick.json not written")
    raw = angle_path.read_text(encoding="utf-8").strip()
    if raw.startswith("```"):
        raw = raw.split("```", 2)[1]
        if raw.startswith("json"):
            raw = raw[4:]
    pick = json.loads(raw)
    if pick.get("status") != "PASS":
        raise RuntimeError(f"VIRALDZEN BLOCKER: angle pick blocked — {pick.get('reason') or pick}")
    return pick


def run_slot(
    *,
    root: Path,
    article_dir: Path | None,
    dry_run_collect: bool = False,
) -> dict[str, Any]:
    cfg = _load_config(root)
    hub = _discover_hubs(root, cfg)
    handoff_name = str(cfg.get("handoff_filename") or "viral-dzen-handoff.json")

    with tempfile.TemporaryDirectory(prefix="viraldzen-slot-") as tmp:
        tmp_path = Path(tmp)
        if dry_run_collect:
            candidates = [
                {
                    "title": "dry-run",
                    "url": "https://dzen.ru/a/dry-run",
                    "viral_score": 1.0,
                    "views": 1,
                    "topic": hub["slug"],
                    "snippet": "",
                }
            ]
            pick = {
                "status": "PASS",
                "viral_source": candidates[0],
                "guest_angle_ru": "dry-run angle unique wound kettle filter",
                "tyumen_wound_hint": "dry-run",
                "hub_slug": hub["slug"],
            }
        else:
            candidates = _collect_viral(root, cfg, hub, tmp_path)
            pick = None
            excluded_urls: set[str] = set()
            for _attempt in range(min(8, len(candidates) or 1)):
                pool = [c for c in candidates if c["url"] not in excluded_urls]
                if not pool:
                    break
                pick = _pick_angle(root, hub, pool, tmp_path)
                probe = " ".join(
                    [
                        str(pick.get("guest_angle_ru") or ""),
                        str(pick.get("tyumen_wound_hint") or ""),
                        str((pick.get("viral_source") or {}).get("title") or ""),
                    ]
                )
                repeat_errors = check_topic_repeat(root, probe)
                if not repeat_errors:
                    break
                src_url = str((pick.get("viral_source") or {}).get("url") or "")
                if src_url:
                    excluded_urls.add(src_url)
                pick = None
            if pick is None:
                raise RuntimeError(
                    "VIRALDZEN BLOCKER: no non-repeat viral angle after rework "
                    f"(tried {len(excluded_urls)} sources)"
                )

    src = pick.get("viral_source") or {}
    issued_at = datetime.now(timezone.utc).isoformat()
    handoff_id = str(uuid.uuid4())
    handoff = {
        "status": "PASS",
        "handoff_id": handoff_id,
        "issued_at": issued_at,
        "editorial_canon": "dobry_dom_voice_reset_v1",
        "discovered_hub": hub,
        "viral_source": {
            "title": src.get("title"),
            "url": src.get("url"),
            "viral_score": src.get("viral_score"),
        },
        "guest_angle_ru": pick.get("guest_angle_ru"),
        "tyumen_wound_hint": pick.get("tyumen_wound_hint"),
        "candidates_count": len(candidates) if not dry_run_collect else 0,
        "anti_copy": "Do not copy or closely paraphrase viral_source body; angle only.",
    }

    targets: list[Path] = [root / str(cfg.get("slot_handoff_path") or "memory/scout/viral-dzen-handoff.json")]
    if article_dir is not None:
        ad = article_dir if article_dir.is_absolute() else root / article_dir
        targets.append(ad / handoff_name)
    for target in targets:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(handoff, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return handoff


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--article-dir", type=Path, default=None)
    ap.add_argument("--dry-run", action="store_true", help="Skip network collect (tests only)")
    ap.add_argument("-o", "--output", type=Path, default=None)
    args = ap.parse_args()
    root = ROOT
    try:
        handoff = run_slot(root=root, article_dir=args.article_dir, dry_run_collect=args.dry_run)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        report = {"gate": "viraldzen-slot", "status": "BLOCK", "error": str(exc)}
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 1
    if args.output:
        out = args.output if args.output.is_absolute() else root / args.output
        out.write_text(json.dumps(handoff, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"gate": "viraldzen-slot", "status": "PASS", "hub": handoff["discovered_hub"]["slug"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
