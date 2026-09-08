# Scout handoff B15 — собака / доплата за породу

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-09-08)
klyshin_hook: dog_breed_fee | original: «Можно с собакой» — у двери доплата за породу или залог ×2
wordstat_rework: probe «квартира посуточно с собакой» 8 (55+11176) → «посуточная квартира с собакой» 571 (225) → «снять квартиру посуточно с собакой» 429 (225) → «аренда квартиры посуточно» 704 (55+11176) → final P0 «квартиры посуточно тюмень» 5134 (55+11176) / 10865 (225)
wordstat: mcp_kv live | regions 55+11176 | P0 «квартиры посуточно тюмень» 5134 | compare 225 «квартиры посуточно тюмень» 10865 | P1 «посуточная квартира с собакой» 571 (225) | P1 «снять квартиру посуточно с собакой» 429 (225)
season_note: YEKT 2026-09-08 — early September summer; no winter hero on cover
topic_id: B15
slug: mozhno-s-sobakoj-u-dveri-doplatili-za-porodu
title_draft: «Можно с собакой» написали. У двери доплатили 3 000 за «крупную породу»
angle: guest travels with dog; chat says pet OK; at door host demands breed surcharge or doubled deposit «за шерсть»; moral: pet rules in writing before key; lockpick: «Какая доплата за питомца и когда?»
anti_dup: NOT B04 third guest; NOT live WP goryachaya-voda/boiler, zaselilsya Wi‑Fi, otmenil-bron, zalog-posle-uborki; NOT B01/B13 codes/keybox; NOT B14 neighbors music
dzen_pattern: 2 (case_with_sums)
