---
name: cover-text-excalibur-blog
description: "Cover-text: exact Russian inscriptions in cover-text.json, gate PASS before Cover."
---

# Cover-text Agent — надписи для type+meme+phone-sticker v3

## Cover canon (Добрый дом type_meme_sticker_v3)

- **Spectacular headline 2–8 слов** — hero display typography (NOT wall of type, NOT gold glitter)
- **Телефон +7 (993) 574-83-22 LARGE die-cut sticker** — BIG readable graphic, **без pill**, **не** tiny in-scene door number
- **Ровно 1 meme** из meme-top100.json на обложке (named entry)
- **Логотип:** factory paste alpha PNG top-right empty pad — **не** рисовать в генерации
- **NO people-heavy scene photo on cover**
- **NO host face** на обложке
- **NO +7 922 001 65 05**

## Вход / выход

`cover/cover-text.json` — hook, highlight, sticky (optional short), inline_labels, wordstat_stickers (for inline panels only — NOT cover sticker soup).

## Gate

```bash
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir <article_dir>
```

## Не делай

- Не добавляй Wordstat stickers для cover collage — scene poster only
- Не запускай manifest/prompt/Kie/publish — только cover-text.json + gate
