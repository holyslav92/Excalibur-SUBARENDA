# Pipeline fix queue

## INC-20260824-1050 — Metrika credentials missing (Content-learner B03)

- **Symptom:** `excalibur_blog_metrika_fetch.py --days 30 --ingest` exits 2 with `METRIKA CREDENTIALS BLOCKER`; no `memory/analytics/metrika-latest.json`.
- **Cause:** `YANDEX_METRIKA_OAUTH_TOKEN` and `YANDEX_METRIKA_COUNTER_ID` not set in Cloud Secrets/env; `memory/site.env.local` absent.
- **Fix:** tenant adds OAuth token (`metrika:read`) + counter id to Cloud Secrets; re-run Metrika fetch after publish.
- **Status:** open — blocks Metrika feedback loop for B03 Content-learner; evidence gate SKIP is normal.

## INC-20260824-1038 — live-page gate /blog permalink vs schema URL

- **Symptom:** `live BlogPosting JSON-LD URL does not exactly match permalink` after successful FTP publish (B03).
- **Cause:** WP permalink `/blog/{slug}/` vs schema `{{SITE_BASE}}/{slug}/` (schema-gate forbids `/blog/` in committed JSON-LD).
- **Fix:** `scripts/excalibur_blog_live_page_gate.py` — `_canonical_article_path()` normalizes optional `/blog/` prefix before comparing permalink vs JSON-LD.
- **Status:** fixed in repo; re-run live gate PASS for B03.

## INC-20260824-1042 — llms deploy ImportError

- **Symptom:** `excalibur_blog_llms_deploy.py` ImportError: `resolve_publish_transport` missing from `excalibur_blog_remote_transport`.
- **Fix:** use `upload_bytes` + `transport_mode` from remote transport module.
- **Status:** fixed in repo; FTP upload may hang on large llms-full.txt (monitor separately).
