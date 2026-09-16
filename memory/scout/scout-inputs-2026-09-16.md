# Scout inputs — 2026-09-16 YEKT slot (17:00)

## Date context
- today_iso: 2026-09-16
- timezone: Asia/Yekaterinburg
- weekday: вторник
- season: середина сентября, осень (обложка — текущий сезон, не зима)

## Tenant
- Добрый дом, посуточная аренда Тюмень
- dzen_pattern prefer 2–5 (NOT numbered list default)
- Guest pains only — NO ЕГРН/суд/наследство/Москва/риэлтор/Шакин

## Published titles (anti-dup, last 8)
| topic_id | title |
| B17 | «Коммуналка включена». На выезде — счётчики и 1 840 ₽ |
| B18 | Код уже есть. Только в подъезд не попасть — 20 минут с чемоданом |
| B19 | Написали «не курили». В спальне — запах и окно на замке |
| B20 | Написали «горячая вода есть». Ночью — ледяной душ и 80 минут до тепла |
| B21 | Ранний заезд оплатили. У двери с чемоданом — почти 5 часов ожидания |
| B22 | Оплатили 3 ночи. Фото паспорта в чат — код не пришёл, багаж у двери |
| B23 | В карточке: «уборка включена». Выезд: фото простыни — 1 800 ₽ |
| B24 | «Можно с детьми» в карточке. При заезде: 1 500 ₽ за 2 ночи, 6-летнему |

## WP recent anti-dup (titles only, do NOT repeat angle)
- Залог 5 000 ₽ обещали утром. После уборки — без срока
- Выезд в полдень. За четверть часа — 900 ₽ за «лишний час»
- На фото — стиралка. На третий день — прачечная за 600 ₽
- В чате: «собака до 15 кг». У двери: «крупная» — 2 500 ₽
- Написали «лифт есть». За 8 400 ₽ — пятый этаж пешком

## Angle rotation (last N=3: B22,B23,B24)
- burn-at-door (код/паспорт/дверь): skip — B22 in last 3
- cleaning fee on checkout: skip — B23 just published
- children extra fee: skip — B24 just published
- sleeping_places_mismatch: ACTIVE — fresh guest pain, not in ledger

## Klyshin hook (new guest angle)
- hook_id: sleeping_places_mismatch
- original angle: «Две кровати на фото. Ночью второй гость — на диване и складном матрасе»
- lockpick: «Сколько спальных мест и что именно — кровать или диван?»
- moral: сначала фото/план спальных мест, потом оплата
- dzen_pattern: 2 (кейс с суммами и датами)

## Wordstat preflight
- wordstat_get_user_info: OK (Yandex Cloud API, 2026-09-16)

## Wordstat live probes (MCP-KV)

### P0 spine
- «квартиры посуточно тюмень» RU 225: 10016 | Tyumen 55+11176: 4724
- «снять квартиру посуточно в тюмени» RU: 3542 | Tyumen: 1452

### Hook probes
- «спальные места посуточно» RU 225: 131 (guest intent — sleeping arrangement)
- «спальное место посуточно» RU 225: 131
- «диван вместо кровати аренда» RU 225: empty/weak
- «посуточно или отель» Tyumen 55+11176: 7 (weak — not P0)

### Rework log
1. probe «спальные места посуточно» 131 (225) → guest sleeping-arrangement intent confirmed
2. probe «диван вместо кровати» weak → ride spine P0
3. rework «аренда квартиры посуточно» 38507 (225) / 679+ local → spine
4. final P0 «квартиры посуточно тюмень» 4724 (55+11176) / 10016 (225)

### Final P0
- phrase: «квартиры посуточно тюмень»
- volume: 10016 (RU 225), 4724 (55+11176)
- guest intent: book apartment for N guests — verify real beds vs sofa before pay

## Title draft (two-beat, NOT final Title role)
«Две кровати на фото. Ночью — диван и складной матрас»

## topic_id
B25

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/

## Task
Write the complete scout handoff markdown. The calling script saves your reply to `.cursor/excalibur-blog-handoff.md`.

**OUTPUT RULES (HARD):**
- Return ONLY the handoff markdown body (no refusal, no DEROUTER SCOUT BLOCKER).
- Include all required lines: topic_id, title_draft, klyshin_hook, wordstat_rework, wordstat, angle_rotation, dzen_pattern, dzen_shape_hint, signal_urls, external_signal, opening_direction, moral, lockpick_question, anti_dup_guard.
- Wordstat frequencies are already verified live in this prompt — use them as-is.
