# Scout assembled inputs — 2026-08-29 YEKT 14:00

## CRITICAL INSTRUCTION FOR DEROUTER SCOUT
Wordstat MCP-KV preflight and ALL probes were already executed by the orchestrator via live MCP-KV.
wordstat_preflight: mcp-kv wordstat_get_user_info OK
DO NOT refuse handoff. DO NOT claim CallMcpTool unavailable.
Your job: write the complete `.cursor/excalibur-blog-handoff.md` using ONLY the verified data below.

## Tenant
- Brand: Добрый дом (посуточная / субаренда, Тюмень)
- Voice: клышинская подача, комфорт+, от лица ПК компании. НЕ ЕГРН, НЕ суд, НЕ «мы лучшие»
- Cover season: лето (август, НЕ зима героем)
- dzen_rf_pack: true

## Angle rotation (last N=3 ledger)
- B01: код / бесконтактное заселение — burn-at-door
- B02: залог / скол на плите — deposit
- B03: вуз / «рядом» — parents short stay

angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B01 saturated; queue sept_business_trip SKIP — live WP 2026-08-29 «Звонок в 10:00… розетки» already published; pick parked cancel_prepay

## Klyshin hook
klyshin_hook: cancel_prepay | original: «Перевёл предоплату вечером. Утром — «квартира уже занята».» | angle: сколько и когда платить, как зафиксировать бронь до перевода; lockpick: «Кому именно переводим и что в переписке до денег?» | signal: https://t.me/klyshin_A

## Wordstat rework (LIVE MCP-KV — copy verbatim)
wordstat_rework: probe «предоплата за аренду квартиры посуточно» 42 (225) → probe «предоплата аренда квартиры посуточно» 65 (225) → probe «отмена брони посуточно» 102 (225) → probe «аренда квартиры посуточно» 794 (55+11176) → probe «аренда квартиры тюмень посуточно» 208 (55+11176) → final P0 «аренда квартиры посуточно» 794 (55+11176) | clusters tried: предоплата, отмена брони, аренда посуточно, тюмень посуточно

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «аренда квартиры посуточно» 794 | secondary «аренда квартиры тюмень посуточно» 208 | fear cluster «предоплата за аренду квартиры посуточно» 42 (225)

## topic_id
B04

## short title for research_start (Klyshin rhythm, NOT final H1)
Перевёл предоплату — утром «квартира уже занята»

## dzen_pattern
3 — страх → инструкция в §1
dzen_shape_hint: «перевёл предоплату — «занята»: что спросить до перевода»

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://dzen.ru/holyslav

## Required handoff format
Write markdown handoff with fields: topic_id, short_title, title_draft, dzen_pattern, dzen_shape_hint, external_signal, signal_urls, wordstat_preflight, klyshin_hook, wordstat_rework, wordstat, angle_rotation, queue_slot (parked cancel_prepay — sept_business_trip saturated on live WP), cover_season_note (summer), wp_category_hint (posutochnaya-arenda), interlink_siblings (B01, B02, B03 URLs from published-articles).
