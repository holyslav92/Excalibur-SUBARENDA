# Assembled title inputs — B24

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor guest night CASE — already happened burn, NOT how-to
- Shape anchor (MUST follow): «На фото — стиральная машина. В квартире — раковина и вешалка» — photo promise vs reality after check-in
- Two beats: period, em dash, colon, or contrast («Только», «А потом»)
- MUST include figure for gate: ₽ / ночи / третий день / люди — gate FAIL without digit or night-word
- BAN: «что проверить», «как снять», «разберём», «N советов», HH:MM in H1
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: person who booked 2–3 nights in Tyumen, chose flat by photo with washing machine, after payment finds only sink and hanger
- ~40–70 chars in h1
- Tyumen optional in H1 (P0 demand spine «квартиры посуточно тюмень» — under H1, not SEO tail)
- klyshin_title_shape: 2 — [assertion in listing]. Only [reality contradiction]
- dzen_pattern: 2 — case with sums; hint: «обещали стиралку — на третий день прачечная за 600 ₽»

## Scout handoff

- topic_id: B24
- slug: napisali-stiralnaya-est-v-kvartire-tolko-rakovina
- klyshin_hook: appliance_lie_washing_machine | original: «На фото в объявлении — стиральная машина. В коридоре — вешалка и раковина, бельё на третий день.»
- title_draft calibration: «На фото — стиральная машина. В квартире — раковина и вешалка»
- P0: «квартиры посуточно тюмень» 4724 (55+11176), 10016 (225)
- supporting: «снять квартиру посуточно фото» 3693 (225)
- angle: guest booked short stay; card photo shows washer in unit; on arrival only sink, hanger, drying rack; host says shared basement or broken
- anti_dup: NOT B07 kitchen/cafe; NOT B11 towels; NOT B20 hot water; NOT B23 cleaning fee; NOT B10 «всё включено»; NOT B17 utilities
- case figures: 2–3 nights; laundry cycle ~600 ₽ in Tyumen (illustrative); «третий день» without machine

## Editorial case figures (from research-notes)

- Guest chose flat by photos showing washing machine in bathroom/utility area
- After check-in: sink, hanger, clothes drying on day 3 — no in-unit machine
- Host may say «в подвале», «общая на этаже», «сломалась» — editorial scene only
- 600 ₽ = one self-service wash+dry cycle in Tyumen (BIG WASH / 72.ru range) — scenario cost, not confirmed guest expense
- lockpick question (NOT in H1): «Стиралка в этой квартире или в подвале?»

## Anti-dup H1 (published)

NOT: B07 «кухня есть» + cafe 7 200 ₽
NOT: B11 towels 890 ₽, B20 hot water, B23 cleaning 1 800 ₽
NOT: B10 taxi, B17 utilities, B09 parking
NOT repeat any title in published-titles-only.md

## Good calibration shapes (ORIGINAL text only — gate-safe with figure)

- «На фото — стиральная машина. В квартире — раковина и вешалка» + add nights or 600 ₽ in second beat if needed for gate
- «На фото — стиральная. Третий день — прачечная за 600 ₽»
- «На фото стиралка в санузле. Три ночи — раковина и вешалка»
- Prefer photo-vs-reality two-beat; 600 ₽ or «третий день»/«3 ночи» for figure

## Output JSON schema

```json
{
  "topic_id": "B24",
  "h1": "...",
  "title": "...",
  "slug": "napisali-stiralnaya-est-v-kvartire-tolko-rakovina",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 2,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
```
