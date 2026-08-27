# Excalibur BLOG — content lessons (review-only)

Proposals for human review. Content-learner does not auto-edit Writer prompt or `article.html`.

---

## LESSON-20260827-1136-B03-metrika-credentials-blocker
status: active
topic_id: B03
category: other
confidence: high

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json absent — expected under human-first-v2
- metrika_signal: METRIKA CREDENTIALS BLOCKER — `excalibur_blog_metrika_fetch.py --days 30 --ingest` exit 2; YANDEX_METRIKA_OAUTH_TOKEN and YANDEX_METRIKA_COUNTER_ID unset in Cloud Secrets/env

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS

### Keep
- Mandatory Metrika ingest step before lesson causal claims; do not invent pageviews/bounce from publish artifacts

### Change
- Add `YANDEX_METRIKA_OAUTH_TOKEN` (scope metrika:read) and `YANDEX_METRIKA_COUNTER_ID` to Cursor Cloud Secrets per `shared/yandex-metrika-contract.md`; re-run Content-learner for B03 after credentials land

### Never again
- Silent skip of Metrika on post-publish Content-learner runs
- Fabricating `memory/analytics/metrika-latest.json` or site-feedback rows when API/credentials fail

### Proposed apply
- Cloud Secrets: Yandex Metrika OAuth + counter id for Добрый дом site
- Re-run: `python3 scripts/excalibur_blog_metrika_fetch.py --days 30 --ingest`

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260827-1136-B03-reviews-angle-pipeline
status: proposed
topic_id: B03
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: no content-evidence-report.json; pipeline gates only
- artifact: title-brief.json
  finding: Klyshin pain-scene H1 «Выбрал квартиру с оценкой 4,8. Перед оплатой нашёл одинаковые отзывы»; demand spine «суточно ру отзывы» (3715 RF) held under H1, not raw in title
- artifact: description-brief.json
  finding: Dzen card distinct from H1 — «Хвалебные тексты идут под копирку…»; rhythm klyshin_case_hook; verdict PASS
- artifact: interlink-gate.json + crosslink-qa-gate.json
  finding: 3 contextual outbound siblings (B01 check-in, B02 deposit, hidden fees); HTTP 200 on relative `/blog/` hrefs
- artifact: live-page-report.json
  finding: live-page gate PASS post publish (wp_post_id 4052)
- metrika_signal: none — Metrika ingest blocked; no visits/bounce/duration for B03 cohort

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS
- LOW_SAMPLE (no on-site behavioral data yet)

### Keep
- Scout reviews/отзывы angle: concrete guest action + twist (4,8 vs identical «всё супер») without SEO tail in H1
- Description as separate Dzen hook (копипаста / низкие оценки) — not title duplicate
- Relative `/blog/` internal hrefs for link-verify and crosslink QA on Cyrillic host
- Outbound interlink cluster: pre-payment checks (check-in codes, deposit, hidden fees) around reviews topic

### Change
- After Metrika credentials: compare B03 bounce/duration vs B01/B02 guest-advice cluster; validate whether long checklist closing (5–10 min order) retains readers or spikes bounce
- Monitor llms-full.txt FTP deploy (failed Illegal PORT on first publish run per wp-publish-log) — separate transport incident, not content verdict

### Never again
- Cyrillic absolute blog URLs in `article.html` hrefs (broke verify on this tenant)
- Causal CTR/retention claims for reviews angle without Metrika cohort row for slug `na-kartochke-posutochno-4-8-dva-odinakovyh-vse-super`

### Proposed apply
- Scout: keep Klyshin×Wordstat reviews cluster for future B-series when Metrika confirms engagement
- Publish/transport: ensure llms-full deploy path stable (see INC-20260827-0815-publish-ftp-pasv-bootstrap)

### Durable applied
- none — single run, evidence SKIP, Metrika blocked; no ≥2-run pattern

### Resolution
status: recorded
