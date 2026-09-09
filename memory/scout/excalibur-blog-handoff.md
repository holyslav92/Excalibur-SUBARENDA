# Scout handoff — B15 (Добрый дом)

topic_id: B15
title_draft: «Горячая вода есть». В душе — ледяная струя, ждать полчаса
slug_hint: napisali-goryachaya-voda-est-v-dushe-ledyanaya-struya
dzen_pattern: 2
dzen_shape_hint: сентябрь, семья/командировка; обещание ГВС vs бойлер «включите сами»

klyshin_hook: hot_water_boiler | original: «Горячая вода есть» — в душе ледяная, хозяин: «подождите, бойлер» | angle: до оплаты спросить про бойлер/ГВС | signal: https://t.me/klyshin_A

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-09-09)

wordstat_rework: probe «бойлер посуточно» 11 (225) empty Tyumen → «горячая вода посуточно» 76 (225) / 2 (55+11176) → «в квартире нет горячей воды» 2589 (225) guest pain context → final P0 «квартиры посуточно тюмень» 5134 (55+11176)

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5134 | compare 10865 (225)

angle_rotation: checked last N=3 (B12 тихий центр, B13 код/ключница, B14 соседи) | burn-at-door skip: yes | reason: saturated code/keybox family

signal_urls: https://t.me/klyshin_A , https://добрыйдом-72.рф/blog/ , https://t.me/Dobriy_dom_72
