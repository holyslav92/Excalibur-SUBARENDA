# Title inputs B09

topic_id: B09
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026, командировочный гость

Output ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER.

## Scout / case

- Guest on business trip; late check-in ~22:00; listing says «есть Wi‑Fi» / «подойдёт для работы»; morning video call; speed test ~0,3–0,8 Мбит/с; Zoom/Teams freezes; mobile hotspot unreliable (Aug 2026 regional outages news); host may say «перезагрузите роутер» / «у других работает»
- klyshin_hook: sept_business_trip | original: «Звонок в 10:00. Заселился в 22:00. Стол, розетки, Wi‑Fi на созвон, закрывающие — до оплаты.»
- title_draft calibration (adapt for gate — **remove HH:MM**): Снял квартиру посуточно. Утром созвон — Wi‑Fi не тянет
- dzen_pattern: 2 — утверждение в объявлении, опровержение утром
- klyshin_title_shape: prefer 2 («Wi‑Fi есть». Только утром не тянет) or 3 (прямая речь → что вскрылось) or 5 (цифра ожога: минут/₽/Мбит как факт кейса)
- angle: promised Wi‑Fi vs failed work call; NOT door code (B01), deposit (B02), distance (B03), extra guest (B04), reviews (B05), checkout (B06), kitchen/cafe (B07), prepayment silence (B08)
- burn anchors: 0,3–0,8 Мбит/с; 40+ минут до дедлайна; коворкинг 350–1 000 ₽ аварийный выход
- moral: проверить скорость в рабочей точке вечером после заселения, не за минуту до звонка

## Research signals (research-notes.md)

- Zoom HD 720p needs 1,2 Мбит/с — «Wi‑Fi есть» ≠ рабочий канал
- Full Wi‑Fi bars ≠ stable speed in apartment building
- Guest did not test speed at night due to fatigue after late arrival

## Wordstat P0

- «квартиры посуточно тюмень» — 5320 (55+11176) — demand spine under title/meta
- «снять квартиру посуточно в тюмени» — 1134 (55)
- «квартира посуточно командировка» — 69 (225) — weak alone; Wi‑Fi pain rides local spine

## Anti-dup (published-titles-only.md)

Do NOT repeat: B01 door code, B02 deposit/scratch, B03 40 min walk, B04 third guest fee, B05 rating 4,8, B06 checkout noon luggage, B07 kitchen 7 200 ₽ cafe, B08 3 000 ₽ prepayment silence

## Hard constraints

- Two-beat stop-factor guest-night CASE H1 (~50–70 chars) — already happened burn, NOT how-to
- **BAN `HH:MM` in H1** — use «утром», «ночью», «к созвону»; clock digits fail gate
- Number in H1 = ₽ / минут / ночи / **3+ digit token** (800 кбит, 40 минут, 800 ₽) — NOT «5 советов»
- **GATE FAIL:** decimal speeds like 0,8 Мбит/с do NOT count — use 800 кбит, 40 минут, or 800 ₽
- **REWRITE REQUIRED** — previous draft «0,8 Мбит/с» blocked by figure gate
- Good calibration: ««Wi‑Fi для работы». Утром Zoom завис на 40 минут» or «Снял квартиру посуточно. Утром созвон — сеть на 800 кбит»
- NOT how-to, NOT «N советов», NOT «разберём», NOT SEO tail
- Ban: как снять, что проверить, N советов/шагов, разберём, topic label, ЕГРН, ипотека, Клышин, Шакин
- «Тюмень» in H1 optional
- Fields: topic_id, h1, title, title_tag, meta_description, slug, subject, angle, klyshin_title_shape (1–10), dzen_pattern, wordstat_p0, two_beat_check, verdict: PASS
- slug: snyal-kvartiru-posutochno-sozvon-v-10-00-wi-fi-ne-tyanet
