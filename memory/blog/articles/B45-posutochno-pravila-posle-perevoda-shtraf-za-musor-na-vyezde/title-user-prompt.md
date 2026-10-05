# Title task — B45

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Сгенерируй **один** two-beat stop-factor H1 для guest-night CASE (посуточная аренда, Тюмень).

## Handoff H1 direction (two beats — СВОЙ финальный текст, без копипаста Scout)
Первый удар: **оплатили две ночи** посуточно, деньги ушли — **PDF с правилами прислали только после перевода** (в чат).
Второй удар: на **выезде** потребовали **3 800 ₽** за мусорные пакеты — в **карточке** такого пункта не было (редакционный composite-кейс).

**BAN в H1:** `HH:MM`, how-to, «5 вопросов», topic label («О правилах…»), host-operator, ЕГРН/ипотека/Клышин, скелет «Сняли квартиру посуточно. Хотели X. У двери: +₽».
**Нужны цифры:** **2 ночи** (или «две ночи») и **3 800 ₽**; слово **«посуточно»** обязательно в H1.
**Shape:** dzen_pattern 2 — case with sums; prefer **host_wrote** / **scene** («после перевода» → «на выезде»), **не** клон B23 (уборка/простыни 1 800), B17 коммуналка, B44 hold/залог.
**Не копировать** дословно Scout: «Оплатили две ночи. Правила прислали после перевода. На выезде — 3 800 за пакеты» — перефразируй, сохрани два удара.

## Case spine (research-notes)
- rules_before_keys: правила и порядок мусора — до оплаты, не PDF после перевода
- 3 800 ₽ — только заголовочный ориентир, не тариф Тюмени
- Не named-площадка, не «Добрый дом» как факт инцидента
- Не уводить в залог/холд/коммуналку

## Wordstat P0 (demand spine)
- final P0: «правила проживания посуточно» — 380 (225); Тюмень 55+11176: 4 (актуальный замер)
- spine: «квартиры посуточно тюмень» — 3874 (55+11176)
- supporting: «штраф посуточно» — 168 (225) — контекст, не SEO-хвост в H1

## Klyshin hook
- rules_before_keys | original: «Сначала правила. Потом ключ. Не наоборот.»
- dzen_pattern: 2 | dzen_shape_hint: «Оплатили две ночи. Правила — после перевода. На выезде 3 800 за пакеты»
- klyshin_title_shape: **2** (number-first) or **5** (scene)

## Published titles (anti-dup — только заголовки)
B23: уборка включена → 1 800 ₽ простыни на выезде
B17: коммуналка включена → 1 840 ₽ на выезде
B29: оплатили 2 ночи → бухгалтерия и чек
B31: оплатили 3 ночи → чужие чемоданы
B35: PDF инструкция → не тот подъезд
B44: залог в чате → заморозка 11 400, кода нет

## HARD gates для H1
- Two beats: `.` `—` `:` `?` contrast + figures **две ночи** and **3 800**
- ~40–70 символов (max gate ~85)
- Аудитория: гость
- NOT how-to, NOT «разберём»

## slug (ОБЯЗАТЕЛЬНО)
posutochno-pravila-v-chate-posle-oplaty-shtraf-za-musor

## Выход — ТОЛЬКО валидный JSON, без markdown:
{
  "topic_id": "B45",
  "h1": "...",
  "title": "...",
  "slug": "posutochno-pravila-v-chate-posle-oplaty-shtraf-za-musor",
  "subject": "...",
  "angle": "...",
  "h1_shape": "scene",
  "klyshin_title_shape": 5,
  "wordstat_p0": "правила проживания посуточно",
  "verdict": "PASS",
  "generated_via": "excalibur_blog_derouter_opus_chat.py --role title"
}
