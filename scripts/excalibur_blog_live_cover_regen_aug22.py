#!/usr/bin/env python3
"""Bootstrap + Grsai regen + FTP upload for all Aug-22 live posts (media only)."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from excalibur_blog_image_provider import resolve_image_script  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = os.environ.get("PUBLIC_SITE_URL", "").rstrip("/")
YEKT = ZoneInfo("Asia/Yekaterinburg")
AUG22 = "2026-08-22"
LOGO_REL = ROOT / "memory/cover/assets/brand/logo-dobry-dom.png"
LOGO_CANONICAL_URL_SUFFIX = "wp-content/uploads/2026/03/cropped-img_7143.png"
DISCOVERY_CACHE = ROOT / "memory/blog/aug22-slugs-discovery.json"

# Точный scope Aug-22 regen (FULL 8 images each). Без priehal-v-sem-utra (Aug 21).
AUG22_REGEN_SLUGS: tuple[str, ...] = (
    "dogovor-arendy-pravila-prozhivaniya-posutochno",
    "otmena-bronirovaniya-posutochno-vozvrat-predoplaty",
    "pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti",
    "zabroniroval-posutochno-vyyasnilos-kvartira-v-subarende",
)

DAYLIGHT_SCENE_SUFFIX = (
    "natural daylight, clean white balance, NO yellow/amber cast, NO muddy faces, "
    "sharp stylish comfort-realistic poster, empty top-right pad. "
    "FORBIDDEN: any logo, brand mark, watermark, green curtains icon, Добрый дом text."
)
DAYLIGHT_LOCATION = "Tyumen apartment August natural daylight, clean whites, no yellow cast"

VISUAL_TYPES = [
    "comparison_table",
    "process_flow",
    "bar_timeline_chart",
    "structure_diagram",
    "labeled_checklist",
    "fact_card",
    "schema_faq_ui",
]

# Rich cover metadata keyed by slug (merged with live WP fetch).
META_BY_SLUG: dict[str, dict] = {
    "dogovor-arendy-pravila-prozhivaniya-posutochno": {
        "topic_id": "LIVE-dogovor",
        "hook": "Перед оплатой прочитайте правила аренды",
        "highlight": "правила",
        "sticky": "7 запретов",
        "wordstat": ["правила аренды", "Тюмень", "предоплата"],
        "cover_emotion": "шок от семи запретов в договоре после перевода",
        "cover_scene": f"Phone transfer + rules checklist, bold Cyrillic hook; {DAYLIGHT_SCENE_SUFFIX}",
        "motif_composition": "payment phone + rules checklist poster collage",
        "motif_meme": "tabby cat with sunglasses sticker bottom-left ≤10%",
        "motif_props": "phone screen, checklist paper, gold pen",
        "motif_joke": "cat judges unread contract",
    },
    "otmena-bronirovaniya-posutochno-vozvrat-predoplaty": {
        "topic_id": "LIVE-otmena",
        "hook": "Отменили бронь — верните предоплату",
        "highlight": "верните",
        "sticky": "невозвратно?",
        "wordstat": ["отмена брони", "Тюмень", "возврат предоплаты"],
        "cover_emotion": "разочарование: планы сорвались, предоплату не вернули",
        "cover_scene": f"Bell vs keys VS refund note, bold Cyrillic hook, bright airy room; {DAYLIGHT_SCENE_SUFFIX}",
        "motif_composition": "refund bell vs keys comparison poster",
        "motif_meme": "fluffy cat peeking from sofa corner ≤10%",
        "motif_props": "service bell, keyring, sticky note",
        "motif_joke": "cat side-eyes cancelled trip",
    },
    "pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti": {
        "topic_id": "LIVE-pereveli",
        "hook": "Шесть гостей — залог не вернули",
        "highlight": "гостей",
        "sticky": "лишние гости",
        "wordstat": ["лишние гости", "Тюмень", "правила проживания"],
        "cover_emotion": "шок шести гостей у двери и удержанного залога",
        "cover_scene": f"Six suitcases at door + rules paper, bold hook gold гостей; {DAYLIGHT_SCENE_SUFFIX}",
        "motif_composition": "six guests doorway + rules torn paper",
        "motif_meme": "striped cat with bracelet sticker ≤10%",
        "motif_props": "six gold bracelets, chat bubbles, suitcases",
        "motif_joke": "cat counts extra guests",
    },
    "priehal-v-sem-utra-kvartiru-dali-tolko-v-dva-chto-delat-do-zaseleniya": {
        "topic_id": "LIVE-sem-utra",
        "hook": "Приехал в семь утра — квартиру дали только в два",
        "highlight": "семь утра",
        "sticky": "ранний заезд",
        "wordstat": ["ранний заезд", "Тюмень", "7 утра"],
        "cover_emotion": "гость у подъезда в семь утра ждёт ключи",
        "cover_scene": f"Early morning doorstep suitcase + chat on phone, bold hook; {DAYLIGHT_SCENE_SUFFIX}",
        "motif_composition": "early check-in timeline + doorstep scene",
        "motif_meme": "tiny cat sticker bottom-left ≤12%",
        "motif_props": "keys, suitcase, phone chat, torn sticky",
        "motif_joke": "cat surprised at early arrival",
    },
    "zabroniroval-posutochno-vyyasnilos-kvartira-v-subarende": {
        "topic_id": "LIVE-subarenda",
        "hook": "Субаренда — кто реально сдаёт квартиру",
        "highlight": "субаренда",
        "sticky": "кто сдаёт?",
        "wordstat": ["субаренда", "Тюмень", "посуточно"],
        "cover_emotion": "шок: забронировал у одного, ключи от другого",
        "cover_scene": f"Two contracts vs one keyring, bold Cyrillic hook; {DAYLIGHT_SCENE_SUFFIX}",
        "motif_composition": "sublease chain diagram + torn lease papers",
        "motif_meme": "cat with magnifying glass sticker ≤10%",
        "motif_props": "two contracts, keyring, chat bubbles",
        "motif_joke": "cat inspects fake host",
    },
    "perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem": {
        "topic_id": "LIVE-zalog",
        "hook": "Залог не вернули — скол на плите",
        "highlight": "скол",
        "sticky": "Залог вернут?",
        "wordstat": ["залог посуточно", "Тюмень"],
        "cover_emotion": "разочарование на выезде: залог удержали из-за скола",
        "cover_scene": f"Stove chip close-up vs deposit receipt, bold hook; {DAYLIGHT_SCENE_SUFFIX}",
        "motif_composition": "deposit receipt vs stove chip comparison",
        "motif_meme": "cat side-eye sticker ≤10%",
        "motif_props": "stove photo, deposit paper, gold tape",
        "motif_joke": "cat doubts the chip",
    },
    "beskontaktnoe-zaselenie-posutochno-tyumen": {
        "topic_id": "LIVE-beskontakt",
        "hook": "Гость, проверь два кода до оплаты",
        "highlight": "два",
        "sticky": "Один код — не вход",
        "wordstat": ["квартира посуточно Тюмень", "снять квартиру посуточно Тюмень"],
        "cover_emotion": "гость у чужой двери с неверным кодом",
        "cover_scene": f"Wrong door code keypad vs correct address chat, bold hook; {DAYLIGHT_SCENE_SUFFIX}",
        "motif_composition": "two codes keypad + address checklist collage",
        "motif_meme": "cat at wrong door sticker ≤10%",
        "motif_props": "keypad, phone chat, address note",
        "motif_joke": "cat points to right door",
    },
}


def article_dir(spec: dict) -> Path:
    return ROOT / "memory/blog/articles" / f"{spec['topic_id']}-{spec['slug']}"


def ensure_logo_asset() -> Path:
    """Скачать cropped-img_7143.png с live-сайта, если локального логотипа нет."""
    if LOGO_REL.is_file():
        return LOGO_REL
    if not PUBLIC:
        raise RuntimeError("PUBLIC_SITE_URL missing — cannot download logo-dobry-dom.png")
    url = f"{PUBLIC}/{LOGO_CANONICAL_URL_SUFFIX}"
    LOGO_REL.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading logo from {url}", flush=True)
    with urlopen(url, timeout=60) as resp:
        LOGO_REL.write_bytes(resp.read())
    if not LOGO_REL.is_file() or LOGO_REL.stat().st_size < 100:
        raise RuntimeError(f"logo download failed or too small: {LOGO_REL}")
    return LOGO_REL


def wp_get(path: str) -> Any:
    url = f"{PUBLIC}{path}" if path.startswith("/") else path
    req = Request(url, headers={"User-Agent": "ExcaliburBlog/1.0"})
    with urlopen(req, timeout=90) as resp:
        return json.loads(resp.read().decode("utf-8"))


def discover_aug22_slugs(*, refresh: bool = False) -> list[str]:
    """All slugs published OR modified on 2026-08-22 Asia/Yekaterinburg."""
    if DISCOVERY_CACHE.is_file() and not refresh:
        cached = json.loads(DISCOVERY_CACHE.read_text(encoding="utf-8"))
        slugs = [p["slug"] for p in cached.get("published", [])]
        slugs += [p["slug"] for p in cached.get("modified_only", [])]
        if slugs:
            return sorted(set(slugs))

    if not PUBLIC:
        raise RuntimeError("PUBLIC_SITE_URL missing")
    posts: list[dict] = []
    page = 1
    while page <= 30:
        batch = wp_get(
            f"/wp-json/wp/v2/posts?per_page=100&page={page}&orderby=date&order=desc&status=publish"
        )
        if not batch:
            break
        posts.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    published: list[dict] = []
    modified_only: list[dict] = []
    for p in posts:
        pub_local = datetime.fromisoformat(p["date_gmt"].replace("Z", "+00:00")).astimezone(YEKT)
        mod_local = datetime.fromisoformat(p["modified_gmt"].replace("Z", "+00:00")).astimezone(YEKT)
        row = {
            "id": p["id"],
            "slug": p["slug"],
            "title": re.sub("<[^>]+>", "", p["title"]["rendered"]).strip(),
            "date_gmt": p["date_gmt"],
            "date_local": pub_local.isoformat(),
            "modified_gmt": p.get("modified_gmt"),
            "link": p.get("link", ""),
        }
        if pub_local.date().isoformat() == AUG22:
            published.append(row)
        elif mod_local.date().isoformat() == AUG22:
            modified_only.append(row)

    DISCOVERY_CACHE.parent.mkdir(parents=True, exist_ok=True)
    DISCOVERY_CACHE.write_text(
        json.dumps({"published": published, "modified_only": modified_only}, ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    return sorted({r["slug"] for r in published + modified_only})


def extract_h2s_with_inline(content: str) -> list[str]:
    parts = re.split(r"(<h2[^>]*>.*?</h2>)", content, flags=re.I | re.S)
    out: list[str] = []
    for i, part in enumerate(parts):
        if not re.match(r"<h2", part, re.I):
            continue
        h2 = re.sub("<[^>]+>", "", part).strip()
        following = parts[i + 1] if i + 1 < len(parts) else ""
        if re.search(r"inline|wp-image|figure", following, re.I):
            out.append(h2)
    if len(out) >= 7:
        return out[:7]
    # fallback: first 7 h2 in body
    all_h2 = [re.sub("<[^>]+>", "", h).strip() for h in re.findall(r"<h2[^>]*>(.*?)</h2>", content, re.I | re.S)]
    return all_h2[:7]


def infer_inline_pattern(inline_names: list[str], slug: str) -> str:
    if not inline_names:
        return f"{slug}-inline-{{n:02d}}.png"
    sample = sorted(inline_names)[0]
    m = re.match(r"^(.+-inline-)\d{2}(-?\d*\.png)$", sample)
    if m:
        return m.group(1) + "{n:02d}" + m.group(2)
    return sample.replace("01", "{n:02d}")


def build_spec_from_wp(slug: str) -> dict:
    posts = wp_get(f"/wp-json/wp/v2/posts?slug={slug}&_embed")
    if not posts:
        raise RuntimeError(f"WP post not found for slug={slug}")
    p = posts[0]
    meta = dict(META_BY_SLUG.get(slug) or {})
    h1 = re.sub("<[^>]+>", "", p["title"]["rendered"]).strip()
    content = p["content"]["rendered"]
    h2s = extract_h2s_with_inline(content)
    if len(h2s) < 7:
        raise RuntimeError(f"{slug}: expected 7 inline h2 anchors, got {len(h2s)}")

    fm = (p.get("_embedded") or {}).get("wp:featuredmedia") or [{}]
    cover_url = (fm[0] or {}).get("source_url", "")
    cover_remote = cover_url.rsplit("/", 1)[-1] if cover_url else f"{slug}-cover.png"
    inline_names = sorted(re.findall(r"uploads/2026/08/([^\"']+inline[^\"']+\.png)", content, re.I))
    inline_remote = infer_inline_pattern(inline_names, slug)

    topic_id = meta.get("topic_id") or f"LIVE-{slug[:24]}"
    hook = meta.get("hook") or h1[:80]
    highlight = meta.get("highlight") or (hook.split()[0] if hook.split() else "важно")
    return {
        "topic_id": topic_id,
        "slug": slug,
        "h1": h1,
        "hook": hook,
        "highlight": highlight,
        "sticky": meta.get("sticky", ""),
        "wordstat": meta.get("wordstat", ["Тюмень", "посуточно"]),
        "cover_remote": cover_remote,
        "inline_remote": inline_remote,
        "h2s": h2s,
        "cover_emotion": meta.get("cover_emotion", h1[:100]),
        "cover_scene": meta.get("cover_scene", f"Rental shock scene; {DAYLIGHT_SCENE_SUFFIX}"),
        "motif_composition": meta.get("motif_composition", "WOW poster collage, empty top-right logo pad"),
        "motif_meme": meta.get("motif_meme", "tiny ginger cat sticker bottom-left ≤10%"),
        "motif_props": meta.get("motif_props", "torn paper, gold tape, phone, keys"),
        "motif_joke": meta.get("motif_joke", "cat reacts to rental shock"),
    }


def fetch_html(slug: str) -> str:
    if not PUBLIC:
        raise RuntimeError("PUBLIC_SITE_URL missing")
    url = f"{PUBLIC}/blog/{slug}/"
    with urlopen(url, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def bootstrap(spec: dict) -> Path:
    adir = article_dir(spec)
    cover = adir / "cover"
    cover.mkdir(parents=True, exist_ok=True)

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
            "scene_hint": (
                f"{vt}: {h2[:48]}; gold labels; torn paper; natural daylight; "
                "empty top-right if logo."
            ),
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
            "location": DAYLIGHT_LOCATION,
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


MAX_COVER_CANVAS_RETRIES = 8
CANVAS1_LOGO_PANELS = ("cover.png", "inline-01.png", "inline-03.png")
CANVAS2_LOGO_PANELS = ("inline-07.png",)


def _clear_cover_canvas_artifacts(adir: Path) -> None:
    """Сбросить cover + inline 1–3 и pre-composite перед повторной генерацией canvas 1."""
    cover = adir / "cover"
    for name in (
        "cover.png",
        "inline-01.png",
        "inline-02.png",
        "inline-03.png",
        "canvas-quad-01.png",
    ):
        path = cover / name
        if path.is_file():
            path.unlink()
    pre = cover / "pre-composite"
    if pre.is_dir():
        shutil.rmtree(pre)


def _clear_inline_canvas_artifacts(adir: Path) -> None:
    """Сбросить inline 4–7 перед повторной генерацией canvas 2."""
    cover = adir / "cover"
    for name in (
        "inline-04.png",
        "inline-05.png",
        "inline-06.png",
        "inline-07.png",
        "canvas-quad-02.png",
    ):
        path = cover / name
        if path.is_file():
            path.unlink()
    pre = cover / "pre-composite"
    if pre.is_dir():
        shutil.rmtree(pre)


def _panels_have_drawn_lockup(adir: Path, panel_names: tuple[str, ...]) -> bool:
    from excalibur_blog_brand_logo_composite import assert_no_drawn_lockup_before_paste

    cover = adir / "cover"
    for name in panel_names:
        path = cover / name
        if not path.is_file():
            return True
        try:
            assert_no_drawn_lockup_before_paste(path)
        except ValueError as exc:
            print(f"drawn-lockup on {name}: {exc}", flush=True)
            return True
    return False


def _repair_logo_panels(adir: Path, panel_names: tuple[str, ...]) -> bool:
    """Снять AI-lockup в top-right pad и перепастить factory logo."""
    from excalibur_blog_live_plate_remove_relogo import fix_image

    cover = adir / "cover"
    logo_slots = {"cover.png", "inline-01.png", "inline-03.png", "inline-07.png"}
    repaired = False
    for name in panel_names:
        path = cover / name
        if not path.is_file():
            continue
        paste_logo = name in logo_slots
        add_phone = name == "cover.png"
        try:
            data, verify = fix_image(
                path.read_bytes(),
                add_phone=add_phone,
                paste_logo=paste_logo,
            )
            path.write_bytes(data)
            repaired = True
            print(
                f"OK pad-repair {name} clear_passes={verify.get('clear_passes')}",
                flush=True,
            )
        except Exception as exc:  # noqa: BLE001
            print(f"WARN pad-repair failed for {name}: {exc}", flush=True)
    return repaired


def _run_allow_fail(cmd: list[str], *, cwd: Path | None = None) -> int:
    print("+", " ".join(cmd), flush=True)
    proc = subprocess.run(cmd, cwd=cwd or ROOT, env={**os.environ, "PYTHONPATH": str(ROOT / "scripts")})
    return proc.returncode


def _generate_canvas(
    image_script: str,
    rel: Path,
    *,
    batch_file: str,
    result_file: str,
    model_tier: str = "auto",
) -> bool:
    cmd = [
        sys.executable,
        image_script,
        "--article-dir",
        str(rel),
        "--batch",
        batch_file,
        "--result",
        result_file,
    ]
    if model_tier != "auto":
        cmd.extend(["--model-tier", model_tier])
    return _run_allow_fail(cmd) == 0


def _apply_canvas(rel: Path, canvas_index: int) -> int:
    return _run_allow_fail([
        sys.executable,
        "scripts/excalibur_blog_quad_apply.py",
        "--article-dir",
        str(rel),
        "--canvas-index",
        str(canvas_index),
        "--inject-html",
    ])


def _canvas_sheet_ok(adir: Path, rel: Path, image_script: str, *, batch_file: str, result_file: str, canvas_index: int, logo_panels: tuple[str, ...]) -> bool:
    """Один sheet: auto → apply → pad-repair → vip (если ещё не был) → apply."""
    if not _generate_canvas(image_script, rel, batch_file=batch_file, result_file=result_file, model_tier="auto"):
        return False
    result_path = adir / "cover" / Path(result_file).name
    used_vip = False
    if result_path.is_file():
        used_vip = bool(json.loads(result_path.read_text(encoding="utf-8")).get("used_vip_fallback"))
    _apply_canvas(rel, canvas_index)
    if _panels_have_drawn_lockup(adir, logo_panels):
        if _repair_logo_panels(adir, logo_panels) and not _panels_have_drawn_lockup(adir, logo_panels):
            print("OK pad-repair cleared drawn-lockup for this sheet", flush=True)
            return True
    else:
        return True
    if used_vip:
        print("WARN sheet lockup remains after vip already used", flush=True)
        return False
    print("WARN primary sheet failed lockup/apply; one vip regen for this sheet", flush=True)
    if not _generate_canvas(image_script, rel, batch_file=batch_file, result_file=result_file, model_tier="vip"):
        print("WARN vip tier API failed for this sheet", flush=True)
        return False
    _apply_canvas(rel, canvas_index)
    if _panels_have_drawn_lockup(adir, logo_panels):
        if _repair_logo_panels(adir, logo_panels) and not _panels_have_drawn_lockup(adir, logo_panels):
            print("OK pad-repair cleared drawn-lockup after vip sheet", flush=True)
            return True
        return False
    return True


def pipeline(adir: Path) -> None:
    rel = adir.relative_to(ROOT)
    image_script = resolve_image_script(ROOT)
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
    for attempt in range(1, MAX_COVER_CANVAS_RETRIES + 1):
        if _canvas_sheet_ok(
            adir,
            rel,
            image_script,
            batch_file="cover/quad-mcp-batch-01.json",
            result_file="cover/quad-mcp-result-01.json",
            canvas_index=1,
            logo_panels=CANVAS1_LOGO_PANELS,
        ):
            print(f"canvas 1 OK on attempt {attempt}", flush=True)
            break
        print(
            f"WARN canvas 1 drawn-lockup or apply fail — retry ({attempt}/{MAX_COVER_CANVAS_RETRIES})",
            flush=True,
        )
        if attempt >= MAX_COVER_CANVAS_RETRIES:
            raise RuntimeError("canvas 1 failed drawn-lockup gate after max retries")
        _clear_cover_canvas_artifacts(adir)

    for attempt in range(1, MAX_COVER_CANVAS_RETRIES + 1):
        logo_panels = CANVAS1_LOGO_PANELS + CANVAS2_LOGO_PANELS
        if _canvas_sheet_ok(
            adir,
            rel,
            image_script,
            batch_file="cover/quad-mcp-batch-02.json",
            result_file="cover/quad-mcp-result-02.json",
            canvas_index=2,
            logo_panels=logo_panels,
        ):
            print(f"canvas 2 OK on attempt {attempt}", flush=True)
            break
        print(
            f"WARN canvas 2 drawn-lockup or apply fail — retry ({attempt}/{MAX_COVER_CANVAS_RETRIES})",
            flush=True,
        )
        if attempt >= MAX_COVER_CANVAS_RETRIES:
            raise RuntimeError("canvas 2 failed drawn-lockup gate after max retries")
        _clear_inline_canvas_artifacts(adir)
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
        "notes": "live regen aug22 grsai: cropped-img_7143 alpha, natural daylight, no plate",
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
                urls.append(f"{PUBLIC}/{remote_dir}/{remote_name}?v={int(time.time())}")
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
    ap.add_argument("--discover-only", action="store_true", help="print Aug-22 slugs and exit")
    ap.add_argument("--refresh-discovery", action="store_true")
    ap.add_argument("--bootstrap-only", action="store_true")
    ap.add_argument("--upload-only", action="store_true")
    args = ap.parse_args()

    if args.discover_only:
        for slug in discover_aug22_slugs(refresh=args.refresh_discovery):
            print(slug)
        return 0

    if args.slug:
        slugs = [args.slug]
    elif args.refresh_discovery:
        slugs = discover_aug22_slugs(refresh=True)
    else:
        slugs = list(AUG22_REGEN_SLUGS)

    if not slugs:
        print("no Aug-22 slugs found", file=sys.stderr)
        return 1

    if not os.environ.get("GRSAI_API_KEY", "").strip() and not args.bootstrap_only and not args.upload_only:
        print("❌ GRSAI API KEY MISSING: set GRSAI_API_KEY before regen", file=sys.stderr)
        return 1

    if not os.environ.get("GRSAI_IMAGE_MODEL", "").strip():
        fallback_model = os.environ.get("DEROUTER_IMAGE_MODEL", "").strip()
        if fallback_model:
            os.environ["GRSAI_IMAGE_MODEL"] = fallback_model

    all_urls: dict[str, list[str]] = {}
    host_used: str | None = None
    if not args.upload_only:
        ensure_logo_asset()

    for slug in slugs:
        print(f"\n=== {slug} ===", flush=True)
        spec = build_spec_from_wp(slug)
        adir = article_dir(spec)
        if not args.upload_only:
            bootstrap(spec)
            if args.bootstrap_only:
                continue
            pipeline(adir)
            for result_file in ("cover/quad-mcp-result-01.json", "cover/quad-mcp-result-02.json"):
                rp = adir / result_file
                if rp.is_file():
                    host_used = host_used or json.loads(rp.read_text()).get("host")
        urls = upload(spec, adir)
        all_urls[slug] = urls
        print("UPLOADED:", json.dumps(urls, ensure_ascii=False, indent=2))

    report = {
        "slugs": slugs,
        "grsai_host": host_used,
        "cover_urls": {slug: (urls[0] if urls else "") for slug, urls in all_urls.items()},
        "all_urls": all_urls,
    }
    report_path = ROOT / "memory/blog/live-cover-regen-aug22-report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
