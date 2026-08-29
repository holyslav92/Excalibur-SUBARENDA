# Scout handoff B04

topic_id: B04

short_title: Звонок в 10:00 — заселился в 22:00: стол есть, розетки нет

title_draft: Командировка в Тюмень: созвон в 10:00, заселение в 22:00 — что спросить до оплаты

slug: komandirovka-v-tyumen-sozvon-v-1000-zaselenie-v-2200

dzen_pattern: 2 — живой кейс с суммами/временем (10:00 vs 22:00, Wi‑Fi/закрывающие до оплаты)

dzen_shape_hint: «Командировка в Тюмень: созвон утром — ключ вечером; что спросить до перевода»

external_signal: Klyshin Aug 2026: «Сначала деньги под контролем. Потом договор.» → guest map: закрывающие/реквизиты/рабочее место до предоплаты. Site blog Aug 2026: командировочный кейс 10:00/22:00 — наш угол шире (стол, Wi‑Fi, доки).

signal_urls:
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://dzen.ru/holyslav
- https://t.me/holyslav92

wordstat_preflight: mcp-kv wordstat_get_user_info OK

klyshin_hook: sept_business_trip | original: «Звонок в 10:00. Заселился в 22:00.» | angle: стол, розетки, реальный Wi‑Fi, закрывающие — до оплаты | signal: https://t.me/klyshin_A (live Aug 2026 — мораль «сначала деньги/доки под контролем, потом ключ»; пост про порядок расчётов: расписка до денег = мина → map на закрывающие до предоплаты у хоста)

wordstat_rework: probe «командировка тюмень квартира» API empty → probe «командировка квартира» 41 (55+11176) / 4188 (225) → probe «командировка тюмень» 40 / 82 → probe «квартира для командировки» 18 / 1370 → probe «квартиры посуточно командировка» 60 (225 only) → probe «посуточно или отель» 4 / 445 → probe «аренда квартир посуточно тюмень» 218 → probe «аренда квартиры посуточно» 811 / 46755 → probe «снять квартиру посуточно в тюмени» 1749 / 4560 → final P0 «квартиры посуточно тюмень» 5534 (55+11176) / 12553 (225) | clusters tried: командировка, командировка+тюмень, для командировки, посуточно или отель, аренда посуточно, снять посуточно в тюмени, квартиры посуточно тюмень

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5534 | RU compare 12553 | secondary «снять квартиру посуточно в тюмени» 1749 | hook-local «командировка квартира» 41 Tyumen / 4188 RU (angle only, not P0 spine)

angle_rotation: checked last N=3 | burn-at-door skip: no | reason: hook sept_business_trip = командировка/рабочее место/Wi‑Fi/закрывающие до оплаты; не семья burn-at-door (B01 уже закрыла код/дверь); новый угол — созвон 10:00 vs заселение 22:00, не ранний заезд (skip_used: early_checkin)

queue_slot: 2026-08-29 — 2026-08-31 | queue_num: 2 | hook_id: sept_business_trip

season_note: Лето 2026, обложка без зимнего снега/сугробов.

cover_season_note: Лето 2026, обложка без зимнего снега/сугробов.

wp_category_hint: posutochnaya-arenda

wp_category_slugs: posutochnaya-arenda

interlink_siblings:
- B01: https://добрыйдом-72.рф/blog/beskontaktnoe-zaselenie-posutochno-tyumen/
- B02: https://добрыйдом-72.рф/blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/
- B03: /blog/kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki/
