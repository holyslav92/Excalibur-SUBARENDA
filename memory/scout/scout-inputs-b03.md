# Scout inputs B03 — 2026-08-23 YEKT

## Date context
- today: 2026-08-23, август, YEKT Asia/Yekaterinburg
- season: late summer — обложка без зимнего героя (снег/мороз/лед)

## Tenant
Добрый дом — посуточная аренда / субаренда Тюмень. Голос: клышинская подача, от лица компании, комфорт+.

## Anti-dup (published / recent — НЕ повторять)
- B01: коды/бесконтактное заселение
- B02: залог/скол на плите
- dogovor-arendy-pravila-prozhivaniya, otmena-bronirovaniya, predoplata+правила, ranniy zaezd, subarenda, uborka, skrytye-doplaty, sosedi, cena-ot, internet-tv

## Klyshin signal (live 2026-08-23)
- Channel: https://t.me/klyshin_A — fresh posts about purchase risks, not pets; angle bank hook `contract_bans` + buyer fear «в правилах мелким»
- Bank hook id: pets_short_term (new) | angle from contract_bans: «что написано в правилах до оплаты»

## Wordstat preflight
wordstat_preflight: mcp-kv wordstat_get_user_info OK

## Wordstat probes (live MCP-KV)
| phrase | RU 225 | Tyumen 55+11176 |
|--------|--------|-----------------|
| посуточно квартиры с животными | 1499 | (in RU top) |
| снять квартиру посуточно с животными | 1165 | тюмень: 26 |
| квартиры посуточно тюмень с животными | — | 4 |
| тюмень снять квартиру посуточно с животными | — | 3 |
| показания счетчиков аренда квартиры | 85 | weak — skip |
| коммунальные платежи аренда квартиры | 599 | not short-term buyer |

## Rework log
probe «показания счетчиков аренда» 85 → not buyer P0 for guests
probe «жкх при аренде» weak format → skip
probe «посуточно квартиры с животными» 1499 → «снять квартиру посуточно с животными» 1165 → localize Tyumen 26+3 → final P0 cluster pets+short-term

## Final P0
«снять квартиру посуточно с животными» — 1165 (RU 225); Tyumen slice 26+3

## Dzen
dzen_pattern: 4 — contrast «в объявлении можно, в правилах нет»
dzen_shape_hint: «Забронировал с собакой. На заселении: «мы не знали»»

## Proposed
topic_id: B03
slug: zabroniroval-s-sobakoj-v-pravilah-melkim-s-zhivotnymi-net
title_draft: Забронировал посуточно с собакой. В правилах мелким: «с животными не сдаём»
