# Scout inputs — 2026-09-18 YEKT slot (12:00)

## Date context
- today_iso: 2026-09-18
- timezone: Asia/Yekaterinburg
- weekday: пятница
- season: середина сентября, ранняя осень (обложка — осень, НЕ зима)

## Tenant
- Добрый дом, посуточная аренда Тюмень
- dzen_pattern prefer 2–5 (NOT numbered list default)
- Guest pains only — NO ЕГРН/суд/наследство/Москва/риэлтор/Шакин

## Published titles (anti-dup, last 8)
| topic_id | title |
| B19 | Написали «не курили». В спальне — запах и окно на замке |
| B20 | Написали «горячая вода есть». Ночью — ледяной душ и 80 минут до тепла |
| B21 | Ранний заезд оплатили. У двери с чемоданом — почти 5 часов ожидания |
| B22 | Оплатили 3 ночи. Фото паспорта в чат — код не пришёл, багаж у двери |
| B23 | В карточке: «уборка включена». Выезд: фото простыни — 1 800 ₽ |
| B24 | «Можно с детьми» в карточке. При заезде: 1 500 ₽ за 2 ночи, 6-летнему |
| B25 | На фото две кровати. Ночью троих — диван и складной матрас |
| B26 | «Можно с собакой» написали. При заезде — 2 500 ₽ за «крупную породу» |

## WP recent anti-dup (titles only, do NOT repeat angle)
- Написали «без залога». Перед кодом просят 5 000 ₽ на карту
- Квартира на пятом этаже. Лифт встал — 2 ночи, чемодан внизу
- Квартира дешевле отеля за ночь. За две ночи — 13 400 ₽
- Заезд с двух. 105 мин с чемоданом: мокрый пол, «ещё пять»
- Залог 5 000 ₽ обещали утром. После уборки — без срока
- На фото — стиралка. На третий день — прачечная за 600 ₽

## Angle rotation (last N=3: B24,B25,B26)
- children extra fee: skip — B24
- sleeping places mismatch: skip — B25
- dog breed fee: skip — B26
- cold_radiators_heating_sept: ACTIVE — seasonal autumn guest pain, NOT hot_water_boiler (B20 GVS), NOT neighbors (B14)

## Klyshin hook (new guest angle)
- hook_id: cold_radiators_heating_sept
- original angle: «Написали «отопление есть». В комнате +14 °C — батареи холодные»
- lockpick: «Когда в Тюмени включают отопление и кто отвечает, если батареи ледяные?»
- moral: сначала проверка тепла/батарей (или обогреватель в комплекте), потом ночь
- dzen_pattern: 5 (локальный сезонный) + 2 (кейс с цифрами)

## Wordstat preflight
- wordstat_get_user_info: OK (Yandex Cloud API, 2026-09-18)

## Wordstat live probes (MCP-KV)

### P0 spine
- «квартиры посуточно тюмень» RU 225: 9696 | Tyumen 55+11176: 4495
- «снять квартиру посуточно в тюмени» RU: 3331 | Tyumen: 1341

### Hook probes
- «батареи холодные квартира» RU 225: 674 (guest comfort / heating pain)
- «в квартирах холодно батареи» RU 225: 638
- «холодные батареи в квартире что делать» RU 225: 70
- «отопление квартира посуточно» RU 225: totalCount 12 (weak narrow — ride spine P0)
- «залог посуточно» RU 225: 2689 (supporting cluster, NOT angle — deposit saturated)

### Rework log
1. probe «батареи холодные квартира» 674 (225) → guest heating comfort intent
2. probe «отопление квартира посуточно» 12 total → weak narrow, localize Tyumen
3. rework «аренда квартиры посуточно» → spine
4. final P0 «квартиры посуточно тюмень» 4495 (55+11176) / 9696 (225)

### Final P0
- phrase: «квартиры посуточно тюмень»
- volume: 9696 (RU 225), 4495 (55+11176)
- guest intent: book apartment in Tyumen — verify heating/radiators before pay in early autumn

## Title draft (two-beat, NOT final Title role)
«Написали «отопление есть». В комнате +14 °C — батареи холодные»

## topic_id
B27

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
