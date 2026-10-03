# Title task — B43

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Сгенерируй **один** two-beat stop-factor H1 для guest-night CASE (посуточная аренда, Тюмень, «Добрый дом»).

## Handoff H1 direction (two beats — СВОЙ финальный текст, без копипаста Scout)
Первый удар: в поиске/фильтре отмечено удобство **«детская кроватка»** (семья с ~1-летним ребёнком, посуточно).
Второй удар: после заезда в **чате** — кроватку **привезут только завтра**, отдельно **2 500 ₽**; первую ночь ребёнок без готового спального места (редакционный composite-кейс).

**BAN в H1:** `21:40`, любое `HH:MM`, how-to, «5 вопросов», topic label.
**Нужна цифра** (2 500 ₽) и слово **«посуточно»** в H1 (или явно в формулировке аренды).
**Shape:** scene / dialogue (чат, фильтр) — **не** повторять host_wrote как у B42 («Хозяин ответил…»).
**Не копировать** дословно: B34 «без залога у двери», B24 «можно с детьми» у двери.

## Case spine (research-notes)
- Фильтр «детская кроватка» ≠ кроватка в квартире к моменту заезда
- Отдельная цена, срок «завтра», бельё уточнять отдельно
- Не тариф «Добрый дом», не средняя по Тюмени

## Wordstat P0 (demand spine)
- final P0: «квартиры посуточно тюмень» — 3963 (55+11176) | 8919 (225)
- узкий: «квартира посуточно с детской кроваткой» — 37 (angle only, не SEO-хвост в H1)

## Klyshin hook
- crib_filter_promise | dzen_pattern: 2 (case with sums)
- klyshin_title_shape: **5** (scene) or **3** (dialogue in chat)

## Published titles (anti-dup — только заголовки)
B24: «можно с детьми» + 1 500 ₽ у двери
B25: две кровати на фото → диван
B34: фильтр «без залога» → 5 000 ₽ у двери
B42: двушка → кладовая за дверью

## HARD gates для H1
- Two beats: `.` `—` `:` contrast + figure **2 500 ₽**
- ~40–70 символов (max gate ~85)
- Аудитория: гость
- BAN: ЕГРН, наследство, ипотека, Клышин, +79032334201

## slug (ОБЯЗАТЕЛЬНО)
posutochno-tyumen-v-filtre-detskaya-krovatka-v-chate-zavtra-za-2500

## Выход — ТОЛЬКО валидный JSON, без markdown:
{
  "topic_id": "B43",
  "h1": "...",
  "title": "...",
  "slug": "posutochno-tyumen-v-filtre-detskaya-krovatka-v-chate-zavtra-za-2500",
  "subject": "...",
  "angle": "...",
  "h1_shape": "scene",
  "klyshin_title_shape": 5,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS",
  "generated_via": "excalibur_blog_derouter_opus_chat.py --role title"
}
