wordstat_preflight: mcp-kv wordstat_get_user_info OK (conductor 2026-09-30)
klyshin_hook: no_prepay_filter_lie | original: «В фильтре — без предоплаты. В чате: переведите на карту, потом код» | angle: обещание фильтра vs перевод физлицу до заселения | signal: https://t.me/klyshin_A
wordstat_rework: probe «предоплата посуточно» 690 RU / 7 Tyumen → «квартиры посуточно без предоплаты» 321 RU → final P0 «квартиры посуточно тюмень» 3984 (55+11176) | clusters tried: предоплата, без предоплаты, spine тюмень
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 3984 | RU 8838 | supporting «снять квартиру посуточно в тюмени» 1104
angle_rotation: checked last N=12 | burn-at-door skip: partial — не код/дверь, угол предоплата-фильтр | reason: B08 тишина после предоплаты; B34 залог; B39 минимум суток — новый угол «без предоплаты» в фильтре + перевод до кода
dzen_pattern: 2
dzen_shape_hint: «Фильтр без предоплаты — в чате 30% на карту до кода, гость у подъезда»
topic_id: B40
title_draft: «В фильтре — «без предоплаты». До кода попросили 3 200 ₽ на карту»
primary_query: квартиры посуточно тюмень
priority: P0
slug_draft: posutochno-tyumen-v-filtre-bez-predoplaty-perevod-do-koda
wp_category_slugs: posutochno, zaselenie
signal_urls:
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72
