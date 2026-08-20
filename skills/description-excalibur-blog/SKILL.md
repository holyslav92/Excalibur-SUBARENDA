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
**До Cover-text** (и параллельно Schema можно готовить позже, но Description — до cover-text).

## Вход

- `article.html` — финальный текст (не `drafts/writer.html`)
- `title-brief.json` — H1 (description **не** копирует)
- `research-notes.md` — Wordstat / угол
- `shared/dzen-description-rules.md` — **обязательно**

## Что пишешь

**1–2 предложения** для карточки Дзена (~120–220 символов):

- **Ритм Klyshin** — case hook, разговорная первая реплика, интрига.
- **Факты / город:** Святослав Шакин / Тюмень.
- **≠ title** — другая формулировка, не SEO-хвост H1.
- **≠ truncated lead** — не первые абзацы статьи (double card).

## Выход: `description-brief.json`

```json
{
  "topic_id": "B01",
  "description": "Продавец говорит «всё чисто». Одна строка в реквизите 4 говорит обратное — и аванс уже поздно отменять без нервов.",
  "rhythm": "klyshin_case_hook",
  "geo": "Тюмень",
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

- Копировать H1 из title-brief
- Обрезать первый абзац article.html
- Brand vanity «риэлтор тюмень» как единственный смысл
- Плагиат постов @klyshin_A

Agent: `agents/excalibur-blog-description.md`
