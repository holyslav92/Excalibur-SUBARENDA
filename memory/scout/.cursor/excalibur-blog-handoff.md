# Scout handoff B07

wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API, Folder b1g6bq34gkivjj20be06)

klyshin_hook: kitchen_vs_hotel_cafes | original: «Три ночи. Кухня «есть» — или каждый день кафе?» | angle: контраст+цифра — обещанная кухня vs фактические 2 400–3 600 ₽/сутки на еду вне дома; NOT «скрытые доплаты у двери» duplicate | lockpick: «Что именно на кухне: сковорода, масло, соль, кружки?» | signal: https://t.me/klyshin_A

wordstat_rework: probe «посуточно или отель» 433 (225) / cluster «отель или посуточная квартира» 312 → probe «квартира с кухней посуточно» 89 (225) → probe «аренда квартиры посуточно» 756 (55+11176) → probe «квартира посуточно тюмень» → final P0 «квартиры посуточно тюмень» 5446 (55+11176) / 12048 (225) | clusters tried: посуточно или отель, квартира с кухней посуточно, аренда посуточно, квартиры посуточно тюмень

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5446 | RU compare 12048 | secondary «посуточно или отель» 433 / «квартира с кухней посуточно» 89 | angle spine «отель или посуточная квартира» 312 (contrast case localizes to kitchen promise vs cafe spend)

angle_rotation: checked last N=3 | burn-at-door skip: no | reason: last 3 are extra-guest/reviews/luggage; B07 = кухня «есть» vs реальные траты в кафе каждый день; NOT hidden_fees-at-door duplicate

dzen_pattern: 4 — контраст с ответом в лиде

dzen_shape_hint: «Кухня в объявлении — а готовить не на чём: сколько съела поход в кафе за три ночи»

topic_id: B07

short_title: Кухня «есть» — три ночи в кафе каждый день

title_draft: Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽

slug: kuhnya-est-tri-nochi-v-kafe-kazhdyy-den

signal_urls:
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://dzen.ru/holyslav

external_signal: Klyshin live Aug 2026: number = price of burn; guest CASE: kitchen checkbox vs empty drawers. Wordstat contrast cluster «отель или посуточная квартира» 312; P0 spine «квартиры посуточно тюмень» 5446.

queue_slot: 2026-09-08 — 2026-09-10 (queue #3 kitchen_vs_hotel_cafes; early run 2026-09-02)

cover_season_note: YEKT 2026-09-02, начало сентября, летний свет; kitchen/cafe scene; no winter hero

wp_category_slugs:
- posutochnaya-arenda
- sovety-gostyam

interlink_siblings:
- B03 /blog/kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki/ (family trip)
- B04 /blog/oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego/ (money surprise)
- B05 /blog/rejting-4-8-u-kvartiry-posutochno-dva-otzyva-odno-i-to-zhe-vse-super/ (trust)

format_note: guest-night CASE, 1100–1800 слов; NOT guide, NOT «N советов». Reader is inside as a guest. One case → one verdict; the kitchen list/checklist follows the moral. Demand spine: «квартиры посуточно тюмень». Supply and case localization: посуточная аренда/субаренда в Тюмени. Do not duplicate checkout/luggage, reviews, extra-guest, parking, hot-water, dog-fee, passport, Wi‑Fi, prepayment, early-check-in, hidden-fees-at-door, or burn-at-door/code angles.
