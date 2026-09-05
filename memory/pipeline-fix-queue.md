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

## INC-20260828-1246-schema-derouter-output-root
status: fixed
run_date: 2026-08-28
role: excalibur-blog-schema
topic_id: B03
article_dir: memory/blog/articles/B03-kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki
severity: medium
category: script

### What went wrong

- `excalibur_blog_derouter_opus_chat.py --role schema --output schema.jsonld --article-dir memory/blog/articles/B03-…` wrote `schema.jsonld` to repo root (`workspace/schema.jsonld`), not under `--article-dir`. Stamp landed correctly in article dir; gate FAIL `missing schema.jsonld` until manual move.

### How the agent recovered this run

- Copied JSON-LD from root `schema.jsonld` into `memory/blog/articles/B03-…/schema.jsonld`, deleted stray root file, re-ran `excalibur_blog_schema_gate.py` → PASS.

### Durable fix needed before next run

- When `--article-dir` is set and `--output` is a bare filename, resolve output under article dir (mirror stamp path). Or skill must pass full repo-relative output path.

### Suggested files to inspect/change

- `scripts/excalibur_blog_derouter_opus_chat.py`
- `skills/schema-excalibur-blog/SKILL.md`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-28
fix_summary:
- `resolve_derouter_output_path()` uses `resolve_article_output()` when `--article-dir` is set; bare filenames (e.g. `schema.jsonld`) land under article dir, not repo root.
- Schema skill documents bare `--output` resolution rule.
files_changed:
- `scripts/excalibur_blog_derouter_opus_chat.py`
- `skills/schema-excalibur-blog/SKILL.md`
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
- `tests/test_derouter_output_path.py`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_derouter_opus_chat.py`
- `python3 -m unittest tests.test_derouter_output_path -v`
commit: 06ef2a4

## INC-20260828-1335-link-verify-idna-cyrillic-host
status: fixed
run_date: 2026-08-28
role: excalibur-blog-publish
topic_id: B03
article_dir: memory/blog/articles/B03-kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki
severity: medium
category: script

### What went wrong

- `excalibur_blog_link_verify.py` with `--site-base` on Cyrillic IDN host (`добрыйдом-72.рф`) raised `UnicodeEncodeError: 'latin-1' codec can't encode characters` when urllib opened internal links.

### How the agent recovered this run

- Added `encode_idna_url()` (punycode host) before HTTP HEAD/GET; re-ran link-verify → PASS.

### Durable fix needed before next run

- All live HTTP checks must IDNA-encode non-ASCII hostnames before urllib.

### Suggested files to inspect/change

- `scripts/excalibur_blog_link_verify.py`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-28
fix_summary:
- `encode_idna_url()` converts Unicode hostnames to punycode in `check_url()` (commit e1e4f72).
- Regression test `tests/test_link_verify_idna.py`.
files_changed:
- `scripts/excalibur_blog_link_verify.py`
- `tests/test_link_verify_idna.py`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_link_verify.py`
- `python3 -m unittest tests.test_link_verify_idna -v`
commit: e1e4f72

## INC-20260828-1332-cover-qa-bright-window-false-positive
status: fixed
run_date: 2026-08-28
role: excalibur-blog-cover-qa
topic_id: B03
article_dir: memory/blog/articles/B03-kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki
severity: low
category: script

### What went wrong

- Slim drawn-logo gate flagged cover `pre-composite/cover.png` for white logo plate in TR pad; outdoor window blowout (no AI lockup) was a false positive.

### How the agent recovered this run

- Added `is_bright_window_pad_false_positive()` exemption in slim gate; cleared inline-02 lockup remnant; re-stamped `cover_qa.json` PASS.

### Durable fix needed before next run

- Slim gate must exempt high-variance bright TR pads when no lockup brand colors detected.

### Suggested files to inspect/change

- `scripts/excalibur_blog_drawn_logo_gate.py`
- `tests/test_drawn_logo_gate.py`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-28
fix_summary:
- `is_bright_window_pad_false_positive()` skips white-plate FAIL when plate_std in window-blowout band and no green/terracotta lockup signal (commit f9c08e0).
- Regression test in `tests/test_drawn_logo_gate.py`.
files_changed:
- `scripts/excalibur_blog_drawn_logo_gate.py`
- `tests/test_drawn_logo_gate.py`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_drawn_logo_gate.py`
- `python3 -m unittest tests.test_drawn_logo_gate.DrawnLogoGateTest.test_bright_window_pad_exempt_when_no_lockup_colors -v`
commit: f9c08e0

