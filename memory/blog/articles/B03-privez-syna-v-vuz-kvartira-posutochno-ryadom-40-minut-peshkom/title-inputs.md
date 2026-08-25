# Title inputs B03

## Task
Invent ONE catchy H1 for Excalibur BLOG / tenant «Добрый дом» (посуточная аренда, Тюмень).
Output **ONLY** valid `title-brief.json` — a single JSON object, no markdown wrapper, no commentary.

Required fields: `topic_id`, `h1`, `title`, `subject`, `angle`, `verdict` ("PASS").

## topic_id
B03

## Scout handoff (klyshin_hook)
- hook family: parents_sept_uni
- original: «Привёз сына в вуз. Три ночи. В объявлении — „рядом с вузом“.»
- angle: 2–4 ночи на оформление в сентябре, не годовая аренда; проверять реальный маршрут до нужного корпуса, а не только слово «рядом»
- lockpick question: «Сколько минут пешком до корпуса?»
- title_draft (reference rhythm, NOT copy): «Привёз сына в вуз на три ночи: „рядом“ оказалось 40 минут пешком»

## Wordstat P0 (demand spine under H1 — do NOT paste raw phrase into H1)
- P0: «квартиры посуточно тюмень» — 5875 (regions 55+11176)
- P1: «снять квартиру посуточно в тюмени» — 1902
- clusters tried: multi-day rental, vuz proximity, daily Tyumen, посуточно Tyumen spine

## dzen_pattern
5 — локальный сезонный кейс (parents + university + short stay)

## dzen_shape_hint
Родитель приехал с сыном в Тюмень на 2–4 ночи для оформления в вуз; в объявлении было «рядом», но до нужного корпуса оказалось 40 минут пешком — сначала проверяем маршрут, потом оплачиваем бронь.

## Reader pain (from research-notes.md)
- Parent books 2–4 nights for university paperwork / student pack / waiting for dorm
- Listing says «рядом с вузом» but doesn't name which campus/building
- Result: ~40 minutes on foot to the actual building they need
- Moral: first check route to exact corpus address, then pay

## Constraints
- Klyshin cable pain-scene: short punch, scene in H1, strong verb, guest pain only
- ~50–70 characters
- «Тюмень» in H1 optional — no SEO stuffing
- NO: «полный гайд», «2026», «5 вопросов», «7 шагов», «ТОП-10», «лучшие», ЕГРН, наследство, ипотека, Шакин, риэлтор
- NO label head («Проверка заселения», «Как выбрать квартиру»)
- NO SEO tail / keyword dump («квартиры посуточно тюмень» as raw H1 phrase)
- NOT duplicate of published titles (see below)
- Do NOT plagiarize @klyshin_A posts — own text, same rhythm

## Anti-dup (published titles only)
| topic_id | title |
|----------|-------|
| B01 | Оплатил квартиру посуточно. Код прислали от чужой двери |
| B02 | Снял квартиру посуточно. Залог не вернули — нашли скол на плите |

B03 must NOT repeat B01 (code/check-in) or B02 (deposit) angles.

## Good H1 patterns for this topic (prefer pattern 5 — local seasonal case)
- Two short beats: action → twist («Привёз сына…» / «„рядом“ — 40 минут пешком»)
- Number = price of burn: 40 minutes, 3 nights — NOT list skeleton
- Lockpick lives in article, not as «N вопросов» in H1

## slug_draft (for reference)
privyoz-syna-v-vuz-ryadom-okazalos-40-minut-peshkom

## subject hint
родитель с сыном, посуточная квартира на 2–4 ночи к вузу; «рядом» ≠ нужный корпус — проверять маршрут пешком до оплаты
