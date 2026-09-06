# ЗАДАНИЕ DEROUTER SCOUT

Ты — Derouter utility tier (gpt-5.6-terra). Верни **полный** `.cursor/excalibur-blog-handoff.md` в ответе.
Скрипт `excalibur_blog_derouter_opus_chat.py` сам запишет файл. **Не** отвечай BLOCKER — MCP Wordstat уже проверен дирижёром, частоты ниже live.

---

# Scout inputs — 2026-09-06 YEKT (Добрый дом, B12)

## Дата и слот
- today: 2026-09-06 (Asia/Yekaterinburg)
- season: конец лета / начало осени — обложка без зимы
- slot: B12, p0_queue window 2026-09-08–10 batch (queue #7 quiet_center_maps)

## Published titles (anti-dup, B01–B11)
B01 код/заселение, B02 залог-скол, B03 вуз рядом, B04 третьий гость, B05 отзывы, B06 выезд/багаж, B07 кухня/кафе, B08 предоплата тишина, B09 парковка шлагбаум, B10 всё включено/такси, B11 полотенца/«всё для гостей»

WP recent (не повторять близкие H1): отмена брони 2500, залог после уборки, голый матрас, бойлер, собака, wifi, ключница, **тихий двор стройка**

## Angle rotation (last N=3)
- B09: парковка / шлагбаум
- B10: скрытая доплата / «всё включено»
- B11: удобства ванной / полотенца

**Skip families:** parking, hidden fees, bathroom amenities, burn-at-door (B01), pack_vs_flat towels (B11 done)

## Queue decision
- pack_vs_flat — saturated (B11), skip
- checkout_train — done B06
- kitchen_vs_hotel — done B07
- **Selected:** `quiet_center_maps` (queue #7) — Maps/panorama angle, NOT «тихий двор» duplicate

## Klyshin hook (guest pain, NOT legal)
- hook_id: `quiet_center_maps`
- original: ««Тихий центр» — за окном стройка»
- angle: 7 минут в Яндекс Картах/панорамах — не слова хоста; гость бронирует «тихий центр», просыпается от крана/стройки
- klyshin_signal (mechanics only): reader inside; number = 6:30 wake-up / 3 ночи без сна; moral: сначала панорама и слой стройки, потом оплата
- lockpick: «Что видно в панораме с балкона, если включить слой стройки?»
- refusal beat: «Нет. Так не бронируем.» / «Сначала карта и панорама. Потом деньги.»
- dzen_pattern: **5** — локальный + сезонный (центр Тюмени, начало сентября, бронь на выходные)
- dzen_shape_hint: «Обещали тихий центр. В 6:30 за окном — кран» (shape, не финальный H1)

## Title draft (two-beat stop-factor, для handoff)
**«Написали «тихий центр». В 6:30 за окном — кран»**

- slug_hint: `napisali-tihij-centr-v-6-30-za-oknom-kran`
- НЕ использовать: «тихий двор», двор+стройка (WP duplicate), парковка, залог, полотенца, кухня, такси

## Wordstat (MCP-KV live, 2026-09-06)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

### Probes и rework
| probe | Tyumen 55+11176 | RU 225 |
|-------|-----------------|--------|
| тихий центр квартира посуточно | empty | — |
| аренда квартиры тюмень центр | 16 | — |
| квартира посуточно тюмень центр | 68 | 268 |
| снять квартиру посуточно в центре тюмени | 54 | 223 |
| тихий район квартира | 9 | — |
| соседи шум | 220 | — |
| отмена брони | 64 | — |
| квартиры посуточно тюмень | **5235** | **11220** |

wordstat_rework: probe «тихий центр квартира посуточно» empty → «аренда квартиры тюмень центр» 16 → «квартира посуточно тюмень центр» 68 → «снять квартиру посуточно в центре тюмени» 54 → final P0 «квартиры посуточно тюмень» 5235 (55+11176) | compare 11220 (225) | clusters tried: тихий центр, центр тюмень, посуточно центр

**Note:** соседи/шум 220 и отмена брони 64 — ниже queue priority и neighbors в skip_last5; cancel близко к WP «отмена брони 2500»

## Topic assignment
- topic_id: **B12**
- priority: P0
- article format: CASE 700–1100 слов, не гайд

## Case spine (для Writer)
1. Пара бронирует «тихий центр» на 3 ночи в начале сентября — командировка + прогулки.
2. В объявлении: «тихий центр, рядом набережная».
3. Заселились вечером — тихо. Утром в 6:30 — гул крана, стройка в соседнем квартале (видно на панораме, если бы смотрели).
4. Хозяин: «Ну это же центр, что вы хотели».
5. Burn: 3 ночи × ~4 200 ₽ = 12 600 ₽; сон сорван; отель last-minute +2 800 ₽ не вариант.
6. Lockpick: панорама + слой стройки до оплаты.
7. Moral: сначала карта/панорама, потом деньги.

## Signal URLs (обязательно)
- https://t.me/klyshin_A — rhythm «сначала проверка объекта, потом деньги» (post про гостиницу/KRT: проверить до покупки)
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## Tenant
Добрый дом, посуточная Тюмень, голос тёплого хоста, не риэлтор, не Клышин сделки/Москва.

## Handoff format
Полный handoff как B11 в memory/scout/.cursor/excalibur-blog-handoff.md: секции Topic, Title draft, Dzen shape, Klyshin hook, Case spine, Wordstat, Angle rotation, External signal, Final handoff lines.

Обязательные строки:
```
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: quiet_center_maps | original: ««Тихий центр» — за окном стройка» | angle: ... | signal: https://t.me/klyshin_A
wordstat_rework: ...
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5235 | ...
angle_rotation: checked last N=3 | burn-at-door skip: no | reason: ...
```
