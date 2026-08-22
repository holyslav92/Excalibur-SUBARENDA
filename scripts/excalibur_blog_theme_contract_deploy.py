#!/usr/bin/env python3
"""Idempotently teach the WP theme to respect future Excalibur post meta."""
from __future__ import annotations

import argparse
import json
import os
import posixpath
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable


SCHEMA_MARKER = "function excalibur_blog_output_schema_jsonld()"
SCHEMA_HOOK = r"""

// Excalibur future posts own their schema and topic FAQ.
function excalibur_blog_output_schema_jsonld() {
	if ( ! is_single() || '1' !== get_post_meta( get_the_ID(), '_excalibur_blog_skip_engagement_quiz', true ) ) {
		return;
	}
	$schema = get_post_meta( get_the_ID(), '_excalibur_blog_schema_jsonld', true );
	if ( is_string( $schema ) && '' !== trim( $schema ) ) {
		echo '<script type="application/ld+json">' . $schema . '</script>' . PHP_EOL; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
	}
}
add_action( 'wp_head', 'excalibur_blog_output_schema_jsonld', 20 );
"""


def _append_schema_hook(text: str, *, anchor: str) -> str:
    if SCHEMA_MARKER in text:
        return text
    if anchor not in text:
        raise ValueError(f"functions.php anchor not found: {anchor!r}")
    return text.replace(anchor, anchor + SCHEMA_HOOK, 1)


def patch_functions_kov4eg(text: str) -> str:
    old = "if ( is_single() && 'post' === get_post_type() ) {"
    new = (
        "if ( is_single() && 'post' === get_post_type() "
        "&& ! ( '1' === get_post_meta( get_the_ID(), "
        "'_excalibur_blog_skip_theme_faq', true ) "
        "&& '1' === get_post_meta( get_the_ID(), "
        "'_excalibur_blog_skip_engagement_quiz', true ) ) ) {"
    )
    if new not in text:
        function_start = text.find("function custom_theme_add_faq_to_single")
        filter_anchor = text.find(
            "add_filter( 'the_content', 'custom_theme_add_faq_to_single', 99 );"
        )
        if function_start < 0 or filter_anchor < function_start:
            raise ValueError("functions.php FAQ function bounds not found")
        faq_function = text[function_start:filter_anchor]
        if old not in faq_function:
            raise ValueError("functions.php FAQ anchor not found")
        patched_function = faq_function.replace(old, new, 1)
        text = text[:function_start] + patched_function + text[filter_anchor:]

    return _append_schema_hook(
        text,
        anchor="add_filter( 'the_content', 'custom_theme_add_faq_to_single', 99 );",
    )


def patch_functions_dobry_dom(text: str) -> str:
    return _append_schema_hook(text, anchor="include_once 'inc/BEM_Walker_Nav_Menu.php';")


def patch_single_kov4eg(text: str) -> str:
    marker = """\t\tthe_post();

\t\t$excalibur_skip_side_stickers = '1' === get_post_meta( get_the_ID(), '_excalibur_blog_skip_side_stickers', true );
\t\t$excalibur_skip_quiz = '1' === get_post_meta( get_the_ID(), '_excalibur_blog_skip_engagement_quiz', true );
"""
    if "$excalibur_skip_side_stickers" not in text:
        anchor = "\t\tthe_post();\n"
        if anchor not in text:
            raise ValueError("single.php the_post anchor not found")
        text = text.replace(anchor, marker, 1)

    side_open = '\t\t<div class="article-side-stickers"'
    side_guard = "\t\t<?php if ( ! $excalibur_skip_side_stickers ) : ?>\n" + side_open
    if side_guard not in text:
        if side_open not in text:
            raise ValueError("single.php side stickers anchor not found")
        text = text.replace(side_open, side_guard, 1)
        side_end = """\t\t</div>

\t\t<article id="post-<?php the_ID(); ?>"""
        guarded_end = """\t\t</div>
\t\t<?php endif; ?>

\t\t<article id="post-<?php the_ID(); ?>"""
        if side_end not in text:
            raise ValueError("single.php side stickers terminator not found")
        text = text.replace(side_end, guarded_end, 1)

    signal_open = '\t\t\t<section class="article-signal-cards"'
    signal_guard = "\t\t\t<?php if ( ! $excalibur_skip_quiz ) : ?>\n" + signal_open
    if signal_guard not in text:
        if signal_open not in text:
            raise ValueError("single.php signal cards anchor not found")
        text = text.replace(signal_open, signal_guard, 1)
        quiz_end = """\t\t\t</section>

\t\t\t<?php if ( has_post_thumbnail() ) : ?>"""
        guarded_quiz_end = """\t\t\t</section>
\t\t\t<?php endif; ?>

\t\t\t<?php if ( has_post_thumbnail() ) : ?>"""
        if quiz_end not in text:
            raise ValueError("single.php quiz terminator not found")
        text = text.replace(quiz_end, guarded_quiz_end, 1)
    return text


