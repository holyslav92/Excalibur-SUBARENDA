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

## LESSON-20260829-1237-B04-dual-track-uze-sdali
status: proposed
topic_id: B04
category: structure
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: opening paragraphs mirror 22:15 scene twice — fraud (link out of platform) vs in-platform calendar conflict; first H2 «Уже сдали — это не всегда одна и та же история» forks routes (police vs support).
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (INC-20260829-1237); sample absent, no retention/scroll validation

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Одна утренняя фраза «уже сдали» → два маршрута (мошенничество / конфликт броней), не смешивать в один нарратив.
- Lead с конкретным временем 28 августа 22:15 и 08:40 у подъезда — cable scene до ветвления.
- Bold-разделители «Если платили вне площадки» / «Если платили внутри площадки» как decision tree для 08:40.

### Change
- Для fear-кластеров prepay/booking всегда ставить **fork в первые 2–3 абзаца**, не откладывать «мошенник или календарь» в середину.
- Support vs police — назвать канал сразу после классификации, не после utility-блоков.

### Never again
- Писать «уже занято» как единую историю обмана без ветки легитимного рассинхрона календарей.
- Смешивать фишинговую ссылку и Avito 6h cancel в одном абзаце без подзаголовка-развилки.

### Proposed apply
- Writer checklist (review-only): prepay/cancel hooks → dual-track opening + first H2 fork.
- Scout handoff для fear_prepay: логировать **fraud path vs platform-conflict path** как обязательные углы.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260829-1237-B04-six-hour-cancel-window-math
status: proposed
topic_id: B04
category: utility
confidence: medium

### Evidence
- artifact: title-brief.json#stickers + article.html H2 «Шесть часов, которые легко проспать»
  finding: concrete math — оплата 22:15 → окно до 04:15 → приезд 08:40 без бесплатной отмены; inline-03 alt дублирует таймлайн.
- metrika_signal: none (credentials BLOCKER; cannot validate scroll-to-H2)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Числовой таймлайн вместо абстрактного «есть 6 часов на отмену».
- Список тарифов Avito (1/3/5/7/14 дней, невозвратный, мгновенная бронь 2h / подтверждённая 12h) как utility-слой под таймлайном.
- Sticker «На Авито бесплатная отмена — 6 часов после оплаты» из title-brief → body proof.

### Change
- Для evening-pay / morning-arrival сценариев всегда считать **конец free-cancel окна vs время заезда** явно (не только «ночью оплатил»).
- Упоминать day-in-day exception (бронь день в день — без возврата) рядом с 6h rule.

### Never again
- Оставлять 6-часовое правило без привязки к часам оплаты и утреннего поезда/заезда.
- Обещать возврат «в каждом случае» при platform-conflict (статья честно: зависит от тарифа).

### Proposed apply
- Research/Writer: при Avito prepay темах включать **sample timeline** (оплата HH:MM → cancel deadline → arrival HH:MM) в research-notes.
- Description: не дублировать цифры H1 — держать «держу до полуночи» + вопрос про настоящую бронь (PASS в description-brief B04).

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260829-1237-B04-lk-not-chat-screenshot
status: proposed
topic_id: B04
category: utility
confidence: medium

### Evidence
- artifact: description-brief.json + article.html closing checklist item «Бронь видна в личном кабинете»
  finding: diagnostic question «где подтверждение — в ЛК или скрин в чате?» в conclusion + CTA MAX; contrasts chat image «бронь подтверждена» in lead.
- metrika_signal: none (credentials BLOCKER)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Один замок-вопрос в финале: ЛК vs картинка — повторяет description-brief без копипаста H1.
- Lead: картинка «бронь подтверждена» после списания по ссылке — контраст с настоящей записью в заказах.
- Sticker «Подтверждение брони — в личном кабинете, не скрин в мессенджере».

### Change
- Для prepay/fear тем выносить **LK-vs-screenshot check** в conclusion checklist (не только в description).
- CTA «напишите в MAX» привязать к спорному тезису (перевод на карту = красный флаг), не generic.

### Never again
- Принимать скрин «бронь подтверждена» или код двери как доказательство брони без записи в ЛК/заказах.
- Description дублировать H1 дословно (B04 description PASS — другой угол «держу до полуночи»).

### Proposed apply
- Description skill review: prepay fear → prefer chat-pressure phrase + LK diagnostic question.
- Interlink to B01 (код от чужой двери) как sibling proof «код ≠ бронь».

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260829-1237-B04-prepay-title-klyshin-fork
status: proposed
topic_id: B04
category: voice
confidence: low

### Evidence
- artifact: title-brief.json#pain_scene + rejected_variants
  finding: H1 «Перевёл предоплату… Утром её уже сдали» — Klyshin evening→morning rhythm; rejected copypaste hook and B01 «оплатил» overlap; «посуточно» holds Wordstat spine without raw P0 stuffing.
- metrika_signal: none (credentials BLOCKER; no CTR causal claim)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Две фразы через точку: вечернее действие (перевёл) → утренний поворот (уже сдали).
- Тюмень в lead, не в H1 (supply_vs_demand.city_in_h1=false).
- b04_delta vs B01–B03: отдельный глагол/объект конфликта (предоплата, не код/залог/расстояние).

### Change
- Fear_prepay titles: prefer **перевёл/оплатил вечером + утренний обрыв** over «N вопросов» / SEO tail.
- Wordstat spine «аренда квартиры посуточно» — через «посуточно» в H1, fear cluster в H2/body.

### Never again
- Дословная копия Klyshin hook в H1 (rejected: «Перевёл предоплату вечером. Утром — квартира уже занята»).
- H1-паттерн «5 вопросов» или «полный гайд» для cancel_prepay angle.

### Proposed apply
- Title skill: prepay/cancel cluster — evening action + morning «уже сдали/занята» with distinct verb from sibling topics.
- Scout: log original Klyshin hook + final P0 «аренда квартиры посуточно» (794 Tyumen) per handoff.

### Durable applied
- none

### Resolution
status: recorded
