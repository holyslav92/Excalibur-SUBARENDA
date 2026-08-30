# Title inputs B04

Read: research-notes.md, .cursor/excalibur-blog-handoff.md, published-titles-only.md, shared/article-style.md
Output ONLY valid title-brief.json (JSON object, no markdown wrapper).

## topic_id
B04

## tenant
«Добрый дом», Тюмень, посуточная аренда

## klyshin_hook
passport_photo_before_pay | original: «Попросили фото паспорта в чат. До оплаты.» | angle: что можно прислать, что нельзя, когда норма хоста vs разворот; moral: сначала договорённость/бронь, потом документы

## title_draft (Scout)
Попросили фото паспорта до перевода. Что отвечать — и что не слать

## dzen_pattern
3 — Страх → сцена в §1 (risk money/housing). NOT numbered list. NOT «5 вопросов» / «7 шагов».

## dzen_shape_hint
«фото паспорта до перевода — что отвечать»

## reader_problem
Гость не понимает, является ли просьба прислать фото паспорта до перевода денег обычной процедурой хоста или признаком мошенничества; боится потерять деньги и передать персональные данные незнакомцу.

## pain_scene (must map to H1)
В переписке перед поездкой хост просит фото паспорта раньше адреса, понятных условий и оплаты через проверенный способ. Гость застрял между «отказаться — потерять жильё» и «отправить — рискнуть данными».

## angle (Title draft)
Passport photo requested BEFORE payment for short-term rental. Cable case + consequence — scene where it hurts, what to do today. Klyshin rhythm: short punch.

## wordstat P0 (demand spine under H1)
- final P0: «паспорт при заселении в квартиру посуточно» — 99 (RF 225)
- secondary: «фото паспорта при заселении в квартиру посуточno» — 52 (225)
- local spine: «квартиры посуточно тюмень» — 5500 (55+11176)

## season_context
Август 2026, перед учебным сезоном — родители и студенты бронируют посуточно.

## DO NOT duplicate (published titles)
- B01: Оплатил квартиру посуточно. Код прислали от чужой двери
- B02: Снял квартиру посуточно. Залог не вернули — нашли скол на плите
- B03: Привезли сына к вузу — «рядом» оказалось 40 минут пешком

## DO NOT repeat angles
- B01: код от чужой двери, бесконтактное заселение
- B02: залог, скол на плите, невозврат на выезде
- B03: «рядом с вузом», расстояние пешком

## BANNED in H1
- «5 вопросов», «7 шагов», numbered list skeleton
- «что проверить первым», «полный гайд», «2026», SEO tails
- ЕГРН, наследство, ипотека, Шакин, риэлтор
- Label head («Проверка заселения», «Паспорт при заселении» as dry label)
- Duplicate B01 codes/deposit angles

## H1 rules
- ~50–70 characters
- «Тюмень» in H1 NOT required
- Cable case + consequence (guest daily-rental pain)
- Number = ₽, nights, minutes — NOT list count
- One variant only, verdict PASS
- JSON fields: topic_id, h1, title, subject, angle, pain_scene, wordstat (p0, p0_frequency, secondary, secondary_frequency), checks (array), rejected_variants (array), verdict

## Good shape examples (own text, not copy)
- «Залог 5 000 ₽: на выезде сказали — не вернём»
- «Почти перевели предоплату — собаку не пустили»
- «23:40 — код есть, из крана холодное»

Задача: один H1 в ритме Klyshin — короткий удар, сцена где больно, последствие/граница. Pattern 3: страх → сцена. Wordstat P0 под H1, не legal essay.
