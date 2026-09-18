# Scout inputs — B27 slot 2026-09-18 YEKT

## Date
2026-09-18, Asia/Yekaterinburg, осень (не зима на обложке)

## Angle rotation (last N=3)
- B24: дети / доплата за ребёнка
- B25: кровати на фото vs диван
- B26: собака / доплата за породу
burn-at-door skip: no (не код/ключница семья)
skip families: dog, children, beds — saturated last-3

## Published anti-dup (H1/slug families to avoid)
B02 zalog-skоl на плите; B13 ключница; B18 код+домофон; B08/B16 предоплата; B10 всё включено; B26 собака; WP recent: lift, stiralnaya, zalog-5000-utrom, deshevle-otelya, vyezd-900, mokryj-pol-14-00

## Klyshin hook (NEW guest angle)
hook_id: no_deposit_door_surprise
original: «В карточке — без залога. Перед кодом просят перевод на карту.»
angle: обещание «без залога» vs перевод/удержание до выезда; NOT B02 скол на плите, NOT zalog-5000-утром return delay
klyshin_signal: moral — сначала условия залога письменно, потом ключ; lockpick: «Залог в цене или отдельно? Срок возврата?»
signal: https://t.me/klyshin_A (delivery mechanics only, not legal deals)

## Wordstat preflight
wordstat_preflight: mcp-kv wordstat_get_user_info OK

## Wordstat probes (live MCP-KV)
| probe | RU 225 | Tyumen 55+11176 |
|-------|--------|-----------------|
| залог посуточно | 2689 | 27 |
| квартира посуточно без залога | 1101 | 6 |
| не вернули залог за квартиру посуточно | 53 | 1 |
| квартиры посуточно тюмень | 9696 | 4495 |

wordstat_rework: probe «без залога посуточно» 1785 (225) → «залог посуточно» 2689 (225) / 27 (55+11176) → «квартира посуточно залог» 1718 (225) → final P0 «квартиры посуточно тюмень» 4495 (55+11176) / 9696 (225) | clusters tried: без залога, залог посуточно, вернут залог

## Dzen
dzen_pattern: 2 (кейс с суммами и датами)
dzen_shape_hint: «Написали «без залога». Перед кодом — 5 000 ₽ на карту»

## Title draft (two-beat, NOT final H1)
«Написали «без залога». Перед кодом — 5 000 ₽ на карту»

## Topic assignment
topic_id: B27
slug draft: bez-zaloga-pered-kodom-5000-na-kartu
brand: Добрый дом, посуточная Тюмень, guest-night CASE not guide
