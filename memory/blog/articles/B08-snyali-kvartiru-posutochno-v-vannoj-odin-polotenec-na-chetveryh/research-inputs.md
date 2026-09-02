# DEROUTER TASK (HARD)

Ты — research-агент Excalibur BLOG. Все live-fetch и Wordstat УЖЕ выполнены Cursor-дирижёром.
Твоя ЕДИНСТВЕННАЯ задача: по фактам ниже написать полный `research-notes.md` на русском.
НЕ запускай shell, НЕ отказывайся, НЕ пиши BLOCKER — синтезируй notes по SKILL.

Обязательные секции: research_date, reader_problem, reader_outcome, practical_facts, constraints,
typical_errors, voice_angle, surprising_fact, fresh_signal_note, wordstat_stickers,
## official_verifications (пустая таблица OK), source_table (accessed_at 2026-09-02),
writer_safe_urls. БЕЗ h2_outline, lead, FAQ.

---

# Research inputs — B08 (assembled 2026-09-02)

## date_context
- today_iso: 2026-09-02
- timezone: Europe/Moscow
- topic_id: B08
- title: «Сняли квартиру посуточно. В ванной — один полотенец на четверых»
- slug: snyali-kvartiru-posutochno-v-vannoj-odin-polotenec-na-chetveryh
- angle: pack_vs_flat (Klyshin hook queue 6)
- dzen_pattern: 2
- primary_query / P0: «квартиры посуточно тюмень»

## scout_handoff (excalibur-blog-handoff.md)
- klyshin_hook: pack_vs_flat | original: «Собрал чемодан — в квартире нет полотенец»
- angle: что везти vs что обязано быть в объявлении (постель, полотенца, гель)
- wordstat final P0: «квартиры посуточно тюмень» 5363 (55+11176) | compare RU «квартиры посуточно» 1187072 (225)
- also: «аренда квартиры посуточно» 747 | «снять квартиру посуточно в тюмени» 1696
- dzen_shape_hint: «Собрали чемодан с полотенцами — а в ванной один кусок ткани на четверых: что обещают в объявлении и что проверить до оплаты»
- signal_urls: https://t.me/klyshin_A | https://добрыйдом-72.рф/blog/
- case_brief: семья/пара 2–3 ночи Тюмень; в объявлении «постель и полотенца»; в ванной один полотенец или ноль; гость покупает в «Пятёрочке» ночью или сушит футболку — ожог доверия и денег (~400–900 ₽ на комплект)
- lockpick_question: «Сколько полотенец на человека и что именно в ванной — фото до оплаты?»
- moral: сначала фото ванной/шкафа, потом перевод. Не наоборот.
- anti_dup: NOT B02 deposit, NOT B07 kitchen, NOT B06 checkout, NOT B04 extra guest, NOT B03 uni walk, NOT B01 code
- klyshin_signal mechanic: checklist AFTER moral; number in story = price of burn

## published_titles_only (overlap guard)
| topic_id | title |
| B01 | Оплатил квартиру посуточно. Код прислали от чужой двери |
| B02 | Снял квартиру посуточно. Залог не вернули — нашли скол на плите |
| B03 | Привезли сына к вузу — «рядом» оказалось 40 минут пешком |
| B04 | Оплатили за двоих. У двери попросили доплату за третьего |
| B05 | Рейтинг 4,8. Два «всё супер» — и 3 900 ₽ под вопросом |
| B06 | Выезд в полдень. Поезд через 4 часа — чемоданы у подъезда |
| B07 | Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽ |

B08 = amenities/packing angle; NOT door/code/deposit/kitchen/checkout/rating duplicate.

## dzen_content_rules (constraints)
- RF law; no Meta/IG heroes; no VPN how-to; no clickbait H1; no mat
- CTA channels allowed: Telegram, VK, Дзен, MAX, tenant links
- tenant cta_links: https://t.me/Dobriy_dom_72 | https://t.me/Dobriy_dom_Tyumen | https://max.ru/id660300569233_biz | https://добрыйдом-72.рф/booking/ | tel:+79935748322

## wordstat (mcp-kv, accessed 2026-09-02)

