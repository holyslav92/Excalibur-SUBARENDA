# Assembled title inputs — B15

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened), NOT how-to, NOT guide
- Two beats: period, em dash, colon, or contrast («Только», «А потом»)
- MUST include figure: ₽ / ночи / минуты / люди (gate FAIL without digit)
- BAN: «что проверить», «как снять», «разберём», HH:MM in H1 (words «ночью»/«утром»/«вечером» OK — NOT 10:00 or 22:00)
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: person booking nightly stay in Tyumen on business trip — not host-operator report
- ~40–70 chars in h1
- Tyumen optional in H1 (P0 demand spine is «квартиры посуточно тюмень» — under H1, not SEO tail)
- klyshin_title_shape: 2 — [Утверждение/обещание]. [Опровержение/обрыв]
- dzen_pattern: NOT list/how-to

## Scout handoff

- topic_id: B15
- slug: pozvonili-v-10-00-v-22-00-wifi-ne-tyanet-sozvon
- klyshin_hook: sept_business_trip | original: «Звонок в 10:00. Заселился в 22:00.» (times ONLY in body/angle — NOT in H1)
- title_draft calibration (REWORK — remove HH:MM): two-beat with morning promise vs evening Wi-Fi/workspace failure
- P0: «квартиры посуточно тюмень» 5020 (55+11176)
- P1: «справка о проживании» 160
- angle: business-trip guest books 3 nights (~11 400 ₽); morning host promises fast internet + docs; late check-in — coffee table, outlet behind sofa, ~8 Mbps, unstable video call; docs «after checkout»
- anti_dup: B14 = neighbors/music; B12 = external noise; 08.09 WP «Заселился после рейса. За 10 200 ₽ Wi‑Fi сорвал созвон» = AFTER payment — B15 = pre-payment lockpick on workspace/Wi-Fi/docs, different wound

## Editorial case figures (from research-notes)

- ~11 400 ₽ for three nights (3 × ~3 800 ₽)
- three nights stay
- Wi‑Fi ~8 Мбит, unstable video call
- journal table, outlet behind sofa
- host: «ну вы же не просили отдельно рабочее место»

## Anti-dup H1 (published)

NOT: B14 «тихий дом» + music; B12 «тихий центр» + crane; any duplicate of published titles in published-titles-only.md; NOT repeat 08.09 «Wi‑Fi сорвал созвон» headline shape

## Good calibration shapes (ORIGINAL text only)

- «Быстрый интернет» обещали. За 11 400 ₽ — созвон срывается утром
- «Всё есть» в чате. Три ночи за 11 400 ₽ — Wi‑Fi не тянет созвон
- Shape anchor: morning promise (internet/docs) + evening/workspace/Wi-Fi contrast + money/nights figure

## Output JSON schema

```json
{
  "topic_id": "B15",
  "h1": "...",
  "title": "...",
  "slug": "pozvonili-v-10-00-v-22-00-wifi-ne-tyanet-sozvon",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 2,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
```
