# Content lessons — Excalibur BLOG

## LESSON-20260825-0600-B04-gvs-posutochno
status: proposed
topic_id: B04
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json absent; gate SKIP
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID not set in env)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Klyshin hook utilities_counters → Wordstat rework на «нет горячей воды в квартире» (2494 RF) дал сильный buyer-intent без привязки «Тюмень» в H1.
- Чеклист «5 вопросов до оплаты» + TG после чеклиста — воронка в теле, не простыня.
- Летняя ванная/кран на обложке (август YEKT), без зимнего героя.

### Change
- (optional, low-confidence) При публикации ЖКХ/ГВС-тем усилить inline-схему «бойлер vs центральная» — читательский запрос «что делать» 215 RF.

### Never again
- Публиковать без проверки 7 inline URL на live (wp-content, не cover/).

### Proposed apply
- review-only; durable apply после повторения паттерна или Metrika feedback

### Rollback
- n/a (no durable apply)
