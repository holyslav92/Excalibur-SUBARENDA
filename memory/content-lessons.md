# Excalibur BLOG — content lessons

Active lessons from post-publish content-learner runs. Review-only proposals;
Writer prompt changes require explicit human decision.

---

## LESSON-20260827-1140-B03-kitchen-quote-hook-utility
status: proposed
topic_id: B03
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json absent; structural gates PASS (structure, opening-meta, html-linter, interlink×3, community-cta, cover-qa, live-page)
- metrika_signal: none — METRIKA FEEDBACK BLOCKER (YANDEX_METRIKA_OAUTH_TOKEN / YANDEX_METRIKA_COUNTER_ID not set)

### Named blockers
- METRIKA_FEEDBACK_MISSING
- EVIDENCE_SKIPPED
- LOW_SAMPLE (article published 2026-08-27; no behavioral data ingested)

### Keep
- Opening pain-scene: конкретное время + действие гостя (покупка продуктов) + цитата из объявления «кухня» — без term-dump и research-брифинга.
- Дословный вопрос до оплаты в `<b>`: «Плита и сковородка или только микроволновка?» — отделяет рабочую кухню от «кухонной зоны».
- Арифметика через разницу «квартира vs отель с завтраком» (3 000–5 000 ₽ за три ночи), а не через полную цену квартиры.
- Честное признание хоста, когда отель с завтраком выгоднее на 1–3 ночи — усиливает доверие без подмены utility.
- Demand spine Wordstat P0 («квартиры посуточно тюмень», 5583) в теле/CTA и description-brief, не в H1 (title-brief angle).

### Change
- После настройки Metrika credentials — пересмотреть bounce/duration/pageDepth когорты B03 vs sibling B01/B02; до этого не делать причинных выводов по hook.

### Never again
- Выдумывать точные чеки гостя («Точные чеки я не буду придумывать за него»).
- Превращать H1 в SEO-хвост demand spine — pain-scene + quoted listing word сильнее для buyer-intent.

### Proposed apply
- Review-only: для тем «обещание в карточке vs реальность» (кухня, wifi, парковка, бесконтакт) повторять паттерн дословного pre-booking вопроса + чек-лист до оплаты.
- Не добавлять в `shared/writer-master-prompt.md` без решения человека.

### Durable applied
- none

### Resolution
status: recorded
article_dir: memory/blog/articles/B03-kvartira-posutochno-kuhnya-est-ili-kazhdyj-den-kafe
live_url: https://добрыйдом-72.рф/blog/kvartira-posutochno-kuhnya-est-ili-kazhdyj-den-kafe/
