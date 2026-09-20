wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: prepay_filter_trap | original: «В фильтре стояло «без предоплаты». За сутки до заезда — 50% на карту или отмена» | angle: фильтр «без предоплаты» vs требование СБП за день до заезда | signal: https://t.me/klyshin_A
wordstat_rework: probe «предоплата посуточно» RU 743 → «квартиры посуточно без предоплаты» RU 359 → «залог посуточно» RU 2686 (adjacent, skip dup) → final P0 «квартиры посуточно тюмень» 4413 (55+11176)
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4413 | supporting «квартиры посуточно без предоплаты» 359 (225)
angle_rotation: checked last N=3 B28/B29/B30 | burn-at-door skip: yes | reason: доплата/фильтр, не код у двери
dzen_pattern: 2
dzen_shape_hint: «Без предоплаты в фильтре — за день до заезда 4 200 ₽ на карту и угроза снять бронь»
topic_id: B31
title_draft: «В фильтре стояло «без предоплаты». За день до заезда попросили 4 200 ₽ на карту»
primary_query: квартиры посуточно тюмень
priority: P0
slug_hint: filtre-bez-predoplati-za-den-do-zaezda-4200-na-kartu
