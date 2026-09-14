# Scout inputs — 2026-09-14 YEKT (Добрый дом, слот B23)

## ОБЯЗАТЕЛЬНО (дирижёр уже выполнил)
- MCP-KV Wordstat preflight: **OK** (wordstat_get_user_info успешен 2026-09-14)
- Частоты ниже — **live**, не выдумывать. Тебе **не нужно** вызывать MCP.
- **Не возвращай SCOUT BLOCK.** Верни только handoff в ```md блоке по формату B18.

## Дата и слот
- today: 2026-09-14, понедельник, сентябрь (Asia/Yekaterinburg)
- season_visual: ранняя осень, тёплый день, НЕ зима на обложке
- topic_id: **B23**
- director angle: **checkout cleaning fee / «уборка включена» → доплата за «грязное бельё» на выезде** (guest CASE, not guide; NOT legal Klyshin)

## Published titles (anti-dup, ledger B01–B22)

| topic_id | title |
|----------|-------|
| B20 | Написали «горячая вода есть». Ночью — ледяной душ и 80 минут до тепла |
| B21 | Ранний заезд оплатили. У двери с чемоданом — почти 5 часов ожидания |
| B22 | Оплатили 3 ночи. Фото паспорта в чат — код не пришёл, багаж у двери |

### Last N=3 (angle rotation)
- B22: паспорт в чат / код не пришёл / burn-at-door
- B21: ранний заезд / уборка до 14:00
- B20: бойлер / горячая вода

**burn-at-door skip:** последние 3 включают B22 (код/дверь) и B21 (у двери) — новый угол НЕ у двери при заселении, а **на выезде**, доплата за уборку/бельё.

### WP extra (не в ledger, НЕ дублировать H1)
- napisali-mozhno-s-sobakoj-u-dveri-doplatili-3-000 (собака)
- zalog-5-000-obeschali-vernut-utrom (залог утром)
- kvartira-posutochno-lift-pyatyj-etazh (лифт)
- posutochno-v-tyumeni-napisali-teplo-est-batarei-holodnye (батареи)

Запрет дублей: код/ключница/паспорт (B01,B13,B18,B22), залог-скол (B02), коммуналка-счётчики (B17), полотенца одно (B11), ранний заезд (B21), бойлер (B20), всё включено такси (B10).

## Klyshin hook (guest pain, mechanics only)

- hook_id: **deposit_cleaning** (unpark from parked_hooks)
- original: «Три ночи. В объявлении — «уборка включена». На выезде — фото простыни и доплата 1 800 ₽.»
- angle: маркетинг «уборка в цене» / «финальная уборка включена» vs счёт на выезде за «грязное бельё» или «не убрали кухню»; гость уже сдаёт ключи, поезд через 2 часа
- lockpick_question: «Уборка и бельё входят в цену или отдельно — и кто решает, что «грязно»?»
- refusal beat: «Нет. Так не сдаём.» / «Сначала правила уборки в переписке. Потом ключ.»
- klyshin_signal: moral «сначала правила/что включено, потом деньги на выезде» — ритм Клышина, не Москва/ЕГРН
- dzen_pattern: **2** (кейс с суммами и датами)
- title_draft (two-beat): «Написали «уборка включена». На выезде — 1 800 ₽ за «грязные простыни»»

## Wordstat (live MCP-KV, дирижёр проверил)

preflight: wordstat_get_user_info OK

probes (дирижёр):
| phrase | 55+11176 | 225 |
|--------|----------|-----|
| уборка посуточно | — | 2018 (host bias: вакансии) |
| уборка на выезде посуточно | empty | empty |
| постельное белье посуточно | — | 239 |
| стиральная машина посуточно | 2 | 57 |
| квартиры посуточно тюмень | 4805 | — |
| аренда квартиры посуточно | 640 | — |

rework_log (для handoff):
probe «уборка на выезде посуточно» empty → «уборка посуточно» 2018 (225, host jobs) → «постельное белье посуточно» 239 (225) → «доплата за уборку посуточно» weak → final P0 «квартиры посуточно тюмень» 4805 (55+11176) | supporting guest cluster «постельное белье посуточно» 239

final_p0: «квартиры посуточно тюмень» — 4805 (55+11176)

## Director mandate
- CASE only, 1100–1800 words, holyslav §1
- Voice: «Я хост посуточной в Тюмени. Это «Добрый дом».»
- Funnel once at end; mid-article question → t.me/Dobriy_dom_72 or MAX
- 3–4 /blog/ crosslinks to published siblings
- Cover: early autumn Tyumen, NOT winter

Верни полный handoff в формате ```md блока как B18/B10.
