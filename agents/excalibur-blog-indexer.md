---
name: excalibur-blog-indexer
description: "⑤ Indexer: llms.txt only. Субагент Task."
model: inherit
readonly: false
is_background: false
---

**Язык:** русский. **Шаг пайплайна:** ⑤

## Incident memory

Блокер/retry → `memory/pipeline-fix-queue.md`.
`incident_report: none | memory/pipeline-fix-queue.md#INC-...`

## Задачи

1. `python3 scripts/excalibur_blog_llms_generator.py --blog-dir memory/blog/articles --blog-path / --out-dir memory/blog`
2. Secret-scan `memory/blog/llms.txt` + `llms-full.txt` (placeholders only).
3. Handoff `=== EXCALIBUR BLOG INDEXER ===`

**HARD:** только llms. Не меняй `article.html`. Не promotion-checklist. Interlinker удалён.

## Skill

`skills/indexer-excalibur-blog/SKILL.md`
