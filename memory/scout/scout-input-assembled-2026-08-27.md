# Scout assembled inputs — 2026-08-27 YEKT

## Date context
- today: 2026-08-27, август, четверг
- timezone: Asia/Yekaterinburg
- season: late summer (обложка — текущий сезон, не зима)

## Tenant
Добрый дом — посуточная аренда Тюмень. Говорим от лица ПКОМПАНИИ. Комфорт+, не бизнес-класс.

## Published titles (anti-dup)
- B01: код/бесконтактное заселение — SKIP burn-at-door family
- B02: залог на выезде — SKIP deposit family
- Recent WP: parents/uni, business trip wifi, hot water, neighbors, hidden fees, dog, passport, contract, cancel, parking, checkout bags

## Angle rotation (last N=3)
Last 3: checkout bags, parking, business trip — NOT burn-at-door. reviews_not_rating NOT covered.

## Queue slot
window_yekt: 2026-08-26 — 2026-09-03 (reviews_not_rating queue 5, approaching 01-03.09)

## Klyshin hook (bank)
- hook_id: reviews_not_rating
- original: «4.8 — и два одинаковых «всё супер»»
- angle: не звёзды — повторы, свежесть, Sutochno/Avito guest angle
- klyshin_signal: quote review → break; refusal: «Нет. Так не выбираем.»
- dzen_pattern_prefer: [2, 3]

## Wordstat preflight
wordstat_preflight: mcp-kv wordstat_get_user_info OK

## Wordstat probes (live MCP-KV)

### Probe 1: «отзывы аренда квартиры»
- RU 225: 3463 (аренда квартиры отзывы)
- Tyumen 55+11176: 27 (слабый локальный)

### Rework round 1: «аренда квартиры посуточно отзывы»
- RU 225: 248
- «суточно ру отзывы» в related: 3506

### Rework round 2: «суточно отзывы»
- RU 225: 6260 (суточно отзывы)
- «суточно ру отзывы»: 3715
- «отзыв на квартиру по суточно»: 331
- «квартиры на суточно ру отзывы»: 145

### Rework round 3 (Tyumen localize): «квартира посуточно тюмень»
- RU 225: 12957
- Tyumen 55+11176: 5675

### Final P0 spine
- RU: «суточно ру отзывы» — 3715
- Tyumen demand: «квартиры посуточно тюмень» — 5675
- Guest intent cluster: читать отзывы перед бронированием посуточно в Тюмени

## Title draft (Klyshin rhythm, NOT final H1)
На карточке 4,8 — и два одинаковых «всё супер»

## topic_id suggestion
B03

## dzen_pattern
2 (кейс с суммами/датами) + guest reading reviews before paying

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/

## Forbidden dup
NOT codes/settlement, NOT deposit/scratch on plate, NOT parents/uni (Aug 25), NOT parking/checkout/business trip (recent)
