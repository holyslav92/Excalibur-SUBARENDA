# Scout inputs — 2026-09-16 YEKT (Добрый дом, слот B24)

## ОБЯЗАТЕЛЬНО (дирижёр уже выполнил)
- MCP-KV Wordstat preflight: **OK** (wordstat_get_user_info успешен 2026-09-16)
- Частоты ниже — **live**, не выдумывать. Тебе **не нужно** вызывать MCP.
- **Не возвращай SCOUT BLOCK.** Верни только handoff в ```md блоке по формату B23.

## Дата и слот
- today: 2026-09-16, среда, ранняя осень (Asia/Yekaterinburg)
- season_visual: сентябрь, тёплый день, НЕ зима на обложке
- topic_id: **B24**
- director angle: **«можно с детьми» в карточке → доплата за ребёнка на заселении** (guest CASE, not guide; NOT legal Klyshin)

## Published titles (anti-dup, ledger B01–B23)

| topic_id | title |
|----------|-------|
| B21 | Ранний заезд оплатили. У двери с чемоданом — почти 5 часов ожидания |
| B22 | Оплатили 3 ночи. Фото паспорта в чат — код не пришёл, багаж у двери |
| B23 | В карточке: «уборка включена» — 3 ночи. Выезд: фото простыни — 1 800 ₽ |

### Last N=3 (angle rotation)
- B23: уборка на выезде / бельё
- B22: паспорт / код / burn-at-door
- B21: ранний заезд / у двери

**burn-at-door skip:** последние 3 включают B22 и B21 — новый угол НЕ «код не пришёл» и НЕ «ждём у двери часами», а **доплата за ребёнка после брони** (семейный кейс).

### WP extra (не в ledger, НЕ дублировать H1)
- zalog-5000-obeshchali-utrom-posle-uborki-bez-sroka (залог утром — сегодня на WP)
- sobaka-do-15-kg-doplata-u-dveri (собака)
- napisali-stiralnaya-est-v-kvartire-tolko-rakovina (стиралка)
- vyezd-v-polden-v-11-45-poprosili-900-za-lishnij-chas (лишний час)

Запрет дублей: код/ключница/паспорт (B01,B13,B18,B22), залог (B02 + WP сегодня), коммуналка (B17), уборка/бельё (B23), собака (WP), ранний заезд (B21), бойлер (B20), всё включено такси (B10), третий гость (B04).

## Klyshin hook (guest pain, mechanics only)

- hook_id: **kids_extra_fee** (новый guest hook, mechanics Klyshin)
- original: «В карточке — «можно с детьми». На заселении — «за ребёнка отдельно» 1 500 ₽.»
- angle: маркетинг «family friendly» / «можно с детьми» без цены в карточке → доплата при заселении за ребёнка, кроватку, постель; гость уже оплатил 2–3 ночи, ребёнок 5–7 лет
- lockpick_question: «Ребёнок входит в цену или доплата — и с какого возраста?»
- refusal beat: «Нет. Так не заселяем.» / «Сначала правила по детям в переписке. Потом ключ.»
- klyshin_signal: moral «сначала правила/возраст/доплата, потом деньги» — ритм Клышина, не Москва/ЕГРН
- dzen_pattern: **2** (кейс с суммами и датами)
- title_draft (two-beat): «Написали «можно с детьми». У двери — 1 500 ₽ за ребёнка»

## Wordstat (live MCP-KV, дирижёр проверил)

preflight: wordstat_get_user_info OK

probes (дирижёр):
| phrase | 55+11176 | 225 |
|--------|----------|-----|
| квартира посуточно с детьми | — | 239 |
| снять квартиру посуточно с детьми | — | 168 |
| квартиры посуточно тюмень | 4724 | — |
| отели тюмень | 7102 | — |
| посуточно или отель | 7 | — |
| доплата за ребенка посуточно | — | 14 |

rework_log (для handoff):
probe «доплата за ребенка посуточно» 14 (225) → «квартира посуточно с детьми» 239 (225) → «снять квартиру посуточно с детьми» 168 → supporting «отели тюмень» 7102 (contrast, не P0) → final P0 «квартиры посуточно тюмень» 4724 (55+11176) | guest cluster «квартира посуточно с детьми» 239

final_p0: «квартиры посуточно тюмень» — 4724 (55+11176); supporting guest cluster «квартира посуточно с детьми» — 239 (225)

## Director mandate
- CASE only, 1100–1800 words, holyslav §1
- Voice: «Я хост посуточной в Тюмени. Это «Добрый дом».»
- Funnel once at end; mid-article question → t.me/Dobriy_dom_72 or MAX
- 3–4 /blog/ crosslinks to published siblings
- Cover: early autumn Tyumen, family at door scene, NOT winter

Верни полный handoff в формате ```md блока как B23.
