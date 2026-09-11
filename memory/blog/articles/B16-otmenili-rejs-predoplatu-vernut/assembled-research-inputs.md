# Assembled research inputs — B16

**Return ONLY research-notes markdown in response; do NOT return DEROUTER RESEARCH BLOCKER**

Ты — Derouter utility tier. Верни полный research-notes.md. Скрипт запишет файл.

## Topic & handoff

- topic_id: B16
- slug: otmenili-rejs-predoplatu-vernut
- title_draft: «Отменили рейс. 4 200 ₽ обещали вернуть за три дня — срок вышел»
- research_date: 2026-09-11
- market: посуточная аренда, Тюмень, tenant «Добрый дом»
- format: guest-night CASE (700–1100 слов), NOT guide, NOT legal essay, NOT «N советов»
- angle: cancel_prepay — отмена поездки ДО заселения, хозяин ОТВЕТИЛ и обещал возврат, но названный срок истёк; НЕ тишина до заезда (B08)
- dzen_pattern: 2 (кейс с суммами и датами)
- lockpick_question: «Если поездка сорвётся до заселения, в какой день и каким способом вы вернёте предоплату?»
- case_numbers: 4 200 ₽ предоплаты; обещанный срок возврата — 3 дня «после проверки»; точка напряжения — четвёртый день
- wp_category_slugs (hint): posutochnaya-arenda, sovety-gostyam
- interlink siblings: B08 (prepayment silence), B06 (checkout), B04 (extra guest), B01 (code)

## Scout signal

- klyshin_hook: cancel_prepay | original: «Поездку сорвали. Предоплату обещали вернуть — сроки плывут»
- external_signal: отмена поездки + обещанный возврат предоплаты с обозначенным, но истёкшим сроком
- signal_urls:
  - https://t.me/klyshin_A
  - https://добрыйдом-72.рф/blog/
  - https://www.avito.ru/brands/dobriydomtymen/

## Anti-dup (published titles only)

Already covered: B01 code, B02 deposit, B03 vuz walk, B04 third guest, B05 reviews, B06 checkout, B07 kitchen, B08 prepayment SILENCE before keys, B09 parking, B10 taxi, B11 towels, B12 construction noise, B13 keybox, B14 neighbors music, B15 wifi desk.
B16 must NOT duplicate: silence before check-in (B08), code/keybox, deposit, hidden fees at door.

## Wordstat MCP-KV (accessed 2026-09-11, live)

| phrase | region | volume |
|--------|--------|--------|
| квартиры посуточно тюмень | 55+11176 | 4929 |
| квартиры посуточно тюмень | 225 | 10527 |
| предоплата посуточно | 225 | 913 |
| посуточно предоплата | 225 | 913 |
| вернуть предоплату за квартиру посуточно | 225 | 46 |
| отмена брони посуточно | 225 | 85 |
| отмена брони авито посуточно | 225 | 41 |
| авито квартиры посуточно тюмень | 55+11176 | 307 (top phrase) |

P0 spine: «квартиры посуточно тюмень». Узкий конфликт — возврат предоплаты при отмене до заселения.

## Fresh community / news signal (week of 2026-09-08 — 2026-09-11)

### Klyshin Telegram (accessed 2026-09-11)
URL: https://t.me/s/klyshin_A

- Hook `cancel_prepay` validated Scout 2026-09-11: «Поездку сорвали. Предоплату обещали вернуть — сроки плывут» — mechanics only, не копировать сделки/Москву/ЕГРН.
- Fresh channel activity this week: post 2026-09-10 about sellers not vacating on agreed deadline («по договорённости через две недели» → сроки плывут) — editorial parallel: обещанный срок ≠ выполненный срок; не юридический разбор.
- Post 2026-09-09 about deal chain — angle: фиксировать договорённости письменно до денег.

### iRecommend community — cancelled flight + prepayment dispute (accessed 2026-09-11)
URL: https://irecommend.ru/content/pri-otmene-broni-snimayut-komissiyu-bolee-80

- Guest cancelled because airline cancelled flight; expected partial refund per rules but platform calculated ~80% penalty; after review support refunded full amount.
- Pattern for B16: отмена из‑за сорванного рейса — уважительная бытовая причина; важно что гость сохранил переписку и добился возврата через напоминание/эскалацию, не молчал.
- NOT claim this happened in Tyumen or on Avito — только паттерн поведения гостя.

### vc.ru Приёмная — Avito prepayment hold dispute (accessed 2026-09-11)
URL: https://vc.ru/claim/2147656-avito-i-arendodatel-uderzhali-predoplatu
Published: 2025-08-09 (older; context only, NOT fresh signal)

