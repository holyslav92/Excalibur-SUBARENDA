# ЗАДАНИЕ DEROUTER SCOUT

Ты — Derouter utility tier (gpt-5.6-terra). Верни **полный** `.cursor/excalibur-blog-handoff.md` в ответе.
Скрипт `excalibur_blog_derouter_opus_chat.py` сам запишет файл. **Не** отвечай BLOCKER — MCP Wordstat уже проверен дирижёром, частоты ниже live.

---

# Scout inputs — 2026-09-10 09:00 YEKT (Добрый дом, B15)

## Дата и слот
- today: 2026-09-10 (Asia/Yekaterinburg)
- season: начало осени, сентябрь — командировочный сезон
- slot: p0_queue priority #2 `sept_business_trip` (window 2026-08-29 — 2026-08-31 overdue → берём сейчас)

## Published titles (anti-dup, B01–B14)
B01 код/заселение, B02 залог-скол, B03 вуз рядом, B04 третьий гость, B05 отзывы, B06 выезд/багаж, B07 кухня/кафе, B08 предоплата тишина, B09 парковка шлагбаум, B10 всё включено/такси, B11 полотенца, B12 тихий центр/стройка, B13 ключница пустая, B14 соседи/музыка ночью

WP recent (не повторять близкие H1): дети+доплата, уборка+списание, без залога у двери 5000, горячая вода/бойлер, собака+порода, WiFi+созвон, код+ключница, скрытые доплаты, предоплата+тишина, парковка, кухня, выезд+чемоданы, залог+плита, код чужой двери, рядом с вузом

## Angle rotation (last N=3)
- B12: локация / «тихий центр» vs стройка
- B13: burn-at-door / ключница пустая (код сработал)
- B14: соседи / шум ночью

**Skip families:** burn-at-door saturated (B01, B13), neighbors (B14), код/ключница, boiler/dog/children on WP, deposit-chip (B02)

## Queue decision
- **Selected:** `sept_business_trip` (queue #2, PRIORITY) — командировка: стол, розетки, Wi‑Fi на созвон, закрывающие до оплаты
- NOT picked: kitchen (B07), checkout (B06), parking (B09), hotel_vs_daily (parked, low vol), cancel_prepay (B08 overlap)

## Klyshin hook (guest pain, NOT legal)
- hook_id: `sept_business_trip`
- original: «Звонок в 10:00. Заселился в 22:00.»
- angle: командировочный гость: рабочий стол, розетки, реальный Wi‑Fi для видеосозвона, закрывающие документы — всё уточнить до оплаты, не после заселения в 22:00
- klyshin_signal (mechanics only): reader inside; moral: сначала созвон/проверка рабочего места и документов, потом ключ; number = 12 часов между звонком и заселением / 3 ночи × цена
- lockpick: «Где розетка у стола и какой реальный Wi‑Fi на видеосозвон? Закрывающие пришлёте до оплаты?»
- refusal beat: «Нет. Так не бронируем.» / «Сначала созвон и документы. Потом деньги.»
- dzen_pattern: **2** — кейс с суммами и датами (командировка, сентябрь)
- dzen_shape_hint: «Звонок в 10:00. Заселился в 22:00 — Wi‑Fi не тянет созвон» (shape, не финальный H1)

## Title draft (two-beat stop-factor, для handoff)
**«Позвонили в 10:00. В 22:00 Wi‑Fi не тянет созвон»**

- slug_hint: `pozvonili-v-10-00-v-22-00-wifi-ne-tyanet-sozvon`
- НЕ использовать: ключница, код, соседи, бойлер, собака, дети, залог-скол, парковка, кухня, тихий центр

## Wordstat (MCP-KV live, 2026-09-10)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

### Probes и rework
| probe | Tyumen 55+11176 | RU 225 |
|-------|-----------------|--------|
| командировка тюмень квартира | API empty | — |
| командировка тюмень | 45 | — |
| командировка квартира посуточно | API empty (55+11176) | 85 |
| квартиры посуточно командировка | API empty (55+11176) | 85 |
| аренда квартир посуточно тюмень | 179 | — |
| аренда квартиры посуточно | 695 | 41237 |
| посуточно или отель | 9 | — |
| справка о проживании | 160 | — |
| справка о проживании в гостинице | 18 | — |
| отели тюмень | 7182 | — |
| снять квартиру посуточно в тюмени | 1621 | — |
| квартиры посуточно тюмень | **5020** | **10694** |

wordstat_rework: probe «командировка тюмень квартира» empty → «командировка тюмень» 45 → «квартиры посуточно командировка» 85 (225 only) → «аренда квартир посуточно тюмень» 179 → «снять квартиру посуточно в тюмени» 1621 → final P0 «квартиры посуточно тюмень» 5020 (55+11176) | compare 10694 (225) | clusters tried: командировка, посуточно командировка, аренда тюмень, отели тюмень 7182 (contrast only)

**Note:** hook cluster «командировка» weak locally (45–85) but honest guest-intent for September; spine rides high-volume P0 «квартиры посуточно тюмень». Wi‑Fi angle NOT duplicated on WP as standalone article (WP had wifi+созвон as topic — our angle = desk/outlets/docs + timing 10:00 vs 22:00).

## Topic assignment
- topic_id: **B15**
- priority: P0
- article format: CASE 700–1100 слов, не гайд

## Case spine (для Writer)
1. Менеджер в командировке, 3 ночи в Тюмени в начале сентября — нужен стол, розетка, стабильный Wi‑Fi для 10:00 созвона с Москвой.
2. Утром созвон с хостом в 10:00 — «всё есть, быстрый интернет, справку пришлём».
3. Заселение в 22:00 после поезда: стол — узкий журнальный, одна розетка за диваном, Wi‑Fi 8 Мбит, созвон рвётся.
4. Хозяин: «Ну вы же не просили отдельно рабочее место».
5. Burn: 3 ночи × ~3 800 ₽ = 11 400 ₽; бухгалтерия ждёт справку о проживании — «пришлём после выезда».
6. Lockpick: видеосозвон 2 мин + скриншот speedtest + список закрывающих до оплаты.
7. Moral: сначала созвон/документы/рабочее место, потом деньги.

## Signal URLs (обязательно)
- https://t.me/klyshin_A — rhythm «сначала проверка, потом деньги» (механика отказа, не копировать сделки)
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## Tenant
Добрый дом, посуточная Тюмень, голос тёплого хоста, не риэлтор, не Клышин сделки/Москва.

## Handoff format
Полный handoff: секции Topic, Title draft, Dzen shape, Klyshin hook, Case spine, Wordstat, Angle rotation, External signal, Final handoff lines.

Обязательные строки:
```
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: sept_business_trip | original: «Звонок в 10:00. Заселился в 22:00.» | angle: ... | signal: https://t.me/klyshin_A
wordstat_rework: ...
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5020 | ...
angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B13 ключница в last-3; sept_business_trip — новый угол командировка/Wi‑Fi/доки
dzen_pattern: 2
dzen_shape_hint: «…»
```
