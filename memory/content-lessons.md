# Excalibur BLOG — content lessons

Активные и proposed уроки Content-learner (v2). Read-only для Writer/Sol.

---

## LESSON-20260901-1220-B06-baggage-before-keys
status: proposed
topic_id: B06
category: utility
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Publish-артефакты: title-brief.json, description-brief.json, scout handoff checkout_train_bags, case-delivery-gate PASS, interlink-gate PASS (4 outbound).
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER по credentials.

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Klyshin moral «сначала порядок действий, потом ключ» → кейс: **сначала договориться о багаже, потом сдавать ключи** (scout handoff + финальный вердикт в article.html).
- Two-beat H1 «Выезд в полдень. Поезд через 4 часа — чемоданы у подъезда» — полдень → поезд → багаж у двери, без how-to.
- Lockpick до брони: «где будут вещи между выездом и поездом — и кто отвечает за доступ?» + 4 вопроса (до брони / до часа / где / кто выдаст).
- Разведение **поздний выезд** и **хранение багажа** как отдельных договорённостей (inline-стикеры inline_5).
- Иллюзия отеля (ресепшен, камера хранения) vs квартира после выезда — отдельный H2 «Нет камеры хранения».
- Wordstat P0 «квартиры посуточно тюмень» 5446 + secondary «хранение багажа» 133 / «хранение багажа тюмень» 28.

### Change
- В checkout-gap темах (выезд 12:00 + транспорт днём) в §1 называть **длину окна в часах** (4,5 ч), не только «до вечера».
- Scout handoff: при hook checkout_train_bags логировать final P0 + secondary bag cluster + explicit NOT early_checkin.

### Never again
- Сдавать ключи и «разбираться с чемоданами у двери» в коридоре за 15 минут до выезда.
- Считать поздний выезд автоматическим разрешением оставить багаж.
- Оставлять чемоданы у подъезда / в тамбуре «на полчасика» как рабочий план.

### Proposed apply
- Scout: checkout_train_bags → handoff с rework-логом bag clusters + spine Tyumen P0.
- Description (Дзен): вопрос «на полчаса у подъезда?» до чемоданов в руках — как description-brief B06.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260901-1220-B06-vokzal-locker-route-math
status: proposed
topic_id: B06
category: utility
confidence: medium

### Evidence
- artifact: article.html#«Камера на вокзале» + research-notes.md (Свердловская ж.д., ячейки 1-й этаж 24/7)
  finding: fallback-маршрут: такси 300–500 ₽ → вокзальные ячейки → 3–3,5 ч без багажа; не брать «100 ₽/час» из старых справочников.
- metrika_signal: none (credentials unavailable; causal retention не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Арифметика окна: 4,5 ч − дорога − сдача − 30–60 мин запас = ~3–3,5 ч «город без чемоданов».
- Конкретика вокзала Тюмени: 1-й этаж, 24/7, три размера, от 1 ч до суток; ~26 100 использований янв–июль 2026 (не гарантия свободной ячейки).
- Перекрёстная ссылка на B03: пешком с чемоданами ≠ пешком налегке.
- Inline-стикеры inline_6 / inline_7 дублируют маршрут и ₽.

### Change
- Для train-day checkout тем всегда включать **fallback на вокзальную ячейку** с запасом по размеру и времени, не только «спросите хоста».
- Упоминать продление по QR/SMS 2026 как ориентир, но не как замену запаса до поезда.

### Never again
- План «успеем ровно за четыре часа» без проверки занятости ячейки и размера багажа.
- Цитировать устаревший тариф «100 ₽/час» без «смотрите на терминале».

### Proposed apply
- Research checklist: checkout+train Tyumen → verify locker location/tariff on terminal + Sverdlovskaya press stat as demand signal only.
- Review only.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260901-1220-B06-checkout-day-interlink-cluster
status: proposed
topic_id: B06
category: structure
confidence: low

### Evidence
- artifact: interlink-gate.json#outbound_found
  finding: 4 sibling: бесконтактное заселение (логика «сначала договорённость»), доплата за третьего у двери, залог на выезде, «три остановки» с чемоданом — кластер «день отъезда / условия заметили поздно».
- metrika_signal: none (credentials unavailable)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Interlink как narrative cluster: поздно замеченные условия в день выезда (B04 доплата, B02 залог) + procedural siblings (B01 keys, B03 distance с багажом).
- CTA «напишите заранее — посмотрим окно до выезда» — не обещание сервиса на сайте.

### Change
- При publish checkout-gap тем — inbound из sibling «день у двери» (B02/B04) и outbound на procedural + geo-with-luggage (B03).

### Never again
- Checkout-gap материал без sibling на «условие существовало заранее, заметили у двери».

### Proposed apply
- Publish/interlink review: checkout_train_bags ↔ burn-at-door + luggage-distance siblings.
- Review only.

### Durable applied
- none

### Resolution
status: recorded

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