- Guest cancelled booking before check-in; host kept full prepayment citing «штрафной период»; guest documented chat + payment.
- Writer: не цитировать как свежую новость; только как фон — платформенные «штрафные периоды» и обещания хозяина могут расходиться с ожиданием гостя.

## Official / platform sources (accessed 2026-09-11)

### Авито Журнал — онлайн-бронирование посуточно
URL: https://www.avito.ru/journal/articles/onlayn-bronirovanie-na-avito-chto-delat-v-neponyatnyh-situaciyah

Key facts for guest mechanics (NOT legal advice):
- Два типа брони: «гибкая отмена» (срок 1/3/5/7/14 дней до заезда) и «без возврата» (бесплатная отмена только 6 часов после оплаты).
- Период бесплатной отмены виден в карточке и в автосообщении чата до оплаты.
- При отмене в период бесплатной отмены: деньги отправляют сразу, на карту обычно в течение **пяти рабочих дней** (зависит от банка).
- Вне периода бесплатной отмены: звонок в поддержку 8 804 700-04-40, доказательства по причине; решение — в течение **двух рабочих дней** после документов; при одобрении возврат на карту в течение **пяти рабочих дней**.
- Арендодатель не должен уводить на оплату вне Авито — платформа не гарантирует возврат при переводе напрямую.
- Кнопка отмены: «Отменить заявку и вернуть N рублей».

### Суточно.ру — возврат при отмене (официальная справка)
URL: https://sutochno.ru/sj/vozvrat-deneg-za-bronirovaniye-kvartiry-ili-otelya
Published on page: 26 сентября 2025

- Условия отмены — в карточке объекта до оплаты; сумма компенсации считается отдельно.
- Вывод средств на баланс/карту: **от 2 до 10 рабочих дней** (на практике быстрее).
- При отмене хозяином — полный возврат на баланс гостя.
- Нестандартные ситуации — в поддержку сразу.

## Flight cancellation context (trigger for trip cancel, NOT article focus)

SERP / media (2026): с 1 марта 2026 в РФ задержка/отмена рейса более 30 минут — основание для вынужденного отказа и полного возврата билета (медиа: TripProf, Cian, Rosbalt Aug 2026). Writer: рейс — причина отмены поездки в кейсе; не уводить статью в авиаправа; достаточно «рейс отменили → поездка в Тюмень сорвалась → гость отменил бронь до заселения».

## Case facts for Writer (собирательный кейс, НЕ реальный инцидент «Доброго дома»)

- Дата: начало сентября 2026, осень.
- Гость: пара или один человек, планировал прилет в Тюмень.
- Рейс отменили → гость пишет хозяину до даты заселения, просит отменить бронь.
- Уже переведена предоплата **4 200 ₽** (одна-две ночи посуточно — сумма кейса, не «средняя по городу»).
- Хозяин отвечает (не молчит как в B08): «Вернём после проверки, в течение трёх дней».
- День 1–3: гость ждёт; день 4: срок прошёл, перевода нет или односложный ответ «ещё проверяем».
- У гостя есть: скрин отмены рейса, переписка с хозяином, чек перевода, карточка брони/объявления.
- Контраст «Добрый дом»: до оплаты в чате фиксируют сумму возврата при отмене, способ и срок; поддержка в мессенджере; бронь через официальные каналы (сайт/Avito brand), не «СБП на личную карту без условий».

## Dobry Dom tenant CTA (from tenant-config)

- https://t.me/Dobriy_dom_72
- https://max.ru/id660300569233_biz
- https://добрыйдом-72.рф/booking/
- https://t.me/Dobriy_dom_Tyumen
- +7 (993) 574-83-22

## Constraints from handoff

- Не юридическая консультация: ст. 32 ЗоЗПП, суды, Роспотребнадзор — не в центре; гостевая боль и переписка.
- Не повторять B08 (тишина до заселения).
- Не код/ключница/залог/кухня/соседи/wifi.
- Не называть хозяина мошенником.
- «После проверки» без календарной даты — красный флаг для гостя.
- Платформенные сроки (5 рабочих дней Авито) могут быть длиннее обещания хозяина «3 дня» — Writer может показать разрыв ожиданий без обещания мгновенного возврата.

## Required sections in research-notes.md

Follow B15 template: reader_problem, reader_outcome, practical_facts, constraints, typical_mistakes, guest_pain, tyumen_local, wordstat_summary, voice_angle, surprising_fact, official_verifications (N/A if no bank tariffs), source_table, writer_safe_urls.

NO h2_outline, NO lead, NO FAQ skeleton, NO action_outline.
