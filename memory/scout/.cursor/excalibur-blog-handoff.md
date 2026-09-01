# Scout handoff — B05

topic_id: B05  
slug: reyting-48-dva-otzyva-vse-super  
title_draft: **Рейтинг 4,8. Два «всё супер» — и ночь за 3 900 ₽ уже не кажется удачной**  

topic: Гость выбирает квартиру посуточно в Тюмени по рейтингу 4,8, но замечает два одинаковых свежих отзыва. Кейс не о «плохих звёздах», а о проверке повторов, дат и конкретики до предоплаты.

wordstat_preflight: mcp-kv wordstat_get_user_info OK

klyshin_hook: reviews_not_rating | original: «4.8 — и два одинаковых „всё супер“» | angle: не звёзды — повторы, свежесть, конкретика в отзывах Sutochno/Avito глазами гостя | signal: https://t.me/klyshin_A

wordstat_rework: probe «отзывы аренда квартиры» 28 (55+11176) → «аренда квартиры посуточно отзывы» 12 (55+11176) → «суточно отзывы» 5880 (225, guest review-intent) → локальный demand spine «квартиры посуточно тюмень» 5463 (55+11176) + «авито квартиры посуточно тюмень» 335 (55+11176) | clusters tried: отзывы, посуточная аренда, суточно отзывы, квартиры посуточно Тюмень, Avito

wordstat: mcp_kv live | regions 55,11176, compare 225 | P0 «квартиры посуточно тюмень» 5463 | national review-intent comparison: «суточно отзывы» 5880 (225)

angle_rotation: checked last N=3 | burn-at-door skip: no | reason: последние темы — залог/скол на плите, вуз/долгая дорога, доплата за третьего; B05 — отдельное семейство выбора по отзывам и не повторяет запретные углы

dzen_pattern: 2  
dzen_shape_hint: «Рейтинг 4,8. Два отзыва — одно и то же: „всё супер“» — кейс с ценой ночи и проверкой до предоплаты

external_signal: Свежий спрос на квартиры посуточно в Тюмени высокий; узкий запрос про отзывы локально мал, поэтому отзывный хук переработан в P0 выбора квартиры посуточно с конкретным guest-сценарием.

signal_urls:
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- https://t.me/holyslav92

klyshin_bank_update: last_seen 2026-09-01 | wordstat_rework_log updated | final_p0 «квартиры посуточно тюмень» 5463 | used_in_articles B05 planned
