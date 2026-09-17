# TASK FOR DEROUTER RESEARCH (gpt-5.6-terra)

You are the Derouter utility tier synthesizing `research-notes.md`. Output ONLY the complete markdown file content (starting with `# research-notes.md`). Do NOT refuse, do NOT output BLOCKER, do NOT echo instructions. Use facts from inputs below only.

# B26 Research inputs — assembled 2026-09-17

## Topic

- topic_id: B26
- title_draft: «Заселение с 14:00. В 15:45 — мокрый пол и «ещё пять минут»»
- slug: zaselenie-s-14-00-mokryj-pol
- format: guest-night CASE (Тюмень), NOT guide, NOT legal dispute
- tenant: Добрый дом, посуточная аренда Тюмень
- research_date: 2026-09-17 (Asia/Yekaterinburg)

## Scout handoff (checkin_time_not_ready)

- klyshin_hook: checkin_time_not_ready
- original: «В карточке — заселение с 14:00. Приехали вовремя. На пороге — мокрый пол, запах химии и «ещё пять минут».»
- angle: стандартное время в карточке ≠ готовая квартира; гость с чемоданом у двери; **NOT** paid early check-in (B21)
- wordstat P0: «квартиры посуточно тюмень» 4724 (55+11176) / 10016 (225)
- supporting: «время заселения посуточно» 56 (225)
- guest intent: приехать в обещанный час заселения и войти в уже убранную квартиру, а не ждать у двери на мокром полу
- opening_direction (editorial): Гость приезжает в Тюмень на две ночи, в карточке и переписке — «заселение с 14:00». Приезжает вовремя, к 15:45 всё ещё мокрый пол, запах бытовой химии, горничная или хозяин говорит «ещё пять минут». Гость стоит с чемоданом в прихожей или на лестничной клетке. Доплату за ранний заезд не вносил — это стандартный час.
- moral: Время в карточке — не синоним готовности. До оплаты спросить, к какому часу квартира будет полностью убрана с чистым бельём, если в этот день выезд предыдущих гостей.
- lockpick_question: «К какому времени квартира будет готова, если заезд в 14:00?»
- anti_dup_guard: **B21** = платный ранний заезд, приехал в 9:10, ждал до 14:00. **B26** = приехал в стандартный 14:00, не готов к 15:45. Не повторять B23 (уборка на выезде/штраф), B18 (домофон), B13 (ключница). Не уводить в возврат денег и суд.

## Published titles overlap guard

- B21: ранний заезд оплатили, у двери с чемоданом — почти 5 часов ожидания (paid early check-in)
- B23: «уборка включена» — штраф на выезде
- B06: поздний выезд и чемоданы до поезда
- B26 unique: стандартное время заселения наступило, квартира физически не готова

## Wordstat live (MCP-KV, accessed 2026-09-17)

| phrase | volume | region |
|--------|--------|--------|
| квартиры посуточно тюмень | 4724 | 55+11176 |
| снять квартиру посуточно в тюмени | 1452 | 55+11176 |
| время заселения посуточно | 56 | 225 (totalCount only on one call — WORDSTAT PARTIAL) |
| квартиры посуточно ранний заезд | 188 | 225 (contrast: early check-in is separate intent from B26) |

## Fresh community signals (this week)

### Добрый дом Telegram @Dobriy_dom_72 — post ~2026-09-17 (fresh)

Quote:
> После дороги гость замечает не интерьер. Пыль, разводы в ванной, следы прошлого жильца — и квартира уже кажется чужой. Когда до заезда мало времени, уборка «на глаз» даёт сбой. В «Добром Доме» — чек-лист горничной из 30 пунктов: порядок действий, профессиональные методы, проверка. Не спешка, а система.
URL: https://t.me/Dobriy_dom_72
Hashtags: #Тюмень #посуточно #чистота

### Добрый дом Telegram — post ~2026-09-17 (fresh, check-in readiness)

Quote:
> Фиксация состояния квартиры при заезде — не недоверие, а нормальная защита обеих сторон. ... В «Добром Доме» состояние квартиры проверяют до заселения: чистота, комплектация, исправность техники. Если что-то требует внимания, это лучше решить сразу, а не превращать отдых или командировку в спор о деталях.
URL: https://t.me/Dobriy_dom_72

### Klyshin topic bank / Scout signal

