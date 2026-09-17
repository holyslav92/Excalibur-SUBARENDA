# B26 Research inputs — assembled 2026-09-17

## Topic

- topic_id: B26
- title draft: «Квартира на пятом. Лифт не едет — и чемодан уже не в такси»
- format: guest CASE (после дороги/такси, у подъезда), NOT guide, NOT legal/ЕГРН/суд/наследство
- tenant: Добрый дом, посуточная аренда Тюмень
- research_date: 2026-09-17 (Asia/Yekaterinburg)

## Scout handoff (floor_elevator_luggage)

- klyshin_hook: floor_elevator_luggage | original: «Квартира на пятом. Лифт не едет — чемодан уже не в такси»
- angle: гость с багажом; в карточке этаж/лифт не проговорены до оплаты; у подъезда табличка «лифт не работает»; механика — сначала этаж и лифт, потом оплата
- lockpick_question: «На каком этаже и лифт сейчас работает?»
- refusal line: «Нет. Так не заселяем.»
- signal_urls: https://t.me/klyshin_A
- dzen_pattern: 2 (case_with_sums_and_dates); shape_hint: этаж / кг чемодана / минуты подъёма

## Published titles overlap guard (do NOT repeat angles)

- B18: код есть, 20 минут у двери с чемоданом (домофон/подъезд, не лифт)
- B06: чемоданы между выездом и поездом (время выезда, не этаж)
- B21: ранний заезд — часы ожидания у двери (не лифт)
- B22-B25: паспорт/уборка/дети/кровати — skip
- WP recent anti-dup title (не повторять H1): «Написали „лифт есть“. За 8 400 ₽ — пятый этаж пешком»
- B26 focus unique: этаж + работоспособность лифта + багаж не раскрыты до оплаты; табличка у подъезда

## Wordstat live (MCP-KV, accessed 2026-09-17)

| phrase | volume | region |
|--------|--------|--------|
| квартиры посуточно тюмень | 4570 | 55+11176 |
| квартиры посуточно тюмень | 9844 | 225 (compare) |
| снять квартиру посуточно в тюмени | 1404 | 55+11176 |
| этаж лифт квартира | 2413 | 225 |
| квартира 5 этаж без лифта | 101 | 225 |
| квартира пятый этаж без лифта | 36 | 225 |
| этаж лифт посуточно | 9 (totalCount only) | 225 — WORDSTAT PARTIAL |
| залог посуточно | 26 | 55+11176 |

Rework log (Scout): «этаж лифт квартира» 2413 (225) → «квартира 5 этаж без лифта» 101 (225) → Tyumen narrow empty → P0 spine «квартиры посуточно тюмень» 4570 (55+11176). National pain cluster: этаж/лифт/багаж.

## Fresh community signals (this week)

### Добрый дом Telegram @Dobriy_dom_72 — свежие посты (fetch 2026-09-17)

Post about closed entrance / check-in path (low views, fresh channel activity):
> Поездку чаще портит не квартира, а закрытый подъезд. Гость поздно уточняет, где взять ключи и что делать, если домофон не откроет. В «Добром Доме» до заезда проясняют чек-ин и доступ… Путь до двери не должен становиться задачей гостя.
URL: https://t.me/Dobriy_dom_72

Post about listing mismatch (still visible in channel feed, ~mid-September 2026):
> Несоответствие квартиры описанию… Гость часто проверяет только цену и район, а детали замечает уже после оплаты.
URL: https://t.me/Dobriy_dom_72

Post about ЖК «Новин» (tenant inventory contrast — скоростные лифты в их сегменте):
> …закрытый охраняемый двор… скоростные лифты…
URL: https://t.me/Dobriy_dom_72

### Klyshin topic bank / Scout signal 2026-09-17

Hook floor_elevator_luggage from angle bank: fifth floor + broken elevator + luggage after taxi; lockpick «На каком этаже и лифт сейчас работает?»
URL: https://t.me/klyshin_A

