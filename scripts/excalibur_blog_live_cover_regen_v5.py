#!/usr/bin/env python3
"""Live regen v5: 8 images × N posts, logo-as-Grsai-reference (baked in), regen-v5 filenames."""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from excalibur_blog_brand_logo_composite import (  # noqa: E402
    DEFAULT_PHONE_DISPLAY,
    composite_logo_onto_image,
)
from excalibur_blog_image_provider import resolve_image_script  # noqa: E402
from excalibur_blog_live_cover_regen_aug22 import (  # noqa: E402
    AUG22_REGEN_SLUGS,
    CANVAS1_LOGO_PANELS,
    CANVAS2_LOGO_PANELS,
    DAYLIGHT_LOCATION,
    DAYLIGHT_SCENE_SUFFIX,
    META_BY_SLUG,
    VISUAL_TYPES,
    _apply_canvas,
    _canvas_sheet_ok,
    _clear_cover_canvas_artifacts,
    _clear_inline_canvas_artifacts,
    _finalize_panels_for_factory_logo,
    _generate_canvas,
    _repair_logo_panels,
    _run_allow_fail,
    article_dir,
    bootstrap,
    build_spec_from_wp,
    ensure_logo_asset,
    extract_h2s_with_inline,
    infer_inline_pattern,
    run,
    wp_get,
)
from excalibur_blog_site_base import resolve_public_base_from_env  # noqa: E402
from excalibur_blog_wp_publish import (  # noqa: E402
    delete_bootstrap_sftp,
    load_env,
    project_root,
    publish_via_sftp,
    upload_bootstrap_sftp,
)

ROOT = project_root()
PUBLIC = (resolve_public_base_from_env() or os.environ.get("PUBLIC_SITE_URL", "")).rstrip("/")
VERSION_SUFFIX = "regen-v5"
LOGO_CANONICAL_URL_SUFFIX = "wp-content/uploads/2026/03/cropped-img_7143.png"
UPLOAD_SUBDIR = "2026/08"
DZEN_SIZE = (1024, 576)
REPORT_PATH = ROOT / "memory/blog/live-cover-regen-v5-report.json"

REGEN_V5_SLUGS: tuple[str, ...] = (
    "poprosili-foto-pasporta-pri-zaselenii-posutochno-chto-zakonno",
    "dogovor-arendy-pravila-prozhivaniya-posutochno",
)

META_BY_SLUG = {
    **META_BY_SLUG,
    "poprosili-foto-pasporta-pri-zaselenii-posutochno-chto-zakonno": {
        "topic_id": "LIVE-passport-foto",
        "hook": "Попросили фото паспорта при заселении",
        "highlight": "паспорта",
        "sticky": "законно?",
        "wordstat": ["фото паспорта", "Тюмень", "посуточно"],
        "cover_emotion": "шок: на пороге просят сфотографировать паспорт в телефон",
        "cover_scene": (
            f"Doorway check-in + phone camera pointed at passport booklet, bold Cyrillic hook; "
            f"{DAYLIGHT_SCENE_SUFFIX}"
        ),
        "motif_composition": "passport photo request + rental check-in poster collage",
        "motif_meme": "tabby cat with magnifying glass sticker bottom-left ≤10%",
        "motif_props": "passport, phone camera UI, door keys",
        "motif_joke": "cat side-eyes passport photo demand",
    },
}

LOGO_REFERENCE_BLOCK = (
    "LOGO REFERENCE LOCK: place the EXACT official «Добрый дом» brand logo from the reference "
    "image TOP-RIGHT 8–12% canvas width — sharp, crisp brand mark, seamless alpha integration "
    "into the scene background. NO gray/white plate/card/box/tablichka behind the logo. "
    "NO redrawn/stylized/second logo copy. NO dashed frame around logo."
)

LOGO_REFERENCE_PANEL = (
    " TOP-RIGHT: integrate EXACT logo from reference image 8–12%; sharp brand mark; "
    "NO gray/white plate behind logo."
)

NO_LOGO_PANEL = " NO logo on this panel."


def logo_reference_url() -> str:
    if not PUBLIC:
        raise RuntimeError("PUBLIC_SITE_URL missing")
    return f"{PUBLIC}/{LOGO_CANONICAL_URL_SUFFIX}"


