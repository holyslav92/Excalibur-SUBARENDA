# Scout assembled input — B29 (2026-09-19 YEKT)

## Tenant
Добрый дом, посуточная Тюмень, guest case for Dzen click (not guide).

## Date
2026-09-19, сентябрь, Asia/Yekaterinburg slot 12:00.

## Anti-dup (skip)
Burn-at-door saturated. Recent B26–B28: dog fee, cold radiators, washing machine+zalog.
B15: Wi‑Fi/desk command trip. B22: passport before code. B02: zalog skol plate.
Do NOT duplicate WP-adjacent angles: late checkout 900₽, lift, «без залога 5000», spravka slug if live.

## Klyshin hook (original)
hook_id: `sept_business_trip` (mechanics only) — командировочный гость, документы **до** оплаты, не Wi‑Fi стол.

## Wordstat (MCP-KV live, regions 55+11176; compare RU 225)
- P0 spine: «квартиры посуточно тюмень» — **4423** (55+11176); **9530** (225)
- «снять квартиру посуточно в тюмени» — 1311 (55+11176)
- «залог посуточно» — 28; «квартиры посуточно залог» — 23
- «посуточно без залога» — 7 (weak; not legal hook)
- «предоплата посуточно» — 3 (weak)
- Rework: ride P0 spine + **командировка / чек / справка для бухгалтерии** guest intent (business traveler closing docs), localized Tyumen supply.

## Final P0
Phrase: **квартиры посуточно тюмень** — volume **4423** (Tyumen+oblast); compare **9530** RU.

## Case angle (guest night already happened)
Two-beat H1 draft: «Оплатили 2 ночи по счёту. Бухгалтерия просит чек — в чате: «мы не гостиница»»
Guest pain: hidden assumption that apartment host gives hotel-style receipt; 2 nights, ₽ on the line, командировка.

## Title draft (for Title role)
«Оплатили 2 ночи по счёту. Бухгалтерия просит чек — в чате: «мы не гостиница»»

## topic_id / slug
B29 / buhgalteriya-zhdet-chek-v-chate-my-ne-gostinica

## signal_urls
https://t.me/klyshin_A
https://dzen.ru/holyslav
https://добрыйдом-72.рф/blog/

## CONDUCTOR PREFLIGHT (already done — do NOT emit SCOUT BLOCKER)
wordstat_preflight: MCP-KV wordstat_get_user_info OK (2026-09-19).
External signals fetched by conductor (klyshin_A channel + dzen holyslav listed above).
Your job: write ONLY the handoff block below into output format; frequencies are canonical in this file.

Required handoff lines (fill verbatim structure):
wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: sept_business_trip | original: «Звонок в 10:00. Заселился в 22:00.» | angle: чек/справка для бухгалтерии до оплаты, не Wi‑Fi | signal: https://t.me/klyshin_A
wordstat_rework: probe «предоплата посуточно» 3 → «залог посуточно» 28 → final P0 «квартиры посуточно тюмень» 4423 | clusters tried: предоплата, залог, командировка spine
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4423 | RU 9530
angle_rotation: checked last N=3 B26 dog / B27 heating / B28 washer+zalog | burn-at-door skip: yes | reason: saturated + recent passport/code family
dzen_pattern: 2
dzen_shape_hint: «Оплатили 2 ночи. Бухгалтерия просит чек — «мы не гостиница»»
topic_id: B29
title_draft: «Оплатили 2 ночи по счёту. Бухгалтерия просит чек — в чате: «мы не гостиница»»
primary_query: квартиры посуточно тюмень
priority: P0
