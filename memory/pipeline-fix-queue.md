# Pipeline fix queue

## INC-20260926-0937-schema-derouter-output-path
status: fixed
fixed_at: 2026-09-26
run_date: 2026-09-26
role: excalibur-blog-schema
topic_id: B03
article_dir: memory/blog/articles/B03-zaselilsya-posutochno-v-dushe-ledyanaya-voda-a-bojler-molchit
severity: medium
category: script

### What went wrong
- `excalibur_blog_derouter_opus_chat.py --output schema.jsonld --article-dir …` wrote JSON-LD to repo root.

### How the agent recovered this run
- `mv schema.jsonld` into article dir or full path in `--output`.

### Durable fix needed before next run
- Resolve bare `--output` via `resolve_article_output()` when `--article-dir` set.

### Suggested files to inspect/change
- `scripts/excalibur_blog_derouter_opus_chat.py`
- `skills/schema-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
fix_summary:
- `--output` with `--article-dir` uses `excalibur_repo_paths.resolve_article_output` (same as schema gate).
files_changed:
- `scripts/excalibur_blog_derouter_opus_chat.py`
- `skills/schema-excalibur-blog/SKILL.md`
- `.cursor/skills/schema-excalibur-blog/SKILL.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_derouter_opus_chat.py`
- `tests/test_fixer_b03_contracts.py`
commit: fa72eb0

---

## INC-20260926-1537-cover-qa-logo-pad-gate
status: fixed
fixed_at: 2026-09-26
run_date: 2026-09-26
role: excalibur-blog-cover-qa
topic_id: B03
article_dir: memory/blog/articles/B03-zaselilsya-posutochno-v-dushe-ledyanaya-voda-a-bojler-molchit
severity: high
category: script

### What went wrong
- Cover-QA FAIL: `forbid_ai_drawn_logo_pre_composite`, `forbid_logo_white_plate` after regen; manual `clear_logo_pad` on pre-composite insufficient.

### How the agent recovered this run
- Partial opencv scrub + return to Cover for regen.

### Durable fix needed before next run
- Auto pad scrub + second pass before factory logo paste in `excalibur_blog_brand_logo_composite.py`.

### Suggested files to inspect/change
- `scripts/excalibur_blog_brand_logo_composite.py`
- `skills/cover-excalibur-blog/SKILL.md`

### Secrets
- none recorded

### Fixer resolution
fix_summary:
- `scrub_generation_logo_pad()` on pre-composite before paste; retry full pad inpaint when drawn lockup still detected.
files_changed:
- `scripts/excalibur_blog_brand_logo_composite.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_brand_logo_composite.py`
commit: 20f94c1

---

## INC-20260926-1537-grsai-image-404-regen
status: fixed
fixed_at: 2026-09-26
run_date: 2026-09-26
role: excalibur-blog-cover
topic_id: B03
article_dir: memory/blog/articles/B03-zaselilsya-posutochno-v-dushe-ledyanaya-voda-a-bojler-molchit
severity: blocker
category: api

### What went wrong
- Cover regen via GRSAI hit HTTP 404: `grsaiapi.com/openai/v1/images/generations` (wrong path).

### How the agent recovered this run
- Used existing panels / manual scrub; probe logged in `memory/blog/derouter-image-base-probe.json`.

### Durable fix needed before next run
- Image provider base normalization → `/v1` not `/openai/v1`; alternate provider key + default host `/v1` in image base candidates.

### Suggested files to inspect/change
- `scripts/excalibur_blog_derouter_gpt_image2_api.py`
- `shared/derouter-gpt-image-api-contract.md`

### Secrets
- none recorded

### Fixer resolution
fix_summary:
- `normalize_api_base()` GRSAI host branch; per-host API key; GRSAI bases prepended when GRSAI key env set.
files_changed:
- `scripts/excalibur_blog_derouter_gpt_image2_api.py`
- `shared/derouter-gpt-image-api-contract.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_derouter_gpt_image2_api.py`
- `tests/test_fixer_b03_contracts.py`
commit: fa72eb0

---

## INC-20260926-1537-interlink-ledger-live-catalog
status: fixed
fixed_at: 2026-09-26
run_date: 2026-09-26
role: excalibur-blog-writer
topic_id: B03
article_dir: memory/blog/articles/B03-zaselilsya-posutochno-v-dushe-ledyanaya-voda-a-bojler-molchit
severity: medium
category: script

### What went wrong
- Outbound interlink gate saw only ledger siblings (B01/B02) while article linked live-catalog slugs; crosslink QA used `memory/live-catalog.json` (96 posts).

### How the agent recovered this run
- crosslink-qa PASS; interlink-gate PASS with one ledger slug only in report titles.

### Durable fix needed before next run
- Merge `memory/live-catalog.json` into `all_interlink_candidates()` for outbound gate + Writer sibling pool.

### Suggested files to inspect/change
- `scripts/excalibur_blog_interlink_lib.py`
- `shared/interlink-contract.md`

### Secrets
- none recorded

### Fixer resolution
fix_summary:
- `load_live_catalog_posts()` merged into interlink candidates (source `live_catalog`); contract updated.
files_changed:
- `scripts/excalibur_blog_interlink_lib.py`
- `shared/interlink-contract.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_interlink_lib.py`
- `tests/test_fixer_b03_contracts.py`
commit: fa72eb0
