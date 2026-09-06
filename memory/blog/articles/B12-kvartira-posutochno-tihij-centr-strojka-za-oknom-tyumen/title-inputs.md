# Title inputs B12

topic_id: B12
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026, начало осени

Read: research-notes.md, published-titles-only.md, .cursor/excalibur-blog-handoff.md

**OUTPUT:** Return ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER or refusal. Script saves output.

## Scout / case
- Guest books 3 nights in «тихий центр, рядом набережная»; Friday evening quiet; Saturday morning crane noise outside window
- klyshin_hook: quiet_center_maps
- title_draft shape: **«Написали «тихий центр». В 6:30 за окном — кран»** — FIX: **BAN HH:MM in H1** (use «утром», «в субботу утром», not 6:30)
- dzen_pattern: 5 — локальный + сезонный
- angle: «тихий центр» vs стройка/кран; проверка панорамы до оплаты
- lockpick: «Что видно в панораме с балкона, если включить слой стройки?»
- moral: сначала карта и панорама, потом деньги
- host quote in case: «Ну это же центр»

## Research burn numbers
- 3 nights × ~4 200 ₽ = **12 600 ₽** already paid; sleep ruined; last-minute move not an option
- Use figure in H1: ₽ or «3 ночи» or «12 600 ₽»

## Wordstat P0
- «квартиры посуточно тюмень» — 5235 (55+11176) / 11220 (225)
- cluster: «квартира посуточно тюмень центр» 68; «снять квартиру посуточно в центре тюмени» 54

## Anti-dup
NOT: B01 code, B02 deposit, B03 uni walk, B04 third guest, B05 reviews, B06 luggage, B07 kitchen, B08 prepayment silence, B09 parking, B10 taxi extras, B11 towels
NOT in H1: двор, парковка, залог, полотенца, кухня, такси, отмена брони, код

## Hard constraints
- Two-beat stop-factor H1 (~40–70 chars) — guest night already happened
- Shape 2 or 3: «Написали «тихий центр». …» or ««Тихий центр» … Только …»
- **BAN** how-to, N советов/шагов, разберём, topic label, **HH:MM in H1**
- **REQUIRE** figure: ₽ / ночи / люди in H1
- «Тюмень» in H1 optional
- slug hint: napisali-tihij-centr-v-6-30-za-oknom-kran (slug may keep time; H1 must not)
- Fields: topic_id, h1, title (SEO with P0 spine, not duplicate of h1), subject, angle, klyshin_title_shape (1-10), verdict: PASS

## Calibration (original text, not copy)
- «Написали «тихий центр». Утром за окном — кран» — needs ₽/ночи figure added
- ««Тихий центр» в объявлении. Только утром — кран на 12 600 ₽»
- «Заплатили 12 600 ₽ за 3 ночи. Утром — кран под окном»
