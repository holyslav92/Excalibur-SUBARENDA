# Scout assembled inputs — 2026-08-30 YEKT

## CRITICAL INSTRUCTION FOR DEROUTER SCOUT
Wordstat MCP-KV preflight and ALL probes were already executed by the orchestrator via live MCP-KV.
wordstat_preflight: mcp-kv wordstat_get_user_info OK
DO NOT refuse handoff. DO NOT claim CallMcpTool unavailable.
Your job: write the complete `.cursor/excalibur-blog-handoff.md` using ONLY the verified data below.

## Tenant
- Brand: Добрый дом (посуточная / субаренда, Тюмень)
- Voice: клышинская подача, комфорт+, от лица хоста/компании. НЕ ЕГРН, НЕ суд, НЕ «мы лучшие»
- Cover season: лето (август, НЕ зима героем)
- dzen_rf_pack: true

## Angle rotation (last N=3 published)
- B01: «Оплатил квартиру посуточно. Код прислали от чужой двери» — burn-at-door / код
- B02: «Снял квартиру посуточно. Залог не вернули — нашли скол на плите» — deposit
- B03: «Привёз сына в вуз на три ночи — «рядом» оказалось три остановки» — parents/university short stay

angle_rotation: checked last N=3 | burn-at-door skip: yes (B01 saturated) | reason: new hook sept_business_trip — командировка/созвон, NOT code/door family; NOT deposit; NOT university walk

## WP blog anti-dup (HARD — new angle required)
На сайте уже есть пост «Звонок в 10:00. Заселился в 22:00 — у стола нет розетки» (slug zvonok-v-10-00).
**ЗАПРЕЩЕНО** копировать угол «нет розетки / нет у стола розетки».
**Обязательный угол B04:** закрывающие документы (чек/акт/счёт для бухгалтерии) + реальный Wi‑Fi на видеосозвон + рабочий стол — всё это проверить **до оплаты**, не после заселения в 22:00.
Lockpick: «Закрывающие пришлёте до выезда? Какой Wi‑Fi на upload для Zoom?»

## Klyshin hook (queue slot 29–31.08)
klyshin_hook: sept_business_trip | original: «Звонок в 10:00. Заселился в 22:00.» | angle: стол + Wi‑Fi на созвон + закрывающие до оплаты (NOT розетка — WP duplicate) | signal: https://t.me/klyshin_A (live Aug 2026 — ритм «сначала проверка, потом деньги»; map to guest командировка, не Dubai/ЕГРН)

## Wordstat rework (LIVE MCP-KV — copy verbatim)
wordstat_rework: probe «командировка тюмень квартира» ~1 (225, weak) → probe «квартира на командировку тюмень» fail/0 → probe «командировочные расходы квартира» fail/0 → probe «вайфай аренда квартиры» ~2 (weak) → probe «посуточно или отель» 4 (weak) → probe «аренда квартиры посуточно» 794 (55+11176) → probe «снять квартиру на сутки тюмень» 363 (55+11176) → probe «квартира посуточно тюмень» → final P0 «квартиры посуточно тюмень» 5523 (55+11176) / 12487 (225) | clusters tried: командировка, командировочные, вайфай, посуточно/отель, аренда посуточно, на сутки, квартиры посуточно тюмень

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5523 | RU compare 12487 | secondary «снять квартиру посуточно в тюмени» 1755 | tertiary «аренда квартиры посуточно» 794

## topic_id
B04

## short title for research_start (Klyshin rhythm, NOT final H1)
Заселился в 22:00 — в 10:00 созвон, а закрывающие обещают после выезда

## dzen_pattern hint
Prefer pattern 2 (кейс с суммами/датами) or 3 (страх → сцена §1): командировка, созвон 10:00, документы до оплаты.
dzen_shape_hint: «Две ночи в командировке: созвон в 10:00 — Wi‑Fi и закрывающие до перевода, не «пришлём потом»»

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://dzen.ru/holyslav

## interlink siblings (published)
- B01: https://добрыйдом-72.рф/blog/beskontaktnoe-zaselenie-posutochno-tyumen/
- B02: https://добрыйдом-72.рф/blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/
- B03: /blog/kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki/

## queue_slot
2026-08-29 — 2026-08-31 (hook_id sept_business_trip, queue #2)

## wp_category_hint
posutochnaya-arenda

## Required handoff format
Write markdown handoff with fields: topic_id, short_title, title_draft, dzen_pattern, dzen_shape_hint, external_signal, signal_urls, wordstat_preflight, klyshin_hook, wordstat_rework, wordstat, angle_rotation, queue_slot, cover_season_note (лето), wp_category_hint, interlink_siblings.
