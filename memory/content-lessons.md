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

## LESSON-20260910-1354-B16-hotel-vs-apartment-corridor-sleep
status: proposed
topic_id: B16
category: utility
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: title-brief.json, description-brief.json, case-delivery-gate PASS, research-notes hook `hotel_vs_daily`, article.html opening corridor/elevator scene.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER (INC-20260903-0640).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Угол `hotel_vs_daily`: экономия 900 ₽/ночь vs сон — не бинар «отель лучше квартира», а что гость не проверил до оплаты (коридор, лифт, ночная поддержка).
- Two-beat H1 «Отель был дороже на 900 ₽ за ночь. Квартира — две ночи без сна»: цена-контраст → контрфакт сна, не how-to.
- §1: «тихо, как дома» + 2 700 ₽ экономии на три ночи; шум — коридор/лифт/площадка до 03:00, явно «не музыка за стеной» (anti-dup B14).
- H2 «Тихо — это где именно?»: хост контролирует квартиру, не подъезд; ответ «это же МКД» — mismatch до оплаты, не злодейство.
- H2 «Почему отзывы могут ничего не сказать» + interlink B05 рейтинг ≠ ночной коридор.
- H2 «Что реально даёт отель за +900 ₽»: стойка/смена номера как возможный сервис, не гарантия тишины; честный контраст с мессенджером хоста ночью.
- Вопрос-отмычка: свежие отзывы про коридор/лифт + что даёт отель за +900 ₽ → TG mid-body.
- Klyshin «Нет. Так не выбираем.» + «Сначала проверка. Потом перевод.»; чеклист из 5 пунктов в финале.
- Interlink spine: B14 тихий дом/соседи, B12 тихий центр/окно, B05 рейтинг без слов про шум.
- Wordstat P0 spine «квартиры посуточно тюмень» 5020 (Tyumen); supporting «отели тюмень» 7182, «посуточно или отель» 387.
- Description не дублирует H1: «лифт не спит» + проверка за дверью после полуночи (description-brief PASS).
- Cover-QA PASS: 2× Grsai quad, manual manifest-slots (B15 layout legacy).

### Change
- В `hotel_vs_daily` кейсах в §1 сразу фиксировать **источник шума** (коридор/лифт/площадка МКД) и **арифметику экономии** (900 ₽/ночь × N ночей) рядом с цитатой «тихо, как дома» — не смешивать с B14 (соседи/музыка) или B12 (стройка/окно).
- Scout handoff: при weak narrow query логировать rework на spine P0 + sub-angle corridor/elevator vs hotel night service (как assembled-scout-inputs-b16).

### Never again
- Противопоставлять отели и квартиры как «тихий vs шумный» тип жилья.
- Писать hotel-vs-apartment кейс только про цену, игнорируя коридор МКД и ночной канал поддержки.
- Смешивать B14 (бас за стеной) и B16 (подъезд/лифт).
- How-to «как выбрать отель» до морали; чеклист только после «Мой вывод как практика».
- Выдавать 4 500 ₽ срочного отеля или 2 700 ₽ экономии за рыночную статистику без editorial disclaimer.

### Proposed apply
- Scout: hook `hotel_vs_daily` → handoff lockpick (коридор/лифт + отзывы + что даёт отель за Δ₽) + final P0 spine Tyumen + anti-dup note vs B14/B12.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260910-1354-B16-two-nights-emergency-hotel-cost
status: proposed
topic_id: B16
category: structure
confidence: low

### Evidence
- artifact: title-brief.json#angle
  finding: angle «Экономия на квартире обернулась двумя ночами без сна и срочным переездом в отель»; opening-meta-gate PASS; lead фиксирует две бессонные ночи → отель ~4 500 ₽ на последнюю.
- metrika_signal: none (credentials unavailable; causal retention не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Слой «две ночи без сна → срочный отель» отдельным абзацем — asymmetric moment после «разумной» экономии 900 ₽/ночь.
- Формула «Сначала сон и правила, потом экономия» (research voice_angle) — не мораль «всегда берите отель».
- Короткий заезд 2–3 ночи: цена ошибки выше, чем кажется по строке «−900 ₽».
- Связка money-timing spine через interlink B10 (такси-доплата) и B13 (ночь у двери) без дублирования их сюжетов.

### Change
- Для `hotel_vs_daily` hooks всегда включать **стоимость срочного запасного варианта** (отель в последний момент) в utility-блок — не только Δ₽ в объявлении.
- При interlink — sibling про «тихо»-прилагательные (B12, B14, B05) одной красной линией «слово ≠ коридор/окно/соседи».

### Never again
- Считать экономию за N ночей окончательной без учёта срочного переезда после неудачной ночёвки.
- Финал «Наш вывод простой» вместо «Мой вывод как практика».

### Proposed apply
- Writer checklist (review-only): hotel_vs_daily + short_stay → один абзац про price-of-error после второй бессонной ночи.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260910-1354-B16-title-price-inversion-sleep-reveal
status: proposed
topic_id: B16
category: voice
confidence: low

### Evidence
- artifact: title-brief.json / scout handoff
  finding: scout shape «Квартира дешевле отеля на 900 ₽. Первая ночь — как в хостеле» → финальный H1 «Отель был дороже на 900 ₽ за ночь. Квартира — две ночи без сна»; slug сохранил corridor hook (`shum-koridor-do-treh`).
- metrika_signal: none (credentials unavailable; causal CTR не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Cable pain-scene: инверсия перспективы (отель дороже) + price anchor (900 ₽) + контрфакт сна (две ночи), без SEO-хвоста.
- Description держит лифт/дверь, не дублирует H1 (description-brief PASS).
- «Первая ночь — как в хостеле» остаётся в research/scout, не в H1-спойлере; раскрытие — две ночи + коридор в lead.

### Change
- Для hotel_vs_daily hooks: prefer **price inversion + sleep failure** over «hostel night» metaphor в H1.
- Slug может нести corridor/timing-hook для URL/anti-dup, пока H1 — ₽ + sleep reveal.

### Never again
- H1 со всеми битами («900 ₽, хостел, коридор, три ночи») — оставлять раскрытие по слоям в lead/H2.
- Description, дублирующий H1 про две ночи без сна.

### Proposed apply
- Title skill review: hotel_vs_daily — price delta inversion + measurable sleep counterfact > hostel metaphor H1.

### Durable applied
- none

### Resolution
status: recorded
