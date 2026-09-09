# Scout inputs B15 — 2026-09-09 YEKT slot 17:00

## Date context
- today: 2026-09-09, среда, сентябрь, Asia/Yekaterinburg
- season: early autumn Tyumen — no winter/snow hero on cover

## Published anti-dup (last 5 + today WP)
- B12 тихий центр/кран, B13 код/ключница, B14 тихий дом/соседи
- WP 2026-09-09: без залога у двери 5000, горячая вода/бойлер, отмена брони 2500
- WP 2026-09-08: собака доплата, wifi/созвон
- SKIP: код/ключница, залог-скол (B02), без залога, бойлер, собака, соседи, отмена, wifi

## Angle rotation
- last_n=3: deposit-at-door, boiler, cancellation — NOT burn-at-door codes
- pick: hidden fee AFTER checkout (cleaning charge) — fresh guest pain

## Klyshin hook (mechanics only, NOT legal/Moscow)
- hook_id: exit_cleaning_charge (new guest pain)
- original: «Убрали за собой — утром списали за уборку»
- angle: гость сдал ключи, квартира чистая; на следующий день холд/списание «финальная уборка» без предупреждения
- klyshin_signal: dialogue quote → «Нет. Так не заселяем.» → moral: сначала фото/акт выезда, потом ключ; lockpick: «Уборка входит в цену или отдельно?»

## Wordstat live MCP-KV (director pulled 2026-09-09)
wordstat_preflight: mcp-kv wordstat_get_user_info OK
- probe «уборка квартира посуточно» 1879 (225) / 14 (55+11176) — host-job bias
- probe «сколько стоит уборка посуточной квартиры» 69 (225)
- probe «уборка квартир посуточно цена» 29 (225)
- rework → «залог посуточно» related cluster weak for this angle
- final P0 «квартиры посуточно тюмень» 5059 (55+11176) | compare 10754 (225)

wordstat_rework: probe «уборка квартира посуточно» 1879 (225) host bias → «сколько стоит уборка посуточной квартиры» 69 → «уборка квартир посуточно цена» 29 → guest cluster «доплата за уборку» weak → final P0 «квартиры посуточно тюмень» 5059 (55+11176) | compare 10754 (225)

## Title draft (two-beat stop-factor)
title_draft: «Сдали ключи чисто. Утром списали 1 500 за уборку»
short_title: Сдали ключи чисто — списали за уборку
topic_id: B15
slug: sdali-klyuchi-chisto-utrom-spisali-za-uborku

## Dzen
dzen_pattern: 2 (case_with_sums_and_dates)
dzen_shape_hint: [нормально]. А потом [ужас/цифра] — NOT how-to, NOT «разберём»

## Interlink siblings (published, HTTP 200)
- /blog/perevel-zalog-za-posutochnuyu-na-vyeezde-skazali-ne-vernem/ (залог)
- /blog/hozyain-skazal-vse-vklyucheno-v-taksi-doplatili-2-400/ (скрытые доплаты)
- /blog/v-obyavlenii-vse-dlya-gostej-v-vannoj-odin-mokryj-kovrik/ (ожидания vs реальность)
- /blog/pereveli-3-000-predoplatoj-k-21-00-tishina-v-chate/ (предоплата)

wp_category_slugs: posutochnaya-arenda, sovety-gostyam
queue_slot: 2026-09-08 — 2026-09-10 batch slot 3 (fresh angle after saturated hooks)
season_note: сентябрь Тюмень, уютный интерьер, без зимнего снега на обложке
signal_urls: https://t.me/klyshin_A, https://добрыйдом-72.рф/blog/
external_signal: guest checkout cleaning fee dispute — daily rental Tyumen
