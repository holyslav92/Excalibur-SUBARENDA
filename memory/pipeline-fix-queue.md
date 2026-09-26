# Pipeline fix queue

## INC-20260926-0937-schema-derouter-output-path
status: open
run_date: 2026-09-26
role: excalibur-blog-schema
article: memory/blog/articles/B03-zaselilsya-posutochno-v-dushe-ledyanaya-voda-a-bojler-molchit
symptom: `excalibur_blog_derouter_opus_chat.py --output schema.jsonld --article-dir memory/blog/articles/...` wrote JSON-LD to repo root `schema.jsonld`, not under article_dir.
workaround: `mv schema.jsonld` into article dir, or pass `--output memory/blog/articles/<slug>/schema.jsonld`.
follow_up: resolve `--output` relative to `--article-dir` when basename only (skill canon).
secondary: Derouter Terra put `sameAs` with `{{SITE_BASE}}/blog/` → schema_gate FAIL (any `/blog/` in file). Stripped sameAs; match B01 author shape.
