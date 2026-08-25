#!/usr/bin/env python3
"""Live fix: Dzen /feed/zen/ — native-no, enclosures, format-article, yzen_options."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from excalibur_blog_site_base import resolve_public_base_from_env  # noqa: E402
from excalibur_blog_wp_dzen_rss import (  # noqa: E402
    build_mu_plugin_deploy_bootstrap,
    build_post_dzen_meta_bootstrap,
    build_yzen_options_bootstrap,
    mu_plugin_bytes,
)
from excalibur_blog_wp_publish import (  # noqa: E402
    delete_bootstrap_sftp,
    load_env,
    project_root,
    publish_via_sftp,
    upload_bootstrap_sftp,
)

YEKT = ZoneInfo("Asia/Yekaterinburg")
REPORT_PATH = ROOT / "memory/blog/live-dzen-rss-fix-report.json"

DEFAULT_POST_ID = 4002
DEFAULT_SLUG = "posutochno-u-vuza-roditeli-s-pervokursnikom-na-3-nochi-ne-na-semestr"


def run_php_bootstrap(env: dict[str, str], php: str, public_base: str, *, bootstrap_name: str) -> str:
    from excalibur_blog_remote_transport import transport_mode

    runtime_env = dict(env)
    configured_root = (runtime_env.get("FTP_ROOT") or runtime_env.get("SSH_ROOT") or "").strip()
    if configured_root:
        runtime_env["SSH_ROOT"] = configured_root
        runtime_env["FTP_ROOT"] = configured_root
    if transport_mode(runtime_env) == "ftp":
        return publish_via_sftp(runtime_env, php, public_base, bootstrap_name=bootstrap_name)

    if not (runtime_env.get("SSH_HOST") or "").strip():
        runtime_env["SSH_HOST"] = (runtime_env.get("FTP_HOST") or "").strip()
    if not (runtime_env.get("SSH_PORT") or "").strip():
        runtime_env["SSH_PORT"] = "22"

    uploaded_path = upload_bootstrap_sftp(runtime_env, bootstrap_name, php.encode("utf-8"))
    url = public_base.rstrip("/") + "/" + bootstrap_name
    try:
        proc = subprocess.run(
            ["curl", "-sS", "-m", "180", url],
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError(f"curl bootstrap failed rc={proc.returncode}: {proc.stderr}")
        return proc.stdout
    finally:
        try:
            delete_bootstrap_sftp(runtime_env, bootstrap_name, uploaded_path)
        except Exception:
            pass


def fetch_feed(public_base: str) -> str:
    url = f"{public_base.rstrip('/')}/feed/zen/"
    req = Request(url, headers={"User-Agent": "ExcaliburBlog/1.0"})
    with urlopen(req, timeout=120) as resp:
        return resp.read().decode("utf-8", errors="replace")


def first_item_block(feed: str, slug: str) -> str:
    marker = f"/blog/{slug}/"
    idx = feed.find(marker)
    if idx < 0:
        raise RuntimeError(f"slug not found in feed: {slug}")
    start = feed.rfind("<item>", 0, idx)
    end = feed.find("</item>", idx)
    if start < 0 or end < 0:
        raise RuntimeError("item block not found in feed")
    return feed[start:end + len("</item>")]


def analyze_item(item: str) -> dict[str, Any]:
    enclosures = re.findall(r"<enclosure\s[^>]*>", item, flags=re.I)
    categories = re.findall(r"<category>([^<]+)</category>", item)
    title_m = re.search(r"<title>([^<]+)</title>", item)
    author_m = re.search(r"<author>([^<]*)</author>", item)
    content_m = re.search(r"<content:encoded><!\[CDATA\[(.*?)\]\]></content:encoded>", item, re.S)
    channel_link_m = re.search(r"<link>(https?://[^<]+)</link>", item)
    return {
        "title": title_m.group(1).strip() if title_m else "",
        "author": author_m.group(1).strip() if author_m else "",
        "categories": categories,
        "enclosure_count": len(enclosures),
        "enclosures": enclosures,
        "has_native_no": "native-no" in categories,
        "has_format_article": "format-article" in categories,
        "content_chars": len(content_m.group(1)) if content_m else 0,
        "item_link": channel_link_m.group(1) if channel_link_m else "",
    }


def channel_link(feed: str) -> str:
    m = re.search(r"<channel>\s*.*?<link>(https?://[^<]+)</link>", feed, re.S)
    return m.group(1).strip() if m else ""


def verify_feed(public_base: str, slug: str) -> dict[str, Any]:
    feed = fetch_feed(public_base)
    item = first_item_block(feed, slug)
    analysis = analyze_item(item)
    analysis["channel_link"] = channel_link(feed)
    analysis["pass"] = (
        analysis["title"] != ""
        and analysis["content_chars"] > 500
        and analysis["enclosure_count"] == 1
        and not analysis["has_native_no"]
        and analysis["has_format_article"]
    )
    analysis["item_snippet"] = item[:3500]
    return analysis


def main() -> int:
    ap = argparse.ArgumentParser(description="Fix live Dzen RSS feed + post meta")
    ap.add_argument("--post-id", type=int, default=DEFAULT_POST_ID)
    ap.add_argument("--slug", default=DEFAULT_SLUG)
    ap.add_argument("--verify-only", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    env = load_env(project_root())
    public_base = resolve_public_base_from_env() or (env.get("PUBLIC_SITE_URL") or "").strip()
    if not public_base:
        print("BLOCKER: PUBLIC_SITE_URL missing", file=sys.stderr)
        return 1

    if args.verify_only:
        report = verify_feed(public_base, args.slug)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report.get("pass") else 2

    steps: list[dict[str, Any]] = []
    before = verify_feed(public_base, args.slug)
    steps.append({"step": "before", "analysis": before})

    if args.dry_run:
        print(
            json.dumps(
                {
                    "public_base": public_base,
                    "post_id": args.post_id,
                    "slug": args.slug,
                    "before": before,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    mu_out = run_php_bootstrap(
        env,
        build_mu_plugin_deploy_bootstrap(mu_plugin_bytes().decode("utf-8")),
        public_base,
        bootstrap_name="excalibur-dzen-mu-plugin-once.php",
    )
    if "OK dzen_mu_plugin_done" not in mu_out:
        print("FAIL mu-plugin deploy", file=sys.stderr)
        print(mu_out)
        return 1
    steps.append({"step": "mu_plugin", "output_tail": mu_out[-500:]})

    opts_out = run_php_bootstrap(
        env,
        build_yzen_options_bootstrap(public_base),
        public_base,
        bootstrap_name="excalibur-dzen-yzen-options-once.php",
    )
    if "OK dzen_yzen_options_done" not in opts_out:
        print("FAIL yzen_options", file=sys.stderr)
        print(opts_out)
        return 1
    steps.append({"step": "yzen_options", "output_tail": opts_out[-500:]})

    post_out = run_php_bootstrap(
        env,
        build_post_dzen_meta_bootstrap(args.post_id, bump_modified=True, repoint_featured_full=True),
        public_base,
        bootstrap_name="excalibur-dzen-post-meta-once.php",
    )
    if "OK dzen_post_meta_done" not in post_out:
        print("FAIL post meta", file=sys.stderr)
        print(post_out)
        return 1
    steps.append({"step": "post_meta", "output_tail": post_out[-800:]})

    after = verify_feed(public_base, args.slug)
    steps.append({"step": "after", "analysis": after})

    report = {
        "fixed_at_yekt": datetime.now(YEKT).isoformat(),
        "public_base": public_base,
        "post_id": args.post_id,
        "slug": args.slug,
        "before": before,
        "after": after,
        "steps": steps,
        "pass": after.get("pass"),
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if after.get("pass") else 2


if __name__ == "__main__":
    raise SystemExit(main())
