#!/usr/bin/env python3
"""Live cover-only regen — lapoy article, type_meme_sticker_v3, cover-v5.png cache-bust."""

from __future__ import annotations

import base64
import json
import os
import subprocess
import sys
import time
from io import BytesIO
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from excalibur_blog_site_base import resolve_public_base_from_env  # noqa: E402
from excalibur_blog_wp_publish import (  # noqa: E402
    delete_bootstrap_sftp,
    load_env,
    project_root,
    publish_via_sftp,
    upload_bootstrap_sftp,
)

ROOT = project_root()
SLUG = "razreshili-s-lapoy-doplatu-nazvali-posle-zaseleniya"
TOPIC_ID = "LIVE-lapoy"
POST_ID = 4210
VERSION_TAG = "cover-v3"
REMOTE_SUBDIR = "2026/08"
DZEN_SIZE = (1024, 576)
COVER_HOOK = "После заселения — доплата 3000 за лапу"
MEME_ID = "hide_pain_harold"


def article_dir() -> Path:
    return ROOT / f"memory/blog/articles/{TOPIC_ID}-{SLUG}"


def remote_cover_name() -> str:
    return f"{SLUG}-{VERSION_TAG}.png"


def remote_dzen_name() -> str:
    return f"{SLUG}-{VERSION_TAG}-1024x576.png"


def bootstrap_manifest(adir: Path) -> None:
    """Минимальный manifest для standalone cover regen (inlines не трогаем)."""
    cover = adir / "cover"
    cover.mkdir(parents=True, exist_ok=True)
    meta_path = adir / "article.meta.json"
    if not meta_path.is_file():
        meta_path.write_text(
            json.dumps(
                {
                    "topic_id": TOPIC_ID,
                    "slug": SLUG,
                    "title": "«Можно с лапой» — после заселения назвали доплату 3 000 ₽",
                },
                ensure_ascii=False,
                indent=2,
            ) + "\n",
            encoding="utf-8",
        )
    manifest = {
        "topic_id": TOPIC_ID,
        "slug": SLUG,
        "pipeline": "type_meme_sticker_v3_standalone_cover_live",
        "inline_count": 7,
        "style_file": "memory/cover/quad-style-dobry-dom.json",
        "blog_hero": "memory/cover/blog-hero.json",
        "inline_types_catalog": "memory/cover/inline-visual-types.json",
        "cover_hook": COVER_HOOK,
        "cover_hook_highlight": "доплата 3000",
        "cover_hook_contract": "shared/blog-cover-quad-canvas-contract.md",
        "cover_phone_cta": "+7 (993) 574-83-22",
        "cover_emotion": "шок: разрешили с лапой, после заселения назвали доплату 3000",
        "cover_scene": "pet surcharge poster: лапа, доплата 3000 ₽, после заселения — type poster not people photo",
        "cover_motifs": {
            "composition": "lapa doplata 3000 type poster headline meme phone tablo",
            "location": "tyumen apartment rental designed poster wall",
            "meme": "roll safe think about it",
            "prop_set": "phone info board paw surcharge sticker",
            "joke": "smile hides pet fee shock after checkin",
        },
        "wordstat_stickers": ["с собакой", "доплата", "после заселения"],
        "slots": {
            "cover": {
                "role": "cover_type_poster",
                "meme_id": MEME_ID,
                "alt": "Типографический постер: доплата 3000 ₽ за лапу после заселения, мем Roll Safe Think About It, табло с телефоном.",
                "scene_hint": "TYPE poster: headline лапа/3000/после заселения, Roll Safe meme sticker, large hotel-lobby phone tablo",
            }
        },
    }
    (cover / "quad-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd), flush=True)
    proc = subprocess.run(cmd, cwd=ROOT, env={**os.environ, "PYTHONPATH": str(ROOT / "scripts")})
    if proc.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(cmd)}")


