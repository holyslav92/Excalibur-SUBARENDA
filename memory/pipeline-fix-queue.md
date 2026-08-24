# Pipeline fix queue

## INC-20260824-1305 — Dzen relative /blog/ href 404

status: fixed
run_date: 2026-08-24
role: excalibur-blog-fixer
topic_id: LIVE
severity: high
category: script

### What went wrong

- Outbound interlink in `article.html` is `href="/blog/{slug}/"`. On the site this works; in Яндекс.Дзен RSS `content:encoded` resolves against `dzen.ru` → 404.
- Inbound default path used `/blog/vtorichka-i-riski/{slug}/` (чужой тенант) instead of `/blog/{slug}/`.

### How the agent recovered this run

- `absolutize_root_relative_hrefs()` in `load_article` at publish.
- Live xfix `--latest 9 --apply` for already published posts.
- Inbound permalink = `/blog/{slug}/` + absolute URL when `PUBLIC_SITE_URL` set.

### Durable fix needed before next run

- WP payload must never ship root-relative `/blog/` hrefs.

### Suggested files to inspect/change

- `scripts/excalibur_blog_site_base.py`
- `scripts/excalibur_blog_wp_publish.py`
- `scripts/excalibur_blog_live_xlink_fix.py`
- `scripts/excalibur_blog_interlink_lib.py`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-24
fix_summary:
- Publish absolutizes root-relative hrefs for Dzen/RSS.
- Live xfix converts existing posts; inbound path without WP category slug.
files_changed:
- `scripts/excalibur_blog_site_base.py`
- `scripts/excalibur_blog_wp_publish.py`
- `scripts/excalibur_blog_live_xlink_fix.py`
- `scripts/excalibur_blog_interlink_lib.py`
- `scripts/excalibur_blog_post_publish_interlink.py`
checks_run:
- `python3 -m unittest tests/test_absolutize_hrefs.py`
commit: pending-parent-commit

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
