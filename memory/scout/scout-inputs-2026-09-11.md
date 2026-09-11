# Задание Scout-handoff (Derouter utility)

Ты — Scout Derouter. Все Wordstat-данные уже собраны дирижёром через MCP-KV.
**Не** проверяй окружение и **не** пиши BLOCKER. Сформируй handoff по skill.

## Date
2026-09-11, пятница, сентябрь, Asia/Yekaterinburg. Обложка — осень, не зима.

## Angle rotation (last N=3)
- B15: wifi/рабочий стол
- B14: соседи/музыка ночью  
- B13: код/пустая ключница
burn-at-door skip: YES

## Anti-dup
Не дублировать: код-заселение, залог-скол, кухня→кафе B07, предоплата-тихина B08, собака, отель-дороже, уборка-списали, без-залога-у-двери, горячая-вода (всё уже в published/WP).

## Klyshin hook
hook_id: cancel_prepay
original: «Поездку сорвали. Предоплату обещали вернуть — сроки плывут»
angle: отмена поездки, возврат предоплаты, «вернём после проверки» — НЕ тишина до заезда (B08)
signal: https://t.me/klyshin_A

## Wordstat (live MCP-KV, уже проверено)
wordstat_preflight: mcp-kv wordstat_get_user_info OK
rework: «отмена брони посуточно» 85 → «отмена брони авито посуточно» 41 → «предоплата посуточно» 913 → «вернуть предоплату за квартиру посуточно» 46
final P0: «квартиры посуточно тюмень» 4929 (55+11176) | 10527 (225)

## Dzen
dzen_pattern: 2
dzen_shape_hint: кейс с суммами и датами — отмена рейса, предоплата, сроки возврата

## Topic
topic_id: B16
title_draft: «Отменили рейс. Предоплату 4 200 обещали вернуть за три дня — тишина в чате»

## Signal URLs
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://www.avito.ru/brands/dobriydomtymen/

Напиши полный `.cursor/excalibur-blog-handoff.md` со всеми обязательными полями из skill.