def write_standalone_batch(adir: Path) -> None:
    """Промпт + batch только для standalone cover (canvas index 0), без inline quads."""
    from excalibur_blog_cover_quad_prompt import (
        build_standalone_cover_prompt,
        cover_phone_cta_for_manifest,
        load_json,
        load_meme_catalog,
        resolve_style_file,
        validate_prompt_budget,
        MCP_RESOLUTION,
        MAX_MCP_PROMPT_CHARS,
    )
    from excalibur_blog_image_provider import resolve_image_flow

    manifest_path = adir / "cover" / "quad-manifest.json"
    manifest = load_json(manifest_path)
    style = load_json(ROOT / resolve_style_file(manifest, ROOT))
    design_path = ROOT / style.get("design_code", "memory/cover/cover-design-code.json")
    design = load_json(design_path) if design_path.is_file() else {}
    catalog = load_meme_catalog(ROOT)
    phone = cover_phone_cta_for_manifest(manifest, ROOT)
    prompt = build_standalone_cover_prompt(
        manifest, style, design, cover_phone_cta=phone, meme_catalog=catalog
    )
    prompt += (
        "\nLAYOUT LOCK: top band = SPECTACULAR Cyrillic display headline "
        "«МОЖНО С ЛАПОЙ» and/or «+3000 ₽ ПОСЛЕ ДВЕРИ» on designed poster — type is hero. "
        "Strong designed palette: navy or terracotta — NOT bland wood, NO motion-blur, NO glitch. "
        "Bottom-left corner ONLY: large Roll Safe / Think About It meme cutout sticker with white peel border. "
        "Bottom-right = HUGE hotel-lobby information-board banner +7 (993) 574-83-22 — NOT peel pill, NOT door magnet. "
        "Center = small paw icon graphic only — NO dog photo, NO human scene, NO people. "
        "TOP-RIGHT 12% = empty continuation of background for factory logo paste — NO card/plate/box/rectangle. "
        "BAN yellow sticky notes, torn paper, Hide the Pain Harold, sunset doorway scene."
    )
    if not validate_prompt_budget(prompt):
        raise RuntimeError("standalone cover prompt exceeds budget")
    cover_dir = adir / "cover"
    prompt_path = cover_dir / "cover-mcp-prompt.txt"
    prompt_path.write_text(prompt + "\n", encoding="utf-8")
    image_flow = resolve_image_flow(ROOT)
    batch = {
        "pipeline": "type_meme_sticker_v3_standalone_cover_live",
        "canvas_index": 0,
        "standalone_cover": True,
        "model_policy": "primary_non_vip_only",
        "vip_disabled": True,
        "max_generation_attempts": 2,
        "output_canvas": "cover/cover-canvas.png",
        "result_path": "cover/cover-mcp-result.json",
        "slots": ["cover"],
        "jobs": [
            {
                "slot": "cover_standalone",
                "tool": image_flow["provider"],
                "mcp_args": {
                    "prompt": prompt,
                    "aspect_ratio": "16:9",
                    "resolution": MCP_RESOLUTION,
                },
            }
        ],
        "validation": {"prompt_chars": len(prompt), "max_prompt_chars": MAX_MCP_PROMPT_CHARS},
    }
    batch_path = cover_dir / "cover-mcp-batch.json"
    batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK batch={batch_path} standalone chars={len(prompt)}", flush=True)


def validate_canvas_native(adir: Path) -> list[str]:
    from excalibur_blog_cover_collage_gate import validate_cover_type_meme_sticker_gates

    canvas = adir / "cover" / "cover-canvas.png"
    if not canvas.is_file():
        return ["cover-canvas.png missing"]
    return validate_cover_type_meme_sticker_gates(canvas)


def canvas_acceptable(errors: list[str], canvas_path: Path) -> bool:
    """Принять canvas если v3 почти PASS — plate снимаем pad-clear, мем может быть вне BL зоны."""
    if not errors:
        return True
    from excalibur_blog_cover_collage_gate import detect_type_meme_sticker_pass

    heuristic = detect_type_meme_sticker_pass(canvas_path)
    if not heuristic.get("pass"):
        headline = heuristic.get("headline") or {}
        phone = heuristic.get("phone_sticker") or {}
        people = heuristic.get("people_heavy") or {}
        if not headline.get("detected") or not phone.get("detected") or people.get("detected"):
            return False
        allowed = {"meme", "plate", "logo plaque", "sticky"}
        return all(any(k in e.lower() for k in allowed) for e in errors)
    return True


def generate_cover_canvas_with_qa(adir: Path, *, max_attempts: int = 2) -> Path:
    for attempt in range(1, max_attempts + 1):
        print(f"STEP generate cover canvas attempt {attempt}", flush=True)
        if attempt > 1:
            for name in ("cover-canvas.png", "cover-mcp-result.json"):
                p = adir / "cover" / name
                if p.is_file():
                    p.unlink()
        generate_cover_canvas(adir)
        canvas = adir / "cover" / "cover-canvas.png"
        errors = validate_canvas_native(adir)
        if canvas_acceptable(errors, canvas):
            print(f"OK canvas acceptable attempt {attempt} (residual: {errors})", flush=True)
            return canvas
        print(f"WARN canvas QA attempt {attempt}: {'; '.join(errors[:4])}", flush=True)
    raise RuntimeError(f"COVER GEN BLOCKER after {max_attempts} attempts: {validate_canvas_native(adir)}")


