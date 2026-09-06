# Scout inputs — 2026-09-06 YEKT slot 09:00

## Date
2026-09-06 (Asia/Yekaterinburg, early September, NOT winter)

## Published anti-dup (last 10)
B01 код/заселение, B02 залог/скол, B03 вуз рядом, B04 третий гость, B05 отзывы, B06 выезд/багаж, B07 кухня/кафе, B08 предоплата тишина, B09 парковка, B10 всё включено/такси

## Angle rotation
Last 3: B08 predоплата, B09 parking, B10 hidden fees taxi — skip burn-at-door, skip hidden fees family

## Klyshin hook (queue_active #6 pack_vs_flat)
- hook_id: pack_vs_flat
- hook_ru: «Собрал чемодан — в квартире нет полотенец»
- angle: что везти vs что обязано быть в объявлении; number = price of burn (покупка полотенец/постель в 23:00)
- klyshin_signal: checklist AFTER moral; lockpick: «Сколько комплектов постельного и полотенец на гостя?»
- anti_dup: NOT kitchen (B07), NOT third guest (B04), NOT deposit (B02)

## Wordstat (live MCP-KV 2026-09-06)
| probe | region | volume |
|-------|--------|--------|
| квартиры посуточно тюмень | 55+11176 | 5235 |
| квартиры посуточно тюмень | 225 | 11220 |
| полотенца квартира посуточно | 225 | 109 |
| аренда квартиры посуточно | 225 | 42979 |
| что нужно для аренды квартиры | (rework) | probe next |

## Rework log
1. Original hook: pack_vs_flat / полотенца
2. Probe «полотенца квартира посуточно» → 109 (225) — weak but honest guest-intent
3. Rework «аренда квартиры посуточно» → 42979 (225) — demand spine
4. Final P0: «квартиры посуточно тюмень» 5235 (55+11176) / 11220 (225)

## Title draft (two-beat case)
«В объявлении — «всё для гостей». В ванной один мокрый коврик»

## Topic assignment
- topic_id: B11
- slug: v-obyavlenii-vse-dlya-gostej-v-vannoj-odin-mokryj-kovrik
- dzen_pattern: case_with_sums_and_dates (2)
