# Title inputs B06

topic_id: B06
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026

Read: research-notes.md, published-titles-only.md, scout handoff (memory/scout/.cursor/excalibur-blog-handoff.md)

Output ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER.

## Scout / case

- Guest checks out at noon (12:00), train at 16:30 — 4,5 hours dead window with suitcases; nowhere safe to leave bags after handing keys
- klyshin_hook: checkout_train_bags | original: «Выезд в 12:00. Поезд в 16:30.»
- title_draft calibration shape (intent, adapt for gate): **Выезд в полдень. Поезд через 4 часа — чемоданы остались на лестнице у подъезда**
- dzen_pattern: 2 (живой кейс с датами/окном)
- klyshin_title_shape: prefer 1 (action → catastrophe) or 4 (said X, found only now)
- angle: выезд из квартиры, поезд днём — куда деть багаж между; NOT early check-in (B01); NOT hotel luggage desk assumption
- moral: сначала договориться про багаж/хранение, потом сдача ключей
- lockpick: «Можно оставить багаж до вокзала?» / «Есть камера хранения у вас?»

## Wordstat P0

- «квартиры посуточно тюмень» — 5446 (55+11176) — demand spine under H1
- «хранение багажа» — 133 (55+11176)
- «хранение багажа тюмень» — 28 (55+11176)

## Anti-dup (published-titles-only.md)

Do NOT repeat: B01 wrong door code, B02 deposit/chip, B03 uni 40 min walk, B04 extra guest fee, B05 rating 4,8 reviews

## Hard constraints

- Two-beat stop-factor guest-night CASE H1 (~50–70 chars) — already happened burn, NOT how-to
- Shape like: «Выезд в полдень. Поезд через 4 часа — чемоданы остались на лестнице у подъезда»
- **BAN `HH:MM` in H1** (gate fails clock stamps) — use «в полдень», «через 4 часа», «вечером»; number = hours/₽/minutes not list count
- NOT how-to, NOT «N советов», NOT «разберём», NOT «куда деть» as guide label
- Ban: как снять, что проверить, N советов/шагов, разберём, topic label, ЕГРН, ипотека, Клышин
- «Тюмень» in H1 optional
- Fields: topic_id, h1, title, subject, angle, klyshin_title_shape (1–10), verdict: PASS
- h1 and title may differ; title can carry Wordstat spine lightly
