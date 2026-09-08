# Scout task — OUTPUT handoff markdown only

Wordstat preflight: OK (live MCP-KV this run).
Derouter: you ARE the utility tier — write the handoff text in your reply.

## Data (use as-is)

topic_id: B14
hook_id: neighbors_night
klyshin original: «В объявлении тихо. В 23:00 за стеной — вечеринка»
angle: гость внутри; хост обещал «тихий дом»; в 23:40 музыка за стеной; стук в дверь; moral: сначала этаж/соседи/правила, потом оплата
dzen_pattern: 2
title_draft: «Написали «тихий дом». В 23:40 соседи включили музыку на полную»
slug_hint: napisali-tihij-dom-v-23-40-sosedi-vklyuchili-muzyku-posutochno-tyumen

wordstat_preflight: mcp-kv wordstat_get_user_info OK
wordstat_rework: probe «соседи шум посуточно» 2 (55+11176) → «шум соседей» 240/17298 → «аренда квартиры посуточно» 710 → final P0 «квартиры посуточно тюмень» 5220/11084
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5220 | RU 11084
angle_rotation: last N=3 B11/B12/B13 | burn-at-door skip yes | neighbors fresh vs B12 construction

signal_urls:
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

case_angle for Research: ночь без сна в посуточной Тюмень; обещание тишины; соседи-вечеринка; хост берёт конфликт в чат; 2 ночи ~8400₽; сентябрь 2026

Write complete handoff now.
