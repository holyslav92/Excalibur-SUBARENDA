# ЗАДАНИЕ DEROUTER SCOUT

Ты — Derouter utility tier (gpt-5.6-terra). Верни **полный** `.cursor/excalibur-blog-handoff.md` в ответе.
Скрипт `excalibur_blog_derouter_opus_chat.py` сам запишет файл. **Не** отвечай BLOCKER — MCP Wordstat уже проверен дирижёром, частоты ниже live.

---

# Scout inputs — 2026-09-22 10:00 YEKT (Добрый дом, B32)

См. полное задание в `memory/scout/scout-inputs-b32.md` — ниже ключевые поля для handoff.

topic_id: B32
hook_id: checkout_price_stack
title_draft: «В карточке 3 400 ₽ за ночь. На оплате — 8 816 ₽ за две»
slug_draft: v-kartochke-3400-za-noch-na-oplate-8816-za-dve

wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: checkout_price_stack | original: «В карточке 3 400 ₽ за ночь. Две ночи — 6 800 ₽. На оплате +12% сервиса и 1 200 ₽ уборка» | angle: строка «за ночь» vs итог на оплате; сравнение с отелем | signal: https://t.me/klyshin_A
wordstat_rework: probe «комиссия посуточно» 1903 (225) → «уборка посуточно» 1932 (225) → «посуточно или отель» 8 (55+11176) / «отель или посуточная квартира» 280 (225) → «квартира посуточно тюмень цена» 92 (225) → final P0 «квартиры посуточно тюмень» 4409 (55+11176) | 9372 (225) | clusters tried: комиссия, уборка, hotel contrast, цена, бронирование
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4409 (55+11176) | 9372 (225) | supporting «комиссия посуточно» 1903 (225) | contrast «отели тюмень» 7002 (55+11176)
angle_rotation: checked last N=3 | burn-at-door skip: yes | zalog-scol skip: yes | reason: B29–B31 другие углы; saturated families код/залог-скол не трогаем

dzen_pattern: 4
dzen_shape_hint: «За ночь квартира казалась дешевле отеля — пока не открыли шаг оплаты с +12% и уборкой»

signal_urls:
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/
