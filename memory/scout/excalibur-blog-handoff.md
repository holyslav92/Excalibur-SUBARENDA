# Scout handoff B03

wordstat_preflight: mcp-kv wordstat_get_user_info OK  
klyshin_hook: hook_id exit_cleaning_charge; original «Убрали за собой — утром списали за уборку»; angle: гость сдал ключи, квартира чистая; на следующий день холд/списание «финальная уборка» без предупреждения; klyshin_signal: dialogue quote → «Нет. Так не заселяем.» → moral: сначала фото/акт выезда, потом ключ; lockpick: «Уборка входит в цену или отдельно?»  
wordstat_rework: probe «уборка квартира посуточно» 1879 (225) host bias → «сколько стоит уборка посуточной квартиры» 69 → «уборка квартир посуточно цена» 29 → guest cluster «доплата за уборку» weak → final P0 «квартиры посуточно тюмень» 5059 (55+11176) | compare 10754 (225)  
wordstat: P0 «квартиры посуточно тюмень» 5059 (55+11176) | compare 10754 (225)  
angle_rotation: last_n=3: deposit-at-door, boiler, cancellation — NOT burn-at-door codes; pick: hidden fee AFTER checkout (cleaning charge) — fresh guest pain  
dzen_pattern: 2 (case_with_sums_and_dates)  
dzen_shape_hint: [нормально]. А потом [ужас/цифра] — NOT how-to, NOT «разберём»  
topic_id: B15  
short_title: Сдали ключи чисто — списали за уборку  
title_draft: «Сдали ключи чисто. Утром списали 1 500 за уборку»  
slug: sdali-klyuchi-chisto-utrom-spisali-za-uborku  
signal_urls: https://t.me/klyshin_A, https://добрыйдом-72.рф/blog/  
external_signal: guest checkout cleaning fee dispute — daily rental Tyumen  
queue_slot: 2026-09-08 — 2026-09-10 batch slot 3 (fresh angle after saturated hooks)  
season_note: сентябрь Тюмень, уютный интерьер, без зимнего снега на обложке  
interlink_siblings: /blog/perevel-zalog-za-posutochnuyu-na-vyeezde-skazali-ne-vernem/ (залог); /blog/hozyain-skazal-vse-vklyucheno-v-taksi-doplatili-2-400/ (скрытые доплаты); /blog/v-obyavlenii-vse-dlya-gostej-v-vannoj-odin-mokryj-kovrik/ (ожидания vs реальность); /blog/pereveli-3-000-predoplatoj-k-21-00-tishina-v-chate/ (предоплата)  
wp_category_slugs: posutochnaya-arenda, sovety-gostyam