### Kerch.FM — табличка «лифт не работает» (Aug 2026, evergreen mechanic)

Passengers with heavy suitcases climb stairs while elevator has sign «не работает»; passengers pressed call button — elevator was working. Illustrates: табличка у подъезда ≠ финальный ответ до проверки/уточнения у хозяина.
URL: https://kerchfm.ru/2026/08/25/na-stancii-kerch-juzhnaja-passazhirov-dezinformirujut-o-rabote-lifta.html

## Platform norms — floor & elevator (NOT legal)

### Sutochno.ru listing structure (live cards, Tyumen catalog 2026-09-17)

- Tyumen catalog: ~3 990 offers, prices from ~1 090 ₽/сутки; typical band on first page ~2 400–5 400 ₽/сутки (season/listing dependent).
- Cards show «Этаж X из Y» in header; amenities block can include «лифт» checkbox.
- Example titles on Tyumen page explicitly mention floor: «23 этаж», «12 этаж», «9 этаж», «10 этаж» — floor is a visible filter signal when host fills it.
URL: https://tyumen.sutochno.ru/

### Sutochno.ru blog «Как составить описание» (2025-12-22, fetched 2026-09-17)

- Settings include accessibility/amenities — guest filters depend on checkboxes.
- «Информация и фотографии должны соответствовать фактическому состоянию жилья».
- Checklist: «соответствуют ли фотографии тексту».
URL: https://sutochno.ru/blog/opisanie

### Sutochno.ru blog rules for hosts

- Must disclose conditions upfront; guests dislike surprises after booking.
URL: https://sutochno.ru/blog/rules

## Guest reviews — floor/elevator/luggage pain (live Sutochno, fetched 2026-09-17)

### Listing 1315421 (Moscow, Anna Room) — negative

Guest: «4й этаж без лифта (не обратила внимания, когда бронировала), с чемоданами идти вверх-вниз тяжко»; also asked to carry trash while «мы с чемоданами».
URL: https://www.sutochno.ru/1315421

### Listing 1309701 (Moscow hotel room) — honest disclosure + reviews May 2026

Host text in card: «Мы находимся на 5 этаже без лифта!!!»
Review May 2026: «Единственный минус это отсутствие лифта. Отель находится на 5 этаже.»
Another May 2026: «Нужно быть готовым к проживанию на 5 этаже без лифта.»
URL: https://www.sutochno.ru/1309701

### Listing 2201120 (Moscow) — 5th floor pain with suitcase

Review: «Из минусов пятый этаж без лифта… С чемоданом было сложно подняться»; another: «пятый этаж… подниматься пешком с чемоданами и пакетами тяжело».
URL: https://www.sutochno.ru/2201120

### Listing 1742300 (Magadan) — contrast: low floor as plus

Review Jan 2026: «Квартира на 2м этаже. Не на пятом, не на четвёртом, что при наличии чемоданов является большим плюсом.»
URL: https://sutochno.ru/front/searchapp/detail/1742300

### Listing 2008179 (Volgograd) — 3rd floor as plus for heavy luggage

Review mentions «Квартира находится на 3-м этаже, что в целом является плюсом при поднятии/спуске тяжёлых чемоданов.»
URL: https://sutochno.ru/front/searchapp/detail/2008179

### Hostel review pattern (international, luggage weight anchor)

Guest carried «20-килограммовый чемодан» alone when elevator broken — illustrates weight class, not Tyumen-specific.
URL: https://tropki.ru/shvetsiya/8890-stokgolm-arlanda/419023-hostel-stf-jumbo-stay-stockholm

## Guest mechanics / practical facts

