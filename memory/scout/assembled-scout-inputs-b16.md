# ЗАДАНИЕ DEROUTER SCOUT

Ты — Derouter utility tier (gpt-5.6-terra). Верни **полный** `.cursor/excalibur-blog-handoff.md` в ответе.
Скрипт `excalibur_blog_derouter_opus_chat.py` сам запишет файл. **Не** отвечай BLOCKER — MCP Wordstat уже проверен дирижёром, частоты ниже live.

---

# Scout inputs — 2026-09-10 17:00 YEKT (Добрый дом, B16)

## Дата и слот
- today: 2026-09-10 (Asia/Yekaterinburg)
- season: начало осени, сентябрь — без зимы на обложке
- slot: p0_queue `kitchen_vs_hotel_cafes` saturated (B07) → **parked hook `hotel_vs_daily`** restored

## Published titles (anti-dup, B01–B15)
B01 код/заселение, B02 залог-скол, B03 вуз рядом, B04 третий гость, B05 отзывы, B06 выезд/багаж, B07 кухня/кафе, B08 предоплата тишина, B09 парковка шлагбаум, B10 всё включено/такси, B11 полотенца, B12 тихий центр/стройка, B13 ключница пустая, B14 соседи/музыка, B15 рабочий стол/Wi‑Fi/созвон

WP recent (не повторять близкие H1): дети+доплата, уборка+списание, без залога 5000, горячая вода/бойлер, собака+порода, WiFi+созвон, отмена брони 2500, ранний заезд+поезд, код+отчёт, скрытые доплаты

## Angle rotation (last N=3)
- B13: burn-at-door / ключница
- B14: соседи / шум ночью
- B15: командировка / Wi‑Fi / рабочее место

**Skip families:** burn-at-door, neighbors, wifi/desk/command trip, kitchen/cafe (B07), prepay silence (B08), cancel (WP), boiler/dog/children (WP)

## Queue decision
- **Selected:** `hotel_vs_daily` (parked → restore) — гость выбирал «квартира vs отель», сэкономил на цене, проиграл на сне/сервисе
- NOT picked: cancel_prepay (B08+WP), hot_water_boiler (WP), deposit_cleaning (WP), kitchen_vs_hotel (B07)

## Klyshin hook (guest pain, NOT legal)
- hook_id: `hotel_vs_daily`
- original: «Квартира дешевле отеля на 900 ₽. Первая ночь — как в хостеле»
- angle: сравнение на брони: «квартира посуточно или отель»; гость экономит 800–900 ₽/ночь, получает тонкие стены, общий коридор, нет ресепшена в 2:00
- klyshin_signal (mechanics only): reader inside; moral: сначала сравнить не цену, а сон и правила; number = 3 ночи × разница vs отель +1 800 ₽ vs бессонница
- lockpick: «Что в отзывах про шум и выезд — и что в отеле за +900 ₽?»
- refusal beat: «Нет. Так не выбираем.» / «Сначала сон и правила. Потом экономия.»
- dzen_pattern: **4** — контраст с ответом в лиде
- dzen_shape_hint: «Отель был на 900 ₽ дороже. Квартира — шум из коридора до трёх» (shape, не финальный H1)

## Title draft (two-beat stop-factor, для handoff)
**«Отель был на 900 ₽ дороже. Квартира — шум из коридора до трёх»**

- slug_hint: `otel-byl-dorozhe-900-kvartira-shum-koridor-do-treh`
- НЕ использовать: Wi‑Fi, ключница, код, соседи музыка (B14), кухня, парковка, залог, предоплата, бойлер, собака, дети

## Wordstat (MCP-KV live, 2026-09-10)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

### Probes и rework
| probe | Tyumen 55+11176 | RU 225 |
|-------|-----------------|--------|
| посуточно или отель | weak locally | 387 |
| квартира посуточно или отель | — | 282 |
| что лучше отель или квартира посуточно | — | 15 |
| отели тюмень | 7182+23102 context | — |
| квартиры посуточно тюмень | **10694** | **10694** |
| аренда квартиры посуточно | — | 41237 |

wordstat_rework: probe «посуточно или отель» 387 (225) → «квартира посуточно или отель» 282 → «отели тюмень» 23102 (contrast only, not P0) → final P0 «квартиры посуточно тюмень» 10694 (55+11176) | compare 10694 (225) | clusters tried: hotel vs flat choice, отели тюмень contrast

## Topic assignment
- topic_id: **B16**
- priority: P0
- article format: CASE 1100–1800 слов, не гайд

## Case spine (для Writer)
1. Пара в командировке+отдых, 3 ночи в Тюмени, начало сентября — выбирают между отелем у ТРЦ и квартирой на сутки.
2. Квартира на 900 ₽/ночь дешевле; хозяин: «тихо, как дома, всё своё».
3. Первая ночь: общий коридор, хлопанье дверей, разговор у лифта до 3:00 — стены тонкие, ресепшена нет.
4. Хозяин: «Ну это же многоквартирный дом, что вы хотели».
5. Burn: 3 ночи × ~3 100 ₽ = 9 300 ₽ сэкономили 2 700 ₽ vs отель, но две ночи без сна; отель last-minute +4 500 ₽.
6. Lockpick: отзывы про шум + правила дома + сравнение «+900 ₽ за сон» до оплаты.
7. Moral: сначала сон и правила, потом экономия на строке «дешевле отеля».

## Signal URLs (обязательно)
- https://t.me/klyshin_A — rhythm «сначала проверка, потом деньги» (механика, не сделки)
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## Tenant
Добрый дом, посуточная Тюмень, голос тёплого хоста, не риэлтор, не Клышин сделки/Москва.

## Handoff format
Полный handoff: секции Topic, Title draft, Dzen shape, Klyshin hook, Case spine, Wordstat, Angle rotation, External signal, Final handoff lines.

Обязательные строки:
```
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: hotel_vs_daily | original: «Квартира дешевле отеля…» | angle: ... | signal: https://t.me/klyshin_A
wordstat_rework: ...
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 10694 | ...
angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B13; hotel_vs_daily fresh vs B07 kitchen and B15 wifi
dzen_pattern: 4
dzen_shape_hint: «…»
```