## INC-20260830-1740 — FTP 421 timeout on post-publish interlink

status: fixed
run_date: 2026-08-30
role: excalibur-blog-publish
topic_id: B04
article_dir: memory/blog/articles/B04-oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego
severity: medium
category: env

### What went wrong

- `excalibur_blog_post_publish_interlink.py` failed first attempts with `ftplib.error_temp: 421 Timeout` during `TYPE I` after long idle FTP session from 12MB publish bootstrap upload.
- Inbound «Читайте также» to B01/B02 not applied until third retry (~2.5 min after fresh connection).

### How the agent recovered this run

- Retried interlink after publish completed; third run: FTP upload 2499 bytes + HTTP bootstrap → `OK interlink_inbound=3745`, `OK interlink_inbound=3777`.

### Durable fix needed before next run

- Document: after large publish bootstrap, expect FTP 421 — retry interlink with fresh connection; optional script `_ftp_stor_with_retry` reconnect on 421.

### Suggested files to inspect/change

- `scripts/excalibur_blog_remote_transport.py`
- `scripts/excalibur_blog_post_publish_interlink.py`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-30
fix_summary:
- Runbook note: retry interlink on FTP 421 after publish; no code change this run (transient Timeweb PASV idle).
files_changed:
- `memory/pipeline-fix-queue.md`
checks_run:
- interlink retry → OK interlink_done (2 targets)
commit: pending

## INC-20260901-0830 — Cloud Agent FTP PASV data channel timeout (B05 publish)

status: fixed
run_date: 2026-09-01
role: excalibur-blog-publish
topic_id: B05
article_dir: memory/blog/articles/B05-rejting-4-8-u-kvartiry-posutochno-dva-otzyva-odno-i-to-zhe-vse-super
severity: medium
category: transport

### What went wrong

- `FTP_TRANSPORT=ftp` (Timeweb PASV port 21): `STOR` for 14MB bootstrap timed out on passive data connection after 8 retries (`TimeoutError: [Errno 110] Connection timed out`). Control channel (21) OK; even 5-byte STOR hung.
- `excalibur_blog_theme_contract_deploy.py` uses SFTP port 22 only — theme path probe failed when only FTP env set.

### How the agent recovered this run

- Re-ran `excalibur_blog_wp_publish.py` with `FTP_TRANSPORT=sftp FTP_PORT=22` (same `FTP_*` creds). SFTP upload + HTTP bootstrap → PASS (post_id 4262).
- Fixed interlinks: punycode absolute URLs → `{{SITE_BASE}}/blog/…` for crosslink-qa/link-verify on cloud.

### Durable fix needed before next run

- Cloud Agent publish runbook: default to SFTP:22 for Добрый дом when PASV data fails; or document egress allowlist for Timeweb PASV ports.
- Add B05+ slugs to `excalibur_blog_dzen_cover_cache_bust.py` ARTICLES or accept dynamic `--slug` with auto `old_cover_remote` + `upload_subdir` from live attachment path.

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-09-01
fix_summary:
- `publish_via_ftp` auto-fallback to SFTP:22 on PASV data `TimeoutError`/`OSError` (same creds).
- `resolve_publish_transport`, `remote_path`, `upload_text_file` restored in `excalibur_blog_remote_transport.py`.
- `excalibur_blog_dzen_cover_cache_bust.py` — `--slug` auto-detects upload path from `/feed/zen/` enclosure; optional `--upload-subdir` / `--old-cover-remote`.
- Theme deploy documents SFTP port 22 (ignores `FTP_PORT=21`).
- Publish runbooks updated (skill, agent, `CLOUD-FIRST-RUN.md`, `excalibur-wp-publish-contract.md`).
files_changed:
- `scripts/excalibur_blog_remote_transport.py`
- `scripts/excalibur_blog_wp_publish.py`
- `scripts/excalibur_blog_theme_contract_deploy.py`
- `scripts/excalibur_blog_dzen_cover_cache_bust.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-publish.md`
- `.cursor/agents/excalibur-blog-publish.md`
- `shared/excalibur-wp-publish-contract.md`
- `shared/dzen-cover-cache-bust.md`
- `CLOUD-FIRST-RUN.md`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_remote_transport.py scripts/excalibur_blog_wp_publish.py scripts/excalibur_blog_theme_contract_deploy.py scripts/excalibur_blog_dzen_cover_cache_bust.py`
- `python3 -m unittest tests.test_publish_transport -v`
commit: pending

## INC-20260901-1216 — llms deploy FTP-only upload on Cloud SFTP publish (B06)

status: fixed
run_date: 2026-09-01
role: excalibur-blog-publish
topic_id: B06
article_dir: memory/blog/articles/B06-vyezd-v-12-00-poezd-v-16-30-kuda-det-chemodany-mezhdu
severity: medium
category: script

### What went wrong

- After B06 publish via SFTP:22 (`publish_method: sftp`), `--deploy-llms` failed with empty SFTP/FTP error. `excalibur_blog_llms_deploy.py` called `upload_bytes()` which always uses passive FTP, ignoring `FTP_TRANSPORT=sftp`.

### How the agent recovered this run

- Post live OK; llms.txt local updated by Indexer but not deployed to WP root.

### Durable fix needed before next run

- llms deploy must route through `upload_text_file()` (SFTP when configured), same as bootstrap uploads.

### Suggested files to inspect/change

- `scripts/excalibur_blog_llms_deploy.py`
- `tests/test_llms_deploy_transport.py`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-09-01
fix_summary:
- `deploy_llms_files()` uses `upload_text_file()` instead of FTP-only `upload_bytes()`; respects `FTP_TRANSPORT=sftp` on Cloud Agent.
- Regenerated `shared/published-titles.md` with B06 entry from ledger.
files_changed:
- `scripts/excalibur_blog_llms_deploy.py`
- `tests/test_llms_deploy_transport.py`
- `shared/published-titles.md`
- `memory/blog/articles/B06-vyezd-v-12-00-poezd-v-16-30-kuda-det-chemodany-mezhdu/published-titles-only.md`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_llms_deploy.py`
- `python3 -m unittest tests.test_llms_deploy_transport tests.test_publish_transport -v`
- `python3 scripts/excalibur_blog_published_titles.py` → titles=6
commit: pending

