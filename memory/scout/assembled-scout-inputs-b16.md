# ЗАДАНИЕ DEROUTER SCOUT

Ты — Derouter utility tier (gpt-5.6-terra). Верни **полный** `.cursor/excalibur-blog-handoff.md` в ответе.
Скрипт `excalibur_blog_derouter_opus_chat.py` сам запишет файл. **Не** отвечай BLOCKER — MCP Wordstat уже проверен дирижёром, частоты ниже live.

---

# Scout inputs — 2026-09-11 09:00 YEKT (Добрый дом, B16)

## Дата и слот
- today: 2026-09-11 (Asia/Yekaterinburg), пятница
- season: начало осени, сентябрь — командировки и поездки с питомцами
- slot: restore from parked_hooks `dog_breed_fee` (queue after 2026-09-10 batch)

## Published titles (anti-dup, B01–B15)
B01 код/заселение, B02 залог-скол плита, B03 вуз рядом, B04 третий гость, B05 отзывы, B06 выезд/багаж, B07 кухня/кафе, B08 предоплата тишина, B09 парковка шлагбаум, B10 всё включено/такси, B11 полотенца, B12 тихий центр/стройка, B13 ключница пустая, B14 соседи/музыка, B15 Wi‑Fi/созвон командировка

## Angle rotation (last N=3)
- B13: burn-at-door / ключница пустая
- B14: соседи / шум ночью
- B15: командировка / Wi‑Fi / созвон

**Skip families:** burn-at-door (B01,B13), neighbors (B14), wifi/commandovka (B15), код/ключница, залог-скол (B02), kitchen (B07), parking (B09), hidden fees all-inclusive (B10)

## Queue decision
- **Selected:** `dog_breed_fee` (parked_hooks restore 2026-09-11) — гость с собакой: «можно» в чате → доплата за породу/размер у двери
- NOT picked: kitchen_vs_hotel (B07 overlap), hotel_vs_daily (low vol 9), cancel_prepay (B08 overlap), boiler (saturated WP), deposit_cleaning (B02 overlap)

## Klyshin hook (guest pain, NOT legal)
- hook_id: `dog_breed_fee`
- original: «Написали «можно с собакой». У двери — доплата за породу.»
- angle: питомец в объявлении/чате «можно», на пороге — «метис крупный, +3 000» или «только до 10 кг»; сумма и правила до оплаты
- klyshin_signal (mechanics only): reader inside with dog on leash at door; moral: сначала правила и доплата в переписке, потом ключ
- lockpick: «Какая максимальная вес/порода и доплата за питомца в рублях — в объявлении или пришлёте письменно до оплаты?»
- refusal beat: «Нет. Так не заселяем.» / «Не на словах. Не у двери. А в чате до перевода.»
- dzen_pattern: **2** — кейс с суммами и датами
- dzen_shape_hint: «Написали «можно с собакой». У двери попросили 3 000 за метиса» (shape, не финальный H1)

## Title draft (two-beat stop-factor, для handoff)
**«Написали «можно с собакой». У двери — доплата 3 000 за метиса»**

- slug_hint: `napisali-mozhno-s-sobakoj-u-dveri-doplatili-3-000`
- НЕ использовать: ключница, код, соседи, Wi‑Fi, бойлер, залог-скол, парковка, кухня, тихий центр, предоплата тишина

## Wordstat (MCP-KV live, 2026-09-11)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

### Probes и rework
| probe | Tyumen 55+11176 | RU 225 |
|-------|-----------------|--------|
| квартира посуточно с собакой | 7 | — |
| посуточная квартира с собакой | 7 | — |
| снять квартиру посуточно с собакой | 7 | **427** |
| снять квартиру с собакой | — | **1998** |
| доплата за собаку посуточно | API empty | — |
| залог посуточно | 35 | — |
| квартиры посуточно тюмень | **5020** | **10694** |
| отели тюмень | 7181 | — |

wordstat_rework: probe «квартира посуточно с собакой» 7 (55+11176) → «снять квартиру посуточно с собакой» 7 local / 427 (225) → «снять квартиру с собакой» 1998 (225, long-term bias) → guest P0 spine «снять квартиру посуточно с собакой» 427 (225) | Tyumen supply spine «квартиры посуточно тюмень» 5020 (55+11176) compare 10694 (225) | clusters tried: собака посуточно, залог, отели тюмень 7181 (contrast only)

**Note:** hook cluster weak locally (7) but honest buyer-intent nationally (427); localize supply Тюмень; article = one case with dog at door + written rules before pay.

## Topic assignment
- topic_id: **B16**
- priority: P0
- article format: CASE 1100–1800 слов, не гайд

## Case spine (для Writer)
1. Семья/пара с метисом ~18 кг, 2 ночи в Тюмени в сентябре — в объявлении «можно с животными».
2. В чате: «Собака небольшая, приучена» — хозяин: «Да, можно».
3. У двери после оплаты 2 ночей × 4 200 ₽ = 8 400 ₽: «У нас до 10 кг. Ваша — доплата 3 000 или отказ».
4. Гость: «Почему не написали до перевода?» — «Так у всех, вы сами не спросили».
5. Burn: 8 400 + 3 000 = 11 400 ₽ или отказ в 23:00 с собакой на улице.
6. Lockpick: вес/порода/доплата в рублях письменно до оплаты + фото правил в объявлении.
7. Moral: сначала правила питомца в переписке, потом деньги и ключ.

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
klyshin_hook: dog_breed_fee | original: «Написали «можно с собакой». У двери — доплата за породу.» | angle: ... | signal: https://t.me/klyshin_A
wordstat_rework: ...
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «снять квартиру посуточно с собакой» 427 | Tyumen spine «квартиры посуточно тюмень» 5020 | ...
angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B13 в last-3; dog_breed_fee — новый угол питомец/доплата у двери
dzen_pattern: 2
dzen_shape_hint: «…»
```
