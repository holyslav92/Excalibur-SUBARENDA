# Scout inputs — B03 slot 2026-08-23 YEKT

Date: 2026-08-23, Asia/Yekaterinburg, август (лето — без зимнего героя на обложке)
Tenant: Добрый дом — посуточная аренда Тюмень, голос ПКОМПАНИИ, комфорт+
Brand: не дублировать B01 (коды/заселение), B02 (залог/скол на плите)

## Published anti-dup (titles only)
- B01 beskontaktnoe-zaselenie — коды/чужая дверь
- B02 zalog skol na plite — залог не вернули
Recent WP: договор/запреты, отмена, вечеринки, ранний заезд, субаренда, уборка, доплаты, соседи, цена «от», интернет

## Klyshin bank hook (rework for pets)
hook_id: contract_bans (rework)
original: «что нельзя делать по договору аренды» → angle: животные в посуточной — что спросить до оплаты
signal: https://t.me/klyshin_A (angle: правила в договоре vs обещание в объявлении)

## Wordstat live (MCP-KV, 2026-08-23)
wordstat_preflight: wordstat_get_user_info OK

Probes:
- «снять квартиру посуточно с животными» RU 225 → 1139 (P0)
- «снять квартиру посуточно с животными» Tyumen 55+11176 → 11
- «снять квартиру посуточно можно с животными» RU → 64
- «снять квартиру в тюмени посуточно с животными» RU → 24
- «тюмень снять квартиру посуточно с животными» Tyumen → 3
- compare: «животные в квартире посуточно» RU → 910 (city noise, not P0)

wordstat_rework: hook «животные в квартире посуточно» 910 (много Москва/СПб) → buyer spine «снять квартиру посуточно с животными» 1139 → localize Tyumen supply only in article body

final P0: «снять квартиру посуточно с животными» 1139 RU / 11 Tyumen

## dzen_pattern
dzen_pattern: 1
dzen_shape_hint: «5 вопросов хозяину до оплаты, если едете с питомцем»

## External signal URLs (fetch for scout)
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- Avito/forum: опыт «с животными» посуточно, доплаты, отказ после брони

## Output required
topic_id B03, slug, title_draft (Klyshin case hook, без SEO-хвоста), angle, anti_dup note, season_note, wordstat lines for handoff template.
