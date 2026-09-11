# Assembled title inputs — B16

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened), NOT how-to, NOT guide
- Two beats: period, em dash, colon, or contrast
- MUST include figure: ₽ / ночи / минуты / люди (gate FAIL without digit)
- BAN: «что проверить», «как снять», «разберём», «N советов», «N шагов»
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: person with dog booking nightly stay — not host-operator report
- ~40–70 chars in h1
- Tyumen optional in H1
- klyshin_title_shape: 2 — [Утверждение/обещание]. [Опровержение/обрыв]
- dzen_pattern: 2 (case with sums)

## Scout handoff

- topic_id: B16
- slug: napisali-mozhno-s-sobakoj-u-dveri-doplatili-3-000
- klyshin_hook: dog_breed_fee | original: «Написали «можно с собакой». У двери — доплата за породу.»
- title_draft: «Написали «можно с собакой». У двери — доплата 3 000 за метиса»
- P0: «снять квартиру посуточно с собакой» 427 (225); Tyumen spine «квартиры посуточно тюмень» 5020
- angle: «можно с животными» + чат «да, можно» → у двери после 8 400 ₽ доплата 3 000 за метиса 18 кг («до 10 кг»)
- anti_dup: NOT B04 third guest; NOT B02 deposit chip; NOT B13 code; NOT B14 neighbors; NOT B15 wifi

## Editorial case figures (from research-notes)

- 2 ночи × 4 200 ₽ = 8 400 ₽ paid
- доплата 3 000 ₽ at door
- итого 11 400 ₽ or refusal at 23:00
- метис ~18 кг, limit «до 10 кг»

## Good calibration shapes (ORIGINAL text only)

- «Написали «можно с собакой». У двери — доплата 3 000 за метиса»
- «В чате «да, можно». За 8 400 ₽ у двери попросили ещё 3 000»
- «Обещали «можно с собакой». В 23:00 — +3 000 за вес»

## Output JSON schema

```json
{
  "topic_id": "B16",
  "h1": "...",
  "title": "...",
  "slug": "napisali-mozhno-s-sobakoj-u-dveri-doplatili-3-000",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 2,
  "wordstat_p0": "снять квартиру посуточно с собакой",
  "wordstat_p0_volume": 427,
  "dzen_pattern": 2
}
```
