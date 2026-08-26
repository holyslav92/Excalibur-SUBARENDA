# Pipeline fix queue

## INC-20260826-1257 — Metrika credentials missing (Content-learner B03)

status: open
run_date: 2026-08-26
role: excalibur-blog-content-learner
topic_id: B03
article_dir: memory/blog/articles/B03-vyezd-v-12-00-poezd-v-16-30-chemodany-ne-v-taksi
severity: medium
category: secrets

### What went wrong

- `excalibur_blog_metrika_fetch.py --days 30 --ingest` exit 2:
  `METRIKA CREDENTIALS BLOCKER` — `YANDEX_METRIKA_OAUTH_TOKEN` and
  `YANDEX_METRIKA_COUNTER_ID` not set in Cloud Secrets/env.
- `memory/analytics/metrika-latest.json` not created; cohort analysis skipped.

### How the agent recovered this run

- evidence_gate=SKIP (no content-evidence-report.json — expected under human-first-v2).
- Recorded low-confidence lesson `LESSON-20260826-1257-B03-bagazh-okno-vyezd` in
  `memory/content-lessons.md` from pipeline artifacts only (title-brief, gates, publish).
- No durable apply; rollback_check=INSUFFICIENT_DATA.

### Durable fix needed before next run

- Set `YANDEX_METRIKA_OAUTH_TOKEN` (OAuth scope `metrika:read`) and
  `YANDEX_METRIKA_COUNTER_ID` in Cloud Secrets or `memory/site.env.local`.
- Re-run Content-learner for B03 after credentials available to ingest Metrika cohort.

### Suggested files to inspect/change

- Cloud Secrets / `.env` per `CLOUD-FIRST-RUN.md` and `shared/yandex-metrika-contract.md`
- `scripts/excalibur_blog_metrika_fetch.py`

### Secrets

- YANDEX_METRIKA_OAUTH_TOKEN — missing
- YANDEX_METRIKA_COUNTER_ID — missing

## INC-20260824-1038 — live-page gate /blog permalink vs schema URL

status: fixed
run_date: 2026-08-24
role: excalibur-blog-publish
topic_id: B03
article_dir: memory/blog/articles/B03-skrytye-doplaty-pri-posutochnoj-arende-ot-hozyaina
severity: medium
category: script

### What went wrong

- After successful FTP publish (B03, wp_post_id 3947), `excalibur_blog_live_page_gate.py` failed: `live BlogPosting JSON-LD URL does not exactly match permalink`.
- WP permalink is `/blog/{slug}/`; committed schema JSON-LD uses `{{SITE_BASE}}/{slug}/` (schema-gate forbids `/blog/` in repo JSON-LD).

### How the agent recovered this run

- Added `_canonical_article_path()` in live-page gate to strip optional `/blog/` prefix before comparing permalink vs JSON-LD URL.
- Re-ran live gate → PASS for B03.

### Durable fix needed before next run

- Gate must normalize `/blog/{slug}/` vs `/{slug}/` without requiring schema or WP permalink rewrites.

### Suggested files to inspect/change

- `scripts/excalibur_blog_live_page_gate.py`
- `shared/live-page-contract.md`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-24
fix_summary:
- `_canonical_article_path()` normalizes optional `/blog/` prefix before permalink vs BlogPosting URL compare.
- Documented parity rule in `shared/live-page-contract.md`.
files_changed:
- `scripts/excalibur_blog_live_page_gate.py`
- `shared/live-page-contract.md`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_live_page_gate.py`
- B03 `live-page-report.json` status PASS
commit: 3b837c2

## INC-20260824-1042 — llms deploy ImportError

status: fixed
run_date: 2026-08-24
role: excalibur-blog-publish
topic_id: B03
article_dir: memory/blog/articles/B03-skrytye-doplaty-pri-posutochnoj-arende-ot-hozyaina
severity: medium
category: script

### What went wrong

- `excalibur_blog_llms_deploy.py` raised ImportError: `resolve_publish_transport` missing from `excalibur_blog_remote_transport`.

### How the agent recovered this run

- Switched to `upload_bytes` + `transport_mode` from `excalibur_blog_remote_transport` (same module publish uses).

### Durable fix needed before next run

- llms deploy must import only symbols that exist in remote transport module.

### Suggested files to inspect/change

- `scripts/excalibur_blog_llms_deploy.py`
- `scripts/excalibur_blog_remote_transport.py`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-24
fix_summary:
- `excalibur_blog_llms_deploy.py` uses `upload_bytes` + `transport_mode` instead of missing `resolve_publish_transport`.
- Note: large `llms-full.txt` FTP upload may still be slow; monitor separately (not ImportError).
files_changed:
- `scripts/excalibur_blog_llms_deploy.py`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_llms_deploy.py`
- `python3 scripts/excalibur_blog_llms_deploy.py --dry-run` → llms files present, transport ftp
commit: 3b837c2
