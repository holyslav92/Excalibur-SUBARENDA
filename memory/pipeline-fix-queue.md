# Excalibur BLOG — pipeline fix queue

Durable incident memory for Director and fixer. See `shared/pipeline-incident-fix-contract.md`.

## INC-20260822-1307-content-learner-metrika-credentials
status: open
run_date: 2026-08-22
role: excalibur-blog-content-learner
topic_id: B03
article_dir: memory/blog/articles/B03-dogovor-arendy-pravila-prozhivaniya-posutochno
severity: blocker
category: env

### What went wrong
- `excalibur_blog_metrika_fetch.py --days 30 --ingest` exited 2 with `METRIKA CREDENTIALS BLOCKER`.
- `YANDEX_METRIKA_OAUTH_TOKEN` and `YANDEX_METRIKA_COUNTER_ID` are not set in Cloud Secrets/env.
- Post-publish content learning for B03 cannot ingest on-site behavioral signals (pageviews, bounce, duration).

### How the agent recovered this run
- Recorded METRIKA FEEDBACK BLOCKER incident in this queue.
- Wrote optional/low-confidence lesson in `memory/content-lessons.md` from publish artifacts only (evidence_gate=SKIP).
- Did not invent Metrika metrics or content-evidence-report.json.

### Durable fix needed before next run
- Add `YANDEX_METRIKA_OAUTH_TOKEN` (OAuth scope `metrika:read`) and `YANDEX_METRIKA_COUNTER_ID` to Cursor Cloud Secrets per `shared/yandex-metrika-contract.md`.
- Re-run content-learner for B03 after credentials are available.

### Suggested files to inspect/change
- `shared/yandex-metrika-contract.md`
- `scripts/excalibur_blog_metrika_fetch.py`
- Cursor Cloud Secrets (tenant env)

### Secrets
- none recorded

### Fixer resolution
- pending
