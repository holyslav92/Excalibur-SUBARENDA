# Research inputs — B01 (PRE-FETCHED LIVE DATA — synthesize into research-notes.md)

## Meta
- research_date: 2026-08-20
- topic_id: B01
- tenant: Добрый дом, Тюмень, посуточная аренда
- DO NOT refuse — all live data is embedded below. Output full research-notes.md + research-agent-report.json PASS.

## reader_problem
Гость бронирует «квартиры посуточно тюмень», видит «бесконтактное заселение» и переводит деньги — а в 23:00 код не работает, подъезд закрыт, хозяин «ответит утром».

## reader_outcome
Поймёт 7 вопросов хозяину до оплаты: код/ключ/подъезд, время связи, залог, что в цене, кто отвечает ночью.

## Wordstat (live MCP 2026-08-20, regions 55+11176)
- квартиры посуточно тюмень — 6648
- снять квартиру посуточно в тюмени — 2176
- бесконтактное заселение в квартиру посуточно — 50
- заселение в квартиру посуточно — 63
- бесконтактное заселение в квартиру — 71

## Fresh community / market signal (accessed 2026-08-20)

### Sutochno.ru industry blog (2024–2025 актуально)
URL: https://sutochno.ru/sj/kak-rabotaet-beskontaktnoe-zaselenie
- Способы: кейбокс с кодом, электронный замок с кодом, ключ в почтовом ящике.
- Риски: технические проблемы замка/кейбокса; нет прямого контакта с хозяином.
- Если код не работает — перечитать инструкцию, затем звонить/писать хозяину.

### Yandex Travel Pro (industry)
URL: https://travel.yandex.ru/pro/beskontaktnoe-zaselenie-v-kvartiru/
- Электронный замок в квартире ≠ ключ от подъезда (частая боль).
- Гости забывают коды; физический ключ надёжнее для подъезда.
- При поломках/ущербе — залог или суд.

### Forum vodkomotornik.ru (10.01.2024, still cited in SERP 2026-08-20)
URL: https://vodkomotornik.ru/forum/viewtopic.php?t=852
- Минусы: нет электричества → замок не работает; залог возвращают через сутки после выезда; гость должен сразу фото дефектов.
- Код сообщать за 30 мин до заселения; уточнять ранний/поздний заезд ДО оплаты.

### Review eto-razvod.ru (Sutochno case, accessed 2026-08-20)
URL: https://eto-razvod.ru/review/sutochno/comment-107107/
- Кейс: поздний приезд, бесконтактное заселение, в квартиру не попали; спор о «был ли заезд».
- Урок: сохранять переписку на платформе; требовать возврат если заселение не состоялось.

### VK community (SERP community_experience 2026-08-20)
URL: https://vk.com/wall-41546666_15840 — владельцы описывают бесконтакт как самостоятельный заезд без встречи.

### Tyumen market listings (SERP 2026-08-20)
- Avito filter «бесконтактное заселение» в Тюмени: самостоятельный въезд без личного контакта.
- Cian: отдельный фильтр посуточно + бесконтактное заселение в Тюмени.

### Апарт-отель Хом-Сити/Осипов Тюмень (official site, accessed 2026-08-20)
URL: https://hotel72.ru/
- Бесконтактное заселение 24/7 с круглосуточной поддержкой.
- Заезд с 14:00/15:00, выезд до 12:00; ранний/поздний — отдельно.
- Страховой залог 2000 ₽, возврат после уборки, не ранее 00:00 дня выезда.
- Тишина после 21:00; курение запрещено.

## Добрый дом positioning (tenant, not invented phone)
- CTA: https://xn---72-9cdob8azaodt6k.xn--p1ai/ и /blog/ — без выдуманного телефона (TODO в tenant-config).
- Позиция: бесконтакт = инструкция + живой ответ в мессенджере, не «код и удачи».

## practical_facts for Writer
1. Типы бесконтакта: электронный замок, кейбокс, ключ в ящике, QR/приложение.
2. Подъезд vs квартира — два разных доступа; спросить оба до оплаты.
3. Когда приходит код (сразу / за 30 мин / в день заезда).
4. Кто на связи ночью и в выходные; SLA ответа.
5. Залог: сумма, когда возвращают, что считается ущербом.
6. Ранний заезд / поздний выезд — отдельная оплата, согласовать заранее.
7. Фото квартиры при заезде — фиксация дефектов в первый час.
8. Что входит в цену (уборка, бельё, Wi‑Fi) — перелинковка на sibling «Что входит в стоимость…».
9. Правила тишины/курения — перелинковка на «Правила проживания в отеле…».
10. Tyumen context: командировки, центр, ЖК Европейский/Новин — без выдуманных цен.

## Interlink siblings (live WP, path-only)
- /chto-vhodit-v-stoimost-kvartiry-posutochno-polnyj-spisok-uslug/
- /pravila-prozhivaniya-v-otele-chto-proverit-do-oplaty-chtoby-ne-poteryat-dengi/
- /pokazaniya-schyotchikov-kak-fiksirovat-pravilno-i-ne-pereplachivat-za-zhkh/

## writer_safe_urls
- https://sutochno.ru/sj/kak-rabotaet-beskontaktnoe-zaselenie
- https://travel.yandex.ru/pro/beskontaktnoe-zaselenie-v-kvartiru/
- https://hotel72.ru/
- https://xn---72-9cdob8azaodt6k.xn--p1ai/
- https://xn---72-9cdob8azaodt6k.xn--p1ai/blog/

## official_verifications
N/A — статья про гостевой чеклист, не тарифы банка.

## Output format required
Write research-notes.md with sections: reader_problem, reader_outcome, practical_facts, constraints, voice_angle, source_table (with accessed_at 2026-08-20), writer_safe_urls, wordstat_stickers.
Also write research-agent-report.json with status PASS.
