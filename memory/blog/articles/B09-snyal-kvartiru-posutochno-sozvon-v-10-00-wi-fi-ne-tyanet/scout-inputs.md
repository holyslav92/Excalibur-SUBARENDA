# Scout inputs — B09

**Date:** 2026-09-03 (YEKT, early autumn, NOT winter)

## Published titles (anti-dup)
B01 codes, B02 deposit/scratch, B03 university distance, B04 extra guest fee, B05 fake reviews, B06 checkout bags, B07 kitchen vs cafe, B08 prepayment silence.

## Klyshin hook
- **hook_id:** `sept_business_trip`
- **original:** Звонок в 10:00. Заселился в 22:00. Стол, розетки, Wi‑Fi на созвон, закрывающие — до оплаты.
- **angle:** Guest on business trip; Wi‑Fi speed fails morning video call; host promised "есть интернет".

## Wordstat (MCP-KV live, 2026-09-03)
| phrase | region | volume |
|--------|--------|--------|
| квартиры посуточно тюмень | 55+11176 | 5320 |
| снять квартиру посуточно в тюмени | 55 | 1134 |
| квартира посуточно командировка | 225 | 69 |
| уборка посуточных квартир | 225 | 1951 |

**final P0:** квартиры посуточно тюмень — 5320 (demand spine)
**guest sub-cluster:** Wi‑Fi / интернет для созвона при посуточной аренде

## Rework log
1. Hook sept_business_trip → weak "командировка" alone (69 RU) → localized Tyumen spine 5320 + Wi‑Fi pain angle
2. Skip burn-at-door (saturated B01/B08), skip kitchen (B07), skip prepayment (B08)

## Title draft (two-beat)
Снял квартиру посуточно. Созвон в 10:00 — Wi‑Fi не тянет

## Tenant
Добрый дом, Tyumen short-term rental, dzen_rf_pack.
