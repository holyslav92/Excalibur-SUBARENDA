# Pipeline fix queue

## INC-20260824-1038 — live-page gate /blog permalink vs schema URL

- **Symptom:** `live BlogPosting JSON-LD URL does not exactly match permalink` after successful FTP publish (B03).
- **Cause:** WP permalink `/blog/{slug}/` vs schema `{{SITE_BASE}}/{slug}/` (schema-gate forbids `/blog/` in committed JSON-LD).
- **Fix:** `scripts/excalibur_blog_live_page_gate.py` — `_canonical_article_path()` normalizes optional `/blog/` prefix before comparing permalink vs JSON-LD.
- **Status:** fixed in repo; re-run live gate PASS for B03.

## INC-20260824-1042 — llms deploy ImportError

- **Symptom:** `excalibur_blog_llms_deploy.py` ImportError: `resolve_publish_transport` missing from `excalibur_blog_remote_transport`.
- **Fix:** use `upload_bytes` + `transport_mode` from remote transport module.
- **Status:** fixed in repo; FTP upload may hang on large llms-full.txt (monitor separately).
