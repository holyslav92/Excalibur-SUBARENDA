# Scout inputs — 2026-08-27 YEKT

## Run context
- date_yekt: 2026-08-27 (четверг, август, лето)
- tenant: Добрый дом, посуточная аренда Тюмень
- season: late summer — обложка и сцены БЕЗ зимы/снега/льда

## Angle rotation (last N=3 published WP)
1. «Три ночи. «Кухня есть» — каждый завтрак всё равно в кафе» (kitchen_vs_hotel)
2. «Выбрал квартиру с оценкой 4,8. Перед оплатой нашёл одинаковые отзывы» (reviews)
3. «Гость выехал в 12:00. Поезд в 16:30. Чемоданы — не в такси» (checkout_train)

burn-at-door skip: yes (B01 codes + B02 zalog already; not repeating)

## Queue pick
- hook_id: quiet_center_maps (queue_num 7)
- window: 2026-09-08 — 2026-09-10 batch, but prior queue slots 1–5 done on WP
- original Klyshin hook: «Тихий центр» — за окном стройка
- angle: 7 минут в Картах/панорамах — не слова хоста; проверить шум до брони
- dzen_pattern: 5 (локальный + сезонный)
- anti_dup: not kitchen, reviews, parking, checkout, parents_uni, business_trip, codes, zalog

## Wordstat live (MCP-KV, regions 55+11176)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probe original «аренда квартиры тюмень центр»: 15
Probe rework «квартира посуточно тюмень»: 5583
Probe rework «тюмень квартиры посуточно центр»: 282
Probe rework «снять квартиру посуточно в центре тюмени»: 230
Compare RU 225 «квартира посуточно тюмень»: 12766

wordstat_rework: probe «аренда квартиры тюмень центр» 15 → «тюмень квартиры посуточно центр» 282 → final P0 «квартира посуточно тюмень» 5583 | clusters tried: center, посуточно тюмень, центр тюмень

## Published titles anti-dup (ledger)
- B01 beskontaktnoe-zaselenie (коды/заселение) — SKIP family
- B02 perevel-zalog (залог/скол на плите) — SKIP family

## Klyshin signal
- bank: memory/scout/klyshin-topic-bank.json hook quiet_center_maps
- channel: https://t.me/klyshin_A (angle only, localize Tyumen guest)

## Title draft (Klyshin rhythm, NOT final)
«Тихий центр» в объявлении. За окном — стройка

## Required handoff fields
Write .cursor/excalibur-blog-handoff.md with topic_id B03, slug, title_draft, dzen_pattern, signal_urls, all wordstat lines.
