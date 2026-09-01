#!/usr/bin/env python3
"""Live B06 rewrite — dobry_dom_gen_only_human_v1: text + 1 Grsai draw + slice + logo + SFTP."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from excalibur_blog_live_cover_regen_aug22 import article_dir, wp_get  # noqa: E402
from excalibur_blog_live_cover_regen_v5 import upload_all  # noqa: E402
from excalibur_blog_site_base import resolve_public_base_from_env  # noqa: E402
from excalibur_blog_wp_publish import load_env, project_root, publish_via_sftp  # noqa: E402

ROOT = project_root()
PUBLIC = (resolve_public_base_from_env() or os.environ.get("PUBLIC_SITE_URL", "")).rstrip("/")
SLUG = "vyezd-v-12-00-poezd-v-16-30-kuda-chemodany"
WP_POST_ID = 4274
TOPIC_ID = "B06"
VERSION_SUFFIX = "gen-only-v1"
UPLOAD_SUBDIR = "2026/09"
REPORT_PATH = ROOT / "memory/blog/live-b06-gen-only-rewrite-report.json"

NEW_H1 = "Выезд в 12:00, поезд в 16:30 — +2 100 ₽, а чемоданы в коридоре"

H2S = (
    "Полдень — это про уборку, не про ваш поезд",
    "2 100 ₽ — не штраф, а вопрос времени",
    "Подъезд — не камера хранения",
    "Мой вывод как практика",
)

BRIEF = """
Кейс B06 переписать в dobry_dom_gen_only_human_v1.
Суть: гость выезжает в 12:00, поезд в 16:30, хост берёт +2 100 ₽ за поздний выезд,
а чемоданы некуда деть — предлагают оставить в коридоре подъезда.
H1: {h1}
Телефон +7 (993) 574-83-22 только в тексте статьи в конце, не на картинке.
700–900 слов, разговор у двери, первые 2–3 предложения: цитата или ₽.
4 H2: {h2s}
Один mid fight-question → Telegram/MAX. Один CTA в конце.
3 перелинковки на sibling из published-articles.
HARD: без HH:MM в теле; «Нет. Так не заселяем.» max 1 раз;
обязательно identity: «Я хост посуточной в Тюмени. Это «Добрый дом».» после §1;
чистый HTML без markdown fences.
""".format(h1=NEW_H1, h2s=" | ".join(H2S))


def _run(cmd: list[str], *, cwd: Path | None = None, allow_fail: bool = False) -> int:
    print("+", " ".join(cmd), flush=True)
    proc = subprocess.run(cmd, cwd=cwd or ROOT, capture_output=True, text=True)
    if proc.stdout:
        print(proc.stdout, end="", flush=True)
    if proc.returncode != 0:
        print(proc.stderr, file=sys.stderr, flush=True)
        if not allow_fail:
            raise RuntimeError(f"command failed: {' '.join(cmd)}")
    return proc.returncode


def build_spec() -> dict[str, Any]:
    posts = wp_get(f"/wp-json/wp/v2/posts/{WP_POST_ID}?_embed")
    if isinstance(posts, list):
        p = posts[0]
    else:
        p = posts
    return {
        "topic_id": TOPIC_ID,
        "slug": SLUG,
        "h1": NEW_H1,
        "hook": "чемоданы в коридоре",
        "highlight": "чемоданы",
        "sticky": "",
        "wordstat": ["поздний выезд", "посуточно тюмень", "чемоданы"],
        "cover_remote": f"{SLUG}-cover-{VERSION_SUFFIX}.png",
        "inline_remote": f"{SLUG}-inline-{{n:02d}}-{VERSION_SUFFIX}.png",
        "h2s": list(H2S),
        "cover_emotion": "усталость: выезд в полдень, поезд вечером, чемоданы в коридоре",
        "cover_scene": (
            "Bright Tyumen apartment hallway, two suitcases by door, printed paper on table "
            "with Cyrillic headline about late checkout fee — photoreal, no graphic overlays"
        ),
        "motif_composition": "hallway suitcases + paper note on table",
        "motif_props": "suitcases, door, printed paper",
    }


def bootstrap_article(spec: dict[str, Any]) -> Path:
    adir = article_dir(spec)
    adir.mkdir(parents=True, exist_ok=True)
    (adir / "drafts").mkdir(exist_ok=True)
    (adir / "cover").mkdir(exist_ok=True)

    (adir / "title-brief.json").write_text(
        json.dumps(
            {
                "h1": spec["h1"],
                "title": spec["h1"],
                "hook": spec["hook"],
                "manner_canon": "dobry_dom_gen_only_human_v1",
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    brief_path = adir / "rewrite-brief.md"
    brief_path.write_text(BRIEF.strip() + "\n", encoding="utf-8")

    (adir / "research-notes.md").write_text(
        """# B06 — поздний выезд и чемоданы