1. Problem split: (a) permanent «без лифта» in old 5-floor building vs (b) high-rise where лифт в карточке есть, но у подъезда табличка «не работает» — разные сценарии, одинаковая боль у двери с чемоданом.
2. Sutochno cards can show «лифт» in amenities AND «Этаж 5 из 9» — guest must read both; checkbox does not guarantee lift works today.
3. Honest hosts sometimes shout in description: «5 этаж без лифта!!!» — when this absent, guest assumes elevator or low floor.
4. Typical Tyumen nightly band on Sutochno catalog first screen: roughly 2 400–5 400 ₽/сутки (wide market); editorial case sum for two nights in tenant canon: 8 400 ₽ (WP anti-dup title reference — editorial scenario, not verified tariff).
5. Luggage weight anchors: 20 kg rolling suitcase (guest review); standard checked airline bag often up to 23 kg — two adults may mean 2×20–23 kg plus hand luggage.
6. Time anchors: wellness article cites ~5 minutes to walk up 5 floors without load; with 20 kg suitcase + breaks + narrow stairwell — plan 8–15 minutes one way; second trip if partner stays below with bags.
7. Early check-in surcharge example from bad stay: 380 ₽/hour when guest waited 2 hours (listing 1315421) — shows paid waiting + stairs compound stress.
8. What to ask BEFORE pay (written):
   - exact floor number and total floors in section;
   - «лифт работает сегодня?» not just «есть лифт»;
   - if tablichka at entrance — who updates guest (building management vs host);
   - help with luggage / can host meet at entrance;
   - entrance from which side (courtyard vs street) — affects taxi drop-off with bags.
9. Direct messenger booking often skips structured «Этаж X из Y» and «лифт» fields — higher need for written answers.
10. Anti-dup vs B18: B18 = can't enter building (domofon); B26 = inside building path but vertical access surprise.

## Editorial case boundary

- Composite Scout case for Добрый дом voice; NOT verified transcript of one Tyumen booking
- Scene: guest arrives by taxi, sees «лифт не работает» tablichka, apartment on 5th floor, paid 8 400 ₽ for two nights before learning vertical access
- Host moral line from Scout: «Нет. Так не заселяем.» — ask floor + working elevator first
- Do NOT drift to legal/ЕГРН, refund law, consumer court, залог, код, уборка, дети, кровати
- Do NOT make h2_outline, FAQ skeleton, lead paragraph
- Do NOT cite tymenrieltor.ru or Excalibur-2-Cloud repo

## official_verifications

N/A — no bank/developer/gov tariff digits. Platform policies cited as Sutochno official context only. Case sums editorial.

## writer_safe_urls (tenant CTA)

- https://t.me/Dobriy_dom_72
- https://t.me/Dobriy_dom_Tyumen
- https://max.ru/id660300569233_biz
- https://добрыйдом-72.рф/
- https://добрыйдом-72.рф/booking/
- https://добрыйдом-72.рф/blog/
- https://tyumen.sutochno.ru/
- https://sutochno.ru/blog/opisanie
- https://sutochno.ru/blog/rules
- https://www.sutochno.ru/1315421
- https://www.sutochno.ru/1309701
- https://www.sutochno.ru/2201120
- https://kerchfm.ru/2026/08/25/na-stancii-kerch-juzhnaja-passazhirov-dezinformirujut-o-rabote-lifta.html

## Derouter synthesis task (HARD)

Ты — Derouter utility tier для роли research. Верни **только** полный markdown-текст файла `research-notes.md` на русском. Скрипт сохранит твой ответ в файл; тебе не нужен доступ к ФС.

Обязательные секции:
research_date, reader_problem, reader_outcome, signal_and_demand, community_signal, practical_facts, editorial_case_boundary, constraints, typical_reader_mistakes, voice_angle, surprising_fact, official_verifications, source_table (accessed_at 2026-09-17 у каждой строки), writer_safe_urls.

Формат — гостевой кейс прибытия с багажом. Только факты — без h2_outline, без lead, без FAQ. Не пиши DEROUTER BLOCKER и не отказывайся.
