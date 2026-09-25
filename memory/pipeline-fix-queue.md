# Excalibur BLOG — pipeline fix queue

Durable incident memory for the fixer loop. See `shared/pipeline-incident-fix-contract.md`.

## INC-20260925-1500-cover-qa-gate-json-script-split
status: fixed
run_date: 2026-09-25
role: excalibur-blog-cover-qa
topic_id: B03
article_dir: memory/blog/articles/B03-posutochno-tyumen-v-filtre-mozhno-s-sobakoj-u-dveri-otkaz
severity: medium
category: qa

### What went wrong
- `cover/cover_qa.json` stamped `status: PASS` with all `checks: true`, but
  `python3 scripts/excalibur_blog_cover_qa_gate.py` FAIL locally (drawn-logo /
  white-plate / official PNG pixel checks on cover + inline panels).
- Publish preflight did not run the cover QA gate script — only checked
  `cover/cover.png` exists — so B03 shipped with JSON PASS vs script FAIL split.

### How the agent recovered this run
- Cover regen + manual PASS stamp after visual review; publish completed with live PASS.
- Gate script was not re-run as publish blocker before upload.

### Durable fix needed before next run
- Enforce `excalibur_blog_cover_qa_gate.py` in `check_publish_prerequisites`.
- Cover-QA agent/skill: JSON PASS only after script exit 0; publish re-validates.

### Suggested files to inspect/change
- `scripts/excalibur_blog_wp_publish.py`
- `agents/excalibur-blog-cover-qa.md`
- `skills/cover-qa-excalibur-blog/SKILL.md`
- `shared/excalibur-wp-publish-contract.md`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-09-25
fix_summary:
- Publish preflight runs `excalibur_blog_cover_qa_gate.py` (same as Cover-QA handoff).
- Cover-QA agent + skill: HARD — JSON PASS insufficient without script OK (B03 note).
- WP publish contract documents cover QA script + llms FTP transport path.
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `scripts/excalibur_blog_cover_qa_gate.py`
- `agents/excalibur-blog-cover-qa.md`
- `.cursor/agents/excalibur-blog-cover-qa.md`
- `skills/cover-qa-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-qa-excalibur-blog/SKILL.md`
- `shared/excalibur-wp-publish-contract.md`
- `tests/test_publish_cover_qa_prereq.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_wp_publish.py scripts/excalibur_blog_cover_qa_gate.py`
- `python3 -m unittest tests.test_publish_cover_qa_prereq tests.test_publish_transport -q`
- `python3 scripts/excalibur_blog_cover_qa_gate.py --article-dir memory/blog/articles/B03-posutochno-tyumen-v-filtre-mozhno-s-sobakoj-u-dveri-otkaz` (still FAIL on B03 artifacts — expected until Cover regen + gate PASS)
commit: e92fc99c

## INC-20260925-1506-content-learner-metrika-credentials
status: open
run_date: 2026-09-25
role: excalibur-blog-content-learner
topic_id: B03
article_dir: memory/blog/articles/B03-posutochno-tyumen-v-filtre-mozhno-s-sobakoj-u-dveri-otkaz
severity: blocker
category: env

### What went wrong
- `python3 scripts/excalibur_blog_metrika_fetch.py --days 30 --ingest` exited with
  `METRIKA CREDENTIALS BLOCKER` — `YANDEX_METRIKA_OAUTH_TOKEN` and
  `YANDEX_METRIKA_COUNTER_ID` unset in Cloud env.
- No `memory/analytics/metrika-latest.json` refresh; B03 post-publish behavioral
  feedback loop blocked for this content-learner run.

### How the agent recovered this run
- Recorded LESSON-20260925-1506-B03-cover-qa-json-gate-split from pipeline
  artifacts + cover QA gate FAIL vs JSON PASS (Metrika-independent).
- Did not invent Metrika metrics or content-evidence-report.

### Durable fix needed before next run
- Set Yandex Metrika OAuth (`metrika:read`) and counter id in Cloud Secrets/env.
- Re-run content-learner Metrika ingest after credentials land.

### Suggested files to inspect/change
- Cloud Secrets / tenant env for Metrika vars
- `scripts/excalibur_blog_metrika_fetch.py`

### Secrets
- none recorded (missing vars only)

## INC-20260925-1500-llms-deploy-ftp-transport
status: fixed
run_date: 2026-09-25
role: excalibur-blog-publish
topic_id: B03
article_dir: memory/blog/articles/B03-posutochno-tyumen-v-filtre-mozhno-s-sobakoj-u-dveri-otkaz
severity: medium
category: script

### What went wrong
- Post-publish `llms.txt` deploy on Timeweb needed FTP text upload; helper was missing
  (`upload_text_file` / `resolve_publish_transport`) while article publish used FTP bootstrap.

### How the agent recovered this run
- Added `resolve_publish_transport`, `upload_text_file`, `_upload_text_ftp` in
  `excalibur_blog_remote_transport.py` (commit 89981c5d); B03 publish + llms deploy PASS.

### Durable fix needed before next run
- Keep FTP llms path tested; document in publish contract (already in repo after 89981c5d).

### Suggested files to inspect/change
- `scripts/excalibur_blog_remote_transport.py`
- `scripts/excalibur_blog_llms_deploy.py`
- `tests/test_publish_transport.py`

### Secrets
- none recorded

### Fixer resolution
status: fixed
fixed_at: 2026-09-25
fix_summary:
- Transport helpers landed in 89981c5d; fixer synced publish contract + verified unit tests.
- No additional code change required beyond documentation alignment this run.
files_changed:
- `shared/excalibur-wp-publish-contract.md`
- `scripts/excalibur_blog_wp_publish.py` (load_env doc: FTP transport not SFTP-only)
- `tests/test_publish_transport.py` (align with transport dict in env-check report)
checks_run:
- `python3 -m unittest tests.test_publish_transport -q`
commit: e92fc99c
