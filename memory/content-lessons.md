# Excalibur BLOG — content lessons

Active learning memory (v2 contract). Review-only — do not auto-apply to Writer prompt.

## LESSON-20260822-1307-B03-dogovor-preoplat-hook
status: proposed
topic_id: B03
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json absent; gate SKIP per human-first-v2
- artifact: title-brief.json
  finding: PASS — pain-scene H1 «7 запретов», P0 «договор аренды квартиры» (Tyumen 1974) вынесен в тело, не в сырой SEO-заголовок
- artifact: description-brief.json
  finding: PASS — Klyshin case hook (оплата до чтения оферты), geo Тюмень, не дублирует H1
- artifact: interlink-gate.json + link-verify.json
  finding: PASS — 2 outbound sibling links (B01 бесконтакт, B02 залог), все ссылки 200
- artifact: wp-publish-result.json / live-page-report.json
  finding: live-page gate BLOCK — JSON-LD/FAQ/container mismatch on live (systemic; same pattern as B01); blocks on-site verification, not a prose verdict
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (fetch failed; no pageviews/bounce sample)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS
- LOW_SAMPLE
- ASSUMED_BEHAVIOR (live-page QA cannot confirm schema/FAQ until publish/theme fix)

### Keep
- Нумерованный чеклист «7 пунктов» как spine статьи — согласован с H1 и description hook.
- Buyer-жаргон посуточного найма (оферта, акцепт, залог, часы заезда) без термин-дампа в лиде.
- Локализация Тюмень + естественное вшивание P0 Wordstat в середину текста.
- Контекстные sibling-ссылки на B01/B02 внутри списка условий.

### Change
- После появления Metrika credentials — повторить ingest за 30 дней и сопоставить bounce/duration с длиной чеклиста и opening hook.
- Дождаться fixer/publish по live-page gate (JSON-LD, article-content container) перед выводами о FAQ/schema на live.

### Never again
- Не делать причинных выводов о hook/retention без Metrika sample.
- Не выдумывать content-evidence-report.json или Metrika rows при SKIP/blocker.

### Proposed apply
- Review-only: при повторе «N пунктов» + pre-payment hook в ≥2 статьях с сильным Metrika engagement — зафиксировать в `memory/content-meta-ab-learnings.md` (не Writer).
- Writer prompt не менять автоматически.

### Durable applied
- none

### Resolution
status: recorded
