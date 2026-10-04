# Title task — B45

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Сгенерируй **один** two-beat stop-factor H1 для guest-night CASE (посуточная аренда, Тюмень).

## Handoff H1 direction (two beats — СВОЙ финальный текст, без копипаста Scout)
Первый удар: в спешке **оплатили короткую поездку** (2 ночи), **ссылку на правила дома не открыли** (страх потерять бронь).
Второй удар: **на выезде** в переписке — **штраф/претензия за мусор и посуду**, угроза удержать депозит; правила всплыли постфактум (редакционный composite-кейс).

**Ритм-ориентир (не копировать дословно):** «Оплатили две ночи. На выезде прислали штраф за мусор — правила не читали».

**BAN в H1:** `HH:MM`, how-to, «5 вопросов», topic label, host-operator, ЕГРН/ипотека/Клышин/+79032334201.
**Нужны:** слово **«посуточно»** в H1; **цифра** — `2` ночи и/или ₽ (не выдавать 2000–5000 ₽ как «норму Тюмени»).
**Shape:** **не** scene как у B44 («В чате посуточно…») — предпочти fork / quote-first / number-first / dialogue.
**Не клонировать:** B23 уборка/простыни 1 800 ₽ на выезде; B29 «оплатили 2 ночи» + бухгалтерия; B44 залог/заморозка; B40 предоплата до кода.

## Case spine (research-notes)
- Скорость бронирования ≠ отмена опубликованных правил
- Мусор/посуда vs «уборка включена» — разные споры
- Угроза удержания депозита, не факт удержания
- Не тариф «Добрый дом», не штраф Кисловодска

## Wordstat P0 (demand spine)
- final P0: «квартиры посуточно тюмень» — 3889 (55+11176) | 8881 (225)
- supporting: «правила проживания посуточно» — 387 (225); angle only, не SEO-хвост в H1

## Klyshin hook
- hot_booking_skip_house_rules | dzen_pattern: **2** (case with sums/nights)
- klyshin_title_shape: **6** (fork) or **1** (quote-first про правила/мусор)

## Published titles (anti-dup — только заголовки)
B23: уборка включена → 1 800 ₽ простыни на выезде
B29: оплатили 2 ночи → чек «не гостиница»
B44: в чате залог → заморозка 11 400
B33: Авито оплачено → второй перевод

## HARD gates для H1
- Two beats: `.` `—` `:` contrast + figure (**2 ночи** или ₽)
- ~40–70 символов (max gate ~85)
- Аудитория: гость
- NOT how-to

## slug (ОБЯЗАТЕЛЬНО)
posutochno-tyumen-pravila-prozhivaniya-shtraf-musor-vyezd

## Выход — ТОЛЬКО валидный JSON, без markdown:
{
  "topic_id": "B45",
  "h1": "...",
  "title": "...",
  "slug": "posutochno-tyumen-pravila-prozhivaniya-shtraf-musor-vyezd",
  "subject": "...",
  "angle": "...",
  "h1_shape": "fork",
  "klyshin_title_shape": 6,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS",
  "generated_via": "excalibur_blog_derouter_opus_chat.py --role title"
}