### Tyumen regions 55+11176
| phrase | totalCount | top related |
| посуточно | 25041 | квартиры посуточно 17127; посуточно тюмень 7757; квартиры посуточно тюмень 5363 |
| полотенца | 9690 | полотенце купить 661; полотенца тюмень 290; полотенце для ванной 271; 2 полотенца 243 |
| что взять | 11878 | что нужно взять с собой 461; что взять в дорогу 349 (generic, not rental-specific) |
| аренда квартиры посуточно | 747 | аренда квартир посуточно тюмень 188; договор посуточной аренды 44 |

### Compare RU 225
| phrase | totalCount |
| квартиры посуточно тюмень | 11916 |
| снять квартиру посуточно в тюмени | 4290 |

### Scout P0 confirmation
- final P0: «квартиры посуточно тюмень» — 5363 (55+11176) / 11916 (225)

## fresh_signal (week of 2026-09-02)

### 1. Klyshin Telegram @klyshin_A (accessed 2026-09-02)
- URL: https://t.me/s/klyshin_A
- Channel: юрист по недвижимости, ~61k subs
- pack_vs_flat hook from topic bank queue 6: «Собрал чемодан — в квартире нет полотенец»; klyshin_signal = checklist AFTER moral
- Fresh posts visible in feed (Sep 2026): recurring mechanic «сначала проверка/документы/порядок — потом деньги/договор» (e.g. post «Расписку написали, а денег нет» — порядок действий; «10 документов после покупки»)
- NOT direct towel case; angle = verification checklist before payment applies to amenities

### 2. Суточно.ру live reviews feed (accessed 2026-09-02)
- URL: https://sutochno.ru/votes
- Fresh review pattern (no date on page, live feed): «Количество гигиенических наборов не соответствовало числу проживающих, долго искали губку для посуды, кухонное полотенце и тряпку для стола. Небольшие замечания к качеству уборки.»
- Positive counterexamples in same feed: hosts praised for «постельное, полотенца — чистое», «полотенца, гель, шампунь, фен»

### 3. Rutube community video (Aug 2026, ~20 days before 2026-09-02)
- URL: https://rutube.ru/video/4cb5af9f74000d55aa42121bf46ef24a/
- Title: «Сняли посуточно КВАРТИРУ на Авито: сюрпризы на КАЖДОМ ШАГУ»
- Published ~13 Aug 2026; self-check-in via mailbox; surprises after arrival
- NOT towel-specific but confirms gap between listing and reality on arrival

### 4. Добрый дом blog (tenant, Tyumen)
- URL: https://добрыйдом-72.рф/blog/
- Tyumen посуточная аренда operator; blog lists case-style articles (e.g. B07 kitchen case on blog index)
- Signal context: local operator documents guest pain scenarios

## serp_highlights (research-serp.json, searched 2026-09-02)
- Rutube/VK videos «сюрпризы посуточно» Aug–Jul 2026
- pravoved.ru: guests discover problems after paying full sum upfront
- woman.ru threads blocked from cloud fetch (captcha)
- community: short-term rental surprise stories dominate SERP, not legal guides on towels

## deep_research_facts

### Legal / norm (NOT mandatory towel law)
- ГК РФ ст. 683 — посуточный найм; конкретный перечень полотенец законом для частников НЕ закреплён
- РБК Недвижимость (industry norm, realty.rbc.ru): для посуточной сдачи «базовые вещи» включают постельное бельё, полотенца, шампунь, гель, тапочки — рыночный стандарт сервиса, не судебная обязанность
- bezriskoff.ru / договор: смена белья и полотенец — по договору между хозяином и гостем
- tiktur.ru (2026-07-07): в частных апартаментах наличие белья/полотенец «почти всегда указано отдельно» в удобствах; если галочка стоит — можно рассчитывать; качество отдельный вопрос; совет: спросить за сутки до заезда «сколько комплектов белья и полотенец»; запросить фото шкафов/ванной; закрепить в переписке («для четырёх гостей — четыре полотенца»)
- tiktur.ru also claims textile «в абсолютном большинстве случаев не входит» for private rent — CONFLICTS with modern aggregator listings; Writer: present as market split (hotel-type vs bare flat), not universal rule

