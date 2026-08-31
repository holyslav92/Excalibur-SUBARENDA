# Excalibur BLOG — content lessons

Активные и proposed уроки Content-learner (v2). Read-only для Writer/Sol.

---

## LESSON-20260831-1654-B05-boiler-on-wall-not-hot-now
status: proposed
topic_id: B05
category: utility
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: article.html §«Две отмычки», research-notes.md Wordstat, title-brief angle.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER по credentials.

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE

### Keep
- Разведение «бойлер есть» и «горячая вода будет прямо сейчас» — в §1 цитата «Горячая вода есть, заходите» vs факт пустого бака после предыдущих гостей.
- Две отмычки перед переводом: «Бойлер включён — или просто висит на стене?» + «Сколько минут горячей воды сейчас в баке и через сколько он нагреется, если я приеду поздно?»
- Klyshin-отрез «Нет. Так не заселяем.» + «Сначала проверка. Потом перевод.»
- Три сценария отказа (расходован запас / не нагрелся / неисправность) — не сводить всё к «маленькому баку».
- Wordstat P0 «бойлер горячая вода» 374 (Tyumen) + spine «квартиры посуточно тюмень» 5463.

### Change
- В boiler/STR-темах сразу в lead называть объём бака (50 л) и ориентир 10–15 мин / ~час нагрева — не прятать цифры в H2 «Что на самом деле происходит с баком».
- Хост-ответ шаблон: «50 литров, бойлер включён, бак полный, воды хватит на два душа» или «бак пустой, нагрев ~час» — до оплаты.

### Never again
- Принимать «горячая вода есть» / «всё есть, не переживайте» как ответ на вопрос о бойлере.
- Отправлять инструкцию PDF вместо статуса бака в момент, когда гость уже под холодной водой.
- How-to «как включить бойлер» без морали про обещание vs факт из крана.

### Proposed apply
- Scout: при hook sept_business_trip / late_checkin + boiler rework логировать final P0 «бойлер горячая вода» + late-arrival sub-angle.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260831-1654-B05-late-flight-boiler-preheat
status: proposed
topic_id: B05
category: structure
confidence: medium

### Evidence
- artifact: research-notes.md#reader_problem
  finding: поздний заезд после рейса + накопительный бойлер; article.html H2 «Две минуты…» и чат-переписка «мокрый стою».
- metrika_signal: none (credentials unavailable)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Слой «поздний рейс → код → сумка → сразу душ» поверх технического объяснения бака.
- Связка с B01 (бесконтактный заезд): чат = часть замка; инструкция не заменяет проверку перед душем.
- Вопрос-отмычка mid-body: «сорок минут ждать нагрев после позднего перелёта — нормально или перебор?» → TG/MAX.
- ₽ в opening (3 500 предоплатой) — арифметика боли, как в B04.

### Change
- Для late-checkin + boiler тем всегда включать **окно нагрева** (40–60 мин) в utility-блок рядом с кодами/залогом, не только «бойлер есть».
- Interlink: B01 codes + B02 deposit + B04 door fee как sibling «обещание → оплата → сюрприз».

### Never again
- Писать late-arrival материал только про код/домофон, игнорируя готовность горячей воды к первому душу.
- Считать «инструкцию отправил» достаточной защитой хоста при позднем заезде.

### Proposed apply
- Writer checklist (review-only): late_checkin + boiler → preheat window + two unlock questions в одном материале.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260831-1654-B05-two-minute-title-reveal
status: proposed
topic_id: B05
category: voice
confidence: low

### Evidence
- artifact: title-brief.json#klyshin_title_shape
  finding: H1 shape 2 «Горячая вода была. На второй минуте душ — холод»; description-brief not_equal_title PASS («После рейса… бойлер»).
- metrika_signal: none (credentials unavailable; causal CTR не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Cable pain-scene: обещание в прошлом («была») + измеримый контрфакт («вторая минута» / «холод»), без SEO-хвоста в H1.
- Cover hook «Вода кончилась прямо в душе» + sticky «А бойлер просто висит» — визуальный дубль H1, не дубль description.
- Lead opens with quoted host message «Горячая вода есть, заходите» — не дублирует H1 дословно.

### Change
- Повторять формулу «обещание в кавычках / прошлое → время/температура-контрфакт» для amenity-failure hooks (Wi‑Fi, вода, розетки).

### Never again
- Заголовок-спойлер со всей механикой («бойлер 50 л выключен после уборки») — оставлять раскрытие в lead/H2.

### Proposed apply
- Title skill review: amenity-failure — prefer two-beat time/temperature reveal over equipment spec in H1.

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
