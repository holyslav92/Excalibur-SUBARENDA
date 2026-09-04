# Title inputs B09

topic_id: B09
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026, начало осени

Read: research-notes.md, published-titles-only.md, scout handoff (.cursor/excalibur-blog-handoff.md)

**OUTPUT:** Return ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER or refusal. Script saves output.

## Scout / case
- Guest books apartment with «парковка рядом»; at barrier «пропуска нет»
- klyshin_hook: parking_before_booking
- title_draft shape: **«Написали „парковка рядом“. У шлагбаума: „пропуска нет“»**
- dzen_pattern: 2 — кейс с суммами и датами
- angle: парковка/пропуск/номер авто — до оплаты, не у шлагбаума
- lockpick: «Куда ставить машину и есть ли пропуск на мой номер?»
- moral: сначала место и въезд, потом перевод

## Research burn numbers
- 4 800 ₽/night × 2 nights; 600 ₽ paid parking wait; risk municipal fine
- arrival evening ~21:30 at ЖК barrier

## Wordstat P0
- «квартиры посуточно тюмень» — 11765 (225) / 5320 (55+11176)

## Anti-dup
NOT: B01 code, B02 deposit, B03 uni, B04 extra guest, B05 reviews, B06 luggage, B07 kitchen, B08 prepayment silence

## Hard constraints
- Two-beat stop-factor H1 (~50–70 chars) — guest night already happened
- Shape: «Написали „парковка рядом“. У шлагбаума: „пропуска нет“»
- BAN how-to, N советов, разберём, topic label, HH:MM in H1
- «Тюмень» in H1 optional
- Fields: topic_id, h1, title, subject, angle, klyshin_title_shape (1-10), verdict: PASS
