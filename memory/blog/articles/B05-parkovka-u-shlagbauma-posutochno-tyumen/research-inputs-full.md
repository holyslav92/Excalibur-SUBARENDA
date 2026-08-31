# Research inputs B05 (embedded)
# Scout handoff — B05 parking_before_booking

- **topic_id:** B05
- **hook_id:** parking_before_booking (Klyshin queue slot 4, YEKT 2026-08-29 — 2026-09-07)
- **original Klyshin hook:** «Парковка рядом» — шлагбаум не пускает
- **angle:** место, пропуск, номер авто — до брони, не у барьера
- **klyshin_signal:** lockpick: «Где именно место и как въезд?»

## Wordstat (MCP-KV live 2026-08-31)

| phrase | volume | region |
|--------|--------|--------|
| аренда квартиры посуточно тюмень | 394 | 225 |
| квартиры в тюмени посуточно с парковкой | 7 | 225 |
| парковка квартира посуточно (cluster) | 420 | 225 |

**rework_log:** probe «парковка аренда квартиры» weak Tyumen slice → localize «квартиры посуточно тюмень с парковкой» 7 + parent «аренда квартиры посуточно тюмень» 394 → final P0 spine under H1.

**final P0:** `аренда квартиры посуточно тюмень` (394 RU) + pain cluster `посуточно с парковкой` (7 Tyumen)

## Anti-dup

Skip: lapoy, passport photo, uni-parents B03, B04 extra guest, B01 code, B02 deposit, hot water, wifi/10:00, contract bans, towels, reviews, checkout train.

## Proposed H1 shape (Title agent refines)

«Парковка бесплатно». У шлагбаума попросили 800 ₽

## Slug target

`parking-besplatno-shlagbaum-poprosili-800-rub`

## dzen_pattern_prefer

3 (страх → сцена), 2 (кейс с суммами)

## published-titles-only
# Published titles only — не читать тела статей

Этот файл — единственный «памятный» список для Writer/Research:
только topic_id, slug и заголовок.

**Запрещено:** открывать `memory/blog/articles/*/article.html`, drafts,
lessons, benchmarks, QA reports или соседние research-notes как образец
прозы. Заголовки нужны только чтобы не повторить уже покрытую тему.

| topic_id | slug | title | status |
|----------|------|-------|--------|
| B01 | beskontaktnoe-zaselenie-posutochno-tyumen | Оплатил квартиру посуточно. Код прислали от чужой двери | published |
| B02 | perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem | Снял квартиру посуточно. Залог не вернули — нашли скол на плите | published |
| B03 | kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki | Привезли сына к вузу — «рядом» оказалось 40 минут пешком | published |
| B04 | oplatil-za-dvoih-u-dveri-poprosili-doplatu-za-tretego | Оплатили за двоих. У двери попросили доплату за третьего | published |

## research-serp.json excerpts

### primary_fresh
- Парковки в Тюмени 2026: платные и бесплатные места, тарифы и штрафы — https://visittyumen.ru/what-to-do/prigoditsya-v-puteshestvii/parkovki-v-tyumeni-polnyy-gid-dlya-avtoputeshestvennikov/
  
- Парковку на набережной временно закрыли — шлагбаум опущен — https://tyumen72.info/2026/05/08/parkovku-na-naberezhnoi-vremenno-zakryli-shlagbaum-opushchen/
  В Тюмени два типа парковок, каждый имеет свою особенность. Это огражденные территории со шлагбаумом и автоматической кассой для оплаты. Например, большая парковка на набережной в районе моста Влюбленных или у Городской площади (ул. Первомайская, 20).
- Шлагбаум раздора появился в Тюмени — его хозяина ищут - 10 июня 2026 ... — https://72.ru/text/gorod/2026/06/10/76471940/
  Шлагбаум на въезде на набережную опущен, парковка временно недоступна. Рекомендуем учитывать это при планировании маршрута и искать альтернативные места для стоянки.
- Штрафы за неоплаченную парковку в Тюмени — https://shtrafy-gibdd.ru/articles/shtrafy-za-neoplachennuyu-parkovku-v-tyumeni-proverit-oplatit
  Родители тюменских футболистов пожаловались на установленный шлагбаум на парковку, которая находится недалеко от стадиона «Геолог» и совсем рядом со Дворцом спорта на Розы ...
