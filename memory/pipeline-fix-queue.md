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

### Suggested files to inspect/change

- `scripts/excalibur_blog_remote_transport.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `shared/excalibur-wp-publish-contract.md`
- `shared/interlink-contract.md`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-27
fix_summary:
- `excalibur_blog_remote_transport.py`: PASV-then-ACTIVE STOR; `_ftp_upload_timeout()` auto-scales 180s/300s for ≥5MB/≥10MB payloads; env `FTP_TIMEOUT` 30–600.
- Publish skill + wp-publish contract document large-bootstrap FTP behavior.
- `shared/interlink-contract.md`: path-only `/blog/{slug}/` hrefs — no Cyrillic absolute host URLs for link-verify.
files_changed:
- `scripts/excalibur_blog_remote_transport.py`
- `skills/publish-excalibur-blog/SKILL.md`
- `.cursor/skills/publish-excalibur-blog/SKILL.md`
- `shared/excalibur-wp-publish-contract.md`
- `shared/interlink-contract.md`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_remote_transport.py`
commit: c8f07f2

## INC-20260827-0820-cover-drawn-logo-pre-composite

status: fixed
run_date: 2026-08-27
role: excalibur-blog-cover
topic_id: B03
article_dir: memory/blog/articles/B03-na-kartochke-posutochno-4-8-dva-odinakovyh-vse-super
severity: medium
category: qa

### What went wrong

- Canvas-01 first split had AI-drawn logo lockup in cover top-right pad (`pre-composite/cover.png`); drawn_logo_gate blocked factory paste until regen + pad-clear.

### How the agent recovered this run

- Regenerated canvas-01; pad-clear top-right pad; factory logo paste on cover + inline 01/03/07; cover_qa.json PASS.

### Durable fix needed before next run

- Standard cover runbook: auto-detect drawn lockup → pad-clear → `--after-pad-clear` composite without live-regen-only script.

### Suggested files to inspect/change

- `scripts/excalibur_blog_cover_logo_pad_clear.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `skills/cover-qa-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-cover.md`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-27
fix_summary:
- New `scripts/excalibur_blog_cover_logo_pad_clear.py` (`--auto-detect`, `--recomposite`).
- Cover + Cover-QA skills/agents document recovery before `brand_logo_composite`.
files_changed:
- `scripts/excalibur_blog_cover_logo_pad_clear.py`
- `skills/cover-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-excalibur-blog/SKILL.md`
- `skills/cover-qa-excalibur-blog/SKILL.md`
- `.cursor/skills/cover-qa-excalibur-blog/SKILL.md`
- `agents/excalibur-blog-cover.md`
- `.cursor/agents/excalibur-blog-cover.md`
- `memory/pipeline-fix-queue.md`
checks_run:
- `python3 -m py_compile scripts/excalibur_blog_cover_logo_pad_clear.py`
commit: 038fc30

## INC-20260827-0604-scout-derouter-mcp-workaround

status: fixed
run_date: 2026-08-27
role: excalibur-blog-scout
topic_id: B03
article_dir: n/a
severity: low
category: docs

### What went wrong

- Scout handoff prose risk: conductor may call `DEROUTER` MCP namespace instead of REST script; canonical path is `excalibur_blog_derouter_opus_chat.py` with assembled Wordstat inputs file.

### How the agent recovered this run

- Director assembled `memory/scout/scout-input-assembled-2026-08-27.md` (live Wordstat facts) + `derouter-opus-stamp-scout.json` via REST script; handoff written to `.cursor/excalibur-blog-handoff.md`.

### Durable fix needed before next run

- Scout agent/skill/derouter contract: REST script only; forbid DEROUTER MCP namespace for scout prose; document assembled-inputs filename pattern.

### Suggested files to inspect/change

- `agents/excalibur-blog-scout.md`
- `skills/scout-excalibur-blog/SKILL.md`
- `shared/derouter-opus-brain-contract.md`

### Secrets

- none recorded

### Fixer resolution

fixed_at: 2026-08-27
fix_summary:
- Scout agent + skill: REST script only; assembled `memory/scout/scout-input-assembled-YYYY-MM-DD.md`; forbid CallDynamicTool DEROUTER MCP.
- `shared/derouter-opus-brain-contract.md`: scout assembled-inputs note.
files_changed:
- `agents/excalibur-blog-scout.md`
- `.cursor/agents/excalibur-blog-scout.md`
- `skills/scout-excalibur-blog/SKILL.md`
- `.cursor/skills/scout-excalibur-blog/SKILL.md`
- `shared/derouter-opus-brain-contract.md`
- `memory/pipeline-fix-queue.md`
checks_run:
- `rg 'CallDynamicTool.*DEROUTER' agents/excalibur-blog-scout.md skills/scout-excalibur-blog/SKILL.md` → forbid documented
commit: 038fc30