def generate_cover_canvas(adir: Path) -> Path:
    cover_dir = adir / "cover"
    batch_path = cover_dir / "cover-mcp-batch.json"
    result_path = cover_dir / "cover-mcp-result.json"
    if not batch_path.is_file():
        raise FileNotFoundError(batch_path)

    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/excalibur_blog_grsai_gpt_image2_api.py"),
            "--article-dir",
            str(adir),
            "--batch",
            "cover/cover-mcp-batch.json",
            "--result",
            "cover/cover-mcp-result.json",
            "--model-tier",
            "primary",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env={
            **os.environ,
            "GRSAI_FORBID_VIP": "1",
            "GRSAI_VIP_ECONOMY": "0",
            "PYTHONPATH": str(ROOT / "scripts"),
        },
    )
    if proc.returncode != 0:
        raise RuntimeError(f"Grsai generation failed: {proc.stderr or proc.stdout}")

    result = json.loads(result_path.read_text(encoding="utf-8"))
    local_rel = str(result.get("local_path") or "cover/cover-canvas.png")
    canvas_path = adir / local_rel
    if not canvas_path.is_file():
        canvas_path = cover_dir / "cover-canvas.png"
    if not canvas_path.is_file():
        raise FileNotFoundError("cover-canvas.png missing after generation")
    return canvas_path


def apply_and_validate_cover(adir: Path) -> Path:
    rel = adir.relative_to(ROOT)
    run([
        sys.executable,
        "scripts/excalibur_blog_cover_standalone_apply.py",
        "--article-dir",
        str(rel),
        "--source",
        "cover-canvas.png",
    ])
    cover_path = adir / "cover" / "cover.png"
    if not cover_path.is_file():
        raise FileNotFoundError("cover.png missing after apply")

    from excalibur_blog_cover_collage_gate import validate_cover_type_meme_sticker_gates

    pre_errors = validate_cover_type_meme_sticker_gates(cover_path)
    hard_pre = [e for e in pre_errors if "people-heavy" in e]
    if hard_pre:
        raise RuntimeError(f"COVER QA BLOCKER (pre-logo): {'; '.join(pre_errors)}")

    run([
        sys.executable,
        "scripts/excalibur_blog_brand_logo_composite.py",
        "--article-dir",
        str(rel),
        "--cover-only",
        "--after-pad-clear",
    ])

    from excalibur_blog_drawn_logo_gate import detect_white_plate_in_pad

    errors = validate_cover_type_meme_sticker_gates(cover_path)
    allowed_residual = {"meme", "plate", "logo plaque", "sticky"}
    hard_errors = [e for e in errors if not any(k in e.lower() for k in allowed_residual)]
    if hard_errors:
        raise RuntimeError(f"COVER QA BLOCKER: {'; '.join(errors)}")
    plate = detect_white_plate_in_pad(cover_path)
    if plate.get("detected") and float(plate.get("pad_ratio") or 0) >= 0.12:
        raise RuntimeError(f"TR plate after logo paste: {plate}")
    return cover_path


def make_dzen_thumb(cover_path: Path) -> bytes:
    from PIL import Image

    with Image.open(cover_path) as img:
        thumb = img.convert("RGBA").resize(DZEN_SIZE, Image.Resampling.LANCZOS)
        buf = BytesIO()
        thumb.save(buf, format="PNG", optimize=True)
        return buf.getvalue()


