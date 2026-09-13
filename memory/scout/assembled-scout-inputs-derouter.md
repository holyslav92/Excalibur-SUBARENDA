Ты — Scout (gpt-5.6-terra). Среда рабочая: Derouter REST, MCP-KV Wordstat уже вызван дирижёром.
ЗАДАЧА: вывести ТОЛЬКО готовый handoff markdown (без BLOCKER, без «не могу писать файлы»).
Ниже факты слота — оформи по контракту Scout skill.

## Published titles (last 3)
- B17: «Коммуналка включена». На выезде — счётчики и 1 840 ₽
- B18: Код уже есть. Только в подъезд не попасть — 20 минут с чемоданом
- B19: Написали «не курили». В спальне — запах и окно на замке

## Klyshin hook
hot_water_boiler | original: «Написали «горячая вода есть». В 23:10 — ледяной душ и мигающий бойлер» | angle: гость ночью, бойлер/ГВС, не отопление/батареи

## Wordstat (live MCP-KV)
wordstat_preflight: mcp-kv wordstat_get_user_info OK
wordstat_rework: probe «горячая вода посуточно» 2 (55+11176) / 74 (225) → «бойлер» 9007 (55+11176) → «аренда квартиры посуточно» 664 → final P0 «квартиры посуточно тюмень» 4826 (55+11176) | compare 10308 (225)
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4826 | supporting: бойлер 9007

angle_rotation: checked last N=3 | burn-at-door skip: yes (B18) | reason: saturated

dzen_pattern: 2
dzen_shape_hint: «Горячая вода есть» → ледяной душ ночью

topic_id: B20
title_draft: Написали «горячая вода есть». В 23:10 — ледяной душ и мигающий бойлер
slug: napisali-goryachaya-voda-est-ledyanoj-dush-migayushij-boiler
primary_query: квартиры посуточно тюмень бойлер горячая вода

Формат вывода (обязательные строки):
topic_id: B20
title: ...
slug: ...
primary_query: ...
dzen_pattern: 2
klyshin_hook: ...
wordstat_preflight: ...
wordstat_rework: ...
wordstat: ...
angle_rotation: ...
external_signal: klyshin_A mechanics + guest boiler pain
signal_urls: https://t.me/klyshin_A
