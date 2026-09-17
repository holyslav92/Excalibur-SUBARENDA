# Title task — B26

Сгенерируй **один** two-beat stop-factor H1 для guest-night CASE (посуточная аренда, Тюмень, «Добрый дом»).

## Handoff draft (СОХРАНИТЬ механику — свой текст, не копипаст Klyshin)
«На карточке — 4 200 за ночь. Отель рядом — 4 800. Счёт на две ночи — 13 400»

**Обязательно:** гость сравнил цену за ночь (квартира дешевле отеля), но полный счёт за **две ночи** с уборкой, бельём и сервисным сбором перевернул выбор. Цифры из editorial case — не выдавать как проверенную квитанцию в H1, но **13 400**, **4 200**, **4 800**, **две ночи** — якоря для gate.

**Figure для gate (ОБЯЗАТЕЛЬНО):** ₽ (4 200 / 4 800 / 13 400) и/или «две ночи» / «2 ночи». **BAN HH:MM** в H1.

## Case spine (Scout + research)
- Guest in Tyumen, 2 nights; flat card 4 200 ₽/night vs hotel 4 800 ₽/night — flat looks cheaper per night
- After booking: service fee + linen kit + mandatory cleaning → total 13 400 ₽ instead of expected 8 400 ₽
- Angle: **hotel_vs_daily** — compared one line in card, not full trip budget
- Host line (for article, not necessarily in H1): «Это стандартные доплаты, они указаны»
- NOT B23 checkout cleaning hold; NOT B24 child fee; NOT B25 sleeping places; NOT B22 door/code/passport; NOT deposit return plot (B02)
- Focus: money contrast flat vs hotel **before payment**, full bill for 2 nights

## Wordstat P0 (demand spine)
- final P0: «квартиры посуточно тюмень» (4570, regions 55+11176) / 9844 RU
- supporting: «отели тюмень» 7141 (55+11176); «квартира посуточно или отель» 283 (225)
- H1 = CASE wound; P0 в title/meta опционально, не SEO-хвост в H1

## Klyshin hook
- hotel_vs_daily | original: «Считали квартиру дешевле отеля. На две ночи — на 2 900 ₽ дороже»
- dzen_pattern: 4 — денежный контраст в кейсе с двумя ночами
- shape hint: 5 (цифра = цена ожога) или 3 (прямая речь + вскрытие) или 1 (обыденное → катастрофа)

## Published titles (anti-dup)
B07: «кухня есть» / кафе 7 200 ₽
B10: «всё включено» / такси 2 400 ₽
B23: «уборка включена» / 1 800 ₽ на выезде
B24: «можно с детьми» / доплата за ребёнка
B25: две кровати на фото / диван и матрас

## HARD gates для H1
- Two beats minimum: `.` `—` `:` «Только» «А потом» — [normal]. Then [horror/number/quote]
- Target shape like: «На карточке — 4 200 за ночь. Отель рядом — 4 800. Счёт на две ночи — 13 400» (можно сжать до 2 ударов, но сохранить контраст ночь vs полный счёт)
- BAN: как снять, что проверить, N советов/шагов, разберём, how-to, topic label, ЕГРН, наследство, ипотека, Клышин, +79032334201
- ~40–70 символов (gate min 28, max 85)
- Аудитория: **гость**, бронирующий ночь — не host-operator
- Свой текст — не копировать @klyshin_A

## slug (для title-brief)
kvartira-posutochno-tyumen-deshevle-otelya-schet-dve-nochi

## Выход — ТОЛЬКО валидный JSON, без markdown:
{
  "topic_id": "B26",
  "h1": "...",
  "title": "...",
  "slug": "kvartira-posutochno-tyumen-deshevle-otelya-schet-dve-nochi",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 1-10,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