- Гость: выезд по правилам в 12:00, поезд в 16:30
- Хост: +2 100 ₽ за поздний выезд / хранение
- Боль: чемоданы некуда — предлагают коридор подъезда
- Цитата гостя: «Куда мне с чемоданами до четырёх?»
- Хост: «Оставьте в коридоре, камеры нет»
""",
        encoding="utf-8",
    )

    _run(
        [
            sys.executable,
            "scripts/excalibur_blog_derouter_opus_chat.py",
            "--role",
            "writer",
            "--article-dir",
            str(adir.relative_to(ROOT)),
            "--system-file",
            "shared/writer-master-prompt.md",
            "--user-prompt",
            BRIEF.strip(),
            "--output",
            "drafts/writer.html",
        ]
    )
    _run(
        [
            sys.executable,
            "scripts/excalibur_blog_case_delivery_gate.py",
            "--article-dir",
            str(adir.relative_to(ROOT)),
            "--stage",
            "writer",
        ],
        allow_fail=True,
    )
    _run(
        [
            sys.executable,
            "scripts/excalibur_blog_derouter_opus_chat.py",
            "--role",
            "sol",
            "--article-dir",
            str(adir.relative_to(ROOT)),
            "--system-file",
            "shared/SOUL.md",
            "--user-file",
            str((adir / "drafts" / "writer.html").relative_to(ROOT)),
            "--output",
            "article.html",
        ]
    )
    _run(
        [
            sys.executable,
            "scripts/excalibur_blog_case_delivery_gate.py",
            "--article-dir",
            str(adir.relative_to(ROOT)),
            "--stage",
            "article",
        ]
    )

    meta = {
        "title": spec["h1"],
        "h1": spec["h1"],
        "slug": SLUG,
        "topic_id": TOPIC_ID,
        "author_id": "dobry-dom",
        "pipeline_canon": "human-first-v3",
        "editorial_manner_canon": "dobry_dom_gen_only_human_v1",
        "cover_pipeline_canon": "dobry_dom_gen_only_human_v1",
        "wp_category_slugs": ["posutochnaya-arenda", "sovety-gostyam"],
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }
    (adir / "article.meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return adir


def cover_pipeline(adir: Path) -> None:
    rel = str(adir.relative_to(ROOT))
    _run([sys.executable, "scripts/excalibur_blog_cover_text_gate.py", "--article-dir", rel])
    _run([sys.executable, "scripts/excalibur_blog_quad_manifest.py", "--article-dir", rel, "--merge"])
    _run([sys.executable, "scripts/excalibur_blog_cover_quad_prompt.py", "--article-dir", rel, "--write-batch"])
    _run(
        [
            sys.executable,
            "scripts/excalibur_blog_grsai_gpt_image2_api.py",
            "--article-dir",
            rel,
            "--batch",
            "cover/slice4-mcp-batch.json",
            "--result",
            "cover/slice4-mcp-result.json",
        ]
    )
    _run(
        [
            sys.executable,
            "scripts/excalibur_blog_cover_quad_split.py",
            "--article-dir",
            rel,
            "--inject-html",
        ]
    )
    _run([sys.executable, "scripts/excalibur_blog_brand_logo_composite.py", "--article-dir", rel])
    _run([sys.executable, "scripts/excalibur_blog_slice4_gate.py", "--article-dir", rel])


def build_publish_php(spec: dict[str, Any], html: str, urls: dict[str, str]) -> str:
    import base64

    inlines = [spec["inline_remote"].format(n=n) for n in range(1, 4)]
    payload = {
        "post_id": WP_POST_ID,
        "title": spec["h1"],
        "content": html,
        "upload_subdir": UPLOAD_SUBDIR,
        "cover_remote": spec["cover_remote"],
        "inlines": inlines,
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
$cover = (string)($p['cover_remote'] ?? '');
$content = (string)($p['content'] ?? '');
$title = (string)($p['title'] ?? '');
wp_update_post([
  'ID' => $post_id,
  'post_title' => $title,
  'post_content' => wp_slash($content),
  'post_modified' => current_time('mysql'),
  'post_modified_gmt' => gmdate('Y-m-d H:i:s'),
]);
$upload = wp_upload_dir();
$cover_path = $upload['basedir'] . '/' . $subdir . '/' . $cover;
$cover_url = $upload['baseurl'] . '/' . $subdir . '/' . $cover;
$att_id = attachment_url_to_postid($cover_url);
if ($att_id <= 0 && is_file($cover_path)) {{
  $attachment = [
    'post_mime_type' => 'image/png',
    'post_title' => sanitize_file_name(preg_replace('/\\.png$/i', '', $cover)),
    'post_content' => '',
    'post_status' => 'inherit',
    'guid' => $cover_url,
  ];
  $att_id = (int) wp_insert_attachment($attachment, $cover_path, $post_id);
  if ($att_id > 0) {{
    wp_update_attachment_metadata($att_id, wp_generate_attachment_metadata($att_id, $cover_path));
  }}
}}
if ($att_id > 0) {{
  set_post_thumbnail($post_id, $att_id);
}}
echo 'OK post_updated=' . $post_id . PHP_EOL;
echo 'OK attachment_id=' . (int)$att_id . PHP_EOL;
echo 'OK permalink=' . get_permalink($post_id) . PHP_EOL;
"""


