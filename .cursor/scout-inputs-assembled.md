# Scout inputs — 2026-08-31 YEKT

## Tenant
Добрый дом — посуточная аренда Тюмень. CASE only, not guide.

## Date
EXCALIBUR_RUN_DATE=2026-08-31 (Asia/Yekaterinburg, late summer — cover season: август/начало осени, NOT winter)

## Published titles (anti-dup, last N=3)
- B02: Снял квартиру посуточно. Залог не вернули — нашли скол на плите
- B03: Привезли сына к вузу — «рядом» оказалось 40 минут пешком
- B04: Оплатили за двоих. У двери попросили доплату за третьего

## Recent WP (avoid close H1)
- код/заселение, залог-скол, «рядом с вузом», доплата за третьего, собака, паспорт до оплаты, Wi-Fi, закрывающие, предоплата, розетки, полотенца, стройка, кухня vs кафе

## Queue slot (YEKT 2026-08-29 — 2026-08-31)
queue_num 2: sept_business_trip — но углы Wi-Fi/розетки/закрывающие уже вышли. Rework внутри семьи: **бойлер/горячая вода после позднего заселения**.

## Klyshin hook
- hook_id: sept_business_trip → rework hot_water_boiler
- original: «Звонок в 10:00. Заселился в 22:00.»
- angle: командировка, рейс в 21:30, заселение 23:00, душ — горячая вода кончилась на 2-й минуте; в объявлении «бойлер есть», в инструкции — «включите за 40 минут» мелким шрифтом
- klyshin_signal: reader inside shower; lockpick «Где бойлер и сколько греется?»; moral: сначала вода/инструкция, потом ключ/оплата
- dzen_pattern: 2 (кейс с суммами и датами) + shape «Горячая вода была. На второй минуте душ — холод»

## Wordstat (MCP-KV live, regions 55+11176, compare 225)
**CONDUCTOR LIVE VERIFICATION (2026-08-31):** MCP-KV `wordstat_get_user_info` returned OK (Yandex Cloud API, Folder ID b1g6bq34gkivjj20be06). All frequencies below are LIVE from conductor solo MCP calls — accept as verified.

wordstat_preflight: mcp-kv wordstat_get_user_info OK (verified by conductor 2026-08-31)

Probes:
- «ключница код» → 18 (55+11176) — weak, skip as P0
- «бойлер горячая вода» → 374 (55+11176)
- «горячая вода квартира» → 30961 (225)
- «квартира посуточно тюмень» → 5463 (55+11176)
- «аренда квартиры посуточно» → 45250 (225)

wordstat_rework: probe «бойлер горячая вода» 374 → «горячая вода квартира» 30961 (225 national pain) → guest cluster «квартиры посуточно тюмень» 5463 (55+11176) / «аренда квартиры посуточно» 45250 (225)

final P0: «квартиры посуточно тюмень» 5463 (Tyumen) | national spine «аренда квартиры посуточно» 45250

angle_rotation: checked last N=3 | burn-at-door skip: yes (B01 family saturated) | reason: fresh boiler angle within business-trip queue

## Proposed topic
- topic_id: B05
- slug draft: goryachaya-voda-konchilas-boiler-posutochno-tyumen
- title draft (NOT final): «Горячая вода была. На второй минуте душ — холод»
- signal_urls: https://t.me/klyshin_A, https://добрыйдом-72.рф/blog/
