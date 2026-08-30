# Research assembled inputs — B04 Wi-Fi на созвоне

## EXECUTION INSTRUCTION (Derouter utility)
You ARE the Derouter research synthesizer. Output ONLY the complete `research-notes.md` markdown body per SKILL.md format. Do NOT mention shell, BLOCKER, or inability to run scripts — this API call is the synthesis. Use facts from inputs below only.

research_date: 2026-08-30
topic_id: B04
tenant: Добрый дом, посуточная аренда, Тюмень
priority: P0

## Scout handoff (2026-08-30)

- klyshin_hook: sept_business_trip | original: «Звонок в 10:00. Заселился в 22:00.»
- angle: Wi-Fi падает на видеосозвоне; в объявлении «быстрый интернет»; moral: сначала тест скорости/роутер, потом оплата
- signal_urls: https://t.me/klyshin_A, https://добрыйдом-72.рф/blog/
- final P0 wordstat: «квартиры посуточно тюмень» 5500 (55+11176) / 12325 (225)
- secondary: «аренда квартиры посуточно» 792 (55+11176) / 45932 (225)
- dzen_pattern: 3 (страх → инструкция)
- season_note: YEKT 2026-08-30 — конец августа, командировочный сезон к сентябрю
- interlink_siblings:
  - https://добрыйдом-72.рф/blog/beskontaktnoe-zaselenie-posutochno-tyumen/
  - https://добрыйдом-72.рф/blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/
- wp_category_hint: posutochnaya-arenda

## Published titles (anti-dup only)

- B01: Оплатил квартиру посуточно. Код прислали от чужой двери
- B02: Снял квартиру посуточно. Залог не вернули — нашли скол на плите
- B03: Привезли сына к вузу — «рядом» оказалось 40 минут пешком

## Wordstat live (MCP-KV, regions 55+11176, accessed 2026-08-30)

### P0 «квартиры посуточно тюмень» — totalCount 5500
1. квартиры посуточно тюмень — 5500
2. снять квартиру посуточно в тюмени — 1761
3. квартиры посуточно в тюмени недорого — 430
4. квартиры посуточно тюмень без посредников — 360
5. авито квартиры посуточно тюмень — 341
6. аренда квартиры тюмень посуточно — 207
7. квартиры посуточно тюмень от хозяев — 141

### Secondary «аренда квартиры посуточно» — totalCount 792
1. аренда квартиры посуточно — 792
2. аренда квартиры тюмень посуточно — 207
3. договор посуточной аренды квартиры — 45
4. авито аренда квартир посуточно — 42

### Probe «командировка квартира посуточно» — totalCount-only 1 (WORDSTAT PARTIAL)
- Слишком узкий кластер; основной спрос — широкий P0 «квартиры посуточно тюмень»

### Probe «интернет квартира посуточно» — totalCount-only 1 (WORDSTAT PARTIAL)
- Wi-Fi не выделяется отдельным высокочастотным кластером; угол — buyer pain внутри P0

## Fresh community / market signals (accessed 2026-08-30)

### 1. Raido — гайд для командировочных (industry, июнь 2026)
URL: https://go.raido.moscow/guides/internet-i-rabochee-mesto-v-komandirovke/
- «Есть Wi-Fi» почти ничего не говорит о качестве: важны скорость, стабильность, задержка, покрытие в конкретном номере, VPN, отсутствие разрывов вечером.
- Перед важным созвоном — короткий тест: VPN, файлы, микрофон, камера, скорость в месте, где реально сидите.
- Zoom 720p group: ~2.6 Mbps upload / 1.8 Mbps download; 1080p выше.
- Microsoft Teams: recommended 2500–4000 kbit/s up/down для видеовстреч.
- Практика: не ставить главный созвон сразу после заезда; отключить лишние загрузки; держать мобильный резерв.
- После заселения: поставить ноутбук на рабочее место, тестовый звонок без аудитории, проверить фон для видео.