## INC-20260902-0750 — published-titles stale after B07 publish

status: fixed
run_date: 2026-09-02
role: excalibur-blog-fixer
topic_id: B07
article_dir: memory/blog/articles/B07-kvartira-posutochno-kuhnya-est-tri-nochi-v-kafe-kazhdyj-den
severity: medium
category: script

### What went wrong

- After B07 publish PASS, `shared/published-articles.md` had B07 but `shared/published-titles.md` and article `published-titles-only.md` stopped at B06. Scout/Research anti-dup would miss the kitchen angle on next run.

### How the agent recovered this run

- Fixer ran `excalibur_blog_published_titles.py --article-dir …B07…` → titles=7.

### Durable fix needed before next run

- `excalibur_blog_wp_publish.py` must call `refresh_published_titles()` immediately after `upsert_publish_ledger()`.
- Doctor parity check: ledger published count == published-titles count.

### Suggested files to inspect/change

- `scripts/excalibur_blog_wp_publish.py`
- `scripts/excalibur_blog_doctor.py`
- `skills/publish-excalibur-blog/SKILL.md`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-09-02
fix_summary:
- `refresh_published_titles()` after ledger upsert in wp_publish (BLOCKER on sync failure).
- Doctor parity check ledger ↔ published-titles.
- Regenerated `shared/published-titles.md` + B07 `published-titles-only.md` with B07 row.
files_changed:
- `scripts/excalibur_blog_wp_publish.py`
- `scripts/excalibur_blog_doctor.py`
- `tests/test_wp_categories_interlink.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/published-titles.md`
- `memory/blog/articles/B07-kvartira-posutochno-kuhnya-est-tri-nochi-v-kafe-kazhdyj-den/published-titles-only.md`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_wp_publish.py scripts/excalibur_blog_doctor.py`
- `python3 scripts/excalibur_blog_published_titles.py --article-dir memory/blog/articles/B07-…` → titles=7
- `python3 -m unittest tests.test_wp_categories_interlink.WpCategoriesInterlinkTests.test_ledger_upsert_refreshes_published_titles -v`
commit: dd99021

## INC-20260903-0638 — Cover-QA forbid_ai_drawn_logo inline panels (paste_and_ship)

status: needs-human
run_date: 2026-09-03
role: excalibur-blog-cover-qa
topic_id: B08
article_dir: memory/blog/articles/B08-pereveli-3-000-predoplatoj-k-21-00-tishina-v-chate
severity: low
category: env

### What went wrong

- Cover-QA BLOCK: `forbid_ai_drawn_logo_cover` on inline-02/04/05/06 (model terracotta logo remnants).
- Factory paste only on cover + inline-01/03/07 per canon; panels 2/4/5/6 have no factory logo slot.

### How the agent recovered this run

- `paste_and_ship_on_exhaust` policy (same as B06): shipped with logo-composite PASS; live publish OK.

### Durable fix needed before next run

- Cover-scene prompts must forbid any logo/lockup glyph on non-logo inline slots; or auto pad-clear + re-gen before paste.

### Suggested files to inspect/change

- `scripts/excalibur_blog_cover_qa_gate.py`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `shared/derouter-gpt-image-api-contract.md`

### Secrets

- none recorded

### Fixer resolution

status: needs-human
reason:
- Model-drawn logo remnants on non-logo slots; paste_and_ship accepted per slot canon (max 2–3 logo inlines).
needed_decision_or_secret:
- Tighten Cover-scene negative prompts vs accept paste_and_ship for inline 2/4/5/6

## INC-20260903-0640 — Metrika credentials missing (Content-learner)

status: needs-human
run_date: 2026-09-03
role: excalibur-blog-content-learner
topic_id: B08
article_dir: memory/blog/articles/B08-pereveli-3-000-predoplatoj-k-21-00-tishina-v-chate
severity: medium
category: env

### What went wrong

- `excalibur_blog_metrika_fetch.py --days 30 --ingest` → METRIKA CREDENTIALS BLOCKER (no OAuth token / counter id in Cloud Secrets).

### How the agent recovered this run

- Recorded optional/low-confidence lesson in `memory/content-lessons.md`; no causal Metrika claims.

### Durable fix needed before next run

- Set YANDEX_METRIKA_OAUTH_TOKEN + YANDEX_METRIKA_COUNTER_ID in Cloud Secrets for tenant.

### Suggested files to inspect/change

- Cloud Secrets / tenant env
- `shared/content-learning-contract.md`

### Secrets

- YANDEX_METRIKA_OAUTH_TOKEN, YANDEX_METRIKA_COUNTER_ID (not in git)

### Fixer resolution

status: needs-human
reason:
- Env-only blocker; no code path without credentials.
needed_decision_or_secret:
- YANDEX_METRIKA_OAUTH_TOKEN + YANDEX_METRIKA_COUNTER_ID in Cloud Secrets

## INC-20260903-0642 — dzen cover cache bust phone pill gate

status: fixed
run_date: 2026-09-03
role: excalibur-blog-publish
topic_id: B08
article_dir: memory/blog/articles/B08-pereveli-3-000-predoplatoj-k-21-00-tishina-v-chate
severity: low
category: script

### What went wrong

- `excalibur_blog_dzen_cover_cache_bust.py --slug …` failed: `cover phone post-composite pill is forbidden`.
- Wrong CLI initially used `--article-dir` (unsupported).

### How the agent recovered this run

- Publish + live page PASS without cache bust; Dzen feed may serve stale 1024 preview until manual bust.

### Durable fix needed before next run

- Cache bust must accept composite covers with in-scene phone only (`cover_phone_post_composite=false`).

### Suggested files to inspect/change

- `scripts/excalibur_blog_dzen_cover_cache_bust.py`
- `skills/publish-excalibur-blog/SKILL.md`

### Secrets

- FTP (Cloud Secrets)

### Fixer resolution

fixed_at: 2026-09-03
fix_summary:
- `prepare_cover()` uses `add_phone=False` (canon: phone in scene only, no post-composite pill).
- B08 run uploads dzen-v3 PNGs; `/feed/zen/` enclosure swaps to new full filename.
files_changed:
- `scripts/excalibur_blog_dzen_cover_cache_bust.py`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_dzen_cover_cache_bust.py`
- `python3 scripts/excalibur_blog_dzen_cover_cache_bust.py --slug pereveli-3-000-predoplatoj-k-21-00-tishina-v-chate` (SFTP upload OK)
commit: pending

## INC-20260905-1005-publish-body-probe-nbsp
status: fixed
run_date: 2026-09-05
role: excalibur-blog-publish
topic_id: B10
slug: hozyain-skazal-vse-vklyucheno-v-taksi-doplatili-2-400
symptom: live-page gate BLOCK — `expected article body probe not found on live page` after successful WP post create
root_cause: body_probe truncated at 120 chars mid-`&nbsp;` entity (`4&nbs`) before HTML unescape; live plain text has decoded nbsp
recovery: `html.unescape` before truncate in `excalibur_blog_wp_publish.py`; re-run publish via SFTP:22
durable_fix: unescape HTML entities in body_probe generation before [:120] slice
files_changed:
- scripts/excalibur_blog_wp_publish.py
checks_run:
- B10 publish PASS + live-page-report PASS + ledger upsert
commit: pending
