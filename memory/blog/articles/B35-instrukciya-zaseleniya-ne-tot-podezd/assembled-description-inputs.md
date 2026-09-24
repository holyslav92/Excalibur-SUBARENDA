# Description inputs B35

Return ONLY valid description-brief.json. NO BLOCKER.

H1: PDF на три страницы. Дом верный — 35 минут с чемоданом у чужого подъезда
dzen_pattern: 1
Angle: гость оплатил 2 ночи в Тюмени, навигатор привёл к верному дому; PDF с подъездом, кодом и этажом; код сработал — но это другой подъезд, ключницы нет; хозяин пишет «Вы не туда»; 35 минут с чемоданом по мокрому двору. Guest pain: не неверный адрес и не мёртвый домофон — чужой вход при правильном доме; длинная инструкция без маршрута от тротуара.
Teaser for Dzen card — NOT duplicate H1, NOT lead copy (lead opens with «Вы не туда», такси уехало, PDF три страницы, 9 600 ₽, осень/дождь — do not echo that opening or repeat «PDF на три страницы» / «35 минут» as in H1). Klyshin rhythm, 1-2 sentences (~120-220 chars).
Brand: Добрый дом (author_brand field only). HARD: description text must NOT contain «Добрый дом» together with 3–5 digit amounts (gate). Avoid guest-burn price ladder. No Шакин / The Риэлтор. Prefer NOT putting brand name in teaser if it forces awkward phrasing — author_brand stays in JSON.
Geo: Тюмень. Guest pain: самозаселение, инструкция заселения, не тот подъезд, маршрут vs адрес, бесконтактное заселение.
Wordstat P0: квартиры посуточно тюмень.
Key hooks (pick one): «код щёлкнул — а этаж чужой»; «дом тот, подъезд нет»; «Вы не туда» после трёх страниц текста; сверить путь до двери, не только адрес на карте.

Article lead (DO NOT truncate): composite Tyumen evening case, wrong entrance despite working code.
Research voice: контраст PDF в телефоне и двора, где подъезд не находится по тексту.
