# Content evidence contract v4

Редакционное качество — свидетельством, не рейтингом.

## human-first-v2: optional / legacy

Под `pipeline_canon=human-first-v2` отчёт
`content-evidence-report.json` **опционален** (legacy paperwork).

| Кто | Правило |
|-----|---------|
| Publish | не требует отчёт |
| `structure_gate` | пропускает, если файла нет |
| `content_evidence_gate` | файл отсутствует → `status: SKIP`, exit 0 |
| Content-learner | missing report → **SKIP** evidence (не BLOCK); Metrika ingest всё равно |

Если файл **есть** — gate проверяет schema v2; invalid → BLOCK.
Не выдумывать scorecards / LLM judge / fake report, чтобы «закрыть» gate.

## Артефакт

`<article_dir>/content-evidence-report.json`

## Required evidence (если отчёт пишете)

- `research_notes` → `research-agent-report.json`
- `writer_ready` → `writer-ready-gate.json`
- `links` → `link-verify.json`
- `html` → `html-linter-report.json`

## Required editorial_judgments

`standalone`, `utility`, `human_voice`, `direct_plain_language` —
`status=PASS`, `decided_by=excalibur-blog-writer`, цитата из текста.

## Gate

```bash
python3 scripts/excalibur_blog_content_evidence_gate.py --article-dir <article_dir>
```

Выход gate: `PASS` | `SKIP` | `BLOCK`. `SKIP` и `PASS` = exit 0.
