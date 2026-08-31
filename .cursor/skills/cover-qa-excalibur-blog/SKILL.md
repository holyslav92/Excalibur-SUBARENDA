---
name: cover-qa-excalibur-blog
description: "Cover-QA: scene_poster_v2 — no meme/collage on cover, logo+phone in-scene, stamp cover_qa.json."
---

# Cover-QA — scene_poster_v2 slim gate

## FAIL if broken

| Check | What |
|-------|------|
| `forbid_split_white_collage` | no split white-panel + photo cover |
| `forbid_cover_meme_collage` | no meme/sticker cutout on cover |
| `cover_logo_pasted` | factory logo on cover |
| `inline_logo_count_2_3` | 2–3 inline logos |
| `cover_phone_993_in_scene` | phone in artwork, not pill |
| `forbid_phone_pill_post_composite` | no opaque phone button |
| `no_logo_plate_cover` | no plate under logo |
| `forbid_ai_drawn_logo_cover` | no AI lockup |
| `max_one_cat_meme_slot` | ≤1 cat on **inlines only** (NOT cover) |

```bash
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```
