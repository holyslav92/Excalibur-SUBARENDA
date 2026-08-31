# Scout assembled inputs — 2026-08-31 YEKT

## CRITICAL INSTRUCTION FOR DEROUTER SCOUT
Wordstat MCP-KV preflight and ALL probes were already executed by the orchestrator via live MCP-KV.
wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06)
DO NOT refuse handoff. DO NOT claim CallMcpTool unavailable.
Your job: write the complete handoff markdown using ONLY the verified data below.

## Tenant
- Brand: Добрый дом (посуточная / субаренда, Тюмень)
- Voice: guest-night CASE, комфорт+, тёплый хост. НЕ ЕГРН, НЕ суд, НЕ «мы лучшие»
- Cover season: конец лета / начало сентября (НЕ зима героем)
- dzen_rf_pack: true

## Angle rotation (last N=3)
- B02: залог / скол на плите — deposit family
- B03: «рядом с вузом» — distance/maps
- B04: доплата за третьего у двери — hidden fee at check-in

angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B01 burn-at-door in ledger; B04 hidden fee at door; new hook dog_breed_fee (pet allowed → surprise surcharge after check-in)

## Klyshin hook
klyshin_hook: dog_breed_fee | original: «В объявлении — «можно с лапой». После заселения доплата за собаку.» | angle: гость с питомцем, доплату не озвучили до оплаты; lockpick: «Какая порода и сколько весит?» | signal: https://t.me/klyshin_A (механика отказа «Нет. Так не заселяем.» — структура, не копировать сделки)

## Wordstat rework (LIVE MCP-KV — copy verbatim)
wordstat_rework: probe «посуточная квартира с собакой» 600 (225) / 8 (55+11176) → probe «квартира с собакой снять посуточно» 462 (225) → probe «снять квартиру посуточно в тюмени» 1761 (55+11176) / 4483 (225) → probe «аренда квартиры посуточно» 792 (55+11176) / 45932 (225) → final P0 «посуточная квартира с собакой» 600 (225) spine «снять квартиру посуточно в тюмени» 1761 | clusters tried: с собакой, посуточно тюмень, аренда посуточно

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «посуточная квартира с собакой» 600 | RU compare 600 | Tyumen spine «снять квартиру посуточно в тюмени» 1761 | RU spine 4483

## topic_id
B05

## slug
razreshili-s-lapoy-doplatu-nazvali-posle-zaseleniya

## short title for research_start (Klyshin rhythm, NOT final H1)
В объявлении «можно с лапой» — после заселения доплата 3 000 ₽

## title_draft (two-beat H1 candidate)
«В объявлении — «можно с лапой». После заселения доплата 3 000 ₽»

## dzen_pattern
2 — кейс с суммами и датами
dzen_shape_hint: «Разрешили с лапой → после заселения 3 000 ₽ за «уборку»»

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/

## wp_category_hint
posutochnaya-arenda

## interlink_siblings
- /blog/beskontaktnoe-zaselenie-posutochno-tyumen/
- /blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/
- /blog/oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego/

## Required handoff format
Write markdown handoff with fields: topic_id, slug, short_title, title_draft, dzen_pattern, dzen_shape_hint, external_signal, signal_urls, wordstat_preflight, klyshin_hook, wordstat_rework, wordstat, angle_rotation, queue_slot, cover_season_note, wp_category_hint, interlink_siblings.
