#!/usr/bin/env python3
"""Minimal preflight for clean human-first Excalibur BLOG pipeline."""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def check(condition: bool, label: str, errors: list[str], warnings: list[str], *, warn: bool = False) -> None:
    if condition:
        print(f"OK {label}")
        return
    if warn:
        warnings.append(label)
        print(f"WARN {label}")
    else:
        errors.append(label)
        print(f"FAIL {label}")


def module_available(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def read_env_file(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.is_file():
        return env
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip()
    return env


def merged_publish_env(root: Path) -> dict[str, str]:
    keys = {
        "PUBLIC_SITE_URL",
        "WP_HOME",
        "WP_SITE_URL",
        "FTP_HOST",
        "FTP_PORT",
        "FTP_USER",
        "FTP_PASS",
        "FTP_PASSWORD",
        "FTP_ROOT",
        "EXCALIBUR_BLOG_ALLOW_PUBLISH",
    }
    env = read_env_file(root / "memory/site.env.local")
    for key in keys:
        value = os.environ.get(key)
        if value:
            env[key] = value
    if not env.get("FTP_PASS") and env.get("FTP_PASSWORD"):
        env["FTP_PASS"] = env["FTP_PASSWORD"]
    return env


def git_ls_files(root: Path, pathspec: str) -> list[str]:
    proc = subprocess.run(
        ["git", "ls-files", pathspec],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return []
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Excalibur BLOG preflight doctor")
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()

    root = project_root()
    errors: list[str] = []
    warnings: list[str] = []
    print(f"EXCALIBUR_ROOT={root}")

    required = (
        "AGENTS.md",
        "SETUP.md",
        "CLOUD-FIRST-RUN.md",
        "shared/writer-master-prompt.md",
        "shared/article-style.md",
        "shared/tenant-config.json",
        "shared/SOUL.md",
        "shared/soul-examples/good-outputs.md",
        "shared/soul-examples/bad-outputs.md",
        "shared/soul-examples/SOURCE.md",
        "shared/soul-examples/post-to-article.md",
        "shared/dzen-content-rules.md",
        "shared/dzen-description-rules.md",
        "shared/rf-blocked-entities.json",
        "shared/pipeline-canon.json",
        "shared/published-titles.md",
        "shared/topic-focus-contract.md",
        "memory/setup/status.json",
        "scripts/excalibur_blog_topic_focus.py",
        "agents/excalibur-blog-setup.md",
        "agents/excalibur-blog-setup-voice.md",
        "agents/excalibur-blog-setup-visual.md",
        "agents/excalibur-blog-writer.md",
        "agents/excalibur-blog-sol.md",
        "agents/excalibur-blog-research.md",
        "agents/excalibur-blog-title.md",
        "agents/excalibur-blog-cover-text.md",
        "agents/excalibur-blog-description.md",
        "agents/excalibur-blog-cover-qa.md",
        "agents/excalibur-blog-publish.md",
        "skills/description-excalibur-blog/SKILL.md",
        "skills/cover-qa-excalibur-blog/SKILL.md",
        "scripts/excalibur_blog_description_gate.py",
        "scripts/excalibur_blog_cover_qa_gate.py",
        "shared/derouter-opus-brain-contract.md",
        "skills/setup-voice-excalibur-blog/SKILL.md",
        "skills/setup-visual-excalibur-blog/SKILL.md",
        "skills/writer-excalibur-blog/SKILL.md",
        "skills/sol-excalibur-blog/SKILL.md",
        "skills/title-excalibur-blog/SKILL.md",
        "skills/cover-text-excalibur-blog/SKILL.md",
        "skills/director-excalibur-blog/SKILL.md",
        "scripts/excalibur_blog_research_start.py",
        "scripts/excalibur_blog_published_titles.py",
        "scripts/excalibur_blog_slim_blog_topics.py",
        "scripts/excalibur_blog_pipeline_canon.py",
        "scripts/excalibur_blog_structure_gate.py",
        "scripts/excalibur_blog_opening_meta_gate.py",
        "scripts/excalibur_blog_case_delivery_gate.py",
        "scripts/excalibur_blog_writer_ready_gate.py",
        "scripts/excalibur_blog_cover_text_gate.py",
        "scripts/excalibur_blog_derouter_opus_chat.py",
        "scripts/excalibur_blog_interlink_lib.py",
        "scripts/excalibur_blog_interlinker.py",
        "scripts/excalibur_blog_live_catalog.py",
        "scripts/excalibur_blog_crosslink_qa_gate.py",
        "scripts/excalibur_blog_live_xlink_fix.py",
        "scripts/excalibur_blog_post_publish_interlink.py",
        "scripts/excalibur_blog_kie_gpt_image2_api.py",
        "scripts/excalibur_blog_wp_publish.py",
        "scripts/excalibur_blog_merge_to_main.py",
        "scripts/excalibur_blog_community_cta_gate.py",
    )
    for rel in required:
        check((root / rel).is_file(), f"{rel} exists", errors, warnings)

    check((root / ".cursor/agents").is_dir(), ".cursor/agents exists", errors, warnings)

    CANONICAL_PIPELINE_AGENTS = (
        "excalibur-blog-setup",
        "excalibur-blog-setup-voice",
        "excalibur-blog-setup-visual",
        "excalibur-blog-director",
        "excalibur-blog-scout",
        "excalibur-blog-research",
        "excalibur-blog-title",
        "excalibur-blog-writer",
        "excalibur-blog-sol",
        "excalibur-blog-description",
        "excalibur-blog-cover-text",
        "excalibur-blog-schema",
        "excalibur-blog-cover",
        "excalibur-blog-cover-qa",
        "excalibur-blog-indexer",
        "excalibur-blog-publish",
        "excalibur-blog-fixer",
        "excalibur-blog-content-learner",
    )
    for agent_name in CANONICAL_PIPELINE_AGENTS:
        for agents_dir in (root / "agents", root / ".cursor/agents"):
            rel = f"{agents_dir.name}/{agent_name}.md"
            check(
                (agents_dir / f"{agent_name}.md").is_file(),
                f"{rel} exists",
                errors,
                warnings,
            )
    cursor_agent_files = sorted((root / ".cursor/agents").glob("excalibur-blog-*.md"))
    check(
        len(cursor_agent_files) == len(CANONICAL_PIPELINE_AGENTS),
        f"18 pipeline agent files in .cursor/agents (got {len(cursor_agent_files)})",
        errors,
        warnings,
    )
    check(module_available("PIL"), "Pillow available", errors, warnings)
    check(module_available("numpy"), "numpy available", errors, warnings)

    topics_dir = root / "memory/topics"
    check(
        not topics_dir.exists(),
        "memory/topics/ removed (no blog-topics pool)",
        errors,
        warnings,
    )

    forbidden = (
        "agents/excalibur-blog-lead.md",
        "agents/excalibur-blog-article-editor.md",
        "agents/excalibur-blog-geo-qa.md",
        "agents/excalibur-blog-hook.md",
        "skills/lead-excalibur-blog/SKILL.md",
        "skills/article-editor-excalibur-blog/SKILL.md",
        "skills/excalibur-geo-qa/SKILL.md",
        "skills/hook-excalibur-blog/SKILL.md",
        "scripts/excalibur_blog_lead_meta_gate.py",
        "scripts/excalibur_blog_geo_qa_gate.py",
        "scripts/excalibur_blog_editor_choice_gate.py",
        "scripts/excalibur_blog_writer_finalize.py",
        "agents/excalibur-blog-writing-critic.md",
        "agents/excalibur-blog-reader-panel.md",
        "agents/excalibur-blog-glavred.md",
        "agents/excalibur-blog-visual-qa.md",
        "agents/excalibur-blog-thesis-editor.md",
        "agents/excalibur-blog-headline-director.md",
        "agents/excalibur-blog-metrika-analyst.md",
        "agents/excalibur-blog-policy-learner.md",
        "agents/excalibur-blog-voice-curator.md",
        "agents/excalibur-blog-reader-sim.md",
        "skills/excalibur/SKILL.md",
        "skills/excalibur-wp-publish/SKILL.md",
        "scripts/excalibur_blog_draft_meta_upsert.py",
        "scripts/excalibur_blog_editorial_swarm_gate.py",
        "scripts/excalibur_blog_visual_qa_gate.py",
        "scripts/excalibur_blog_content_experiments.py",
        "scripts/excalibur_blog_scorecard_coverage_report.py",
        "shared/golden-benchmark",
        "shared/editorial-swarm-contract.md",
        "shared/anti-template-contract.md",
        "shared/quality-blog.md",
        "shared/writer-operating-system.md",
        "shared/writer-brief-slim.md",
        "shared/agent-pipeline-pitfalls.md",
        "shared/pipeline-speed-contract.md",
        "shared/blog-visual-pipeline-contract.md",
        "shared/cover-hook-contract.md",
        "shared/mcp-image-async-contract.md",
        "shared/excalibur-blog-cover-index.md",
        "shared/editorial-read-bundle.md",
        "shared/editorial-utility-only.md",
        "shared/contract-freshness-contract.md",
        "shared/excalibur-blog-handoff.template.md",
        "shared/cloud-preflight-workflow.yml.example",
        "CURSOR-CLOUD-RUNBOOK.md",
        "CURSOR-CLOUD-AGENT-PIPELINE-FROM-SCRATCH.md",
        "SUBAGENTS.md",
        "memory/topics/blog-topics.md",
    )
    for rel in forbidden:
        check(not (root / rel).exists(), f"garbage removed: {rel}", errors, warnings)

    check(
        not git_ls_files(root, "shared/excalibur-blog-handoff.md"),
        "runtime handoff not tracked",
        errors,
        warnings,
    )

    # Setup / tenant status
    setup_path = root / "memory/setup/status.json"
    tenant_path = root / "shared/tenant-config.json"
    setup_complete = False
    try:
        setup = json.loads(setup_path.read_text(encoding="utf-8")) if setup_path.is_file() else {}
        tenant = json.loads(tenant_path.read_text(encoding="utf-8")) if tenant_path.is_file() else {}
        setup_complete = bool(setup.get("complete")) and bool(tenant.get("setup_complete"))
    except json.JSONDecodeError:
        setup = {}
        tenant = {}
        check(False, "setup/tenant JSON valid", errors, warnings)

    if setup_complete:
        check(True, "setup complete", errors, warnings)
        for marker_rel in (
            "shared/SOUL.md",
            "shared/article-style.md",
            "shared/soul-examples/good-outputs.md",
            "memory/cover/blog-hero.json",
            "memory/cover/cover-design-code.json",
            "shared/authors-registry.json",
            "memory/brief/site-brief.md",
        ):
            text = (root / marker_rel).read_text(encoding="utf-8") if (root / marker_rel).is_file() else ""
            check(
                "SETUP_REQUIRED" not in text,
                f"{marker_rel} filled (no SETUP_REQUIRED)",
                errors,
                warnings,
            )
        from excalibur_blog_identity_real import missing_identity_files

        missing_identity = missing_identity_files(root)
        check(
            not missing_identity,
            "identity-real live photos present (face_primary + body/scene refs)",
            errors,
            warnings,
        )
        if missing_identity:
            for rel in missing_identity:
                print(f"  missing: {rel}")
        check(
            not (root / "memory/cover/assets/hero-ref-office-risk-hologram.jpg").is_file(),
            "reconstructed AI hero-ref removed from assets root",
            errors,
            warnings,
        )
        for cover_marker in (
            "memory/cover/cover-canon.json",
            "memory/cover/used-motifs.json",
            "memory/cover/wordstat-geo.json",
        ):
            check((root / cover_marker).is_file(), f"{cover_marker} exists", errors, warnings)
        canon_path = root / "memory/cover/cover-canon.json"
        if canon_path.is_file():
            try:
                canon = json.loads(canon_path.read_text(encoding="utf-8"))
                daypart = canon.get("forbidden_daypart_formula") or {}
                check(
                    bool(daypart.get("never_use")),
                    "cover-canon rejects daypart formula",
                    errors,
                    warnings,
                )
            except json.JSONDecodeError:
                check(False, "cover-canon.json valid JSON", errors, warnings)
        for gate_cmd in (
            [sys.executable, str(root / "scripts/excalibur_blog_cover_motif_gate.py"), "doctor"],
            [sys.executable, str(root / "scripts/excalibur_blog_wordstat_gate.py"), "doctor"],
            [sys.executable, str(root / "scripts/excalibur_blog_cover_qa_gate.py"), "--doctor"],
            [sys.executable, str(root / "scripts/excalibur_blog_description_gate.py"), "--doctor"],
        ):
            proc = subprocess.run(gate_cmd, cwd=root, capture_output=True, text=True, check=False)
            label = gate_cmd[1].rsplit("/", 1)[-1]
            check(proc.returncode == 0, f"{label} doctor", errors, warnings)
        klyshin_bank = str(tenant.get("scout_klyshin_topic_bank") or "").strip()
        if klyshin_bank:
            bank_path = root / klyshin_bank
            check(bank_path.is_file(), f"{klyshin_bank} exists", errors, warnings)
            md_path = root / "memory/scout/klyshin-topic-bank.md"
            check(md_path.is_file(), "memory/scout/klyshin-topic-bank.md exists", errors, warnings)
            signals = tenant.get("scout_signal_urls") or []
            has_klyshin = any("klyshin" in str(u).lower() for u in signals)
            check(has_klyshin, "scout_signal_urls includes t.me/klyshin_A", errors, warnings)
    else:
        check(
            True,
            "setup incomplete — run excalibur-blog-setup before publish pipeline",
            errors,
            warnings,
            warn=True,
        )

    # Privacy deny-list (product must stay tenant-clean)
    deny = (
        "temalebedev",
        "t.me/maya_pro",
        "max.ru/maya_pro",
        "kv-ai.ru",
        "kovcheg_ai",
        "artur-horoshev",
        "Артур Хорошев",
        "Хорошев",
        "blog.tema.ru",
        "mayai.ru",
    )
    privacy_hits: list[str] = []
    scan_roots = [
        root / "agents",
        root / "skills",
        root / "shared",
        root / "AGENTS.md",
        root / "CLOUD-AUTOMATION.md",
        root / "README.md",
        root / "SETUP.md",
        root / "CLOUD-FIRST-RUN.md",
        root / "memory/brief",
        root / "memory/cover",
        root / "memory/setup",
    ]
    for scan in scan_roots:
        paths = [scan] if scan.is_file() else list(scan.rglob("*")) if scan.is_dir() else []
        for path in paths:
            if not path.is_file():
                continue
            if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
                continue
            # Deny-list literals live in this script — skip self and tests that assert cleanliness.
            rel = str(path.relative_to(root)).replace("\\", "/")
            if rel in {
                "scripts/excalibur_blog_doctor.py",
                "tests/test_privacy_deny_list.py",
            }:
                continue
            try:
                body = path.read_text(encoding="utf-8")
            except Exception:
                continue
            for token in deny:
                if token in body:
                    privacy_hits.append(f"{rel}:{token}")
                    break
    check(not privacy_hits, "privacy deny-list clean", errors, warnings)
    if privacy_hits:
        print("PRIVACY_HITS: " + "; ".join(privacy_hits[:20]))

    env = merged_publish_env(root)
    if setup_complete or args.publish:
        check(
            bool(env.get("PUBLIC_SITE_URL") or env.get("WP_SITE_URL") or env.get("WP_HOME")),
            "site URL configured",
            errors,
            warnings,
            warn=not args.publish,
        )
        check(bool(env.get("FTP_HOST")), "publish host configured (FTP/SFTP)", errors, warnings, warn=not args.publish)
        check(bool(env.get("FTP_USER")), "publish user configured", errors, warnings, warn=not args.publish)
        check(bool(env.get("FTP_PASS")), "publish password configured", errors, warnings, warn=not args.publish)
    else:
        print("NOTE skip publish secret checks until setup complete (use --publish to force)")
    if args.publish:
        check(env.get("EXCALIBUR_BLOG_ALLOW_PUBLISH", "").lower() == "yes", "EXCALIBUR_BLOG_ALLOW_PUBLISH=yes", errors, warnings)
        check(setup_complete, "setup complete before --publish", errors, warnings)

    derouter_key = os.environ.get("DEROUTER_API_KEY", "").strip()
    check(
        bool(derouter_key),
        "DEROUTER_API_KEY set (factory brain + Cover; missing → DEROUTER * BLOCKER)",
        errors,
        warnings,
        warn=True,
    )
    derouter_text_model = os.environ.get("DEROUTER_TEXT_MODEL", "").strip()
    if derouter_text_model and "opus" not in derouter_text_model.lower():
        check(
            True,
            f"DEROUTER_TEXT_MODEL ignored for powerful roles (legacy non-Opus: set); tier map is source of truth",
            errors,
            warnings,
            warn=True,
        )
    derouter_opus_env = os.environ.get("DEROUTER_OPUS_MODEL", "").strip()
    powerful_cfg = (tenant.get("writing_model") or {}).get("powerful") or {}
    powerful_model = str(powerful_cfg.get("model") or "claude-opus-5")
    opus_check = derouter_opus_env or powerful_model
    check(
        bool(opus_check) and "opus" in opus_check.lower(),
        f"powerful tier Opus family ({opus_check})",
        errors,
        warnings,
        warn=not derouter_key,
    )
    utility_cfg = (tenant.get("writing_model") or {}).get("utility") or {}
    utility_model = str(utility_cfg.get("model") or "gpt-5.6-terra")
    terra_env = os.environ.get("DEROUTER_TERRA_MODEL", "").strip()
    terra_check = terra_env or utility_model
    check(
        bool(terra_check) and "terra" in terra_check.lower(),
        f"utility tier terra id ({terra_check})",
        errors,
        warnings,
        warn=not derouter_key,
    )
    derouter_image_model = os.environ.get("DEROUTER_IMAGE_MODEL", "").strip()
    image_api_cfg = tenant.get("image_api") or {}
    image_gen_cfg = tenant.get("image_generation") or {}
    image_provider = (
        os.environ.get(str(image_api_cfg.get("provider_env") or "IMAGE_PROVIDER"), "").strip()
        or str(image_api_cfg.get("provider") or image_gen_cfg.get("provider") or "").strip()
        or "derouter-rest"
    ).casefold()
    if image_provider == "grsai":
        grsai_key = os.environ.get("GRSAI_API_KEY", "").strip()
        check(
            bool(grsai_key),
            "GRSAI_API_KEY set (Cover image; missing → GRSAI BLOCKER)",
            errors,
            warnings,
            warn=True,
        )
        grsai_model = (
            os.environ.get(str(image_api_cfg.get("model_env") or "GRSAI_IMAGE_MODEL"), "").strip()
            or os.environ.get("GRSAI_IMAGE_MODEL", "").strip()
        )
        check(
            bool(grsai_model) and not grsai_model.casefold().endswith("-vip"),
            f"Grsai image model set and not vip ({grsai_model})",
            errors,
            warnings,
            warn=not grsai_key,
        )
        check(
            image_api_cfg.get("script") == "scripts/excalibur_blog_grsai_gpt_image2_api.py",
            "tenant image_api.script → excalibur_blog_grsai_gpt_image2_api.py",
            errors,
            warnings,
        )
        check(
            image_api_cfg.get("contract") == "shared/grsai-gpt-image-api-contract.md",
            "tenant image_api.contract → grsai-gpt-image-api-contract.md",
            errors,
            warnings,
        )
    else:
        check(
            bool(derouter_image_model),
            "DEROUTER_IMAGE_MODEL set (Cover image model id)",
            errors,
            warnings,
            warn=True,
        )
    brain = tenant.get("writing_model") or {}
    check(
        brain.get("script") == "scripts/excalibur_blog_derouter_opus_chat.py",
        "tenant writing_model.script → excalibur_blog_derouter_opus_chat.py",
        errors,
        warnings,
    )
    check(
        brain.get("contract") == "shared/derouter-opus-brain-contract.md",
        "tenant writing_model.contract → derouter-opus-brain-contract.md",
        errors,
        warnings,
    )
    check(
        brain.get("fail_loud_if_unavailable") is True,
        "tenant writing_model.fail_loud_if_unavailable=true",
        errors,
        warnings,
    )
    powerful_roles = set((brain.get("powerful") or {}).get("roles") or [])
    utility_roles = set((brain.get("utility") or {}).get("roles") or [])
    check(
        powerful_roles == {"writer"},
        "tenant writing_model.powerful.roles is writer-only (Opus 5 = Writer only; everything else Terra)",
        errors,
        warnings,
    )
    check(
        not powerful_roles.intersection({"scout", "title", "sol"}),
        "tenant writing_model.powerful.roles must not include scout/title/sol (Terra roles)",
        errors,
        warnings,
    )
    check(
        {"scout", "title", "sol", "research", "description", "cover-text", "schema", "cover-scene"}.issubset(
            utility_roles
        ),
        "tenant writing_model.utility.roles includes all non-writer text roles",
        errors,
        warnings,
    )

    # Dzen + RF canon must be readable before Scout (when pack enabled)
    if tenant.get("dzen_rf_pack", True):
        rf_path = root / "shared/rf-blocked-entities.json"
        dzen_path = root / "shared/dzen-content-rules.md"
        if rf_path.is_file():
            try:
                rf = json.loads(rf_path.read_text(encoding="utf-8"))
                heroes = {h.get("id") for h in rf.get("hard_deny_heroes", [])}
                check(
                    {"meta", "instagram", "facebook"}.issubset(heroes),
                    "rf-blocked-entities has meta/instagram/facebook",
                    errors,
                    warnings,
                )
            except json.JSONDecodeError:
                check(False, "rf-blocked-entities.json valid JSON", errors, warnings)
        dzen_text = dzen_path.read_text(encoding="utf-8") if dzen_path.is_file() else ""
        check(
            "rules.html" in dzen_text and "Meta" in dzen_text and "Instagram" in dzen_text,
            "dzen-content-rules covers rules.html + Meta/Instagram",
            errors,
            warnings,
        )
        print("NOTE read shared/dzen-content-rules.md + rf-blocked-entities.json BEFORE Scout")

    print(f"SUMMARY errors={len(errors)} warnings={len(warnings)} setup_complete={setup_complete}")
    if errors:
        print("ERRORS: " + "; ".join(errors))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
