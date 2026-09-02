# Title inputs B07

topic_id: B07
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026

Read: research-serp.json, published-titles-only.md, scout handoff (memory/scout/.cursor/excalibur-blog-handoff.md)

Output ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER.

## Scout / case

- Guest books apartment for 3 nights; listing says kitchen «есть» — in reality empty drawers: no oil, salt, mugs, pan unusable; every breakfast and dinner ends up in café
- klyshin_hook: kitchen_vs_hotel_cafes | original: «Три ночи. Кухня «есть» — или каждый день кафе?»
- title_draft calibration shape (intent, adapt for gate): **Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽**
- dzen_pattern: 4 — контраст с ответом в лиде
- dzen_shape_hint: «Кухня в объявлении — а готовить не на чём: сколько съела поход в кафе за три ночи»
- klyshin_title_shape: prefer 3 (прямая речь → что вскрылось) or 5 (цифра = цена ожога)
- angle: обещанная кухня vs фактические 2 400–3 600 ₽/сутки на еду вне дома; NOT hidden_fees-at-door (B04); NOT checkout/luggage (B06); NOT reviews (B05)
- moral: спросить «что именно на кухне» до оплаты — сковорода, масло, соль, кружки
- lockpick: «Что именно на кухне: сковорода, масло, соль, кружки?»

## Research signals (research-serp.json)

- Contrast case: kitchen checkbox in listing vs café spend every day for 3 nights
- Burn number anchor: ~7 200 ₽ total café spend over 3 nights (2 400 ₽/day × 3)
- Guest audience: family or couple expecting to cook like at home, not hotel breakfast

## Wordstat P0

- «квартиры посуточно тюмень» — 5446 (55+11176) — demand spine under H1
- «посуточно или отель» — 433 (225) — contrast cluster
- «квартира с кухней посуточно» — 89 (225)
- «отель или посуточная квартира» — 312 (225)

## Anti-dup (published-titles-only.md)

Do NOT repeat: B01 wrong door code, B02 deposit/chip, B03 uni 40 min walk, B04 extra guest fee, B05 rating 4,8 reviews, B06 checkout noon train luggage

## Hard constraints

- Two-beat stop-factor guest-night CASE H1 (~50–70 chars) — already happened burn, NOT how-to
- Shape example: «Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽»
- **BAN `HH:MM` in H1** — number = ₽ / ночи / people, not list count
- NOT how-to, NOT «N советов», NOT «разберём», NOT «кухня посуточно» SEO tail
- Ban: как снять, что проверить, N советов/шагов, разберём, topic label, ЕГРН, ипотека, Клышин
- «Тюмень» in H1 optional
- Fields: topic_id, h1, title, subject, angle, klyshin_title_shape (1–10), verdict: PASS
- h1 and title may differ; title can carry Wordstat spine lightly
