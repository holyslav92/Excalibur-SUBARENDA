# Scout handoff — B24

**topic_id:** B24  
**slug:** vyezd-v-polden-v-11-45-poprosili-900-za-lishnij-chas  
**date_yekt:** 2026-09-15

## Klyshin hook (original)
«Выезд в 12:00. Поезд в 16:30.» — семейство checkout_train_bags; **новый угол:** уборщица в 11:45 при checkout 12:00 → 900 ₽/час «задержки».

## Wordstat rework log
1. probe «поздний выезд аренда» → empty  
2. «поздний выезд» → **11935** (RU 225)  
3. «ранний заезд и поздний выезд» → 386 (225)  
4. «аренда квартиры посуточно» → **623** (55+11176)  
5. final P0 **«квартиры посуточно тюмень»** → **4724** (55+11176) / **10016** (225)

## Title draft (two-beat)
«Выезд в полдень. В 11:45 попросили 900 ₽ — «каждый лишний час»»

## Angle
Guest still inside paid checkout window; host bills "extra hour" when cleaning arrives early. NOT B06 bags, NOT B21 early check-in, NOT B23 sheet fee.

## signal_urls
- scout-inputs.md wordstat live MCP-KV 2026-09-15
- research-serp.json

## dzen_pattern
2 (case_with_sums_and_dates)
