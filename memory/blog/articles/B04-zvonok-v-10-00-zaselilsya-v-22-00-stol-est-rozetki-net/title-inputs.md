# Title inputs B04

topic_id: B04
tenant: Добрый дом (ПКОМПАНИИ), Тюмень, посуточная аренда, комфорт+
season_context: лето 2026, командировочный гость

slug_confirmed: zvonok-v-10-00-zaselilsya-v-22-00-stol-est-rozetki-net

Read: research-notes.md, memory/scout/.cursor/excalibur-blog-handoff.md, published-titles-only.md

Output ONLY valid title-brief.json (JSON object, no markdown wrapper, no commentary).

## Scout handoff / klyshin_hook

- Hook: sept_business_trip — «Звонок в 10:00. Заселился в 22:00.»
- Original Klyshin shape: короткий удар — время созвона vs время заселения; сцена, куда кинут
- Angle: стол, розетки, реальный Wi‑Fi для видеосвязи, закрывающие документы — что спросить ДО оплаты
- Klyshin Aug 2026 editorial map: «Сначала деньги под контролем. Потом договор.» → закрывающие/реквизиты/рабочее место до предоплаты
- dzen_pattern: 2 — живой кейс с временем (10:00 vs 22:00)
- dzen_shape_hint: cable pain-scene + consequence; NOT «5 советов», NOT «7 шагов», NOT label head, NOT SEO tail

## Wordstat P0 (demand spine under H1, do NOT paste raw phrase into H1)

- «квартиры посуточно тюмень» — 5534 (55+11176); RU 225 — 12553
- Secondary: «снять квартиру посуточно в тюмени» 1749; «аренда квартиры посуточно» 811
- Hook-local angle only: «командировка квартира» 41 Tyumen / 4188 RU

## Anti-dup (published-titles-only)

- B01: «Оплатил квартиру посуточно. Код прислали от чужой двери» — do NOT repeat codes/door/check-in angle
- B02: «Снял квартиру посуточно. Залог не вернули — нашли скол на плите» — do NOT repeat deposit angle
- B03: «Привезли сына к вузу — «рядом» оказалось 40 минут пешком» — do NOT repeat university/district angle
- Sibling blog anti-dup: «Гость снял квартиру на сутки: в 10:00 работал, к 22:00 искал кабель» — do NOT angle on cable search story; our angle is checklist BEFORE payment (desk/outlets/Wi‑Fi/docs)

## Hard constraints

- Klyshin rhythm: short punch, scene, cable pain + consequence (~50–70 chars)
- H1 may be WITHOUT «Тюмень»
- Voice: ПКОМПАНИЯ «Добрый дом», комфорт+, спокойный практический тон
- Subject: посуточная аренда для командировочного — созвон утром, заселение вечером, рабочее место
- Ban: «5 советов», «7 шагов», «полный гайд», «2026», SEO tail, label head, ЕГРН, наследство, ипотека, риэлтор, залог as central theme
- Number in H1 = time (10:00, 22:00), ₽ — NOT list count
- One variant only, verdict: PASS
- Include: topic_id, h1, title (same as h1), slug (confirmed), subject, angle, dzen_hints (pattern, lead_hint, stickers, h2_candidates), wordstat, pain_scene, checks, rejected_variants, generated_via

## Research pain facts (for scene calibration)

- Командировочный день: созвон/видеовстреча ~10:00, рейс приходит вечером, заселение около 22:00
- В объявлении галочки «Wi‑Fi», «рабочий стол», «отчётные документы» — без розетки у стола, без скорости, без срока чека
- «Рабочий стол» может быть кухонной стойкой без розетки
- «Быстрый Wi‑Fi» без цифр — не факт для видеосвязи в 10:00
- Закрывающие «потом» = мина для бухгалтерии
- Противоречие в карточках: «заселение до 21:00» и «круглосуточно» одновременно
- Strong scene elements: стол есть / розетки нет; созвон в 10:00; заселился в 22:00; чек «потом»
