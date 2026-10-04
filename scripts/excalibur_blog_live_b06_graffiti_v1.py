#!/usr/bin/env python3
"""Live B06: graffiti WOW cover (Grsai vip full-bleed) + H1 #4 + og:image fix."""

from __future__ import annotations

import base64
import json
import os
import re
import subprocess
import sys
import time
from io import BytesIO
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from excalibur_blog_site_base import resolve_public_base_from_env  # noqa: E402
from excalibur_blog_wp_publish import (  # noqa: E402
    delete_bootstrap_sftp,
    load_env,
    project_root,
    publish_via_sftp,
    sftp_remote_path,
    sftp_root_candidates,
    upload_bootstrap_sftp,
    _ssh_creds,
    is_missing_remote_path_error,
)

ROOT = project_root()
PUBLIC = (resolve_public_base_from_env() or os.environ.get("PUBLIC_SITE_URL", "")).rstrip("/")
SLUG = "vyezd-v-12-00-poezd-v-16-30-kuda-chemodany"
TOPIC_ID = "B06"
WP_POST_ID = 4274
VERSION_TAG = "cover-graffiti-v1"
REMOTE_SUBDIR = "2026/09"
DZEN_SIZE = (1024, 576)
REPORT_PATH = ROOT / "memory/blog/live-b06-graffiti-v1-report.json"

NEW_H1 = (
    "Сняли квартиру посуточно. Хотели дождаться поезда. "
    "У двери: +2 100 ₽ или чемоданы в подъезд"
)

COVER_PROMPT = (
    "EDITORIAL 16:9 Dzen cover poster 2048×1152 full-bleed cinematic still, photoreal Tyumen "
    "daily-rental apartment doorway and stairwell, natural daylight. Bold beautiful GRAFFITI / "
    "mural / spray-painted Cyrillic headline painted ON the wall or door — huge readable stylish "
    "street lettering with wow energy, NOT Arial on white tent card, NOT Canva sticker, NOT printed "
    "paper on table. Split headline across 2–3 lines exactly:\n"
    "Сняли квартиру посуточно.\n"
    "Хотели дождаться поезда.\n"
    "У двери: +2 100 ₽ или чемоданы в подъезд\n"
    "Scene: two suitcases in a bright stairwell OR guest at apartment door facing +2100 rub late "
    "checkout fork. Lighting matches the photo. Russian Cyrillic only, no Latin garbage text. "
    "Few or zero faces. TOP-RIGHT corner must stay EMPTY — plain wall/ceiling texture only, "
    "NO gray/white rectangle, NO logo pad, NO blank card, NO light box — leave clean area "
    "for factory logo paste later. Do NOT draw any logo or brand mark. Phone may appear as a real object in the scene, "
    "not a UI pill overlay.\n"
    "BAN: meme cutouts, sticker soup, torn-paper collage, split white-panel headline, table tent, "
    "printed paper note headline, phone pill overlay, model-drawn logo, dashed frame plaque, "
    "empty stock hallway, gray/white logo placeholder rectangle top-right."
)


def article_dir() -> Path:
    return ROOT / f"memory/blog/articles/{TOPIC_ID}-{SLUG}"


def remote_cover_name() -> str:
    return f"{SLUG}-{VERSION_TAG}.png"


def remote_dzen_name() -> str:
    return f"{SLUG}-{VERSION_TAG}-1024x576.png"


def wp_get_post() -> dict[str, Any]:
    url = f"{PUBLIC}/wp-json/wp/v2/posts/{WP_POST_ID}"
    with urlopen(Request(url, headers={"User-Agent": "ExcaliburBlog/1.0"}), timeout=90) as resp:
        return json.loads(resp.read().decode("utf-8"))


def content_without_duplicate_h1(html: str, *, new_h1: str) -> str:
    """Убрать on-page H1 из контента — тема рисует один H1 из post_title."""
    out = re.sub(r"<h1\b[^>]*>.*?</h1>\s*", "", html, count=1, flags=re.I | re.S)
    if out.lstrip().startswith("<h1"):
        out = re.sub(r"<h1\b[^>]*>.*?</h1>\s*", "", out, count=1, flags=re.I | re.S)
    return out.strip() + "\n"


