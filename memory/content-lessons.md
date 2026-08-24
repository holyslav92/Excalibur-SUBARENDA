# Content lessons — Excalibur BLOG (review-only)

Proposals for durable pipeline changes. Writer prompt protected — apply only after human review.

---

## LESSON-20260824-1050-B03-metrika-feedback-missing
status: proposed
topic_id: B03
category: other
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: `content-evidence-report.json` absent; gate `content-evidence-gate.json` → SKIP (optional under human-first-v2).
- metrika_signal: none — `excalibur_blog_metrika_fetch.py --days 30 --ingest` → METRIKA CREDENTIALS BLOCKER (no `YANDEX_METRIKA_OAUTH_TOKEN` / `YANDEX_METRIKA_COUNTER_ID` in env or `memory/site.env.local`).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING
- LOW_SAMPLE (B03 fresh publish 2026-08-24; cohort B01–B03 too small for causal Metrika even after credentials fix)

### Keep
- B03 publish complete: FTP post 3947, live-page gate PASS, cover QA PASS, interlink outbound to B01/B02 siblings.
- «Всё включено» / скрытые доплаты angle aligned with scout hook and wp categories `posutochnaya-arenda` + `zhkh-i-doplaty`.

### Change
- Configure Yandex Metrika OAuth (`metrika:read`) + counter id in Cloud Secrets so Content-learner can ingest `memory/analytics/metrika-latest.json` after each publish.
- After credentials: re-run Metrika ingest for B03 cohort (B01–B03) before claiming retention/CTR lessons.

### Never again
- Do not infer editorial quality or causal CTR/retention for B03 without Metrika ingest or invented `content-evidence-report.json`.
- Do not auto-apply Writer/Sol rule changes from a single Metrika-less publish.

### Proposed apply
- Human: add `YANDEX_METRIKA_OAUTH_TOKEN` and `YANDEX_METRIKA_COUNTER_ID` to Cloud Secrets; optional `memory/site.env.local` for local runs.
- Re-run: `python3 scripts/excalibur_blog_metrika_fetch.py --days 30 --ingest` then refresh this lesson with matched rows for slug `skrytye-doplaty-pri-posutochnoj-arende-ot-hozyaina`.

### Durable applied
- none

### Resolution
status: recorded
