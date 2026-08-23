# Excalibur BLOG — pipeline fix queue

Durable incident memory for Director and fixer. Canonical filename only.

## INC-20260823-1235-cover-derouter-image-kie
status: needs-human
fixed_at: 2026-08-23
run_date: 2026-08-23
role: excalibur-blog-cover
topic_id: B03
article_dir: memory/blog/articles/B03-zhivotnye-posutochno
severity: blocker
category: api

### What went wrong
- Derouter image model env: generation discontinued on all Derouter bases (api.derouter.ai, api.apikey.cloud, api-direct.*) — probe memory/blog/derouter-image-base-probe.json.
- Kie fallback createTask HTTP 402 — credits insufficient.
- MCP-KV sync image tool path also failed (forbidden/off-pipeline; not a durable Cover fallback).
- Canvas PNGs not generated; cover.png and inline-01..07 missing.

### How the agent recovered this run
- Wrote cover/cover-blocker.json with completed_steps and remediation; pipeline stopped before Cover-QA/Publish.

### Durable fix needed before next run
- Restore working image generation (new Derouter image model id or base per shared/derouter-gpt-image-api-contract.md) OR top up Kie credits.
- Rerun derouter_gpt_image2_api for quad-mcp-batch-01 and quad-mcp-batch-02.

### Suggested files to inspect/change
- `shared/derouter-gpt-image-api-contract.md`
- `shared/kie-gpt-image-api-contract.md`
- `scripts/excalibur_blog_derouter_gpt_image2_api.py`
- Cloud Secrets: Derouter image model, Kie API key

### Secrets
- none recorded

### Fixer resolution
fix_summary:
- Added `scripts/excalibur_blog_cover_image_preflight.py` — fail-fast before cover-scene/quad-prompt when Derouter discontinued and Kie missing/402-known.
- Kie script: `KieCreditsBlocker` + HTTP 402 detection → **KIE CREDITS BLOCKER** (no silent retry).
- Doctor WARN when derouter-image-base-probe.json shows all bases discontinued.
- Cover skill/agents runbook: preflight step after cover-text gate.
- Contracts updated (derouter + kie).
reason:
- Image provider outage + Kie billing — not fixable in repo without owner action on Derouter image model or Kie credits.
needed_decision_or_secret:
- Set working Derouter image model id (GET /v1/models) or image API base override with image gen enabled.
- Top up Kie account / verify Kie API key billing.
files_changed:
- `scripts/excalibur_blog_cover_image_preflight.py`
- `scripts/excalibur_blog_kie_gpt_image2_api.py`
- `scripts/excalibur_blog_doctor.py`
- `shared/derouter-gpt-image-api-contract.md`
- `shared/kie-gpt-image-api-contract.md`
- `agents/excalibur-blog-cover.md`
- `.cursor/agents/excalibur-blog-cover.md`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `shared/tenant-config.json`
- `tests/test_cover_image_preflight.py`
checks_run:
- python3 -m py_compile scripts/excalibur_blog_cover_image_preflight.py scripts/excalibur_blog_kie_gpt_image2_api.py scripts/excalibur_blog_doctor.py
- python3 -m unittest tests.test_cover_image_preflight -v
commit: 79a24f8

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
