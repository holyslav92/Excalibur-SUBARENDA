# Scout assembled inputs — 2026-08-28 YEKT

## CRITICAL INSTRUCTION FOR DEROUTER SCOUT
Wordstat MCP-KV preflight and ALL probes were already executed by the orchestrator via live MCP-KV.
wordstat_preflight: mcp-kv wordstat_get_user_info OK
DO NOT refuse handoff. DO NOT claim CallMcpTool unavailable.
Your job: write the complete `.cursor/excalibur-blog-handoff.md` using ONLY the verified data below.

## Tenant
- Brand: Добрый дом (посуточная / субаренда, Тюмень)
- Voice: клышинская подача, комфорт+, от лица компании. НЕ ЕГРН, НЕ суд, НЕ «мы лучшие»
- Cover season: лето (не зима героем)
- dzen_rf_pack: true

## Angle rotation (last N=3)
- B01: «Оплатил квартиру посуточно. Код прислали от чужой двери» — burn-at-door
- B02: залог на выезде / «не вернём» — deposit family

angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B01 burn-at-door; new hook parents_sept_uni (university short stay, not code/door)

Site blog anti-dup sibling (different angle required): «Приехали на 3 ночи к вузу — три остановки. Кровати не хватило» — our article = minutes walk to campus + enrollment window, NOT beds.

## Klyshin hook
klyshin_hook: parents_sept_uni | original: «Привёз сына в вуз. Три ночи. В объявлении — «рядом с вузом».» | angle: 2–4 ночи на оформление, не годовая; lockpick: сколько минут пешком до корпуса? | signal: https://t.me/klyshin_A (live Aug 26 2026 — «формально чисто → риск», map to «рядом с вузом» в объявлении)

## Wordstat rework (LIVE MCP-KV — copy verbatim)
wordstat_rework: probe «аренда квартиры на несколько дней» 66 (225) → probe «снять квартиру на несколько дней тюмень» 1 (55+11176) → probe «снять квартиру на сутки тюмень» 363 (55+11176) → probe «аренда квартиры посуточно» 811 (55+11176) / 46755 (225) → probe «снять квартиру посуточно в тюмени» 1749 (55+11176) → final P0 «квартиры посуточно тюмень» 5534 (55+11176) / 12553 (225) | clusters tried: несколько дней, студент, на сутки, посуточно, квартиры посуточно тюмень

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5534 | RU compare 12553 | secondary «снять квартиру посуточно в тюмени» 1749

## topic_id
B03

## short title for research_start (Klyshin rhythm, NOT final H1)
Привёз сына в вуз на три ночи — «рядом» оказалось три остановки

## dzen_pattern
5 — локальный + сезонный (1 сентября, родители + вуз, август бронь)
dzen_shape_hint: «Три ночи к вузу: «рядом» в объявлении vs минуты пешком на карте»

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://dzen.ru/holyslav

## Required handoff format
Write markdown handoff with fields: topic_id, short_title, title_draft, dzen_pattern, dzen_shape_hint, external_signal, signal_urls, wordstat_preflight, klyshin_hook, wordstat_rework, wordstat, angle_rotation, queue_slot, cover_season_note, wp_category_hint (posutochnaya-arenda), interlink_siblings (B01, B02 URLs from published-articles).
