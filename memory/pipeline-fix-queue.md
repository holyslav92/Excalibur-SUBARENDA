# Pipeline fix queue

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

## INC-20260827-0815-publish-ftp-pasv-bootstrap
status: fixed
run_date: 2026-08-27
role: excalibur-blog-publish
topic_id: B03
article_dir: memory/blog/articles/B03-na-kartochke-posutochno-4-8-dva-odinakovyh-vse-super
severity: medium
category: transport

### What went wrong

- First two publish attempts failed on FTP passive data-channel TimeoutError uploading ~13MB bootstrap.
- Cyrillic absolute blog hrefs broke link-verify and crosslink-qa HTTP checks.

### How the agent recovered this run

- Relative `/blog/` hrefs; wp_category_slugs; ACTIVE FTP fallback + FTP_TIMEOUT in remote transport.
- Publish OK post=4052; live-page gate PASS; inline src → wp-content URLs.

### Durable fix needed before next run

- Keep ACTIVE fallback and FTP_TIMEOUT=300 for 7-inline articles; prefer relative internal hrefs.

fix_summary:
- `excalibur_blog_remote_transport.py` PASV-then-ACTIVE STOR; env FTP_TIMEOUT.

commit: pending

## INC-20260827-1136-metrika-credentials-content-learner
status: open
run_date: 2026-08-27
role: excalibur-blog-content-learner
topic_id: B03
article_dir: memory/blog/articles/B03-na-kartochke-posutochno-4-8-dva-odinakovyh-vse-super
severity: high
category: secrets

### What went wrong

- Post-publish Content-learner for B03 (reviews/отзывы angle, live
  `/blog/na-kartochke-posutochno-4-8-dva-odinakovyh-vse-super/`) could not
  run mandatory Metrika ingest:
  `python3 scripts/excalibur_blog_metrika_fetch.py --days 30 --ingest` → exit 2
  `METRIKA CREDENTIALS BLOCKER`.
- `YANDEX_METRIKA_OAUTH_TOKEN` and `YANDEX_METRIKA_COUNTER_ID` unset in Cloud
  Secrets/env. No `memory/analytics/metrika-latest.json` snapshot exists.

### How the agent recovered this run

- Evidence gate SKIP (no content-evidence-report.json — normal human-first-v2).
- Recorded `METRIKA FEEDBACK BLOCKER` + lessons in `memory/content-lessons.md`
  without inventing metrics. No durable content apply.

### Durable fix needed before next run

- Configure Metrika OAuth (metrika:read) + counter id per
  `shared/yandex-metrika-contract.md`.
- Re-run Content-learner for B03 (and subsequent publishes) with Metrika PASS.

### Suggested files to inspect/change

- Cursor Cloud Secrets / `memory/site.env.local` (local only, never commit)
- `shared/yandex-metrika-contract.md`
- `scripts/excalibur_blog_metrika_fetch.py`

### Secrets

- `YANDEX_METRIKA_OAUTH_TOKEN` — missing
- `YANDEX_METRIKA_COUNTER_ID` — missing
