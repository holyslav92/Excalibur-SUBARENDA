# Title inputs B03

topic_id: B03
tenant: Добрый дом (ПКОМПАНИИ), Тюмень, посуточная аренда
season_context: август 2026, бронь перед 1 сентября; родители с будущим студентом на 2–4 ночи

Read: research-notes.md, published-titles-only.md, assembled-research-inputs.md (Scout handoff summary)

Output ONLY valid title-brief.json (JSON object, no markdown wrapper, no commentary).

## Scout handoff / klyshin_hook

- Hook: parents_sept_uni — привёз сына в вуз на 2–4 ночи; в объявлении «рядом с вузом», на деле три остановки.
- Original Klyshin shape: «Привёз сына в вуз. Три ночи. В объявлении — «рядом с вузом».»
- Angle: минуты пешком до **конкретного корпуса** на карте; lockpick: сколько минут пешком до корпуса?
- dzen_pattern: 5 (локальный + сезонный) + 2 (живой кейс)
- dzen_shape_hint: cable pain-scene + consequence; NOT «5 советов», NOT «гайд», NOT list skeleton in H1

## Wordstat P0 (demand spine under H1, do NOT paste raw phrase into H1)

- «квартиры посуточно тюмень» — 5534 (55+11176); RU 225 — 12553
- Secondary: «снять квартиру посуточно в тюмени» 1749; «квартиры посуточно тюмень рядом» 79

## Anti-dup (published-titles-only)

- B01: «Оплатил квартиру посуточно. Код прислали от чужой двери» — do NOT repeat codes/check-in angle
- B02: «Снял квартиру посуточно. Залог не вернули — нашли скол на плите» — do NOT repeat deposit angle
- Sibling anti-dup: «Приехали на 3 ночи к вузу — три остановки. Кровати не хватило» — do NOT angle on beds/sleeping places

## Hard constraints

- Klyshin rhythm: short punch, scene, cable pain + consequence (~50–70 chars)
- H1 may be WITHOUT «Тюмень»
- Subject: посуточная аренда квартиры, родители перед 1 сентября, «рядом с вузом» vs реальный маршрут
- Ban: «5 советов», «7 шагов», «полный гайд», «2026», SEO tail, label head, ЕГРН, наследство, ипотека, риэлтор
- Number in H1 = minutes, stops, nights, ₽ — NOT list count
- One variant only, verdict: PASS
- Include: topic_id, h1, title (same as h1), subject, angle, verdict; follow B02 title-brief.json richness (pain_scene, wordstat, checks, rejected_variants) if useful

## Research pain facts (for scene calibration)

- «Рядом с вузом» может значить район, остановку с названием вуза или пешую доступность — не одно и то же
- «Три остановки» — маршрут на транспорте, не пешком
- У ТюмГУ несколько корпусов (Володарского, Ленина, Семакова, Пржевальского, 8 Марта, Республики 9)
- Reader checks route on map пешком before payment
