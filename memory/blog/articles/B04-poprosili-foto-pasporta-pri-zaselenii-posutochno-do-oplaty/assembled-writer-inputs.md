# Writer inputs — B04

topic_id: B04
article_dir: memory/blog/articles/B04-poprosili-foto-pasporta-pri-zaselenii-posutochno-do-oplaty
tenant: «Добрый дом», Тюмень, посуточная аренда, комфорт+
H1 (already chosen, do NOT repeat as h1 tag): Попросили фото паспорта до оплаты — под угрозой бронь и данные

## Output contract

Write ONLY clean HTML fragment to drafts/writer.html:
- NO `<h1>` (Sol adds it)
- ~1100–1800 words Russian
- dzen_pattern 3 (fear → dense case in §1) + 2 (live case with nights/₽)
- One case → one verdict; checklist AFTER moral
- All facts ONLY from research-notes.md below — do NOT invent

## Voice (HARD)

- От лица компании «Добрый дом», хост посуточной в Тюмени
- Клышинская подача: burn scene §1, short paragraphs, illusion break, lockpick question, refusal beat
- Простой язык; НЕ адвокат, НЕ ЕГРН, НЕ суд, НЕ «мы лучшие», НЕ бизнес-класс
- Angle: просьба фото паспорта в чате **до** оплаты, адреса и ясных условий
- Anti-dup B01 (codes/check-in), B02 (deposit/scratch), B03 (distance to university)

## Mandatory writer.html elements (HARD)

1. Date or time in opening (e.g. «28 августа, 22:15»)
2. Quote from host or guest in quotes
3. ₽ or number of nights (use research-safe numbers only — e.g. nights before 1 Sept, RT scam range 5–30 тыс. as journalistic context only)
4. One illusion break after host quote («Нет. Так не…» / «Была. И не соврала.»)
5. One mid comment fight-question (answer in TG or MAX)

## Opening (HARD)

- §1 = 1–2 dense paragraphs: whole case on first screen (chat, passport photo request before payment, threat to lose booking)
- NO chopped telegram-cosplay lead
- After lead: identity «Я хост посуточной в Тюмени. Это «Добрый дом».» + mention Telegram · MAX

## Funnel placement (HARD — user override)

Embed funnel IN TEXT (not banner at end only):
1. **After checklist block** → link https://t.me/Dobriy_dom_72 (channel, save checklist)
2. **After «у нас так» / how we work block** → MAX https://max.ru/id660300569233_biz OR manager https://t.me/Dobriy_dom_Tyumen
3. **Final block**: phone <a href="tel:+79935748322">+7 (993) 574-83-22</a>, booking/site https://добрыйдом-72.рф/ and https://добрыйдом-72.рф/booking/
4. One full funnel at end (TG + MAX + site + tel + manager) — woven in prose, no double glued CTAs

## Interlink (interlink_old_articles=true)

Include **1–3 contextual** sibling links to published articles:
- B01: /blog/beskontaktnoe-zaselenie-posutochno-tyumen/ — «Оплатил квартиру посуточно. Код прислали от чужой двери»
- B02: /blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/ — «Снял квартиру посуточно. Залог не вернули — нашли скол на плите»
- B03: /blog/kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki/ — «Привезли сына к вузу — «рядом» оказалось 40 минут пешком»
Weave naturally (e.g. before paying also check check-in codes, deposit, address) — NOT forced list.

## FIGURE placeholders

Insert `<!-- FIGURE inline_N -->` before major H2 sections (inline_1 … inline_7) like sibling articles.

## title-brief.json summary

```json
{
  "h1": "Попросили фото паспорта до оплаты — под угрозой бронь и данные",
  "angle": "Гость получает просьбу прислать паспорт раньше понятных условий и оплаты и рискует одновременно бронью и персональными данными.",
  "pain_scene": "Перед поездкой хост просит фото паспорта в чате до оплаты, адреса и ясной договорённости. Гость боится отказаться и потерять квартиру, но не хочет отправлять документы незнакомцу."
}
```

## research-notes.md (ONLY fact source)

# research-notes.md

