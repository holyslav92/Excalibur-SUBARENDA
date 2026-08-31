#!/usr/bin/env python3
"""Cover QA gate — stamp cover/cover_qa.json after visual checks."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


# Slim gate (2026-08): beauty = agent judgment; brand lock = logo + phone + no plate + no WP UI.
BRAND_LOGO_PASTE_CHECKS = (
    "logo_composite_stamp_pass",
    "cover_logo_pasted",
    "inline_logo_count_2_3",
    "cover_phone_993_large_sticker",
    "forbid_phone_pill_post_composite",
    "forbid_922_phone",
    "forbid_ai_drawn_logo_cover",
    "forbid_wordpress_ui_in_art",
    "no_logo_plate_cover",
    "forbid_logo_overlaps_headline_phone",
    "type_meme_sticker_editorial",
    "require_cover_meme_sticker",
    "require_display_headline",
    "require_large_phone_sticker",
    "forbid_people_heavy_cover",
    "forbid_split_white_collage",
)

LOGO_REFERENCE_CHECKS = (
    "logo_reference_in_generation",
    "cover_phone_993_post_composite",
    "forbid_922_phone",
    "forbid_ai_drawn_logo_cover",
    "forbid_wordpress_ui_in_art",
    "no_logo_plate_cover",
    "inline_logo_count_2_3",
)

HOST_IDENTITY_CHECKS = (
    "identity_face_28yo",
    "identity_body_medium_slim",
    "identity_expression_invented",
    "cover_phone_readable",
    "identity_real_files",
)

COMMON_CHECKS = (
    "eight_png_exist",
    "quad_manifest_valid",
    "wordstat_stickers_1_3",
    "motif_no_collision_14d",
    "max_one_cat_meme_slot",
    "light_high_key",
)

REQUIRED_IMAGES = (
    "cover/cover.png",
    "cover/inline-01.png",
    "cover/inline-02.png",
    "cover/inline-03.png",
    "cover/inline-04.png",
    "cover/inline-05.png",
    "cover/inline-06.png",
    "cover/inline-07.png",
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_tenant_cover_mode(root: Path) -> dict:
    cfg_path = root / "shared" / "tenant-config.json"
    if not cfg_path.is_file():
        return {}
    try:
        tenant = json.loads(cfg_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    channels = tenant.get("cta_channels") or {}
    mode = str(tenant.get("cover_mode") or "").strip().casefold()
    logo_mode = str(tenant.get("logo_mode") or tenant.get("cover_mode") or "").strip().casefold()
    logo_reference = logo_mode in {
        "reference_in_generation",
        "logo_reference_in_generation",
        "reference_in_gen",
    }
    return {
        "brand_logo_paste": mode in {"brand_logo_paste", "brand_logo_composite", "paste_png"}
        and not logo_reference,
        "logo_reference_in_generation": logo_reference,
        "phone_display": str(channels.get("phone_display") or "+7 (993) 574-83-22").strip(),
    }


def validate_cover_qa(article_dir: Path, root: Path) -> dict:
    errors: list[str] = []
    qa_path = article_dir / "cover" / "cover_qa.json"
    tenant_cover = load_tenant_cover_mode(root)
    brand_logo_paste = bool(tenant_cover.get("brand_logo_paste"))
    logo_reference = bool(tenant_cover.get("logo_reference_in_generation"))

    from excalibur_blog_identity_real import missing_identity_files

    if not brand_logo_paste:
        missing_identity = missing_identity_files(root)
        if missing_identity:
            errors.append(f"identity-real missing: {', '.join(missing_identity)}")

    for rel in REQUIRED_IMAGES:
        if not (article_dir / rel).is_file():
            errors.append(f"missing image: {rel}")

    if not qa_path.is_file():
        errors.append("cover/cover_qa.json missing — run excalibur-blog-cover-qa")
        return {"status": "FAIL", "errors": errors}

    try:
        qa = load_json(qa_path)
    except json.JSONDecodeError as exc:
        return {"status": "FAIL", "errors": [f"cover_qa.json invalid JSON: {exc}"]}

    if str(qa.get("agent") or "") != "excalibur-blog-cover-qa":
        errors.append("cover_qa.json agent must be excalibur-blog-cover-qa")
    if str(qa.get("status") or "").upper() != "PASS":
        errors.append(f"cover_qa.json status must be PASS, got {qa.get('status')!r}")

    checks = qa.get("checks") or {}
    required = list(COMMON_CHECKS)
    if brand_logo_paste:
        required.extend(BRAND_LOGO_PASTE_CHECKS)
    elif logo_reference:
        required.extend(LOGO_REFERENCE_CHECKS)
    else:
        required.extend(HOST_IDENTITY_CHECKS)
    for key in required:
        if not checks.get(key):
            errors.append(f"cover_qa check failed or missing: {key}")

    manifest_path = article_dir / "cover" / "quad-manifest.json"
    meme_catalog = root / "memory" / "cover" / "meme-top100.json"
    if not meme_catalog.is_file():
        errors.append("memory/cover/meme-top100.json missing — meme catalog required")
    if manifest_path.is_file():
        try:
            manifest = load_json(manifest_path)
            stickers = manifest.get("wordstat_stickers") or []
            if not (1 <= len(stickers) <= 3):
                errors.append(f"wordstat_stickers count {len(stickers)}, need 1-3 in quad-manifest")
            phone = str(manifest.get("cover_phone_cta") or "").strip()
            expected_phone = str(tenant_cover.get("phone_display") or "+7 (993) 574-83-22")
            if phone != expected_phone:
                errors.append(
                    f"cover_phone_cta must be {expected_phone!r} in quad-manifest (got {phone!r})"
                )
            if "922" in phone.replace(" ", ""):
                errors.append("cover_phone_cta must not contain 922 (forbidden rieltor number)")
            slots = manifest.get("slots") or {}
            allowed_types = {
                "comparison_table",
                "process_flow",
                "bar_timeline_chart",
                "structure_diagram",
                "labeled_checklist",
                "fact_card",
                "workflow_diagram",
                "checklist_board",
                "schema_faq_ui",
                "tool_screenshot",
                "infographic_card",
            }
            for i in range(1, 8):
                key = f"inline_{i}"
                slot = slots.get(key) or {}
                if not str(slot.get("visual_type") or "").strip():
                    errors.append(f"{key}.visual_type missing in quad-manifest")
                elif str(slot.get("visual_type")) not in allowed_types:
                    errors.append(f"{key}.visual_type invalid: {slot.get('visual_type')}")
                labels = slot.get("labels") or []
                if not (2 <= len(labels) <= 6):
                    errors.append(f"{key}.labels count {len(labels)}, need 2-6")
        except json.JSONDecodeError:
            errors.append("quad-manifest.json invalid JSON")
        else:
            try:
                from excalibur_blog_meme_cat_gate import load_meme_catalog, validate_max_one_cat_meme

                catalog = load_meme_catalog(root)
                errors.extend(validate_max_one_cat_meme(manifest, catalog))
            except ImportError:
                errors.append("excalibur_blog_meme_cat_gate.py missing — cat-meme quota QA unavailable")

    if brand_logo_paste:
        try:
            from excalibur_blog_brand_logo_composite import validate_logo_stamp

            errors.extend(validate_logo_stamp(article_dir, root))
        except ImportError:
            stamp_path = article_dir / "cover" / "logo-composite-stamp.json"
            if not stamp_path.is_file():
                errors.append("cover/logo-composite-stamp.json missing — run brand logo composite")
        try:
            from excalibur_blog_drawn_logo_gate import (
                validate_article_logo_gates_slim,
                validate_cover_phone_and_overlap_gates,
            )

            errors.extend(validate_article_logo_gates_slim(article_dir, root))
            errors.extend(validate_cover_phone_and_overlap_gates(article_dir, root))
            try:
                from excalibur_blog_cover_collage_gate import validate_cover_type_meme_sticker_gates

                errors.extend(validate_cover_type_meme_sticker_gates(article_dir / "cover" / "cover.png"))
            except ImportError:
                errors.append("excalibur_blog_cover_collage_gate.py missing — scene poster QA unavailable")
        except ImportError:
            errors.append("excalibur_blog_drawn_logo_gate.py missing — logo paste QA unavailable")
    elif logo_reference:
        stamp_path = article_dir / "cover" / "logo-composite-stamp.json"
        if stamp_path.is_file():
            try:
                stamp = load_json(stamp_path)
                if str(stamp.get("status") or "").upper() != "PASS":
                    errors.append("logo-composite-stamp.json status != PASS (phone-only expected)")
            except json.JSONDecodeError:
                errors.append("logo-composite-stamp.json invalid JSON")
        try:
            from excalibur_blog_drawn_logo_gate import validate_article_logo_gates_reference_mode

            errors.extend(validate_article_logo_gates_reference_mode(article_dir, root))
        except ImportError:
            errors.append("excalibur_blog_drawn_logo_gate.py missing — logo reference QA unavailable")

    status = "PASS" if not errors else "FAIL"
    return {"status": status, "errors": errors}


def cmd_doctor(root: Path) -> int:
    agent_cursor = root / ".cursor/agents/excalibur-blog-cover-qa.md"
    agent_repo = root / "agents/excalibur-blog-cover-qa.md"
    skill = root / "skills/cover-qa-excalibur-blog/SKILL.md"
    for path in (agent_cursor, agent_repo, skill):
        if not path.is_file():
            print(f"FAIL missing {path.relative_to(root)}", file=sys.stderr)
            return 1
    print("OK cover-qa agent + skill present")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Cover QA gate for longform 8-image set")
    parser.add_argument("--article-dir", help="Article directory to validate")
    parser.add_argument("--doctor", action="store_true", help="Repo-level doctor check")
    args = parser.parse_args()
    root = project_root()

    if args.doctor:
        return cmd_doctor(root)

    if not args.article_dir:
        print("FAIL --article-dir required", file=sys.stderr)
        return 1

    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    result = validate_cover_qa(article_dir, root)
    if result["status"] != "PASS":
        print(f"FAIL COVER QA GATE: {'; '.join(result['errors'])}", file=sys.stderr)
        return 1
    print("OK cover QA stamp (cover_qa.json PASS)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