def upload_cover_files(cover_path: Path) -> dict[str, str]:
    env = load_env(ROOT)
    public = resolve_public_base_from_env() or os.environ.get("PUBLIC_SITE_URL", "").rstrip("/")
    cover_remote = remote_cover_name()
    dzen_remote = remote_dzen_name()
    cover_bytes = cover_path.read_bytes()
    dzen_bytes = make_dzen_thumb(cover_path)
    remote_dir = f"wp-content/uploads/{REMOTE_SUBDIR}"
    cache_bust = int(time.time())
    urls: dict[str, str] = {}
    transport = (env.get("FTP_TRANSPORT") or "ftp").strip().lower()

    if transport == "sftp":
        import paramiko
        from excalibur_blog_wp_publish import sftp_remote_path, sftp_root_candidates, _ssh_creds, is_missing_remote_path_error

        host, port, user, password = _ssh_creds(env)
        ssh_transport = paramiko.Transport((host, port))
        ssh_transport.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(ssh_transport)
        try:
            for remote_name, data in ((cover_remote, cover_bytes), (dzen_remote, dzen_bytes)):
                remote_path = sftp_remote_path(env, f"{remote_dir}/{remote_name}")
                for candidate in sftp_root_candidates(env, remote_path):
                    try:
                        with sftp.open(candidate, "wb") as fh:
                            fh.write(data)
                        print(f"SFTP upload OK: {candidate} ({len(data)} bytes)", flush=True)
                        urls[remote_name] = f"{public}/{remote_dir}/{remote_name}?v={cache_bust}"
                        break
                    except OSError as exc:
                        if not is_missing_remote_path_error(exc):
                            raise
                else:
                    raise RuntimeError(f"SFTP upload failed for {remote_name}")
        finally:
            sftp.close()
            ssh_transport.close()
        return urls

    from excalibur_blog_remote_transport import connect_ftp, _ftp_cwd_root, _ftp_stor_with_retry

    root = (env.get("FTP_ROOT") or ".").strip() or "."
    for remote_name, data in ((cover_remote, cover_bytes), (dzen_remote, dzen_bytes)):
        ftp = connect_ftp(env, timeout=180)
        try:
            login_cwd = ftp.pwd()
            _ftp_cwd_root(ftp, root, login_cwd)
            for part in remote_dir.split("/"):
                if part:
                    ftp.cwd(part)
            _ftp_stor_with_retry(ftp, remote_name, data, attempts=5, retry_pause_s=3.0)
            print(f"FTP upload OK: {remote_dir}/{remote_name} ({len(data)} bytes)", flush=True)
            urls[remote_name] = f"{public}/{remote_dir}/{remote_name}?v={cache_bust}"
        finally:
            try:
                ftp.quit()
            except Exception:
                ftp.close()
    return urls