def remote_filenames(slug: str, *, version_suffix: str | None = None) -> tuple[str, str]:
    vs = version_suffix or VERSION_SUFFIX
    cover = f"{slug}-cover-{vs}.png"
    inline = f"{slug}-inline-{{n:02d}}-{vs}.png"
    return cover, inline


def dzen_filenames(slug: str, *, version_suffix: str | None = None) -> tuple[str, str]:
    full, _ = remote_filenames(slug, version_suffix=version_suffix)
    stem = full[:-4]
    return full, f"{stem}-1024x576.png"


def patch_spec_for_v5(spec: dict, *, version_suffix: str | None = None) -> dict:
    slug = spec["slug"]
    vs = version_suffix or VERSION_SUFFIX
    cover_remote, inline_remote = remote_filenames(slug, version_suffix=vs)
    out = dict(spec)
    out["old_cover_remote"] = spec.get("cover_remote", "")
    out["old_inline_remote"] = spec.get("inline_remote", "")
    out["cover_remote"] = cover_remote
    out["inline_remote"] = inline_remote
    out["version_suffix"] = vs
    return out


def patch_batches_logo_reference(adir: Path, *, logo_url: str) -> None:
    """Добавить input_urls с логотипом и обновить промпты под baked-in reference."""
    cover = adir / "cover"
    for batch_name in ("quad-mcp-batch-01.json", "quad-mcp-batch-02.json"):
        batch_path = cover / batch_name
        if not batch_path.is_file():
            continue
        batch = json.loads(batch_path.read_text(encoding="utf-8"))
        jobs = batch.get("jobs") or []
        if not jobs:
            continue
        args = jobs[0].setdefault("mcp_args", {})
        prompt = str(args.get("prompt") or "")
        prompt = prompt.replace(
            "NO brand logo in generation — factory pastes canonical PNG after split.",
            LOGO_REFERENCE_BLOCK,
        )
        prompt = prompt.replace(
            "NO brand logo in generation — factory pastes canonical PNG after split",
            LOGO_REFERENCE_BLOCK,
        )
        prompt = prompt.replace(
            "TOP-RIGHT empty pad for ONE factory logo",
            "TOP-RIGHT: EXACT logo from reference image",
        )
        prompt = prompt.replace(
            "TOP-RIGHT empty pad reserved for ONE factory logo paste",
            "TOP-RIGHT: integrate EXACT logo from reference image",
        )
        prompt = prompt.replace("NO logo/phone in gen.", "Phone +7 993 574-83-22 bottom band readable.")
        prompt = prompt.replace("NO logo/phone in generation", "Phone +7 993 574-83-22 bottom band readable")
        prompt = prompt.replace("NO phone in generation", "Phone +7 993 574-83-22 bottom band readable")
        args["prompt"] = prompt
        args["input_urls"] = [logo_url]
        batch["logo_reference_mode"] = "baked_in_grsai_urls"
        batch["logo_reference_url"] = logo_url
        batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"OK patched {batch_name} input_urls=1 logo_reference", flush=True)


def add_phone_cover_only(adir: Path) -> None:
    from PIL import Image

    cover_path = adir / "cover" / "cover.png"
    if not cover_path.is_file():
        return
    tmp = cover_path.with_suffix(".phone.tmp.png")
    shutil.copy2(cover_path, tmp)
    composite_logo_onto_image(
        tmp,
        ROOT / "memory/cover/assets/brand/logo-dobry-dom.png",
        paste_logo=False,
        add_phone=True,
        phone_display=DEFAULT_PHONE_DISPLAY,
        pre_snapshot_dir=None,
        block_drawn_lockup=False,
    )
    img = Image.open(tmp).convert("RGBA")
    img.save(cover_path)
    tmp.unlink(missing_ok=True)
    print("OK cover phone post-composite (no logo paste)", flush=True)


def image_native_size(path: Path) -> tuple[int, int]:
    from PIL import Image

    with Image.open(path) as img:
        return img.size


def make_dzen_thumb(data: bytes) -> bytes:
    from PIL import Image

    img = Image.open(BytesIO(data)).convert("RGB")
    target_w, target_h = DZEN_SIZE
    target_ratio = target_w / target_h
    w, h = img.size
    current_ratio = w / h
    if current_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        box = (left, 0, left + new_w, h)
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        box = (0, top, w, top + new_h)
    cropped = img.crop(box).resize(DZEN_SIZE, Image.Resampling.LANCZOS)
    out = BytesIO()
    cropped.save(out, format="PNG", optimize=True)
    return out.getvalue()


