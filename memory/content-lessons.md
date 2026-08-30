# Excalibur BLOG — content lessons

Активные и proposed уроки Content-learner (v2). Read-only для Writer/Sol.

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

## LESSON-20260830-0800-B04-after-checkout-docs-deadline
status: proposed
topic_id: B04
category: utility
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: H2 «Обещание „после выезда“ иногда длиннее самой командировки»; lead: чек на 10-й день vs 3 рабочих дня на авансовый отчёт; 4 200 ₽ личными деньгами.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER (METRIKA CREDENTIALS)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Второй удар Klyshin в H1: не «нет чека», а «обещают **после выезда**» — иллюзия срока, не отсутствие документа.
- Description не дублирует H1: вопрос ««После выезда» — это когда?» + авансовый отчёт (description-brief PASS).
- Три письменных фиксации до оплаты: какие документы, кто выдаёт, **когда** у гостя (не «потом»).
- Чеклист п.4–6: тип выдавшего (самозанятый/ИП/ООО), комплект, дата в рамках 3 рабочих дней.

### Change
- Для business-travel / командировка тем всегда связывать «после выезда» с **конкретной датой** и дедлайном бухгалтерии, не только с фактом выдачи.
- Scout handoff: при hook про закрывающие логировать sub-angle «срок vs авансовый отчёт», не только «нужен чек».

### Never again
- Принимать «сделаем после выезда» как достаточное обещание без даты, когда гость отчитывается за 3 рабочих дня.
- Писать командировочный материал только про Wi‑Fi/стол, игнорируя пакет закрывающих и срок.

### Proposed apply
- Writer checklist (review-only): командировка → документы + срок в одном материале с рабочим местом.
- Interlink sibling B02 (залог на выезде) как «деньги после ключей», B04 — «документы после выезда».

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260830-0800-B04-wifi-desk-at-point
status: proposed
topic_id: B04
category: utility
confidence: medium

### Evidence
- artifact: title-brief.json#checks.not_rozetka_angle
  finding: угол NOT «розетка» (WP duplicate); вместо этого стол + Wi‑Fi + чек до оплаты. Вопрос-отмычка: «Где будет стоять ноутбук — и какая скорость Wi‑Fi именно там?»
- metrika_signal: none (METRIKA CREDENTIALS BLOCKER)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Разделение H2: «Wi‑Fi есть» ≠ рабочая связь; Zoom 720p/1080p с цифрами Мбит/с.
- Барная стойка vs стол: «пришлите фото этого места» — не общее «да, есть».
- Inline alt дублирует риск: Wi‑Fi в прихожей vs обрыв в дальней комнате на 3-й минуте.

### Change
- Для remote-work / видеосозвон тем парить **точку ноутбука** (фото + скриншот speedtest), не «есть интернет».
- Отличать от розетка-angle в Scout: business-travel = стол + связь + документы.

### Never again
- Считать строку «Wi‑Fi и всё необходимое» доказательством готовности к 10:00 видеосозвону.
- Принимать барную стойку за «рабочее место» без фото и розетки рядом.

### Proposed apply
- Cover-text / inline stickers: «скорость **у стола**», не «Wi‑Fi есть».
- Title rejected_variant зафиксирован: чеклист «нужны» слабее, чем иллюзия «обещают после выезда».

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260830-0800-B04-late-checkin-morning-call-window
status: proposed
topic_id: B04
category: structure
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: lead 22:10 заезд → 10:00 созвон; H2 «Заезд в 22:00 — это не полночи на проверку»: ~40 минут на проверку; ошибка всплывает при включённой камере.
- metrika_signal: none (METRIKA CREDENTIALS BLOCKER)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Двойной якорь времени в H1 (22:00 + 10:00) сжимает день сильнее, чем одна метка.
- Interlink B01 (бесконтакт): вопрос после перевода = ночная переписка.
- Чеклист п.3: поздний заезд письменно до оплаты.

### Change
- Business-travel материалы: **окно между заездом и первым обязательным событием** (созвон/встреча) — отдельный слой боли, как у B03 parents+check-in.
- При позднем заезде — все проверки (стол, Wi‑Fi, документы) **до** оплаты, не «успею утром».

### Never again
- Писать про 22:00 заезд без привязки к завтрашнему дедлайну (созвон, отчёт, выезд).
- Оставлять проверку рабочего места на утро перед видеозвоном.

### Proposed apply
- Scout/Title: hook «поздний заезд» → handoff с **утренним якорем** (созвон/встреча/поезд).
- Sibling cluster B01–B04: «деньги/ключи до проверки» как сквозная нить.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260830-0800-B04-title-double-time-klyshin
status: proposed
topic_id: B04
category: voice
confidence: low

### Evidence
- artifact: title-brief.json#pain_scene
  finding: две короткие фразы (22:00 заселился / 10:00 созвон) + второй удар «закрывающие обещают после выезда»; demand spine «квартиры посуточно тюмень» (5523) не в H1.
- metrika_signal: none (METRIKA CREDENTIALS BLOCKER; causal CTR не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Klyshin consequence: strong_verb «обещают после выезда» — не чеклист, а иллюзия срока.
- length_50_70 PASS (68 chars); city_in_h1 false — geo в description/теле.

### Change
- Повторять формулу «два времени + обещание с подвохом» для business-travel hooks.
- Rejected «5 вопросов» — держать историю, не N-вопросов в H1.

### Never again
- Заголовок-чеклист («нужны Wi‑Fi и чек») вместо сцены с ущербом/иллюзией.

### Proposed apply
- Title skill review: командировка — prefer double time anchor + misleading promise over checklist H1.

### Durable applied
- none

### Resolution
status: recorded