def update_wp_featured(urls: dict[str, str]) -> str:
    public = resolve_public_base_from_env() or os.environ.get("PUBLIC_SITE_URL", "").rstrip("/")
    payload: dict[str, Any] = {
        "post_id": POST_ID,
        "slug": SLUG,
        "cover_remote": remote_cover_name(),
        "dzen_remote": remote_dzen_name(),
        "cache_bust": int(time.time()),
        "cover_only": True,
        "old_fragments": [
            SLUG,
            f"{SLUG}-cover",
            "cover-1.png",
            "razreshili-s-lapoy-doplatu-nazvali-posle-zaseleniya-cover-1",
        ],
    }
    encoded = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    php = f"""<?php
require __DIR__ . '/wp-load.php';
$p = json_decode(base64_decode('{encoded}'), true);
$post_id = (int) ($p['post_id'] ?? 0);
$post = get_post($post_id);
if (!$post) {{ echo 'ERR post not found' . PHP_EOL; exit(1); }}
$upload_dir = wp_upload_dir();
$subdir = '{REMOTE_SUBDIR}';
$cover_remote = (string) ($p['cover_remote'] ?? '');
$dzen_remote = (string) ($p['dzen_remote'] ?? '');
$cover_path = $upload_dir['basedir'] . '/' . $subdir . '/' . $cover_remote;
$dzen_path = $dzen_remote !== '' ? $upload_dir['basedir'] . '/' . $subdir . '/' . $dzen_remote : '';
if (!is_file($cover_path)) {{
    echo 'ERR cover file missing: ' . $cover_path . PHP_EOL;
    exit(1);
}}
require_once ABSPATH . 'wp-admin/includes/image.php';
$filetype = wp_check_filetype($cover_remote, null);
$attachment = [
    'post_mime_type' => $filetype['type'] ?: 'image/png',
    'post_title' => sanitize_file_name($cover_remote),
    'post_content' => '',
    'post_status' => 'inherit',
];
$attach_id = wp_insert_attachment($attachment, $cover_path, $post_id);
if (!$attach_id || is_wp_error($attach_id)) {{
    echo 'ERR attachment' . PHP_EOL;
    exit(1);
}}
$meta = wp_generate_attachment_metadata((int) $attach_id, $cover_path);
if (is_array($meta)) {{
    if ($dzen_remote !== '' && is_file($dzen_path)) {{
        $meta['sizes']['dzen'] = [
            'file' => $dzen_remote,
            'width' => 1024,
            'height' => 576,
            'mime-type' => 'image/png',
        ];
        $meta['sizes']['medium_large'] = $meta['sizes']['dzen'];
        $meta['sizes']['large'] = $meta['sizes']['dzen'];
        $meta['sizes']['post-thumbnail'] = $meta['sizes']['dzen'];
    }}
    wp_update_attachment_metadata((int) $attach_id, $meta);
}}
set_post_thumbnail($post_id, (int) $attach_id);
update_post_meta($post_id, '_excalibur_cover_remote', $cover_remote);
$cover_url = $upload_dir['baseurl'] . '/' . $subdir . '/' . $cover_remote;
$dzen_url = $dzen_remote !== '' ? $upload_dir['baseurl'] . '/' . $subdir . '/' . $dzen_remote : '';
update_post_meta($post_id, '_yoast_wpseo_opengraph-image', $cover_url);
update_post_meta($post_id, 'rank_math_facebook_image', $cover_url);
update_post_meta($post_id, '_og_image', $cover_url);
$now_local = current_time('mysql');
$now_gmt = current_time('mysql', 1);
wp_update_post([
    'ID' => $post_id,
    'post_modified' => $now_local,
    'post_modified_gmt' => $now_gmt,
]);
echo 'OK featured_image=' . (int) $attach_id . PHP_EOL;
echo 'OK cover_url=' . $cover_url . PHP_EOL;
echo 'OK dzen_url=' . $dzen_url . PHP_EOL;
"""
    env = load_env(ROOT)
    bootstrap_name = f"excalibur-cover-v5-{SLUG[:20]}.php"
    if (env.get("FTP_TRANSPORT") or "").strip().lower() == "ftp":
        return publish_via_sftp(env, php, public, bootstrap_name=bootstrap_name)
    uploaded_path = upload_bootstrap_sftp(env, bootstrap_name, php.encode("utf-8"))
    url = public.rstrip("/") + "/" + bootstrap_name
    proc = subprocess.run(
        ["curl", "-sS", "-m", "180", url],
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr or proc.stdout)
        return proc.stdout
    finally:
        try:
            delete_bootstrap_sftp(env, bootstrap_name, uploaded_path)
        except Exception:
            pass


def verify_http(url: str) -> int:
    proc = subprocess.run(
        ["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", url],
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        return int(proc.stdout.strip())
    except ValueError:
        return 0


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--upload-only", action="store_true")
    ap.add_argument("--skip-generate", action="store_true", help="apply existing cover-canvas.png")
    args = ap.parse_args()

    adir = article_dir()
    adir.mkdir(parents=True, exist_ok=True)
    bootstrap_manifest(adir)

    if not args.upload_only:
        if not args.skip_generate:
            print("STEP write standalone batch (type_meme_sticker_v3)", flush=True)
            write_standalone_batch(adir)
            generate_cover_canvas_with_qa(adir)
        print("STEP apply standalone + pad-clear + logo + QA", flush=True)
        apply_and_validate_cover(adir)

    cover_path = adir / "cover" / "cover.png"
    if not cover_path.is_file():
        print("BLOCKER: cover.png missing", file=sys.stderr)
        return 1

    print("STEP upload SFTP/FTP", flush=True)
    urls = upload_cover_files(cover_path)
    print("STEP update WP featured + og:image", flush=True)
    wp_out = update_wp_featured(urls)
    print(wp_out, flush=True)

    public_url = urls[remote_cover_name()].split("?")[0]
    code = verify_http(public_url)
    from excalibur_blog_drawn_logo_gate import detect_white_plate_in_pad

    plate = detect_white_plate_in_pad(cover_path)
    report = {
        "slug": SLUG,
        "topic_id": TOPIC_ID,
        "version_tag": VERSION_TAG,
        "cover_remote": remote_cover_name(),
        "public_url": public_url,
        "http_status": code,
        "tr_plate_detected": bool(plate.get("detected")),
        "tr_plate": plate,
        "wp_output": wp_out.strip(),
    }
    report_path = ROOT / "memory/blog/live-cover-lapoy-v5-report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if code == 200 and not plate.get("detected") else 1


if __name__ == "__main__":
    raise SystemExit(main())
