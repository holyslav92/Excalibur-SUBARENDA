# Scout assembled inputs — B45 — 2026-10-04 YEKT

## Tenant
Добрый дом, посуточная Тюмень, dzen_rf_pack, case Дзен (не гайд).

## Anti-dup (published B01–B44)
BAN families today: код/заселение (B01,B13,B18,B22,B35), залог скол (B02), залог банк заморозка (B44), предоплата (B08,B40), собака (B26,B36), бойлер (B20,B38), соседи/тишина (B14), рядом с вузом (B03).
Last N=3: B44 залог+банк, B43 кроватка, B42 двушка/кладовая.
Last N=12: avoid door-surcharge clone; not legal ЕГРН.

## Chosen angle
hook_id: `hot_booking_skip_house_rules`
Guest pain: скрытая доплата / правила проживания — штраф на выезде (мусор, посуда), гость не открыл памятку, боялся потерять бронь на даты.
NOT B23 (простыни/уборка на выезде), NOT залог/код/предоплата.

## Klyshin (angle only, NOT legal copy)
signal: https://t.me/klyshin_A/3186
original hook (ритм Клышина, покупатель на горячем рынке): «Если я сейчас начну задавать вопросы, квартиру заберёт следующий» — перенос на гостя посуточно: не читал правила до оплаты, после списания нашёл пункты про штрафы.
angle: moral сначала правила/штрафы в переписке, потом ночь; lockpick: «Где памятка и что считается «грязной посудой»?»

## Wordstat live MCP-KV (2026-10-04)
preflight: wordstat_get_user_info OK

probes:
- «правила проживания посуточно» → 387 (225); 3 (55) — weak Tyumen, guest intent OK
- «правила проживания в квартире посуточно» → 283 (225)
- «уборка посуточно» → 1932 (225) host/job bias
- «отмена брони посуточно» → 53 (225) — skip as spine
- rework → final P0 «квартиры посуточно тюмень» → 3889 (55+11176) | 8881 (225)
- supporting «снять квартиру посуточно в тюмени» → 1071 (55+11176) | 2990 (225)

## H1 shape (двухтакт, стоп-фактор ночи, не how-to)
«Оплатили две ночи. На выезде — штраф по правилам, которые не открывали»

## dzen
pattern: 2 (кейс с суммами)
shape_hint: боязнь сорвать бронь → оплата → пункт про мусор/посуду и сумма на выезде

## topic_id B45
slug hint: posutochno-tyumen-pravila-prozhivaniya-shtraf-musor-vyezd
wp_category_slugs: posutochno, zaselenie
short title for research_start: «Оплатили две ночи. На выезде прислали штраф за мусор — правила не читали»

## signal_urls required
- https://t.me/klyshin_A/3186
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

Write handoff markdown per scout skill with mandatory lines: wordstat_preflight, klyshin_hook, wordstat_rework, wordstat, angle_rotation, dzen_pattern, topic_id, title_draft, signal_urls.
