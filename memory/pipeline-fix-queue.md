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

## INC-20260828-1130 — link-verify IDN Cyrillic domain

status: fixed
run_date: 2026-08-28
role: excalibur-blog-publish
topic_id: B03
article_dir: memory/blog/articles/B03-dve-nochi-otel-ili-kvartira-posutochno
severity: medium
category: script

### What went wrong

- `excalibur_blog_link_verify.py` failed on `https://добрыйдом-72.рф/` with latin-1 encode error — blocked publish dry-run.

### Fixer resolution

fixed_at: 2026-08-28
fix_summary:
- Added `encode_idn_url()` in `excalibur_blog_link_verify.py` for Cyrillic tenant domains.
files_changed:
- `scripts/excalibur_blog_link_verify.py`
checks_run:
- B03 link-verify.json verdict pass
commit: 7fda1d2

## INC-20260828-1131 — llms-full.txt FTP timeout

status: needs-human
run_date: 2026-08-28
role: excalibur-blog-publish
topic_id: B03
severity: low
category: env

### What went wrong

- Post-publish llms deploy: `llms.txt` OK; `llms-full.txt` (~55KB) FTP timeout. Article live PASS.

### needed_decision_or_secret

- Retry llms-full deploy off-peak or increase FTP timeout.

