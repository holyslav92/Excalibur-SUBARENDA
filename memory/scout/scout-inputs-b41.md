# Scout inputs B41 — 2026-10-01 YEKT (conductor)

## ViralDzen handoff (PASS)
- hub: travel
- viral_source title only (angle, no copy): Ozon Travel support / cancel booking
- guest_angle_ru: посуточно Тюмень — правила заселения, залог, код, связь с хозяином при сбое
- tyumen_wound_hint: поздний приезд, страх остаться без кода/сети, спор о залоге

## Published anti-dup (last 12 + titles)
B30–B40: late checkout charge, chuzhie chemodany, price mismatch, avito double pay, deposit at door, wrong entrance PDF, dog fee, lift 8th, min 2 nights, no prepay filter lie.
B15: desk not wifi. B13/B18: code/keybox/domofon. B08: silence after prepay. B10: taxi hidden fee.
LIVE WP slugs do not reuse: komissii, minimum nights, manager at door, tishina drill, 4200/5050 price.

## Klyshin angle (mechanics only)
hook_id: wifi_call_burn | original: «Wi‑Fi для созвона обещали. К девятому утра — роутер мигает, чат молчит»
angle: карточка обещает интернет для работы; гость внутри квартиры без сети перед созвоном/отчётом
signal: https://t.me/klyshin_A

## Wordstat (MCP-KV live 2026-10-01)
| phrase | RU 225 | Tyumen 55+11176 |
| квартиры посуточно тюмень | 8838 | 3984 |
| залог посуточно | 2497 | (probe spine) |
| посуточно комиссия | 1833 | — |
| квартира посуточно wi fi | totalCount 17 | empty |
| квартиры посуточно ранний заезд | 239 | — |

Rework log: probe «квартира посуточно wi fi» weak volume → rework to spine «квартиры посуточно тюмень» + guest wound Wi‑Fi/созвон (buyer: командировка, связь с хозяином при сбое — из viral hint)

## Rotation
Not door-surcharge clone. Not filter-card lie (B40). Not code-at-wrong-door (B35/B18). Fresh: **интернет в карточке vs реальность + молчание в чате перед созвоном**.

## Draft
topic_id: B41
title_draft: «Wi‑Fi для созвона обещали. К девяти утра — «нет сети», 10 600 ₽ за две ночи»
primary_query: квартиры посуточно тюмень
slug_draft: posutochno-wifi-obeshchali-k-sozvonu-net-seti
wp_category_slugs: posutochno, zaselenie
dzen_pattern: 2
