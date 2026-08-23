# Excalibur BLOG — pipeline fix queue

Durable incident memory for Director and fixer. Canonical filename only.

## INC-20260823-1235-cover-derouter-image-kie
status: open
run_date: 2026-08-23
role: excalibur-blog-cover
topic_id: B03
article_dir: memory/blog/articles/B03-zhivotnye-posutochno
severity: blocker
category: api

### What went wrong
- DEROUTER_IMAGE_MODEL image generation discontinued on all Derouter bases (api.derouter.ai, api.apikey.cloud, api-direct.*) — probe memory/blog/derouter-image-base-probe.json.
- Kie fallback createTask HTTP 402 — credits insufficient.
- Canvas PNGs not generated; cover.png and inline-01..07 missing.

### How the agent recovered this run
- Wrote cover/cover-blocker.json with completed_steps and remediation; pipeline stopped before Cover-QA/Publish.

### Durable fix needed before next run
- Restore working image generation (new DEROUTER_IMAGE_MODEL or base per shared/derouter-gpt-image-api-contract.md) OR top up Kie credits.
- Rerun derouter_gpt_image2_api for quad-mcp-batch-01 and quad-mcp-batch-02.

### Suggested files to inspect/change
- `shared/derouter-gpt-image-api-contract.md`
- `shared/kie-gpt-image-api-contract.md`
- `scripts/excalibur_blog_derouter_gpt_image2_api.py` (if exists)
- Cloud Secrets: DEROUTER_IMAGE_MODEL, KIE_API_KEY

### Secrets
- none recorded

### Fixer resolution
- pending

## INC-20260823-1235-content-learner-metrika-credentials
status: open
run_date: 2026-08-23
role: excalibur-blog-content-learner
topic_id: B03
article_dir: memory/blog/articles/B03-zhivotnye-posutochno
severity: medium
category: env

### What went wrong
- `excalibur_blog_metrika_fetch.py --days 30 --ingest` exited METRIKA CREDENTIALS BLOCKER: YANDEX_METRIKA_OAUTH_TOKEN and YANDEX_METRIKA_COUNTER_ID not set.

### How the agent recovered this run
- Recorded lesson with metrika_signal: none; logged incident; no fabricated metrics.

### Durable fix needed before next run
- Set YANDEX_METRIKA_OAUTH_TOKEN and YANDEX_METRIKA_COUNTER_ID in Cloud Secrets per shared/yandex-metrika-contract.md.

### Suggested files to inspect/change
- `shared/yandex-metrika-contract.md`
- Cursor Cloud Secrets / env

### Secrets
- none recorded

### Fixer resolution
- pending
