# Scout inputs — conductor 2026-09-30 YEKT slot 12:00

## Published anti-dup (last 12)
B30–B40: door/filter surcharge family saturated (поздний выезд, чемоданы, цена на оплате, авито перевод, залог, подъезд PDF, собака, лифт, минимум суток, без предоплаты).

## Forbidden dup angles
B01 код, B02 залог скол плита, B13 ключница, B14 тихий дом музыка, B12 тихий центр стройка у окна, B35 заселение подъезд.

## Klyshin hook pick
hook_id: `neighbors_rules_night_noise`
original: «В правилах тишина после 23:00. Ночью — сборка мебели за стеной»
angle: обещание режима тишины vs реальный шум соседей; гость уже оплатил ночи, не может «переехать за час»
signal: https://t.me/klyshin_A

## Wordstat (MCP-KV live, conductor)
wordstat_preflight: wordstat_get_user_info OK
- P0 spine «квартиры посуточно тюмень» — 3984 (regions 55+11176), compare RU 8838
- supporting «снять квартиру посуточно в тюмени» — 1104
- probe «посуточно соседи шум» — totalCount 22 RU (225), Tyumen cluster thin → rework to spine P0
- probe «шум соседей аренда квартиры» — totalCount 16 RU (225)
wordstat_rework: weak local on «соседи шум» → anchor demand on P0 «квартиры посуточно тюмень» 3984; angle stays guest pain «соседи/тишина в правилах»

## Angle rotation
burn-at-door skip: yes — не код/залог/фильтр-доплата у двери
reason: свежий угол «правила тишины vs ночной шум», не дублирует B14 (музыка) и B12 (стройка за окном днём)

## Dzen
dzen_pattern: 2
dzen_shape_hint: «Тишина после 23:00 в PDF — в 1:17 дрель за стеной, 2 ночи уже оплачены»

## Draft output fields
topic_id: B41
title_draft: «В правилах — «тишина после 23:00». В 1:17 — дрель за стеной»
primary_query: квартиры посуточно тюмень
priority: P0
slug_draft: posutochno-tyumen-v-pravilah-tishina-posle-23-drill-za-stenkoj
wp_category_slugs: posutochno, pravila-prozhivaniya
signal_urls:
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72
