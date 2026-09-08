---
name: excalibur-blog-cover-qa
description: "Cover-QA: type+meme+phone-sticker v3 — require meme+headline+large phone on cover, stamp cover_qa.json."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский.

## Роль

**Slim gate после Cover**, до Indexer/Publish.

## FAIL только если (brand lock + type_meme_sticker_v3)

- нет spectacular display headline на cover (`require_display_headline`)
- нет ровно 1 catalog meme на cover (`require_cover_meme_sticker`) или meme soup (2+)
- нет LARGE phone die-cut sticker (`require_large_phone_sticker`) или phone pill
- people-heavy group scene photo (`forbid_people_heavy_cover`)
- split white-panel collage (`forbid_split_white_collage`)
- нет factory logo на cover или inline count не 2–3
- AI-drawn lockup / house-with-heart / plate под logo
- WordPress UI в арте
- номер 922
- 2+ cat-meme frames (max 1 across cover+inlines)

## PASS → ship

После max-2 gen + pad-clear: если brand lock OK → `status: PASS`, не возвращай Cover.

**Drawn logo on no-logo inline** (inline_2/4/5/6): сначала `excalibur_blog_cover_inline_pad_clear.py`, затем `drawn_logo_gate`; при повторном FAIL — regen canvas.

```bash
python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir <dir>
```

Skill: `skills/cover-qa-excalibur-blog/SKILL.md`
