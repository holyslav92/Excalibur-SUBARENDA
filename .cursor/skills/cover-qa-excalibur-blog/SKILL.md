---
name: cover-qa-excalibur-blog
description: "Cover-QA: slim gate — logo overlay, phone in-scene, no plate/pill, no WP UI; stamp cover_qa.json."
---

# Cover-QA — slim gate (после Cover)

## Philosophy

**Beauty = agent judgment on topic.** Do NOT block publish for typography pedantry.

**Brand lock FOREVER (FAIL if broken):**
1. Official logo PNG pasted AFTER gen (not AI-drawn lockup, never Grsai reference)
2. NO white/gray/beige plate under logo pad
3. Phone **+7 (993) 574-83-22** painted **IN the scene** (tape/paper/magnet) — NOT post-composite pill
4. NO logo/phone over cat/meme/sticky/headline
5. NO WordPress UI in art
6. Logo on cover + 2–3 inline (not all 8)

## Когда

**После** Cover + `excalibur_blog_brand_logo_composite.py` PASS.  
**До** Indexer/Publish.

On drawn-lockup after max-2 gen: pad-clear → official paste → stamp PASS if brand lock OK.

## Slim checks

| Check | What |
|-------|------|
| `eight_png_exist` | cover.png + inline-01…07 |
| `logo_composite_stamp_pass` | stamp PASS + canonical sha256 |
| `cover_logo_pasted` | cover has factory logo |
| `inline_logo_count_2_3` | 2–3 inline logos |
| `cover_phone_993_in_scene` | +7 (993) 574-83-22 in artwork, not pill |
| `forbid_phone_pill_post_composite` | no opaque white/gray phone button overlay |
| `forbid_922_phone` | no realtor 922 number |
| `forbid_ai_drawn_logo_cover` | no AI lockup in cover pre-composite pad |
| `forbid_wordpress_ui_in_art` | no WP/Gutenberg/Dashboard in art |
| `no_logo_plate_cover` | no white/gray card under logo pad on cover |
| `forbid_logo_overlaps_meme_cat_headline` | logo not over cat zone or headline band |
| `quad_manifest_valid` | manifest structure OK |
| `wordstat_stickers_1_3` | 1–3 Wordstat stickers |
| `motif_no_collision_14d` | no 14d motif repeat |
| `light_high_key` | agent: scene is bright (honor) |

Python gates (automatic): `validate_article_logo_gates_slim` + `validate_cover_phone_and_overlap_gates`.

## Выход: `cover/cover_qa.json`

```json
{
  "agent": "excalibur-blog-cover-qa",
  "status": "PASS",
  "checked_at": "2026-08-25",
  "topic_id": "B01",
  "checks": {
    "eight_png_exist": true,
    "logo_composite_stamp_pass": true,
    "cover_logo_pasted": true,
    "inline_logo_count_2_3": true,
    "cover_phone_993_in_scene": true,
    "forbid_phone_pill_post_composite": true,
    "forbid_922_phone": true,
    "forbid_ai_drawn_logo_cover": true,
    "forbid_wordpress_ui_in_art": true,
    "no_logo_plate_cover": true,
    "forbid_logo_overlaps_meme_cat_headline": true,
    "quad_manifest_valid": true,
    "wordstat_stickers_1_3": true,
    "motif_no_collision_14d": true,
    "light_high_key": true
  },
  "notes": "slim gate: logo overlay + phone in-scene OK"
}
```

## Gate (shell)

```bash
ARTICLE="memory/blog/articles/<topic_id>-<slug>"
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir "$ARTICLE"
```

Только `OK cover QA stamp` → Indexer.

Agent: `agents/excalibur-blog-cover-qa.md`
