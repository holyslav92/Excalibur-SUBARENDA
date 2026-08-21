---
name: cover-qa-excalibur-blog
description: "Cover-QA: visual gate after Cover, before Indexer/Publish; stamp cover_qa.json."
---

# Cover-QA — visual gate (после Cover)

## Когда

**После** `excalibur-blog-cover` (8 PNG готовы + `excalibur_blog_brand_logo_composite.py` PASS).  
**До** Indexer и Publish.

FAIL → **вернуть Cover** (не Indexer/Publish).

## WOW cover rules (Добрый дом — FAIL if broken)

Канон: `memory/cover/visual-notes-dobry-dom.json` · `shared/tenant-config.json` → `cover_wow_rules`

1. **forbid_wordpress_ui_in_art** — нет WordPress/Gutenberg/Add title/Publish/Dashboard/wp-admin/block editor/theme chrome/cookie bars в арте.
2. **no_element_overlap** — headline, stickers, meme, cat, phone, people, logo pad не перекрываются.
3. **wow_poster_magazine_typography** — magazine poster, bold readable Russian display hook, scene + one sharp line; не timid system font / label wall / empty stock / WP screenshot.
4. **inline_logo_count_2_3** + **forbid_multiple_logos_per_image** + **logo_top_right_fixed** — логотип на cover + 2–3 inline (default inline_1/3/7), TOP-RIGHT pad; never 2+ logos per frame.
5. **forbid_ai_drawn_logo_pre_composite** — pre-composite panels MUST NOT contain AI-drawn lockup (curtains+flower, dashed frame, wordmark).
6. **official_logo_pixels_only** — post-composite logo region MUST match official `logo-dobry-dom.png` pixels.
7. **logo_no_text_overlap** — factory logo MUST NOT overlap readable text.
8. **cover_phone_993_post_composite** + **cover_phone_not_in_logo_pad** — +7 (993) 574-83-22 только на cover post-composite, не в logo pad.

## Что проверяешь (визуально + артефакты)

1. **Light / high-key** — светлая картинка, sun flare/glow; **нет** dark cinematic / low-key / twilight.
2. **Motif 14д** — нет коллизии с `memory/cover/used-motifs.json`.
3. **Люди в 8-set** — гости по теме OK; inline people-memes только маленькие стикеры из `meme-top100.json`.
4. **Коты** — meme-cat на cover bottom-left ≤12% **или** недельная каденция не просела.
5. **Wordstat stickers** — 1–3 читаемых стикера с live P0-фразами.
6. **Inline utility (все 7)** — факт/порядок/число/сравнение по H2; не host face.
7. **Brand logo composite** — `cover/logo-composite-stamp.json` PASS; canonical PNG sha256; logo 8–12% TOP-RIGHT.

Канон: `memory/cover/cover-canon.json`.

## Выход: `cover/cover_qa.json`

```json
{
  "agent": "excalibur-blog-cover-qa",
  "status": "PASS",
  "checked_at": "2026-08-18",
  "topic_id": "B01",
  "checks": {
    "light_high_key": true,
    "motif_no_collision_14d": true,
    "people_in_8_set": true,
    "cats_cadence_ok": true,
    "wordstat_stickers_1_3": true,
    "inline_utility_all_7": true,
    "inline_no_host_face": true,
    "inline_no_co_host_human": true,
    "inline_meme_sticker_scale": true,
    "meme_people_real_catalog": true,
    "brand_logo_paste_png": true,
    "logo_top_right_fixed": true,
    "inline_logo_count_2_3": true,
    "forbid_multiple_logos_per_image": true,
    "logo_width_fraction_8_12": true,
    "forbid_ai_drawn_logo_pre_composite": true,
    "official_logo_pixels_only": true,
    "logo_no_text_overlap": true,
    "cover_phone_993_post_composite": true,
    "forbid_922_phone": true,
    "cover_phone_not_in_logo_pad": true,
    "forbid_wordpress_ui_in_art": true,
    "no_element_overlap": true,
    "wow_poster_magazine_typography": true
  },
  "notes": "кратко: что смотрел"
}
```

При FAIL — `status: FAIL`, перечисли checks=false и **не** пускай дальше.

## Gate (shell)

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ARTICLE"
```

Только `OK cover QA stamp` → Indexer.

## Blockers

- COVER QA BLOCKER — любой check false (включая WOW rules)
- logo-composite-stamp missing / sha256 mismatch
- dark cinematic / overlapping elements / WordPress UI in art → return Cover

Agent: `agents/excalibur-blog-cover-qa.md`
