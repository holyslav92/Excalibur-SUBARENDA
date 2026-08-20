# Excalibur BLOG — content learning contract v2

Новый контур учится на проверяемых evidence и сигналах поведения, а не на
числовых редакционных рейтингах.

Исторические `content-scorecard*.json`, judge/ensemble reports, score-based
lessons и ledgers остаются read-only. Их нельзя переписывать, дополнять или
использовать как шаблон будущей статьи.

## Канонические входы

- `<article_dir>/content-evidence-report.json` schema v2 — **optional** under
  `pipeline_canon=human-first-v2`. Если файла нет → evidence_gate=`SKIP`,
  не CONTENT EVIDENCE BLOCKER. Lesson можно записать как
  optional/low-confidence (Metrika-only). Если файл есть → verdict PASS
  обязателен (invalid report = BLOCK).
- артефакты из `shared/content-evidence-contract.md`;
- `memory/analytics/metrika-latest.json` (Metrika ingest внутри Content-learner;
  обязателен даже при evidence SKIP);
- active lessons из `memory/content-lessons.md`;
- `shared/content-evidence-contract.md` + `shared/pipeline-canon.json`.

Для новой статьи запрещено создавать `content-scorecard.json`,
`content-scorecard-gate.json`, LLM judge report и evaluation ensemble.
Не invent'ить `content-evidence-report.json`, чтобы обойти SKIP.

## Порядок

1. Проверить evidence:

   ```bash
   python3 scripts/excalibur_blog_content_evidence_gate.py \
     --article-dir <article_dir>
   ```

   - exit 0 + `status: SKIP` — отчёта нет; продолжить без evidence BLOCK.
   - exit 0 + `status: PASS` — использовать named findings.
   - exit 1 + `status: BLOCK` — только если report **есть**, но invalid;
     тогда `CONTENT EVIDENCE BLOCKER` + incident.

2. Content-learner сам выполняет
   `excalibur_blog_metrika_fetch.py --days 30 --ingest`. Credentials/API
   failure = `METRIKA FEEDBACK BLOCKER` + incident, не silent skip.
   Metrika ingest **обязателен** даже при evidence_gate=SKIP.
3. Сопоставить named findings с actionable Metrika signals. Low sample,
   отсутствующая цель, слабая confidence или evidence SKIP не подтверждают
   причинность.
4. Записать именованные lessons и blockers. При evidence SKIP —
   lesson optional/low-confidence, category может быть `other`, без
   CONTENT EVIDENCE BLOCKER.
5. Применять durable change только при повторённом evidence-паттерне минимум в
   двух запусках либо high-severity blocker с прямой проверяемой причиной.
   `writer-master-prompt.md` и Writer agent/skill защищены: Content Learner
   не добавляет туда правила автоматически. Writer prompt меняется только по
   явному решению человека; proposals → `memory/content-lessons.md`.
6. Записать durable apply и rollback path; затем fixer обрабатывает только
   pipeline/tool incidents.

## Формат lesson

```markdown
## LESSON-YYYYMMDD-HHMM-Bxx-short-name
status: proposed | active | validated | superseded | rejected
topic_id: Bxx
category: voice | utility | structure | beginner | geo | cta | other
confidence: high | medium | low

### Evidence
- artifact: content-evidence-report.json#… | none (skipped under human-first-v2)
  finding: ...
- metrika_signal: none | exact signal id and confidence/sample

### Named blockers
- none | MISSING_UI_BRIDGE | ASSUMED_BEHAVIOR | LOW_SAMPLE | EVIDENCE_SKIPPED | ...

### Keep
- ...

### Change
- ...

### Never again
- ...

### Proposed apply
- ...

### Durable applied
- none | path — change and rollback

### Resolution
status: recorded | applied | skipped_duplicate | needs-human
```

## Запрет числовых ratings

Нельзя производить или переносить в новые артефакты:

- overall 0–100 и любой «общий балл»;
- CORE-EEAT x/20;
- `judge_score`;
- child/parent score;
- weighted quality / ensemble;
- score delta и утверждение «качество выросло на N баллов»;
- автоматический рейтинг, который решает PASS.

`article-qa.md` содержит только `verdict: PASS|BLOCK` и evidence table. Metrika
даёт поведенческие сигналы, но не редакционный балл.

## Handoff

```text
=== EXCALIBUR BLOG CONTENT LEARNER ===
status: recorded | applied | skipped_duplicate | needs-human | blocker
topic_id:
article_dir:
evidence_gate: PASS | SKIP | BLOCK
metrika_feedback: PASS | BLOCKER
named_blockers:
lessons_recorded:
durable_applied:
rollback_check: OK | NEEDS_ROLLBACK | INSUFFICIENT_DATA
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```

`evidence_gate: SKIP` — нормальный исход human-first-v2 без отчёта; не
считать pipeline blocker. `evidence_gate: BLOCK` — только invalid present
report.

Не переписывать `article.html`, не выводить причинность из CTR/retention без
достаточной выборки и настроенной цели, не раздувать skills по одному кейсу.
