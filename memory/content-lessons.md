# Excalibur BLOG — content lessons

Активные и proposed уроки Content-learner (v2). Read-only для Writer/Sol.

---

## LESSON-20260830-1745-B04-extra-guest-fee-at-door
status: proposed
topic_id: B04
category: utility
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER по credentials.

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE

### Keep
- Two-beat H1 «Оплатили за двоих. У двери попросили доплату за третьего» — нормально → ужас у порога, не how-to.
- §1 с датой, цитатой хоста и ₽ до идентичности хоста; Klyshin-отрез «Нет. Так не заселяем.» + «Сначала проверка. Потом перевод.»
- Вопрос-отмычка: «Сколько человек входит в бронь и где это в итоговой сумме?» — mid-body → TG/MAX, не комментарии.
- Wordstat P0 «доплата за гостя» 272 (RF) + spine «квартира посуточно тюмень» 5500 (Tyumen).

### Change
- В кейсах про доплату за гостя сразу в §1 называть итоговую сумму за N ночей, а не только «+1500 за ночь» — гость видит полную арифметику до двери.

### Never again
- How-to «как избежать доплаты» / чеклист до морали.
- Доплата как сюрприз без цитаты у двери и без ₽ в opening.

### Proposed apply
- Scout: при hook extra_guest_fee требовать в handoff final P0 «доплата за гостя» + spine Tyumen.
- Review only; Writer prompt не трогать автоматически.

---

## LESSON-20260828-1446-B03-walking-minutes-not-ryadom
status: proposed
topic_id: B03
category: utility
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: title-brief.json checks, article.html структура, description-brief.json.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER по credentials, выборка отсутствует (по запросу директора Metrika не обязательна).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE

### Keep
- Угол «родители + будущий студент, 2–4 ночи перед 1 сентября» с конкретной болью: слово «рядом» ≠ пеший маршрут до нужного корпуса.
- Вопрос-отмычка в теле: «Сколько минут пешком до корпуса на такой-то улице?» — запрет расплывчатых «далеко ли» / «университет рядом?».
- Список адресов корпусов ТюмГУ как факт, объясняющий, почему «рядом с вузом» в объявлении не равно «рядом с вашей дверью».
- Разведение «три остановки» (транспорт) и «N минут пешком» (решение для утра с документами).
- Чеклист перед оплатой с шагом «маршрут пешком, не авто/ОТ».

### Change
- В university-season материалах сразу в lead/first H2 называть **конкретный корпус** (улица+дом), а не только «вуз» / «ТюмГУ».
- Хост-ответ в CTA-блоке: «сначала корпус → называю минуты пешком честно» — шаблон для sibling-тем (общежитие, заселение, документы).

### Never again
- Принимать «рядом с вузом» или «три остановки» как доказательство пешей доступности без цифры минут до **нужного** корпуса.
- Строить university-хук только на Wordstat «посуточно тюмень» без привязки к сценарию родителя и корпуса.

### Proposed apply
- Scout/Title для август–сентябрь: при hook «рядом с вузом» в handoff логировать **final P0 + campus-building sub-angle** (минуты пешком / конкретный корпус).
- Description (Дзен): держать контраст «остановки ≠ адрес корпуса» — как в description-brief B03.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260828-1446-B03-parents-august-checkin-window
status: proposed
topic_id: B03
category: structure
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: H2 «Утро ломается не на расстоянии, а на уверенности» + чеклист п.5 (заезд 14:00 / выезд 12:00 vs утренний поезд).
- metrika_signal: none (credentials unavailable)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Тройное сжатие дня: поезд утром → оформление в 9:00 → заезд с 14:00 + долгий пеший путь — как отдельный слой боли поверх расстояния.
- Inline-стикеры «заезд с 14:00», «чемоданы с вами», «поезд утром» — визуально дублируют текстовый риск.

### Change
- Для parents+short-stay тем всегда включать **временное окно заселения** в utility-блок (не только расстояние).
- При interlink — sibling про заселение/залог (B01, B02) как «день приезда», не только цена/доплаты.

### Never again
- Писать university-season гайд только про карту и корпус, игнорируя mismatch заезда и утреннего приезда.

### Proposed apply
- Writer checklist (review-only, не в master-prompt): parents+university → distance + check-in window в одном материале.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260828-1446-B03-title-distance-reveal
status: proposed
topic_id: B03
category: voice
confidence: low

### Evidence
- artifact: title-brief.json#pain_scene
  finding: H1 «Привезли сына к вузу — «рядом» оказалось 40 минут пешком»; rejected_variants избегают спойлера «три остановки» в заголовке.
