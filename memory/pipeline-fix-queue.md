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

## INC-20260826-1257 — link_verify latin-1 on Cyrillic URLs

status: fixed
run_date: 2026-08-26
role: excalibur-blog-publish
topic_id: B03
article_dir: memory/blog/articles/B03-vyezd-v-12-00-poezd-v-16-30-chemodany-ne-v-taksi
severity: medium
category: script

### What went wrong

- Preflight `excalibur_blog_link_verify.py` raised `UnicodeEncodeError: 'latin-1' codec can't encode characters` on CTA hrefs with Unicode host `https://добрыйдом-72.рф/` and `/booking/`.
- `structure-gate` / `crosslink_qa` failed on same HTTP path.

### How the agent recovered this run

- Publish workaround: rewrote same-site CTA to relative `/` and `/booking/` in `article.html` so link_verify could run.

### Durable fix needed before next run

- Encode IDN hostnames to punycode before urllib HTTP checks; allow absolute Cyrillic CTA without manual relative rewrite.

### Suggested files to inspect/change

- `scripts/excalibur_blog_link_verify.py`
- `scripts/excalibur_blog_site_base.py`
- `shared/excalibur-wp-publish-contract.md`
- `skills/publish-excalibur-blog/SKILL.md`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-26
fix_summary:
- Added `normalize_url_for_http()` in `excalibur_blog_site_base.py` (IDNA punycode before HTTP).
- `excalibur_blog_link_verify.check_url` uses punycode host; Cyrillic CTA no longer needs relative rewrite.
files_changed:
- `scripts/excalibur_blog_site_base.py`
- `scripts/excalibur_blog_link_verify.py`
- `tests/test_link_verify_idna.py`
- `shared/excalibur-wp-publish-contract.md`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_site_base.py scripts/excalibur_blog_link_verify.py`
- `python3 -m unittest tests.test_link_verify_idna -v`
- E2E link_verify on Cyrillic href → verdict pass
commit: bf563b1

## INC-20260826-1258 — cover QA white plate on pre-composite

status: fixed
run_date: 2026-08-26
role: excalibur-blog-cover
topic_id: B03
article_dir: memory/blog/articles/B03-vyezd-v-12-00-poezd-v-16-30-chemodany-ne-v-taksi
severity: medium
category: script

### What went wrong

- First canvas-quad-01 generation left white logo plate/card in TOP-RIGHT pad on `cover/pre-composite/cover.png`; Cover-QA / drawn_logo gate caught it after composite attempt.

### How the agent recovered this run

- Regenerated canvas-1 with stronger empty-pad prompt; factory logo paste on cover + inline-01/03/07; `cover_qa.json` PASS.

### Durable fix needed before next run

- Block logo composite when pre-composite pad has white/gray plate; strengthen default cover TL prompt for empty TOP-RIGHT pad.

### Suggested files to inspect/change

- `scripts/excalibur_blog_brand_logo_composite.py`
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `skills/cover-excalibur-blog/SKILL.md`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-26
fix_summary:
- `assert_no_white_plate_before_paste()` blocks factory logo paste when pad has white/gray plate.
- Default cover TL prompt: TOP-RIGHT = empty bright wall ONLY; phone vertical on right margin.
files_changed:
- `scripts/excalibur_blog_brand_logo_composite.py`
- `scripts/excalibur_blog_cover_quad_prompt.py`
- `tests/test_drawn_logo_gate.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_brand_logo_composite.py scripts/excalibur_blog_cover_quad_prompt.py`
- `python3 -m unittest tests.test_drawn_logo_gate.DrawnLogoGateTest.test_composite_blocks_white_plate_before_paste -v`
commit: 8651ae0
