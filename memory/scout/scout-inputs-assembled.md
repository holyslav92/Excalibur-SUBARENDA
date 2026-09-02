# Scout assembled inputs — 2026-09-02 YEKT

## CRITICAL INSTRUCTION FOR DEROUTER SCOUT
Wordstat MCP-KV preflight and ALL probes were already executed by the orchestrator via live MCP-KV.
wordstat_preflight: mcp-kv wordstat_get_user_info OK (Yandex Cloud API, Folder b1g6bq34gkivjj20be06)
DO NOT refuse handoff. DO NOT claim CallMcpTool unavailable.
Your job: write the complete `.cursor/excalibur-blog-handoff.md` using ONLY the verified data below.

## Tenant
- Brand: Добрый дом (посуточная / субаренда, Тюмень)
- Format: guest-night CASE (~1100–1800 слов), NOT guide, NOT «N советов»
- Voice: Klyshin rhythm (case hook, two-beat title), reader inside as guest
- Cover season: начало сентября / летний свет (не зима героем)
- dzen_rf_pack: true

## Slot context
- topic_id: B08
- queue_num: 7, hook_id: quiet_center_maps
- window YEKT: 2026-09-08 — 2026-09-10 (batch slot; today 2026-09-02 slot 12:00 YEKT)
- B07 kitchen/café published 2026-09-02 — do NOT duplicate kitchen angle
- Site today also covers: towels 4 guests, heater +500, parking 800, hot water, dog fee, passport, wifi — NOT these angles
- BAN: юр-крючки (ЕГРН, суд, наследники), burn-at-door/code family, early_checkin (used), towels/pack_vs_flat (live WP today)

## Angle rotation (last N=3)
- B05: «Рейтинг 4,8 — и два одинаковых «всё супер»» — reviews
- B06: «Выезд в 12:00. Поезд в 16:30» — checkout/luggage
- B07: «Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽» — kitchen/café

angle_rotation: checked last N=3 | burn-at-door skip: no (B08 is quiet/maps/construction, not code/door) | reason: last 3 are reviews/checkout/kitchen; B08 = «тихий центр» vs шум стройки за окном; NOT neighbors_night parked duplicate (construction/maps angle)

## Published anti-dup (do not repeat)
B01 contactless code wrong door | B02 deposit chip on stove | B03 vuz walk | B04 third guest fee | B05 fake reviews | B06 checkout train luggage | B07 kitchen café 7200

## Klyshin hook
klyshin_hook: quiet_center_maps | original: ««Тихий центр» — за окном стройка» | angle: 7 минут в Картах/панорамах — не слова хозяина; guest wakes to jackhammer after «quiet courtyard» promise | lockpick: «Что слышно из окна спальни на 7 утра? Есть панорама двора?» | signal: https://t.me/klyshin_A (ритм: цитата хоста → факт за окном → «Нет. Так не бронируем.»)

## Wordstat rework (LIVE MCP-KV — copy verbatim)
wordstat_rework: probe «аренда квартиры тюмень центр» 13 (55+11176) → weak local → probe «шум соседи» 183 (55 only; generic noise, not rental) → probe «квартира посуточно тюмень» cluster → final P0 «квартиры посуточно тюмень» 5363 (55+11176) / 11916 (225) | clusters tried: аренда квартиры тюмень центр, шум соседи, квартира посуточно тюмень, квартиры посуточно тюмень

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 5363 | RU compare 11916 | secondary «снять квартиру посуточно в тюмени» 1696 | angle spine quiet/maps localizes under посуточно Тюмень demand

## topic_id
B08

## short title for research_start (Klyshin rhythm, NOT final H1)
Тихий центр в объявлении — за окном стройка в семь утра

## title_draft hint (two-beat stop-factor, CASE not guide)
Написали «тихий двор». В 6:45 за окном — перфоратор

## slug hint
napisali-tihij-dvor-v-645-za-oknom-perforator

## dzen_pattern
5 — локальный + сезонный (район/двор, начало сентября, шум стройки)
dzen_shape_hint: «Обещали тишину в центре — а утром будильник не нужен: стройка под окном»

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://dzen.ru/holyslav

## external_signal
Klyshin live Aug–Sep 2026: «сначала проверка факта, потом перевод» → guest CASE: сначала панорама двора/окна в Картах, потом предоплата. Wordstat P0 spine квартиры посуточно тюмень 5363.

## wp_category_slugs
posutochnaya-arenda, sovety-gostyam

## interlink_siblings (published)
- B03 /blog/kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki/ (район/локация)
- B05 /blog/rejting-4-8-u-kvartiry-posutochno-dva-otzyva-odno-i-to-zhe-vse-super/ (доверие к объявлению)
- B06 /blog/vyezd-v-12-00-poezd-v-16-30-kuda-det-chemodany-mezhdu/ (комфорт ночи)
- B07 /blog/kvartira-posutochno-kuhnya-est-tri-nochi-v-kafe-kazhdyj-den/ (обещание vs факт)

## queue_slot
2026-09-08 — 2026-09-10 (queue #7 quiet_center_maps)

## cover_season_note
YEKT 2026-09-02 early September, summer light; no winter hero; construction noise = seasonal urban reality

## Required handoff format
Write markdown starting with `# Scout handoff B08`. Include: wordstat_preflight, klyshin_hook, wordstat_rework, wordstat, angle_rotation, dzen_pattern, dzen_shape_hint, topic_id, short_title, title_draft, slug, signal_urls, external_signal, queue_slot, cover_season_note, wp_category_slugs, interlink_siblings, format_note (guest-night CASE not guide).
