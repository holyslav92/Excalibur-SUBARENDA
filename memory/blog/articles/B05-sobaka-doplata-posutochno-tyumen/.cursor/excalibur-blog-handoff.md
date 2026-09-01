# Scout handoff — B05 (2026-08-31 YEKT)

topic_id: B05
slug: razreshili-s-lapoy-doplatu-nazvali-posle-zaseleniya
short_title: В объявлении «можно с лапой» — после заселения доплата 3 000 ₽
title_draft: «В объявлении — «можно с лапой». После заселения доплата 3 000 ₽»
dzen_pattern: 2
dzen_shape_hint: «Разрешили с лапой → после заселения 3 000 ₽ за «уборку»»
external_signal: guest pain — pet allowed in listing, surprise surcharge after check-in; live Wordstat demand «посуточная квартира с собакой» 600 RU
signal_urls: https://t.me/klyshin_A | https://добрыйдом-72.рф/blog/
wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-08-31)
klyshin_hook: dog_breed_fee | original: «В объявлении — «можно с лапой». После заселения доплата за собаку.» | angle: гость с питомцем, доплату не озвучили до оплаты; lockpick: «Какая порода и сколько весит?» | signal: https://t.me/klyshin_A
wordstat_rework: probe «посуточная квартира с собакой» 600 (225) / 8 (55+11176) → probe «квартира с собакой снять посуточно» 462 (225) → probe «снять квартиру посуточно в тюмени» 1761 (55+11176) / 4483 (225) → probe «аренда квартиры посуточно» 792 (55+11176) / 45932 (225) → final P0 «посуточная квартира с собакой» 600 | clusters tried: с собакой, посуточно тюмень, аренда посуточно
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «посуточная квартира с собакой» 600 | «аренда квартиры посуточно» 792 (55+11176) / 45932 (225) | «снять квартиру посуточно в тюмени» 1761 | RU spine 4483
angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B02 deposit, B03 vuz distance, B04 third guest fee; new pet surcharge angle
queue_slot: 2026-08-29 — 2026-08-31 (guest pain override sept_business_trip saturation)
cover_season_note: конец лета / начало сентября — без зимних сцен
wp_category_hint: posutochnaya-arenda
interlink_siblings: /blog/beskontaktnoe-zaselenie-posutochno-tyumen/ | /blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/ | /blog/oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego/
