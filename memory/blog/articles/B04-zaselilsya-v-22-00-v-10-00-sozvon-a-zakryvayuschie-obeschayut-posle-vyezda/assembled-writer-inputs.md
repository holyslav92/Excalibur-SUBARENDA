# Writer inputs — B04

topic_id: B04
article_dir: memory/blog/articles/B04-zaselilsya-v-22-00-v-10-00-sozvon-a-zakryvayuschie-obeschayut-posle-vyezda
tenant: ПКОМПАНИЯ «Добрый дом», Тюмень, посуточная аренда, комфорт+
H1 (already chosen, do NOT repeat as h1 tag): Заселился в 22:00. В 10:00 созвон — закрывающие обещают после выезда

## Output contract

Write ONLY clean HTML fragment to drafts/writer.html:
- NO `<h1>` (Sol adds it)
- ~1100–1800 words Russian
- dzen_pattern 2 (live case with sums/time) + 3 (fear→scene in §1)
- One case → one verdict; checklist AFTER moral
- All facts ONLY from research-notes.md below — do NOT invent

## Voice (HARD)

- От лица ПКОМПАНИИ «Добрый дом», хост посуточной в Тюмени
- Клышинская подача: cable pain-scene, illusion break, lockpick question
- Простой язык; НЕ адвокат, НЕ ЕГРН, НЕ суд, НЕ «мы лучшие», НЕ бизнес-класс
- Angle: **стол + Wi‑Fi + закрывающие до оплаты** — NOT розетка (WP duplicate)
- Anti-dup B01 (codes/check-in), B02 (deposit), B03 (walk to university)

## Mandatory writer.html elements (HARD)

1. Date or time in opening (e.g. «29 августа, 22:10»)
2. Quote from host or guest in quotes
3. ₽ or number of nights (2 nights from research)
4. One illusion break after host quote («Нет. Так не…» / «Была. И не соврала.»)
5. One mid comment fight-question (answer in TG or MAX)

## Opening (HARD)

- §1 = 1–2 dense paragraphs: whole case on first screen (command trip, 22:00 check-in, 10:00 video call, closing docs promised after checkout)
- NO chopped telegram-cosplay lead
- After lead: identity «Я хост посуточной в Тюмени. Это «Добрый дом».» + mention Telegram · MAX

## Funnel placement (HARD — user override)

1. **After checklist block** → link https://t.me/Dobriy_dom_72 (channel, save checklist)
2. **After «у нас так» / how we work block** → MAX https://max.ru/id660300569233_biz OR manager https://t.me/Dobriy_dom_Tyumen
3. **Final block**: phone <a href="tel:+79935748322">+7 (993) 574-83-22</a>, booking/site https://добрыйдом-72.рф/ and https://добрыйдом-72.рф/booking/
4. One full funnel at end (TG + MAX + site + tel + manager) — no double glued CTAs elsewhere

## Interlink (interlink_old_articles=true)

Include **1–3 contextual** sibling links to published articles (relative /blog/ paths OK):
- B01: /blog/beskontaktnoe-zaselenie-posutochno-tyumen/ — «Оплатил квартиру посуточно. Код прислали от чужой двери»
- B02: /blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/ — «Снял квартиру посуточно. Залог не вернули — нашли скол на плите»
- B03: /blog/kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki/ — «Привезли сына к вузу — «рядом» оказалось 40 минут пешком»
Weave naturally (e.g. late check-in codes, deposit on checkout, verifying conditions before pay) — NOT forced list.

## FIGURE placeholders

Insert `<!-- FIGURE inline_N -->` before major H2 sections (inline_1 … inline_7) like sibling articles.

## title-brief.json summary

```json
{
  "h1": "Заселился в 22:00. В 10:00 созвон — закрывающие обещают после выезда",
  "angle": "Klyshin-ритм: ночной заезд и утренний созвон, второй удар — обещание закрывающих только после выезда (риск для авансового отчёта). Стол + Wi‑Fi + чек/акт до оплаты.",
  "pain_scene": {
    "setup": "командированный снимает квартиру на 2 ночи, заселяется около 22:00",
    "turn": "утром в 10:00 обязательный видеосозвон, закрывающие обещают только после выезда",
    "conflict": "к сроку авансового отчёта (3 рабочих дня) чек и акт могут не успеть; Wi‑Fi и стол не проверены до оплаты"
  }
}
```

## research-notes.md (ONLY fact source)

# Research notes — B04

research_date: 2026-08-30  
topic_id: B04  
tenant: Добрый дом (ПКОМПАНИИ), Тюмень, посуточная аренда  
season_context: лето 2026, командировка на 2 ночи, поздний заезд ~22:00, видеосозвон в 10:00

## reader_problem

