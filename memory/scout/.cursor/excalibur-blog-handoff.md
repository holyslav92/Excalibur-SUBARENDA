Соберу handoff через Derouter utility по переданным верифицированным данным, без добавления непроверенных частот или фактов.Сначала передаю Derouter полный контекст с обязательными полями и ограничениями anti-dup.```markdown
# Excalibur blog scout handoff

topic_id: B04

short_title: «Заселился в 22:00 — в 10:00 созвон, а закрывающие обещают после выезда»

title_draft: «Квартира посуточно в Тюмени на две ночи: в 10:00 созвон, а закрывающие обещают после выезда»

dzen_pattern: 3

dzen_shape_hint: «Две ночи в командировке: созвон в 10:00 — Wi‑Fi и закрывающие до перевода, не «пришлём потом»»

external_signal: Клышинский ритм «сначала проверка, потом деньги», переложенный на командировку в Тюмени: рабочий стол, реальный Wi‑Fi для видеосозвона и закрывающие документы нужно проверить до оплаты. Угол не повторяет розетку, код от двери, залог или близость к вузу.

signal_urls:
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://dzen.ru/holyslav

wordstat_preflight: mcp-kv wordstat_get_user_info OK

klyshin_hook: sept_business_trip | original: «Звонок в 10:00. Заселился в 22:00.» | angle: стол + Wi‑Fi на созвон + закрывающие до оплаты (NOT розетка — WP duplicate) | signal: https://t.me/klyshin_A (live Aug 2026 — ритм «сначала проверка, потом деньги»; map to guest командировка, не Dubai/ЕГРН)

wordstat_rework: probe «командировка тюмень квартира» ~1 (225, weak) → probe «квартира на командировку тюмень» fail/0 → probe «командировочные расходы квартира» fail/0 → probe «вайфай аренда квартиры» ~2 (weak) → probe «посуточно или отель» 4 (weak) → probe «аренда квартиры посуточно» 794 (55+11176) → probe «снять квартиру на сутки тюмень» 363 (55+11176) → probe «квартира посуточно тюмень» → final P0 «квартиры посуточно тюмень» 5523 (55+11176) / 12487 (225) | clusters tried: командировка, командировочные, вайфай, посуточно/отель, аренда посуточно, на сутки, квартиры посуточно тюмень

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5523 | RU compare 12487 | secondary «снять квартиру посуточно в тюмени» 1755 | tertiary «аренда квартиры посуточно» 794

angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: new hook sept_business_trip — командировка/созвон, NOT code/door family; NOT deposit; NOT university walk

queue_slot: 2026-08-29 — 2026-08-31 (hook_id sept_business_trip, queue #2)

cover_season_note: лето

wp_category_hint: posutochnaya-arenda

interlink_siblings:
- B01: https://добрыйдом-72.рф/blog/beskontaktnoe-zaselenie-posutochno-tyumen/
- B02: https://добрыйдом-72.рф/blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/
- B03: /blog/kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki/
```
