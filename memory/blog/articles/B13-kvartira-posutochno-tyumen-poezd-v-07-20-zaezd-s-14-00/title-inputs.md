# Title inputs B13

topic_id: B13
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: начало сентября 2026, осень (не зима на обложке)

Read: research-notes.md, published-titles-only.md, scout handoff (memory/scout/.cursor/excalibur-blog-handoff.md)

**OUTPUT:** Return ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER or refusal. Script saves output.

## Scout / case

- Family (2 adults + child) books 2 nights (~8 400 ₽); night train arrives morning; listing says «бесконтактное заселение»
- After payment host writes: «ключ с 14:00, раньше нельзя» — 4+ hours cold wait (+9 °C) or hotel ~3 200 ₽; taxi 420 ₽
- klyshin_hook: early_checkin | original: parked_hooks early_checkin — гость приехал раньше окна заселения
- title_draft calibration intent (adapt for gate): **«Поезд утром. Написали: «заезд только с двух»»** — scout had 07:20/14:00; **BAN HH:MM in H1** (gate fails clock stamps); use «утром», «с двух», «4 часа»
- dzen_pattern: 2 — кейс с суммами и датами
- klyshin_title_shape: prefer 1 (action → catastrophe) or 3 (direct speech → what surfaced)
- angle: morning train vs host holds key until 14:00; NOT late checkout/luggage (B06); NOT wrong door code (B01); NOT prepayment silence (B08)
- lockpick: «Можно зайти в 8:00, если уеду в 8:00?» / refusal: «Нет. Так не заселяем.»
- moral: сначала письменное окно заезда и ранний заезд, потом оплата
- NOT in H1: код, залог, парковка, кухня, предоплата, тихий центр, соседи, полотенца, такси extras

## Research burn numbers

- 2 nights ~8 400 ₽; 4+ hours wait (07:20→14:00); hotel fallback ~3 200 ₽; taxi 420 ₽
- Use in H1: «4 часа», «2 ночи», «8 400 ₽», «3 200 ₽» — not list skeleton «5 вопросов»

## Wordstat P0

- «квартиры посуточно тюмень» — 5235 (55+11176) / compare 11220 (225) — demand spine under title/meta
- «ранний заезд посуточно» — 316 (225); «квартиры посуточно ранний заезд» — 229 (225)

## Anti-dup (published-titles-only.md)

NOT: B01 code, B02 deposit, B03 uni walk, B04 third guest, B05 reviews, B06 checkout luggage/train, B07 kitchen, B08 prepayment silence, B09 parking, B10 taxi extras, B11 towels, B12 quiet center crane

## Hard constraints

- Two-beat stop-factor guest-night CASE H1 (~40–70 chars) — already happened burn, NOT how-to, NOT guide
- Shape like scout: **«Поезд утром. Написали: «заезд только с двух»»** or **«Утренний поезд. Четыре часа у двери — ключ с двух»**
- **BAN `HH:MM` in H1** (07:20, 14:00, 8:00 fail gate) — story words OK
- **REQUIRE** figure: ₽ / ночи / часы / люди in H1
- Ban: как снять, что проверить, N советов/шагов, разберём, topic label, ЕГРН, ипотека, Клышин, риэлтор
- «Тюмень» in H1 optional
- slug hint: poezd-v-07-20-napisali-zaezd-tolko-s-14-00 (slug may keep time; H1 must not)
- Fields: topic_id, h1, title (SEO with P0 spine, not duplicate of h1), subject, angle, klyshin_title_shape (1-10), verdict: PASS

## Calibration (original text, not copy)

- «Поезд утром. Написали: «заезд только с двух»»
- «Утренний поезд. Четыре часа у двери — ключ с двух»
- «Оплатили 8 400 ₽ за 2 ночи. Ключ только с двух»
