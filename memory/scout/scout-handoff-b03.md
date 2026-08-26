# Scout handoff B03 — выезд и поезд (чемоданы)

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-08-26)
klyshin_hook: checkout_train_bags | original: «Выезд в 12:00. Поезд в 16:30.» | angle: куда деть чемоданы между выездом и поездом; moral: сначала багаж/хранение, потом ключ | signal: https://t.me/klyshin_A/ (ритм «сюда деньги не несем» → уточнить багаж до выезда, не у такси)
wordstat_rework: probe «хранение багажа» 122 → «хранение багажа тюмень» 22 → «поздний выезд» 130 → «аренда квартиры посуточно» 821 → final P0 «квартиры посуточно тюмень» 5675 | clusters tried: хранение багажа, поздний выезд, аренда квартиры посуточно, квартира посуточно тюмень
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5675 | P1 «снять квартиру посуточно в тюмени» 1819 | P1 «поздний выезд» 130 | P1 «хранение багажа» 122 | compare RU225 «квартиры посуточно тюмень» 12957
angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B01 burn-at-door published; queue slot parents_sept_uni saturated (WP 2026-08-25 вуз/родители); sept_business_trip saturated (WP 2026-08-25); parking saturated (WP 2026-08-26); early_checkin saturated (WP 2026-08-21) → override to checkout_train_bags
dzen_pattern: 2
dzen_shape_hint: «Выезд 12:00, поезд 16:30 — где чемоданы и сколько продление»
queue_slot: 8 | window_yekt 2026-08-26 — override from slot 1 (saturated)
season_note: YEKT 2026-08-26 summer; cover = summer (no winter hero)
topic_id: B03
slug: vyezd-v-12-poezd-v-16-30-gde-chemodany-posutochno
title_draft: Выезд в 12:00. Поезд в 16:30. Чемоданы — не в такси
angle: до брони/заезда — где хранить багаж, до скольки выезд, цена продления; от лица ПКОМПАНИИ «Добрый дом», комфорт+, Тюмень
anti_dup: early_checkin (ранний заезд) — другой угол; burn-at-door B01; залог B02
external_signal: klyshin_A live — проверка до аванса; dzen holyslav — сделка сорвалась до денег (проверить до оплаты)
signal_urls:
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- https://добрыйдом-72.рф/blog/
- https://t.me/holyslav92