## season_context
Август 2026 года, период перед учебным сезоном. Гость бронирует посуточное жильё в переписке и получает просьбу прислать фото паспорта до оплаты.

## reader_problem
Гость не понимает, является ли просьба прислать фото паспорта до перевода денег обычной процедурой хоста или признаком мошенничества, и боится одновременно потерять деньги и передать незнакомцу лишние персональные данные.

## reader_outcome
Гость сможет отличить нормальный порядок оформления от подозрительной схемы, проверить хоста и объект до отправки документов, а также выбрать менее рискованный способ передачи данных.

## practical_facts
- Запрос паспортных данных при посуточном найме сам по себе не доказывает мошенничество: хосту могут понадобиться данные для договора краткосрочного найма, идентификации гостя, передачи сведений консьержу или фиксации ответственности за имущество.
- Ключевой вопрос — не только «нужен ли паспорт», но и когда, кому и каким способом его отправляют.
- Более безопасный порядок: сначала согласовать даты и точный адрес, проверить хоста и объект, оформить бронь или договорённость, затем передать только необходимые данные для договора.
- Просьба прислать паспорт до любого подтверждения объекта и условий — тревожный признак, особенно если адрес, даты и сведения о хосте ещё не подтверждены.
- Повышенный риск возникает при связке «фото паспорта + срочный перевод на карту физлица». Передача одновременно документа и денег лишает гостя возможности спокойно проверить контрагента.
- Дополнительные красные флаги: просьба отправить документ «менеджеру» в другой чат или по незнакомой ссылке; требование полного комплекта страниц; требование селфи с паспортом без понятного объяснения; давление вроде «ещё двое смотрят, решайте сейчас»; слишком низкая цена и отсутствие точного адреса; предложение оплатить бронь до просмотра, договора или подтверждения через площадку.
- До проверки можно не отправлять полный скан. Варианты если согласовано с хостом: ФИО и серию/номер текстом после подтверждения брони; показать оригинал при заселении; только нужный разворот с пометкой «Только для договора найма с [название/ФИО], даты [даты]»; форма проверенной площадки.
- На изображении закрыть данные, которые не нужны для цели. Водяная пометка не делает файл полностью безопасным, но снижает риск повторного использования.
- Если документ уже отправлен — удалить сообщение, попросить собеседника удалить файл, сохранять переписку.
- Фото паспорта от «арендодателя» не подтверждает честность: мошенники могут использовать чужие или поддельные документы (RT).
- Проверка хоста: совпадение телефона с объявлением; точный адрес и даты; созвон; готовность показать детали квартиры; понятный способ бронирования; отсутствие давления.
- Сезонный риск перед учебным годом: объявления рядом с вузами, низкая цена, «эксклюзивный просмотр», срочный залог/бронь, потом пропадают.
- Не переходить по ссылкам «банка» или «бронирования» от незнакомца в чате.
- Правила гостиниц (цифровой ID 2026) нельзя автоматически переносить на квартиру посуточно у частного хоста.
- Суммы 5–30 тыс. рублей — только как диапазон из журналистского комментария RT о схемах обмана, не как рыночный тариф.
- Цены на 20–30% ниже рынка — сигнал из RT о мошенничестве в аренде.

## surprising_fact
Даже снимок паспорта, который прислал сам арендодатель в качестве «гарантии», ничего не доказывает: мошенники могут использовать чужой или поддельный документ.

## BAN
ЕГРН, нотариус, суд, Шакин by name, риэлтор, WhatsApp, +7 922 001 65 05, «мы лучшие», «№1», бизнес-класс, invented prices for Добрый дом

## CTA links (only these)
- https://t.me/Dobriy_dom_72
- https://t.me/Dobriy_dom_Tyumen
- https://max.ru/id660300569233_biz
- https://добрыйдом-72.рф/
- https://добрыйдом-72.рф/booking/
- tel:+79935748322 display +7 (993) 574-83-22

## Moral / verdict shape
First: dates + address + verify host/object. Then: booking agreement. Then: passport data (minimal). Then: money/key.
Lockpick question example: «Какой разворот вам нужен для договора — и можно показать при заселении?»
Refusal beat: guest can refuse full scan before verification without being «rude».
