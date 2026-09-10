# Assembled title inputs — B15

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened at the door), NOT how-to, NOT guide
- Two beats: period, em dash, colon, or contrast («Только», «А потом», «У двери»)
- MUST include figure: ₽ / ночи / минуты / люди (gate FAIL without digit)
- BAN: «что проверить», «как снять», «разберём», HH:MM in H1 (words «ночью»/«утром» OK)
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- BAN: N советов/шагов/вопросов, topic label («О детях…»), SEO tail
- Guest audience: family booking nightly stay in Tyumen — not host-operator report
- ~40–70 chars in h1
- Tyumen optional in H1 (P0 demand spine is «квартиры посуточно тюмень» — under H1, not SEO tail)
- klyshin_title_shape: 3 — [Прямая речь]. [Что вскрылось]
- dzen_pattern: 2 — case with sums at door

## Scout handoff

- topic_id: B15
- slug: napisali-s-detmi-mozhno-doplata-za-malysha
- klyshin_hook: children_daily_rental | original: «С детьми можно» в объявлении — у двери доплата за малыша или нет детской кроватки
- dzen_shape_hint: «Написали «с детьми можно». У двери попросили 2 000 за малыша»
- title_draft calibration: two-beat with «с детьми можно» promise vs 2 000 ₽ surprise at door for toddler
- P0: «квартиры посуточно тюмень» 5059 (55+11176) / 10754 (225)
- P1: «квартира посуточно с детьми» 283 | «детская кроватка посуточно» 67
- angle: family with ~3-year-old, two nights (~7 600–8 400 ₽ total); card/chat says «с детьми можно»; at door host asks 2 000 ₽ for child OR no crib promised — couch without rails
- anti_dup: B04 = extra ADULT guest at door; B15 = CHILD, crib, child surcharge — different wound

## Editorial case figures (from research-notes)

- 2 000 ₽ unexpected child surcharge at door (editorial reconstruction)
- two nights, family with toddler ~3 years
- alternative conflict: no crib on arrival (body only — H1 focuses on door surcharge)

## Anti-dup H1 (published)

NOT: B04 «доплату за третьего»; B11 towels; B10 included taxi; any title in published-titles-only.md
Similar tenant line «у двери попросили» OK if child-specific (cf. B09 parking, B04 third guest)

## Good calibration shapes (ORIGINAL text only — prefer shape #3)

- «Написали «с детьми можно». У двери попросили 2 000 за малыша»
- ««С детьми можно» в чате. У двери — 2 000 ₽ за трёхлетку»
- Shape anchor: quote «с детьми можно» + door surprise 2 000 ₽ for child

## Output JSON schema

```json
{
  "topic_id": "B15",
  "h1": "...",
  "title": "...",
  "slug": "napisali-s-detmi-mozhno-doplata-za-malysha",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 3,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
```
