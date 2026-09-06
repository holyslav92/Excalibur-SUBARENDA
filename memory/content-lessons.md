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

## LESSON-20260906-0646-B11-cancel-link-after-payment
status: proposed
topic_id: B11
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: title-brief.json, description-brief.json, case-delivery-gate PASS, article.html, research-notes hook `cancel_prepay`.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER (INC-20260903-0640).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Two-beat H1 «Отменил за сутки. 2 500 ₽ — «по условиям ссылки»»: действие → контрфакт ссылки, не how-to «как отменить бронь».
- §1: отмена за сутки, цитата «по условиям ссылки предоплата не возвращается», 2 500 ₽ до идентичности хоста; pain = ссылку открыли впервые **после** отмены.
- Угол отличен от B08: не «тишина в чате после предоплаты», а «правила появились ссылкой только при отмене».
- Klyshin «Нет. Так не заселяем.» + «Сначала проверка. Потом перевод.»; вопрос-отмычка «Какие условия отмены и когда вернут предоплату — до перевода?» → TG/MAX mid-body.
- H2 «Почему на площадке проще, а в личке опаснее» — контраст карточки отмены vs прямой перевод без оговорки.
- Редакционный дисклеймер: 2 500 ₽ — конструкция кейса, не средняя предоплата по Тюмени.
- Interlink: B10 «всё включено», B02 залог, B04 доплата, B05 рейтинг ≠ условия.
- Wordstat: spine «квартиры посуточно тюмень» 11 342 (225) / 5 261 (55+11176); P0 «отмена брони посуточно» 78; «вернуть предоплату посуточно» 81.

### Change
- В кейсах `cancel_prepay` в §1 фиксировать **момент появления ссылки** (после отмены, не до перевода) — это отделяет от B08 silence-hook.
- Параллельно с суммой предоплаты называть три поля до оплаты: срок бесплатной отмены, сумма удержания, срок/способ возврата.

### Never again
- Смешивать cancel-link кейс с B08 «тишина после перевода» без явного угла «ссылка после отмены».
- Принимать «ссылку потом» как условия; «разберёмся» / «всё по стандарту» — не ответ.
- How-to чеклист до кейса; чеклист только после «Мой вывод как практика».

### Proposed apply
- Scout: при hook `cancel_prepay` логировать original Klyshin + final P0 «отмена брони посуточно» / «вернуть предоплату посуточно» + note «не дублировать B08 silence».
- Description: контраст «можно отменить vs правила до перевода» — как description-brief B11.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260906-0646-B11-messenger-no-cancel-card
status: proposed
topic_id: B11
category: structure
confidence: low

### Evidence
- artifact: title-brief.json#angle
  finding: angle «ссылку на невозврат получил только после отмены»; opening-meta-gate PASS; lead фиксирует перевод до появления условий.
- metrika_signal: none (credentials unavailable; causal retention не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- H2 «Три сообщения, после которых начинаются споры» — цена → перевод → ссылка после отмены как narrative spine.
- Bold beat «Не бронь. Не удержание дат. А перевод без прописанных условий отмены.» — точка риска до платформенного сравнения.
- Platform facts (Суточно/Авито) с оговоркой «не переносить на прямой чат» — из research-notes constraints.

### Change
- Для cancel_prepay hooks всегда включать **platform-vs-messenger** блок — не только список вопросов гостю.
- При interlink — sibling money-before-clarity (B08 transfer, B10 taxi fee) одной красной линией «условия до денег».

### Never again
- Писать cancel-кейс только про сумму удержания, игнорируя отсутствие карточки отмены в мессенджере.
- Ссылку на правила после оплаты подавать как норму без требования текстом в чат до перевода.

### Proposed apply
- Writer checklist (review-only): cancel_prepay → один абзац platform card vs messenger + screenshot-before-pay.

### Durable applied
- none

### Resolution
status: recorded
