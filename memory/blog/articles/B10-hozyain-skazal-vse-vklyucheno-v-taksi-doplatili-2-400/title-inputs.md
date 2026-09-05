# Title inputs B10

topic_id: B10
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026, начало осени

Read: research-notes.md, research-inputs.md, published-titles-only.md, scout handoff (memory/scout/.cursor/excalibur-blog-handoff.md)

**OUTPUT:** Return ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER or refusal. Script saves output.

## Scout / case
- Guest books apartment in Tyumen with «всё включено» in listing
- klyshin_hook: hidden_fees_all_inclusive
- title_draft shape: **«Хозяин сказал «всё включено». В такси доплатили 2 400»**
- dzen_pattern: 2 — кейс с суммами и датами
- angle: marketing «all inclusive» vs stack of fees before check-in (cleaning, utilities, service fee, towels)
- lockpick: «Что именно входит в “всё включено” и какие доплаты возможны при заселении?»
- moral: сначала список включённого, потом деньги и ключ
- refusal beat: «Нет. Так не заселяем» / «Сначала список включённого. Потом ключ.»

## Research burn numbers
- Unexpected stack **2 400 ₽** in taxi before check-in (editorial case sum, not market stat)
- Typical line items: cleaning 800–1500 ₽, service fee 1000–1500 ₽, towels/utilities if not stated
- Guest already in taxi en route when host sends fee list in chat

## Wordstat P0
- «квартиры посуточно тюмень» — 5261 (55+11176)
- compare «снять квартиру посуточно» — 728517 (225)
- secondary: «аренда квартиры посуточно» — 729 (55+11176)

## Anti-dup
NOT: B01 code, B02 deposit, B03 uni walk, B04 extra guest, B05 reviews, B06 luggage, B07 kitchen/cafe, B08 prepayment silence, B09 parking/barrier

## Hard constraints
- Two-beat stop-factor H1 (~50–70 chars) — guest night already happened, NOT how-to
- Target shape: **«Хозяин сказал «всё включено». В такси доплатили 2 400»** (or very close; keep 2 400 ₽ figure)
- BAN how-to, N советов, разберём, topic label, HH:MM in H1
- «Тюмень» in H1 optional; title/meta may carry P0 demand spine
- Fields: topic_id, h1, title, subject, angle, klyshin_title_shape (1-10), verdict: PASS
