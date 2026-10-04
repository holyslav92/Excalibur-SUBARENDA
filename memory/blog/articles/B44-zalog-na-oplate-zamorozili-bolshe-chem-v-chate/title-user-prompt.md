# Title task — B44

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Сгенерируй **один** two-beat stop-factor H1 для guest-night CASE (посуточная аренда, Тюмень).

## Handoff H1 direction (two beats — СВОЙ финальный текст, без копипаста Scout)
Первый удар: в **чате** обещали небольшой **залог 3 000 ₽** (посуточно).
Второй удар: на экране **оплаты** банк показывает **заморозку 11 400 ₽**, **код заселения ещё не прислали** (редакционный composite-кейс, hold ≠ «списали залог»).

**BAN в H1:** `HH:MM`, how-to, «5 вопросов», topic label, host-operator, ЕГРН/ипотека/Клышин.
**Нужны цифры** 3 000 ₽ и 11 400 (или 11 400 ₽) и слово **«посуточно»** в H1.
**Shape:** scene / dialogue («в чате» → «на оплате») — **не** клон B32 («В карточке… На оплате…» без залога/кода).
**Не копировать** дословно: B34 залог у двери, B40 перевод до кода, B08 тишина в чате.

## Case spine (research-notes)
- Hold на карте больше, чем «залог» в переписке; код ещё нет
- Не named-площадка, не «Добрый дом» как факт инцидента
- P0 demand: «квартира посуточно залог»

## Wordstat P0 (demand spine)
- final P0: «квартира посуточно залог» — 22 (55+11176); live vs handoff 17
- supporting: «посуточно комиссия» 1769 (225) — контекст checkout, не SEO-хвост в H1

## Klyshin hook
- deposit_before_keys | dzen_pattern: 2
- dzen_shape_hint: «В чате 3 000 — на оплате заморозили 11 400, код ещё не прислали»
- klyshin_title_shape: **2** (number-first) or **6** (scene «в чате»)

## Published titles (anti-dup — только заголовки)
B32: карточка 3 400 → оплата 8 816 за две ночи
B34: фильтр без залога → 5 000 у двери
B40: без предоплаты в фильтре → 3 200 до кода
B08: 3 000 предоплата → тишина в чате
B22: оплатили 3 ночи → код не пришёл

## HARD gates для H1
- Two beats: `.` `—` `:` contrast + figures **3 000** and **11 400**
- ~40–70 символов (max gate ~85)
- Аудитория: гость
- NOT how-to

## slug (ОБЯЗАТЕЛЬНО)
posutochno-tyumen-v-chate-zalog-3000-bank-zamorozil-11400

## Выход — ТОЛЬКО валидный JSON, без markdown:
{
  "topic_id": "B44",
  "h1": "...",
  "title": "...",
  "slug": "posutochno-tyumen-v-chate-zalog-3000-bank-zamorozil-11400",
  "subject": "...",
  "angle": "...",
  "h1_shape": "scene",
  "klyshin_title_shape": 6,
  "wordstat_p0": "квартира посуточно залог",
  "verdict": "PASS",
  "generated_via": "excalibur_blog_derouter_opus_chat.py --role title"
}
