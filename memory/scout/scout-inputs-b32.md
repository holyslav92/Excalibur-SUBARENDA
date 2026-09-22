# Scout inputs — 2026-09-22 YEKT (Добрый дом, B32)

## Дата и слот
- today: 2026-09-22 (Asia/Yekaterinburg), вторник
- season: конец сентября, ранняя осень (обложка — осень, не зима)
- topic_id: **B32** (следующий после B31 в ledger)

## Published titles (anti-dup, last 3 — angle rotation N=3)
| topic_id | title |
| B29 | Оплатили 2 ночи. Бухгалтерия просит чек — «мы не гостиница» |
| B30 | Продление до двух согласовали. После сдачи ключей с карты списали 1 800 ₽ |
| B31 | Оплатили 3 ночи. Открыли дверь — внутри чужие чемоданы |

## Skip families (HARD)
- **burn-at-door / code / ключница / паспорт у двери:** skip (B01,B13,B18,B22 saturated; not in last 3 but family saturated)
- **zalog-scol / залог на выезде / скол на плите:** skip (B02, WP «без залога у двери», B28 залог+стиралка)
- **overlap / чужие вещи внутри:** skip — B31 just published
- **уборка на выезде / простыни:** skip — B23
- **коммуналка счётчики:** B17 | **receipt бухгалтерия:** B29 | **списание после ключей:** B30

## Angle rotation decision
- last N=3: бухгалтерия/чек, списание после выезда, двойное бронирование
- **ACTIVE:** цена в карточке vs итог на шаге оплаты (сервис + уборка), NOT at door, NOT zalog
- burn-at-door skip: **yes** | reason: saturated family; B32 — конфликт на экране оплаты до заселения

## Klyshin hook (guest pain, mechanics only — NOT legal/matcapital)
- hook_id: **`checkout_price_stack`**
- original: «В карточке 3 400 ₽ за ночь. Две ночи — 6 800 ₽. На оплате внезапно +12% сервиса и 1 200 ₽ уборка»
- angle: гость сравнивает квартиру с отелем по строке «за ночь»; платформа/хост добавляет сборы на последнем шаге — итог выше отеля с завтраком
- klyshin_signal: пост «Посудомойка за 1,3 млн» — механика «мелочь в карточке → большой переплат» (не копировать сделку/ипотеку/Москву)
- signal URL: https://t.me/klyshin_A (механика числа и контраста)
- lockpick: **«Итоговая сумма за все ночи с уборкой и сервисом — какая, до оплаты?»**
- refusal beat: «Нет. Так не бронируем.» → «Сначала полная сумма в переписке. Потом оплата.»
- moral: сначала полная цена (ночи + сервис + уборка), потом сравнение с отелем и оплата
- dzen_pattern: **4** (контраст квартира vs отель с ответом в лиде)
- dzen_shape_hint: «За ночь квартира казалась дешевле отеля — пока не открыли шаг оплаты с +12% и уборкой»

## Title draft (two-beat, handoff only — NOT Title role)
**«В карточке 3 400 ₽ за ночь. На оплате — 8 816 ₽ за две»**

- slug_draft: `v-kartochke-3400-za-noch-na-oplate-8816-za-dve`

## Wordstat (MCP-KV live, 2026-09-22)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

### P0 spine (final)
- «квартиры посуточно тюмень» — **4409** (regions 55+11176) | **9372** (225 compare)

### Hook + rework probes (numPhrases=1 where API 499 on large requests)
| probe | volume | region |
| «комиссия посуточно» | 1903 | 225 |
| «уборка посуточно» | 1932 | 225 (supporting; NOT article duplicate B23) |
| «бронирование квартир посуточно» | 3656 | 225 |
| «посуточно или отель» | 8 | 55+11176 |
| «отель или посуточная квартира» | 280 | 225 (from top_requests under посуточно или отель) |
| «квартира посуточно тюмень цена» | 92 | 225 |
| «квартира не соответствует фото» | 31 | 225 (weak, not picked) |
| «снять квартиру посуточно в тюмени» | 1304 | 55+11176 |
| «отели тюмень» | 7002 | 55+11176 (contrast only, NOT P0) |

wordstat_rework: probe «комиссия посуточно» 1903 (225) → «уборка посуточно» 1932 (225) → «посуточно или отель» 8 (55+11176) / «отель или посуточная квартира» 280 (225) → «квартира посуточно тюмень цена» 92 (225) → final P0 «квартиры посуточно тюмень» 4409 (55+11176) | 9372 (225) | clusters tried: комиссия, уборка, hotel contrast, цена, бронирование

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4409 (55+11176) | 9372 (225) | supporting «комиссия посуточно» 1903 (225) | contrast «отели тюмень» 7002 (55+11176)

## External signal
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/

## Derouter task
Верни полный handoff `.cursor/excalibur-blog-handoff.md` по формату B23/B24: topic_id B32, CASE 1100–1800, guest inside, Klyshin delivery 10 rules, wordstat lines verbatim, article spine 5 sections, cover_brief осень Тюмень.
