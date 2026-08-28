# Scout input — B03 pack_vs_flat

## Date
2026-08-28 (YEKT), пятница, август — летний сезон (обложка без зимы).

## Tenant
Добрый дом — посуточная аренда Тюмень. Голос от лица ПКОМПАНИИ.

## Angle rotation (last N=3 from WP)
1. Сняли квартиру посуточно в «тихом центре» — рядом стройка (quiet_center_maps)
2. Три ночи. «Кухня есть» — каждый завтрак всё равно в кафе (kitchen_vs_hotel)
3. Выбрал квартиру с оценкой 4,8. Перед оплатой нашёл одинаковые отзывы (reviews_not_rating)

Burn-at-door skip: YES (B01 codes already published).
Deposit/stove skip: YES (B02 already published).

## Klyshin hook (selected)
- hook_id: pack_vs_flat
- queue_num: 6
- original: «Собрал чемодан — в квартире нет полотенец»
- angle: что везти с собой vs что обязано быть в объявлении (полотенца, постель, мыло, шампунь)
- klyshin_signal: checklist AFTER moral; number = price of burn (ночь без душа / 400₽ в магазине)
- dzen_pattern_prefer: [2, 5] → use pattern 2 (кейс с суммами)

## Wordstat preflight
wordstat_get_user_info: OK (MCP-KV Yandex Cloud)

## Wordstat probes (live MCP-KV)
| phrase | region | volume |
|--------|--------|--------|
| квартира посуточно | 225 RU | 1,264,029 |
| снять квартиру посуточно | 225 RU | 812,812 |
| аренда квартиры посуточно | 225 RU | 47,060 |
| квартира посуточно тюмень | 55+11176 | 5,583 |
| снять квартиру посуточно в тюмени | 55+11176 | 1,772 |
| что нужно для аренды квартиры | 225 RU | 591 |
| что нужно для аренды квартиры посуточно | 225 RU | 42 |

## Wordstat rework log
probe «что взять в аренду квартиры» → API format error (totalCount only)
→ rework «что нужно для аренды квартиры» 591 RU
→ rework «аренда квартиры посуточно» 47060 RU (strong P0 spine)
→ localize «квартира посуточно тюмень» 5583 Tyumen
→ final P0: «аренда квартиры посуточно» 47060 RU + «квартира посуточно тюмень» 5583 local

## Anti-dup
NOT duplicate: B01 codes/settlement, B02 deposit/stove scratch.
NOT duplicate: kitchen vs hotel, parking, reviews, checkout bags, quiet center (already on WP).

## Topic assignment
topic_id: B03
slug: sobral-chemodan-v-kvartire-net-polotenec
title draft: Собрал чемодан — в квартире нет полотенец

## CTA funnel (for downstream)
- after checklist → https://t.me/Dobriy_dom_72
- after «у нас так» → MAX https://max.ru/id660300569233_biz or manager https://t.me/Dobriy_dom_Tyumen
- phone: +7 993 574-83-22
- booking: https://добрыйдом-72.рф/
