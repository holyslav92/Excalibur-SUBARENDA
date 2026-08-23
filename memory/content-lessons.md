# Excalibur BLOG — content lessons

Active lessons for content-learner v2 (evidence + Metrika). Historical scorecards read-only.

## LESSON-20260823-1235-B03-cover-image-api-blocker
status: proposed
topic_id: B03
category: other
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; editorial evidence gate SKIP — оценка текста по named findings недоступна.
- artifact: cover/cover-blocker.json
  finding: Cover остановлен после PASS cover-text + quad-manifest + motif gate; Derouter image generation discontinued на всех базах; Kie fallback HTTP 402 (credits insufficient).
- artifact: opening-meta-gate.json, html-linter-report.json
  finding: Sol+Description+Schema+Indexer upstream PASS — html-linter 0 errors, opening-meta PASS.
- metrika_signal: none (METRIKA CREDENTIALS BLOCKER; статья status=draft, не в published-articles ledger — поведенческих данных по slug нет даже при рабочем API)

### Named blockers
- DEROUTER_IMAGE_DISCONTINUED
- KIE_CREDITS_INSUFFICIENT
- METRIKA_CREDENTIALS_MISSING
- EVIDENCE_SKIPPED
- LOW_SAMPLE (unpublished — нет on-site трафика)

### Keep
- Текстовый контур B03 (Research → Writer → Sol → Description → Schema → Indexer) прошёл без редакционных гейтов; cover-text и quad-prompts готовы к повторному прогону после восстановления image API.
- Угол «кот в объявлении vs штраф в договоре» — отдельный от B01/B02; не дублирует заселение/залог.

### Change
- Перед следующим Cover-run: восстановить Derouter image model/base или пополнить Kie credits; не переписывать article.html/Sol из‑за infra-blocker.
- Настроить YANDEX_METRIKA_OAUTH_TOKEN + YANDEX_METRIKA_COUNTER_ID в Cloud Secrets для post-publish feedback loop.

### Never again
- Не трактовать Cover image API failure как сигнал к правке прозы Writer/Sol.
- Не выводить причинность по CTR/retention для неопубликованного черновика.
- Не invent'ить content-evidence-report.json ради закрытия evidence gate.

### Proposed apply
- Fixer: проверить DEROUTER_IMAGE_MODEL / derouter-image-base-probe, обновить контракт или env; пополнить Kie; rerun derouter_gpt_image2_api для quad-mcp-batch-01/02.
- Human: Metrika OAuth + counter id (см. shared/yandex-metrika-contract.md).
- Content: после publish — повторный content-learner с Metrika ingest для cohort B01/B02/B03.

### Durable applied
- none

### Resolution
status: recorded
