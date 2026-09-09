# Scout handoff B15

wordstat_preflight: mcp-kv wordstat_get_user_info OK
klyshin_hook: no_deposit_at_door | original: «Написали одно — у двери другое»; guest pain, не legal Klyshin
wordstat_rework: probe «без залога посуточно тюмень» → «квартира посуточно без залога» 1173 (225) | «снять квартиру посуточно без залога» 923 (225) | «залог посуточно» 3070 (225) | «не возвращают залог за квартиру посуточно» 64 (225) → final P0 «квартиры посуточно тюмень» 3552 (55) | compare 3552+11176 region | compare RU spine «квартира посуточно без залога» 1173 (225)
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 3552 | guest cluster «квартира посуточно без залога» 1173 (225)
angle_rotation: новый угол после B12 «тихий центр/стройка», B13 «ключница пустая», B14 «соседи/шум»; фильтр «без залога» в карточке против залога/депозита у двери
dzen_pattern: 2
dzen_shape_hint: двухтактный stop-factor; объявление «без залога» vs терминал/перевод у двери; сумма 5 000 ₽
topic_id: B15
short_title: Без залога — 5 000 у двери
title_draft: «Написали «без залога». У двери попросили 5 000 ₽»
slug: napisali-bez-zaloga-u-dveri-poprosili-5-000
signal_urls: https://t.me/klyshin_A | https://добрыйдом-72.рф/blog/ | https://t.me/Dobriy_dom_72
external_signal: Telegram: Klyshin_A и Dobriy_dom_72; блог «Добрый дом»
queue_slot: B15
season_note: 2026-09-09, Asia/Yekaterinburg; начало осени, не зима на обложке
interlink_siblings: B02 залог не вернули; B05 залог утром после уборки; B08 предоплата тишина; B10 всё включено
wp_category_slugs: posutochno, zalog
case_spine: Гость бронирует 2–3 ночи в Тюмени. В карточке «без залога», ночи оплачены ~7–9 тыс ₽. У двери хозяин: «залог 5 000, вернём после уборки». Цитата хозяина. Moral: сначала скрин условий из чата/карточки, потом ключ.
lockpick: «Залог в объявлении ноль — что будет у двери, если что-то поцарапаю?»
refusal: «Нет. Так не заселяем.» / «Сначала условия в переписке. Потом перевод. Не наоборот.»
