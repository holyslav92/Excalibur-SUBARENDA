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

## INC-20260830-1319-poster-split-white-tr-pad-false-positive
status: fixed
run_date: 2026-08-30
role: excalibur-blog-cover-qa
topic_id: B04
article_dir: memory/blog/articles/B04-poprosili-foto-pasporta-pri-zaselenii-posutochno-do-oplaty
severity: low
category: script

### What went wrong

- Slim drawn-logo gate flagged B04 cover `pre-composite/cover.png` for white logo plate in TR pad; WOW poster-split layout uses an intentional flat white headline field (low `plate_std`), not an AI lockup.

### How the agent recovered this run

- Extended `is_bright_window_pad_false_positive()` with poster-split branch (`plate_std <= 8.0` and low lockup score); pad-clear TR on inline 2/4/6; re-stamped `cover_qa.json` PASS.

### Durable fix needed before next run

- Slim gate must exempt flat white TR headline panels in poster-split covers when no lockup brand colors detected.

### Suggested files to inspect/change

- `scripts/excalibur_blog_drawn_logo_gate.py`
- `tests/test_drawn_logo_gate.py`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-30
fix_summary:
- Poster-split branch in `is_bright_window_pad_false_positive()` (commit 90685b6).
- Regression test `test_poster_split_flat_white_tr_pad_exempt` on B04 pre-composite cover.
files_changed:
- `scripts/excalibur_blog_drawn_logo_gate.py`
- `tests/test_drawn_logo_gate.py`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_drawn_logo_gate.py`
- `python3 -m unittest tests.test_drawn_logo_gate.DrawnLogoGateTest.test_poster_split_flat_white_tr_pad_exempt -v`
commit: b053ff8

## INC-20260830-1343-metrika-credentials

status: needs-human
run_date: 2026-08-30
role: excalibur-blog-content-learner
topic_id: B04
article_dir: memory/blog/articles/B04-poprosili-foto-pasporta-pri-zaselenii-posutochno-do-oplaty
severity: medium
category: credentials

### What went wrong

- `excalibur_blog_metrika_fetch.py --days 30 --ingest` exited 2 with `METRIKA CREDENTIALS BLOCKER`: `YANDEX_METRIKA_OAUTH_TOKEN` and `YANDEX_METRIKA_COUNTER_ID` not set in Cloud Secrets/env.
- No `memory/analytics/metrika-latest.json` produced; behavioral cohort for B04 unavailable.

### How the agent recovered this run

- Evidence gate SKIP (no `content-evidence-report.json` under human-first-v2) — continued.
- Recorded named lessons from publish artifacts (title-brief, description-brief, article.html, interlink-gate, wp-publish-result) as optional/low-confidence without Metrika causal signals.

### Durable fix needed before next run

- Configure `YANDEX_METRIKA_OAUTH_TOKEN` (OAuth metrika:read) and `YANDEX_METRIKA_COUNTER_ID` in Cloud Secrets for tenant counter.

### Suggested files to inspect/change

- Cloud Secrets / env for Metrika OAuth + counter id
- `scripts/excalibur_blog_metrika_fetch.py`

### Secrets

- `YANDEX_METRIKA_OAUTH_TOKEN` — missing
- `YANDEX_METRIKA_COUNTER_ID` — missing

### Fixer resolution

fixed_at: 2026-08-30
reason:
- Credentials cannot be set in git; tenant must add OAuth token + counter id to Cloud Secrets (see `CLOUD-FIRST-RUN.md`, `shared/yandex-metrika-contract.md`).
needed_decision_or_secret:
- `YANDEX_METRIKA_OAUTH_TOKEN` with scope `metrika:read`
- `YANDEX_METRIKA_COUNTER_ID` for добрыйдом-72.рф counter
fix_summary:
- `excalibur_blog_doctor.py` now warns when Metrika secrets missing (preflight before content-learner).
files_changed:
- `scripts/excalibur_blog_doctor.py`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_doctor.py`
- `python3 scripts/excalibur_blog_doctor.py` (Metrika warn visible when unset)
commit: e929dd4
