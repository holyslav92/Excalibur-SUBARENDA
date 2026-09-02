# Title inputs B08

topic_id: B08
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026

Read: research-notes.md, published-titles-only.md, scout handoff (research-inputs.md § scout_handoff)

Output ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER.

## Scout / case

- Family of four books apartment for 2–3 nights in Tyumen; listing says «постельное бельё и полотенца»; in bathroom — one towel for four people (or zero)
- klyshin_hook: pack_vs_flat | original: «Собрал чемодан — в квартире нет полотенец»
- title_draft calibration shape (intent, adapt for gate): **Сняли квартиру посуточно. В ванной — одно полотенце на 4 гостей**
- gate figure: H1 MUST include digit+гост/чел/ноч OR ₽ — «четверых» alone fails gate; use «4 гостей» or «4 человек»
- dzen_pattern: 2 — утверждение + опровержение / контраст
- dzen_shape_hint: «Собрали чемодан с полотенцами — а в ванной один кусок ткани на четверых: что обещают в объявлении и что проверить до оплаты»
- klyshin_title_shape: prefer 2 (утверждение → опровержение) or 1 (действие → катастрофа)
- angle: галочка «полотенца» ≠ число на гостя; NOT deposit (B02); NOT kitchen/café (B07); NOT checkout/luggage (B06); NOT code (B01); NOT extra guest (B04); NOT rating (B05); NOT uni walk (B03)
- moral: фото ванной/шкафа и число полотенец в переписке — до перевода денег
- lockpick: «Сколько полотенец на человека и что именно в ванной — фото до оплаты?»
- burn anchor: ~400–900 ₽ emergency towel purchase at night (optional in H1; people count «четверых» is stronger figure)

## Research signals (research-notes.md)

- Checkbox «полотенца» in listing does not specify count per guest
- Guest arrives after payment; discovers one towel for four
- Market split: some hosts give 2 towels/guest, others one set total
- Fresh Sutochno.ru review: hygiene kits mismatch guest count

## Wordstat P0

- «квартиры посуточно тюмень» — 5363 (55+11176) — demand spine under title/meta
- «снять квартиру посуточно в тюмени» — 1696 (55+11176) / 4290 (225)
- «аренда квартиры посуточно» — 747
- «полотенца» — 9690 (adjacent pain cluster)

## Anti-dup (published-titles-only.md)

Do NOT repeat: B01 wrong door code, B02 deposit/chip, B03 uni 40 min walk, B04 extra guest fee, B05 rating 4,8 reviews, B06 checkout noon train luggage, B07 kitchen 7 200 ₽ café

## Hard constraints

- Two-beat stop-factor guest-night CASE H1 (~50–70 chars) — already happened burn, NOT how-to
- Shape example: «Сняли квартиру посуточно. В ванной — одно полотенце на 4 гостей»
- **BAN `HH:MM` in H1** — number = ₽ / ночи / «4 гостей» (digit required for gate), not list count
- NOT how-to, NOT «N советов», NOT «разберём», NOT «что проверить» SEO tail
- Ban: как снять, что проверить, N советов/шагов, разберём, topic label, ЕГРН, ипотека, Клышин
- «Тюмень» in H1 optional
- Fields: topic_id, h1, title, subject, angle, klyshin_title_shape (1–10), verdict: PASS
- h1 and title may differ; title can carry Wordstat spine lightly