- Парковки Тюмени: с 2 июня платить придётся ещё на 10 улицах — https://megatyumen.ru/avto/shtraf-mozhno-poluchit-uzhe-segodnya-v-tyumeni-zarabotali-novye-platnye-parkovki/
  Рассказываем, как это сделать, какой штраф за неоплату парковки в Тюмени и где смотреть штрафы за парковку в Тюмени.

### title_fresh
- Парковки в Тюмени 2026: платные и бесплатные места, тарифы и штрафы — https://visittyumen.ru/what-to-do/prigoditsya-v-puteshestvii/parkovki-v-tyumeni-polnyy-gid-dlya-avtoputeshestvennikov/
  
- Парковку на набережной временно закрыли — шлагбаум опущен — https://tyumen72.info/2026/05/08/parkovku-na-naberezhnoi-vremenno-zakryli-shlagbaum-opushchen/
  В Тюмени два типа парковок, каждый имеет свою особенность. Это огражденные территории со шлагбаумом и автоматической кассой для оплаты. Например, большая парковка на набережной в районе моста Влюбленных или у Городской площади (ул. Первомайская, 20).
- Шлагбаум раздора появился в Тюмени — его хозяина ищут - 10 июня 2026 ... — https://72.ru/text/gorod/2026/06/10/76471940/
  Шлагбаум на въезде на набережную опущен, парковка временно недоступна. Рекомендуем учитывать это при планировании маршрута и искать альтернативные места для стоянки.
- Штрафы за неоплаченную парковку в Тюмени — https://shtrafy-gibdd.ru/articles/shtrafy-za-neoplachennuyu-parkovku-v-tyumeni-proverit-oplatit
  Родители тюменских футболистов пожаловались на установленный шлагбаум на парковку, которая находится недалеко от стадиона «Геолог» и совсем рядом со Дворцом спорта на Розы ...
- Парковки Тюмени: с 2 июня платить придётся ещё на 10 улицах — https://megatyumen.ru/avto/shtraf-mozhno-poluchit-uzhe-segodnya-v-tyumeni-zarabotali-novye-platnye-parkovki/
  Рассказываем, как это сделать, какой штраф за неоплату парковки в Тюмени и где смотреть штрафы за парковку в Тюмени.

### official_docs
- Парковки в Тюмени 2026: платные и бесплатные места, тарифы и штрафы — https://visittyumen.ru/what-to-do/prigoditsya-v-puteshestvii/parkovki-v-tyumeni-polnyy-gid-dlya-avtoputeshestvennikov/
  
- В Тюмени неизвестные установили шлагбаум, перекрывающий парковку ... — https://72.ru/text/gorod/2026/06/10/76471940/comments/
  В Тюмени два типа парковок, каждый имеет свою особенность. Это огражденные территории со шлагбаумом и автоматической кассой для оплаты. Например, большая парковка на набережной в районе моста Влюбленных или у Городской площади (ул. Первомайская, 20).
- Как работают платные парковки в центре Тюмени: подробная инструкция — https://fedpress.ru/article/2884772
  Шлагбаум раздора появился в Тюмени — его хозяина ищут. Количество комментариев 47 | 72.ру.
- Парковку на набережной временно закрыли — шлагбаум опущен — https://tyumen72.info/2026/05/08/parkovku-na-naberezhnoi-vremenno-zakryli-shlagbaum-opushchen/
  Платные парковки в Тюмени работают с 9:00 до 18:00 по будням согласно производственному календарю. Стоимость часа варьируется от 25 до 40 рублей в зависимости от расположения и загруженности...
- Шлагбаум раздора появился в Тюмени — его хозяина ищут - 10 июня 2026 ... — https://72.ru/text/gorod/2026/06/10/76471940/
  Шлагбаум на въезде на набережную опущен, парковка временно недоступна. Рекомендуем учитывать это при планировании маршрута и искать альтернативные места для стоянки.

Write research-notes.md markdown with sections:
reader_problem, reader_outcome, practical_facts, constraints, typical_errors, voice_angle, surprising_fact, signal_urls, writer_checklist

Case: guest with car, host wrote «parking free/nearby», gated yard barrier demands 800 ₽ or pass not shared before booking.
Use only facts from SERP above. Wordstat: аренда квартиры посуточно тюмень 394; квартиры посуточно тюмень с парковкой 7.
No invented addresses. Ban ЕГРН/Шакин/922 phone.
Output ONLY research-notes.md body markdown.
