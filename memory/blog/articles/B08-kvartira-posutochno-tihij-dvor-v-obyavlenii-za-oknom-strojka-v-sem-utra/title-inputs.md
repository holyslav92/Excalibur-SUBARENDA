# Title inputs B08

topic_id: B08
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026

Read: research-notes.md, published-titles-only.md, scout handoff (.cursor/excalibur-blog-handoff.md)

Output ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER.

## Scout / case

- Guest books 2 nights; listing says «тихий двор» / «центр, тишина»; first morning at 6:45 jackhammer from construction site visible only after arrival in maps
- klyshin_hook: quiet_center_maps | original: «Тихий центр» — за окном стройка
- title_draft calibration shape: **Написали «тихий двор». Утром за окном — перфоратор**
- dzen_pattern: 5 — локальный + сезонный
- dzen_shape_hint: «Обещали тишину в центре — утром будильник не нужен: стройка под окном»
- klyshin_title_shape: prefer 3 (прямая речь → что вскрылось) or 1 (нормально → ужас)
- angle: обещанная тишина vs перфоратор в 6:45; NOT neighbors essay; NOT legal complaint guide
- moral: панорама двора в Картах до оплаты
- lockpick: «Что слышно из окна спальни на 7 утра?»

## Research signals

- Case: 2 nights, ~3 hours sleep first night, host says «стройка временная»
- SanPin reference only: 55 dB day / 45 dB night — not spine of article
- Maps check 7 minutes before booking vs 2 ruined nights

## Wordstat P0

- «квартиры посуточно тюмень» — 5363 (55+11176)
- «снять квартиру посуточно в тюмени» — 1696

## Anti-dup

Do NOT repeat: B01 code, B02 deposit, B03 vuz, B04 extra guest, B05 reviews, B06 luggage, B07 kitchen

## Hard constraints

- Two-beat stop-factor guest-night CASE H1 (~50–70 chars)
- Shape: «Написали «тихий двор». Утром за окном — перфоратор»
- **BAN `HH:MM` in H1** — use «утром», «в семь утра», not 6:45
- NOT how-to, NOT «N советов», NOT «разберём»
- «Тюмень» in H1 optional
- title can carry Wordstat spine lightly: квартиры посуточно тюмень
