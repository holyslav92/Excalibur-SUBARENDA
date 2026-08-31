# Title inputs B05

topic_id: B05
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: август 2026, позднее лето — командировка/рейс, позднее заселение

Read: .cursor/excalibur-blog-handoff.md, research-serp.json, published-titles-only.md
(research-notes.md ещё не готов — не использовать stub; угол только из handoff + SERP)

Output ONLY valid title-brief.json (JSON object, no markdown wrapper, no commentary).

## Scout handoff / klyshin_hook

- Hook: sept_business_trip | original: «Звонок в 10:00. Заселился в 22:00.» | rework → бойлер/горячая вода после позднего заселения
- title_draft (calibration): «Горячая вода была. На второй минуте душ — холод»
- dzen_pattern: 2 (кейс с последствием)
- dzen_shape_hint: «Горячая вода была. На второй минуте душ — холод» / «Заселились поздно. Бойлер «есть» — в инструкции мелким: греть 40 минут»
- klyshin_title_shape: prefer 1 ([действие]. А потом [катастрофа]) or 2 ([утверждение]. Только [опровержение])
- reader_pain: гость после рейса заселяется поздно, лезет в душ — горячая вода кончилась через минуту-две; бойлер маленький или выключен, «греть 40 минут» спрятано в инструкции
- signal: https://t.me/klyshin_A (delivery: quote → break → moral — сначала вода, потом ключ)

## Wordstat P0 (demand spine under H1 — не вставлять сырую фразу в H1)

- «квартиры посуточно тюмень» — 5463 (55+11176); RU «аренда квартиры посуточно» 45250
- «бойлер горячая вода» — 374 (Tyumen 55+11176)
- «горячая вода квартира» — 30961 (225)

## SERP angle (research-serp, без research-notes)

- Конкуренты = how-to про смеситель/подмес в многоэтажке — НЕ наш кейс
- Наш угол: посуточная квартира, бойлер на 40–80 л, гость не знал про нагрев
- Факт из SERP snippet (gkhnews): «стандартные 100 л — горячая кончается на втором душе» — калибровка объёма, не копировать в H1 дословно
- Lockpick для статьи (не в H1): где бойлер, сколько минут греть, включён ли

## Anti-dup (published-titles-only)

- B01: код от чужой двери / бесконтакт — не повторять check-in/code
- B02: залог / скол на плите — не депозит
- B03: «рядом с вузом» / 40 минут пешком — не расстояние/карта
- B04: доплата за третьего у двери — не extra guest fee
- Не повторять недавние WP: Wi-Fi, 10:00/22:00 dispatch, prepaid occupied, towels, checkout train

## Hard constraints

- Two-beat stop-factor CASE H1 (~50–70 chars) — уже случившийся ожог гостя
- Аудитория: гость, бронирующий ночь — не host-operator report
- **BAN `HH:MM` в H1** — «поздно»/«ночью» OK, цифровые часы (23:00, 22:00) в заголовке нет
- Число в H1 = минуты ожога / ₽ / ночи — НЕ «5 вопросов», «7 шагов», N советов
- Ban: как снять, что проверить, разберём, лучшие, topic label, SEO tail, 2026, ЕГРН, наследство, ипотека, риэлтор, Клышин
- «Тюмень» в H1 не обязательна
- Свой текст — rhythm from Klyshin only, never paste @klyshin_A plots
- Include: topic_id, h1, title (same as h1), subject, angle, klyshin_title_shape (1–10), verdict: PASS
- Optional richness like B02: pain_scene, wordstat, checks, rejected_variants

## Preferred H1 direction (one variant)

Shape: «Горячая вода была. На второй минуте душ — холод» — two beats, minutes = burn number, guest shower scene, no how-to label.
