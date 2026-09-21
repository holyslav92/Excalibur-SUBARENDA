# ЗАДАНИЕ DEROUTER SCOUT

Ты — Derouter utility tier (gpt-5.6-terra). Верни **полный** handoff в формате B30 (memory/scout/excalibur-blog-handoff.md).
Cursor проверил Wordstat live. **Не** BLOCKER.

---

# Scout inputs — 2026-09-21 YEKT (Добрый дом, слот B31)

## Дата и слот
- today: 2026-09-21 (Asia/Yekaterinburg)
- season: конец сентября, осень — обложка без зимы как героя
- topic_id: **B31**
- director angle: **залог / обещали вернуть утром → «после уборки»** (guest CASE, NOT guide, NOT B02 скол на плите)

## Published titles (anti-dup, last entries)

Last N=3:
- B30: продление / списание 1 800 ₽ после ключей
- B29: бухгалтерия / чек / «не гостиница»
- B28: стиральная в фильтре / залог на выезде (другой угол — техника, не «утром на карту»)

Запрет дублей: код/дверь (B01,B13,B18,B22), залог-скол плита (B02), «всё включено» такси (B10), предоплата тишина (B08), уборка простыни 1800 (B23).

## Klyshin hook (guest pain, mechanics NOT legal)

- hook_id: **deposit_return_sliding_window**
- original rhythm: «Сначала проверка. Потом перевод. Не наоборот.» (канал t.me/klyshin_A — moral timing, не копировать сделки/ЕГРН)
- scene: гость сдал ключи в 11:00, залог 5 000 ₽ на карту «до обеда»; в 10:40 — «вернём после уборки и фото»
- lockpick: «Когда именно возвращают залог и что должно быть в переписке до выезда?»
- refusal: «Нет. Так не заселяем.» / «Не «утром». Не «потом». А срок в чате до заезда.»
- dzen_shape_hint: «Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»»

## Wordstat (MCP-KV live, 2026-09-21)

preflight: wordstat_get_user_info OK

| probe | region | volume | note |
|-------|--------|--------|------|
| залог посуточно | 225 | **2686** | **final P0 spine** |
| залог посуточно | 55+11176 | 26 | local compare |
| не вернули залог за квартиру посуточно | 225 | 29 | buyer pain |
| не возвращают залог за квартиру посуточно | 225 | 55 | buyer pain |
| квартиры посуточно без залога | 225 | 1130 | related |
| предоплата посуточно | 225 | 743 | skip — B08/B16 saturated |

Rework: слабый «после уборки» vanity → ride **залог посуточно** + Tyumen supply CASE (перенос срока возврата, не спор о сколе).

## Handoff fields required

topic_id: B31
slug draft: zalog-obeshchali-vernut-utrom-posle-uborki
title draft (two-beat): Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»
final_p0: залог посуточно — 2686 (225); 26 (55+11176)
original_klyshin_hook: deposit timing moral «Сначала проверка. Потом перевод.»
signal_urls: https://t.me/klyshin_A, https://добрыйдом-72.рф/blog/, https://t.me/Dobriy_dom_72
