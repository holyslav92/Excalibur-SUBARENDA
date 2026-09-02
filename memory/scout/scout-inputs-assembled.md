# Scout assembled inputs — 2026-09-02 YEKT

## CRITICAL INSTRUCTION FOR DEROUTER SCOUT
Wordstat MCP-KV preflight and ALL probes were already executed by the orchestrator via live MCP-KV.
wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API, Folder b1g6bq34gkivjj20be06)
DO NOT refuse handoff. DO NOT claim CallMcpTool unavailable.
Your job: write the complete `.cursor/excalibur-blog-handoff.md` using ONLY the verified data below.

## Tenant
- Brand: Добрый дом (посуточная / субаренда, Тюмень)
- Format: guest-night CASE (1100–1800 слов), NOT guide, NOT «N советов»
- Voice: Klyshin rhythm (case hook, two-beat title), reader inside as guest
- Cover season: начало сентября, летний свет (не зима героем)
- dzen_rf_pack: true

## Slot context
- topic_id: B07
- queue_num: 3, hook_id: kitchen_vs_hotel_cafes
- window YEKT: 2026-09-08 — 2026-09-10 (early slot 2026-09-02; prior queue #5 reviews done B05)
- B06 checkout/luggage published 2026-09-01 — do NOT duplicate checkout/baggage angle
- Site recent WP (not in B ledger): parking 800₽, hot water, dog fee, passport, wifi, prepayment — NOT these angles
- BAN: юр-крючки (ЕГРН, суд, наследники), burn-at-door/code family, early_checkin, hidden_fees duplicate wording

## Angle rotation (last N=3)
- B04: «Оплатили за двоих. У двери попросили доплату за третьего» — extra guest at door
- B05: «Рейтинг 4,8 — и два одинаковых «всё супер»» — reviews
- B06: «Выезд в полдень. Поезд через 4 часа — чемоданы у подъезда» — checkout/luggage gap

angle_rotation: checked last N=3 | burn-at-door skip: no (B07 is kitchen/eating cost contrast, not code/door) | reason: last 3 are extra-guest/reviews/luggage; B07 = кухня «есть» vs реальные траты в кафе каждый день; NOT hidden_fees-at-door duplicate

## Published anti-dup (do not repeat)
B01 contactless code wrong door | B02 deposit chip on stove | B03 vuz walk | B04 third guest fee | B05 fake reviews | B06 checkout bags on stairs

## Klyshin hook
klyshin_hook: kitchen_vs_hotel_cafes | original: «Три ночи. Кухня «есть» — или каждый день кафе?» | angle: контраст+цифра — обещанная кухня vs фактические 2 400–3 600 ₽/сутки на еду вне дома; NOT «скрытые доплаты у двери» duplicate | lockpick: «Что именно на кухне: сковорода, масло, соль, кружки?» | signal: https://t.me/klyshin_A (live 2026-08 — ритм «цифра = цена ожога»; map to moral: сначала список кухни/посуды, потом бронь)

## Wordstat rework (LIVE MCP-KV — copy verbatim)
wordstat_rework: probe «посуточно или отель» 433 (225) / cluster «отель или посуточная квартира» 312 → probe «квартира с кухней посуточно» 89 (225) → probe «аренда квартиры посуточно» 756 (55+11176) → probe «квартира посуточно тюмень» → final P0 «квартиры посуточно тюмень» 5446 (55+11176) / 12048 (225) | clusters tried: посуточно или отель, квартира с кухней посуточно, аренда посуточно, квартиры посуточно тюмень

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5446 | RU compare 12048 | secondary «посуточно или отель» 433 / «квартира с кухней посуточно» 89 | angle spine «отель или посуточная квартира» 312 (contrast case localizes to kitchen promise vs cafe spend)

## topic_id
B07

## short title for research_start (Klyshin rhythm, NOT final H1)
Кухня «есть» — три ночи в кафе каждый день

## title_draft hint (two-beat stop-factor, CASE not guide)
Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽

## slug hint
kuhnya-est-tri-nochi-v-kafe-kazhdyy-den

## dzen_pattern
4 — контраст с ответом в лиде (кухня vs кафе/отель; цифра ожога)
dzen_shape_hint: «Кухня в объявлении — а готовить не на чём: сколько съела поход в кафе за три ночи»

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://dzen.ru/holyslav

## external_signal
Klyshin live Aug 2026: number = price of burn; guest CASE: kitchen checkbox vs empty drawers. Wordstat contrast cluster «отель или посуточная квартира» 312; P0 spine квартиры посуточно тюмень 5446.

## wp_category_slugs
posutochnaya-arenda, sovety-gostyam

## interlink_siblings (published)
- B03 /blog/kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki/ (family trip)
- B04 /blog/oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego/ (money surprise)
- B05 /blog/rejting-4-8-u-kvartiry-posutochno-dva-otzyva-odno-i-to-zhe-vse-super/ (trust)

## queue_slot
2026-09-08 — 2026-09-10 (queue #3 kitchen_vs_hotel_cafes; early run 2026-09-02)

## cover_season_note
YEKT 2026-09-02 early September, summer light; kitchen/cafe scene; no winter hero

## Required handoff format
Write markdown starting with `# Scout handoff B07`. Include: wordstat_preflight, klyshin_hook, wordstat_rework, wordstat, angle_rotation, dzen_pattern, dzen_shape_hint, topic_id, short_title, title_draft, slug, signal_urls, external_signal, queue_slot, cover_season_note, wp_category_slugs, interlink_siblings, format_note (guest-night CASE not guide).
