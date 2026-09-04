# Title inputs B10

topic_id: B10
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026, начало осени

Read: research-notes.md, published-titles-only.md, scout handoff (.cursor/excalibur-blog-handoff.md)

**OUTPUT:** Return ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER or refusal. Script saves output.

## Scout / case
- Guest with labrador; listing «можно с животными»; at door +1 500 ₽ breed fee
- klyshin_hook: dog_breed_fee
- title_draft shape: **«Написали «можно с собакой». У двери попросили +1 500 ₽ за породу»**
- dzen_pattern: 2 — кейс с суммами и датами
- angle: pet rules (breed, weight, fee) BEFORE prepay, not at door
- lockpick: «Какая порода и какая доплата в объявлении?»
- moral: сначала правила по животным в тексте, потом перевод

## Research burn numbers
- 5 200 ₽/night × 2 nights = 10 400 ₽ paid; +1 500 ₽ surprise at door
- arrival evening ~20:15 with labrador ~30 kg

## Wordstat P0
- «квартиры посуточно тюмень» — 11765 (225) / 5320 (55+11176)
- «квартира посуточно с животными» — 1352 (225) / 25 (Tyumen)

## Anti-dup
NOT: B02 deposit chip, B04 extra guest, B08 prepayment silence, B09 parking

## Hard constraints
- Two-beat stop-factor H1 (~50–70 chars) — guest night already happened
- Shape: «Написали «можно с собакой». У двери попросили +1 500 ₽ за породу»
- BAN how-to, N советов, разберём, topic label, HH:MM in H1
- «Тюмень» in H1 optional
- Fields: topic_id, h1, title, subject, angle, klyshin_title_shape (1-10), verdict: PASS