### 2. Sutochno.ru — каталог «квартир с Wi-Fi» + акция до 31.08.2026 (marketplace)
URL: https://www.sutochno.ru/wifi
- Заголовок раздела: «В каждой квартире есть Wi-Fi интернет».
- Промо: «Забронируйте до 31 августа 2026 — и получите кэшбэк бонусами после оценки проживания».
- Фильтр Wi-Fi в объявлениях ≠ гарантия скорости под видеозвонок; SLA на Мбит/с в карточке нет.

### 3. vc.ru — отзыв про Авито Путешествия (community, 2026)
URL: https://vc.ru/services/1992198-otzyv-o-avito-puteshestviya
- Кейс: в забронированной квартире не работал обещанный Wi-Fi; после обращения в поддержку проблема решена за ~1 час.
- Практика: писать хозяину в чат до оплаты; проверять скорость и стабильность для видеозвонков.
- Автор vc.ru/travel/3042793 отмечает «быстрый Wi-Fi» как критерий при выборе жилья, если работает из номера.

### 4. Klyshin topic bank hook (angle seed, NOT legal post)
- hook_id: sept_business_trip
- Сцена: «Звонок в 10:00. Заселился в 22:00.»
- Lockpick: стол, розетки, Wi-Fi на созвон, закрывающие — до оплаты
- Канал https://t.me/klyshin_A — свежие посты августа 2026 про сделки/риски; прямого поста про Wi-Fi в ленте нет, угол из topic bank + guest pain

### 5. SERP community_experience (research-serp.json 2026-08-30)
- Агрегаторы (Sutochno, Avito, Ozon Travel) — фильтр «интернет/Wi-Fi» как стандарт, без теста роутера.
- Отзывы на агрегаторах: встречаются жалобы «wi-fi не работает» / «интернет есть, но слабый».

## Brand facts Добрый дом (allowed)

- Бесконтактное заселение, поддержка в мессенджере
- Инструкция заранее, не у двери
- До заселения гость получает данные Wi-Fi; при проблемах — менеджер на связи
- По запросу — тестовый созвон до оплаты (brand positioning, не независимый отзыв)
- Комфорт+, не бизнес-класс / не люкс
- 10 лет Сургут+Тюмень
- Телефон: +7 (993) 574-83-22
- TG канал: https://t.me/Dobriy_dom_72
- TG менеджер: https://t.me/Dobriy_dom_Tyumen
- MAX: https://max.ru/id660300569233_biz
- Бронь: https://добрыйдом-72.рф/booking/
- Блог: https://добрыйдом-72.рф/blog/

## Buyer pain (for Writer)

- Гость в командировке заселяется поздно (22:00), утром в 10:00 — важный видеосозвон.
- В объявлении «быстрый интернет» / галочка Wi-Fi; на 3-й минуте Zoom/Teams рвётся.
- Роутер в коридоре, в спальне 1–2 деления; speedtest у двери ≠ у стола.
- Проверка связи после оплаты — поздно менять квартиру.
- Нужны конкретные вопросы хосту до перевода денег.

## Checklist для Writer (после moral)

1. Спросить SSID, пароль, фото роутера и рабочего места
2. Speedtest у стола (download, upload, ping) — не у входной двери
3. Один роутер или репитер; 2.4 vs 5 ГГц
4. Короткий тестовый видеозвон с хостом до оплаты (2 мин)
5. План B: мобильный интернет, контакт менеджера ночью
6. «У нас»: инструкция заранее + тестовый созвон по запросу

## Forbidden to invent

- Конкретные коды доступа, суммы залогов
- «Гарантируем 100 Мбит» без подтверждения
- SLA платформ на скорость
- Тарифы провайдеров без official_verifications

## Required output in research-notes.md

- research_date: 2026-08-30
- reader_problem / reader_outcome (одна боль)
- practical_facts, constraints
- voice_angle, surprising_fact (если есть в источниках)
- source_table (accessed_at 2026-08-30 у каждой строки)
- writer_safe_urls
- official_verifications (N/A unless bank/platform tariff digits)
- НЕ писать h2_outline, lead, FAQ, action_outline
