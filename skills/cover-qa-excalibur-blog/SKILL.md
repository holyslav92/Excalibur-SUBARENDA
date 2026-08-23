---
name: cover-qa-excalibur-blog
description: "Cover-QA: SHORT gate — logo official, no plate, phone, no WP UI; stamp cover_qa.json."
---

# Cover-QA — slim gate (после Cover)

## Philosophy

**Beauty = agent judgment on topic.** Do NOT block publish for typography overlap, meme density, or WOW poster pedantry.

**Brand lock (FAIL if broken):**
1. Official logo PNG pasted (not AI-drawn lockup)
2. NO white/gray plate under logo pad
3. Phone **+7 (993) 574-83-22** on cover post-composite
4. NO WordPress UI in art
5. Logo on cover + 2–3 inline (not all 8)

## Когда

**После** Cover + `excalibur_blog_brand_logo_composite.py` PASS.  
**До** Indexer/Publish.

On drawn-lockup after max-2 gen: pad-clear was applied → stamp PASS if brand lock OK. **Do not return to Cover loop.**

## Slim checks

| Check | What |
|-------|------|
| `eight_png_exist` | cover.png + inline-01…07 |
| `logo_composite_stamp_pass` | stamp PASS + canonical sha256 |
| `cover_logo_pasted` | cover has factory logo |
| `inline_logo_count_2_3` | 2–3 inline logos |
| `cover_phone_993_post_composite` | +7 (993) 574-83-22 on cover |
| `forbid_922_phone` | no realtor 922 number |
| `forbid_ai_drawn_logo_cover` | no AI lockup in cover pre-composite pad |
| `forbid_wordpress_ui_in_art` | no WP/Gutenberg/Dashboard in art |
| `no_logo_plate_cover` | no white card under logo pad on cover |
| `quad_manifest_valid` | manifest structure OK |
| `wordstat_stickers_1_3` | 1–3 Wordstat stickers |
| `motif_no_collision_14d` | no 14d motif repeat |
| `light_high_key` | agent: scene is bright (honor) |

**Dropped** (no longer gate): `official_logo_pixels_only`, `logo_no_text_overlap`, `forbid_logo_white_plate` heuristics, `no_element_overlap`, `wow_poster_magazine_typography`, `inline_utility_all_7`, `august_no_winter_hero`, cats cadence, board stationery.

## Выход: `cover/cover_qa.json`

```json
{
  "agent": "excalibur-blog-cover-qa",
  "status": "PASS",
  "checked_at": "2026-08-23",
  "topic_id": "B01",
  "checks": {
    "eight_png_exist": true,
    "logo_composite_stamp_pass": true,
    "cover_logo_pasted": true,
    "inline_logo_count_2_3": true,
    "cover_phone_993_post_composite": true,
    "forbid_922_phone": true,
    "forbid_ai_drawn_logo_cover": true,
    "forbid_wordpress_ui_in_art": true,
    "no_logo_plate_cover": true,
    "quad_manifest_valid": true,
    "wordstat_stickers_1_3": true,
    "motif_no_collision_14d": true,
    "light_high_key": true
  },
  "notes": "slim gate: brand lock OK"
}
```

## Gate (shell)

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ARTICLE"
```

Только `OK cover QA stamp` → Indexer.

Agent: `agents/excalibur-blog-cover-qa.md`
