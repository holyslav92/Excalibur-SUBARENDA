---
name: cover-qa-excalibur-blog
description: "Cover-QA: scene_composite_v1 — anti-collage gates + poster composite stamp, stamp cover_qa.json."
---

# Cover-QA — scene_composite_v1 slim gate (COVER only)

## HARD anti-collage FAIL on `cover.png`

| Check | What |
|-------|------|
| `forbid_overlapping_text_blocks` | no 2+ stacked/overlapping model type layers |
| `forbid_giant_cropped_glyph` | no magnified letter crop >12% canvas |
| `forbid_model_drawn_meme_template` | no Trade Offer / Drake / Wojak drawn by model |
| `poster_composite_stamp_pass` | `cover/poster-composite-stamp.json` PASS from factory composite |
| `require_display_headline` | factory Cormorant+Onest headline after poster composite |
| `require_cover_meme_sticker` | exactly ONE catalog meme PNG pasted |
| `require_large_phone_sticker` | kitchen-tablo phone +7 (993) 574-83-22 after poster composite |
| `forbid_people_heavy_cover` | no people-heavy group scene photo |
| `forbid_split_white_collage` | no split white-panel + photo cover |
| `forbid_phone_pill_post_composite` | no opaque phone button/chip from brand_logo_composite |
| `no_logo_plate_cover` | no plate under logo |
| `forbid_ai_drawn_logo_cover` | no AI lockup |
| `cover_logo_pasted` | factory logo on cover |
| `inline_no_logo_on_inlines` | ZERO company logos on all 7 inline frames |

```bash
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

Python gates: `validate_cover_type_meme_sticker_gates` + `validate_cover_anti_collage_gates` on `cover.png`.
