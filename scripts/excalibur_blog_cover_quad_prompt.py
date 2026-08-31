#!/usr/bin/env python3
"""Build MCP prompt + batch for ONE quad canvas (4 panels) with hero i2i reference."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from excalibur_blog_meme_cat_gate import (
    count_cat_meme_slots,
    load_meme_catalog,
    pick_non_cat_meme_hint,
    slot_has_cat_meme,
)
from excalibur_blog_identity_real import (
    pick_identity_reference,
    resolve_logo_reference_for_api,
    tenant_uses_logo_reference_in_generation,
)
from excalibur_blog_image_provider import resolve_image_flow
from excalibur_blog_quad_slots import (
    CANVAS_1_SLOTS,
    active_inline_keys,
    all_canvas_specs,
    canvas_specs_for_inline_count,
    inline_count_from_manifest,
    uses_scene_poster_v2,
)
from excalibur_blog_site_base import (
    REDACTED_LITERAL,
    SITE_BASE_PLACEHOLDER,
    SITE_HOST_PLACEHOLDER,
    expand_site_base,
    host_from_public_base,
    redact_site_base,
    resolve_public_base_from_env,
    to_git_safe_site_url,
)


# Stale Cover agents leave «pink «время»» in scene_hint after changing highlight —
# the model follows the leftover and repaints hollow TIME (B73 / INC-20260722-1525).
_PINK_WORD_IN_SCENE = re.compile(
    r"(pink\s*(?:ONLY\s*)?[«\"']\s*)([^»\"']+?)(\s*[»\"'])",
    re.IGNORECASE,
)


def sanitize_cover_scene_hint(scene: str, highlight: str) -> str:
    """Rewrite conflicting pink-word directives in scene_hint to match highlight."""
    hl = (highlight or "").strip()
    if not hl or not (scene or "").strip():
        return scene or ""

    def _repl(match: re.Match[str]) -> str:
        word = match.group(2).strip()
        if word.casefold() == hl.casefold():
            return match.group(0)
        return f"{match.group(1)}{hl}{match.group(3)}"

    return _PINK_WORD_IN_SCENE.sub(_repl, scene)


BODY_LOCK = "face-studio identity: jaw/stubble/hairline/eyes; medium-slim; NOT chubby/puffy"
I2I_EXPRESSION_LOCK = (
    "same person as reference, NEW expression for the hook, "
    "do NOT copy reference closed-mouth smile/pose/head angle; "
    "FORBIDDEN polite studio smile"
)
DEFAULT_COVER_PHONE_CTA = "+7 (993) 574-83-22"
FORBIDDEN_COVER_PHONE = "+7 922 001 65 05"
BOARD_STATIONERY = "tape/pins/strings/paper scraps; high-key #FFF/gold; not noir"
INLINE_BAN_EXTRA = (
    "icon slogans; empty cells; desk scene; cover copy; celebrity memes; "
    "stock model man; handsome realtor co-host; generated stranger presenter; "
    "large human on inline; meme person >15% frame; invented meme face; "
    "WordPress; Gutenberg; wp-admin; block editor; theme chrome; cookie bar; "
    "overlapping headline stickers meme cat phone logo; timid system font; "
    "wall of tiny labels; empty stock; wordpress screenshot"
)
WOW_POSTER_BAN = (
    "WordPress; Gutenberg; Add title; Publish; Dashboard; wp-admin; "
    "block editor; theme chrome; cookie bar; timid system font; "
    "wall of tiny labels; empty stock; wordpress screenshot"
)
LOGO_DRAW_HARD_BAN = (
    "NO drawn logo/wordmark/lockup/curtains+red flower/dashed logo frame/gold house; "
    "factory cropped-img_7143.png PNG paste after split"
)
LOGO_WHITE_PLATE_BAN = (
    "NO white/gray card/plate/tablichka under TOP-RIGHT pad; factory alpha PNG after split only"
)
LOGO_REFERENCE_INTEGRATION = (
    "Reference logo: exact brand mark small top-right, transparent alpha, NO white/gray plate/card"
)
LOGO_REFERENCE_BAN = (
    "NO second logo copy; NO logo comparison table; NO dashed logo frame; "
    "NO gold house-with-heart logo; NO УЮТНЫЕ КВАРТИРЫ В АРЕНДУ subtitle in art"
)
NO_OVERLAP_RULE = (
    "Separate zones — headline top, Wordstat stickers, meme cat bottom-left ≤12%, "
    "phone quiet zone on bottom edge or side paper ONLY; TOP-RIGHT empty logo pad; "
    "phone/logo NEVER over cat/meme/sticky/headline"
)
PHONE_IN_SCENE_RULE = (
    "Phone EXACT «{phone}» painted IN scene as tape strip, torn paper, door plate, "
    "fridge magnet, or poster edge — readable Cyrillic, pretty, NOT opaque pill/button/banner; "
    "quiet zone on bottom edge or side margin; NEVER over cat bottom-left, sticky, meme, or headline"
)
MEME_CATALOG_REL = "memory/cover/meme-top100.json"
MEME_STICKER_INLINE_MAX_SHARE = 0.15
MAX_CAT_MEME_SLOTS_PER_ARTICLE = 1
CAT_MEME_QUOTA_RULE = (
    "CAT-MEME QUOTA: max ONE cat-meme sticker across entire 8-panel set (cover + 7 inlines). "
    "Prefer cover OR one inline — never both. All other meme slots = people-memes/reaction templates "
    f"from {MEME_CATALOG_REL} (Roll Safe, Harold, Pepe, Wojak, Gigachad, etc.) — "
    "NOT grumpy/ginger/tardar/smudge cat repeats."
)
NON_CAT_MEME_INLINE_HINT = (
    f"tiny people-meme sticker only (≤{int(MEME_STICKER_INLINE_MAX_SHARE * 100)}% frame, "
    f"corner accent — Roll Safe / Harold / Pepe / reaction face from {MEME_CATALOG_REL}; NO cat)"
)
MAX_MCP_PROMPT_CHARS = 3500
# Compact limits leave headroom under 3500 after style boilerplate (INC-20260721-0837).
# Cover raw ≈80–140 (from blog-hero lock); inline ≈100–220. Long MUST/face essays
# starve host space (B80 / INC-20260724-0837) and bilingual essays blow MCP budget.
# After EXCALIBUR-stamp ban (INC-20260723-1223) shared locks ate most of the budget
# (B79 / INC-20260723-1626): keep one shared «Inline all» suffix (not ×3) and reclaim
# from shared negatives first — never force agents to empty scene_hint.
COVER_SCENE_HINT_COMPACT = 200
INLINE_SCENE_HINT_COMPACT = 180
COVER_SCENE_HINT_RAW_TARGET_MAX = 140
INLINE_SCENE_HINT_RAW_TARGET_MAX = 220
# Backward-compatible alias (inline / general budget messaging).
SCENE_HINT_RAW_TARGET_MAX = INLINE_SCENE_HINT_RAW_TARGET_MAX
# Minimum empty-base headroom so ≈100-char scene_hint ×4 still fits under 3500.
MIN_EMPTY_PROMPT_HEADROOM = 500
_COVER_FACE_ESSAY = re.compile(
    r"\bMUST\b|\bglasses\b|\bquiff\b|\bbeard\b|\bfacial\b",
    re.IGNORECASE,
)
# Live host for runtime URL checks only — never write this into git batch JSON.
# Prefer PUBLIC_SITE_URL hostname; fallback for offline validate when env empty.
_LEGACY_REFERENCE_HOST_FALLBACK = ""  # no personal default host
MCP_RESOLUTION = "2K"
KIE_IMAGE_MODEL = "gpt-image-2-image-to-image"


def required_reference_host_runtime() -> str:
    """Hostname accepted in live reference URLs (env or legacy fallback)."""
    return host_from_public_base() or _LEGACY_REFERENCE_HOST_FALLBACK


def project_root() -> Path:
    env_root = os.environ.get("EXCALIBUR_PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def compact(value: object, limit: int) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def inline_panel_prompt(
    slot: dict,
    types_catalog: dict,
    *,
    logo_paste: bool = False,
    logo_reference: bool = False,
    cat_meme_allowed: bool = False,
    people_meme_hint: str = "",
) -> str:
    type_id = slot.get("visual_type") or "fact_card"
    type_def = (types_catalog.get("types") or {}).get(type_id) or {}
    label = type_def.get("label_ru", type_id)
    h2 = compact(slot.get("h2_anchor", ""), 72)
    scene = compact(slot.get("scene_hint", ""), INLINE_SCENE_HINT_COMPACT)
    base = f"{label}; «{h2}»; {scene}."
    labels = [str(x).strip() for x in (slot.get("labels") or []) if str(x).strip()]
    if labels:
        exact = " | ".join(labels)
        base += f" TXT:{exact}."
    if slot.get("meme_sticker") or cat_meme_allowed:
        if cat_meme_allowed:
            base += (
                f" +tiny cat-meme sticker only (≤{int(MEME_STICKER_INLINE_MAX_SHARE * 100)}% frame, "
                f"bottom-left or bottom-right corner only — NEVER top-right pad; "
                f"ONLY cat slot this article; from {MEME_CATALOG_REL}; NO co-host human)."
            )
        else:
            hint = people_meme_hint or NON_CAT_MEME_INLINE_HINT
            base += f" +{hint}."
    if logo_reference and logo_paste:
        base += " Logo ref top-right, no plate."
    elif logo_paste:
        base += " TOP-RIGHT empty pad; no drawn logo; no white/gray plate."
    elif logo_reference:
        base += " TOP-RIGHT clean; NO visible brand logo on this panel; no white/gray plate."
    else:
        base += " TOP-RIGHT clean; no logo; no white/gray plate."
    return base


def _manifest_slot_keys(manifest: dict) -> tuple[str, ...]:
    inline_count = inline_count_from_manifest(manifest)
    keys = ["cover"] + list(active_inline_keys(inline_count))
    return tuple(keys)


def warn_long_scene_hints(manifest: dict) -> None:
    """Advisory: long raw scene_hint blows MCP budget; cover face essays omit host."""
    slots = manifest.get("slots") or {}
    for key in _manifest_slot_keys(manifest):
        raw = " ".join(str((slots.get(key) or {}).get("scene_hint") or "").split())
        if not raw:
            continue
        if key == "cover":
            if len(raw) > COVER_SCENE_HINT_RAW_TARGET_MAX:
                print(
                    f"WARN cover.scene_hint is {len(raw)} chars "
                    f"(target ≈80–{COVER_SCENE_HINT_RAW_TARGET_MAX}; "
                    "prefer short hero lock from blog-hero — long hints omit host). "
                    "Shorten before --write-batch.",
                    file=sys.stderr,
                )
            elif _COVER_FACE_ESSAY.search(raw) and len(raw) > 100:
                print(
                    "WARN cover.scene_hint looks like a MUST/face-feature essay "
                    "(tenant visual_lock). Prefer short hero lock from blog-hero + "
                    "one object; face lock is already in i2i reference "
                    "(INC-20260724-0837).",
                    file=sys.stderr,
                )
            continue
        if len(raw) > INLINE_SCENE_HINT_RAW_TARGET_MAX:
            print(
                f"WARN {key}.scene_hint is {len(raw)} chars "
                f"(target ≤{INLINE_SCENE_HINT_RAW_TARGET_MAX}; "
                "bilingual essays blow MCP budget). "
                "Shorten to compact RU/EN labels before --write-batch.",
                file=sys.stderr,
            )


def _topic_blob(manifest: dict, article_dir: Path | None = None) -> str:
    parts = [
        str(manifest.get("topic_id") or ""),
        str(manifest.get("cover_hook") or ""),
        " ".join(str(x) for x in (manifest.get("cover_keys_ru") or [])),
    ]
    slots = manifest.get("slots") or {}
    for key in _manifest_slot_keys(manifest):
        slot = slots.get(key) or {}
        parts.append(str(slot.get("h2_anchor") or ""))
        parts.append(str(slot.get("scene_hint") or ""))
        parts.append(str(slot.get("alt") or ""))
    if article_dir is not None:
        parts.append(article_dir.name)
    return " ".join(parts).lower()


def is_cursor_sdk_local_agent_topic(manifest: dict, article_dir: Path | None = None) -> bool:
    """Detect Cursor SDK / «локальный ai агент» covers (B72 fact lock)."""
    blob = _topic_blob(manifest, article_dir)
    has_sdk = any(
        marker in blob
        for marker in (
            "cursor sdk",
            "cursor-sdk",
            "@cursor/sdk",
            "agent.create",
            "composer-2",
        )
    )
    has_local = any(
        marker in blob
        for marker in ("локальн", "lokalnyy", "localnyy", "local agent", "local ai")
    )
    has_agent = any(
        marker in blob for marker in ("ai агент", "ai-agent", "ai agent", "агент")
    )
    return has_sdk or (has_local and has_agent)


def topic_fact_lock_lines(
    manifest: dict, article_dir: Path | None = None
) -> list[str]:
    """Short prompt lines that lock topic facts the model often invents wrong."""
    lines: list[str] = []
    if is_cursor_sdk_local_agent_topic(manifest, article_dir):
        # Keep short: full bilingual essays blow MCP 3500 (INC-20260721-0837).
        lines.append(
            "FACT LOCK SDK/local: local=files on disk not offline; "
            "Chat YES/Ollama NO/SDK YES net; never «интернет не нужен» on Chat/SDK; "
            "one hook — no «Ключевые темы»/keys list."
        )
    return lines


def validate_reference_url(ref_url: str) -> bool:
    """Accept live site host URL, {{SITE_BASE}}/… path, or reject [REDACTED]/tool masks."""
    value = (ref_url or "").strip()
    host = required_reference_host_runtime()
    if not value:
        return False
    if REDACTED_LITERAL in value:
        print(
            "❌ COVER HERO BLOCKER: reference_url_hosted contains [REDACTED]; "
            f"use {SITE_BASE_PLACEHOLDER}/wp-content/... or a live {host} URL",
            file=sys.stderr,
        )
        return False
    if value.startswith(SITE_BASE_PLACEHOLDER):
        path = value[len(SITE_BASE_PLACEHOLDER) :]
        if "/wp-content/" in path or path.startswith("/wp-content/"):
            return True
        print(
            f"❌ COVER HERO BLOCKER: {SITE_BASE_PLACEHOLDER} reference must point at /wp-content/... media",
            file=sys.stderr,
        )
        return False
    if host and host in value:
        return True
    # Also accept legacy fallback host if env host differs (offline / mixed artifacts).
    if _LEGACY_REFERENCE_HOST_FALLBACK in value and _LEGACY_REFERENCE_HOST_FALLBACK != host:
        return True
    print(
        f"❌ COVER HERO BLOCKER: reference_url_hosted must use stable {host} "
        f"WordPress media URL or {SITE_BASE_PLACEHOLDER}/wp-content/..., got: {value}",
        file=sys.stderr,
    )
    return False


def git_safe_reference_url(ref_url: str) -> str:
    """Write {{SITE_BASE}}/path into committed batch; keep non-site hosts as-is."""
    value = (ref_url or "").strip()
    if not value:
        return value
    if value.startswith(SITE_BASE_PLACEHOLDER):
        return value
    safe = to_git_safe_site_url(value)
    if safe.startswith(SITE_BASE_PLACEHOLDER):
        return safe
    host = required_reference_host_runtime()
    if host and host in value and "://" in value:
        path = urlparse(value).path or "/"
        return f"{SITE_BASE_PLACEHOLDER}{path}"
    if _LEGACY_REFERENCE_HOST_FALLBACK in value and "://" in value:
        path = urlparse(value).path or "/"
        return f"{SITE_BASE_PLACEHOLDER}{path}"
    return redact_site_base(value)


def run_motif_gate(root: Path, manifest: dict, article_dir: Path) -> bool:
    """Preflight anti-repeat if cover_motifs present in manifest."""
    motifs = (manifest.get("cover_motifs") or {})
    if not isinstance(motifs, dict) or not motifs:
        return True
    import subprocess

    cmd = [
        sys.executable,
        str(root / "scripts/excalibur_blog_cover_motif_gate.py"),
        "check",
        "--topic-id",
        str(manifest.get("topic_id") or ""),
        "--slug",
        str(manifest.get("slug") or article_dir.name),
    ]
    field_map = {
        "composition": "composition",
        "location": "location",
        "meme": "meme",
        "prop_set": "prop-set",
        "sticker_set": "sticker-set",
        "joke": "joke",
    }
    for key, flag in field_map.items():
        value = str(motifs.get(key) or "").strip()
        if value:
            cmd.extend([f"--{flag}", value])
    proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True, check=False)
    if proc.returncode != 0:
        if proc.stdout.strip():
            print(proc.stdout.strip(), file=sys.stderr)
        if proc.stderr.strip():
            print(proc.stderr.strip(), file=sys.stderr)
        return False
    if proc.stdout.strip():
        print(proc.stdout.strip())
    return True


def validate_prompt_budget(prompt: str) -> bool:
    prompt_chars = len(prompt)
    if prompt_chars <= MAX_MCP_PROMPT_CHARS:
        return True
    print(
        f"❌ COVER PROMPT BLOCKER: MCP prompt is {prompt_chars} chars, max {MAX_MCP_PROMPT_CHARS}. "
        "Shorten cover scene_hint to ≈80–140 (blog-hero lock, no MUST/face essay) "
        "and each inline to ≈100–220 (compact RU/EN labels, not bilingual essays); "
        "do not duplicate style/negative blocks per panel (one shared «Inline all» lock). "
        "If hints are already short and budget still fails, reclaim chars from shared "
        "style/ban/Inline-all text in this script — do not empty scene_hint. "
        f"Script compact caps: cover≤{COVER_SCENE_HINT_COMPACT}, inline≤{INLINE_SCENE_HINT_COMPACT}.",
        file=sys.stderr,
    )
    return False


def style_allows_cat_stickers(style: dict) -> bool:
    """True when style preset explicitly allows funny cat sticker cutouts."""
    if style.get("allows_animal_stickers") is True:
        return True
    motif = str(style.get("allowed_animal_motif") or "").strip().casefold()
    return "cat" in motif


def load_tenant_cover_config(root: Path) -> dict:
    cfg_path = root / "shared" / "tenant-config.json"
    if not cfg_path.is_file():
        return {}
    try:
        tenant = json.loads(cfg_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    channels = tenant.get("cta_channels") or {}
    return {
        "cover_mode": str(tenant.get("cover_mode") or "").strip(),
        "phone_display": str(channels.get("phone_display") or DEFAULT_COVER_PHONE_CTA).strip(),
    }


def tenant_uses_brand_logo_paste(root: Path, style: dict | None = None) -> bool:
    if tenant_uses_logo_reference_in_generation(root):
        return False
    tenant = load_tenant_cover_config(root)
    mode = str(tenant.get("cover_mode") or "").strip().casefold()
    if mode in {"brand_logo_paste", "brand_logo_composite", "paste_png"}:
        return True
    if style:
        hero_mode = str(style.get("cover_hero_mode") or "").strip().casefold()
        if hero_mode in {"brand_logo_paste", "brand_logo_composite", "paste_png"}:
            return True
        if style.get("skip_human_host") is True and hero_mode == "brand_logo_paste":
            return True
    return False


def cover_phone_cta_for_manifest(manifest: dict, root: Path) -> str:
    manifest_phone = str(manifest.get("cover_phone_cta") or "").strip()
    if manifest_phone and manifest_phone != FORBIDDEN_COVER_PHONE:
        return manifest_phone
    tenant = load_tenant_cover_config(root)
    return str(tenant.get("phone_display") or DEFAULT_COVER_PHONE_CTA)


def style_is_situational_cat_hero(style: dict) -> bool:
    """Cat is the cover hero (not host+sticker cats)."""
    mode = str(style.get("cover_hero_mode") or "").strip().casefold()
    if mode in {"situational_cat", "cat_hero", "situational_cat_hero"}:
        return True
    if style.get("skip_human_host") is True and style_allows_cat_stickers(style):
        return True
    motif = str(style.get("allowed_animal_motif") or "").strip().casefold()
    return motif in {"situational_cat_hero", "cat_hero"}


def resolve_manifest_inline_logo_keys(manifest: dict, root: Path) -> set[str]:
    cfg = load_tenant_cover_config(root)
    tenant = load_json(root / "shared" / "tenant-config.json") if (root / "shared" / "tenant-config.json").is_file() else {}
    composite = (tenant.get("logo_composite") or {})
    raw = manifest.get("logo_paste_inline_slots") or manifest.get("inline_logo_slots")
    if isinstance(raw, list) and raw:
        return {str(x).strip() for x in raw if str(x).strip()}
    defaults = composite.get("inline_logo_slots_default") or ["inline_1", "inline_3", "inline_7"]
    return {str(x).strip() for x in defaults}


def build_prompt(
    manifest: dict,
    style: dict,
    hero: dict,
    types_catalog: dict,
    design_code: dict,
    article_dir: Path | None = None,
    *,
    canvas_slots: tuple[str, ...] | None = None,
    has_cover: bool = True,
    brand_logo_paste: bool = False,
    logo_reference_in_generation: bool = False,
    cover_phone_cta: str = DEFAULT_COVER_PHONE_CTA,
    inline_logo_keys: set[str] | None = None,
    meme_catalog: dict | None = None,
) -> str:
    slots = manifest.get("slots") or {}
    canvas_slots = canvas_slots or tuple(CANVAS_1_SLOTS)

    def slot(key: str) -> dict:
        return slots.get(key) or {}

    fact_locks = topic_fact_lock_lines(manifest, article_dir)
    cat_ok = style_allows_cat_stickers(style)
    cat_hero = style_is_situational_cat_hero(style)
    catalog = meme_catalog or {}
    _, cat_slot_keys = count_cat_meme_slots(manifest, catalog) if catalog else (0, [])
    cover_cat_allowed = "cover" in cat_slot_keys
    people_meme_hint = pick_non_cat_meme_hint(catalog) if catalog else ""

    style_prefix = compact(
        style.get("global_prompt_prefix")
        or design_code.get("cover_panel_prompt_block")
        or design_code.get("inline_information_block")
        or "",
        380,
    )
    if not style_prefix:
        style_prefix = (
            "Dense RU editorial collage, WHITE #FFFFFF, BLACK #141821 Cyrillic ink, "
            "gold #dcc5a1 one accent only. Torn paper, gold tape/sticky, informative UI cards."
        )

    quadrant_labels = ("Top-left", "Top-right", "Bottom-left", "Bottom-right")
    panel_lines: list[str] = []

    inline_logo_keys = inline_logo_keys or set()

    def inline_prompt_for(key: str) -> str:
        return inline_panel_prompt(
            slot(key),
            types_catalog,
            logo_paste=(key in inline_logo_keys),
            logo_reference=logo_reference_in_generation,
            cat_meme_allowed=(key in cat_slot_keys),
            people_meme_hint=people_meme_hint,
        )

    if has_cover and "cover" in canvas_slots:
        cover = slot("cover")
        highlight = compact(manifest.get("cover_hook_highlight", ""), 24)
        highlight_rule = (
            f'paint ONLY the highlight word "{highlight}" in gold #dcc5a1'
            if highlight
            else "paint at most ONE punch word in gold #dcc5a1"
        )
        cover_emotion = compact(
            str(cover.get("cover_emotion") or manifest.get("cover_emotion") or ""), 120
        )
        cover_scene = sanitize_cover_scene_hint(str(cover.get("scene_hint") or ""), highlight)
        cover_hook_text = compact(manifest.get("cover_hook", ""), 120)
        cover_sticky = compact(str(cover.get("sticky") or ""), 48)
        sticky_lock = (
            f" Small gold sticky with EXACTLY «{cover_sticky}» in Cyrillic."
            if cover_sticky
            else ""
        )
        cover_meme_clause = (
            "cat-meme sticker bottom-left ≤12% (ONLY cat slot this article)"
            if cover_cat_allowed
            else f"people-meme sticker bottom-left ≤12% ({people_meme_hint or 'Roll Safe / Harold / Pepe'}; NO cat)"
        )
        if logo_reference_in_generation:
            emotion_clause = f"Expr: {cover_emotion}." if cover_emotion else ""
            panel_lines.append(
                f"TL COVER WOW POSTER (magazine, not stock): «{cover_hook_text}» bold DISPLAY Cyrillic readable, {highlight_rule}; "
                f"sticky «{cover_sticky or 'Залог вернут?'}»; scene props; natural daylight clean white balance, "
                f"NO yellow/amber cast, NO muddy skin, NO winter/snow. "
                f"NO phone in gen. {LOGO_REFERENCE_INTEGRATION}. "
                f"{emotion_clause} soft daylight crisp sharp; gold tape; 1-3 Wordstat; "
                f"{compact(cover_scene, COVER_SCENE_HINT_COMPACT)}; {cover_meme_clause}; "
                f"{BOARD_STATIONERY}; #FFF"
            )
        elif brand_logo_paste:
            emotion_clause = f"Expr: {cover_emotion}." if cover_emotion else ""
            phone_clause = PHONE_IN_SCENE_RULE.format(phone=cover_phone_cta)
            panel_lines.append(
                f"TL COVER WOW POSTER (magazine, not stock): «{cover_hook_text}» bold DISPLAY Cyrillic readable, {highlight_rule}; "
                f"sticky «{cover_sticky or 'Залог вернут?'}»; scene props; natural daylight clean white balance, "
                f"NO yellow/amber cast, NO muddy skin, NO winter/snow. "
                f"NO logo in gen. {phone_clause}. "
                f"{emotion_clause} soft daylight crisp sharp; gold tape; 1-3 Wordstat; "
                f"{compact(cover_scene, COVER_SCENE_HINT_COMPACT)}; {cover_meme_clause}; "
                f"TOP-RIGHT empty clear pad — no logo, no house icon, no «Добрый дом» lettering, no plate, no sticker; "
                f"{BOARD_STATIONERY}; #FFF"
            )
        else:
            emotion_clause = (
                f"Expression: {cover_emotion}. {I2I_EXPRESSION_LOCK}."
                if cover_emotion
                else f"{I2I_EXPRESSION_LOCK}."
            )
            panel_lines.append(
                f"TL COVER TXT «{cover_hook_text}» bold Cyrillic black, {highlight_rule}.{sticky_lock} "
                f"Phone EXACT «{cover_phone_cta}» readable CTA sticker. "
                f"Host i2i left ({BODY_LOCK}); {emotion_clause} natural daylight, no yellow cast; "
                f"{compact(cover_scene, COVER_SCENE_HINT_COMPACT)}; "
                f"1-2 meme stickers; {BOARD_STATIONERY}; Wordstat/Tyumen; #FFF; perfect Cyrillic"
            )
        inline_keys = [k for k in canvas_slots if k != "cover"]
        for label, key in zip(quadrant_labels[1:], inline_keys[:3]):
            panel_lines.append(f"{label} inline: {inline_prompt_for(key)}")
    else:
        for label, key in zip(quadrant_labels, list(canvas_slots)[:4]):
            panel_lines.append(f"{label} inline: {inline_prompt_for(key)}")

    if logo_reference_in_generation:
        ban_line = (
            "Ban: dark/low-key; inventory props; celebrity memes; EXCALIBUR stamp; chubby host; "
            f"stock/generated man co-host on inline; large meme person on inline; "
            f"{INLINE_BAN_EXTRA}; {LOGO_REFERENCE_BAN}; NO white/gray plate under logo."
        )
    else:
        ban_line = (
            "Ban: dark/low-key; inventory props; celebrity memes; EXCALIBUR stamp; chubby host; "
            f"stock/generated man co-host on inline; large meme person on inline; "
            f"{INLINE_BAN_EXTRA}; {LOGO_DRAW_HARD_BAN}; {LOGO_WHITE_PLATE_BAN}."
        )
    if has_cover and logo_reference_in_generation:
        reference_line = (
            f"Cover TL: logo from reference image only — {LOGO_REFERENCE_INTEGRATION}; "
            "NO phone in generation (factory adds post-composite)."
        )
    elif has_cover and brand_logo_paste:
        reference_line = (
            "Cover TL: NO host; NO logo in gen (factory cropped-img_7143.png alpha after split); "
            f"phone IN scene only — {PHONE_IN_SCENE_RULE.format(phone=cover_phone_cta)}; "
            "NEVER post-composite pill."
        )
    elif has_cover:
        reference_line = (
            f"Cover TL only: i2i face-studio-2026-06-23 ({BODY_LOCK}); {I2I_EXPRESSION_LOCK}; "
            "invent scene; no AI hero-ref."
        )
    elif logo_reference_in_generation:
        reference_line = (
            f"Inlines: logo from reference on 2–3 panels only (inline_1/3/7 default); "
            f"{LOGO_REFERENCE_INTEGRATION}; other panels NO visible logo; "
            f"{LOGO_REFERENCE_BAN}; "
            f"people-memes only as tiny stickers (≤{int(MEME_STICKER_INLINE_MAX_SHARE * 100)}% frame, "
            f"never top-right pad) from real templates in {MEME_CATALOG_REL}; "
            "mix sketch/table/chart/scheme collage — not text walls."
        )
    else:
        reference_line = (
            "Inlines: NO host face; NO stock/generated man; NO large human co-host/presenter; "
            f"NO brand logo in generation (factory pastes PNG on 2–3 panels only, TOP-RIGHT pad); "
            f"{LOGO_DRAW_HARD_BAN}; {LOGO_WHITE_PLATE_BAN}; "
            f"people-memes only as tiny stickers (≤{int(MEME_STICKER_INLINE_MAX_SHARE * 100)}% frame, "
            f"never top-right pad) from real templates in {MEME_CATALOG_REL}; "
            "mix sketch/table/chart/scheme collage — not text walls."
        )
    inline_suffix = (
        f"Inline all: #FFF collage, gold/black Cyrillic labels, {BOARD_STATIONERY}; "
        "dense facts/numbers; exact TXT per panel; meme only if +meme AND sticker-scale; "
        f"{CAT_MEME_QUOTA_RULE}; "
        "no human hero on inline; no icon soup; zero typos."
    )

    lines = [
        style_prefix,
        CAT_MEME_QUOTA_RULE,
        "Canvas 2048x1152 exact 2x2; four 16:9 panels (1024x576); thin white gutters; no bleed.",
        "",
        ban_line,
        "TEXT LANGUAGE LOCK: all visible text is RUSSIAN Cyrillic only; exact LABELS per panel only.",
        "",
        reference_line,
        "",
        *panel_lines,
        "",
        inline_suffix,
    ]
    if fact_locks:
        lines.extend(["", *fact_locks])
    return "\n".join(line for line in lines if line)


SCENE_POSTER_COVER_BAN = (
    "BAN: meme cutouts, cat stickers, Roll Safe, Harold, Pepe, Wordstat sticker soup, "
    "torn-paper collage, gold-glitter type, yellow sticky notes, split white-panel+photo, "
    "phone pill, post-composite phone, model-drawn logo, house-with-heart, logo plate, "
    "empty stock room, WordPress UI, wow poster collage, dark cinematic"
)


def build_standalone_cover_prompt(
    manifest: dict,
    style: dict,
    design_code: dict,
    *,
    cover_phone_cta: str = DEFAULT_COVER_PHONE_CTA,
) -> str:
    cover = (manifest.get("slots") or {}).get("cover") or {}
    style_prefix = compact(
        style.get("cover_standalone_prompt_prefix")
        or design_code.get("cover_panel_prompt_block")
        or "",
        520,
    )
    cover_hook = compact(manifest.get("cover_hook", ""), 80)
    cover_scene = sanitize_cover_scene_hint(
        str(cover.get("scene_hint") or manifest.get("cover_scene") or ""),
        str(manifest.get("cover_hook_highlight") or ""),
    )
    cover_emotion = compact(str(cover.get("cover_emotion") or manifest.get("cover_emotion") or ""), 120)
    phone_clause = PHONE_IN_SCENE_RULE.format(phone=cover_phone_cta)
    hook_clause = f'Optional short Cyrillic hook in scene: «{cover_hook}».' if cover_hook else ""
    emotion_clause = f"Emotion: {cover_emotion}." if cover_emotion else ""
    lines = [
        style_prefix,
        "Standalone cover canvas 2048x1152 exact 16:9 full-bleed — NOT a quad quadrant.",
        hook_clause,
        emotion_clause,
        phone_clause,
        f"Scene: {compact(cover_scene, COVER_SCENE_HINT_COMPACT)}.",
        "TOP-RIGHT empty clear pad 8-12% — no logo, no house icon, no «Добрый дом», no plate.",
        SCENE_POSTER_COVER_BAN + ".",
        "TEXT LANGUAGE LOCK: visible text RUSSIAN Cyrillic only; short readable labels.",
        "Magazine-clean editorial still — designed inline energy as cinematic scene poster.",
    ]
    return "\n".join(line for line in lines if line)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", required=True)
    ap.add_argument("--manifest", default="cover/quad-manifest.json")
    ap.add_argument("--canvas-index", type=int, default=0, help="Write batch for canvas 1 or 2; 0=all")
    ap.add_argument("--write-batch", action="store_true", help="Write quad-mcp-batch JSON per canvas")
    args = ap.parse_args()

    root = project_root()
    article_dir = Path(args.article_dir)
    if not article_dir.is_absolute():
        article_dir = root / article_dir

    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = article_dir / manifest_path
    if not manifest_path.is_file():
        print(f"❌ PROMPT BLOCKER: {manifest_path} not found", file=sys.stderr)
        return 1

    manifest = load_json(manifest_path)
    hero = load_json(root / manifest.get("blog_hero", "memory/cover/blog-hero.json"))
    style = load_json(
        root
        / manifest.get(
            "style_file",
            "memory/cover/quad-style-pink-cat-digital-collage-ru.json",
        )
    )
    types_path = root / manifest.get("inline_types_catalog", "memory/cover/inline-visual-types.json")
    types_catalog = load_json(types_path) if types_path.is_file() else {"types": {}}
    design_code_path = root / style.get("design_code", "memory/cover/cover-design-code.json")
    design_code = load_json(design_code_path) if design_code_path.is_file() else {}
    meme_catalog = load_meme_catalog(root)

    cat_hero = style_is_situational_cat_hero(style)
    local_reference = str(style.get("local_reference") or "").strip()
    brand_logo_paste = tenant_uses_brand_logo_paste(root, style)
    logo_reference_in_generation = tenant_uses_logo_reference_in_generation(root)
    cover_phone_cta = cover_phone_cta_for_manifest(manifest, root)

    inline_count = inline_count_from_manifest(manifest)
    scene_v2 = uses_scene_poster_v2(root)
    canvas_specs = all_canvas_specs(inline_count) if scene_v2 else canvas_specs_for_inline_count(inline_count)
    if args.canvas_index:
        canvas_specs = [s for s in canvas_specs if s["index"] == args.canvas_index]
        if not canvas_specs:
            print(f"❌ PROMPT BLOCKER: unknown canvas-index={args.canvas_index}", file=sys.stderr)
            return 1

    for spec in canvas_specs:
        has_cover = bool(spec.get("has_cover"))
        standalone_cover = bool(spec.get("standalone_cover"))
        canvas_slots = tuple(spec["slots"])
        identity_spec: dict[str, str] = {}
        identity_rel = ""
        if has_cover and not standalone_cover and not brand_logo_paste and not logo_reference_in_generation:
            topic_id = str(manifest.get("topic_id") or "").strip()
            slug = str(manifest.get("slug") or article_dir.name).strip()
            identity_spec = pick_identity_reference(topic_id, slug)
            identity_rel = f"memory/cover/assets/identity-real/{identity_spec['file']}"
            identity_path = root / identity_rel
            if not identity_path.is_file():
                print(
                    f"❌ IDENTITY BLOCKER: missing live reference {identity_rel} "
                    f"(stage via memory/setup/visual-inbox/)",
                    file=sys.stderr,
                )
                return 1
            ref_url = (hero.get("reference_url_hosted") or "").strip()
            if not ref_url:
                print("❌ COVER HERO BLOCKER: reference_url_hosted missing", file=sys.stderr)
                return 1
            if not validate_reference_url(ref_url):
                return 1
            batch_ref_url = git_safe_reference_url(ref_url)
        else:
            batch_ref_url = ""

        warn_long_scene_hints(manifest)
        inline_logo_keys = resolve_manifest_inline_logo_keys(manifest, root)
        if standalone_cover:
            prompt = build_standalone_cover_prompt(
                manifest,
                style,
                design_code,
                cover_phone_cta=cover_phone_cta,
            )
        else:
            prompt = build_prompt(
                manifest,
                style,
                hero,
                types_catalog,
                design_code,
                article_dir=article_dir,
                canvas_slots=canvas_slots,
                has_cover=has_cover,
                brand_logo_paste=brand_logo_paste,
                logo_reference_in_generation=logo_reference_in_generation,
                cover_phone_cta=cover_phone_cta,
                inline_logo_keys=inline_logo_keys,
                meme_catalog=meme_catalog,
            )
        if not validate_prompt_budget(prompt):
            return 1
        prompt_path = article_dir / "cover" / Path(str(spec["prompt_file"])).name
        prompt_path.write_text(prompt + "\n", encoding="utf-8")
        print(f"OK prompt={prompt_path} chars={len(prompt)} max={MAX_MCP_PROMPT_CHARS}")

        if not args.write_batch:
            continue

        if has_cover and not standalone_cover and not run_motif_gate(root, manifest, article_dir):
            print("❌ COVER MOTIF BLOCKER: 14-day anti-repeat collision", file=sys.stderr)
            return 1
        if standalone_cover and not run_motif_gate(root, manifest, article_dir):
            print("❌ COVER MOTIF BLOCKER: 14-day anti-repeat collision", file=sys.stderr)
            return 1

        required_errors: list[str] = []
        if has_cover or standalone_cover:
            if not str(manifest.get("cover_hook") or "").strip():
                required_errors.append("cover_hook empty")
            if not str(manifest.get("cover_hook_highlight") or "").strip():
                required_errors.append("cover_hook_highlight empty")
        for key in canvas_slots:
            if key in {"panel_quiet_pad"}:
                continue
            slot_data = (manifest.get("slots") or {}).get(key) or {}
            if not str(slot_data.get("scene_hint") or "").strip():
                required_errors.append(f"{key}.scene_hint empty")
            if not str(slot_data.get("alt") or "").strip():
                required_errors.append(f"{key}.alt empty")
        if required_errors:
            print("❌ COVER MANIFEST BLOCKER:", file=sys.stderr)
            for err in required_errors:
                print(f"  - {err}", file=sys.stderr)
            return 1

        logo_ref_spec = resolve_logo_reference_for_api(root) if logo_reference_in_generation else {}
        logo_ref_url = ""
        if logo_reference_in_generation:
            raw_logo_url = str(logo_ref_spec.get("url") or "").strip()
            if raw_logo_url:
                if validate_reference_url(raw_logo_url):
                    logo_ref_url = git_safe_reference_url(raw_logo_url)
                else:
                    logo_ref_url = raw_logo_url if raw_logo_url.startswith("http") else ""

        api_input: dict[str, object] = {
            "prompt": prompt,
            "aspect_ratio": "16:9",
            "resolution": MCP_RESOLUTION,
        }
        if batch_ref_url and not brand_logo_paste and not logo_reference_in_generation:
            api_input["input_urls"] = [batch_ref_url]
        if logo_reference_in_generation:
            api_input["logo_reference_local"] = str(logo_ref_spec.get("local") or "")
            api_input["logo_reference_url"] = logo_ref_url
            api_input["logo_reference_in_generation"] = True
            if logo_ref_url:
                api_input["input_urls"] = [logo_ref_url]

        image_flow = resolve_image_flow(root)
        apply_script = (
            "python3 scripts/excalibur_blog_cover_standalone_apply.py "
            f"--article-dir <article_dir>"
            if standalone_cover
            else (
                "python3 scripts/excalibur_blog_quad_apply.py "
                f"--article-dir <article_dir> --canvas-index {spec['index']} --inject-html"
            )
        )
        batch = {
            "pipeline": manifest.get("pipeline") or (
                "scene_poster_v2_standalone_cover" if standalone_cover else "quad_canvas_2x_image_api_longform"
            ),
            "canvas_index": spec["index"],
            "standalone_cover": standalone_cover,
            "identity_reference_local": identity_rel if has_cover and not brand_logo_paste and not logo_reference_in_generation else "",
            "identity_reference_id": identity_spec.get("id", "") if has_cover and not brand_logo_paste and not logo_reference_in_generation else "",
            "logo_reference_local": str(logo_ref_spec.get("local") or "") if logo_reference_in_generation else "",
            "logo_reference_url": logo_ref_url if logo_reference_in_generation else "",
            "logo_reference_in_generation": bool(logo_reference_in_generation),
            "reference_url_hosted": batch_ref_url,
            "output_canvas": spec["canvas_file"],
            "result_path": spec["result_file"],
            "slots": list(canvas_slots),
            "preferred_image_flow": {
                "provider": image_flow["provider"],
                "script": image_flow["script"],
                "resolution": MCP_RESOLUTION,
                "note": image_flow["note"],
                "apply_script": apply_script,
            },
            "jobs": [
                {
                    "slot": "canvas_quad",
                    "tool": image_flow["provider"],
                    "mcp_args": api_input,
                }
            ],
            "validation": {
                "prompt_chars": len(prompt),
                "max_prompt_chars": MAX_MCP_PROMPT_CHARS,
                "required_reference_host": SITE_HOST_PLACEHOLDER if has_cover else "",
                "resolution": MCP_RESOLUTION,
            },
        }
        batch_path = article_dir / "cover" / Path(str(spec["batch_file"])).name
        save_json(batch_path, batch)
        print(f"OK batch={batch_path} canvas={spec['index']} jobs=1")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