def write_cover_batch(adir: Path, *, attempt: int) -> None:
    cover_dir = adir / "cover"
    cover_dir.mkdir(parents=True, exist_ok=True)
    prompt = COVER_PROMPT
    if attempt > 1:
        prompt += (
            "\nRETRY: Cyrillic graffiti letters must be sharp, correctly spelled Russian words, "
            "fully readable at thumbnail size — no smashed glyphs."
        )
    (cover_dir / "cover-mcp-prompt.txt").write_text(prompt + "\n", encoding="utf-8")
    batch = {
        "pipeline": "b06_graffiti_full_bleed_v1",
        "canvas_index": 0,
        "standalone_cover": True,
        "model_policy": "vip_only",
        "output_canvas": "cover/cover-canvas.png",
        "result_path": "cover/cover-mcp-result.json",
        "jobs": [
            {
                "slot": "cover_standalone",
                "tool": "grsai",
                "mcp_args": {
                    "prompt": prompt,
                    "aspect_ratio": "16:9",
                    "resolution": "2K",
                },
            }
        ],
    }
    (cover_dir / "cover-mcp-batch.json").write_text(
        json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def generate_cover_canvas(adir: Path, *, attempt: int) -> Path:
    write_cover_batch(adir, attempt=attempt)
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
            "vip",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"Grsai vip generation failed (attempt {attempt}): {proc.stderr or proc.stdout}")

    result_path = adir / "cover" / "cover-mcp-result.json"
    result = json.loads(result_path.read_text(encoding="utf-8"))
    local_rel = str(result.get("local_path") or "cover/cover-canvas.png")
    canvas_path = adir / local_rel
    if not canvas_path.is_file():
        canvas_path = adir / "cover" / "cover-canvas.png"
    if not canvas_path.is_file():
        raise FileNotFoundError("cover-canvas.png missing after generation")
    return canvas_path


def apply_cover_pipeline(adir: Path) -> Path:
    proc = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/excalibur_blog_cover_standalone_apply.py"),
            "--article-dir",
            str(adir),
            "--source",
            "cover-canvas.png",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"standalone apply failed: {proc.stderr or proc.stdout}")

    rel = adir.relative_to(ROOT)
    proc2 = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts/excalibur_blog_brand_logo_composite.py"),
            "--article-dir",
            str(rel),
            "--cover-only",
            "--after-pad-clear",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        env={**os.environ, "PYTHONPATH": str(ROOT / "scripts")},
    )
    if proc2.returncode != 0:
        raise RuntimeError(f"logo composite failed: {proc2.stderr or proc2.stdout}")

    cover_path = adir / "cover" / "cover.png"
    if not cover_path.is_file():
        raise FileNotFoundError("cover.png missing after apply")
    return cover_path


def make_dzen_thumb(cover_path: Path) -> bytes:
    from PIL import Image

    with Image.open(cover_path) as img:
        thumb = img.convert("RGBA").resize(DZEN_SIZE, Image.Resampling.LANCZOS)
        buf = BytesIO()
        thumb.save(buf, format="PNG", optimize=True)
        return buf.getvalue()


