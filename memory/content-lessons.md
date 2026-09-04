# Excalibur BLOG — content lessons

Активные и proposed уроки Content-learner (v2). Read-only для Writer/Sol.

---

## LESSON-20260904-1337-B10-hot-water-exists-not-ready
status: proposed
topic_id: B10
category: utility
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json отсутствует; gate SKIP. Урок из publish-артефактов: title-brief.json, article.html §1–3, description-brief.json PASS, scout handoff wordstat_rework.
- metrika_signal: none — YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID не заданы; ingest BLOCKER по credentials.

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- LOW_SAMPLE

### Keep
- Two-beat H1 ««Горячая вода есть». Включили душ — лёд и 40 минут нагрева»: цитата обещания → контрфакт (лёд + таймер), не how-to.
- §1: после дороги на машине, ~10 мин до душа, бойлер OFF, ~40 мин нагрева; цитата гостя «Я же с дороги, думал, уже всё включено»; идентичность хоста после лида.
- H2 ««Есть» — не значит «готово прямо сейчас»»: разведение «оборудование есть» vs «душ готов»; сентябрьский контекст (городские отключения ГВС к концу августа → лёд скорее квартира/бойлер).
- Вопрос-отмычка mid-body: «Где бойлер и как включить ДО душа?» → TG/MAX, не комментарии.
- Klyshin: «Нет. Так не заселяем.» + «Сначала проверка. Потом перевод.» / «Сначала кран и бойлер — потом ключ и ночь».
- Sibling interlink: B09 parking «слово есть, действия не описаны»; B07 «кухня есть»; B08 предоплата/тишина; B06 первые часы брони.
- Wordstat P0 «квартиры посуточно тюмень» 5320 Tyumen / 11765 RU; supporting «бойлер горячая вода» 419 / «нет горячей воды квартира» 34.

### Change
- В hot-water/boiler кейсах в §1 сразу фиксировать: городское ГВС или бойлер, кто включает до заезда, ожидаемое время нагрева (цифра минут) — не только «горячая вода есть».
- Description (Дзен) держать сцену «после дороги → лёд → 40 минут», не дублировать H1 (description-brief PASS).

### Never again
- How-to «как включить бойлер» до морали / чеклист вместо кейса у душа.
- Обещание «горячая вода есть» без различения «прибор» vs «готово к заселению».
- Игнорировать сезон: в начале сентября лёд в кране чаще бойлер/режим, не городское отключение.

### Proposed apply
- Scout: при hook hot_water_boiler логировать final P0 spine + lockpick «Где бойлер и как включить ДО душа?» в handoff.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260904-1337-B10-case-delivery-heading-shipped
status: proposed
topic_id: B10
category: structure
confidence: medium

### Evidence
- artifact: case-delivery-gate.json#errors
  finding: gate BLOCK на banned stamp «Наш вывод простой.» в writer.html и article.html; статья опубликована с этим H2 (live-page PASS). Повтор паттерна B08 (LESSON-20260903-0602-B08-prepayment-silence-chat).
- metrika_signal: none (credentials unavailable)

### Named blockers
- EVIDENCE_SKIPPED
- METRIKA_UNAVAILABLE
- CASE_DELIVERY_GATE_OVERRIDE (BLOCK ignored at publish)

### Keep
- Чеклист из 7 пунктов после финального H2 — utility без how-to в opening.
- Метафора «пустой бак с красивой крышкой» перед чеклистом.

### Change
- Enforce case-delivery gate перед publish: «Наш вывод простой.» → «Мой вывод как практика» (один раз) или rerun Sol/Writer.
- assembled-sol-inputs.md не должен mandate banned heading при manner_canon dobry_dom_gen_only_human_v1.

### Never again
- Ship при case-delivery BLOCK на conclusion heading — второй подряд кейс (B08, B10).
- Writer/Sol inputs с user slot «Наш вывод простой.» при активном manner_canon ban.

### Proposed apply
- Publish preflight: fail on case-delivery BLOCK (не только live-page/cover).
- Human decision: обновить assembled-writer/sol inputs template vs manner_canon.
- Durable candidate после 2-го повтора (B08+B10) — needs-human, не auto Writer prompt.

### Durable applied
- none

### Resolution
status: needs-human

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

### Proposed apply
- Cover canon: при gen_only slice4 документировать допустимость копий inline для publish-слота 7.
- Review only; Writer prompt не трогать автоматически.

### Durable applied
- none

### Resolution
status: recorded
