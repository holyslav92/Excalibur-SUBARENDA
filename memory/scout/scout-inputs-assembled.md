# Scout assembled inputs — 2026-09-01 YEKT

## CRITICAL INSTRUCTION FOR DEROUTER SCOUT
Wordstat MCP-KV preflight and ALL probes were already executed by the orchestrator via live MCP-KV.
wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API, Folder b1g6bq34gkivjj20be06)
DO NOT refuse handoff. DO NOT claim CallMcpTool unavailable.
Your job: write the complete `.cursor/excalibur-blog-handoff.md` using ONLY the verified data below.

## Tenant
- Brand: Добрый дом (посуточная / субаренда, Тюмень)
- Format: guest-night CASE (~1100–1800 слов), NOT guide, NOT «N советов»
- Voice: Klyshin rhythm (case hook, two-beat title), reader inside as guest
- Cover season: лето/начало сентября (не зима героем)
- dzen_rf_pack: true

## Slot context
- topic_id: B06
- queue_num: 8, hook_id: checkout_train_bags
- window YEKT: 2026-09-08 — 2026-09-10 (batch slot; today 2026-09-01 user assigned B06)
- B05 reviews published today 2026-09-01 — do NOT duplicate reviews angle
- Site today also covers: parking 800₽, hot water, dog fee, passport, wifi, prepayment — NOT these angles
- BAN: юр-крючки (ЕГРН, суд, наследники), burn-at-door if saturated, early_checkin (used)

## Angle rotation (last N=3)
- B03: «Привезли сына к вузу — «рядом» оказалось 40 минут пешком» — parents/uni
- B04: «Оплатили за двоих. У двери попросили доплату за третьего» — extra guest at door
- B05: «Рейтинг 4,8 — и два одинаковых «всё супер»» — reviews (published 2026-09-01)

angle_rotation: checked last N=3 | burn-at-door skip: no (B06 is checkout/luggage gap, not code/door family) | reason: last 3 are uni/extra-guest/reviews; B06 = выезд 12:00 + поезд днём, куда чемоданы; NOT early_checkin

## Published anti-dup (do not repeat)
B01 contactless code wrong door | B02 deposit chip on stove | B03 vuz walk | B04 third guest fee | B05 fake reviews

## Klyshin hook
klyshin_hook: checkout_train_bags | original: «Выезд в 12:00. Поезд в 16:30.» | angle: куда деть чемоданы между выездом и транспортом; NOT early check-in (banned used) | lockpick: «Можно оставить багаж до вокзала?» / «Есть камера хранения у вас?» | signal: https://t.me/klyshin_A (live 2026-08-31 — ритм «сначала порядок действий, потом ключ/деньги»; map to moral: сначала багаж/хранение, потом сдача ключей)

## Wordstat rework (LIVE MCP-KV — copy verbatim)
wordstat_rework: probe «поздний выезд аренда» API empty → probe «выезд посуточно» API empty → probe «поздний выезд» 142 (55+11176, hotel-skew) → probe «хранение багажа» 133 (55+11176) / 12186 (225) → probe «хранение багажа тюмень» 28 (55+11176) → probe «камера хранения багажа тюмень» 18 (55+11176, from cluster) → probe «аренда квартиры посуточно» 756 (55+11176) → probe «квартира посуточно тюмень» → final P0 «квартиры посуточно тюмень» 5446 (55+11176) / 12048 (225) | clusters tried: поздний выезд, выезд посуточно, хранение багажа, хранение багажа тюмень, аренда посуточно, квартиры посуточно тюмень

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5446 | RU compare 12048 | secondary «хранение багажа» 133 / «хранение багажа тюмень» 28 | angle spine «поздний выезд» 142 (hotel context — case localizes to apartment checkout gap)

## topic_id
B06

## short title for research_start (Klyshin rhythm, NOT final H1)
Выезд в 12:00, поезд в 16:30 — куда деть чемоданы между

## title_draft hint (two-beat stop-factor, CASE not guide)
Выезд в 12:00. Поезд в 16:30 — чемоданы остались на лестнице у подъезда

## slug hint
vyezd-v-12-poezd-v-16-30-kuda-det-chemodany

## dzen_pattern
2 — живой кейс с суммами/датами (12:00 / 16:30 / 4,5 часа окно)
dzen_shape_hint: «Выезд в полдень, поезд вечером: куда деть чемоданы до вокзала»

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://dzen.ru/holyslav

## external_signal
Klyshin live Aug 2026: «сначала порядок действий, потом подпись/ключ» → guest CASE: сначала договориться про багаж/хранение, потом сдача ключей. Wordstat: хранение багажа тюмень 28; P0 spine квартиры посуточно тюмень 5446.

## wp_category_slugs
posutochnaya-arenda, sovety-gostyam

## interlink_siblings (published)
- B02 /blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/ (выезд family)
- B04 /blog/oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego/
- B05 /blog/rejting-4-8-u-kvartiry-posutochno-dva-otzyva-odno-i-to-zhe-vse-super/

## queue_slot
2026-09-08 — 2026-09-10 (queue #8 checkout_train_bags)

## cover_season_note
YEKT 2026-09-01 early September, summer light; no winter hero

## Required handoff format
Write markdown starting with `# Scout handoff B06`. Include: wordstat_preflight, klyshin_hook, wordstat_rework, wordstat, angle_rotation, dzen_pattern, dzen_shape_hint, topic_id, short_title, title_draft, slug, signal_urls, external_signal, queue_slot, cover_season_note, wp_category_slugs, interlink_siblings, format_note (guest-night CASE not guide).