def patch_single_dobry_dom(text: str) -> str:
    replacements = (
        (
            '<div class="articles-typical__image">',
            '<div class="articles-typical__image post-thumbnail">',
        ),
        (
            '<div class="articles-typical__content">',
            '<div id="article-content" class="articles-typical__content">',
        ),
    )
    for old, new in replacements:
        if new in text:
            continue
        if old not in text:
            raise ValueError(f"single.php anchor not found: {old!r}")
        text = text.replace(old, new, 1)
    return text


THEME_PATCHERS: dict[str, tuple[Callable[[str], str], Callable[[str], str]]] = {
    "theme": (patch_functions_dobry_dom, patch_single_dobry_dom),
    "kov4eg-mcp-theme": (patch_functions_kov4eg, patch_single_kov4eg),
}


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def theme_slug_candidates(root: Path | None = None) -> list[str]:
    root = root or project_root()
    configured: list[str] = []
    tenant_path = root / "shared/tenant-config.json"
    if tenant_path.is_file():
        try:
            tenant = json.loads(tenant_path.read_text(encoding="utf-8"))
            slug = str((tenant.get("publish_options") or {}).get("wp_theme_slug") or "").strip()
            if slug:
                configured.append(slug)
        except json.JSONDecodeError:
            pass
    defaults = ["theme", "kov4eg-mcp-theme"]
    return list(dict.fromkeys(configured + defaults))


def _settings() -> tuple[str, str, str, int, list[str]]:
    values = dict(os.environ)
    local = project_root() / "memory/site.env.local"
    if local.is_file():
        for raw in local.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values.setdefault(key.strip(), value.strip().strip("\"'"))
    host = values.get("FTP_HOST") or values.get("SSH_HOST") or ""
    user = values.get("FTP_USER") or values.get("SSH_USER") or ""
    password = (
        values.get("FTP_PASS")
        or values.get("FTP_PASSWORD")
        or values.get("SSH_PASS")
        or values.get("SSH_PASSWORD")
        or ""
    )
    if not all((host, user, password)):
        raise RuntimeError("SFTP credentials missing")
    port = int(values.get("SSH_PORT") or 22)
    configured_root = (values.get("SSH_ROOT") or values.get("FTP_ROOT") or ".").strip()
    if configured_root in {"", "/"}:
        configured_root = "."
    roots = list(dict.fromkeys((configured_root, ".")))
    return host, user, password, port, roots


def resolve_theme_base(sftp, roots: list[str], theme_slugs: list[str]) -> tuple[str, str]:
    for root in roots:
        for slug in theme_slugs:
            candidate = posixpath.normpath(posixpath.join(root, "wp-content/themes", slug))
            try:
                sftp.stat(candidate)
            except OSError:
                continue
            if slug not in THEME_PATCHERS:
                raise RuntimeError(f"theme {slug!r} found but no patcher registered")
            return candidate, slug
    raise RuntimeError(
        "WordPress theme path not found; tried: "
        + ", ".join(theme_slugs)
    )


def deploy() -> str:
    import paramiko

    host, user, password, port, roots = _settings()
    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    theme_slug = ""
    try:
        base, theme_slug = resolve_theme_base(sftp, roots, theme_slug_candidates())
        patch_functions, patch_single = THEME_PATCHERS[theme_slug]
        print(f"OK theme={theme_slug} path={base}")
        for name, patcher in (
            ("functions.php", patch_functions),
            ("single.php", patch_single),
        ):
            remote = posixpath.join(base, name)
            with sftp.open(remote, "r") as handle:
                original = handle.read().decode("utf-8")
            patched = patcher(original)
            if patched == original:
                print(f"OK unchanged={name}")
                continue
            backup = f"{remote}.bak-excalibur-{stamp}"
            with sftp.open(backup, "w") as handle:
                handle.write(original.encode("utf-8"))
            with sftp.open(remote, "w") as handle:
                handle.write(patched.encode("utf-8"))
            print(f"OK patched={name} backup={posixpath.basename(backup)}")
    finally:
        sftp.close()
        transport.close()
    return theme_slug


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--deploy",
        action="store_true",
        help="Patch remote theme over SFTP; otherwise only validates local fixture args",
    )
    args = parser.parse_args()
    if not args.deploy:
        parser.error("--deploy required")
    deploy()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
