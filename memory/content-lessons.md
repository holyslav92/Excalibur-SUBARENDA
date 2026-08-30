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

## LESSON-20260830-1343-B04-passport-order-not-binary
status: proposed
topic_id: B04
category: utility
confidence: medium

### Evidence
- artifact: title-brief.json#pain_scene
  finding: сцена «фото паспорта + селфи + перевод за ночь» до адреса; H2 «Паспорт сам по себе мошенничество не доказывает» — снятие бинарного «попросили = скам».
- artifact: article.html#h2-order
  finding: граница по порядку (адрес → даты/цена → бронь → данные → деньги), не по слову «паспорт».
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (INC-20260830-1343-metrika-credentials); causal CTR/retention не выводить.

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Открывающий nuance-блок: честный хост может просить данные для договора / консьержа — до красных флагов.
- Формулировка «по новым правилам вы обязаны загрузить паспорт» как давление, не как объяснение найма.
- Связка «полный паспорт + срочный перевод на карту физлица» как compound-risk, не отдельные «может быть норм» пункты.

### Change
- Для buyer-intent «паспорт при заселении посуточно» (P0 99 / secondary 52) сразу давать **порядок шагов**, а не только список red flags.
- Scout handoff: при hook про паспорт логировать sub-angle «order vs binary scam» рядом с final P0.

### Never again
- Заголовок или lead «попросили паспорт — мошенники» без оговорки про легитимный договор и пропускную систему.
- Смешивать гостиничную цифровую идентификацию с частным наймом без разведения контекстов.

### Proposed apply
- Writer checklist (review-only): passport/data темы → H2 «не бинарно» + H2 «порядок шагов» до чеклиста.
- Description (Дзен): держать контраст «сначала паспорт, потом адрес» — как в description-brief B04.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260830-1343-B04-address-before-data-refusal-script
status: proposed
topic_id: B04
category: structure
confidence: medium

### Evidence
- artifact: article.html#marina-case
  finding: кейс Марины (28.08 22:15, 4 ночи, общежитие до 1 сентября); отказный скрипт «адрес + созвон → бронь → данные»; исход «не потеряла ни ночей, ни данных, ни денег».
- artifact: cover/cover-text.json#inline_6
  finding: стикеры «адрес и созвон», «не доверяете?», «через 10 минут аккаунт молчит».
- metrika_signal: none (credentials unavailable)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Именованный протагонист с датой/временем и университетским контекстом (связка с B03 без дублирования «40 минут»).
- Короткий ответ-шаблон гостя в кавычках — copy-paste utility.
- Позитивный финал отказа: «квартира ушла» ≠ проигрыш, если сохранены документы и деньги.
- Вопрос-отмычка: «если откажусь — назовут адрес или начнут пугать?»

### Change
- Для pre-payment / data-risk тем всегда включать **готовую фразу ответа** и **ожидаемую реакцию скама** (обида, «отдаю другим», молчание).
- CTA «пришлите переписку» — до tenant-блока, не только в финале.

### Never again
- Писать passport-scam гайд только списком red flags без сценария «что сказать» и «что будет дальше».
- Заканчивать материал моралью «будьте осторожны» без именованного кейса с исходом.

### Proposed apply
- Sol/Writer: data-risk + urgency → один именованный кейс + refusal script + scam reaction timeline (≤3 сообщения).
- Cover-text: дублировать refusal-script стикером в inline_6 band.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260830-1343-B04-checkin-cluster-interlink
status: proposed
topic_id: B04
category: structure
confidence: medium

### Evidence
- artifact: interlink-gate.json
  finding: 3 outbound sibling: B03 (distance/«рядом»), B02 (код/дверь), B01 (залог) — PASS min 3.
- artifact: article.html#pre-arrival-checklist
  finding: interlink в блоке «вопросы, которые зададите потом, когда будет поздно» — контекстная кластеризация pre-check-in.
- metrika_signal: none (credentials unavailable)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Passport/data тема как **хаб** для sibling: расстояние (B03) + доступ (B02) + залог (B01) в одном utility-абзаце.
- Формулировка «на этапе проверки» — мост от паспорта к остальным рискам заселения.

### Change
- Для check-in / trust / payment-risk материалов планировать interlink-plan заранее как **check-in cluster** (distance + access + deposit + data).
- Не ограничиваться sibling только «паспорт/мошенничество» — расширять на operational risks заезда.

### Never again
- Outbound только на «похожие по ключу» без сценария «день приезда».
- Interlink в отдельном SEO-блоке «читайте также» вместо inline utility.

### Proposed apply
- Publish/interlink: при topic_id B04-подобных (data, trust, pre-payment) default cluster = B03+B02+B01 или актуальные published siblings из `shared/published-articles.md`.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260830-1343-B04-host-mirror-passport-trap
status: proposed
topic_id: B04
category: utility
confidence: medium

### Evidence
- artifact: article.html#h2-mirror-passport
  finding: H2 «Чужой паспорт в ответ тоже не является гарантией»; RT-контекст 5–30 тыс. ₽ и цена −20–30% как сигнал вместе с отсутствием адреса.
- artifact: research-agent-report.json#news_signals
  finding: RT 24.08.2026 депутат Панеш + мошенники квартиры/вузы — external anchor без выдуманных тарифов.
- metrika_signal: none (credentials unavailable)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Разбор «давайте я тоже пришлю паспорт» как false comfort — отдельный H2, не абзац внутри red flags.
- Проверочный чеклист вместо картинки: телефон = объявление, адрес, созвон, вид из окна, способ бронирования.
- Журналистский диапазон ущерба с оговоркой «не тариф» — честный research cite.

### Change
- Trust/scam темы: отдельный блок про **reciprocal document bait** до tenant CTA.
- При −20% цене в кейсе всегда связывать с compound flags (нет адреса, срочность, файл).

### Never again
- Считать фото паспорта хоста достаточным KYC для гостя.
- Использовать RT-суммы как обязательный размер ущерба без disclaimer.

### Proposed apply
- Research: для scam-angle подтягивать свежий RT/community signal (как B04 29–30.08.2026).
- Writer: reciprocal-passport trap → отдельный H2 в trust-кластере.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260830-1343-B04-title-dual-threat-hook
status: proposed
topic_id: B04
category: voice
confidence: low

### Evidence
- artifact: title-brief.json#h1
  finding: H1 «…под угрозой бронь и данные» — двойное последствие; rejected_variants избегают «что отвечать» в заголовке.
- artifact: description-brief.json
  finding: Klyshin case hook «Сначала паспорт, потом адрес»; not_equal_title PASS.
- metrika_signal: none (credentials unavailable; causal CTR не выводить)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Cable pain-scene в H1: просьба до оплаты + два риска (бронь + персональные данные).
- Description с цитатой-перевёртышем порядка, не дублирует H1.

### Change
- Для data/trust hooks повторять формулу «действие до оплаты → двойная ставка» вместо how-to в H1.

### Never again
- Заголовок-инструкция «что отвечать / что не слать» — оставлять utility в теле.

### Proposed apply
- Title skill review: pre-payment data risk → dual consequence (booking + data) over how-to headline.

### Durable applied
- none

### Resolution
status: recorded
