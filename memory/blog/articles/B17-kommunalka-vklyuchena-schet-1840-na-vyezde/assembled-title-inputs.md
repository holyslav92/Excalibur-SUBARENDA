# Assembled title inputs — B17

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor guest night: [normal]. Then [horror] / quote / number
- Two beats: period, em dash, colon, or contrast («Только», «А потом»)
- MUST include figure: ₽ / ночи / дни / люди (gate FAIL without digit)
- BAN: «что проверить», «как снять», «разберём», «N советов», HH:MM in H1
- BAN: ЕГРН, наследство, ипотека, Шакin, риэлтор, Клышин, +79032334201
- Guest audience: person who booked 3 nights in Tyumen, promised «коммуналка включена», hit with meter bill on checkout
- ~40–70 chars in h1
- Tyumen optional in H1 (P0 demand spine is «квартиры посуточно тюмень» — under H1, not SEO tail)
- klyshin_title_shape: 3 or 5 — direct speech «коммуналка включена» + checkout horror 1 840 ₽
- dzen_pattern: 2 — case with sums

## Scout handoff

- topic_id: B17
- slug: kommunalka-vklyuchena-schet-1840-na-vyezde
- klyshin_hook: utilities_jkh | original: «Три ночи. В объявлении — „коммуналка включена“. На выезде — фото счётчиков и доплата 1 840 ₽»
- title_draft calibration: «Написали „коммуналка включена“. На выезде прислали счётчики — 1 840 ₽»
- P0: «квартиры посуточно тюмень» 4 840 (55+11176), 10 385 (225)
- angle: guest booked 3 nights in Tyumen; card said «коммуналка включена»; on checkout host sent meter photos and demands 1 840 ₽ «по факту расхода»
- anti_dup: NOT B10 «всё включено» + taxi 2 400; NOT B12 hot water; NOT B14 neighbors; NOT B15 wifi; NOT B16 flight refund
- case_number: 1 840 ₽; three nights; «коммуналка включена» vs meter bill on checkout

## Editorial case figures (from research-notes)

- 3 nights, ~9 600 ₽ booking price (3 200 ₽/night — case fiction)
- promise: «коммуналка включена» / «все коммунальные платежи включены»
- checkout: photos of meters + 1 840 ₽ demand
- host line: «Это по факту расхода — свет, вода, стиралка»
- lockpick question (NOT in H1): «Коммуналка в цене или по счётчикам?»

## Anti-dup H1 (published)

NOT: B10 «Хозяин сказал «всё включено». В такси доплатили 2 400 ₽» (taxi, not utilities)
NOT: B02 deposit, B04 third guest, B08 silence, B13 code/keybox, B14 neighbors, B15 workspace, B16 refund
NOT repeat published titles in published-titles-only.md

## Good calibration shapes (ORIGINAL text only)

- «Написали „коммуналка включена“. На выезде прислали счётчики — 1 840 ₽»
- «„Коммуналка включена“ — на выезде счёт по счётчикам: 1 840 ₽»
- Shape anchor: included utilities promise + checkout meter bill with sum (NOT how-to, NOT ЖКХ essay)

## Output JSON schema

```json
{
  "topic_id": "B17",
  "h1": "...",
  "title": "...",
  "slug": "kommunalka-vklyuchena-schet-1840-na-vyezde",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 3,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
```
