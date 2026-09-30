# Scout inputs B39 — 2026-09-30 YEKT

## Constraints (slot)
- Guest-night CASE «Добрый дом», Tyumen supply only. Not guide, not legal Klyshin hooks.
- Anti-dup: skip boiler/B20, B38 draft, codes/keybox/wrong door (B01,B13,B18,B22,B35), dog B26/B36, lift B37, zalog-at-door B34, early check-in cleaning wait B21.
- Last-3 published: B35 wrong entrance, B36 dog filter, B37 lift — rotate away from burn-at-door, animals, lift.

## Wordstat (MCP-KV live, conductor 2026-09-30)
- wordstat_preflight: wordstat_get_user_info OK
- P0 «квартиры посуточно тюмень» → 4194 (55+11176) | 9212 (225)
- supporting «снять квартиру посуточно в тюмени» → 1201 (55+11176) | 3175 (225)
- probe «заселение в квартиру посуточно» → 2662 (225) — guest intent, not how-to essay
- probe «заселение посуточно тюмень» → weak local; spine stays P0 Tyumen cluster
- rework: avoid бесконтактное заселение (saturated); angle = **правила брони / минимум ночей на месте**

## Klyshin (angle mechanics only)
- hook_id: min_nights_at_door
- original rhythm: «В карточке — от одной ночи. У двери — только от двух»
- angle: фильтр/цена за одну ночь vs отказ заселить без доплаты за вторую; lockpick «Сколько ночей в договоре до оплаты?»
- signal: https://t.me/klyshin_A

## Proposed case
- topic_id: B39
- title_draft: «В фильтре — «от одной ночи». У домофона: «минимум двое суток»»
- slug_draft: posutochno-tyumen-v-filtre-ot-odnoj-nochi-u-domofona-minimum-dvoe-sutok
- dzen_pattern: 2 (case + ₽ за вторую ночь или отказ)
- season: конец сентября, прохлада, командировка/пара с одной ночью между рейсами
- wp_category_slugs: posutochno, zaselenie

## signal_urls
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## published-titles excerpt (avoid close H1)
B32 price stack, B34 zalog, B04 third guest, oplachena-odna-noch-minimum-dvoe-sutok (WP slug if live — new angle: filter «one night» not generic minimum)