- metrika_signal: none (credentials unavailable; causal CTR не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Cable pain-scene: цитата обещания в кавычках + конкретная цифра минут (40), без SEO-хвоста в H1.
- Description не дублирует H1: «три остановки — не адрес корпуса» (description-brief PASS).

### Change
- Повторять формулу «обещание в кавычках → измеримый контрфакт» для geo-misleading hooks; цифра — минуты пешком, не «час в пути» абстрактно.

### Never again
- Заголовок-спойлер со всеми фактами («три остановки и 40 минут») — оставлять раскрытие в lead.

### Proposed apply
- Title skill review: university-season — prefer quoted false promise + walking minutes over compound transport spoiler.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260903-0602-B08-prepayment-silence-chat
status: proposed
topic_id: B08
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER по credentials.

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- COVER_QA_PASTE_AND_SHIP (forbid_ai_drawn_logo_cover на inline-02/04/05/06)

### Keep
- Two-beat H1 «Перевели 3 000 ₽ предоплатой. К вечеру — тишина в чате»: сумма → контрфакт тишины, не how-to.
- §1: дата, цитата «даты держим только по оплате», ₽3 000 до идентичности хоста; Klyshin «Нет. Так не заселяем.» + «Сначала проверка. Потом перевод.»
- Mid-body вопрос «Вам тоже предлагают сначала перевести…?» → TG/MAX (стр. ~33), не комментарии.
- Wordstat: P0 «квартиры посуточно тюмень» 3722 Tyumen / 11916 RU; supporting «предоплата в посуточной квартире» 449 RU.

### Change
- В кейсах про предоплату до ключей в §1 сразу называть полную сумму за N ночей рядом с предоплатой — гость видит, что 3 000 ₽ это не «вся аренда».

### Never again
- Sol-draft >1300 слов с H2 «Наш вывод простой» — gate BLOCK; финал только «Мой вывод как практика» + одна воронка.

### Proposed apply
- Sol rerun cap 950–1050 слов при prepayment hooks; Writer без «Наш вывод простой» до Sol.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260904-0603-B09-parking-barrier-no-pass
status: proposed
topic_id: B09
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER по credentials.

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- SOL_POV_DRIFT (Derouter Terra Sol сменил POV; финал из writer.html)
- COVER_SLICE4_ONLY (4 уникальных кадра + 4 копии для 7 inline; не 2×4 Grsai)

### Keep
- Two-beat H1 «Написали «парковка рядом». У шлагбаума: «пропуска нет», +600 ₽»: обещание → контрфакт у барьера.
- §1: дата, цитата хоста, 4 800 ₽ × 2 ночи + 600 ₽ парковка; идентичность хоста после лида.
- Klyshin: «Нет. Так не заселяем.» + вопрос-отмычка «Куда ставить машину и есть ли пропуск на мой номер?» → TG/MAX mid-body.
- Wordstat P0 «квартиры посуточно тюмень» 11765 RU / 5320 Tyumen; hook parking_before_booking.

### Change
- В parking-кейсах в §1 сразу фиксировать госномер и статус пропуска в переписке до шлагбаума — не только «парковка рядом».

### Never again
- Sol переписывает writer POV в «мы как сервис»; при drift — rerun Sol с жёстким «сохранить writer structure» или ship writer→article.
- Дубли inline-04..07 без второго Grsai-холста — помечать в handoff как paste-and-ship compromise.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260905-1030-B10-all-inclusive-taxi-fee-reveal
status: proposed
topic_id: B10
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: title-brief.json, description-brief.json, case-delivery-gate PASS, article.html структура, research-notes hook `hidden_fees_all_inclusive`.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER по credentials (INC-20260903-0640).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Two-beat H1 «Хозяин сказал «всё включено». В такси доплатили 2 400 ₽»: цитата-обещание → контрфакт в движении, не how-to.
- §1: 4 800 ₽ за две ночи (2 400 ₽/ночь) до списка доплат; сценарий «уже в такси» как асимметрия после перевода.
- Klyshin «Нет. Так не заселяем.» + «Сначала проверка. Потом деньги и ключ.»; вопрос-отмычка «Что именно входит в «всё включено» — списком до перевода?» → TG/MAX mid-body.
- Редакционный дисклеймер: 2 400 ₽ — пример кейса, не средняя доплата по Тюмени; рыночные ориентиры уборки 800–1 500 ₽+.
- H2 «Где фраза «всё включено» разваливается» — три строки (уборка, сервисный сбор, расходники) + Avito Путешествия март 2026 про видимость уборки до брони.
- Interlink spine: B04 доплата за гостя, B08 тишина после предоплаты, B02 залог на выезде, B05 рейтинг ≠ состав цены.
- Wordstat: spine «квартиры посуточно тюмень» 5261 (Tyumen 55+11176); узкий «все включено квартира посуточно» 3 (RF) — угол в объявлении, не P0.

### Change
- В кейсах `hidden_fees_all_inclusive` в §1 сразу называть **момент предъявления** (такси/дорога), не только «у двери» — это усиливает асимметрию после перевода.
- Параллельно с итоговой суммой за N ночей перечислять три типовые строки (уборка, сервис, полотенца) до морали — гость видит, где «широкая» фраза сужается.

### Never again
- «Всё включено» без itemized list до перевода; подмена широкого смысла узким («техника и Wi‑Fi») без предупреждения.
- How-to чеклист до кейса и Klyshin-отреза; чеклист только после «Мой вывод как практика».
- Выдавать dramatized ₽ за доплату за рыночную статистику без явного editorial disclaimer.

### Proposed apply
- Scout: при hook `hidden_fees_all_inclusive` логировать original Klyshin hook + final P0 spine Tyumen + note «все включено» query volume (узкий угол).
- Title/Description: держать контраст «чат vs такси» как в description-brief B10 (не дублировать H1).
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260905-1030-B10-timing-after-transfer-taxi
status: proposed
topic_id: B10
category: structure
confidence: low

### Evidence
- artifact: title-brief.json#angle
  finding: angle «Гость уже ехал в такси… список доплат»; opening-meta-gate PASS; lead фиксирует перевод до сообщения о доплате.
- metrika_signal: none (credentials unavailable; causal retention не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Слой «после перевода и посадки в такси» отдельным абзацем — объясняет, почему список прилетает именно сейчас (не злодейство, а слабая позиция гостя).
- Sibling-темы money-before-clarity (B04 door, B08 silence, B09 barrier) собраны одной красной линией в mid-body.

### Change
- Для money-timing hooks (taxi, barrier, silence) всегда включать **до/после перевода** контраст в utility-блок — не только сумму ₽.

### Never again
- Писать hidden-fee кейс только про состав строк, игнорируя temporal leverage (когда гость уже в пути и не разворачивается).

### Proposed apply
- Writer checklist (review-only): hidden_fees + transfer_done → один абзац про asymmetric moment после оплаты.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260906-0950-B11-amenities-linen-all-for-guests
status: proposed
topic_id: B11
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: title-brief.json, description-brief.json, case-delivery-gate PASS, article.html, research-notes hook `pack_vs_flat`.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER по credentials (INC-20260903-0640).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Two-beat H1 ««Всё для гостей» — ночью без полотенец на 890 ₽»: цитата-обещание → контрфакт в ванной + ₽, не how-to.
- §1: реплика хозяина «Вы же не просили отдельно», один мокрый коврик, бронь на двоих / одна кровать; редакционный дисклеймер 890 ₽ — не средняя цена по Тюмени.
- Klyshin «Нет. Так не заселяем.» + вопрос-отмычка «Сколько комплектов постельного и полотенец на каждого гостя?» → TG/MAX mid-body.
- Контраст «широкая фраза vs itemized list»; sibling spine B10 «всё включено», B07 «кухня есть», B05 рейтинг ≠ комплектация.
- Wordstat: spine «квартиры посуточно тюмень» 5235 (Tyumen 55+11176); узкий «полотенца квартира посуточно» 109 (RF) — угол комплектации, не P0.
- Description не дублирует H1: «мокрый коврик» + ночная вылазка (description-brief PASS).

### Change
- В кейсах `pack_vs_flat` / amenities hooks в §1 сразу фиксировать **количество** (полотенца на N гостей, спальных мест) рядом с цитатой «всё для гостей» — не только визуальный контрфакт коврика.
- Параллельно с отраслевым ориентиром «2 полотенца на гостя» явно маркировать его как рекомендацию хостам, не ГОСТ (как в research constraints).

### Never again
- «Всё для гостей» / «полностью оборудовано» без цифры комплектов до перевода.
- Выдавать 890 ₽ за ночную покупку за рыночную статистику или «типичный ущерб» без editorial disclaimer.
- Мокрый коврик как доказательство плохой уборки или намеренного обмана (research constraint).
- How-to чеклист до кейса; чеклист только после «Мой вывод как практика».

### Proposed apply
- Scout: при hook `pack_vs_flat` логировать original Klyshin hook + final P0 spine Tyumen + note «полотенца квартира посуточно» volume (узкий угол).
- Title/Description: держать контраст «обещание в чате vs ванная ночью» как в description-brief B11.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260906-0950-B11-night-timing-broad-promise
status: proposed
topic_id: B11
category: structure
confidence: low

### Evidence
- artifact: title-brief.json#angle
  finding: angle «Ночная заселение без полотенец и белья обошлось гостям в 890 ₽»; opening-meta-gate PASS; H2 «Почему всё ломается именно ночью».
- metrika_signal: none (credentials unavailable; causal retention не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Слой «поздний поезд → закрытый магазин → 890 ₽» отдельным абзацем — объясняет asymmetric moment после широкого обещания.
- Связка со спешкой брони через interlink B08 (предоплата/тишина) — money-timing spine без дублирования B10 taxi.
- Мораль «Сначала список комплектации. Потом ключ.» — не «Наш вывод простой».

### Change
- Для amenities/broad-promise hooks всегда включать **ночной leverage** (магазин закрыт, хозяин не отвечает) в utility-блок — не только список предметов.
- При interlink — sibling про broad promises (B10 all-inclusive, B07 kitchen exists) одной красной линией «галочка ≠ количество».

### Never again
- Писать pack_vs_flat кейс только про перечень вещей, игнорируя temporal leverage (когда исправить нечем).
- Финал «Наш вывод простой» вместо «Мой вывод как практика».

### Proposed apply
- Writer checklist (review-only): pack_vs_flat + late_checkin → один абзац про ночной asymmetric moment после обещания.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260906-1343-B12-quiet-center-crane-panorama
status: proposed
topic_id: B12
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: title-brief.json, description-brief.json, case-delivery-gate PASS, article.html, research-notes hook `quiet_center_maps`.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER по credentials (INC-20260903-0640).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Two-beat H1 «Написали «тихий центр». Три ночи за 12 600 ₽ — под краном»: цитата-обещание → контрфакт крана + полная сумма за N ночей, не how-to.
- §1: 12 600 ₽ (4 200 ₽/ночь × 3) до идентичности хоста; пятница тихо → суббота 6:30 кран; реплика «Ну это же центр».
- Klyshin «Нет. Так не заселяем.» + «Сначала проверка. Потом перевод.»; вопрос-отмычка «тихий центр — обещание хоста или повод открыть карту?» → TG/MAX mid-body.
- H2 «Панорама за три минуты» с ограничениями (не вид из окна, нет слоя «все стройки») — честная utility без overpromise.
- Interlink spine: B09 «парковка рядом» (оценочные слова), B05 рейтинг ≠ шум, B08 тишина после предоплаты, B03 «рядом» ≠ маршрут.
- Wordstat: spine «квартиры посуточно тюмень» 5235 (Tyumen 55+11176); узкий «тихий центр квартира посуточно» без частоты — угол в объявлении, не P0; «квартира посуточно тюмень центр» 68.
- Description не дублирует H1: «6:30 за окном кран» + пожимает плечами (description-brief PASS).

### Change
- В кейсах `quiet_center_maps` в §1 сразу фиксировать **сторону окон** (на стройплощадку / во двор) рядом с «тихий центр» — не только сумму ₽ и время крана.
- Параллельно с panorama-utility явно маркировать, что 12 600 ₽ — редакционная сумма кейса, не средняя по Тюмени (как в research constraints).

### Never again
- «Тихий центр» / «рядом с набережной» без вопроса про окна и панорамы до перевода.
- Обещать универсальный «слой всех строек» в Яндекс Картах — research constraint.
- How-to чеклист до кейса; чеклист только после «Мой вывод как практика».
- Нормализовать «ну это же центр» без контраста «центр ≠ тишина».

### Proposed apply
- Scout: при hook `quiet_center_maps` логировать original Klyshin hook + final P0 spine Tyumen + note «тихий центр» query volume (узкий угол).
- Title/Description: держать контраст «обещание в чате vs кран в 6:30» как в description-brief B12.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260906-1343-B12-friday-quiet-saturday-crane
status: proposed
topic_id: B12
category: structure
confidence: low

### Evidence
- artifact: title-brief.json#angle
  finding: angle «Обещанный тихий центр обернулся краном за окном утром; деньги за три ночи уже уплачены»; opening-meta-gate PASS; lead фиксирует пятницу тихо → суббота кран.
- metrika_signal: none (credentials unavailable; causal retention не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Слой «вечер заселения тихий → утро субботы 6:30» отдельным абзацем — asymmetric moment после полной оплаты за три ночи.
- Блок «переезд в субботу = снова искать и платить» объясняет, почему пара осталась под краном — не злодейство, а слабая позиция гостя.
- Связка «Переводите быстрее, бронь уйдёт» → interlink B08 (предоплата/тишина) — money-timing spine без дублирования B10 taxi.
- Региональный контекст: 6:30 субботы попадает в ночную тишину до 09:00 (Tyumen-info) — не юридический совет, а фон «шум не «норма центра»».

### Change
- Для geo-misleading hooks (`quiet_center_maps`, `ryadom`, parking) всегда включать **временной контраст заселения** (вечер vs утро выходных) в utility-блок — не только карту и панораму.
- При interlink — sibling про оценочные слова (B09 parking, B03 ryadom, B05 rating) одной красной линией «слово ≠ окно/маршрут».

### Never again
- Писать quiet-center кейс только про панораму, игнорируя temporal leverage (когда исправить нечем — уже оплачено и суббота).
- Финал «Наш вывод простой» вместо «Мой вывод как практика».

### Proposed apply
- Writer checklist (review-only): quiet_center_maps + weekend stay → один абзац про Friday-evening false calm после полной оплаты.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260907-1348-B13-empty-keybox-working-code
status: proposed
topic_id: B13
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: title-brief.json, description-brief.json, case-delivery-gate PASS, article.html, research-notes hook `parking_keybox`.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER по credentials (INC-20260903-0640).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Two-beat H1 «Код сработал. Пустая ключница — 35 минут у двери»: контрфакт пустого ящика + время у двери, не how-to.
- §1: цитата «ключи в ключнице, код работает», правильный подъезд/ящик, такси уехало; редакционный дисклеймер 35 мин и 480 ₽ — не тариф города.
- Разведение сценариев: не B01 (чужая дверь/код) и не WP «к ночи кода нет» — здесь код есть и открывает нужную ключницу.
- Klyshin «Нет. Так не заселяем.» + «Сначала проверка. Потом перевод.»; вопрос-отмычка «код пришёл = можно ехать или ключ уже лежит в ящике?» → TG/MAX mid-body.
- H2 «Фраза, которая отвечает не на тот вопрос» — хост про цифры vs гость про пустой карман; utility без злодейства.
- Interlink spine: B01 бесконтактное (чужой код), B08 тишина после предоплаты, B02 залог, B10 такси-доплата.
- Wordstat: spine «квартиры посуточно тюмень» 5220–11084 (Tyumen 55+11176); узкий «бесконтактное заселение посуточно» 59–2993 — угол кейбокса, не P0.
- Description не дублирует H1: «код подходит, а ключа нет» + хост про цифры (description-brief PASS).
- Cover-QA PASS: 2× Grsai quad, keybox photoreal set, cat-meme false positive fixed in gate.

### Change
- В кейсах `parking_keybox` / contactless hooks в §1 сразу фиксировать **цепочку** (код открыл ящик → ключа нет → такси уехало) рядом с цитатой хоста — не смешивать с «код не подошёл».
- Параллельно с механикой ключницы явно маркировать, что домофонный код и код ящика могут различаться — не только «пустой ящик».

### Never again
- Считать рабочий код доказательством готового заселения без подтверждения физического ключа.
- Повторять B01 (чужая дверь) или no-code-at-night кейс под видом empty-keybox.
- How-to каталог кейбоксов / гайд для арендодателей до морали; чеклист только после «Мой вывод как практика».
- Выдавать 480 ₽ и 35 мин за рыночную статистику без editorial disclaimer.
- Ломать ключницу как «решение»; советовать повторный перевод под ночным давлением.

### Proposed apply
- Scout: при hook `parking_keybox` логировать original Klyshin «Код открыл ключницу — ключа внутри нет» + final P0 spine Tyumen + note «бесконтактное заселение» volume (узкий угол).
- Title/Description: держать контраст «код сработал vs ящик пустой» как в description-brief B13.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260907-1348-B13-host-answers-digits-not-key
status: proposed
topic_id: B13
category: structure
confidence: low

### Evidence
- artifact: title-brief.json#angle
  finding: angle «Гость около 23:40 оказался у подъезда без ключа и ждал около 35 минут»; opening-meta-gate PASS; H2 «Фраза, которая отвечает не на тот вопрос» с циклом переписки.
- metrika_signal: none (credentials unavailable; causal retention не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Слой «такси уехало → 35 минут у пустого ящика → вторая машина 480 ₽» отдельным абзацем — asymmetric moment после «код отправлен».
- Блок переписки «ящик открылся, ключа нет» ↔ «ключи в ключнице, код работает» — объясняет mismatch вопросов без обвинения.
- Связка night leverage + money-timing spine через interlink B08 (тишина) и B10 (такси) без дублирования B01 wrong-door.
- Мораль «ключница — обещание, не замок» + «Мой вывод как практика», не «Наш вывод простой».

### Change
- Для contactless/keybox hooks всегда включать **host-answer mismatch** (ответ про код vs вопрос про ключ) в utility-блок — не только механику ящика.
- При interlink — sibling про access-timing (B08 silence, B10 taxi, B01 wrong door) одной красной линией «код ≠ ключ внутри».

### Never again
- Писать empty-keybox кейс только про «наберите код ещё раз», игнорируя temporal leverage (ночь, такси уехало, второй рейс).
- Финал «Наш вывод простой» вместо «Мой вывод как практика».

### Resolution
status: recorded

---

## LESSON-20260908-0735-B14-quiet-home-bass-through-wall
status: proposed
topic_id: B14
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: title-brief.json (8 400 ₽ / две ночи / «тихий дом»), description-brief.json PASS, research-notes hook `neighbors_night`, case-delivery-gate PASS, article.html opening bass-through-wall scene.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER (INC-20260903-0640).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Two-beat H1 ««Тихий дом» обещали. За 8 400 ₽ — музыка за стеной ночью»: обещание + цена + источник шума (стена, не улица).
- §1: бас через стену, подушка вибрирует, 23:40; явное «не с улицы» — anti-dup B12.
- H2 «Что хост на самом деле продал гостю»: «тихий дом» не отвечает на вопросы про этаж/соседей/жалобы.
- Klyshin «Нет. Так не заселяем.» + «Сначала проверка. Потом перевод.»; вопрос-отмычка про соседей до оплаты.
- Tyumen quiet-hours context (22:00–08:00) как фон, не legal guide.
- Interlink spine: B12 внешний шум, B08 тишина после предоплаты, B01/B02 access/deposit siblings.
- Wordstat P0 spine «квартиры посуточно тюмень»; узкий «шум соседей» на cover sticker.
- Cover-QA PASS after regen + pad-clear on no-logo inlines (INC-20260908-0733).

### Change
- В `neighbors_night` hooks в §1 сразу фиксировать **источник шума** (стена vs окно/дорога) — не смешивать с B12 crane/road.
- Utility-блок: конкретные вопросы хосту (этаж, сбоку/сверху, жалобы за месяц) рядом с цитатой «тихий дом».

### Never again
- Писать quiet-home кейс только про панораму/фото, игнорируя соседей через стену.
- Смешивать B12 (стройка/дорога за окном) и B14 (вечеринка в доме).
- How-to для арендодателей до морали; финал «Наш вывод простой».

### Proposed apply
- Scout: при hook `neighbors_night` логировать Klyshin angle + anti-dup note vs B12 + final P0 spine Tyumen.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260908-0735-B14-host-sells-adjective-not-facts
status: proposed
topic_id: B14
category: structure
confidence: low

### Evidence
- artifact: title-brief.json#angle
  finding: angle «обещание тихого дома → музыка в 23:40 через стену»; opening-meta-gate PASS; blockquote «Не «тихий дом»… А бас из соседней квартиры».
- metrika_signal: none (credentials unavailable; causal retention не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Контраст прилагательного («тихий дом», «всегда тихо») vs проверяемых фактов (этаж, соседи, жалобы).
- Хост как первая линия в чате ночью — без выдуманных адресов/дБ.
- Description не дублирует H1: «после одиннадцати всё стихает» vs бас (description-brief PASS).

### Change
- Title/Description: держать price anchor (8 400 ₽) + temporal beat (23:40) в паре с обещанием тишины.

### Never again
- Принимать «у нас всегда тихо» за ответ на вопрос «кто сбоку?».
- Legal-гайд по шумовым нормам вместо guest-case utility.

### Proposed apply
- Description agent: rhythm klyshin_case_hook + not_equal_title как в B14 description-brief.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260910-1045-B15-business-trip-desk-wifi-docs
status: proposed
topic_id: B15
category: utility
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: article.html (§Wi‑Fi/стол/документы), title-brief.json angle, scout handoff sept_business_trip.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER (INC-20260903-0640).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Угол `sept_business_trip`: стол + розетка + Wi‑Fi **на видеосозвон** + закрывающие **до оплаты**, не после заселения в 22:00.
- §1 с ₽ (11 400 за 3 ночи), цитатой хоста «ну вы же не просили отдельно рабочее место» и конкретикой: журнальный столик, розетка за диваном, ~8 Мбит/с.
- Разведение «Wi‑Fi есть» vs «созвон пройдёт» — замер из точки ноутбука / тестовый видеозвонок, не обещание «быстрый».
- Фото стола и розетки в одном кадре — utility-шаг, не общий интерьер.
- Закрывающие: список документов и срок в чате до перевода; «потом» как красный флаг.
- Вопрос-отмычка: «Где розетка у стола и какой реальный Wi‑Fi на видеосозвон? Закрывающие пришлёте до оплаты?»
- Klyshin «Нет. Так не заселяем.» + «Сначала проверка. Потом перевод.»; чеклист из 4 пунктов в финале.
- Interlink spine: B10 «всё включено», B05 рейтинг≠рабочее место, B08 предоплата+тишина, B06 поздний заезд без запаса.
- Wordstat P0 spine «квартиры посуточно тюмень» 5020 (Tyumen); hook «командировка» слабый локально (45–85) — честный guest-intent на сентябрь.

### Change
- В `sept_business_trip` кейсах в §1 называть **все три слоя** сразу: поверхность стола, розетка в досягаемости, Mbps/видеозвон — не раскрывать по одному H2.
- Scout handoff: при weak local «командировка» логировать rework на spine P0 + sub-angle desk/Wi‑Fi/docs (как в assembled-scout-inputs-b15).

### Never again
- Принимать «Wi‑Fi есть» / «быстрый интернет» без проверки с рабочего места.
- Считать барную стойку / журнальный столик «рабочим столом» из объявления.
- Оставлять закрывающие на «пришлём после выезда» без письменного списка до оплаты.
- How-to для арендодателей; legal-гайд по справкам вместо guest-case.

### Proposed apply
- Scout: hook `sept_business_trip` → handoff lockpick (розетка + Wi‑Fi созвон + документы) + final P0 spine Tyumen.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260910-1045-B15-title-desk-reveal-over-timing
status: proposed
topic_id: B15
category: voice
confidence: low

### Evidence
- artifact: derouter-title-raw.json / title-brief.json
  finding: scout shape «Позвонили в 10:00. В 22:00 Wi‑Fi не тянет созвон» → финальный H1 ««Рабочий стол» обещали. За 11 400 ₽ — журнальный столик»; slug сохранил timing (`pozvonili-v-10-00-v-22-00-wifi-ne-tyanet-sozvon`).
- metrika_signal: none (credentials unavailable; causal CTR не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Cable pain-scene: обещание в кавычках + price anchor (11 400 ₽) + физический контрфакт (журнальный столик), без SEO-хвоста.
- Description держит Wi‑Fi/розетку, не дублирует H1 (description-brief PASS: «Wi‑Fi есть» vs столик).
- Timing 10:00 vs 22:00 остаётся в теле (H2 «Спешка всегда просит не проверять»), не в заголовке-спойлере.

### Change
- Для business-trip hooks: prefer **quoted amenity lie + ₽ + tangible mismatch** over compound timing spoiler в H1.
- Slug может нести timing-hook для URL/anti-dup, пока H1 — desk/price reveal.

### Never again
- H1 со всеми битами («10:00, 22:00, Wi‑Fi, стол») — оставлять раскрытие по слоям в lead/H2.
- Description, дублирующий H1 про стол (как в meta_ab B15 — там дубль, но description-brief корректен).

### Proposed apply
- Title skill review: sept_business_trip — quoted promise + price + physical counterfact > timing-only H1.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260911-1046-B16-cancel-prepay-refund-deadline
status: proposed
topic_id: B16
category: utility
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: article.html (§отмена рейса/4200₽/четвёртый день), scout handoff cancel_prepay, title-brief.json, description-brief.json.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER (INC-20260903-0640, INC-20260911-1046).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Угол `cancel_prepay`: отмена поездки **до заселения**, хозяин **отвечает**, но «вернём после проверки за три дня» без даты отправки — не дублировать B08 (тишина в чате).
- §1: цитата «Вернём после проверки, в течение трёх дней», **4 200 ₽** за две ночи, отменённый рейс за день до заезда; четвёртый день — «ещё проверяем».
- Разведение «три дня» vs **календарный день отправки** и **канал возврата** (площадка / тот же перевод); банковское зачисление ≠ отправка.
- Utility: маршруты Avito / Суточно.ру (сроки зачисления) vs прямой перевод хозяину — без юридического гайда.
- Вопрос-отмычка: «Если поездка сорвётся до заселения, в какой день и каким способом вы вернёте предоплату?»
- Klyshin «Нет. Так не заселяем.» → «так не **берём** предоплату»; «Сначала проверка. Потом деньги и ключи.»
- Interlink spine: B08 тишина после предоплаты, B04 доплата у двери, B02 залог на выезде, B10 «всё включено» — одна красная линия «сумма названа, условия нет».
- Wordstat P0 spine «квартиры посуточно тюмень» 4 929 (Tyumen); узкие «вернуть предоплату» 46 — честный rework на широкий spine + конфликтный sub-angle.
- Description не дублирует H1: «после проверки» vs четвёртый день (description-brief PASS).

### Change
- В `cancel_prepay` кейсах в §1 сразу фиксировать **от какого дня** считаются «три дня» (отмена / сообщение / заезд) — не оставлять в теле.
- Scout handoff: при weak refund phrases логировать rework chain (как B16 handoff) + anti-dup vs B08 silence.

### Never again
- Строить возврат-предоплаты кейс как юридическую консультацию или how-to «как вернуть через суд».
- Смешивать B08 (хозяин молчит) и B16 (хозяин вежлив, но без даты).
- Принимать «после проверки» или «в течение трёх дней» за согласованный срок без даты отправки и канала.
- Финал «Наш вывод простой»; чеклист только после вывода.

### Proposed apply
- Scout: hook `cancel_prepay` → handoff lockpick (дата + способ возврата) + final P0 spine Tyumen + anti-dup B08.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260911-1046-B16-polite-vagueness-vs-silence
status: proposed
topic_id: B16
category: voice
confidence: low

### Evidence
- artifact: title-brief.json#angle
  finding: angle «хозяин обещал вернуть 4 200 ₽ после проверки за три дня, на четвёртый день деньги не поступили»; H1 «Рейс отменили. 4 200 ₽ обещали вернуть за три дня — срок вышел»; opening-meta-gate PASS.
- metrika_signal: none (credentials unavailable; causal CTR не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Cable pain-scene: внешнее событие (рейс отменили) + price anchor (4 200 ₽) + истёкший срок — без SEO-хвоста в H1.
- Контраст «вежливый ответ как обезболивающее» vs B08 «тишина в чате» — mid-body явная ссылка на sibling.
- Description rhythm klyshin_case_hook: «после проверки» звучит вежливо, пока четвёртый день (not_equal_title PASS).
- Cover-text sticky «Дата и способ до оплаты» + wordstat spine на обложке.

### Change
- Для money-before-clarity hooks после B08: если хозяин **отвечает**, держать tension в **пустом параметре** (дата/канал), не в молчании.
- Title: prefer **event + ₽ + deadline breach** over narrow «вернуть предоплату» SEO lead.

### Never again
- H1-спойлер со всеми платформенными сроками Avito/Суточно — оставлять в utility H2.
- Description, дублирующий H1 про рейс и 4 200 ₽ (meta_ab B16 дублирует; description-brief корректен).

### Proposed apply
- Title/Description review: cancel_prepay — quoted vague promise + ₽ + expired deadline > refund-keyword H1.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260911-1046-B16-post-sol-inline-inject-pipeline
status: proposed
topic_id: B16
category: other
confidence: high

### Evidence
- artifact: memory/pipeline-fix-queue.md#INC-20260911-1040
  finding: Cover `--inject-html` до Sol; Sol перезаписал article.html без `<figure>`; manifest `h2_anchor` не совпал с Sol H2 → quad-split пропустил inline_2/4/6; publish вручную вставил inline_1/2/3/5/7.
- metrika_signal: none (pipeline incident; не поведенческий сигнал)

### Named blockers
- ASSUMED_BEHAVIOR

### Keep
- Publish live-page PASS post 4668; cover_qa PASS; 5 inline figures на live.

### Change
- После Sol всегда `--inject-only` из cover-registry (durable fix INC-20260911-1040: positional H2 fallback + wp_publish preflight).

### Never again
- Inject figures до Sol без post-Sol re-inject.
- Phantom h2_anchor из cover-scene draft, не сверенные с финальными Sol H2.

### Proposed apply
- Publish skill runbook: post-Sol inject-only обязателен (уже в fixer resolution INC-20260911-1040).

### Durable applied
- scripts/excalibur_blog_cover_quad_split.py — positional H2 fallback + --inject-only
- scripts/excalibur_blog_wp_publish.py — auto inject-only preflight
- rollback: revert commits on cover_quad_split/wp_publish if inject breaks legacy articles

### Resolution
status: recorded

---

## LESSON-20260912-1047-B17-utilities-included-vs-meter-checkout
status: proposed
topic_id: B17
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: title-brief.json, description-brief.json, case-delivery-gate PASS, article.html, research-notes hook `utilities_jkh`, scout handoff 2026-09-12.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER (INC-20260912-1047).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Two-beat H1 ««Коммуналка включена». На выезде — счётчики и 1 840 ₽»: цитата-обещание → контрфакт счётчиков + ₽ на выезде, не how-to ЖКХ.
- §1: 9 600 ₽ (3 200 ₽/ночь × 3) до идентичности хоста; «коммуналка включена» — не «частично», не «по приборам»; три фото счётчиков и 1 840 ₽ когда чемодан у двери.
- Разведение «включено» vs честный расчёт по счётчикам **если согласовано до брони** — utility H2 «Считаем то, что показали», не legal guide.
- Проверяемая математика: 12 418 → 12 847 = 429 кВт·ч ≈ 1 841 ₽ при 4,29 ₽/кВт·ч (сентябрь 2026, Тюмень); обычный расход 150–320 ₽ за три ночи — editorial disclaimer, не норма рынка.
- Ключевой перелом: **нет стартовых показаний при заезде** — фото на выезде не доказывает базу расчёта.
- Klyshin «Нет. Так не заселяем.» → «Так не считаем»; вопрос-отмычка «Коммуналка в цене или по счётчикам?» → TG/MAX mid-body.
- Interlink spine: B10 «всё включено»+такси, B02 залог на выезде, B11 «всё для гостей», B04 доплата у двери — одна красная линия «условие до брони vs на пороге».
- Wordstat P0 spine «квартиры посуточно тюмень» 4 840 (Tyumen); узкие «жкх посуточно» / «коммуналка посуточно» API empty — стоп-фактор внутри spine, не P0.
- Description не дублирует H1: ««Включено» — пока не взяли чемодан?» + счётчики вслепую (description-brief PASS).
- Anti-dup vs B10 (taxi all-inclusive), B12 (кран/шум), hot water — центральный конфликт только utilities_jkh.

### Change
- В `utilities_jkh` кейсах в §1 сразу фиксировать **три слоя**: (1) цитата «включено» в карточке, (2) отсутствие стартовых показаний, (3) сумма на выезде — не раскрывать математику только во втором H2.
- Scout handoff: при weak ЖКХ Wordstat логировать rework chain (как B17 handoff) + note «коммуналка посуточно» empty → spine Tyumen.

### Never again
- Строить utilities-кейс как статью о тарифах ЖКХ или перечень всех скрытых платежей.
- Смешивать B10 «всё включено»+такси и B17 «коммуналка включена»+счётчики — разные hook_id.
- Принимать фото счётчика на выезде без стартовой точки и тарифа за доказательство расхода гостя.
- Выдавать 1 840 ₽ или диапазон 150–320 ₽ за рыночную статистику без editorial disclaimer.
- Октябрьские тарифы в сентябрьском сюжете (9–12.09.2026).
- How-to для арендодателей; финал «Наш вывод простой».

### Proposed apply
- Scout: hook `utilities_jkh` → handoff lockpick (включено vs счётчики + стартовые показания) + final P0 spine Tyumen + anti-dup B10.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260912-1047-B17-checkout-leverage-meter-photos
status: proposed
topic_id: B17
category: structure
confidence: low

### Evidence
- artifact: title-brief.json#angle
  finding: angle «Гость забронировал… обещанием включённой коммуналки, а при выезде получил фото счётчиков и требование доплатить 1 840 ₽»; opening-meta-gate PASS; H2 «Почему это всплывает именно на выезде».
- metrika_signal: none (credentials unavailable; causal retention не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Слой «чемодан у двери → через час в дорогу → спорить неудобно» отдельным абзацем — asymmetric moment после полной оплаты 9 600 ₽.
- Контраст «до оплаты можно сравнить карточки» vs «после трёх ночей ключи сдавать» — money-timing spine без дублирования B10 taxi.
- Блок «условие до бронирования — выбор; условие на пороге — давление» — объясняет leverage без злодейства.
- Связка с sibling B02 (залог на выезде), B10 (такси), B04 (дверь) в mid-body одной красной линией.

### Change
- Для `utilities_jkh` hooks всегда включать **checkout temporal leverage** (чемодан, ключи, поезд) в utility-блок — не только математику счётчиков.
- При interlink — sibling про broad/included promises (B10, B11) + checkout surprises (B02) одной линией «слово до брони ≠ строка на выезде».

### Never again
- Писать utilities кейс только про тарифы и кВт·ч, игнорируя temporal leverage (когда исправить нечем).
- Финал «Наш вывод простой» вместо «Мой вывод как практика».

### Proposed apply
- Writer checklist (review-only): utilities_jkh + checkout → один абзац про asymmetric moment после «включено» в карточке.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260912-1047-B17-title-quote-meter-reveal
status: proposed
topic_id: B17
category: voice
confidence: low

### Evidence
- artifact: title-brief.json / derouter-title
  finding: scout draft «Написали „коммуналка включена“. На выезде прислали счётчики — 1 840 ₽» → финальный H1 ««Коммуналка включена». На выезде — счётчики и 1 840 ₽»; klyshin_title_shape:3.
- metrika_signal: none (credentials unavailable; causal CTR не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Cable pain-scene: обещание в кавычках + temporal beat «на выезде» + tangible counterfact (счётчики) + ₽ (1 840), без SEO-хвоста ЖКХ.
- Description rhythm klyshin_case_hook: ««Включено» — пока не взяли чемодан?» (not_equal_title PASS).
- Cover-text sticky «Сначала проверка, потом перевод» + wordstat spine «квартиры посуточно тюмень» на обложке.

### Change
- Для utilities_jkh hooks: prefer **quoted «включено» + checkout beat + meter/₽ reveal** over narrow «жкх посуточно» SEO lead.
- Title: двухчастный ритм (обещание / контрфакт на выезде) > compound «три ночи + счётчики + тариф» spoiler.

### Never again
- H1-спойлер со всей математикой 429 кВт·ч — оставлять расчёт в utility H2.
- Description, дублирующий H1 про «коммуналка включена» и 1 840 ₽.

### Proposed apply
- Title/Description review: utilities_jkh — quoted promise + checkout + ₽ > ЖКХ-keyword H1.

### Durable applied
- none

### Resolution
status: recorded
