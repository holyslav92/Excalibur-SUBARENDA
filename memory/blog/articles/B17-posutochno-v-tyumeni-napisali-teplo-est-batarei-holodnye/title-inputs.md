# Title inputs B17

topic_id: B17
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026, переходный сезон — отопление в городе может ещё не стартовать

Read: research-notes.md, published-titles-only.md, scout handoff (.cursor/excalibur-blog-handoff.md at repo root)

**OUTPUT:** Return ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER or refusal. Script saves output.

## Scout / case
- Guest books apartment in Tyumen; listing/chat says «тепло есть» or «отопление есть»
- Evening: outside ~+6 °C, radiators cold, room ~16–17 °C — paid night ahead
- klyshin_hook: sept_cold_radiators_guest
- title_draft shape: **«Написали «тепло есть». За окном +6 °C — батареи холодные»**
- dzen_pattern: 5 (цифра = цена ожога) — but guest-night CASE with temperature contrast OK if figure present (₽ / ночи / минуты)
- klyshin_title_shape: 2 — [Утверждение]. Только [опровержение] OR shape 3 direct speech
- angle: promise «тепло» vs cold radiators; NOT hot water, NOT winter hero
- NOT how-to, NOT «когда включат отопление в городе» essay

## Research burn numbers
- 2–3 nights prepaid; room 16–17 °C; outside +6 °C; September heating may start only in October per forecasts
- Guest pain: one night to sleep tonight, not after 5-day +8°C rule

## Wordstat P0
- «квартиры посуточно тюмень» — 4929 (55+11176)
- supporting «батареи холодные» — 7704 (225)

## Anti-dup (published-titles-only.md)
NOT: B01 code, B02 deposit, B03 uni walk, B04 extra guest, B05 reviews, B06 luggage, B07 kitchen, B08 chat silence, B09 parking, B10 included, B11 towels, B12 construction noise, B13 keybox, B14 neighbors, B15 wifi desk, B16 flight cancel refund

## Hard constraints
- Two-beat stop-factor H1 (~40–70 chars) — guest night already burning
- **LOCK opening:** «Написали «тепло есть». За окном +6 °C — батареи холодные» — do NOT reverse to «Тепло есть», написали
- Figure gate: append «на 2 ночи» or «за 6 800 ₽» at end — required for PASS
- Final H1 example: «Написали «тепло есть». За окном +6 °C — батареи холодные на 2 ночи»
- BAN: как снять, что проверить, разберём, лучшие, topic label, HH:MM in H1, ЕГРН, ипотека, Клышин
- «Тюмень» in H1 optional
- Fields: topic_id, h1, title, subject, angle, klyshin_title_shape (1-10), verdict: PASS
- h1 and title should match (same string)
