# Scout inputs — B04 (2026-08-25 Asia/Yekaterinburg)

## Preflight
wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-08-25)

## Tenant
Добрый дом — посуточная аренда / субаренда Тюмень. Голос: от лица компании, клышинская подача, комфорт+, не адвокат.

## Anti-dup (published / recent WP — НЕ повторять)
- B01: бесконтактное заселение / коды
- B02: залог / скол на плите
- 2026-08-24: соседи ночью, скрытые доплаты, собака, паспорт, договор, отмена, предоплата/вечеринки, ранний заезд, субаренда

## Klyshin hook (bank)
id: utilities_counters
original: «показания счётчиков — не переплатить ЖКХ»
angle: как фиксировать при посуточной/субаренде; сезонный pivot → горячая вода / ГВС при заезде
signal: https://t.me/klyshin_A (angle bank utilities_counters)

## Wordstat live (MCP-KV)
probe A «показания счетчиков аренда квартиры» → 76 RF / 2 Tyumen — слабый buyer cluster
probe B «нет горячей воды в квартире» → 2494 RF / 22 Tyumen
  - «нет горячей воды в квартире что делать» → 215 RF
  - «в съемной квартире нет горячей воды» → 16 RF
  - «нет горячей воды в квартире куда звонить» → 202 RF
probe C «штраф за курение в квартире» → 210 RF — отложить (другой pain)
compare RU 225 vs Tyumen 55+11176

wordstat_rework: utilities_counters weak → pivot same risk (ЖКХ/коммуналка в съёмной) → final P0 «нет горячей воды в квартире» 2494 RF (Tyumen 22)

## Season (YEKT August 2025)
Late summer — возможны плановые отключения ГВС, не зимний герой. Обложка: лето/ванная/кран, без снега.

## Dzen pattern
3 — страх → инструкция в §1
dzen_shape_hint: «Сняли посуточно — горячей воды нет. Что спросить до оплаты и куда звонить»

## Proposed
topic_id: B04
slug: net-goryachej-vody-posutochno-chto-delat
title_draft: Заселились посуточно — горячей воды нет. Что спросить до оплаты
primary_query: нет горячей воды в квартире
signal_urls:
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72
