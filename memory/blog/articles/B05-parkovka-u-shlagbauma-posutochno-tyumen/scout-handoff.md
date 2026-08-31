# Scout handoff — B05 parking_before_booking

- **topic_id:** B05
- **hook_id:** parking_before_booking (Klyshin queue slot 4, YEKT 2026-08-29 — 2026-09-07)
- **original Klyshin hook:** «Парковка рядом» — шлагбаум не пускает
- **angle:** место, пропуск, номер авто — до брони, не у барьера
- **klyshin_signal:** lockpick: «Где именно место и как въезд?»

## Wordstat (MCP-KV live 2026-08-31)

| phrase | volume | region |
|--------|--------|--------|
| аренда квартиры посуточно тюмень | 394 | 225 |
| квартиры в тюмени посуточно с парковкой | 7 | 225 |
| парковка квартира посуточно (cluster) | 420 | 225 |

**rework_log:** probe «парковка аренда квартиры» weak Tyumen slice → localize «квартиры посуточно тюмень с парковкой» 7 + parent «аренда квартиры посуточно тюмень» 394 → final P0 spine under H1.

**final P0:** `аренда квартиры посуточно тюмень` (394 RU) + pain cluster `посуточно с парковкой` (7 Tyumen)

## Anti-dup

Skip: lapoy, passport photo, uni-parents B03, B04 extra guest, B01 code, B02 deposit, hot water, wifi/10:00, contract bans, towels, reviews, checkout train.

## Proposed H1 shape (Title agent refines)

«Парковка бесплатно». У шлагбаума попросили 800 ₽

## Slug target

`parking-besplatno-shlagbaum-poprosili-800-rub`

## dzen_pattern_prefer

3 (страх → сцена), 2 (кейс с суммами)
