# Scout inputs — Добрый дом — 2026-08-25 YEKT

## CONDUCTOR PREFLIGHT (HARD — use as-is, do NOT call MCP)
wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API, confirmed by Cursor conductor 2026-08-25)
Derouter utility tier: ACTIVE (this request proves gpt-5.6-terra works)
Your job: write handoff prose ONLY from the frequencies and facts below. Do NOT refuse or ask for MCP.

## Tenant & canon
- tenant: Добрый дом — посуточная аренда / субаренда Тюмень
- topic_id: B03
- date_yekt: 2026-08-25 (summer — NO winter hero on cover)
- dzen_rf_pack: true
- season_note: август/сентябрь, командировочный сезон; не зимний cover

## Angle rotation (last N=3)
Published ledger (`shared/published-titles.md`):
- B01 | beskontaktnoe-zaselenie-posutochno-tyumen | Оплатил квартиру посуточно. Код прислали от чужой двери

Live site recent (anti-dup angles — DO NOT repeat):
parents+vuz 3 nights, hot water, neighbors night, hidden fees, dog at door, passport photo, contract 7 rules, cancellation prepayment, prepayment parties, early 7am checkin, sublease

burn-at-door skip: YES (B01 + saturated on live)
skip families: hot water, neighbors, hidden fees, dog, passport, parents_sept_uni (published today on live — SATURATED)
early check-in: skip (used)

## Queue slot
- window_yekt: 2026-08-29 — 2026-08-31
- queue_num: 2
- selected hook_id: sept_business_trip (best candidate vs parking/kitchen/reviews after Wordstat rework)

## Klyshin hook (original)
- hook_id: sept_business_trip
- original: «Звонок в 10:00. Заселился в 22:00.»
- angle: стол, розетки, реальный Wi‑Fi, закрывающие — до оплаты
- klyshin_signal: reader inside; moral: сначала созвон/доки, потом ключ
- lockpick: «Скорость Wi‑Fi на созвон в 10:00 — где проверить до оплаты?»
- signal: https://t.me/klyshin_A

## Wordstat probes (LIVE mcp-kv — regions 55+11176 Tyumen; compare 225 RU)

### sept_business_trip probes
- «командировка тюмень квартира» — API empty (rework)
- «командировка квартира тюмень» — API empty (rework)
- «командировка тюмень» — 37
- «квартира для командировки» — 18
- «аренда квартиры посуточно» — 801 (similar: «снять квартиру на сутки» 961)
- «снять квартиру посуточно в тюмени» — 1902
- «квартира посуточно тюмень» — 5875 (55+11176) | 13271 (225 RU)

### parking_before_booking probes (compared, not selected)
- «парковка аренда квартиры» — 3 totalCount only
- «парковка при аренде квартиры» — API empty
- «парковка квартира посуточно» — API empty
→ weakest cluster; skip for P0

### kitchen_vs_hotel_cafes probes (compared, not selected)
- «посуточно или отель» — 6 (similar «отель или посуточная квартира» 4)
- «квартира с кухней посуточно» — 3 totalCount
→ very weak; would rework to same high P0 anyway

### reviews_not_rating probes (compared, not selected)
- «отзывы аренда квартиры» — 27
- «посуточная аренда квартир отзывы» — 12
- «суточно ру отзывы» — 38
→ weak vs guest rental P0

## Final P0 (after rework)
- phrase: «квартиры посуточно тюмень»
- volume_tyumen_55_11176: 5875
- volume_ru_225: 13271
- rationale: hook-specific «командировка» clusters 18–37; rework to highest honest guest-intent cluster while keeping business-trip angle (стол/розетки/Wi‑Fi/доки до оплаты)

## wordstat_rework log (for handoff)
probe «командировка тюмень квартира» fail → probe «командировка тюмень» 37 → probe «квартира для командировки» 18 → probe «аренда квартиры посуточно» 801 → probe «снять квартиру посуточно в тюмени» 1902 → final P0 «квартиры посуточно тюмень» 5875 (55+11176) | 13271 (225)

clusters tried: командировка, аренда посуточно, снять посуточно тюмень, parking (3), kitchen (6), reviews (12–38)

## Dzen pattern
- prefer: 2 (кейс с суммами/временем) or 3 (страх → сцена §1)
- NOT pattern 1 (N советов)
- dzen_shape_hint: звонок 10:00 vs заселение 22:00 — стол/розетки/Wi‑Fi до перевода; NOT legal essay

## External signals (today)
1. https://t.me/klyshin_A — angle bank + channel rhythm (guest pain mapping)
2. https://dzen.ru/holyslav — Dzen feed pattern reference (case with sums, docs before money)
3. https://добрыйдом-72.рф/blog/ — tenant blog anti-dup
4. https://t.me/holyslav92 — secondary signal

## Slug suggestion (draft)
komandirovka-stol-rozetki-wifi-do-oplaty

## Anti-dup constraints
- NOT: burn-at-door, parents+vuz, hot water, neighbors, hidden fees, dog, passport, early checkin, sublease
- Guest pain only — no ЕГРН/наследство/ипотека/Шакин
- Facts: Добрый дом хост посуточной Тюмень

## Required handoff format (write this structure verbatim in Russian)

```
topic_id: B03
slug: komandirovka-stol-rozetki-wifi-do-oplaty
title_draft: <Klyshin rhythm, guest pain, no H1 list numbers>
dzen_pattern: 2
dzen_shape_hint: «…»
klyshin_hook: sept_business_trip | original: «Звонок в 10:00. Заселился в 22:00.» | angle: стол, розетки, Wi‑Fi, закрывающие до оплаты | signal: https://t.me/klyshin_A
wordstat_rework: probe «командировка тюмень квартира» fail → «командировка тюмень» 37 → «квартира для командировки» 18 → «аренда квартиры посуточно» 801 → «снять квартиру посуточно в тюмени» 1902 → final P0 «квартиры посуточно тюмень» 5875 | clusters tried: parking 3, kitchen 6, reviews 12–38
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5875 (55+11176) | 13271 (225)
angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B01 + live saturated; parents_sept_uni published today
queue_slot: 2026-08-29 — 2026-08-31 | queue_num 2
external_signal: <1-2 sentences>
signal_urls:
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- https://добрыйдом-72.рф/blog/
```
