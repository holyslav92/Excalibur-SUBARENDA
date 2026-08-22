#!/usr/bin/env python3
"""Idempotently teach the WP theme to respect future Excalibur post meta."""
from __future__ import annotations

import argparse
import io
import posixpath
from datetime import datetime, timezone
from ftplib import error_perm
from typing import Callable

DEFAULT_THEME_SLUG = "kov4eg-mcp-theme"


def patch_functions(text: str) -> str:
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

    schema_marker = "function excalibur_blog_output_schema_jsonld()"
    if schema_marker not in text:
        anchor = "add_filter( 'the_content', 'custom_theme_add_faq_to_single', 99 );"
        if anchor not in text:
            raise ValueError("functions.php FAQ filter anchor not found")
        schema_hook = r"""

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
        text = text.replace(anchor, anchor + schema_hook, 1)
    return text


def patch_single(text: str) -> str:
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


def _theme_slug(env: dict[str, str]) -> str:
    return (env.get("WP_THEME_SLUG") or DEFAULT_THEME_SLUG).strip() or DEFAULT_THEME_SLUG


def _theme_rel_paths(env: dict[str, str], wp_root: str) -> list[str]:
    slug = _theme_slug(env)
    root = wp_root.strip("/") if wp_root not in {".", "./", ""} else ""
    rel = posixpath.join("wp-content", "themes", slug)
    if root:
        return [posixpath.normpath(posixpath.join(root, rel)), posixpath.normpath(rel)]
    return [posixpath.normpath(rel), "."]


def _apply_patches(
    *,
    read_text: Callable[[str], str],
    write_text: Callable[[str, str], None],
    base_label: str,
) -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    for name, patcher in (
        ("functions.php", patch_functions),
        ("single.php", patch_single),
    ):
        original = read_text(name)
        patched = patcher(original)
        if patched == original:
            print(f"OK unchanged={name}")
            continue
        backup = f"{name}.bak-excalibur-{stamp}"
        write_text(backup, original)
        write_text(name, patched)
        print(f"OK patched={name} backup={backup} base={base_label}")


def deploy_via_sftp(env: dict[str, str]) -> None:
    import paramiko

    from excalibur_blog_remote_transport import remote_root_candidates

    host = env.get("SSH_HOST") or env.get("FTP_HOST") or ""
    port = int((env.get("SSH_PORT") or env.get("FTP_PORT") or "22").strip() or "22")
    user = env.get("SSH_USER") or env.get("FTP_USER") or ""
    password = (
        env.get("SSH_PASS")
        or env.get("FTP_PASS")
        or env.get("SSH_PASSWORD")
        or env.get("FTP_PASSWORD")
        or ""
    )
    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    base = ""
    try:
        for root in remote_root_candidates(env):
            for candidate in _theme_rel_paths(env, root):
                try:
                    sftp.stat(candidate)
                    base = candidate
                    break
                except OSError:
                    continue
            if base:
                break
        if not base:
            raise RuntimeError("WordPress theme path not found in configured root or login cwd")

        def read_text(name: str) -> str:
            remote = posixpath.join(base, name)
            with sftp.open(remote, "r") as handle:
                return handle.read().decode("utf-8")

        def write_text(name: str, text: str) -> None:
            remote = posixpath.join(base, name)
            with sftp.open(remote, "w") as handle:
                handle.write(text.encode("utf-8"))

        _apply_patches(read_text=read_text, write_text=write_text, base_label=base)
    finally:
        sftp.close()
        transport.close()


def deploy_via_ftp(env: dict[str, str]) -> None:
    from excalibur_blog_remote_transport import (
        _ftp_cwd_root,
        connect_ftp,
        find_wp_root,
    )

    selected_root, _probe = find_wp_root(env)
    if not selected_root:
        raise RuntimeError("WordPress root not found via FTP (wp-load.php missing)")
    env = dict(env)
    env["FTP_ROOT"] = selected_root
    ftp = connect_ftp(env)
    theme_base = ""
    try:
        login_cwd = ftp.pwd()
        theme_rel = posixpath.join("wp-content", "themes", _theme_slug(env))
        for candidate in _theme_rel_paths(env, selected_root):
            try:
                ftp.cwd(login_cwd)
                _ftp_cwd_root(ftp, selected_root, login_cwd)
                for part in theme_rel.split("/"):
                    if part and part != ".":
                        ftp.cwd(part)
                ftp.size("functions.php")
                theme_base = candidate
                break
            except (error_perm, OSError):
                continue
        if not theme_base:
            raise RuntimeError("WordPress theme path not found via FTP")

        def read_text(name: str) -> str:
            bio = io.BytesIO()
            ftp.retrbinary(f"RETR {name}", bio.write)
            return bio.getvalue().decode("utf-8")

        def write_text(name: str, text: str) -> None:
            bio = io.BytesIO(text.encode("utf-8"))
            ftp.storbinary(f"STOR {name}", bio)

        _apply_patches(read_text=read_text, write_text=write_text, base_label=theme_base)
    finally:
        try:
            ftp.quit()
        except Exception:
            ftp.close()


def deploy() -> None:
    from excalibur_blog_remote_transport import resolve_publish_transport
    from excalibur_blog_wp_publish import load_env, project_root

    env = load_env(project_root())
    if resolve_publish_transport(env) == "ftp":
        deploy_via_ftp(env)
    else:
        deploy_via_sftp(env)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--deploy",
        action="store_true",
        help="Patch remote theme over FTP or SFTP; otherwise only validates local fixture args",
    )
    args = parser.parse_args()
    if not args.deploy:
        parser.error("--deploy required")
    deploy()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
