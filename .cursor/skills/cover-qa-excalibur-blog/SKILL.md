---
name: cover-qa-excalibur-blog
description: "Cover-QA: scene_poster_v2 — no meme/collage on cover, logo+phone in-scene, stamp cover_qa.json."
---

# Cover-QA — scene_poster_v2 slim gate (COVER only)

## FAIL if broken on `cover.png`

| Check | What |
|-------|------|
| `forbid_split_white_collage` | no split white-panel + photo cover |
| `forbid_cover_meme_collage` | no meme/sticker cutout bottom-left on cover |
| `forbid_empty_stock_cover` | no timid empty stock room |
| `forbid_sticky_soup_cover` | no yellow sticky / torn-paper collage soup |
| `forbid_phone_pill_cover` | no opaque phone pill/button |
| `forbid_logo_plaque_cover` | no white/gray plaque under logo pad |
| `forbid_house_heart_lockup` | no model-drawn house-with-heart lockup |
| `cover_logo_pasted` | factory logo on cover |
| `inline_logo_count_2_3` | 2–3 inline logos (inlines unchanged) |
| `cover_phone_993_in_scene` | phone in artwork, not pill |
| `forbid_phone_pill_post_composite` | no opaque phone button |
| `no_logo_plate_cover` | no plate under logo |
| `forbid_ai_drawn_logo_cover` | no AI lockup |
| `max_one_cat_meme_slot` | ≤1 cat on **inlines only** (NOT cover) |

Inlines: existing inline gates only — do **not** fail timid type / off-theme meme on inline panels.

```bash
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

Python collage gates: `scripts/excalibur_blog_cover_collage_gate.py` → `validate_cover_scene_poster_gates(cover.png)`.
