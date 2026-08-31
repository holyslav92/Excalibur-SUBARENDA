---
name: cover-text-excalibur-blog
description: "Cover-text: exact Russian inscriptions in cover-text.json, gate PASS before Cover."
---

# Cover-text Agent — надписи для scene poster v2

## Cover canon (Добрый дом scene_poster_v2)

- **Короткий hook 2–6 слов** — optional in-scene, readable Cyrillic (NOT wall of type, NOT gold glitter collage)
- **Телефон +7 (993) 574-83-22 in-scene** (домофон, бумага на двери, карточка хозяина, магнит) — **без pill**
- **Логотип:** factory paste alpha PNG top-right empty pad — **не** рисовать в генерации
- **NO meme/sticky/Wordstat sticker soup on cover**
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
