# Scout inputs — Добрый дом — 2026-08-26 YEKT (summer)

## Slot
- date_yekt: 2026-08-26
- season: summer 2026, cover = summer (no winter hero)
- tenant: Добрый дом, посуточная аренда Тюмень, комфорт+, voice ПКОМПАНИИ
- dzen_rf_pack: true (read dzen-content-rules + rf-blocked)

## Published / anti-dup
- B01: Оплатил квартиру посуточно. Код прислали от чужой двери (burn-at-door)
- B02: Перевёл залог за посуточную. На выезде сказали: «не вернём»
- Recent WP (do NOT duplicate): парковка шлагбаум, звонок 10:00/заселение 22:00, вуз/родители 3 ночи, горячая вода, соседи ночью, скрытые доплаты, собака, фото паспорта, договор/правила, отмена брони, предоплата/вечеринки, ранний заезд

## Angle rotation (last N=3)
- burn-at-door family: SKIP (B01 + saturated)
- parents_sept_uni: SKIP (WP 2026-08-25 «Приехали на 3 ночи к вузу»)
- sept_business_trip: SKIP (WP 2026-08-25 «в 10:00 работал, к 22:00 искал кабель»)
- parking_before_booking: SKIP (WP 2026-08-26 «парковка рядом — как въехать ночью»)
- early_checkin: SKIP (WP 2026-08-21 ранний заезд)
- Queue slot 26–28.08 was parents_sept_uni → override to unsaturated hook

## Selected hook (Scout decision)
- hook_id: checkout_train_bags
- queue_num: 8
- original Klyshin rhythm: «Выезд в 12:00. Поезд в 16:30.»
- angle: куда деть чемоданы между выездом и поездом; NOT early check-in duplicate
- lockpick: «Где хранить багаж и до скольки?»
- moral: сначала багаж/хранение, потом ключ

## Wordstat live MCP-KV (regions 55+11176; compare 225)
Preflight: wordstat_get_user_info OK

Rework log:
- probe «хранение багажа» → 122 (55+11176)
- probe «хранение багажа тюмень» → 22
- probe «аренда квартиры посуточно» → 821
- probe «квартира посуточно тюмень» / cluster «квартиры посуточно тюмень» → 5675 (55+11176)
- compare RU 225 «квартиры посуточно тюмень» → 12957
- final P0: «квартиры посуточно тюмень» 5675

## Dzen
- pattern: 2 (кейс с суммами и датами) — NOT default list
- shape_hint: выезд 12:00, поезд 16:30, чемоданы/хранение до оплаты продления

## Signal URLs
- https://t.me/klyshin_A — live: проверка до аванса, «сюда деньги не несем» (guest parallel: до выезда уточнить багаж)
- https://dzen.ru/holyslav — сделка сорвалась до нотариуса (проверка до денег)
- https://добрыйдом-72.рф/blog/
- https://t.me/holyslav92

## topic_id
- B03 (next after B01, B02)