Hook from angle bank (editorial guest case, not verified live post on 2026-09-17):
«В карточке — заселение с 14:00. Приехали вовремя. На пороге — мокрый пол, запах химии и «ещё пять минут».»
URL: https://t.me/klyshin_A
Note: Live Klyshin channel posts on 2026-09-16–17 cover real-estate law topics, not this hook — hook is from topic bank angle checkin_time_not_ready.

## Industry / platform facts (live sources 2026-09-17)

### Standard check-in window

- Tutu.ru journal (live): «Чаще всего в отель или апартаменты можно заселиться с 14:00, а выехать нужно до 12:00.» Окно 12:00–14:00 нужно для уборки; в гостиницах оно не должно быть больше трёх часов.
- Rent365.net: заезд с 14:00, выезд до 12:00; промежуток 12:00–14:00 — уборка, смена белья, проверка техники.
- Sutochno.ru listings (pattern): «Заезд после 14:00», «Выезд до 12:00» — industry default on platform cards.
- RentTools.io (2026): Airbnb default checkout 11:00, check-in 15:00 — 4-hour turnover window; same-day turnover eats almost entire window; never let guest in before cleaning finished on turnover day.

### Turnover / cleaning time

- VseUberu.ru blog (updated 2026-01-16): minimum «окно чистоты» between checkout and next check-in — **2–3 hours** for studio/1-room; **4–5 hours** for larger flats or force-majeure.
- RentTools.io: 2-bedroom same-day turnover uses full 4-hour window; offering early check-in at 12:00 on turnover day = asking cleaner to do 3-hour job in 1 hour.
- Flatinfo.ru article 2026: between guest change owner needs 2–3 hours for linen, kitchen, bathroom; if apartment not ready, owner loses that night or discounts; urgent cleaning when booking comes 3 hours before check-in.
- Sutochno.ru blog/cleaning: turnover cleaning = full cycle after checkout; when time is compressed, checklist standardization critical — «на неё отводится час или меньше».

### Guest expectations vs host duty

- T-J.ru «Причины не убираться в квартире с посуточной арендой»: guests expect hotel-like service — linen change and cleaning included in price; cleaning between guests is host duty, not guest duty.
- Otzovik review pattern (Moscow 2022): guest arrived, apartment dirty, had to mop floors herself, bed not made — mismatch at check-in.
- iRecommend / guest reviews: «квартира убрана плохо» at check-in; guests fix shower themselves.

### Wet floor / chemical smell mechanic

- Freshly mopped floor = apartment still in turnover, not ready for luggage and shoes inside.
- Cleaning chemical smell = active or just-finished cleaning; guest enters mid-process.
- «Ещё пять минут» = open-ended wait after promised check-in time already passed.
- Guest with suitcase cannot use bathroom, lie down, or unpack while standing in entryway.

### Dobry Dom tenant positioning (for voice_angle only, not as market proof)

- Channel promises: real photos, honest conditions, check-in 24/7, 5-minute response, maid checklist 30 points, apartment checked before guest arrival.
- CTA URLs from tenant-config: https://t.me/Dobriy_dom_72, https://t.me/Dobriy_dom_Tyumen, https://max.ru/id660300569233_biz, https://добрыйдом-72.рф/booking/

## Editorial case boundary

- Composite guest case for Добрый дом blog; NOT verified transcript of one Tyumen booking.
- Scenario sums (nights, ₽) if used in article = editorial only, not market tariffs.
- Center: standard 14:00 check-in time vs actual readiness at 15:45.
- Do NOT frame as consumer-law dispute; practical guest/host mechanics only.
- Explicitly NOT early check-in paid scenario (B21).

## Constraints for Writer

- Do not claim this happened in a specific Добрый дом apartment.
- Do not promise all Tyumen hosts fail at 14:00.
- Do not invent exact refund/penalty rules.
- Do not merge with B21 early-check-in paid angle.
- Wet floor alone ≠ fraud; it's incomplete turnover.
- Voice: calm host explaining why «14:00 in card» and «ready apartment» are two different questions.

## Output instructions for Derouter research role

Produce research-notes.md with sections:
research_date, reader_problem, reader_outcome, signal_and_demand, community_signal, practical_facts, editorial_case_boundary, constraints, typical_reader_mistakes, voice_angle, surprising_fact, official_verifications (N/A — no bank tariffs), source_table (accessed_at 2026-09-17 for all), writer_safe_urls.

No h2_outline, no lead paragraph, no FAQ skeleton.
