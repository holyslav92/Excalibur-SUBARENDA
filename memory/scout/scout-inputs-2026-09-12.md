# Задание Scout-handoff (Derouter utility) — B17

Ты — Scout Derouter. Все Wordstat-данные уже собраны дирижёром через MCP-KV.
**Не** проверяй окружение и **не** пиши BLOCKER. Сформируй handoff по skill.

## Date
2026-09-12, суббота, сентябрь, Asia/Yekaterinburg. Обложка — осень, не зима.

## Angle rotation (last N=3)
- B16: отмена рейса / возврат предоплаты
- B15: wifi / рабочий стол
- B14: соседи / музыка ночью
burn-at-door skip: YES (код/ключница saturated)
skip families (klyshin bank): hot water, neighbors, extra fees, dog, passport — do NOT use

## Anti-dup (published B01–B16)
НЕ дублировать: код/заселение, залог-скол плита, рядом с вузом, третий гость, отзывы, выезд-чемоданы, кухня-кафе, предоплата-тихина, парковка-шлагбаум, всё-включено-такси (B10), полотенца, тихий-центр-кран/горячая вода, пустая ключница, соседи-музыка, wifi-стол, отмена рейса-предоплата.

## Klyshin hook (parked → activate)
hook_id: utilities_jkh
original: «Три ночи. В объявлении — «коммуналка включена». На выезде — фото счётчиков и доплата 1 840 ₽»
angle: ЖКХ/коммуналка при посуточной — что входит в цену, показания счётчиков и доплата на выезде; NOT «всё включено»+такси (B10), NOT горячая вода/кран (B12), NOT generic hidden-fees list
klyshin_signal: reader inside; moral: сначала список «что включено» (свет/вода/интернет), потом ключ; lockpick: «Коммуналка в цене или по счётчикам?»
signal: https://t.me/klyshin_A

## Wordstat (live MCP-KV, уже проверено)
wordstat_preflight: mcp-kv wordstat_get_user_info OK
rework log:
- probe «жкх посуточно» API empty
- probe «коммуналка посуточно» API empty
- probe «коммунальные посуточно» API empty
- probe «коммунальные аренда квартиры» 24 (55+11176) — long-term bias
- probe «показания счетчиков аренда» 1
- probe «уборка посуточно» 15 — host/cleaning bias
- probe «залог посуточно» 30
- probe «аренда квартиры посуточно» 679 → «аренда квартиры тюмень посуточно» 164
- probe «снять квартиру посуточно в тюмени» 1498
- final P0 «квартиры посуточно тюмень» 4840 (55+11176) | 10385 (225)

## Dzen
dzen_pattern: 2 (NOT pattern 1)
dzen_shape_hint: «Кейс с суммами: три ночи, «коммуналка включена», на выезде счёт 1 840 ₽ по счётчикам»

## Topic
topic_id: B17
title_draft: «Написали «коммуналка включена». На выезде прислали счётчики — 1 840 ₽»
case_type: ONE case (не гайд, не список советов)

## Signal URLs (≥2 besides klyshin)
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://dzen.ru/a/ag2HOFU4_3gzR7YP (Дзен «Добрый дом» — паттерн кейса для командировочных)

Напиши полный `.cursor/excalibur-blog-handoff.md` со всеми обязательными полями из skill: topic_id, title_draft, dzen_pattern, dzen_shape_hint, klyshin_hook, wordstat_preflight, wordstat_rework, wordstat, angle_rotation, signal_urls, external_signal, opening_direction, moral, lockpick_question, anti_dup_guard, bank_update.