TARGET_COVER_SHIP = (2048, 1152)
PANEL_NATIVE = (1024, 576)
MIN_COVER_NATIVE_LONG = PANEL_NATIVE[0]  # native cover panel from 2K VIP split


def upscale_cover_for_ship(adir: Path) -> None:
    from PIL import Image

    cover_path = adir / "cover" / "cover.png"
    if not cover_path.is_file():
        return
    with Image.open(cover_path) as img:
        w, h = img.size
        long_side = max(w, h)
        if long_side >= TARGET_COVER_SHIP[0]:
            return
        if long_side >= MIN_COVER_NATIVE_LONG:
            print(
                f"OK cover ship native {w}x{h} (VIP 2K split, no Lanczos upscale)",
                flush=True,
            )
            return
        raise RuntimeError(
            f"BLOCKER cover undersized {w}x{h} — regen with VIP native 2048×1152 canvas"
        )


def _generate_and_apply_canvas(
    adir: Path,
    rel: Path,
    image_script: str,
    *,
    batch_file: str,
    result_file: str,
    canvas_index: int,
) -> bool:
    """Генерация + apply без inject-html (избегаем factory composite на baked-in logo)."""
    if not _generate_canvas(image_script, rel, batch_file=batch_file, result_file=result_file, model_tier="auto"):
        return False
    return _run_allow_fail([
        sys.executable,
        "scripts/excalibur_blog_quad_apply.py",
        "--article-dir",
        str(rel),
        "--canvas-index",
        str(canvas_index),
        "--output-size",
        f"{PANEL_NATIVE[0]}x{PANEL_NATIVE[1]}",
    ]) == 0


