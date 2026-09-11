# Scout handoff B03

## Topic

- topic_id: B16
- priority: P0
- format: CASE 1100–1800 слов, не гайд
- tenant: Добрый дом, посуточная Тюмень, голос тёплого хоста, не риэлтор, не Клышин сделки/Москва

## Title draft

- short_title: Собака и доплата у двери
- title_draft: «Написали «можно с собакой». У двери — доплата 3 000 за метиса»
- slug: `napisali-mozhno-s-sobakoj-u-dveri-doplatili-3-000`

## Dzen shape

- dzen_pattern: 2
- dzen_shape_hint: «Написали «можно с собакой». У двери попросили 3 000 за метиса»

## Klyshin hook

- klyshin_hook: dog_breed_fee | original: «Написали «можно с собакой». У двери — доплата за породу.» | angle: питомец в объявлении/чате «можно», на пороге — «метис крупный, +3 000» или «только до 10 кг»; сумма и правила до оплаты | signal: https://t.me/klyshin_A
- klyshin_signal: reader inside with dog on leash at door; moral: сначала правила и доплата в переписке, потом ключ
- lockpick: «Какая максимальная вес/порода и доплата за питомца в рублях — в объявлении или пришлёте письменно до оплаты?»
- refusal_beat: «Нет. Так не заселяем.» / «Не на словах. Не у двери. А в чате до перевода.»

## Case spine

1. Семья/пара с метисом примерно 18 кг приезжает на 2 ночи в Тюмени в сентябре; в объявлении указано «можно с животными».
2. В чате гость пишет: «Собака небольшая, приучена». Хозяин отвечает: «Да, можно».
3. После оплаты 2 ночей × 4 200 ₽ = 8 400 ₽ у двери сообщают: «У нас до 10 кг. Ваша — доплата 3 000 или отказ».
4. На вопрос «Почему не написали до перевода?» ответ: «Так у всех, вы сами не спросили».
5. Burn: 8 400 + 3 000 = 11 400 ₽ или отказ в 23:00 с собакой на улице.
6. Lockpick: вес/порода/доплата в рублях письменно до оплаты + фото правил в объявлении.
7. Moral: сначала правила питомца в переписке, потом деньги и ключ.

## Wordstat

- wordstat_preflight: mcp-kv wordstat_get_user_info OK
- wordstat_rework: probe «квартира посуточно с собакой» 7 (55+11176) → «снять квартиру посуточно с собакой» 7 local / 427 (225) → «снять квартиру с собакой» 1998 (225, long-term bias) → guest P0 spine «снять квартиру посуточно с собакой» 427 (225) | Tyumen supply spine «квартиры посуточно тюмень» 5020 (55+11176) compare 10694 (225) | clusters tried: собака посуточно, залог, отели тюмень 7181 (contrast only)
- wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «снять квартиру посуточно с собакой» 427 | Tyumen spine «квартиры посуточно тюмень» 5020 | compare225 «квартиры посуточно тюмень» 10694 | «снять квартиру с собакой» 1998 | local «квартира посуточно с собакой» 7 | «доплата за собаку посуточно» API empty | «залог посуточно» 35 | «отели тюмень» 7181
- wordstat_note: hook cluster weak locally (7) but honest buyer-intent nationally (427); localize supply Тюмень; article = one case with dog at door + written rules before pay

## Angle rotation

- angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B13 в last-3; dog_breed_fee — новый угол питомец/доплата у двери
- last_angles: B13 burn-at-door / ключница пустая; B14 соседи / шум ночью; B15 командировка / Wi‑Fi / созвон
- skip_families: burn-at-door (B01,B13), neighbors (B14), wifi/commandovka (B15), код/ключница, залог-скол (B02), kitchen (B07), parking (B09), hidden fees all-inclusive (B10)

## External signal

- external_signal: https://t.me/klyshin_A — rhythm «сначала проверка, потом деньги» (механика отказа, не копировать сделки)
- signal_urls: https://t.me/klyshin_A | https://добрыйдом-72.рф/blog/ | https://t.me/Dobriy_dom_72

## Final handoff lines

- queue_slot: restore from parked_hooks `dog_breed_fee` (queue after 2026-09-10 batch)
- season_note: начало осени, сентябрь — командировки и поездки с питомцами
- interlink_siblings: B01–B15 anti-dup titles checked; specific sibling interlinks not supplied
- wp_category_slugs: не указаны в scout inputs
- NOT picked: kitchen_vs_hotel (B07 overlap), hotel_vs_daily (low vol 9), cancel_prepay (B08 overlap), boiler (saturated WP), deposit_cleaning (B02 overlap)
- НЕ использовать: ключница, код, соседи, Wi‑Fi, бойлер, залог-скол, парковка, кухня, тихий центр, предоплата тишина

wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: dog_breed_fee | original: «Написали «можно с собакой». У двери — доплата за породу.» | angle: питомец в объявлении/чате «можно», на пороге доплата за породу/вес | signal: https://t.me/klyshin_A
wordstat_rework: probe «квартира посуточно с собакой» 7 (55+11176) → «снять квартиру посуточно с собакой» 7 local / 427 (225) → guest P0 «снять квартиру посуточно с собакой» 427 | Tyumen spine «квартиры посуточно тюмень» 5020/10694
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «снять квартиру посуточно с собакой» 427 | Tyumen «квартиры посуточно тюмень» 5020 | compare225 10694
angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B13 в last-3; dog_breed_fee новый угол
dzen_pattern: 2
dzen_shape_hint: «Написали «можно с собакой». У двери попросили 3 000 за метиса»
topic_id: B16
short_title: Собака доплата у двери
title_draft: «Написали «можно с собакой». У двери — доплата 3 000 за метиса»
slug: napisali-mozhno-s-sobakoj-u-dveri-doplatili-3-000