### Industry standard (hosts)
- RealtyCalendar blog (napolnenie-kvartiry-dlya-posutochnoj-arendy): на каждое спальное место — 3 комплекта белья (застелен / стирка / резерв); расходники: мыло с дозатором vs индивидуальные шампунь/гель на сутки; «самое грязное — ручки и дозаторы»
- Kvartirka/Penza example: в стоимость 1 комплект белья + 2 полотенца; доп. комплект +400 ₽
- Kvartirka/Moscow: 2 полотенца на гостя в базе; доп. комплект 400 ₽
- Kvartirka/Kislovodsk: на двоих — 1 комплект белья и 4 полотенца в базе; доп. бельё 500 ₽
- Tyumen listing mirkupit.ru: «2 комплекта полотенец», мыло, гели; 1 комплект постельного в цене; смена белья каждые 5 дней; доп. комплект белья 200 ₽

### Guest experience / community
- t-j.ru/daily-rent-flat: риск «свежесть постельного белья» при частниках; автор берёт полотенца/бельё в багаж «на всякий случай» — пригодилось 1 раз (не успели высохнуть), не из-за отсутствия
- t-j comment (host SPb): гости ценят тапочки, гель, шампунь, кондиционер, ватные диски, порошок — «бесплатные фишки»
- vc.ru Sochi 2026: checklist «своё постельное и полотенца» + губки/моющее «в квартире может не быть ничего»
- sutochno review: mismatch гигиенических наборов vs число гостей; missing kitchen towel

### Scout case economics (ANCHOR — not verified receipt)
- ~400–900 ₽ emergency комплект полотенец для 4 чел. ночью в магазине
- Market bracket: набор махровых полотенец от ~350–650 ₽ (опт/производитель natasha-tekstil.ru); розница варьирует; Пятёрочка — каталог без фикс. цены в fetch; Scout anchor = вилка, не чек

### Tyumen listings pattern (kvartirka.com, accessed 2026-09-02)
- Multiple Tyumen apartments list amenity «Полотенца, постельное белье» as checkbox
- Descriptions: «свежие полотенца для каждого гостя», «хлопковое постельное бельё»
- Gap: checkbox ≠ count per guest; объявление не всегда указывает N полотенец на человека

### pravoved.ru case (2025-07-20, illustrative)
- Paid full sum upfront without seeing flat; wanted to leave first night — refund dispute
- Pattern: prepayment before visual check amplifies amenity disappointment

## constraints_for_writer
- No bank/gov tariff claims → official_verifications empty; official_source_audit required=false
- 400–900 ₽ = Scout composite anchor (вилка покупки), не верифицированный чек Тюмени
- Klyshin posts = verification-order analogy, not towel court precedent
- tiktur «бельё не входит» vs aggregator norms — present both sides
- Do NOT copy B07 kitchen/café math; towels are separate pain
- Instagram SERP hits — RF-blocked; do not use as hero/CTA
- woman.ru — blocked; do not cite as accessed source

## voice_angle_hints
- Klyshin rhythm: moral first (фото ванной до оплаты), number = burn (цена ночного похода в магазин)
- Tyumen local: квартиры посуточно тюмень P0; ночной «Пятёрочка»/«Магнит» как реалистичный сценарий (магазины 24h в городе есть, но ассортимент текстиля ограничен)
- surprising_fact candidate: галочка «полотенца» в объявлении не указывает количество; industry norm для хостов — 2–3 полотенца на гостя, но это не закон

## writer_safe_urls
- https://t.me/Dobriy_dom_72
- https://t.me/Dobriy_dom_Tyumen
- https://max.ru/id660300569233_biz
- https://добрыйдом-72.рф/booking/
- https://добрыйдом-72.рф/
- https://tiktur.ru/nuzhno-li-brat-s-soboj-polotentsa-i-postelnoe-v-arenduemoe-zhile/
- https://new.realtycalendar.ru/blog/napolnenie-kvartiry-dlya-posutochnoj-arendy
- https://t-j.ru/daily-rent-flat/
- https://sutochno.ru/votes
- https://mirkupit.ru/tyumen/arenda-1-komnatnih-posutochno/1-komnat_1182160

## derouter_task
Synthesize research-notes.md per excalibur-research SKILL:
- research_date: 2026-09-02
- reader_problem / reader_outcome (internal, one pain)
- practical_facts, constraints, voice_angle, surprising_fact
- source_table with accessed_at 2026-09-02
- official_verifications (empty table OK)
- writer_safe_urls
- NO h2_outline, NO lead, NO FAQ skeleton
