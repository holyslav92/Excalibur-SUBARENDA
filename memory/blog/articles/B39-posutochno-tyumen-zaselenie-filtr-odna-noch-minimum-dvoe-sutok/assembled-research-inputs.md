# Assembled research inputs — B39 (2026-09-30 YEKT)

## Topic and case brief (Scout + handoff)
- topic_id: B39
- market: посуточная аренда, Тюмень, бренд «Добрый дом»
- hook_id: min_nights_at_door
- klyshin_original (angle mechanics): «В карточке — от одной ночи. У двери — только от двух»
- editorial composite CASE: пара/командировочный гость выбрал в фильтре «от 1 ночи», оплатил одну ночь (например 4 600–5 200 ₽); у домофона хост/менеджер: «у нас минимум двое суток» или доплата за вторую ночь на месте; такси с багажом уехало; переписка в агрегаторе до оплаты не содержала явного минимума
- dzen_shape: фильтр одна ночь vs правило двух суток у двери + ₽
- anti-dup: не B32 (цена на оплате), не B34 (залог), не B04 (третий гость), не B21 (ранний заезд/уборка), не B35 (подъезд), не live slug oplachena-odna-noch-minimum-dvoe-sutok (если есть — другой угол: здесь фильтр «от одной ночи»)
- wp_category_slugs: posutochno, zaselenie
- title_draft two-beat: «В фильтре — «от одной ночи». У домофона: «минимум двое суток»»

## research-context (today)
- today_iso: 2026-09-30, weekday: среда, сентябрь 2026
- SERP: research-serp.json 2026-09-30 — агрегаторы посуточной аренды Тюмени; обсуждения минимального срока брони на форумах/Дзен

## Wordstat MCP-KV (live 2026-09-30, conductor)
| phrase | region | volume / note |
|--------|--------|----------------|
| квартиры посуточно тюмень | 55+11176 | 4194 |
| квартиры посуточно тюмень | 225 | 9212 |
| снять квартиру посуточно в тюмени | 55+11176 | 1201 |
| заселение в квартиру посуточно | 225 | 2662 |
| заселение посуточно тюмень | 55+11176 | 12 weak local |

P0 spine: «квартиры посуточно тюмень». Угол min nights — guest booking rules at check-in.

## Fresh signals this week (2026-09-23 — 2026-09-30)

### Community — tenant channel Dobriy_dom_72
- Проверить https://t.me/s/Dobriy_dom_72 за 23–30.09: посты про расхождение карточки и оплаты/заселения (комиссия, фильтры, «в карточке одно — у двери другое»).

### Community — Klyshin signal
- https://t.me/s/klyshin_A — активность 28–30.09; mechanics min nights, не копировать сделки/ЕГРН.

### SERP / aggregators
- Sutochno.ru, Avito, ЦИАН — в карточках часто «минимальный срок» в правилах; гость видит фильтр «1 ночь» в поиске.

## Writer constraints (internal)
- Один кейс, 1100–1800 слов target but gate hard fail >1300 — aim 700–1100 for Sol
- Holyslav §1: quote-first, ₽, no clock-stamp ladder in lead
- 3–4 interlink to published siblings from shared/published-articles.md

## Pre-fetched community (conductor 2026-09-30, use as fresh_signal — do NOT fetch)
- https://t.me/s/Dobriy_dom_72 — 27.09.2026: пост про фильтр «без комиссии» vs комиссия на экране оплаты (расхождение карточки/фильтра и следующего шага).
- https://t.me/s/Dobriy_dom_72 — 29.09.2026: forward «Добрый Контент» / живые отзывы — гости пишут про детали (шум, диван, дверь), не только звёзды.
- Klyshin https://t.me/s/klyshin_A active 28–30.09.2026 — mechanics min nights angle only.

## Output instruction for Derouter (HARD)
You have NO web tools in this call. All facts are in this file. Write ONLY the body of `research-notes.md` in Russian markdown sections matching B37 format (# research_date, # reader_problem, # practical_facts, # fresh_signal_note, # source_table with accessed_at 2026-09-30). No BLOCKER, no shell instructions, no meta-refusal.
