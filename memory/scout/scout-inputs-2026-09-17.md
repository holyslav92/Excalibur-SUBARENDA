# Scout inputs — 2026-09-17 YEKT slot (12:00)

## Date context
- today_iso: 2026-09-17
- timezone: Asia/Yekaterinburg
- weekday: четверг
- season: середина сентября, осень (обложка — текущий сезон, не зима)

## Tenant
- Добрый дом, посуточная аренда Тюмень
- dzen_pattern prefer 2–5 (NOT numbered list default)
- Guest pains only — NO ЕГРН/суд/наследство/Москва/риэлтор/Шакин

## Published titles (anti-dup, last 8)
| topic_id | title |
| B18 | Код уже есть. Только в подъезд не попасть — 20 минут с чемоданом |
| B19 | Написали «не курили». В спальне — запах и окно на замке |
| B20 | Написали «горячая вода есть». Ночью — ледяной душ и 80 минут до тепла |
| B21 | Ранний заезд оплатили. У двери с чемоданом — почти 5 часов ожидания |
| B22 | Оплатили 3 ночи. Фото паспорта в чат — код не пришёл, багаж у двери |
| B23 | В карточке: «уборка включена». Выезд: фото простыни — 1 800 ₽ |
| B24 | «Можно с детьми» в карточке. При заезде: 1 500 ₽ за 2 ночи, 6-летнему |
| B25 | На фото две кровати. Ночью троих — диван и складной матрас |

## WP recent anti-dup (titles only, do NOT repeat angle)
- Заезд с двух. 105 мин с чемоданом: пахнет химией, мокрый пол
- Залог 5 000 ₽ обещали утром. После уборки — без срока
- Выезд в полдень. За четверть часа — 900 ₽ за «лишний час»
- На фото — стиралка. На третий день — прачечная за 600 ₽
- В чате: «собака до 15 кг». У двери: «крупная» — 2 500 ₽

## Angle rotation (last N=3: B23,B24,B25)
- cleaning fee on checkout: skip — B23
- children extra fee: skip — B24
- sleeping_places_mismatch: skip — B25 just published
- burn-at-door (код/паспорт/дверь): skip — B22 recent in ledger
- hotel_vs_daily price contrast: ACTIVE — fresh guest pain, not in ledger

## Klyshin hook (parked → restored)
- hook_id: hotel_vs_daily
- original angle: «Считали квартиру дешевле отеля. На две ночи — на 2 900 ₽ дороже»
- lockpick: «Что входит в цену за сутки — уборка, бельё, сервисный сбор?»
- moral: сначала полный расчёт двух ночей vs отель, потом оплата
- dzen_pattern: 4 (контраст посуточно vs отель на 2 ночи)

## Wordstat preflight
- wordstat_get_user_info: OK (Yandex Cloud API, 2026-09-17)

## Wordstat live probes (MCP-KV)

### Hook probes
- «посуточно или отель» RU 225: 370 | Tyumen 55+11176: 7
- «квартира посуточно или отель» RU 225: 283 | Tyumen: 5
- «отели тюмень» Tyumen 55+11176: 7141 | RU 225 (related): 23237
- «постельное белье посуточно» RU 225: 226 (weak host bias — not P0)

### Rework log
1. probe «посуточно или отель» 370 (225) / 7 local → guest contrast intent confirmed
2. probe «скрытая доплата посуточно» empty → rework to price-compare cluster
3. probe «квартира посуточно или отель» 283 (225) → angle spine for contrast case
4. supporting «отели тюмень» 7141 local / 23237 RU — hotel benchmark demand
5. final P0 «квартиры посуточно тюмень» 4570 (55+11176) / 9844 (225)

### Final P0
- phrase: «квартиры посуточно тюмень»
- volume: 9844 (RU 225), 4570 (55+11176)
- guest intent: compare flat vs hotel total for 2 nights before pay — hidden line items

## Title draft (two-beat, NOT final Title role)
«На карточке — 4 200 за ночь. Отель рядом — 4 800. Счёт на две ночи — 13 400»

## topic_id
B26

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/

## Task
Write the complete scout handoff markdown. The calling script saves your reply to `.cursor/excalibur-blog-handoff.md`.

**OUTPUT RULES (HARD):**
- Return ONLY the handoff markdown body (no refusal, no DEROUTER SCOUT BLOCKER).
- Include all required lines: topic_id, title_draft, klyshin_hook, wordstat_rework, wordstat, angle_rotation, dzen_pattern, dzen_shape_hint, signal_urls, external_signal, opening_direction, moral, lockpick_question, anti_dup_guard.
- Wordstat frequencies are already verified live in this prompt — use them as-is.
