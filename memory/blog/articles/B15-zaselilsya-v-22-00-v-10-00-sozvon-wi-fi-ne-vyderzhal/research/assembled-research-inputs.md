# Assembled research inputs — B15

**Return ONLY research-notes markdown in response; do NOT return DEROUTER RESEARCH BLOCKER.**

Live fetch, Wordstat MCP-KV, Telegram and market price checks are already done by the conductor. Use the facts below as-is; do not refuse synthesis.

**research_date:** 2026-09-08 (Asia/Yekaterinburg)  
**topic_id:** B15  
**tenant:** «Добрый дом», посуточная аренда в Тюмени  
**format:** CASE 700–1100 слов, dzen_pattern 2  
**title_draft:** «Заселился в 22:00. В 10:00 созвон — Wi‑Fi не выдержал»  
**hook (Klyshin):** «Звонок в 10:00. Заселился в 22:00.»  
**lockpick:** «Сколько Мбит на загрузку и есть ли розетка у стола, не под кроватью?»  
**refusal:** «Нет. Так не бронируем.» / «Сначала скорость и документы. Потом ключ.»

## Scout handoff — case spine (редакционная реконструкция, не реальная сделка)

1. Инженер/менеджер, командировка в Тюмень, **3 ночи**, сумма **~10 200 ₽** (ориентир ~3 400 ₽/ночь в сентябре).
2. Рейс поздно, **заселение в 22:00**. В объявлении: Wi‑Fi и рабочее место.
3. Утром **10:00** — видеосозвон. Скорость **~3–5 Мбит**: камера рвётся, звук запаздывает.
4. Удобная **розетка у кровати**, не у стола; работа с удлинителем/в неудобной позе.
5. Хозяин: «Ну у нас же интернет есть» — формальное наличие ≠ пригодность для созвона.
6. Закрывающие «**по запросу**» — после заселения нет ясности по срокам и комплекту для бухгалтерии.
7. Вывод: скорость, розетка у стола, документы — **до оплаты** и позднего заезда.

**Не использовать:** Москву, ЕГРН, чужие сделки, B12–B14 углы (шум, ключница, соседи).

## Anti-overlap (published titles only)

B12 тихий центр/стройка; B13 ключница; B14 соседи/музыка. B15 = командировка, Wi‑Fi для созвона, розетка, закрывающие.

## Wordstat (MCP-KV live, accessed 2026-09-08)

| phrase | volume | region |
|--------|--------|--------|
| квартиры посуточно тюмень | 5134 | 55+11176 |
| снять квартиру посуточно в тюмени | 1672 | 55+11176 |
| аренда квартир посуточно тюмень | 187 | 55+11176 |
| аренда квартиры посуточно | 704 | 55+11176 |
| квартира посуточно командировка | 77 | 225 |
| квартиры для командировок | 517 | 225 (scout) |

P0 SEO: «квартиры посуточно Тюмень»; кластер «снять квартиру посуточно в Тюмени».

## Tyumen market prices (сентябрь 2026, вилка, не точная цена кейса)

- **Суточно.ру** (tyumen.sutochno.ru, 2026-09-08): тысячи объявлений; типичные карточки **2 800–3 500 ₽/сутки** при заезде «сегодня»; встречаются **3 900–5 400 ₽**.
- **Авито Путешествия** (avito.ru/tyumen, 2026-09-08): студии **от 1 800–2 300 ₽**, однушки **2 500–3 500 ₽**, частые **3 400 ₽**, верх сегмента **4 500+ ₽**.
- **72.ru / tyumen.ru** (21.03.2026, контекст рынка): средняя посуточная аренда в Тюмени **~3 000 ₽/сутки**, +15% г/г; спрос +20%.
- **Ostrovok** (2026-09-08): апартаменты Тюмень **от ~2 373 до ~5 641 ₽/сутки**.
- **Кейс handoff:** 3 ночи × ~3 400 ₽ ≈ **10 200 ₽** — правдоподобная сумма для сентября, не «средняя по больнице».

## Video call bandwidth — OFFICIAL (для сравнения с 3–5 Мбит)

### Zoom (support.zoom.com, KB0058323 / KB0060748, accessed 2026-09-08)

- 1:1 high-quality video: **600 kbps** up/down
- 1:1 **720p HD: 1.2 Mbps** up/down
- 1:1 **1080p HD: 3.8/3.0 Mbps** up/down
- **Group** high-quality: **1.0 Mbps up / 600 kbps down**
- Group **720p: 2.6 Mbps up / 1.8 Mbps down**
- Group **1080p: 3.8/3.0 Mbps**
- Audio VoIP: 60–80 kbps
- Upload often bottleneck on residential Wi‑Fi

### Microsoft Teams (learn.microsoft.com/prepare-network, accessed 2026-09-08)

- «HD video quality in **under 1.5 Mbps**» (conservative)
- Recommended one-to-one video: **1 500/1 500 kbps** (1.5 Mbps)
- Best performance one-to-one: **4 000/4 000 kbps**
- Meetings recommended video: **2 500/4 000 kbps** up/down
- When bandwidth insufficient, Teams **prioritizes audio over video**
- Minimum video: up to 240p
- Wi‑Fi: recommend QoS/WMM, **5 GHz** over 2.4 GHz for real-time media