def upload_cover_files(cover_path: Path) -> dict[str, str]:
    import paramiko

    env = load_env(ROOT)
    public = PUBLIC
    cover_remote = remote_cover_name()
    dzen_remote = remote_dzen_name()
    files = {
        cover_remote: cover_path.read_bytes(),
        dzen_remote: make_dzen_thumb(cover_path),
    }
    remote_dir = f"wp-content/uploads/{REMOTE_SUBDIR}"
    cache_bust = int(time.time())
    urls: dict[str, str] = {}
    host, port, user, password = _ssh_creds(env)
    transport = paramiko.Transport((host, port))
    transport.connect(username=user, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    try:
        for remote_name, data in files.items():
            remote_path = f"{remote_dir}/{remote_name}"
            uploaded = False
            for root_candidate in sftp_root_candidates(env):
                full = sftp_remote_path(env, remote_path, root_candidate)
                try:
                    with sftp.open(full, "wb") as handle:
                        handle.write(data)
                    print(f"SFTP upload OK: {full} ({len(data)} bytes)", flush=True)
                    urls[remote_name] = f"{public}/{remote_dir}/{remote_name}?v={cache_bust}"
                    uploaded = True
                    break
                except OSError as exc:
                    if is_missing_remote_path_error(exc):
                        continue
                    raise
            if not uploaded:
                raise RuntimeError(f"SFTP upload failed for {remote_path}")
    finally:
        sftp.close()
        transport.close()
    return urls


def build_update_php(*, content_html: str, title: str) -> str:
    payload = {
        "post_id": WP_POST_ID,
        "title": title,
        "content": content_html,
        "upload_subdir": REMOTE_SUBDIR,
        "cover_remote": remote_cover_name(),
        "dzen_remote": remote_dzen_name(),
    }
    b64 = base64.b64encode(json.dumps(payload, ensure_ascii=False).encode("utf-8")).decode("ascii")
    return f"""<?php
require __DIR__ . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/image.php';
$p = json_decode(base64_decode('{b64}'), true);
$post_id = (int)($p['post_id'] ?? 0);
$post = get_post($post_id);
if (!$post) {{ echo 'ERR post_not_found id=' . $post_id . PHP_EOL; exit(1); }}
$subdir = (string)($p['upload_subdir'] ?? '2026/09');
$cover_remote = (string)($p['cover_remote'] ?? '');
$dzen_remote = (string)($p['dzen_remote'] ?? '');
$title = (string)($p['title'] ?? '');
$content = (string)($p['content'] ?? '');
wp_update_post([
  'ID' => $post_id,
  'post_title' => $title,
  'post_content' => wp_slash($content),
  'post_modified' => current_time('mysql'),
  'post_modified_gmt' => gmdate('Y-m-d H:i:s'),
]);
update_post_meta($post_id, '_yoast_wpseo_title', $title);
update_post_meta($post_id, '_yoast_wpseo_opengraph-title', $title);
$upload = wp_upload_dir();
$cover_path = $upload['basedir'] . '/' . $subdir . '/' . $cover_remote;
$dzen_path = $dzen_remote !== '' ? $upload['basedir'] . '/' . $subdir . '/' . $dzen_remote : '';
$cover_url = $upload['baseurl'] . '/' . $subdir . '/' . $cover_remote;
if (!is_file($cover_path)) {{
  echo 'ERR cover_missing path=' . $cover_path . PHP_EOL;
  exit(1);
}}
$att_id = attachment_url_to_postid($cover_url);
if ($att_id <= 0) {{
  $attachment = [
    'post_mime_type' => 'image/png',
    'post_title' => sanitize_file_name(preg_replace('/\\.png$/i', '', $cover_remote)),
    'post_content' => '',
    'post_status' => 'inherit',
    'guid' => $cover_url,
  ];
  $att_id = (int) wp_insert_attachment($attachment, $cover_path, $post_id);
  if ($att_id > 0) {{
    $meta = wp_generate_attachment_metadata($att_id, $cover_path);
    if (is_array($meta) && $dzen_remote !== '' && is_file($dzen_path)) {{
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
    wp_update_attachment_metadata($att_id, $meta);
  }}
}}
if ($att_id > 0) {{
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
  update_post_meta($post_id, $key, $cover_url);
}}
foreach ($og_id_keys as $key) {{
  update_post_meta($post_id, $key, (string) $att_id);
}}
update_post_meta($post_id, '_excalibur_cover_remote', $cover_remote);
echo 'OK post_updated=' . $post_id . PHP_EOL;
echo 'OK post_title=' . get_the_title($post_id) . PHP_EOL;
echo 'OK attachment_id=' . (int)$att_id . PHP_EOL;
echo 'OK cover_url=' . $cover_url . PHP_EOL;
echo 'OK permalink=' . get_permalink($post_id) . PHP_EOL;
"""


def run_wp_update(*, content_html: str) -> str:
    env = load_env(ROOT)
    runtime_env = dict(env)
    runtime_env["FTP_TRANSPORT"] = "sftp"
    php = build_update_php(content_html=content_html, title=NEW_H1)
    return publish_via_sftp(
        runtime_env,
        php,
        PUBLIC,
        bootstrap_name="excalibur-b06-graffiti-v1-once.php",
    )


def verify_live() -> dict[str, Any]:
    html = urlopen(
        Request(
            f"{PUBLIC}/blog/{SLUG}/",
            headers={"User-Agent": "ExcaliburBlog/1.0"},
        ),
        timeout=90,
    ).read().decode("utf-8", errors="replace")
    h1s = re.findall(r"<h1\b[^>]*>(.*?)</h1>", html, flags=re.I | re.S)
    h1_texts = [re.sub(r"<[^>]+>", "", h).strip() for h in h1s]
    og = re.search(r'property="og:image"\s+content="([^"]+)"', html)
    og_image = og.group(1) if og else ""
    featured = re.search(r'wp-post-image[^>]+src="([^"]+)"', html)
    if not featured:
        featured = re.search(r'src="([^"]+cover-graffiti-v1[^"]+)"', html)
    featured_src = featured.group(1) if featured else ""
    return {
        "h1_count": len(h1_texts),
        "h1_texts": h1_texts,
        "og_image": og_image,
        "featured_src": featured_src,
    }


def sync_local_article(content_html: str) -> None:
    adir = article_dir()
    adir.mkdir(parents=True, exist_ok=True)
    (adir / "article.html").write_text(content_html, encoding="utf-8")
    meta_path = adir / "article.meta.json"
    meta: dict[str, Any] = {}
    if meta_path.is_file():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    meta.update({"title": NEW_H1, "h1": NEW_H1, "slug": SLUG, "topic_id": TOPIC_ID})
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tb = adir / "title-brief.json"
    tb.write_text(
        json.dumps({"h1": NEW_H1, "title": NEW_H1}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-generate", action="store_true", help="Use existing cover-canvas.png")
    args = ap.parse_args()

    if not PUBLIC:
        print("BLOCKER: PUBLIC_SITE_URL missing", file=sys.stderr)
        return 1
    if not os.environ.get("GRSAI_API_KEY", "").strip():
        print("BLOCKER: GRSAI_API_KEY missing", file=sys.stderr)
        return 1
    env = load_env(ROOT)
    for key in ("FTP_HOST", "FTP_USER", "FTP_PASS"):
        if not (env.get(key) or os.environ.get(key)):
            print(f"BLOCKER: {key} missing", file=sys.stderr)
            return 1

    adir = article_dir()
    adir.mkdir(parents=True, exist_ok=True)

    wp_post = wp_get_post()
    content_html = content_without_duplicate_h1(wp_post["content"]["rendered"], new_h1=NEW_H1)
    sync_local_article(content_html)

    cover_path: Path | None = None
    if args.skip_generate:
        canvas = adir / "cover" / "cover-canvas.png"
        if not canvas.is_file():
            raise RuntimeError(f"missing {canvas} for --skip-generate")
        print("STEP apply standalone + logo paste (skip-generate)", flush=True)
        cover_path = apply_cover_pipeline(adir)
    else:
        last_error: Exception | None = None
        for attempt in (1, 2):
            try:
                print(f"STEP generate graffiti cover attempt={attempt}", flush=True)
                generate_cover_canvas(adir, attempt=attempt)
                print("STEP apply standalone + logo paste", flush=True)
                cover_path = apply_cover_pipeline(adir)
                break
            except Exception as exc:
                last_error = exc
                print(f"WARN attempt {attempt} failed: {exc}", flush=True)
        if cover_path is None:
            raise RuntimeError(f"cover generation failed: {last_error}")

    print("STEP upload SFTP", flush=True)
    urls = upload_cover_files(cover_path)
    print("STEP update WP title/content/featured/og", flush=True)
    php_out = run_wp_update(content_html=content_html)
    print(php_out, flush=True)
    if "ERR " in php_out or "OK post_updated" not in php_out:
        raise RuntimeError(f"WP update failed:\n{php_out}")

    live = verify_live()
    att_id = 0
    for line in php_out.splitlines():
        if line.startswith("OK attachment_id="):
            att_id = int(line.split("=", 1)[1])

    remote_path = f"wp-content/uploads/{REMOTE_SUBDIR}/{remote_cover_name()}"
    report = {
        "slug": SLUG,
        "wp_post_id": WP_POST_ID,
        "h1": NEW_H1,
        "url": f"{{{{PUBLIC_SITE_URL}}}}/blog/{SLUG}/",
        "cover_remote": remote_cover_name(),
        "cover_url": f"{{{{PUBLIC_SITE_URL}}}}/wp-content/uploads/{REMOTE_SUBDIR}/{remote_cover_name()}",
        "remote_path": remote_path,
        "media_id": att_id,
        "uploaded": {
            remote_cover_name(): f"{{{{PUBLIC_SITE_URL}}}}/wp-content/uploads/{REMOTE_SUBDIR}/{remote_cover_name()}",
            remote_dzen_name(): f"{{{{PUBLIC_SITE_URL}}}}/wp-content/uploads/{REMOTE_SUBDIR}/{remote_dzen_name()}",
        },
        "php_out": php_out.strip(),
        "live_verify": {
            "h1_count": live["h1_count"],
            "h1_texts": live["h1_texts"],
            "og_image_contains": remote_cover_name(),
            "featured_contains": remote_cover_name(),
        },
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))

    ok = (
        live["h1_count"] == 1
        and NEW_H1 in live["h1_texts"]
        and remote_cover_name() in live.get("og_image", "")
        and remote_cover_name() in live.get("featured_src", "")
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