def inject_inline_urls(html: str, urls: dict[str, str], spec: dict[str, Any]) -> str:
    for i in range(1, 4):
        key = spec["inline_remote"].format(n=i)
        url = urls.get(key, "")
        if not url:
            continue
        html = re.sub(
            rf'(<figure[^>]*data-slot="inline_{i}"[^>]*>\s*<img[^>]*src=")[^"]+(")',
            rf"\1{url}\2",
            html,
            count=1,
            flags=re.I | re.S,
        )
    return html.replace("{{SITE_BASE}}", PUBLIC)


def main() -> int:
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

    spec = build_spec()
    adir = bootstrap_article(spec)
    cover_pipeline(adir)

    urls = upload_all(spec, adir, version_suffix=VERSION_SUFFIX)
    html = (adir / "article.html").read_text(encoding="utf-8")
    html = inject_inline_urls(html, urls, spec)

    runtime_env = dict(env)
    runtime_env["FTP_TRANSPORT"] = "sftp"
    php_out = publish_via_sftp(
        runtime_env,
        build_publish_php(spec, html, urls),
        PUBLIC,
        bootstrap_name="excalibur-b06-gen-only-once.php",
    )
    if "ERR " in php_out or "OK post_updated" not in php_out:
        raise RuntimeError(f"WP publish failed:\n{php_out}")

    draw_results = list((adir / "cover").glob("*-mcp-result*.json"))
    report = {
        "slug": SLUG,
        "wp_post_id": WP_POST_ID,
        "h1": spec["h1"],
        "permalink": f"{PUBLIC}/blog/{SLUG}/",
        "grsai_draws": len(draw_results),
        "uploaded": urls,
        "version_suffix": VERSION_SUFFIX,
        "canon": "dobry_dom_gen_only_human_v1",
        "php_out": php_out.strip(),
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
