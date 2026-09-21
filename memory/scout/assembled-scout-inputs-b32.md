Ты — Scout (gpt-5.6-terra). Среда рабочая: Derouter REST, MCP-KV Wordstat уже вызван дирижёром.
ЗАДАЧА: вывести ТОЛЬКО готовый handoff markdown (без BLOCKER, без «не могу писать файлы»).
Ниже факты слота — оформи по контракту Scout skill.

## Published titles (last 3)
- B29: Оплатили 2 ночи. Бухгалтерия просит чек — «мы не гостиница»
- B30: Продление до двух согласовали. После сдачи ключей с карты списали 1 800 ₽
- B31: Оплатили 3 ночи. Открыли дверь — внутри чужие чемodany

## Anti-dup (WP ledger drift — do NOT reuse angles)
- zalog-utrom-posle-uborki, bez-predoplaty-4200-na-kartu, bez-zaloga-pered-kodom-5000
- B10 taxi 2400 «всё включено», B08 predoplata silence, B02 zalog skol plita, kod/keybox family saturated

## Klyshin hook
kitchen_vs_hotel + hidden_fees mechanics | original: «Три ночи. Кухня «есть» — или каждый день кафе?» reworked to **final price in app** | angle: guest sees one nightly price in listing, at checkout aggregator adds service/cleaning line before key — NOT door taxi (B10), NOT post-checkout card (B30), NOT prepay ghost (B08)

## Wordstat (live MCP-KV, director verified)
wordstat_preflight: mcp-kv wordstat_get_user_info OK
wordstat_rework: probe «скрытая доплата посуточно» API totalCount-only → «посуточно комиссия» 1903 (225) | «авито посуточно комиссия» 1036 | «квартиры посуточно без комиссии» 328 (225) → «отель или посуточная квартира» 280 (225) / 7 (55+11176) → «посуточно или отель» 355 (225) → final P0 «квартиры посуточно тюмень» 4409 (55+11176) | compare 9372 (225)
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4409/9372 | supporting: посуточно комиссия 1903 | квартиры посуточно без комиссии 328 | отель или посуточная квартира 280

angle_rotation: checked last N=3 | burn-at-door skip: no (last3 = docs/cleaning/card/chemodany) | skip saturated: kod, zalog-skоl, predoplata-live-slugs

dzen_pattern: 2
dzen_shape_hint: «В карточке 4 200 ₽» → «На оплате 5 050» до ключа

topic_id: B32
title_draft: В карточке 4 200 ₽. На оплате — 5 050. Ключ ещё не брали
slug: v-kartochke-4200-na-oplate-5050-klyuch-eshe-ne-brali
primary_query: квартиры посуточно тюмень комиссия цена в приложении

Формат вывода (обязательные строки):
topic_id: B32
title: ...
slug: ...
primary_query: ...
dzen_pattern: 2
klyshin_hook: ...
wordstat_preflight: ...
wordstat_rework: ...
wordstat: ...
angle_rotation: ...
external_signal: guest final checkout line vs card price; compare hotel vs flat without surprise fees
signal_urls: https://t.me/klyshin_A
