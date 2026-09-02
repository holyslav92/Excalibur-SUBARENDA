# Excalibur BLOG — content lessons

Активные и proposed уроки Content-learner (v2). Read-only для Writer/Sol.

---

## LESSON-20260902-1055-B07-kitchen-three-levels-not-checkbox
status: proposed
topic_id: B07
category: utility
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из article.html §«Не плита. Не галочка. А завтрак на столе», scout handoff lockpick, description-brief PASS.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER (INC-20260902-1055).

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Три уровня обещания: «есть кухня» (зона) → «есть плита» (техника) → «можно поставить завтрак на двоих» (инвентарь + бюджет) — явное разведение в H2.
- Lockpick-вопрос в теле: «Что именно на кухне: сковорода, масло, соль, кружки?» — из scout handoff, не how-to.
- Klyshin-отрез «Нет. Так не заселяем.» + мораль «Сначала проверка. Потом перевод.» — тот же ритм, что B04/B03.
- Wordstat spine P0 «квартиры посуточно тюмень» 5446 (Tyumen) + contrast cluster «отель или посуточная квартира» 312; kitchen sub-angle «квартира с кухней посуточно» 68–89 (RF) — локализация через кейс, не SEO-хвост.

### Change
- В kitchen/equipment кейсах сразу в lead называть **что именно отсутствует** (посуда, масло, губка), а не только «кухня плохая».
- Scout handoff: при hook kitchen_vs_hotel_cafes логировать final P0 spine + kitchen sub-cluster volume.

### Never again
- Принимать галочку «кухня есть» / «оборудована» / «всё необходимое» как доказательство возможности готовить три дня.
- How-to «как выбрать квартиру с кухней» до морали и арифметики кафе.

### Proposed apply
- Scout: hook kitchen_vs_hotel_cafes → handoff lockpick + P0 spine + kitchen sub-phrase volume.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260902-1055-B07-cafe-burn-arithmetic-lead
status: proposed
topic_id: B07
category: structure
confidence: medium

### Evidence
- artifact: article.html#opening + research-agent-report.json#limitations
  finding: lead с разбивкой 500+450+1 450 ≈ 2 400 ₽/день × 3 ночи = 7 200 ₽; disclaimer «собирательный случай» в §1; research notes 7 200 как Scout-якорь.
- metrika_signal: none (credentials BLOCKER; article published 2026-09-02, zero-day sample)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Дневная + итоговая сумма в opening (не только «много потратил в кафе»).
- Диапазон 2 400–3 600 ₽/день как честный разброс, не одна цифра-догма.
- H1/title: цитата обещания + конкретный burn (7 200 ₽) — klyshin_title_shape 5, description не дублирует H1.

### Change
- Для kitchen-vs-cafe кейсов всегда давать **поминутную арифметику дня** (завтрак/обед/ужин) до общего итога за N ночей.
- В limitations research явно маркировать составной якорь — Writer не выдавать за чек одного гостя.

### Never again
- Заголовок/лид только «каждый день в кафе» без ₽ и без N ночей.
- Скрывать, что сумма — модельный расчёт, если нет реального чека.

### Proposed apply
- Research/Writer review: kitchen burn cases → day breakdown + total + collective-case disclaimer in §1.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260902-1055-B07-photo-drawers-before-pay
status: proposed
topic_id: B07
category: cta
confidence: low

### Evidence
- artifact: article.html#«Сообщение, которое стоит дешевле…» + checklist «Проверьте до брони»
  finding: фото открытых ящиков (не гламур кухни) + 8-пунктовый чеклист после морали; CTA «Проверить кухню по конкретной квартире» с TG/MAX.
- metrika_signal: none (credentials unavailable)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Запрос фото ящиков/шкафа как конкретный шаг до брони — дешевле трёх дней кафе.
- Чеклист после verdict (не до боли): сковороды, нож, кружки поштучно, масло/соль, губка, техника.
- Interlink на B01/B02/B04/B05 как sibling «формально прав / деньги каждый день» — не дублировать door-fee angle.

### Change
- В equipment-кейсах CTA-блок хоста: «список + фото по конкретной квартире» — шаблон для kitchen siblings.
- Description (Дзен): контраст «галочка ≠ готовить» + action «фото до оплаты».

### Never again
- Чеклист до раскрытия кейса (термин-дамп).
- Обещать одинаковый kitchen-kit для всех объектов тенанта.

### Proposed apply
- Description skill review: kitchen hooks → not_equal_title + фото-якорь в teaser.
- CTA review-only; не в Writer master-prompt автоматически.

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
