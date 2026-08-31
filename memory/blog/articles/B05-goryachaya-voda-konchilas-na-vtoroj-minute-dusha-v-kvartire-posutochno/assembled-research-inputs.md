# Assembled research inputs — B05 (for Derouter research role)

## Meta
- topic_id: B05
- slug: goryachaya-voda-konchilas-na-vtoroj-minute-dusha-v-kvartire-posutochno
- research_date: 2026-08-31
- tenant: Добрый дом — посуточная аренда Тюмень, comfort+, NOT realtor/legal
- season: конец лета 2026, без зимних мотивов
- overlap check: published B01–B04 — codes, deposit, university distance, extra guest; no duplicate hot-water/boiler case

## Scout handoff (excerpt)
- klyshin_hook: sept_business_trip | original «Звонок в 10:00. Заселился в 22:00.» | rework → бойлер/горячая вода после позднего заселения командировки
- dzen_shape_hint: «Горячая вода была. На второй минуте душ — холод» / «Заселились в 23:00. Бойлер «есть» — в инструкции мелким: греть 40 минут»
- reader_pain: гость после рейса/командировки заселяется поздно, лезет в душ — горячая вода кончилась через минуту-две; бойлер маленький или выключен, инструкция «греть 40 минут» спрятана
- tyumen_supply (brand allowed, not invented inventory): инструкция по бойлеру заранее, не у двери; проверка перед поздним заселением
- signal_urls: https://t.me/klyshin_A , https://добрыйдом-72.рф/blog/

## Wordstat (MCP-KV, accessed 2026-08-31)
| phrase | volume | region |
|--------|--------|--------|
| квартиры посуточно тюмень | 5463 | 55+11176 |
| снять квартиру посуточно в тюмени | 1754 | 55+11176 |
| бойлер горячая вода | 374 | 55+11176 |
| горячая вода квартира | 30961 | 225 |
| аренда квартиры посуточно | 45250 | 225 (conductor) |
| related: водонагреватель | 15727 | 55+11176 |
| related: как включить горячую воду в квартире | 1666 | 225 |

## Fresh signals (accessed 2026-08-31)

### 1. Klyshin channel — https://t.me/s/klyshin_A (channel_signal, this week queue slot 2026-08-29—31)
- Hook bank `sept_business_trip`: «Звонок в 10:00. Заселился в 22:00.» — angle reworked to late check-in + hidden boiler instruction (not original Wi‑Fi/docs angle).
- Klyshin delivery pattern: short quote → break → moral; for this article moral maps to «сначала вода/инструкция, потом ключ», not legal due diligence.
- Channel live 31.08.2026: fresh August posts (e.g. summer law roundup «Пока вы летом отдыхали…», July 2026 Rosreestr stats). No literal hot-water post — use only rhythm/hook, NOT deal facts.

### 2. subsived.ru — посуточная аренда, правила для собственника (industry, modified 12.06.2026, fetched 2026-08-31)
- Техоснащение влияет на отзывы сильнее декора: гостю нужны предсказуемый сон, **горячая вода**, интернет, розетки.
- **Если бойлер включается отдельно — повесьте памятку рядом.** Инструкция экономит десятки звонков.
- Правила проживания: условия использования водонагревателя, порядок сдачи ключей.
- Бесконтактное заселение: код меняют после выезда; журнал передач.

### 3. Mastergrad forum — «Быстро заканчивается горячая вода» (community, thread 20.12.2024, fetched 2026-08-31)
- Thermex EQ50 **50 л**: после замены ТЭНа один человек моется **~5 минут** не очень горячей водой при слабом напоре — **второму уже не хватает** (вода еле тёплая).
- С полностью холодного бака **50 л нагревается ~1 час**.
- Температура на выходе порядка 70°C+.
- Эксперт: полностью прогретый бак 50 л при отключённом нагреве способен выдать тёплую воду **10–15 минут** для «среднестатистического душа» — если исправен забор сверху (не повреждена отводная трубка).
- Симптом «сразу кончилось» может быть не объём, а поломка трубки забора (подмес холодной снизу).

