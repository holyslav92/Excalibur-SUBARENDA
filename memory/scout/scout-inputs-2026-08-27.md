# Scout inputs — 2026-08-27 YEKT slot

## Date / tenant
- run_date: 2026-08-27 (Asia/Yekaterinburg, summer)
- tenant: Добрый дом, посуточная аренда Тюмень
- voice: от лица ПК (управляющая компания), клышинская подача

## Angle rotation (last N=3 published)
1. na-kartochke-posutochno-4-8 — отзывы/рейтинг
2. vyezd-v-12-00-poezd-v-16-30 — выезд/багаж
3. parkovka-u-shlagbauma-posutochno — парковка

burn-at-door skip: yes (B01 codes — saturated)
parents_sept_uni skip: yes (published 2026-08-25)
sept_business_trip skip: yes (published 2026-08-25)
reviews_not_rating skip: yes (published 2026-08-27)
parking_before_booking skip: yes (published 2026-08-26)
checkout_train_bags skip: yes (published 2026-08-26)

## Selected hook (queue #3 kitchen_vs_hotel_cafes)
- hook_id: kitchen_vs_hotel_cafes
- original Klyshin: «Три ночи. Кухня «есть» — или каждый день кафе?»
- angle: контраст+цифра кухня vs отель+кафе; NOT hidden_fees
- lockpick: «Кухня есть — это плита и сковородка или только микроволновка?»
- dzen_pattern: 4 (контраст с ответом в лиде)
- dzen_shape_hint: «Три ночи с кухней vs отель — где дешевле на завтраках»

## Wordstat preflight
wordstat_preflight: mcp-kv wordstat_get_user_info OK

## Wordstat rework log
probe «посуточно или отель» RU 444 / Tyumen 6 → weak local
probe «отель или посуточная квартира» RU 305 → contrast spine OK
probe «квартира с кухней посуточно» RU 65 / Tyumen 3 → weak
probe «аренда квартиры посуточно» RU 47060 → strong national
probe «аренда квартир посуточно тюмень» Tyumen 224 → local spine
probe «квартиры посуточно тюмень» Tyumen 5583 → **final P0 local**

final P0: «квартиры посуточно тюмень» 5583 (regions 55+11176)
compare RU: «аренда квартиры посуточно» 47060 (region 225)
contrast spine: «отель или посуточная квартира» 305 (region 225)

## Anti-dup
NOT duplicate: коды/заселение, залог/скол на плите, hidden fees, parking, reviews, checkout bags, parents uni, business trip wifi

## External signal
- https://t.me/klyshin_A (angle bank)
- https://добрыйдом-72.рф/blog/ (site blog)

## Title draft (Klyshin rhythm, NOT final H1)
«Три ночи. В объявлении — кухня. На месте — чайник и две кружки»

## topic_id suggestion
B03