### Google Meet (support.google.com/a/answer/1279090, ru, accessed 2026-09-08)

- Individuals: **720p up to 1.7 Mbps**, **1080p up to 3.6 Mbps** outbound
- Group meeting: **250 Kbps and up** outbound (minimum floor, not comfort)
- Large org average video: **1 Mbps** out / **1.3 Mbps** in
- If insufficient bandwidth, Meet **lowers video definition** or audio-only
- Live stream ideal: **2.6 Mbps** per viewer

### Практический вывод для кейса

- **3–5 Мбит** на загрузку (upload) — на грани для **720p group** (Zoom 1.8–2.6 Mbps upload) и **ниже комфорта** для стабильного HD+камера+экран.
- При 3 Мбит upload созвон может «работать», но с **просадками, роботизированным звуком, отключением камеры** — особенно если Wi‑Fi не 5 GHz, роутер в коридоре, несколько устройств в сети.
- Фраза «интернет есть» не равна «тянет Zoom/Teams/Meet утром в 10:00».

## Wi‑Fi vs cable — контекст (не официальный тариф)

- Wi‑Fi almost always **slower than wired**; walls, distance, 2.4 GHz congestion, old router (gigaboom.ru, istoki.tv — accessed 2026-09-08).
- Test: speedtest at **desk location**, not at router; multiple tests; check **upload** not only download.
- ipnet.ua (2024, general): unstable Wi‑Fi causes — router placement, microwave interference, too many devices, 2.4 vs 5 GHz.

## Workspace / розетка

- Handoff: «рабочее место» в объявлении ≠ стол с **розеткой у стола**.
- Типичная боль: единственная розетка у кровати → ноутбук на коленях, удлинитель через комнату.
- TG «Добрый дом» (2026-09-08): «Чемодан… Wi‑Fi… лучше проверить **до брони**»; «исправность техники» проверяют до заселения.
- Dzen Dobry Dom (May 2025, editorial): «забыть про рабочее место» — стол, **розетка рядом** — third pitfall for remote work.

## Закрывающие документы для командировки (медиа/право, не банк)

- **Газета УНП** (gazeta-unp.ru, accessed 2026-09-08): пакет для бухгалтерии — договор найма, акт приёма-передачи, платёжный документ (чек/квитанция); у самозанятого **обязателен чек «Мой налог»**, иначе расходы не примут.
- **ЭЛКОД / ФНС контекст** (elcode.ru): чек НПД с **ИНН заказчика**; рекомендуют краткий договор + чек + акт.
- **Главбух** (2026): договор + акт передачи + платёжные документы обязательны; «по запросу» без сроков = риск для отчёта.
- **Суточно.ру /documents** и **kvartirka.com** (2026-09-08): фильтр «с отчётными документами» для командировок — рынок ожидает договор+чек; уточнять **до** брони.
- Фраза «документы по запросу» без: кто выдаёт, когда, чек на юрлицо или физлицо — красный флаг для командировочного.

## Fresh signals (week of 2026-09-08)

1. **Telegram @Dobriy_dom_72** (accessed 2026-09-08): репосты «Добрый Контент» — «Wi‑Fi… проверить до брони»; «ночной рейс… уточнить до оплаты, как попасть внутрь»; «исправность техники» до заселения; «ответ за 5 минут» vs тишина в чате.
2. **Telegram ecosystem** (same date): несоответствие описания — «заявлена тишина» vs факт; B15 другой угол (Wi‑Fi/розетка).
3. **Добрыйдом-72.рф/blog/** (2026-09-08): кейсы B01–B14; позиционирование «для командировок».
4. **Dzen SERP snippet** (ipnet/dzen, Aug 2026): «Добрый Дом» — инженер, командировка, созвон 10:00 (соседний editorial angle; не копировать текст).

## Constraints for Writer

- Не выдумывать адрес, ФИО, площадку брони, имя хозяина, точный speedtest.
- 3–5 Мбит — **реконструкция кейса** из handoff; сравнивать с официальными порогами Zoom/Teams/Meet.
- Не гайд по Speedtest; не VPN; не Meta/IG.
- Не читать соседние article.html.
- CTA: t.me/Dobriy_dom_72, t.me/Dobriy_dom_Tyumen, max.ru/id660300569233_biz, добрыйдом-72.рф/booking/
- official_verifications: банков/тарифов нет — scope PASS not required.

## Required output structure (research-notes.md)

- YAML-style header: research_date, topic_id, hook, anti-dup
- reader_problem (one pain)
- reader_outcome (one result for reader)
- case facts, practical_facts, constraints
- voice_angle, surprising_fact (if sourced)
- demand signals (wordstat table)
- official_verifications (note not required)
- source_table with accessed_at 2026-09-08 for every row
- writer_safe_urls
- NO h2_outline, lead, FAQ skeleton, action_outline
