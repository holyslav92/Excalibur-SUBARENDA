# Title inputs B04

topic_id: B04
tenant: Добрый дом (ПКОМПАНИИ), Тюмень, посуточная аренда
season_context: лето 2026, командировка на 2 ночи, поздний заезд ~22:00, видеосозвон в 10:00

Read: research-notes.md, published-titles-only.md, memory/scout/.cursor/excalibur-blog-handoff.md

Output ONLY valid title-brief.json (JSON object, no markdown wrapper, no commentary).

## Scout handoff / klyshin_hook

- Hook: sept_business_trip — original: «Звонок в 10:00. Заселился в 22:00.»
- Angle: рабочий стол + Wi‑Fi на видеосозвон + закрывающие документы (чек/акт/счёт) ДО оплаты — не «пришлём после выезда»
- dzen_pattern: 3 (страх → сцена в §1)
- dzen_shape_hint: «Две ночи в командировке: созвон в 10:00 — Wi‑Fi и закрывающие до перевода, не «пришлём потом»»
- Klyshin rhythm: «сначала проверка, потом деньги» — редакционный перенос на командировку
- NOT розетка (WP duplicate «Звонок в 10:00… у стола нет розетки»)

## Wordstat P0 (demand spine under H1, do NOT paste raw phrase into H1)

- «квартиры посуточно тюмень» — 5523 (55+11176); RU 225 — 12487
- Secondary: «снять квартиру посуточно в тюмени» 1755; «аренда квартиры посуточно» 794
- Tertiary: «договор посуточной аренды квартиры» 44

## Anti-dup (published-titles-only)

- B01: «Оплатил квартиру посуточно. Код прислали от чужой двери» — NOT code/door/check-in
- B02: «Снял квартиру посуточно. Залог не вернули — нашли скол на плите» — NOT deposit
- B03: «Привезли сына к вузу — «рядом» оказалось 40 минут пешком» — NOT university/walk
- WP sibling: NOT розетка / power outlet angle

## Hard constraints

- Klyshin rhythm: TWO beats — (1) scene with time, (2) illusion break / consequence, NOT checklist «нужны X и Y»
- Shape calibration (свой текст): «Заселился в 22:00. В 10:00 созвон — закрывающие «пришлём после»» OR «Заселился в 22:00 — в 10:00 созвон, а закрывающие обещают после выезда»
- Second clause must be broken promise or damage (документы потом, бухгалтерия не примет), NOT «что проверить»
- ~50–70 chars total
- H1 may be WITHOUT «Тюмень»
- Subject: посуточная аренда, командировка, поздний заезд 22:00, утренний видеосозвон 10:00, закрывающие документы
- Ban: «5 вопросов», «7 шагов», «полный гайд», «2026», SEO tail, label head, ЕГРН, наследство, ипотека, риэлтор, Шакин
- Number in H1 = time (22:00, 10:00), nights, ₽ — NOT list count
- One variant only, verdict: PASS
- Required fields: topic_id, h1, title (same as h1), subject, angle, verdict: PASS
- Optional richness like B02: pain_scene, wordstat, checks, rejected_variants

## Research pain facts (for scene calibration)

- Заселение в 22:00 → утром в 10:00 сразу видеосозвон; мало времени проверить квартиру ночью
- «Есть Wi‑Fi» не гарантирует скорость для Zoom (720p ~1.2–2.6 Мбит/с)
- Стол и стул нужно запрашивать отдельно
- Закрывающие «пришлём после выезда» — риск: авансовый отчёт за 3 рабочих дня, бухгалтерия может не принять
- Самозанятый без чека «Мой налог» — договор может не хватить
