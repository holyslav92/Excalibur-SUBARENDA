# Excalibur BLOG — pipeline fix queue

Durable incident memory for Director and fixer. No secrets in this file.

---

## INC-20260822-1017-content-learner-metrika-credentials
status: open
run_date: 2026-08-22
role: excalibur-blog-content-learner
topic_id: B03
article_dir: memory/blog/articles/B03-otmena-bronirovaniya-posutochno-vozvrat-predoplaty
severity: medium
category: env

### What went wrong
- `python3 scripts/excalibur_blog_metrika_fetch.py --days 30 --ingest` exited 2 with `METRIKA CREDENTIALS BLOCKER`.
- `YANDEX_METRIKA_OAUTH_TOKEN` and `YANDEX_METRIKA_COUNTER_ID` not set in Cloud Secrets/env.

### How the agent recovered this run
- Recorded lesson with `metrika_signal: none` and low-confidence behavioral notes only.
- Did not invent metrics or scorecards.

### Durable fix needed before next run
- Add OAuth token (scope `metrika:read`) and numeric counter id to Cloud Secrets.
- Re-run Metrika ingest after publish learning for cohort comparison.

### Suggested files to inspect/change
- `shared/yandex-metrika-contract.md`
- Cloud Secrets / environment configuration

### Secrets
- none recorded (configure in Cloud Secrets only)

### Fixer resolution
- pending

---

## INC-20260822-1017-research-derouter-blocker-stub
status: open
run_date: 2026-08-22
role: excalibur-blog-research
topic_id: B03
article_dir: memory/blog/articles/B03-otmena-bronirovaniya-posutochno-vozvrat-predoplaty
severity: high
category: api

### What went wrong
- Derouter utility (`gpt-5.6-terra`, role research) returned BLOCKER stub during synthesis.
- `research-agent-report.json` records `derouter_status: BLOCKER`.

### How the agent recovered this run
- Manual research-notes.md from verified serp + harant community signals + Wordstat audit.
- research-agent-report.json still PASS for freshness/wordstat with explicit derouter_note.

### Durable fix needed before next run
- Verify Derouter API budget and utility model availability.
- Add documented single retry before manual fallback in derouter contract.

### Suggested files to inspect/change
- `shared/derouter-opus-brain-contract.md`
- `scripts/excalibur_blog_derouter_opus_chat.py`

### Secrets
- none recorded

### Fixer resolution
- pending

---

## INC-20260822-1017-fixer-live-page-theme-gate
status: open
run_date: 2026-08-22
role: excalibur-blog-publish
topic_id: B03
article_dir: memory/blog/articles/B03-otmena-bronirovaniya-posutochno-vozvrat-predoplaty
severity: high
category: qa

### What went wrong
- `live-page-report.json` BLOCK after publish (HTTP 200, media OK).
- Errors: FAQPage jsonld=0 vs visible FAQ=1; BlogPosting URL mismatch; `#article-content` missing; `.post-thumbnail` missing; FAQ JSON-LD ≠ visible FAQ.
- **Same error bundle on B01 and B02** — systemic gate/theme drift, not article-specific.

### How the agent recovered this run
- Post published (wp post 3845); ledger updated; learning recorded with fixer incident.
- `theme_blocks.faq/quiz/side_stickers=skip` meta applied.

### Durable fix needed before next run
- Inspect live HTML at published permalink; align theme template OR update `excalibur_blog_live_page_gate.py` selectors.
- Ensure FAQPage JSON-LD renders on live page when thematic FAQ present in body.

### Suggested files to inspect/change
- `scripts/excalibur_blog_live_page_gate.py`
- `scripts/excalibur_blog_theme_contract_deploy.py`
- `shared/live-page-contract.md`

### Secrets
- none recorded

### Fixer resolution
- pending
