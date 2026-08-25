---
name: description-excalibur-blog
description: "Description: Dzen card teaser after Sol; Klyshin rhythm; not title/lead duplicate."
---

# Description — Dzen card teaser

## Thin conductor + Derouter utility (HARD)

**Не пиши description моделью Cursor:**

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role description \
  --system-file skills/description-excalibur-blog/SKILL.md \
  --user-file <assembled-description-inputs.md> \
  --output description-brief.json \
  --article-dir <article_dir>
```

`DEROUTER DESCRIPTION BLOCKER` → стоп. Контракт: `shared/derouter-opus-brain-contract.md`.

## Когда

**После Sol** (`article.html` + `pipeline_canon` stamp).  
**До Cover-text**.

## Вход

- `article.html` — финальный текст (не `drafts/writer.html`)
- `title-brief.json` — H1 (description **не** копирует)
- `research-notes.md` — Wordstat / угол
- `shared/dzen-description-rules.md` — **обязательно**

## OG / description factory (HARD)

1. **NEVER** put guest-burn arithmetic (e.g. 2500→6500) in og:description **as if it is Добрый дом's own price**.
2. **NEVER** mention **Святослав Шакин** / **The Риэлтор** in og:description. Author = **Добрый дом**.
3. Teaser = **ожог/риск** (Klyshin rhythm), не прайс-лист и не «история Шакина».

## Что пишешь

**1–2 предложения** для карточки Дзена (~120–220 символов):

- **Ритм Klyshin** — case hook, разговорная первая реплика, интрига.
- **Бренд:** Добрый дом / guest pain Тюмень — **не** Шакин, **не** риэлтор.
- **≠ title** — другая формулировка, не SEO-хвост H1.
- **≠ truncated lead** — не первые абзацы статьи (double card).

## Выход: `description-brief.json`

```json
{
  "topic_id": "B01",
  "description": "Хост пишет «утром будет». Вы уже в квартире — где бойлер, спросите до того, как замёрзнете.",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
  "author_brand": "Добрый дом",
  "not_equal_title": true,
  "not_truncated_lead": true,
  "verdict": "PASS"
}
```

## Gate

```bash
python3 scripts/excalibur_blog_description_gate.py --article-dir <dir>
```

Только PASS → Cover-text.

## Запрещено

- Guest-burn price ladder (2500→6500) как цена **Доброго дома**
- Шакин / The Риэлтор / «история Святослава»
- Копировать H1 из title-brief
- Обрезать первый абзац article.html
- ЕГРН / наследство / ипотека как spine
- Плагиат постов @klyshin_A

Agent: `agents/excalibur-blog-description.md`
