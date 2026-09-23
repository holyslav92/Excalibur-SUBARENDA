# ЗАДАНИЕ DEROUTER SCOUT

Ты — Derouter utility tier (gpt-5.6-terra). Верни **полный** `.cursor/excalibur-blog-handoff.md` в ответе.
Скрипт `excalibur_blog_derouter_opus_chat.py` сам запишет файл. **Не** отвечай BLOCKER — MCP Wordstat уже проверен дирижёром, частоты ниже live.

---

# Scout inputs — 2026-09-23 17:00 YEKT (Добрый дом, B35)

topic_id: B35
hook_id: no_intermediary_manager_door
title_draft: ««От хозяев» в фильтре. У двери менеджер: ещё 2 000 ₽ на карту»
slug_draft: ot-hozyaev-v-filtre-u-dveri-menedzher-eshche-2000-na-kartu

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-09-23)
klyshin_hook: no_intermediary_manager_door | original Klyshin rhythm: «кажется прямой контакт → на пороге чужой посредник и доплата» | angle: фильтр «без посредников / от хозяев» vs человек с ключами и перевод на карту «за заселение» | signal: https://t.me/klyshin_A
wordstat_rework: probe «ночной заезд посуточно» totalCount 15 (225, weak) → «отмена брони посуточно» 63 (225) → «залог посуточно» 2592 (225) saturated B34 → «квартиры посуточно без посредников» 43518 (225) + «квартира без посредников от хозяев посуточно» 14485 (225) → Tyumen spine «квартиры посуточно тюмень» 4304 (55+11176) + «квартиры посуточно тюмень без посредников» 237 (55+11176) | clusters: посредник, от хозяев, заселение, доплата на месте (NOT legal/EGRN)
wordstat: mcp_kv live | regions 55,11176,compare225 | final P0 «квартиры посуточно без посредников» 43518 (225) | Tyumen «квартиры посуточно тюмень» 4304 (55+11176) | supporting «посредник квартир посуточно» 43591 (225)
angle_rotation: last N=3 B32 price stack, B33 avito double pay, B34 zalog at door — skip burn-at-door код/ключница; skip zalog-scol; NEW angle intermediary-at-door distinct from B34 zalog filter lie
dzen_pattern: 4
dzen_shape_hint: «Выбрали «от хозяев» — а у двери не хозяин, а менеджер с QR и суммой, которой не было в брони»

signal_urls:
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/

guest_pain_lockpick: «Кто заселяет — хозяин или агент? И что входит в цену на сайте?»
supply: Тюмень, «Добрый дом», посуточная аренда комфорт+
