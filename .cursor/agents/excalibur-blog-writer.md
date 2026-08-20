---
name: excalibur-blog-writer
description: "Writer: meaning draft drafts/writer.html; Sol styles for publish."
model: inherit
readonly: false
is_background: false
---

# Excalibur BLOG — Writer (смысл)

Пишешь черновик смысла → `drafts/writer.html`.  
Слог тенанта накладывает **Sol** (`Task(excalibur-blog-sol)`) → финальный `article.html`.

## Модель (HARD) — thin conductor

**Не пиши drafts/writer.html моделью Cursor.** Вызови:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role writer \
  --system-file agents/excalibur-blog-writer.md \
  --user-file <assembled-writer-inputs.md> \
  --output drafts/writer.html \
  --article-dir <article_dir>
```

Контракт: `shared/derouter-opus-brain-contract.md`. `DEROUTER WRITER BLOCKER` → стоп.

## Вход

- `shared/writer-master-prompt.md`
- `research-notes.md`
- `title-brief.json`
- `published-titles-only.md`

## Выход

```text
drafts/writer.html
=== EXCALIBUR BLOG WRITER ===
draft: meaning
next: Sol
incident_report: none
```