## Technical / reference sources (fetched 2026-08-31)

### Interfax-Russia — «Как выбрать бойлер…» (17.06.2026)
- Накопительный: холодная снизу, горячая сверху; термостат отключает нагрев; остывание 5–10°C/сутки.
- Большинство моделей греют до **75°C**; премиум до 80–85°C.
- Объёмы: **один человек (душ+посуда) — 30–50 л**; **двое вечером — 50–80 л**; семья 3–4 — 80–100 л.
- Правило: накопительный даёт **~2–2,5 объёма** тёплой смеси: **50 л при 60°C ≈ 90–100 л душевой воды при 38°C**.
- Уход: менять магниевый анод 1–2 года; чистка бака; проверка предохранительного клапана.

### iXBT Live — «Бойлер стоит 10 тысяч…» (2026, fetched 2026-08-31)
- Бойлер 50 л: **2–4 кВт·ч/сутки** (среднее ~3) — расход зависит от привычек; «один и тот же бак у любителей долгого душа» vs экономных отличается вдвое.
- Признаки проблем: дольше греется, шум при нагреве (накипь на ТЭНе), запах из горячего крана.

### SB.by snippet (search; page bot-blocked 31.08.2026)
- Аренда емкостного бойлера 30 л: при среднем напоре душа **~12 минут** горячей воды; **через ~30 минут** снова нагревается (не primary URL for writer — use as volume illustration only).

### SERP community_experience (research-serp.json)
- Mastergrad t324356 — быстро кончается ГВ в бойлере 50 л.
- Mastergrad t211426 — бойлер реагирует только на кран в душе (смежный симптом, не основной кейс).

## Reader problem (internal brief)
Гость командировки/рейса заселяется после 22:00, видит «бойлер есть» в объявлении, заходит в душ сразу — через 1–2 минуты холод. Бойлер 30–50 л не прогрет или последний гость слил запас; инструкция «включить / ждать 40–60 минут» спрятана в PDF или мелким шрифтом в чате.

## Reader outcome (internal brief)
Поймёт, что в посуточной квартире «бойлер есть» ≠ «горячая вода сейчас»; узнает типичные объёмы/время нагрева; поймёт, что инструкцию и статус бойлера надо получить **до** душа (заранее, не у двери); для Тюмени — что нормальный хост при позднем заезде прогревает или предупреждает.

## Brand constraints (Добрый дом)
- comfort+, спокойный тон; без «лучшие/№1/premium»
- allowed brand facts: инструкция заранее не у двери; поддержка в мессенджере; бесконтактное заселение
- forbidden: выдуманные коды, конкретные модели бойлеров в квартирах бренда без источника
- NOT legal/realtor: без ЕГРН, нотариуса, судов
- CTA writer_safe_urls from tenant-config.cta_links:
  - https://t.me/Dobriy_dom_72
  - https://max.ru/id660300569233_biz
  - https://добрыйдом-72.рф/booking/
  - https://добрыйдом-72.рф/
  - tel:+79935748322
  - manager: https://t.me/Dobriy_dom_Tyumen

## official_verifications
NOT_REQUIRED — нет тарифов банков/госорганов с точными цифрами обязательств. Цифры объёма/времени — справочные из Interfax/Mastergrad/iXBT, не «тариф компании».

## Do NOT include in output
- h2_outline, FAQ skeleton, lead paragraph, action_outline
- invented Klyshin deal or specific Tyumen apartment
- continuation of B01–B04 article prose

## Required output structure for research-notes.md
- YAML-style header fields: topic_id, slug, research_date, market
- Sections: reader_problem, reader_outcome, practical_facts, constraints, typical_errors, voice_angle, surprising_fact, official_verifications (note NOT_REQUIRED), source_table (with accessed_at 2026-08-31 for each row), writer_safe_urls
