# Scout assembled inputs — 2026-08-30 YEKT

## CRITICAL INSTRUCTION FOR DEROUTER SCOUT
Wordstat MCP-KV preflight and ALL probes were already executed by the orchestrator via live MCP-KV.
wordstat_preflight: mcp-kv wordstat_get_user_info OK
DO NOT refuse handoff. DO NOT claim CallMcpTool unavailable.
Your job: write the complete handoff markdown using ONLY the verified data below.

## Tenant
- Brand: Добрый дом (посуточная / субаренда, Тюмень)
- Voice: клышинская подача, комфорт+, от лица компании. НЕ ЕГРН, НЕ суд, НЕ «мы лучшие»
- Cover season: конец августа / лето (НЕ зима героем)
- dzen_rf_pack: true

## Queue slot
queue_slot: 2026-08-29 — 2026-08-31 | queue_num 2 | hook_id sept_business_trip

## Angle rotation (last N=3 + recent WP)
- B01: burn-at-door / код — SKIP family
- B02: залог / скол на плите — SKIP
- B03: вуз / «рядом» / родители сентябрь
- WP 2026-08-30: закрывающие после выезда (22:00 + 10:00 созвон) — SKIP angle
- WP 2026-08-29: розетки у стола — SKIP angle
- WP 2026-08-25: где работать — SKIP angle

angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B01; sept_business_trip rework to Wi-Fi on video call — fresh angle within queue

## Klyshin hook
klyshin_hook: sept_business_trip | original: «Звонок в 10:00. Заселился в 22:00.» | angle: Wi-Fi падает на видеосозвоне; в объявлении «быстрый интернет»; moral: сначала тест скорости/роутер, потом оплата | signal: https://t.me/klyshin_A

## Wordstat rework (LIVE MCP-KV — copy verbatim)
wordstat_rework: probe «командировка тюмень квартира» 1 (225) / пусто (55+11176) → probe «командировка квартира посуточно» 61 (225) → probe «аренда квартиры посуточно» 792 (55+11176) / 45932 (225) → probe «квартира посуточно тюмень» 5500 (55+11176) / 12325 (225) → final P0 «квартиры посуточно тюмень» 5500 (55+11176) / 12325 (225) | clusters tried: командировка, посуточно, квартиры посуточно тюмень

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5500 | RU compare 12325 | secondary «аренда квартиры посуточно» 792 / 45932

## topic_id
B04

## short title for research_start (Klyshin rhythm, NOT final H1)
Звонок в 10:00 — Wi-Fi умер на третьей минуте

## title_draft
Звонок в 10:00. На третьей минуте Wi‑Fi умер — в объявлении «быстрый интернет»

## dzen_pattern
3 — страх → инструкция в §1 (созвон сорвался → что проверить до оплаты)
dzen_shape_hint: «Созвон в 10:00: Wi‑Fi умер — что спросить у хоста до перевода»

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/

## cover_season_note
YEKT 2026-08-30 — конец августа, летний свет; no winter/snow/ice hero

## wp_category_hint
posutochnaya-arenda

## interlink_siblings
- https://добрыйдом-72.рф/blog/beskontaktnoe-zaselenie-posutochno-tyumen/
- https://добрыйдом-72.рф/blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/

## Required handoff format
Write markdown handoff with fields: topic_id, slug suggestion, short_title, title_draft, dzen_pattern, dzen_shape_hint, external_signal, signal_urls, wordstat_preflight, klyshin_hook, wordstat_rework, wordstat, angle_rotation, queue_slot, cover_season_note, wp_category_hint, interlink_siblings.