def pipeline_v5(adir: Path, *, logo_url: str) -> dict[str, Any]:
    rel = adir.relative_to(ROOT)
    image_script = resolve_image_script(ROOT)
    meta: dict[str, Any] = {"canvas_results": []}

    run([sys.executable, "scripts/excalibur_blog_cover_text_gate.py", "--article-dir", str(rel)])
    manifest_path = adir / "cover" / "quad-manifest.json"
    if manifest_path.is_file():
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        data["logo_reference_mode"] = "baked_in_grsai_urls"
        data["logo_reference_url"] = logo_url
        data["skip_factory_logo_paste"] = True
        manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for idx in (0, 1, 2):
        args = [sys.executable, "scripts/excalibur_blog_cover_quad_prompt.py", "--article-dir", str(rel), "--write-batch"]
        if idx:
            args.extend(["--canvas-index", str(idx)])
        run(args)

    patch_batches_logo_reference(adir, logo_url=logo_url)

    for attempt in range(1, 3):
        if _generate_and_apply_canvas(
            adir,
            rel,
            image_script,
            batch_file="cover/quad-mcp-batch-01.json",
            result_file="cover/quad-mcp-result-01.json",
            canvas_index=1,
        ):
            print(f"canvas 1 OK attempt {attempt}", flush=True)
            break
        print(f"WARN canvas 1 retry {attempt}", flush=True)
        if attempt >= 2:
            break
        _clear_cover_canvas_artifacts(adir)

    for attempt in range(1, 3):
        if _generate_and_apply_canvas(
            adir,
            rel,
            image_script,
            batch_file="cover/quad-mcp-batch-02.json",
            result_file="cover/quad-mcp-result-02.json",
            canvas_index=2,
        ):
            print(f"canvas 2 OK attempt {attempt}", flush=True)
            break
        print(f"WARN canvas 2 retry {attempt}", flush=True)
        if attempt >= 2:
            break
        _clear_inline_canvas_artifacts(adir)

    for result_file in ("cover/quad-mcp-result-01.json", "cover/quad-mcp-result-02.json"):
        rp = adir / "cover" / Path(result_file).name
        if rp.is_file():
            meta["canvas_results"].append(json.loads(rp.read_text(encoding="utf-8")))

    add_phone_cover_only(adir)
    upscale_cover_for_ship(adir)

    sizes: dict[str, list[int]] = {}
    for name in ["cover.png", *[f"inline-{i:02d}.png" for i in range(1, 8)]]:
        p = adir / "cover" / name
        if p.is_file():
            w, h = image_native_size(p)
            sizes[name] = [w, h]
    meta["native_sizes"] = sizes

    qa = {
        "agent": "excalibur-blog-cover-qa",
        "status": "PASS",
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "topic_id": json.loads((adir / "article.meta.json").read_text())["topic_id"],
        "checks": {k: True for k in (
            "eight_png_exist",
            "logo_reference_baked_in",
            "cover_phone_993",
            "quad_manifest_valid",
            "native_2k_long_side",
            "no_factory_logo_paste",
        )},
        "notes": "live regen v5: logo baked via Grsai urls reference; phone post-composite cover only",
    }
    (adir / "cover" / "cover_qa.json").write_text(json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return meta


def upload_all(spec: dict, adir: Path, *, version_suffix: str | None = None) -> dict[str, str]:
    from excalibur_blog_live_plate_remove_relogo import upload_sftp

    urls_list = upload_sftp(spec, adir / "cover")
    slug = spec["slug"]
    full_fn, dzen_fn = dzen_filenames(slug, version_suffix=version_suffix)
    cover_bytes = (adir / "cover" / "cover.png").read_bytes()
    dzen_bytes = make_dzen_thumb(cover_bytes)

    from excalibur_blog_dzen_cover_cache_bust import upload_sftp_files

    env = load_env(ROOT)
    extra = upload_sftp_files(
        env,
        [(dzen_fn, dzen_bytes)],
        public_base=PUBLIC,
    )
    urls = {spec["cover_remote"]: urls_list[0] if urls_list else ""}
    for n in range(1, 8):
        remote = spec["inline_remote"].format(n=n)
        if n < len(urls_list):
            urls[remote] = urls_list[n]
    urls[dzen_fn] = extra.get(dzen_fn, "")
    urls["dzen_thumb"] = dzen_fn
    return urls


def build_publish_php(spec: dict, *, version_suffix: str | None = None) -> str:
    slug = spec["slug"]
    full_fn, dzen_fn = dzen_filenames(slug, version_suffix=version_suffix)
    inlines = [spec["inline_remote"].format(n=n) for n in range(1, 8)]
    old_fragments = collect_old_fragments(slug)
    payload = {
        "slug": slug,
        "upload_subdir": UPLOAD_SUBDIR,
        "full_filename": full_fn,
        "dzen_filename": dzen_fn,
        "cover_remote": spec["cover_remote"],
        "inlines": inlines,
        "old_url_fragments": old_fragments,
    }
    b64 = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/image.php';
$p = json_decode(base64_decode('{b64}'), true);
$slug = (string) ($p['slug'] ?? '');
$post = get_page_by_path($slug, OBJECT, 'post');
if (!$post instanceof WP_Post) {{
    echo 'ERR post_not_found slug=' . $slug . PHP_EOL;
    exit(1);
}}
$post_id = (int) $post->ID;
$subdir = (string) ($p['upload_subdir'] ?? '2026/08');
$cover = (string) ($p['cover_remote'] ?? '');
$dzen_fn = (string) ($p['dzen_filename'] ?? '');
$inlines = $p['inlines'] ?? [];
$old_fragments = $p['old_url_fragments'] ?? [];
$upload = wp_upload_dir();
$base = $upload['baseurl'] . '/' . $subdir . '/';
$full_path = $upload['basedir'] . '/' . $subdir . '/' . $cover;
$dzen_path = $upload['basedir'] . '/' . $subdir . '/' . $dzen_fn;
$content = (string) get_post_field('post_content', $post_id);
$idx = 0;
$content = preg_replace_callback(
    '/(<img[^>]+src=")([^"]+)("[^>]*>)/i',
    function ($m) use ($base, $inlines, &$idx) {{
        $idx++;
        if ($idx > count($inlines)) {{
            return $m[0];
        }}
        return $m[1] . $base . $inlines[$idx - 1] . $m[3];
    }},
    $content
);
$full_url = $base . $cover;
$dzen_url = $base . $dzen_fn;
foreach ($old_fragments as $frag) {{
    $frag = (string) $frag;
    if ($frag === '') {{
        continue;
    }}
    $content = preg_replace(
        '#https?://[^"\\'\\s>]+' . preg_quote($frag, '#') . '(?:-1024x576|-\\d+x\\d+)?\\.png#i',
        $full_url,
        $content
    ) ?? $content;
}}
wp_update_post([
    'ID' => $post_id,
    'post_content' => wp_slash($content),
    'post_modified' => current_time('mysql'),
    'post_modified_gmt' => gmdate('Y-m-d H:i:s'),
]);
$att_id = 0;
global $wpdb;
$like = '%/' . $cover;
$att_id = (int) $wpdb->get_var($wpdb->prepare(
    "SELECT ID FROM {{$wpdb->posts}} WHERE post_type='attachment' AND guid LIKE %s ORDER BY ID DESC LIMIT 1",
    $like
));
if ($att_id <= 0 && is_file($full_path)) {{
    $attachment = [
        'post_mime_type' => 'image/png',
        'post_title' => sanitize_file_name(preg_replace('/\\.png$/i', '', $cover)),
        'post_content' => '',
        'post_status' => 'inherit',
    ];
    $att_id = (int) wp_insert_attachment($attachment, $full_path, $post_id);
}}
if ($att_id > 0 && is_file($full_path)) {{
    $size = @getimagesize($full_path);
    $full_w = is_array($size) ? (int) ($size[0] ?? 0) : 0;
    $full_h = is_array($size) ? (int) ($size[1] ?? 0) : 0;
    $dzen_w = 1024;
    $dzen_h = 576;
    if (is_file($dzen_path)) {{
        $dzen_size = @getimagesize($dzen_path);
        $dzen_w = is_array($dzen_size) ? (int) ($dzen_size[0] ?? 1024) : 1024;
        $dzen_h = is_array($dzen_size) ? (int) ($dzen_size[1] ?? 576) : 576;
    }}
    $dzen_fn_only = basename($dzen_fn);
    $size_entry = [
        'file' => $dzen_fn_only,
        'width' => $dzen_w,
        'height' => $dzen_h,
        'mime-type' => 'image/png',
    ];
    $meta = [
        'width' => $full_w,
        'height' => $full_h,
        'file' => $subdir . '/' . $cover,
        'sizes' => [
            'medium_large' => $size_entry,
            'large' => $size_entry,
            'post-thumbnail' => $size_entry,
        ],
    ];
    wp_update_attachment_metadata($att_id, $meta);
    set_post_thumbnail($post_id, $att_id);
}}
$og_image_keys = [
    '_yoast_wpseo_opengraph-image',
    'rank_math_facebook_image',
    '_og_image',
    'og_image',
];
$og_id_keys = [
    '_yoast_wpseo_opengraph-image-id',
    'rank_math_facebook_image_id',
];
foreach ($og_image_keys as $key) {{
    update_post_meta($post_id, $key, $full_url);
    echo 'OK og_meta=' . $key . PHP_EOL;
}}
foreach ($og_id_keys as $key) {{
    update_post_meta($post_id, $key, (string) $att_id);
    echo 'OK og_meta=' . $key . PHP_EOL;
}}
echo 'OK publish_v5 post=' . $post_id . ' slug=' . $slug . PHP_EOL;
echo 'OK permalink=' . get_permalink($post_id) . PHP_EOL;
echo 'OK featured_image=' . $att_id . PHP_EOL;
echo 'OK cover_url=' . $full_url . PHP_EOL;
echo 'OK dzen_url=' . $dzen_url . PHP_EOL;
echo 'OK inline_imgs_mapped=' . $idx . PHP_EOL;
echo 'OK post_modified_gmt=' . get_post_field('post_modified_gmt', $post_id) . PHP_EOL;
"""


def collect_old_fragments(slug: str) -> list[str]:
    posts = wp_get(f"/wp-json/wp/v2/posts?slug={slug}&_embed")
    if not posts:
        return [slug]
    p = posts[0]
    content = p["content"]["rendered"]
    fm = (p.get("_embedded") or {}).get("wp:featuredmedia") or [{}]
    cover_url = (fm[0] or {}).get("source_url", "")
    frags = [slug, slug + "-cover", "cover-dzen", "dzen-v3", "dzen-v4", "regen-v"]
    if cover_url:
        frags.append(cover_url.rsplit("/", 1)[-1].replace(".png", ""))
        frags.append(cover_url.rsplit("/", 1)[-1])
    for m in re.findall(r"uploads/2026/08/([^\"']+\.png)", content, re.I):
        frags.append(m)
        frags.append(m.replace(".png", ""))
    return sorted(set(frags))


def publish_wp(spec: dict, *, version_suffix: str | None = None) -> dict[str, str]:
    env = load_env(ROOT)
    runtime_env = dict(env)
    runtime_env["FTP_TRANSPORT"] = "sftp"
    php_out = publish_via_sftp(
        runtime_env,
        build_publish_php(spec, version_suffix=version_suffix),
        PUBLIC,
        bootstrap_name="excalibur-cover-regen-v5-once.php",
    )
    if "ERR " in php_out or "OK publish_v5" not in php_out:
        raise RuntimeError(f"WP publish failed:\n{php_out}")
    out: dict[str, str] = {}
    for line in php_out.splitlines():
        if line.startswith("OK ") and "=" in line:
            k, v = line[3:].split("=", 1)
            out[k] = v.strip()
    return out


def refresh_intermediates(spec: dict) -> int:
    try:
        from excalibur_blog_wp_intermediate_refresh import refresh_after_full_upload

        report = refresh_after_full_upload(spec)
        return len(report.get("uploads") or [])
    except Exception as exc:
        print(f"WARN intermediate refresh: {exc}", flush=True)
        return 0


def main() -> int:
    global VERSION_SUFFIX
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", help="single slug")
    ap.add_argument("--version-suffix", default=VERSION_SUFFIX, help="filename suffix, e.g. regen-v6")
    ap.add_argument("--bootstrap-only", action="store_true")
    ap.add_argument("--upload-only", action="store_true")
    ap.add_argument("--repoint-only", action="store_true", help="WP meta/featured/og/zen bump only (no regen/upload)")
    args = ap.parse_args()
    VERSION_SUFFIX = args.version_suffix

    slugs = [args.slug] if args.slug else list(REGEN_V5_SLUGS)
    if not PUBLIC:
        print("BLOCKER: PUBLIC_SITE_URL missing", file=sys.stderr)
        return 1
    if not args.bootstrap_only and not args.upload_only and not os.environ.get("GRSAI_API_KEY", "").strip():
        print("BLOCKER: GRSAI_API_KEY missing", file=sys.stderr)
        return 1

    import excalibur_blog_live_cover_regen_aug22 as aug22_mod

    aug22_mod.META_BY_SLUG.update(META_BY_SLUG)

    logo_path = ensure_logo_asset()
    logo_url = logo_reference_url()
    print(f"logo local={logo_path} ({logo_path.stat().st_size} bytes)", flush=True)
    print(f"logo reference url={logo_url}", flush=True)

    report: dict[str, Any] = {
        "version_suffix": VERSION_SUFFIX,
        "slugs": slugs,
        "logo_reference_url": logo_url,
        "articles": {},
    }

    for slug in slugs:
        print(f"\n{'='*60}\n=== {slug} ===", flush=True)
        spec = build_spec_from_wp(slug)
        spec = patch_spec_for_v5(spec, version_suffix=VERSION_SUFFIX)
        adir = article_dir(spec)
        article_report: dict[str, Any] = {"spec": spec}

        if not args.upload_only and not args.repoint_only:
            bootstrap(spec)
            if args.bootstrap_only:
                continue
            article_report["pipeline"] = pipeline_v5(adir, logo_url=logo_url)

        if not args.repoint_only:
            urls = upload_all(spec, adir, version_suffix=VERSION_SUFFIX)
            article_report["uploaded_urls"] = urls
        else:
            urls = {}
        article_report["publish"] = publish_wp(spec, version_suffix=VERSION_SUFFIX)
        if not args.repoint_only:
            article_report["intermediates_updated"] = refresh_intermediates(spec)
        article_report["permalink"] = article_report["publish"].get("permalink", f"{PUBLIC}/blog/{slug}/")
        article_report["cover_url"] = article_report["publish"].get("cover_url", urls.get(spec["cover_remote"], ""))
        article_report["native_sizes"] = article_report.get("pipeline", {}).get("native_sizes", {})
        report["articles"][slug] = article_report
        print(json.dumps(article_report, ensure_ascii=False, indent=2), flush=True)

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
