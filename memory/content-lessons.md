# Excalibur BLOG — content lessons

Активные и proposed уроки Content-learner (v2). Read-only для Writer/Sol.

---

## LESSON-20260829-0846-B04-workplace-four-elements
status: proposed
topic_id: B04
category: utility
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: title-brief.json#checks + article.html H2 «Что на самом деле нужно проверить до оплаты»: стол ≠ рабочее место; узкая стойка + розетка за холодильником + Wi-Fi в коридоре.
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID); ingest exit 2, выборка отсутствует.

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Формула «рабочее место = поверхность + розетка на длину шнура + связь в этой комнате + документ после оплаты» — убрать один элемент, остальные не спасают созвон.
- Письменные уточнения до оплаты: «две свободные слева от стола», не «в комнате есть розетки».
- Пятиточечный чеклист: розетка, стул (не табурет), свет/фон, размер поверхности, LAN/патч-корд для RDP.
- Проверка «2 минуты видеозвонка с будущего стула» — не speedtest у окна.
- Запрос живого фото: стол целиком + розетка + стул в одном кадре.

### Change
- Для business-trip / командировочных тем сразу в lead назвать **конкретное время созвона** (10:00), не только «нужен интернет».
- Scout/Title: при hook «рабочий стол» в handoff логировать sub-angle **розетка в руке + Wi-Fi в точке**, не только Wordstat spine.

### Never again
- Принимать галочку «рабочий стол» без розетки в пределах вытянутой руки и Wi-Fi именно на рабочем месте.
- Подменять проверку связи скриншотом тарифа провайдера.

### Proposed apply
- Writer checklist (review-only): командировка → workplace-four-elements + 2-min video test в utility-блоке.
- Cover-text inline_2/inline_3 стикеры дублируют чеклист — повторять для sibling business-trip материалов.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260829-0846-B04-closing-docs-not-potom
status: proposed
topic_id: B04
category: utility
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: article.html H2 «Документы: слово «потом» стоит дороже…»; хозяин «Потом» в мессенджере; разбор ООО/ИП/самозанятый/физлицо + чек QR vs форма 3-Г.
- metrika_signal: none (METRIKA CREDENTIALS BLOCKER)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- ASSUMED_BEHAVIOR

### Keep
- Конкретный шаблон сообщения хозяину: статус исполнителя + договор/акт/чек QR + ИНН до безнала + сроки счёта и акта.
- «Конечно, всё будет» как anti-answer — не закрывает риск отчёта.
- Связка с B02 (залог): деньги до договорённостей возвращаются не легче документов.

### Change
- Business-trip материалы всегда включают **статус исполнителя** (ООО/ИП/самозанятый/физлицо) в чеклист до оплаты, не отдельным FAQ.
- Description (Дзен): держать контраст «карточка убедительна / утром спасать поздно» — как description-brief B04.

### Never again
- Оставлять «закрывающие документы» общим вопросом без сроков, формы и того, кто выдаёт чек.
- Принимать «справку от руки» для командировочного отчёта без предупреждения о риске.

### Proposed apply
- Scout для buyer-жаргона «командировка»: final P0 + **docs-status sub-angle** в handoff.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260829-0846-B04-time-contrast-h1
status: proposed
topic_id: B04
category: voice
confidence: low

### Evidence
- artifact: title-brief.json#pain_scene
  finding: H1 «Звонок в 10:00. Заселился в 22:00 — у стола нет розетки»; rejected «5 советов…» и label-head; description-brief not_equal_title PASS.
- metrika_signal: none (METRIKA CREDENTIALS BLOCKER; causal CTR не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Двойной таймстамп (утренний дедлайн + поздний заезд) + конкретный контрфакт (розетки нет) — cable pain-scene без SEO-хвоста.
- Lead 22:10 / 10:00 раскрывает сцену, H1 не дублирует description дословно.

### Change
- Повторять формулу «время A / время B — измеримый провал utility» для business-trip hooks; payoff — физический объект (розетка, ключ, документ), не абстракт «обман».

### Never again
- Listicle H1 («N советов командировочному») при наличии сильной временной сцены.
- Description-дубль H1 («рабочее место в карточке» = тот же текст, что заголовок).

### Proposed apply
- Title skill review: командировка — prefer dual timestamp + physical payoff over demand-spine в H1.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260829-0846-B04-late-train-early-call-window
status: proposed
topic_id: B04
category: structure
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: article.html H2 «Поздний заезд и ранний выезд»; противоречие 24/7 vs 12:00–21:00; доплата 500 ₽/час; вопрос-отмычка «Поезд 23:40, выезд 15:00 — сколько и кто встретит?»; interlink B01/B03.
- metrika_signal: none (METRIKA CREDENTIALS BLOCKER)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Слой «цена ночи + цена каждого часа вне окна» — 2–3 часа = до 1,5 тыс., «дешёвая» квартира пересчитывается.
- Инструкция по заезду **до оплаты** (связка с B01 бесконтакт).
- Interlink-треугольник B01 (ключ/инструкция) + B02 (залог) + B03 (картинка vs реальность) — каждый sibling закрывает свой риск командировки.

### Change
- Business-trip материалы: temporal window + hourly surcharge в одном блоке с workplace/docs, не только в geo-материалах (см. B03 parents window — другой buyer, тот же structural слой).
- Финальный вердикт-чеклист: время → стол/розетка/Wi-Fi → документы → деньги последним шагом.

### Never again
- Писать командировочный гайд только про стол/Wi-Fi, игнорируя mismatch окон заселения и стоимость позднего поезда.
- Оставлять «24/7» в шапке без сверки с правилами 12:00–21:00 в том же объявлении.

### Proposed apply
- Scout handoff: hook «командировка» → log **check-in-window + hourly surcharge** рядом с workplace sub-angle.

### Durable applied
- none

### Resolution
status: recorded

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
