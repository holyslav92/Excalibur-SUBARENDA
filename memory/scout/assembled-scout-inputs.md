# ЗАДАНИЕ DEROUTER SCOUT

Ты — Derouter utility tier (gpt-5.6-terra). Верни **полный** `.cursor/excalibur-blog-handoff.md` в ответе.
Скрипт `excalibur_blog_derouter_opus_chat.py` сам запишет файл. **Не** отвечай BLOCKER — MCP Wordstat уже проверен дирижёром, частоты ниже live.

---

# Scout inputs — 2026-09-03 YEKT (Добрый дом)

## Дата и слот
- today: 2026-09-03 (Asia/Yekaterinburg)
- season: начало сентября, осень — обложка без зимы
- slot: morning cron 06 UTC

## Published titles (anti-dup, last N=3)
- B07: «Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽»
- B06: «Выезд в полдень. Поезд через 4 часа — чемоданы у подъезда»
- B05: «Рейтинг 4,8. Два «всё супер» — и 3 900 ₽ под вопросом»

Запрет дублей: код/заселение (B01), залог-скол (B02), «рядом с вузом» (B03), доплата за третьего (B04).

## Angle rotation
- burn-at-door family: последние 3 НЕ из семейства → можно hook про деньги до ключей, но НЕ копировать B01 (чужая дверь)
- skip_last5 в банке: hot_water, neighbors, dog, passport, hidden_fees — не брать

## Klyshin hook (guest pain, NOT legal)
- hook_id: prepayment_before_keys (guest cluster, mechanics Klyshin)
- original: «Перевели предоплату. До заселения — тишина в чате.»
- angle: предоплата на карту/СБП до кода и договённостей; хозяин пропал, изменил сумму или «ещё 2 000 до ключа»
- lockpick: «Сколько и за что именно переводим до заселения?»
- refusal beat: «Нет. Так не заселяем.» / «Сначала проверка. Потом перевод. Не наоборот.»
- dzen_pattern: 2 (кейс с суммами и датами)
- dzen_shape_hint: «Перевели X ₽. К [время] — [что сломалось]»

## Wordstat (MCP-KV live, 2026-09-03)

wordstat_preflight: mcp-kv wordstat_get_user_info OK

### Probes и rework
| probe | RU 225 | Tyumen 55 |
|-------|--------|-----------|
| предоплата квартира посуточно | 804 total | 15 |
| квартиры посуточно без предоплаты | 507 | 2 |
| предоплата в посуточной квартире | 449 | — |
| вернуть предоплату за квартиру посуточно | 67 | — |
| квартира посуточно тюмень | 11916 | 3722 |
| бесконтактное заселение посуточно | 3221 | skip (B01) |
| парковка квартира посуточно | 415 | 7 tyumen with parking |

wordstat_rework: probe «предоплата квартира посуточно» 804 (225) / 15 (55) → «квартиры посуточно без предоплаты» 507 (225) → «предоплата в посуточной квартире» 449 → localize spine «квартиры посуточно тюмень» 3722 (55) / 11916 (225)

final P0: «квартиры посуточно тюмень» — buyer spine; angle «предоплата / без предоплаты / вернуть предоплату»

## Topic assignment
- topic_id: B08
- title_draft (two-beat, NOT final): «Перевели 3 000 ₽ предоплатой. К 21:00 — тишина в чате»
- slug_hint: pereveli-predoplatu-k-zaseleniyu-tishina-v-chate

## Signal URLs
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/

## Tenant
Добрый дом, посуточная Тюмень, голос тёплого хоста, не риэлтор.
