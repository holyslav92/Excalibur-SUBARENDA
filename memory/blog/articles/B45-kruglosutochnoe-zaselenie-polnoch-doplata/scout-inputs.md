# Scout inputs B45 — 2026-10-05 YEKT

**Инструкция Derouter:** Wordstat уже выполнен дирижёром через MCP-KV (см. числа ниже). Не вызывай MCP. Напиши полный handoff в markdown по чеклисту skill (topic_id, title draft, wordstat lines, dzen_pattern, signal_urls). Статус PASS.

## ViralDzen (step 0 PASS)
- guest_angle_ru: поздний заезд, код, залог, связь с хозяином
- tyumen_wound_hint: не остаться у двери при позднем заезде

## Published anti-dup (last 3)
- B44 залог заморозка на оплате
- B43 детская кроватка доплата
- B42 двушка кладовая

## Angle rotation
- burn-at-door skip: no (новый угол — обещание 24/7 vs доплата в полночь, не код/ключница)
- NOT duplicate: B08 тишина в чате, B21 ранний заезд, B40 предоплата до кода

## Klyshin hook
- hook_id: `night_24_7_vs_surcharge`
- original: «Кажется, заселение круглосуточное — пока рейс задержали и часы пробили полночь»
- angle: контраст обещания в карточке и доплаты в чате после оплаты ночей
- signal: https://t.me/klyshin_A

## Wordstat (MCP-KV live 2026-10-05)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probes RU 225:
- «квартиры посуточно» — 894821
- «заселение в квартиру посуточно» — 2555
- «бесконтактное заселение посуточно» — 2535
- «квартиры посуточно круглосуточно заселение» — 68
- «залог посуточно» — 2470
- «посуточно предоплата» — 661

Probes Tyumen 55+11176:
- «квартиры посуточно тюмень» — 3874
- «залог посуточно» — 24

wordstat_rework: probe «заезд после 22 посуточно» low → «поздний заезд» low → final P0 «квартиры посуточно тюмень» 3874 | spine RU «заселение в квартиру посуточно» 2555

## Case wound (guest night)
Сцена: в карточке «заселение 24/7» / «круглосуточно». Оплатили 2–3 ночи. Рейс задержали, в 00:10–00:40 хозяин в чате: «ночной заезд +1 500–2 000 ₽» или «после 22 доплата». Гость у подъезда с чемоданом.

## Title draft (Klyshin rhythm, NOT final)
«В карточке «заселение круглосуточно». В 00:20 в чате: «ночной заезд +1 800»»

dzen_pattern: 2
dzen_shape_hint: кейс с суммой и временем в полночь, не гайд

topic_id: B45
slug: kruglosutochnoe-zaselenie-polnoch-doplata
