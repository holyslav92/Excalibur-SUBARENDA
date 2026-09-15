# Scout inputs — 2026-09-15 YEKT slot (B24)

## Date / season
- today: 2026-09-15, сентябрь, Asia/Yekaterinburg
- cover season: осень (не зима героем)

## Angle rotation (last N=3)
- B21: ранний заезд / уборка до 14:00
- B22: фото паспорта / код не пришёл (burn-at-door family)
- B23: уборка включена / доплата на выезде
- burn-at-door skip: YES — последние 3 не из одной семьи без нового угла; берём угол «обещание в карточке vs реальность в квартире» (техника/удобства, не код/залог)

## Published anti-dup + live WP drift (do NOT reuse slugs)
- sobaka-do-15-kg-doplata-u-dveri, kvartira-posutochno-lift-pyatyj-etazh, posutochno-napisali-postelnoe-est, otel-byl-dorozhe-900, zalog-5-000, kitchen B07, boiler B20, cleaning B23

## Klyshin hook (mechanics only, guest pain)
- hook_id: appliance_lie_washing_machine (new)
- original: «На фото в объявлении — стиральная машина. В квартире гость открывает коридор: вешалка, раковина, бельё на третий день.»
- angle: обещание техники в карточке vs реальность; lockpick: «Стиралка в квартире или в подвале/на этаже?»
- klyshin_signal: quote хозяина → «Нет. Так не заселяем.»; moral: сначала фото/видео кухни и санузла, потом оплата
- NOT legal/ЕГРН/Москва/Шакин

## Wordstat (MCP-KV live, regions 55+11176, compare 225)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probes:
1. «стиральная машина посуточно» → totalCount 57 (225)
2. «стиральная машина аренда квартиры» → 114 (225): «аренда квартиры стиральная машина» 114
3. «квартиры посуточно тюмень» → 4724 (55+11176), compare RU 10016
4. «снять квартиру посуточно фото» → 3693 (225) — supporting (фото vs реальность)

wordstat_rework: probe «стиральная машина посуточно» 57 → «стиральная машина аренда квартиры» 114 → «квартиры посуточно тюмень» 4724 (55+11176) | compare 10016 (225) | clusters tried: стиральная, посудомойка path skipped (overlap risk), appliance

final P0: «квартиры посуточно тюмень» 4724 (55+11176) | compare 10016 (225)

## Title draft (two-beat, NOT final H1)
«На фото — стиральная машина. В квартире — раковина и вешалка»

## dzen
- dzen_pattern: 2 (кейс с суммами и датами)
- dzen_shape_hint: «обещали стиралку — на третий день прачечная за 600 ₽»

## topic_id
B24

## primary_query
стиральная машина квартира посуточно тюмень

## suggested slug
napisali-stiralnaya-est-v-kvartire-tolko-rakovina

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
