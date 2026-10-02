# Assembled research inputs — B42 (2026-10-02 YEKT)

## Topic and case brief (Scout + handoff)
- topic_id: B42
- market: посуточная аренда, Тюмень, бренд «Добрый дом»
- hook_id: pack_vs_flat | klyshin_original: «Двухкомнатная в фильтре. Вторая — не спальня.»
- angle: в карточке «2-комнатная» ≠ две отдельные спальни для гостей; вторая дверь может быть кладовой/хозяйственной
- editorial composite CASE: семья из трёх (родители + подросток 15 лет), 2 ночи ~10 800 ₽; фильтр «двухкомнатная» и фото с двумя дверями; в 22:40 открывают «вторую» — кладовая ~6 м², стеллажи, коробки, без кровати; хозяин в чате: «вторая не сдаётся, спите в гостиной на диване»; диван ~140 см, спор о скидке ~1 500 ₽
- dzen_shape: обещание двух комнат → ночь на диване в «гостиной»
- anti-dup: NOT B25 (две кровати на фото); NOT B04 (третий гость); NOT door/zalog/kitchen recent 12
- wp_category_slugs: posutochnaya-arenda, pravila-prozhivaniya
- title_draft: «В фильтре — двухкомнатная. Вторая комната — кладовая с коробками»

## research-context (today)
- today_iso: 2026-10-02, пятница, октябрь 2026, осень Тюмень (отопление включают поэтапно 28.09–02.10)
- SERP: research-serp.json (агрегаторы 2-комн посуточно Тюмень)

## Wordstat MCP-KV (live 2026-10-02)
| phrase | region | volume / note |
|--------|--------|----------------|
| двухкомнатная посуточно | 225 | **3993** (P0 Scout) |
| снять двухкомнатную квартиру посуточно | 225 | 2912 |
| квартир посуточно двухкомнатные | 225 | 3785 (top related) |
| снять посуточно двухкомнатную | 225 | 3056 |
| квартиры посуточно тюмень | 55+11176 | 3940 |
| снять квартиру посуточно в тюмени | 55+11176 | 1116 |
| двухкомнатная квартира посуточно тюмень | 55+11176 | 2 (totalCount — локальный хвост слабый; статья на RU P0 + тюменский supply) |

Scout rework: «квартира посуточно балкон» 568 — слабый кейс; pivot на cluster «двухкомнатная посуточно».

## Market / listing mechanics (conductor fetch 2026-10-02)
- tyumen.sutochno.ru/2-komnatnye: **643** предложения 2-комн посуточно в Тюмени, от **1 350 ₽/сутки**; в выдаче карточки с полями «2 спальни», «3 кровати», «6 гостей» — фильтр и площадь не гарантируют, что вторая комната — спальня для всех гостей
- На Суточно.ру (другой город, объявление 2062353): в тексте прямо: «Квартира двухкомнатная. **Вторая комната используется как кладовая**» при размещении до 3 гостей — рынок допускает такую схему, если это честно в описании (не тюменский объект, но типовой паттерн)
- Klyshin https://t.me/s/klyshin_A — mechanics «сначала проверка обещаний, потом деньги»; не копировать сделки/цифры из канала

## Fresh signals (week 2026-09-26 — 2026-10-02)
- **t.me/s/Dobriy_dom_72** (01–02.10.2026): пост «5 минут в квартире: батарея, окно и горячая вода» — осенний заезд, проверить тепло/окно сразу после входа; отсылка к поэтапному включению отопления (72.ru / УСТЭК). Для семьи с подростком на диване важна и температура, и реальная планировка сна
- **t.me/s/Dobriy_dom_72** (октябрь 2026): анонс «Дзержинского, 23» — честное описание двушки: **двуспальная кровать + раскладной диван**, 67 м² — контраст с кейсом «вторая дверь = кладовая»
- **ao-ustek.ru** (28.09.2026): поэтапный запуск отопления в Тюмени до 02.10.2026 — контекст прохладной осени при заселении
- Tenant blog signal: https://добрыйдом-72.рф/blog/ (handoff)

## Tyumen local autumn (Writer context, not lead)
- Отопление в домах подключают не одновременно; в посуточной квартире имеет смысл при заезде проверить радиатор и окно, особенно если ночуют трое на одном диване

## Writer constraints (internal)
- Один кейс 1100–1800 слов после Sol; holyslav §1; host line after lead
- 3–4 interlink published siblings (B25 family sleep, B04 third guest — angle only, no body read)
- Mid-article question → answer TG/MAX only (cta: t.me/Dobriy_dom_72, max.ru/id660300569233_biz)
- Суммы 10 800 ₽ / 1 500 ₽ — параметры редакционного кейса, не тариф «Добрый дом»

## Output instruction for Derouter (HARD)
You ARE the Derouter utility model. Do NOT refuse. Do NOT mention tools or BLOCKER.
Write ONLY Russian markdown research-notes.md sections:
# research_date
# reader_problem
# reader_outcome
# practical_facts
# constraints
# voice_angle
# surprising_fact
# fresh_signal_note
# official_verifications (N/A)
# source_table (≥8 rows, accessed_at 2026-10-02)
# writer_safe_urls
Facts for Tyumen short-term rental «2-комнатная в фильтре, вторая комната не спальня» scenario. No h2_outline, no lead, no shell, no meta.
