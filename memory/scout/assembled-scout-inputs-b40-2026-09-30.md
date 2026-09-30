# Scout inputs B40 — 2026-09-30 YEKT (cron slot 09:00 UTC)

## Constraints (slot HARD)
- Один guest-night CASE «Добрый дом», не гайд. Факты только Тюмень.
- Anti-dup: не код/чужая дверь B01/B18, не залог-плита B02, не предоплата+тишина B08, не залог-фильтр B34, не минимум суток B39, не лифт B37, не собака B36, не бойлер B20.
- Последние 12: burn-at-door/filter-card mismatch семья — новый угол **предоплата до кода при фильтре «без предоплаты»**, не второй перевод Avito B33.
- Сезон: конец сентября, прохладно, вечернее заселение после поезда. Зима героем — нет.

## Wordstat (MCP-KV live 2026-09-30)
- wordstat_get_user_info: OK
- «предоплата посуточно» (225): **690** (top: посуточно предоплата 690; снять без предоплаты 329; квартиры без предоплаты 321)
- «предоплата посуточно» (55+11176): weak list (6 shows on «квартиры посуточно без предоплаты») → rework to Tyumen spine
- **final P0 spine:** «квартиры посуточно тюмень» → **3984** (55+11176) | **8838** (225)
- supporting: «снять квартиру посуточно в тюмени» → 1104 (55+11176); «залог посуточно» → 2497 (225) contrast only

## Klyshin (angle mechanics only, hook_id: no_prepay_filter_lie)
- original hook: «В фильтре — без предоплаты. В чате после оплаты: переведите 30% на карту, потом код»
- angle: обещание площадки/фильтра vs перевод физлицу **до** заселения; мораль: сначала проверка/договорённость, потом деньги — не наоборот
- signal: https://t.me/klyshin_A

## Proposed P0 case
- topic_id: B40
- title_draft (two-beat): «В фильтре — «без предоплаты». До кода попросили 3 200 ₽ на карту»
- slug_draft: posutochno-tyumen-v-filtre-bez-predoplaty-perevod-do-koda
- guest pain: скрытая предоплата, чат хозяина, код задерживается, гость у подъезда/в такси
- wp_category_slugs: posutochno, zaselenie

## signal_urls
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## published-titles (excerpt last 5)
B35 wrong entrance, B36 dog, B37 lift, B39 min 2 nights filter, B38 draft blocked (not live)
