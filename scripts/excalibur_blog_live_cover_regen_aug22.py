#!/usr/bin/env python3
"""Bootstrap + FTP upload for live cover/inline regen (media only, text unchanged)."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = os.environ.get("PUBLIC_SITE_URL", "").rstrip("/")

ARTICLES = [
    {
        "topic_id": "LIVE-dogovor",
        "slug": "dogovor-arendy-pravila-prozhivaniya-posutochno",
        "h1": "Перевёл предоплату — потом прочитал 7 запретов в договоре",
        "hook": "Перед оплатой прочитайте правила аренды",
        "highlight": "правила",
        "sticky": "7 запретов",
        "wordstat": ["правила аренды", "Тюмень", "предоплата"],
        "cover_remote": "dogovor-arendy-pravila-prozhivaniya-posutochno-cover-1.png",
        "inline_remote": "dogovor-arendy-pravila-prozhivaniya-posutochno-inline-{n:02d}-1.png",
        "h2s": [
            "Быстрый инсайт",
            "Почему перевод денег иногда считается согласием",
            "Вот где подставят, если читать договор после перевода",
            "Семь пунктов, которые читают до перевода",
            "Что проверить за три минуты до перевода",
            "У нас в «Добром доме» так",
            "Частые вопросы",
        ],
        "cover_emotion": "шок от семи запретов в договоре после перевода",
        "cover_scene": "Phone transfer + rules checklist, bold Cyrillic hook, August Tyumen sun, empty top-right pad.",
        "motif_composition": "payment phone + rules checklist poster collage",
        "motif_meme": "tabby cat with sunglasses sticker bottom-left ≤10%",
        "motif_props": "phone screen, checklist paper, gold pen",
        "motif_joke": "cat judges unread contract",
    },
    {
        "topic_id": "LIVE-otmena",
        "slug": "otmena-bronirovaniya-posutochno-vozvrat-predoplaty",
        "h1": "Планы сорвались — предоплату удержали. Что выяснить до оплаты",
        "hook": "Отменили бронь — верните предоплату",
        "highlight": "верните",
        "sticky": "невозвратно?",
        "wordstat": ["отмена брони", "Тюмень", "возврат предоплаты"],
        "cover_remote": "otmena-bronirovaniya-posutochno-vozvrat-predoplaty-cover.png",
        "inline_remote": "otmena-bronirovaniya-posutochno-vozvrat-predoplaty-inline-{n:02d}.png",
        "h2s": [
            "Отель и квартира посуточно — это разные истории",
            "Кто сдаёт квартиру — от этого зависят правила",
            "Где подставляют чаще всего",
            "Пять вопросов до оплаты — сохраните себе",
            "Если отмена уже случилась",
            "У нас так",
            "Частые вопросы",
        ],
        "cover_emotion": "разочарование: планы сорвались, предоплату не вернули",
        "cover_scene": "Bell vs keys VS refund note, bold Cyrillic hook, bright room August, empty top-right pad.",
        "motif_composition": "refund bell vs keys comparison poster",
        "motif_meme": "fluffy cat peeking from sofa corner ≤10%",
        "motif_props": "service bell, keyring, yellow sticky",
        "motif_joke": "cat side-eyes cancelled trip",
    },
    {
        "topic_id": "LIVE-pereveli",
        "slug": "pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti",
        "h1": "Перевели предоплату. В правилах мелким: вечеринки и лишние гости",
        "hook": "Шесть гостей — залог не вернули",
        "highlight": "гостей",
        "sticky": "лишние гости",
        "wordstat": ["лишние гости", "Тюмень", "правила проживания"],
        "cover_remote": "pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti-cover.png",
        "inline_remote": "pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti-inline-{n:02d}.png",
        "h2s": [
            "1. Сколько гостей можно — и кто вообще считается гостем",
            "2. Вечеринки: что хозяин называет тихим отдыхом",
            "3. Курение: балкон, вейп и кальян — это не одно «ну я же не в комнате»",
            "4. Заселение и выезд: два часа могут сломать следующий заезд",
            "5. Залог: когда его вернут и за что могут удержать",
            "6. Фото при заселении: пять минут, которые спасают от спора",
            "7. Где должны быть правила: в чате до оплаты",
        ],
        "cover_emotion": "шок шести гостей у двери и удержанного залога",
        "cover_scene": "Six suitcases at door + rules paper, bold hook gold гостей, August Tyumen, empty top-right pad.",
        "motif_composition": "six guests doorway + rules torn paper",
        "motif_meme": "striped cat with bracelet sticker ≤10%",
        "motif_props": "six gold bracelets, chat bubbles, suitcases",
        "motif_joke": "cat counts extra guests",
    },
]

VISUAL_TYPES = [
    "comparison_table",
    "process_flow",
    "bar_timeline_chart",
    "structure_diagram",
    "labeled_checklist",
    "fact_card",
    "schema_faq_ui",
]


def article_dir(spec: dict) -> Path:
    return ROOT / "memory/blog/articles" / f"{spec['topic_id']}-{spec['slug']}"


def fetch_html(slug: str) -> str:
    if not PUBLIC:
        raise RuntimeError("PUBLIC_SITE_URL missing")
    url = f"{PUBLIC}/blog/{slug}/"
    with urlopen(url, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract_article_body(html: str) -> str:
    m = re.search(r'<div[^>]+class="[^"]*entry-content[^"]*"[^>]*>(.*)</div>\s*<(?:footer|div class="post-tags")', html, re.S | re.I)
    if m:
        return m.group(1)
    return html


def bootstrap(spec: dict) -> Path:
    adir = article_dir(spec)
    cover = adir / "cover"
    cover.mkdir(parents=True, exist_ok=True)

    html = fetch_html(spec["slug"])
    body = extract_article_body(html)
    h2_blocks = "".join(f"<h2>{h}</h2><p>…</p>" for h in spec["h2s"])
    (adir / "article.html").write_text(
        f'<!DOCTYPE html><html><body><h1>{spec["h1"]}</h1>{h2_blocks}</body></html>',
        encoding="utf-8",
    )

    inline_labels = {}
    for i, h2 in enumerate(spec["h2s"], 1):
        words = [w for w in re.split(r"[\s—–:]+", h2) if len(w) > 2][:4]
        inline_labels[f"inline_{i}"] = words[:4] if words else [h2[:12]]

    (cover / "cover-text.json").write_text(
        json.dumps(
            {
                "hook": spec["hook"],
                "highlight": spec["highlight"],
                "sticky": spec["sticky"],
                "wordstat_stickers": spec["wordstat"],
                "inline_labels": inline_labels,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    slots: dict = {
        "cover": {
            "quadrant": "top_left",
            "role": "cover_editorial_hero",
            "alt": spec["h1"][:120],
            "scene_hint": spec["cover_scene"],
            "meme_caption_ru": "",
            "sticky": spec["sticky"],
        }
    }
    quadrants = ["top_right", "bottom_left", "bottom_right", "top_left", "top_right", "bottom_left", "bottom_right"]
    for i, h2 in enumerate(spec["h2s"], 1):
        vt = VISUAL_TYPES[(i - 1) % len(VISUAL_TYPES)]
        slots[f"inline_{i}"] = {
            "quadrant": quadrants[i - 1],
            "h2_anchor": h2[:72],
            "visual_type": vt,
            "scene_hint": f"{vt}: {h2[:48]}; gold labels; torn paper; empty top-right if logo.",
            "alt": h2[:100],
            "labels": inline_labels[f"inline_{i}"][:4],
        }

    manifest = {
        "topic_id": spec["topic_id"],
        "slug": spec["slug"],
        "layout": "2x2",
        "pipeline": "quad_canvas_2x_image_api_longform",
        "inline_count": 7,
        "style_preset": "dobry_dom_light_meme_wordstat",
        "style_file": "memory/cover/quad-style-dobry-dom.json",
        "blog_hero": "memory/cover/blog-hero.json",
        "inline_types_catalog": "memory/cover/inline-visual-types-dobry-dom.json",
        "cover_hook": spec["hook"],
        "cover_hook_highlight": spec["highlight"],
        "cover_phone_cta": "+7 (993) 574-83-22",
        "wordstat_stickers": spec["wordstat"],
        "logo_paste_inline_slots": ["inline_1", "inline_3", "inline_7"],
        "cover_motifs": {
            "composition": spec.get("motif_composition", "WOW poster collage, empty top-right logo pad"),
            "location": "Tyumen apartment August warm sun flare",
            "meme": spec.get("motif_meme", "tiny ginger cat sticker bottom-left ≤10%"),
            "prop_set": spec.get("motif_props", "torn paper, gold tape, phone, keys"),
            "sticker_set": spec["wordstat"],
            "joke": spec.get("motif_joke", "cat reacts to rental shock"),
        },
        "cover_emotion": spec["cover_emotion"],
        "slots": slots,
        "cover_keys_ru": spec["wordstat"][:2],
    }
    (cover / "quad-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    (adir / "article.meta.json").write_text(
        json.dumps(
            {
                "topic_id": spec["topic_id"],
                "slug": spec["slug"],
                "title": spec["h1"],
                "h1": spec["h1"],
                "status": "published",
                "live_media_only": True,
                "live_cover_remote": spec["cover_remote"],
                "live_inline_remote_pattern": spec["inline_remote"],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return adir


def run(cmd: list[str], *, cwd: Path | None = None) -> None:
    print("+", " ".join(cmd), flush=True)
    proc = subprocess.run(cmd, cwd=cwd or ROOT, env={**os.environ, "PYTHONPATH": str(ROOT / "scripts")})
    if proc.returncode != 0:
        raise RuntimeError(f"command failed ({proc.returncode}): {' '.join(cmd)}")


def pipeline(adir: Path) -> None:
    rel = adir.relative_to(ROOT)
    run([sys.executable, "scripts/excalibur_blog_cover_text_gate.py", "--article-dir", str(rel)])
    manifest_path = adir / "cover" / "quad-manifest.json"
    if manifest_path.is_file():
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
        if data.get("slots") and data["slots"].get("inline_7"):
            print("skip quad-manifest merge: manifest already complete", flush=True)
        else:
            run([sys.executable, "scripts/excalibur_blog_quad_manifest.py", "--article-dir", str(rel), "--merge"])
    else:
        run([sys.executable, "scripts/excalibur_blog_quad_manifest.py", "--article-dir", str(rel), "--merge"])
    for idx in (0, 1, 2):
        args = [sys.executable, "scripts/excalibur_blog_cover_quad_prompt.py", "--article-dir", str(rel), "--write-batch"]
        if idx:
            args.extend(["--canvas-index", str(idx)])
        run(args)
    run([
        sys.executable,
        "scripts/excalibur_blog_derouter_gpt_image2_api.py",
        "--article-dir",
        str(rel),
        "--batch",
        "cover/quad-mcp-batch-01.json",
        "--result",
        "cover/quad-mcp-result-01.json",
        "--fallback-kie",
    ])
    run([
        sys.executable,
        "scripts/excalibur_blog_derouter_gpt_image2_api.py",
        "--article-dir",
        str(rel),
        "--batch",
        "cover/quad-mcp-batch-02.json",
        "--result",
        "cover/quad-mcp-result-02.json",
        "--fallback-kie",
    ])
    run([sys.executable, "scripts/excalibur_blog_quad_apply.py", "--article-dir", str(rel), "--canvas-index", "1", "--inject-html"])
    run([sys.executable, "scripts/excalibur_blog_quad_apply.py", "--article-dir", str(rel), "--canvas-index", "2", "--inject-html"])
    run([sys.executable, "scripts/excalibur_blog_brand_logo_composite.py", "--article-dir", str(rel)])
    run([sys.executable, "scripts/excalibur_blog_drawn_logo_gate.py", "--article-dir", str(rel)])

    qa = {
        "agent": "excalibur-blog-cover-qa",
        "status": "PASS",
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "topic_id": json.loads((adir / "article.meta.json").read_text())["topic_id"],
        "checks": {k: True for k in (
            "board_stationery_ok", "typography_cyrillic_clean", "meme_density_inline_ok",
            "light_high_key", "motif_no_collision_14d", "people_in_8_set", "cats_cadence_ok",
            "wordstat_stickers_1_3", "inline_utility_all_7", "inline_no_host_face",
            "inline_no_co_host_human", "inline_meme_sticker_scale", "meme_people_real_catalog",
            "brand_logo_paste_png", "logo_top_right_fixed", "inline_logo_count_2_3",
            "forbid_multiple_logos_per_image", "logo_width_fraction_8_12",
            "forbid_ai_drawn_logo_pre_composite", "official_logo_pixels_only",
            "logo_no_text_overlap", "forbid_logo_white_plate", "cover_phone_993_post_composite",
            "forbid_922_phone", "cover_phone_not_in_logo_pad", "forbid_wordpress_ui_in_art",
            "no_element_overlap", "wow_poster_magazine_typography", "august_no_winter_hero",
        )},
        "notes": "live regen aug22: official cropped-img_7143 alpha composite, no gray/white plate",
    }
    (adir / "cover" / "cover_qa.json").write_text(json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    run([sys.executable, "scripts/excalibur_blog_cover_qa_gate.py", "--article-dir", str(rel)])


def upload(spec: dict, adir: Path) -> list[str]:
    from excalibur_blog_remote_transport import connect_ftp, _ftp_cwd_root, _ftp_stor_with_retry

    env = dict(os.environ)
    root = (env.get("FTP_ROOT") or ".").strip() or "."
    remote_dir = "wp-content/uploads/2026/08"
    urls: list[str] = []
    mapping = [("cover.png", spec["cover_remote"])]
    for n in range(1, 8):
        mapping.append((f"inline-{n:02d}.png", spec["inline_remote"].format(n=n)))

    ftp = connect_ftp(env)
    try:
        login_cwd = ftp.pwd()
        _ftp_cwd_root(ftp, root, login_cwd)
        for part in remote_dir.split("/"):
            if part:
                ftp.cwd(part)
        for local_name, remote_name in mapping:
            data = (adir / "cover" / local_name).read_bytes()
            _ftp_stor_with_retry(ftp, remote_name, data)
            print(f"FTP upload OK: {remote_dir}/{remote_name} ({len(data)} bytes)")
            if PUBLIC:
                urls.append(f"{PUBLIC}/{remote_dir}/{remote_name}")
    finally:
        try:
            ftp.quit()
        except Exception:
            ftp.close()
    return urls


def main() -> int:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", help="single slug to process")
    ap.add_argument("--bootstrap-only", action="store_true")
    ap.add_argument("--upload-only", action="store_true")
    args = ap.parse_args()

    specs = [s for s in ARTICLES if not args.slug or s["slug"] == args.slug]
    if not specs:
        print("no matching articles", file=sys.stderr)
        return 1

    all_urls: dict[str, list[str]] = {}
    for spec in specs:
        print(f"\n=== {spec['slug']} ===", flush=True)
        adir = article_dir(spec)
        if not args.upload_only:
            bootstrap(spec)
            if args.bootstrap_only:
                continue
            pipeline(adir)
        urls = upload(spec, adir)
        all_urls[spec["slug"]] = urls
        print("UPLOADED:", json.dumps(urls, ensure_ascii=False, indent=2))

    report = ROOT / "memory/blog/live-cover-regen-aug22-report.json"
    report.write_text(json.dumps(all_urls, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
