# Writer inputs — B03

topic_id: B03
article_dir: memory/blog/articles/B03-kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki
tenant: ПКОМПАНИЯ «Добрый дом», Тюмень, посуточная аренда, комфорт+
H1 (already chosen, do NOT repeat as h1 tag): Привезли сына к вузу — «рядом» оказалось 40 минут пешком

## Output contract

Write ONLY clean HTML fragment to drafts/writer.html:
- NO `<h1>` (Sol adds it)
- ~1100–1800 words Russian
- dzen_pattern 5 (local seasonal before 1 Sept) + 2 (live case with minutes)
- One case → one verdict; checklist AFTER moral
- All facts ONLY from research-notes.md below — do NOT invent

## Voice (HARD)

- От лица ПКОМПАНИИ «Добрый дом», хост посуточной в Тюмени
- Клышинская подача: cable pain-scene, illusion break, lockpick question
- Простой язык; НЕ адвокат, НЕ ЕГРН, НЕ суд, НЕ «мы лучшие», НЕ бизнес-класс
- Angle: **минуты пешком до конкретного корпуса** — NOT beds, NOT «три остановки кровати»
- Anti-dup B01 (codes/check-in), B02 (deposit/scratch)

## Mandatory writer.html elements (HARD)

1. Date or time in opening (e.g. «27 августа, 19:20»)
2. Quote from host or guest in quotes
3. ₽ or number of nights (2–4 nights from research)
4. One illusion break after host quote («Нет. Так не…» / «Была. И не соврала.»)
5. One mid comment fight-question (answer in TG or MAX)

## Opening (HARD)

- §1 = 1–2 dense paragraphs: whole case on first screen (parents, son, «рядом с вузом», 40 min walk reality)
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
Weave naturally (e.g. parents also need check-in instructions or deposit clarity) — NOT forced list.

## FIGURE placeholders

Insert `<!-- FIGURE inline_N -->` before major H2 sections (inline_1 … inline_7) like sibling articles.

## title-brief.json summary

```json
{
  "h1": "Привезли сына к вузу — «рядом» оказалось 40 минут пешком",
  "angle": "Проверка пешего маршрута до конкретного корпуса вуза до оплаты брони",
  "pain_scene": "Родители бронируют жильё на 2–4 ночи по обещанию «рядом с вузом», а после приезда выясняют, что до нужного корпуса нужно идти 40 минут.",
  "checks": [
    "Уточнить конкретный корпус вуза, а не только название университета",
    "Построить на карте именно пеший маршрут от квартиры до корпуса",
    "Не считать три остановки на транспорте признаком пешей доступности"
  ]
}
```

## research-notes.md (ONLY fact source)

# Research notes — B03

research_date: 2026-08-28  
topic_id: B03  
tenant: Добрый дом (ПКОМПАНИИ), Тюмень, посуточная аренда  
season_context: август 2026, бронь перед 1 сентября; родители с будущим студентом на 2–4 ночи

## reader_problem

Родители приезжают в Тюмень с будущим студентом на 2–4 ночи для оформления документов и ориентировки, находят объявление «рядом с вузом», но не проверяют, о каком именно корпусе идёт речь. В результате квартира может оказаться не в пешей доступности, а в трёх остановках от нужного адреса. Дополнительный риск перед 1 сентября — просьба срочно перевести предоплату до просмотра и проверки условий.

## reader_outcome

Читатель до оплаты сопоставит адрес квартиры с адресом конкретного корпуса на карте, проверит маршрут в режиме «пешком», уточнит у арендодателя корпус и время заселения, а также не будет переводить деньги только из-за обещаний «рядом с вузом» или «цена только сегодня».

## practical_facts

- У ТюмГУ несколько адресов корпусов: ул. Володарского, 6; ул. Ленина, 16, 23 и 38; ул. Семакова, 18; ул. Пржевальского, 37/1; ул. 8 Марта, 2 (официальный сайт utmn.ru).
- Учебно-лабораторный корпус № 1 ТюмГУ — ул. Республики, 9 (страница «Кампус» на utmn.ru; материал 72.ru от 15.08.2025 о вводе корпуса в канун учебного года).
- В Тюмени корпуса разных вузов разнесены по городу. Для ТИУ, ТюмГНГУ, ТюмГМУ и колледжей в объявлениях часто встречаются районы 50 лет Октября и Мельникайте — это не гарантирует близость к конкретному корпусу.
- Формулировка «рядом с вузом» может обозначать район, остановку с названием вуза или фактическую пешую доступность — это не одно и то же.
- Проверка маршрута: открыть Яндекс Карты, 2ГИС или карту площадки; указать адрес квартиры и адрес нужного корпуса; выбрать режим «пешком»; зафиксировать минуты и расстояние.
- До оплаты письменно уточнить: конкретный корпус, адрес квартиры, даты оформления, время заезда и выезда.
- В объявлениях встречается заезд с 14:00 и выезд до 12:00 (пример: gorkvartira.ru/object/300428) — согласовать, если семья приезжает утром или уезжает после оформления.
- «Три остановки» — маршрут на транспорте, а не расстояние пешком.
- На tyumen.sutochno.ru и агрегаторах (Avito, Циан, Яндекс Недвижимость) есть поиск по карте, но объект всё равно нужно сопоставлять с **нужным** корпусом, а не с «вузом» в общем.
- По 5-tv.ru (21.08.2026): перед учебным годом мошенники используют низкую цену, ремонт и «рядом с вузом», после чего требуют предоплату. Безопасная рекомендация: не переводить деньги до просмотра и проверки документов/условий, если формат бронирования это допускает.
- Цены из выдачи — ориентир рынка. В SERP Яндекс Недвижимости встречалась отметка «от 1,5 тыс. руб.» — не переносить на все объекты и не на «Добрый дом» без актуальной брони.

## surprising_fact

У ТюмГУ нет одного адреса «для всех занятий»: корпуса на Володарского, Ленина, Семакова, Пржевальского, 8 Марта и учебно-лабораторный корпус № 1 на Республики, 9. Квартира может быть «рядом с ТюмГУ» в рекламном смысле, но далеко от нужного корпуса пешком.

## fresh_signal_note

- Клышин 26.08.2026: «на красивой презентации продают ЖК, юридически покупаете договор и риски» — редакционный перенос: «рядом с вузом» проверять маршрутом пешком до корпуса.
- 5-tv.ru 21.08.2026: сезон студенческой аренды; мошенники — низкая цена + «рядом с вузом» + предоплата; «никаких денег до просмотра».

## BAN

ЕГРН, нотариус, суд, Шакин by name, риэлтор, WhatsApp, +7 922 001 65 05, «мы лучшие», «№1», бизнес-класс, invented prices for Добрый дом, beds/sleeping angle

## CTA links (only these)

- https://t.me/Dobriy_dom_72
- https://t.me/Dobriy_dom_Tyumen
- https://max.ru/id660300569233_biz
- https://добрыйдом-72.рф/
- https://добрыйдом-72.рф/booking/
- tel:+79935748322 display +7 (993) 574-83-22

## Moral / verdict shape

First: map + corpус name + minutes on foot. Then: money/key/booking.
Lockpick question example: «Сколько минут пешком до вашего корпуса?»
