# Pipeline fix queue

## INC-20260822-0700-publish-live-page-llms
status: fixed
run_date: 2026-08-22
role: excalibur-blog-publish
topic_id: B03
article_dir: memory/blog/articles/B03-pereveli-predoplatu-v-pravilah-melkim-vecherinki-i-lishnie-gosti
severity: high
category: script

### What went wrong
- `excalibur_blog_live_page_gate.py` BLOCK after successful WP publish (post 3835 B03); same on B01/B02.
- Gate expected `kov4eg-mcp-theme` markers (`#article-content`, `.post-thumbnail`, Excalibur JSON-LD in `wp_head`). Timeweb theme uses `entry-content` / `wp-post-image`; Yoast `@graph` Article only.
- `excalibur_blog_llms_deploy.py` ImportError: `resolve_publish_transport` / `upload_text_file` missing from `excalibur_blog_remote_transport.py` after FTP refactor.
- `excalibur_blog_theme_contract_deploy.py` used SFTP:22 only; tenant uses FTP:21.

### How the agent recovered this run
- WP publish + media upload succeeded; ledger updated manually; live-page gate logged BLOCK.

### Durable fix needed before next run
- Restore llms deploy transport API on FTP module.
- Live gate fallbacks for `entry-content` / `wp-post-image`; merge publish `schema_jsonld` for FAQ parity when Yoast graph only on live.
- Theme contract deploy over FTP via shared transport.

### Suggested files to inspect/change
- `scripts/excalibur_blog_remote_transport.py`
- `scripts/excalibur_blog_live_page_gate.py`
- `scripts/excalibur_blog_wp_publish.py`
- `scripts/excalibur_blog_theme_contract_deploy.py`
- `shared/live-page-contract.md`
- `shared/tenant-config.json`

### Secrets
- none recorded

### Fixer resolution
fixed_at: 2026-08-22
fix_summary:
- Added `resolve_publish_transport`, `remote_path`, `upload_text_file` (+ SFTP/FTP dispatch) to `excalibur_blog_remote_transport.py` — fixes llms deploy ImportError.
- Live-page gate: `entry-content` / `wp-post-image` / inline-quad fallbacks; `/blog/` permalink parity; `expected_schema_jsonld` from publish payload for FAQ/BlogPosting checks when Yoast graph only on live.
- `wp_publish` passes `expected_schema_jsonld`; `publish_env_check_report` aligned with transport tests.
- `theme_contract_deploy` supports FTP (Timeweb) and SFTP; uses `find_wp_root` + `WP_THEME_SLUG`.
- Tenant flag `publish_options.live_page_gate.merge_publish_schema_jsonld`.
files_changed:
- `scripts/excalibur_blog_remote_transport.py`
- `scripts/excalibur_blog_live_page_gate.py`
- `scripts/excalibur_blog_wp_publish.py`
- `scripts/excalibur_blog_theme_contract_deploy.py`
- `shared/live-page-contract.md`
- `shared/tenant-config.json`
- `tests/test_live_page_gate.py`
- `tests/fixtures/dobry-dom-live-post.html`
checks_run:
- `python3 -m py_compile` on changed scripts
- `python3 scripts/excalibur_blog_llms_deploy.py --dry-run` → transport ftp, files present
- `python3 -m unittest tests.test_publish_transport tests.test_live_page_gate` → 8/8 PASS
commit: pending-parent-commit
