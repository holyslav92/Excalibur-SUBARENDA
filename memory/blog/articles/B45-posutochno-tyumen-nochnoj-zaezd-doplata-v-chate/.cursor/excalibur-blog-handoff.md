wordstat_preflight: mcp-kv wordstat_get_user_info OK (conductor 2026-10-04 YEKT)
klyshin_hook: night_checkin_surcharge | original: «В карточке заезд с 14:00. Рейс в 00:35 — в чате ночной заезд +2 500 ₽» | angle: доплата за поздний заезд после оплаты ночей, гость у подъезда/в такси
wordstat_rework: probe «поздний заезд посуточно» RU totalCount 37 partial → «ночной заезд посуточно» totalCount 13 partial → spine «бесконтактное заселение посуточно» 2508 (225) + localize «квартиры посуточно тюмень» 3889 (55+11176)
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 3889 (55+11176) | RU spine «бесконтактное заселение посуточно» 2508 (225) | supporting «снять квартиру посуточно в тюмени» 1071 (55+11176)
angle_rotation: checked last N=12 | burn-at-door skip: partial (не код/ключница) | skip: B21 early wait, B40 predoplata, B44 bank hold, LIVE musor-pravila/wifi/komissii-screen
dzen_pattern: 2
dzen_shape_hint: «Заезд с 14:00. Самолёт в 00:35 — в чате: ночной заезд 2 500 ₽»
topic_id: B45
title_draft: «Заезд с 14:00. Самолёт сел в 00:35 — в чате: ночной заезд 2 500 ₽»
primary_query: квартиры посуточно тюмень
priority: P0
slug_draft: posutochno-tyumen-nochnoj-zaed-v-chate-2500
wp_category_slugs: posutochno, zaselenie
signal_urls:
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72
- memory/scout/viral-dzen-handoff.json
