# Content lessons — Добрый дом

Активные и предложенные уроки Content-learner (human-first-v2). Proposals
review-only; Writer prompt не меняется автоматически.

## LESSON-20260826-1257-B03-bagazh-okno-vyezd
status: proposed
topic_id: B03
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; editorial_judgments не собраны в v2-отчёт
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (YANDEX_METRIKA_OAUTH_TOKEN / YANDEX_METRIKA_COUNTER_ID не заданы); metrika-latest.json не создан

### Named blockers
- METRIKA_FEEDBACK_MISSING — нет OAuth/counter id, ingest невозможен
- EVIDENCE_SKIPPED — human-first-v2, отчёт не писался
- LOW_SAMPLE — публикация 2026-08-26, поведенческая выборка отсутствует даже при рабочей Metrika

### Keep
- H1 Клышина: три удара с часами (12:00 / 16:30) + moral punch «не в такси» без сырого P0 «квартиры посуточно тюмень» в заголовке (P0 5675 — в H2/стикерах, title-brief.json)
- Открытие: конкретная сцена в прихожей с двумя чемоданами, 350 ₽ за ячейку, тревога — opening-meta-gate PASS
- Утилитарный угол B03: окно между выездом 12:00 и транспортом 16:30 — отдельный кластер от B01 (заселение) и B02 (залог)
- Перелинковка: 3 sibling (уборка, залог, бесконтакт) + crosslink-qa PASS после publish
- Description Дзен-карточка: «До поезда четыре часа — а чемоданы куда?» — не дублирует H1 (description-brief PASS)

### Change
- После настройки Metrika: перепроверить bounce/duration для slug `vyezd-v-12-00-poezd-v-16-30-chemodany-ne-v-taksi` через 7–14 дней; сравнить с B01/B02 cohort
- При слабом on-site engagement — усилить mid-article CTA «вопрос-отмычка до оплаты» выше fold (сейчас ближе к финалу)
- Зафиксировать в Cloud Secrets `YANDEX_METRIKA_*` до следующего Content-learner (см. INC-20260826-1257)

### Never again
- Не выводить причинность CTR/retention без Metrika ingest и достаточной выборки
- Не повторять иллюзию «в отеле так везде» без явного контраста отель vs посуточная квартира в первых 2–3 абзацах (здесь сработало — держать как паттерн серии B)
- Не invent'ить content-evidence-report.json или scorecards ради закрытия gate

### Proposed apply
- Дождаться Metrika PASS → повторный Content-learner для B03 с cohort B01/B02
- При подтверждении сильного time-beat hook — записать в memory/content-meta-ab-learnings.md (не в Writer)
- Fixer: настроить YANDEX_METRIKA_OAUTH_TOKEN + YANDEX_METRIKA_COUNTER_ID (CLOUD-FIRST-RUN.md)

### Durable applied
- none

### Resolution
status: recorded
