---
name: writer-excalibur-blog
description: Write meaning draft drafts/writer.html; Sol applies tenant SOUL style.
---

# Writer Skill — смысл статьи (черновик)

## Модель (HARD) — thin conductor

**Не пиши прозу моделью Cursor.** Собери `--user-file` из research/title-brief и вызови Derouter powerful tier (claude-opus-5):

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role writer \
  --system-file skills/writer-excalibur-blog/SKILL.md \
  --user-file <assembled-writer-inputs.md> \
  --output drafts/writer.html \
  --article-dir <article_dir>
```

Контракт: `shared/derouter-opus-brain-contract.md`.
`DEROUTER WRITER BLOCKER` → стоп. Запрещён тихий fallback на Composer/Auto.

Тон Klyshin (кейс, короткие абзацы) допустим; **автор фактов** — Святослав / Тюмень.

Ты пишешь **смысл**: факты, тезисы, ограничения, CTA.  
Финал слога делает **Sol** (`excalibur-blog-sol`) по SOUL + examples.

Выход: **`drafts/writer.html`** (чистый HTML-фрагмент без `<h1>`).  
Можно положить ту же копию во временный `article.html`, но канон —
`drafts/writer.html`. Sol перепишет `article.html`.

## Читаешь

1. `shared/writer-master-prompt.md` (секция Writer / смысл)
2. `research-notes.md`
3. `title-brief.json`
4. `published-titles-only.md`
5. `shared/published-articles.md` — **только** `status=published` для outbound interlink
6. `shared/dzen-content-rules.md` + RF (не герой Meta/…) — кратко

## Не обязан читать (это зона Sol)

`shared/SOUL.md`, `shared/soul-examples/*` — Sol применит слог сам.
Можешь писать ясно по-русски без SEO; не трать ход на косплей тенанта.

## Правила смысла

- Все факты только из research; не выдумывай.
- Структура: открытие → несколько H2 с мыслями → практика/ограничения → CTA.
- Без research-даты / Wordstat в открытии (Sol всё равно вычистит, но не засоряй).
- CTA: `tenant-config.cta_links` + MAX по `cta_channels.max` (обязательно при `cta_required=true`).
- **Interlink (если `interlink_old_articles=true`):** 1–3 контекстные `<a href="/blog/...">` на
  опубликованные sibling из ledger; якорь по смыслу H2, не «читайте также» в каждом абзаце.
- Не читай чужие article.html / live-сайт / уже опубликованные статьи сайта / topics.

## Handoff

```text
drafts/writer.html
=== EXCALIBUR BLOG WRITER ===
draft: meaning
next: Sol
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```
