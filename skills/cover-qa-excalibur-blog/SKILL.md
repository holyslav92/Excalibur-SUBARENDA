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

1. **Лицо + телосложение хоста** — тот же человек что `face-studio-2026-06-23.jpg` (кости, hairline, глаза, щетина, 28 лет); **medium slim**. FAIL: chubby, другой человек.
2. **Эмоция НЕ копия референса** — выражение под hook статьи (шок, side-eye, гримаса, недоумение «где деньги?»…). **FAIL** если вежливая студийная closed-mouth smile 1:1 как на reference. PASS если живая мимика под тему.
3. **Light / high-key** — светлая картинка, sun flare/glow; **нет** dark cinematic / low-key / twilight.
3. **Motif 14д** — нет коллизии с `memory/cover/used-motifs.json` (composition/location/meme…).
4. **Люди в 8-set** — host на cover = единственный крупный человек; inline people-memes только как маленькие стикеры из `meme-top100.json`.
5. **Коты** — meme-cat на cover/inline **или** недельная каденция не просела (не 3+ статей подряд без кота).
6. **Wordstat stickers** — 1–3 читаемых стикера с live P0-фразами (из `quad-manifest.json` → `wordstat_stickers`).
7. **identity-real** — 4 live-файла на месте.
8. **Inline utility (все 7)** — каждый inline проходит тест пользы: факт/порядок/число/сравнение по H2; не ряд иконок+3 слова; не host face.
9. **inline_no_host_face** — ни на одном inline нет лица Святослава / identity-real.
10. **inline_no_co_host_human** — нет stock model / generated man / handsome realtor / large meme person как co-host или presenter на inline.
11. **inline_meme_sticker_scale** — если мем-человек на inline, он ≤15% кадра, угол/край, не герой.
12. **meme_people_real_catalog** — people-memes из `memory/cover/meme-top100.json`, не выдуманные лица.

Канон: `memory/cover/cover-canon.json`.

## Выход: `cover/cover_qa.json`

```json
{
  "agent": "excalibur-blog-cover-qa",
  "status": "PASS",
  "checked_at": "2026-08-18",
  "topic_id": "B01",
  "checks": {
    "identity_face_28yo": true,
    "identity_body_medium_slim": true,
    "identity_expression_invented": true,
    "light_high_key": true,
    "motif_no_collision_14d": true,
    "people_in_8_set": true,
    "cats_cadence_ok": true,
    "wordstat_stickers_1_3": true,
    "identity_real_files": true,
    "inline_utility_all_7": true,
    "inline_no_host_face": true,
    "inline_no_co_host_human": true,
    "inline_meme_sticker_scale": true,
    "meme_people_real_catalog": true
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
- identity-real missing
- dark cinematic / wrong face / reference smile clone → return Cover

Agent: `agents/excalibur-blog-cover-qa.md`
