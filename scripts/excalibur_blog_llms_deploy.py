#!/usr/bin/env python3
"""Deploy memory/blog/llms.txt (+ llms-full.txt) to WordPress site root via SFTP or FTP."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from excalibur_blog_remote_transport import transport_mode, upload_text_file
from excalibur_blog_site_base import SITE_BASE_PLACEHOLDER, expand_site_base
from excalibur_blog_wp_publish import load_env, project_root, validate_publish_env


def deploy_llms_files(root: Path, env: dict[str, str], public_base: str) -> dict[str, Any]:
    llms_dir = root / "memory" / "blog"
    files = [
        ("llms.txt", llms_dir / "llms.txt"),
        ("llms-full.txt", llms_dir / "llms-full.txt"),
    ]
    missing = [name for name, path in files if not path.is_file()]
    if missing:
        return {"status": "FAIL", "errors": [f"missing local file: {name}" for name in missing]}

    env_missing = validate_publish_env(env)
    if env_missing:
        return {"status": "FAIL", "errors": [f"missing env: {', '.join(env_missing)}"]}

    uploaded: list[str] = []
    errors: list[str] = []
    transport = transport_mode(env)
    for name, path in files:
        raw = path.read_text(encoding="utf-8")
        body = expand_site_base(raw, public_base)
        if SITE_BASE_PLACEHOLDER in body:
            errors.append(f"{name} still contains {{{{SITE_BASE}}}} after expand")
            continue
        data = body.encode("utf-8")
        try:
            upload_text_file(env, name, data)
            uploaded.append(name)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{name}: {exc}")

    status = "PASS" if uploaded and not errors else "FAIL"
    return {
        "status": status,
        "transport": transport,
        "uploaded": uploaded,
        "errors": errors,
        "public_base_configured": bool(public_base),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Deploy llms.txt to WP root (SFTP or FTP)")
    ap.add_argument("--public-base", type=str, default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    root = project_root()
    env = load_env(root)
    public = args.public_base or env.get("PUBLIC_SITE_URL") or env.get("WP_HOME") or env.get("WP_SITE_URL") or ""

    if args.dry_run:
        llms = root / "memory/blog/llms.txt"
        full = root / "memory/blog/llms-full.txt"
        report = {
            "dry_run": True,
            "llms_txt": llms.is_file(),
            "llms_full_txt": full.is_file(),
            "public_base_configured": bool(public),
            "transport": transport_mode(env),
            "placeholder_remaining": (
                (SITE_BASE_PLACEHOLDER in llms.read_text(encoding="utf-8")) if llms.is_file() and public else None
            ),
        }
        if public and llms.is_file():
            expanded = expand_site_base(llms.read_text(encoding="utf-8"), public)
            report["placeholder_remaining"] = SITE_BASE_PLACEHOLDER in expanded
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["llms_txt"] and report["llms_full_txt"] else 1

    if env.get("EXCALIBUR_BLOG_ALLOW_PUBLISH", "").strip().lower() != "yes":
        print("BLOCKER: EXCALIBUR_BLOG_ALLOW_PUBLISH != yes", file=sys.stderr)
        return 1
    if not public:
        print("BLOCKER: PUBLIC_SITE_URL or --public-base required", file=sys.stderr)
        return 2

    report = deploy_llms_files(root, env, public)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report.get("status") == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
