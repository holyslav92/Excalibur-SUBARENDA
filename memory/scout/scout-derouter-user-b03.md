# Scout task — OUTPUT handoff markdown ONLY

IMPORTANT: Do NOT attempt MCP or shell calls. All Wordstat frequencies below are LIVE from MCP-KV (already fetched by conductor). Your job: write `.cursor/excalibur-blog-handoff.md` content in exact handoff format.

## Required output format (copy structure exactly)

```
wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-08-24)
klyshin_hook: <id> | original: «…» | angle: …
wordstat_rework: probe «…» <freq> → … → final P0 «…» <freq>
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «…» <freq> | …
dzen_pattern: 3
dzen_shape_hint: «…»
topic_id: B03
slug: zabroniroval-posutochno-s-sobakoy-na-zaselenii-skazali-ne-puskayut
title_draft: …
angle: …
anti_dup: …
season_note: YEKT 2026-08-24 август — лето, без зимы на обложке
external_signal: https://t.me/klyshin_A
signal_urls: https://t.me/klyshin_A, https://добрыйдом-72.рф/blog/
```

## Klyshin hook
- id: pets_short_term (new bank entry)
- original: «животные в договоре аренды — пункт до подписания»
- angle: гость с собакой/кошкой посуточно; «на словах можно», на заселении отказ или доплата

## Wordstat LIVE data (MCP-KV 2026-08-24)

### RU 225
- посуточно с собакой — 1370
- квартиры посуточно с собакой — 647
- снять квартиру посуточно с собакой — 502
- аренда квартиры с животными — 1095
- аренда квартиры посуточно с животными — 45
- договор аренды квартиры с животными — 185
- пункт про животных в договоре аренды квартиры — 14

### Tyumen 55+11176
- аренда квартир посуточно тюмень — 210
- снять квартиру посуточно с собакой — 2
- аренда квартиры с животными — 4
- посуточная аренда (similar cluster) — 2172

## Rework path
probe «аренда квартиры с животными» 1095 → «аренда квартиры посуточно с животными» 45 → rework «посуточно с собакой» 1370 → final P0 «посуточно с собакой» 1370; local Tyumen anchor «аренда квартир посуточно тюмень» 210

## Anti-dup
NOT: B01 codes/check-in, B02 deposit/chip, passport, contract bans, cancellation, hidden fees, neighbors, price-from, sublease, early check-in, cleaning

## Title draft (Klyshin case hook, not final H1)
Забронировал посуточно с собакой — на заселении сказали «не пускаем»

Write the complete handoff now. Russian. No BLOCKER messages.
