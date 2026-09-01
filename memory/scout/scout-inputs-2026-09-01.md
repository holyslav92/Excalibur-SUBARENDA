# Scout inputs — 2026-09-01 YEKT slot

## Date context
- today: 2026-09-01 (вторник), Asia/Yekaterinburg
- season: начало сентября, лето/осень переход — обложка без зимнего героя

## Queue slot (p0_queue)
- window: 2026-09-01 — 2026-09-03
- queue_num: 5
- hook_id: reviews_not_rating

## Angle rotation (last N=3 from shared/published-titles.md)
- B02: залог / скол на плите
- B03: рядом с вузом / 40 минут пешком
- B04: доплата за третьего у двери
- burn-at-door skip: no (last 3 not from код/заселение family)

## Klyshin hook (reviews_not_rating)
- original: «4.8 — и два одинаковых «всё супер»»
- angle: не звёзды — повторы, свежесть, Sutochno/Avito guest angle
- signal: https://t.me/klyshin_A (mechanics only, no Moscow/legal copy)

## Wordstat preflight
- wordstat_get_user_info: OK (MCP-KV)

## Wordstat probes (live MCP-KV)
| probe | regions | volume |
|-------|---------|--------|
| отзывы аренда квартиры | 55+11176 | 28 |
| отзывы аренда квартиры | 225 | 3493 |
| аренда квартиры посуточно отзывы | 55+11176 | 12 |
| суточно отзывы | 225 | 5880 |
| посуточная аренда квартир отзывы | 55+11176 | 12 |
| квартиры посуточно тюмень | 55+11176 | 5463 |
| снять квартиру посуточно в тюмени | 55+11176 | 1754 |
| авито квартиры посуточно тюмень | 55+11176 | 335 |

## Rework log
probe «отзывы аренда квартиры» 28 (55+11176) → «аренда квартиры посуточно отзывы» 12 → «суточно отзывы» 5880 (225, guest channel intent) → localize buyer spine «квартиры посуточно тюмень» 5463 (55+11176) + «авито квартиры посуточно тюмень» 335

## Final P0
- phrase: квартиры посуточно тюмень
- volume_tyumen: 5463
- volume_ru_compare: use «суточно отзывы» 5880 as national review-intent spine

## Anti-dup (do NOT repeat H1 angles)
- код/заселение (B01 + recent WP)
- залог скол плита (B02)
- рядом с вузом (B03)
- доплата третьего (B04)
- парковка шлагбаум 800 (WP 2026-09-01)
- собака/лапа, паспорт до оплаты, горячая вода, Wi‑Fi созвон

## Dzen pattern
- prefer: 2 (кейс с суммами) or 3 (страх → инструкция в §1)
- shape hint: «Рейтинг 4,8. Два отзыва — одно и то же: «всё супер»»

## Tenant
- Добрый дом, посуточная Тюмень, guest-night CASE not guide

## Output request
Return ONLY the handoff markdown as your assistant message (the conductor script writes it to disk — you do NOT write files yourself). Do NOT return DEROUTER SCOUT BLOCKER. Format like memory/scout/scout-handoff-b02.md with all required lines: wordstat_preflight, klyshin_hook, wordstat_rework, wordstat, angle_rotation, dzen_pattern, topic_id B05, slug, title_draft (two-beat Klyshin), signal_urls.