Командированный сотрудник приезжает в Тюмень на две ночи поздно вечером, примерно к 22:00, а утром в 10:00 должен подключиться к обязательному видеосозвону. До оплаты он может не проверить, есть ли в квартире рабочие стол и стул, выдержит ли Wi‑Fi видеозвонок именно в нужной комнате и сможет ли арендодатель выдать бухгалтерии подходящие закрывающие документы. После перевода денег изменить условия или получить недостающие документы бывает сложнее.

## reader_outcome

Читатель поймёт, что до перевода нужно письменно уточнить наличие стола и стула, проверить Wi‑Fi, выяснить статус арендодателя и заранее согласовать пакет документов для бухгалтерии. Обещание «документы потом» не равно полученному комплекту.

## practical_facts

- В опубликованных правилах объектов и гостиниц часто встречается расчётное время: заезд после 14:00–15:00, выезд до 12:00. У «Добрый дом» на карточке Otello (ул. Кармацкого, 5) указаны заезд с 15:00 и выезд до 12:00.
- Заселение около 22:00 оставляет мало времени на проверку квартиры перед утром. Ранний заезд и поздний выезд рекомендуется согласовывать заранее.
- В описании «Добрый дом» упоминаются Wi‑Fi и бесконтактное заселение; также заявлены предварительные условия оплаты и быстрый ответ в мессенджере. Это описание бренда, а не гарантия одинаковых условий во всех объектах.
- Формулировка «есть Wi‑Fi» не показывает фактическую скорость и стабильность связи в конкретной комнате. Проверять соединение разумно там, где будет стоять рабочее место.
- По требованиям Zoom для видеосвязи 720p ориентир: индивидуальный звонок — около 1,2 Мбит/с; групповой — около 2,6 Мбит/с на отдачу и 1,8 Мбит/с на загрузку. Для 1080p — до 3,8 Мбит/с (support.zoom.com KB0058323).
- Наличие рабочего стола и стула нужно запрашивать отдельно.
- Для отчётности по проживанию обычно нужны договор, акт приёма-передачи или оказанных услуг и платёжный документ. Конкретный комплект следует сверить с бухгалтерией работодателя.
- Для самозанятого одного договора может быть недостаточно: нужен чек из приложения «Мой налог». Обещание выслать чек позже не заменяет сам чек.
- Для физлица — договор и расписка; для ИП или ООО — договор, акт, счёт и кассовый чек или БСО.
- В договоре желательно заранее зафиксировать адрес, даты, стоимость, реквизиты и срок выдачи платёжных документов.
- Переписка в мессенджере помогает зафиксировать договорённости, но сама по себе не заменяет документы для бухгалтерии.
- Авансовый отчёт подаётся в течение трёх рабочих дней с даты возвращения (п. 23 ПП РФ №501 от 16.04.2025). Если чек или акт обещаны только после выезда, сотрудник может не успеть к этому сроку.
- Сделки между гражданами на сумму свыше 10 000 рублей требуют простой письменной формы (ст. 161 ГК РФ).
- Работодатель компенсирует расходы при наличии подтверждающих документов (ст. 168 ТК РФ).
- «Добрый дом» позиционирует объекты для командировок. На карточке Otello заявлены отчётные документы, но условия конкретной квартиры нужно проверять до бронирования.
- Цены из тизера «2 ночи в командировке: отель 6 800 ₽ или квартира 4 200 ₽» — пример, не единый тариф.

## surprising_fact

Для самозанятого арендодателя договор без чека из «Мой налог» может оказаться недостаточным для бухгалтерии. Обещание «чек и документы вышлем позже» не подтверждает, что расходы примут.

## fresh_signal_note

- gazeta-unp.ru 05.08.2026 — пакет закрывающих документов при посуточной аренде в командировке.
- @Dobriy_dom_72 август 2026 — Wi‑Fi в дальней комнате, проверка условий до оплаты.
- @klyshin_A август 2026 — редакционный перенос: «сначала деньги/документы под контролем, потом сделка»; «на презентации продают одно, по факту покупаете другое».

## BAN

ЕГРН, нотариус, суд, Шакин by name, риэлтор, WhatsApp, +7 922 001 65 05, «мы лучшие», «№1», бизнес-класс, розетка angle, invented prices for Добрый дом

## CTA links (only these)

- https://t.me/Dobriy_dom_72
- https://t.me/Dobriy_dom_Tyumen
- https://max.ru/id660300569233_biz
- https://добрыйдом-72.рф/
- https://добрыйдом-72.рф/booking/
- tel:+79935748322 display +7 (993) 574-83-22

## Moral / verdict shape

First: desk + chair + Wi‑Fi speed at workspace + closing docs package BEFORE payment. Then: money/key.
Lockpick question example: «Где будет стоять ноутбук — и какая скорость Wi‑Fi именно там?»
