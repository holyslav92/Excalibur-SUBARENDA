Ты — Scout (gpt-5.6-terra). Среда рабочая: Derouter REST, MCP-KV Wordstat уже вызван дирижёром.
ЗАДАЧА: вывести ТОЛЬКО готовый handoff markdown (без BLOCKER, без «не могу писать файлы»).
Ниже факты слота — оформи по контракту Scout skill.

## Date context
- today_iso: 2026-09-19
- timezone: Asia/Yekaterinburg
- weekday: суббота
- season_visual: ранняя осень, тёплый сентябрьский день; обложка — осень, НЕ зима

## Tenant
- Добрый дом, посуточная аренда Тюмень
- Guest CASE only — NO ЕГРН/суд/наследство/Москва/риэлтор/Шакин
- dzen_pattern prefer 2–5 (NOT numbered list default)

## Published titles (last N=3 for angle rotation)
- B27: «Отопление есть»: 2 ночи, +14 °C — ледяные батареи, «УК не включила»
- B26: «Можно с собакой» написали. При заезде — 2 500 ₽ за «крупную породу»
- B25: На фото две кровати. Ночью троих — диван и складной матрас

## User skip list (HARD)
- burn-at-door family: B18, B22 (код/заселение у двери)
- B02 залог-скол на плите
- B07 kitchen vs café
- B26 dog breed fee
- B27 heating/cold radiators

## WP recent anti-dup (titles only — do NOT repeat angle)
- Залог 5 000 ₽ обещали утром. После уборки — без срока
- Выезд в полдень. За четверть часа — 900 ₽ за «лишний час»
- На фото — стиралка. На третий день — прачечная за 600 ₽
- Квартира дешевле отеля за ночь. За две ночи — 13 400 ₽
- Написали «лифт есть». За 8 400 ₽ — пятый этаж пешком
- Заезд с двух. 105 мин с чемоданом: мокрый пол, «ещё пять»

## Angle rotation
- last N=3: B25 sleeping places, B26 dog fee, B27 heating — skip those families
- burn-at-door skip: yes (B18,B22 saturated per mandate; NOT last-3 but explicit skip)
- NOT B15 duplicate: B15 = Wi‑Fi/рабочий стол/созвон; B28 = справка/чек для бухгалтерии на командировке

## Klyshin hook (guest pain, mechanics only)
- hook_id: business_trip_receipt
- original: «Командировка в Тюмень. Бухгалтерия просит справку — в чате: «мы не гостиница»»
- angle: закрывающие документы до брони; квартира посуточно vs отель — справка о проживании и чек; NOT Wi‑Fi desk (B15), NOT hotel price compare (WP)
- lockpick_question: «Справку о проживании и чек для отчёта дадите до оплаты — в каком виде?»
- refusal beat: «Нет. Так не бронируем.» / «Сначала документы для бухгалтерии. Потом оплата.»
- moral: сначала справка/договор/чек для командировочных, потом деньги и ключ
- klyshin_signal: ритм Клышина — кейс с денежной точкой, цитата → слом; signal https://t.me/klyshin_A (mechanics only, не юр-темы канала)
- dzen_pattern: **3** (страх → инструкция в §1)
- title_draft (two-beat, NOT final Title): «Нужна справка для бухгалтерии. В чате: «мы не гостиница»»

## Wordstat preflight
- wordstat_get_user_info: OK (user confirmed)

## Wordstat live probes (MCP-KV, дирижёр)

### Final P0 spine
- «квартиры посуточно тюмень» 55+11176: **4495** | RU 225: **9696**

### Hook / rework probes
| phrase | 55+11176 | 225 |
|--------|----------|-----|
| справка о проживании в посуточной квартире | — | 11 |
| справка о проживании в квартире для командировочных | — | 16 |
| справка о проживании в гостинице для командировочных | — | 289 |
| справка о проживании в гостинице | — | 908 |
| командировка тюмень | — | 114 |
| договор посуточной аренды квартиры | 37 | — |
| отели тюмень | 7139 | — |
| снять квартиру посуточно в тюмени | 1341 | — |

### Rework log (for handoff)
probe «справка о проживании в посуточной квартире» 11 (225) → «справка о проживании в квартире для командировочных» 16 (225) → «справка о проживании в гостинице для командировочных» 289 (225) → «командировка тюмень» 114 (225) → «договор посуточной аренды квартиры» 37 (55+11176) → final P0 «квартиры посуточно тюмень» 4495 (55+11176) | compare 9696 (225)

## topic_id
B28

## signal_urls
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## OUTPUT RULES (HARD)
- Return ONLY the handoff markdown body
- Include all required lines: topic_id, title_draft, slug_hint, primary_query, klyshin_hook, wordstat_preflight, wordstat_rework, wordstat, angle_rotation, dzen_pattern, dzen_shape_hint, signal_urls, external_signal, opening_direction, moral, lockpick_question, anti_dup_guard
