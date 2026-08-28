# Scout inputs — B03 (2026-08-28 Asia/Yekaterinburg)

Tenant: Добрый дом — посуточная аренда Тюмень, comfort+, PK company voice
Date: 2026-08-28, slot 14:00 YEKT, late summer (NO winter hero on cover)

## Wordstat preflight
wordstat_get_user_info OK (2026-08-28)

## Angle rotation (last N=3 live WP)
1. Собрал чемodan — нет полотенец (pack_vs_flat) — 2026-08-28
2. «Тихий центр» — стройка за окном — 2026-08-27
3. «Кухня есть» — каждый день кафе — 2026-08-27
burn-at-door skip: yes (B01 published; saturated family)

## Anti-dup HARD (user + ledger)
- B01: код/бесконтактное заселение — SKIP
- B02: залог/скол на плите — SKIP
- Live: pack_vs_flat, kitchen_vs_hotel_cafes, reviews, parking, checkout_train, parents_sept_uni, center_maps — SKIP same angles

## Klyshin hook (parked → active)
hook_id: hotel_vs_daily
original: «Две ночи в командировке. Отель 6800 или квартира 4200 — что выбрать?»
angle: контраст с цифрами; не «гайд», а сцена выбора до оплаты; supply Тюмень
klyshin_signal: reader inside taxi/chat; lockpick: «А завтрак и парковка входят?»
signal: https://t.me/klyshin_A

## Wordstat rework log (MCP-KV live)
probe «посуточно или отель» RU225 → 445 total
  → «отель или посуточная квартира» 310
  → «что лучше отель или квартира посуточно» 16
probe «квартира посуточно тюмень» RU55 → 3822 (supply spine)
probe «хостел тюмень» RU55 → 1133 (contrast anchor, not hero)
final P0: «отель или посуточная квартира» 310 RU + supply «квартира посуточно тюмень» 3822 Tyumen

## dzen_pattern
pattern: 4 (контраст с ответом в лиде)
shape_hint: «Отель 6800 или квартира 4200 на две ночи — где съэкономите и где потеряете»

## topic assignment
topic_id: B03
slug draft: otel-ili-kvartira-posutochno-dve-nochi
title_draft: Две ночи. Отель 6800 или квартира 4200 — где съедите лишнее

## CTA canon
TG after checklist: https://t.me/Dobriy_dom_72
MAX after «у нас так»: https://max.ru/id660300569233_biz or https://t.me/Dobriy_dom_Tyumen
phone: +7 993 574-83-22
booking: https://добрыйдом-72.рф/

## Interlink siblings (published)
B01 /blog/beskontaktnoe-zaselenie-posutochno-tyumen/
B02 /blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/

Write handoff to .cursor/excalibur-blog-handoff.md with all required lines.
