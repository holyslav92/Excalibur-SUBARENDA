# ЗАДАНИЕ DEROUTER SCOUT

Ты — Derouter utility tier (gpt-5.6-terra). Верни **полный** `.cursor/excalibur-blog-handoff.md` в ответе.
Скрипт `excalibur_blog_derouter_opus_chat.py` сам запишет файл. **Не** отвечай BLOCKER — MCP Wordstat уже проверен дирижёром, частоты ниже live.

---

# Scout inputs — 2026-09-03 YEKT (Добрый дом)

## Дата и слот
- today: 2026-09-03 (Asia/Yekaterinburg)
- season: начало сентября, осень — обложка без зимы (не зима героем)
- slot: morning cron 09 UTC

## Published titles (anti-dup, last N=3)
- B08: «Перевели 3 000 ₽ предоплатой. К вечеру — тишина в чате»
- B07: «Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽»
- B06: «Выезд в полдень. Поезд через 4 часа — чемоданы у подъезда»

Запрет дублей: код/чужая дверь (B01), залог-скол (B02), «рядом с вузом» (B03), доплата за третьего (B04), отзывы (B05), предоплата-тишина (B08), кухня-кафе (B07), выезд-чемоданы (B06). Не копировать WP-посты про парковку-800, полотенце на четверых, собаку+доплату.

## Angle rotation
- burn-at-door family: последние 3 НЕ про «код не тот» → ключница/бесконтакт OK если угол **поломка ключницы**, не чужая дверь
- skip_last5 в банке: hot_water, neighbors, dog, passport, hidden_fees — **не** брать; выбран **ключница** (guest pain из brief)

## Klyshin hook (guest pain, NOT legal)
- hook_id: keybox_frozen_panel (parking_keybox family, mechanics Klyshin)
- original: «Код прислали. Ключница у подъезда не открылась.»
- angle: бесконтактное заселение через ключницу; код/ссылка есть, но панель не реагирует (мороз, севшая батарея, «нажмите сильнее»); гость с чемоданом у двери, такси уехало
- lockpick: «Где именно ключница и есть ли запасной способ входа?»
- refusal beat: «Нет. Так не заселяем.» / «Сначала проверка. Потом перевод. Не наоборот.» (про деньги — только если в кейсе; фокус на доступ)
- dzen_pattern: 2 (кейс с суммами и датами) + элемент 3 (страх у двери)
- dzen_shape_hint: «Код прислали. Ключница не открылась. Такси уже уехало»

## Wordstat (MCP-KV live, 2026-09-03)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

### Probes и rework
| probe | RU 225 | Tyumen 55+11176 |
|-------|--------|-----------------|
| ключница посуточно | 17 total | — |
| бесконтактное заселение посуточно | skip angle B01 | — |
| квартиры посуточно тюмень | 11765 | 5320 (из «квартира посуточно» top) |
| квартира посуточно (spine) | — | 16915 total cluster |
| парковка квартира посуточно | 420 | 7 «тюмень с парковкой» — skip (WP dup) |
| собака квартира посуточно | 617 | skip (bank + WP dup) |

wordstat_rework: probe «ключница посуточно» 17 (225) → «бесконтактное заселение» saturated B01 → localize buyer spine «квартиры посуточно тюмень» 5320 (55+11176) / 11765 (225); angle = ключница/код не открывает **свою** дверь

final P0: «квартиры посуточно тюмень» — buyer spine; guest angle «ключница / код не открыл замок»

## Topic assignment
- topic_id: B09
- title_draft (two-beat, NOT final): «Код прислали. Ключница не открылась. Такси уже уехало»
- slug_hint: kod-prislali-klyuchnitsa-ne-otkrylas-taksi-uehalo

## Signal URLs
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/

## Tenant
Добрый дом, посуточная Тюмень, голос тёплого хоста, не риэлтор.
