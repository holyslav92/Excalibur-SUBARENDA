#!/usr/bin/env python3
"""Канонические референсы бренда для cover factory (Добрый дом — logo lockup)."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

IDENTITY_REAL_DIR = Path("memory/cover/assets/identity-real")
VISUAL_INBOX_DIR = Path("memory/setup/visual-inbox")
SCENE_COMPOSITION_DIR = Path("memory/cover/assets/scene-composition-only")
LOGO_LOCKUP_REL = Path("memory/cover/assets/brand/logo-dobry-dom.png")
TENANT_CONFIG_REL = Path("shared/tenant-config.json")

# Legacy identity lock — DISABLED for Добрый дом (logo_lockup mode).
FACE_PRIMARY: dict[str, str | bool] = {
    "id": "face_studio_2026",
    "file": "face-studio-2026-06-23.jpg",
    "role": "face_primary",
    "notes": "LEGACY — DISABLED for logo_lockup. Do not use.",
    "do_not_clone_scene": True,
}

BODY_BUILD_FILES: tuple[dict[str, str | bool], ...] = ()
NOT_FACE_SOURCE_FILES: tuple[dict[str, str | bool], ...] = ()
IDENTITY_REAL_FILES: tuple[dict[str, str | bool], ...] = ()
SCENE_COMPOSITION_ONLY_FILES: tuple[str, ...] = ()


def project_root() -> Path:
    import os

    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_tenant_config(root: Path | None = None) -> dict:
    root = root or project_root()
    path = root / TENANT_CONFIG_REL
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def cover_mode(root: Path | None = None) -> str:
    """Return cover_mode from tenant-config (default brand_logo_paste for Добрый дом)."""
    tenant = load_tenant_config(root)
    return str(tenant.get("cover_mode") or "brand_logo_paste").strip()


def logo_mode(root: Path | None = None) -> str:
    """logo_mode overrides cover_mode for logo pipeline when set."""
    tenant = load_tenant_config(root)
    explicit = str(tenant.get("logo_mode") or "").strip()
    if explicit:
        return explicit
    return cover_mode(root)


LOGO_REFERENCE_MODES = frozenset(
    {"reference_in_generation", "logo_reference_in_generation", "reference_in_gen"}
)


def tenant_uses_logo_reference_in_generation(root: Path | None = None) -> bool:
    """Logo baked into Grsai draw via urls/aroma reference — not alpha-pasted after."""
    mode = logo_mode(root).casefold()
    return mode in LOGO_REFERENCE_MODES


def is_logo_lockup_mode(root: Path | None = None) -> bool:
    mode = cover_mode(root).casefold()
    if tenant_uses_logo_reference_in_generation(root):
        return True
    return mode in {"logo_lockup", "brand_logo_paste", "brand_logo_composite", "paste_png", "illustrative"}


def logo_lockup_path(root: Path | None = None) -> Path:
    root = root or project_root()
    tenant = load_tenant_config(root)
    composite = tenant.get("logo_composite") or {}
    hero_rel = (tenant.get("cover_files") or {}).get("hero") or "memory/cover/blog-hero.json"
    hero_path = root / hero_rel
    hero_logo = ""
    if hero_path.is_file():
        try:
            hero = json.loads(hero_path.read_text(encoding="utf-8"))
            hero_logo = str(
                (hero.get("logo_composite") or {}).get("logo_asset")
                or hero.get("reference_image")
                or ""
            )
        except json.JSONDecodeError:
            hero_logo = ""
    rel = str(composite.get("logo_asset") or hero_logo or tenant.get("logo_lockup") or LOGO_LOCKUP_REL)
    path = Path(rel)
    if not path.is_absolute():
        path = root / path
    return path


def missing_logo_lockup(root: Path | None = None) -> list[str]:
    root = root or project_root()
    path = logo_lockup_path(root)
    if path.is_file():
        return []
    return [str(path.relative_to(root))]


def identity_paths(root: Path | None = None) -> list[Path]:
    if is_logo_lockup_mode(root):
        return []
    base = (root or project_root()) / IDENTITY_REAL_DIR
    return [base / str(spec["file"]) for spec in IDENTITY_REAL_FILES]


def missing_identity_files(root: Path | None = None) -> list[str]:
    """Return missing identity-real files. Empty when logo_lockup mode."""
    if is_logo_lockup_mode(root):
        return []
    root = root or project_root()
    missing: list[str] = []
    for spec in IDENTITY_REAL_FILES:
        rel = IDENTITY_REAL_DIR / str(spec["file"])
        if not (root / rel).is_file():
            missing.append(str(rel))
    return missing


def pick_identity_reference(topic_id: str = "", slug: str = "") -> dict[str, str | bool]:
    """Legacy — returns logo lockup spec when logo_lockup mode."""
    _ = topic_id, slug
    return {
        "id": "logo_dobry_dom",
        "file": "logo-dobry-dom.png",
        "role": "logo_lockup",
        "notes": "Brand logo factory paste — NOT face i2i; NEVER draw lockup in generation.",
        "do_not_clone_scene": False,
    }


def pick_logo_reference(topic_id: str = "", slug: str = "") -> dict[str, str]:
    """Return logo lockup reference spec for cover pipeline."""
    _ = topic_id, slug
    return {
        "id": "logo_dobry_dom",
        "path": str(LOGO_LOCKUP_REL),
        "role": "logo_lockup",
    }


def resolve_logo_reference_url(root: Path | None = None) -> str:
    """Публичный URL официального логотипа для Grsai urls/aroma reference."""
    root = root or project_root()
    from excalibur_blog_site_base import expand_site_base, resolve_public_base_from_env

    live = resolve_public_base_from_env()
    tenant = load_tenant_config(root)
    composite = tenant.get("logo_composite") or {}
    hero_rel = (tenant.get("cover_files") or {}).get("hero") or "memory/cover/blog-hero.json"
    hero_path = root / hero_rel
    hero_hosted = ""
    if hero_path.is_file():
        try:
            hero = json.loads(hero_path.read_text(encoding="utf-8"))
            hero_hosted = str(hero.get("reference_url_hosted") or "").strip()
        except json.JSONDecodeError:
            hero_hosted = ""

    canonical = str(composite.get("canonical_url") or "").strip()
    candidates: list[str] = []
    if canonical:
        candidates.append(canonical)
    if hero_hosted:
        candidates.append(hero_hosted)

    if not live:
        return ""

    for raw in candidates:
        value = str(raw or "").strip()
        if not value:
            continue
        if value.startswith("http://") or value.startswith("https://"):
            return value
        path = value if value.startswith("/") else f"/{value}"
        return expand_site_base(f"{{{{SITE_BASE}}}}{path}", live)
    return ""


def resolve_logo_reference_for_api(root: Path | None = None) -> dict[str, str]:
    """Локальный путь + публичный URL логотипа для batch/grsai."""
    root = root or project_root()
    path = logo_lockup_path(root)
    rel = str(path.relative_to(root)) if path.is_relative_to(root) else str(path)
    return {
        "id": "logo_dobry_dom",
        "path": str(path),
        "local": rel,
        "url": resolve_logo_reference_url(root),
        "role": "logo_reference_in_generation",
    }


def resolve_identity_reference_path(
    topic_id: str = "",
    slug: str = "",
    *,
    root: Path | None = None,
) -> Path:
    root = root or project_root()
    if is_logo_lockup_mode(root):
        return logo_lockup_path(root)
    spec = pick_identity_reference(topic_id, slug)
    return root / IDENTITY_REAL_DIR / str(spec["file"])


def resolve_logo_reference_path(*, root: Path | None = None) -> Path:
    return logo_lockup_path(root)


def stage_from_visual_inbox(root: Path | None = None) -> list[str]:
    """Копирует logo из visual-inbox → brand/ (logo_lockup mode)."""
    root = root or project_root()
    staged: list[str] = []
    if not is_logo_lockup_mode(root):
        return staged
    inbox = root / VISUAL_INBOX_DIR
    dest_dir = root / LOGO_LOCKUP_REL.parent
    dest_dir.mkdir(parents=True, exist_ok=True)
    for name in ("logo-dobry-dom.png", "logo.png"):
        src = inbox / name
        if src.is_file():
            dest = dest_dir / LOGO_LOCKUP_REL.name
            shutil.copy2(src, dest)
            staged.append(str(dest.relative_to(root)))
            break
    return staged


def identity_lock_summary() -> dict:
    root = project_root()
    if is_logo_lockup_mode(root):
        return {
            "cover_mode": cover_mode(root),
            "logo_lockup": str(LOGO_LOCKUP_REL),
            "logo_exists": logo_lockup_path(root).is_file(),
            "identity_lock": "DISABLED — logo lockup only",
        }
    return {
        "identity_real_dir": str(IDENTITY_REAL_DIR),
        "face_primary": str(IDENTITY_REAL_DIR / str(FACE_PRIMARY["file"])),
        "identity_files": [str(spec["file"]) for spec in IDENTITY_REAL_FILES],
        "body_build_only": [str(spec["file"]) for spec in BODY_BUILD_FILES],
        "not_face_source": [str(spec["file"]) for spec in NOT_FACE_SOURCE_FILES],
        "scene_composition_only_dir": str(SCENE_COMPOSITION_DIR),
        "scene_composition_only": list(SCENE_COMPOSITION_ONLY_FILES),
    }


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser(description="Logo lockup / identity staging helpers")
    ap.add_argument("--stage-from-inbox", action="store_true", help="Copy logo from visual-inbox")
    ap.add_argument("--check", action="store_true", help="Check logo lockup or identity-real files")
    ap.add_argument("--pick", metavar="TOPIC_ID", help="Show reference for topic")
    ap.add_argument("--json", action="store_true", help="Emit JSON summary")
    args = ap.parse_args()

    root = project_root()
    if args.stage_from_inbox:
        staged = stage_from_visual_inbox(root)
        if staged:
            print("OK staged:")
            for path in staged:
                print(f"  {path}")
        else:
            print("WARN no logo files found in visual-inbox")
        return 0

    if args.check:
        if is_logo_lockup_mode(root):
            missing = missing_logo_lockup(root)
            if missing:
                print("FAIL missing logo lockup:")
                for path in missing:
                    print(f"  {path}")
                return 1
            print(f"OK logo lockup present ({LOGO_LOCKUP_REL})")
            return 0
        missing = missing_identity_files(root)
        if missing:
            print("FAIL missing identity-real:")
            for path in missing:
                print(f"  {path}")
            return 1
        print("OK identity-real complete")
        return 0

    if args.pick:
        if is_logo_lockup_mode(root):
            spec = pick_logo_reference(args.pick)
            print(json.dumps({"topic_id": args.pick, "reference": spec["path"], "id": spec["id"]}, ensure_ascii=False))
        else:
            spec = pick_identity_reference(args.pick)
            rel = IDENTITY_REAL_DIR / str(spec["file"])
            print(json.dumps({"topic_id": args.pick, "reference": str(rel), "id": spec["id"]}, ensure_ascii=False))
        return 0

    if args.json:
        print(json.dumps(identity_lock_summary(), ensure_ascii=False, indent=2))
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
