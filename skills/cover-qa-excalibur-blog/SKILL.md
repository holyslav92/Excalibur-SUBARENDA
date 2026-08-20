---
name: cover-qa-excalibur-blog
description: "Cover-QA: visual gate after Cover, before Indexer/Publish; stamp cover_qa.json."
---

# Cover-QA — visual gate (после Cover)

## Когда

**После** `excalibur-blog-cover` (8 PNG готовы, inject в `article.html`).  
**До** Indexer и Publish.

FAIL → **вернуть Cover** (не Indexer/Publish).

## Что проверяешь (визуально + артефакты)

1. **Logo lockup на всех 8** — логотип «Добрый дом» читаем на cover + каждом inline; consistent corner placement; не гигантский watermark.
2. **Logo readable** — достаточный контраст (light plate на светлом фоне при необходимости).
3. **NO Shakin identity** — FAIL если face-studio-2026-06-23 / Святослав Шакин на любом изображении.
4. **Light / high-key** — светлая картинка, sun flare/glow, teal/terracotta accents; **нет** dark cinematic / low-key.
5. **Motif 14д** — нет коллизии с `memory/cover/used-motifs.json`.
6. **Wordstat stickers** — 1–3 читаемых стикера с live P0-фразами (из `quad-manifest.json` → `wordstat_stickers`).
7. **Inline utility (все 7)** — каждый inline проходит тест пользы: факт/порядок/число/сравнение по H2; не decorative-only; не ряд иконок+3 слова.
8. **inline_no_decorative_only** — FAIL если inline = пустой красивый интерьер без таблиц/цифр/схем.
9. **inline_no_host_face** — ни на одном inline нет locked host face.
10. **inline_no_co_host_human** — нет stock model / generated man / large meme person как co-host.
11. **inline_meme_sticker_scale** — мем-человек ≤15% кадра, угол/край.
12. **meme_people_real_catalog** — people-memes из `memory/cover/meme-top100.json`.

Канон: `memory/cover/cover-canon.json`.

## Выход: `cover/cover_qa.json`

```json
{
  "agent": "excalibur-blog-cover-qa",
  "status": "PASS",
  "checked_at": "2026-08-20",
  "topic_id": "B01",
  "checks": {
    "logo_lockup_all_8": true,
    "logo_lockup_readable": true,
    "no_shakin_identity_face": true,
    "light_high_key": true,
    "motif_no_collision_14d": true,
    "people_in_8_set": true,
    "cats_cadence_ok": true,
    "wordstat_stickers_1_3": true,
    "inline_utility_all_7": true,
    "inline_no_decorative_only": true,
    "inline_no_host_face": true,
    "inline_no_co_host_human": true,
    "inline_meme_sticker_scale": true,
    "meme_people_real_catalog": true,
    "cover_phone_readable": true,
    "board_stationery_ok": true,
    "typography_cyrillic_clean": true,
    "meme_density_inline_ok": true
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

- COVER QA BLOCKER — любой check false
- logo lockup missing on any of 8
- Shakin face detected → return Cover
- decorative-only inline → return Cover

Agent: `agents/excalibur-blog-cover-qa.md`
