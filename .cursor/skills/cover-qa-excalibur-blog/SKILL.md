---
name: cover-qa-excalibur-blog
description: "Cover-QA: type_meme_sticker_v3 — require meme+headline+large phone sticker on cover, stamp cover_qa.json."
---

# Cover-QA — type_meme_sticker_v3 slim gate (COVER only)

## FAIL if broken on `cover.png`

| Check | What |
|-------|------|
| `require_display_headline` | spectacular Cyrillic display headline typography hero |
| `require_cover_meme_sticker` | exactly ONE catalog meme sticker from meme-top100.json |
| `require_large_phone_sticker` | LARGE die-cut phone sticker +7 (993) 574-83-22 |
| `forbid_people_heavy_cover` | no people-heavy group scene photo |
| `forbid_split_white_collage` | no split white-panel + photo cover |
| `forbid_empty_stock_cover` | no timid empty stock room (without headline) |
| `forbid_sticky_soup_cover` | no yellow sticky / torn-paper collage soup |
| `forbid_phone_pill_cover` | no opaque phone pill/button |
| `forbid_logo_plaque_cover` | no white/gray plaque under logo pad |
| `forbid_house_heart_lockup` | no model-drawn house-with-heart lockup |
| `cover_logo_pasted` | factory logo on cover |
| `inline_no_logo_on_inlines` | ZERO company logos on all 7 inline frames (cover only) |
| `cover_phone_993_large_sticker` | large phone sticker in artwork, not pill |
| `forbid_phone_pill_post_composite` | no opaque phone button/chip |
| `no_logo_plate_cover` | no plate under logo |
| `forbid_ai_drawn_logo_cover` | no AI lockup |
| `max_one_cat_meme_slot` | ≤1 cat across cover+inlines |

Inlines: existing inline gates only — do **not** fail for having a meme on inline panels.

```bash
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

Python collage gates: `scripts/excalibur_blog_cover_collage_gate.py` → `validate_cover_type_meme_sticker_gates(cover.png)`.
