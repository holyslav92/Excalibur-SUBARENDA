# Article style — язык и форма статьи

Правила для Title / Writer / Sol. Живой ритм — в `shared/SOUL.md` и `shared/soul-examples/`.

Язык: **русский** (`tenant-config.language=ru`).

**Длина:** ~**1100–1800 слов** — один CASE (~12–14 мин), не landing-checklist. Пустой how-to 3000w — бан.

**Дзен — поверхность дистрибуции:** карточка в ленте приводит трафик; статья на сайте должна стоять сама и конвертировать в TG/MAX.

**Dzen pattern 1** (N советов / N вопросов) — **NOT default**.

---

## GOOD vs BAD — H1 + §1 (gate calibration)

См. `shared/soul-examples/good-outputs.md` и `bad-outputs.md`. Gate: `scripts/excalibur_blog_case_delivery_gate.py`.

---

## CASE delivery — 10 правил (HARD, одна формулировка)

1. **§1 = плотный кейс.** 1–2 абзаца с цитатой, ₽/ночами, что сломалось. **BAN duty-log** (дата/часы/`HH:MM` в §1). **BAN** chopped 3-word lead.
2. **Identity** после лида: «Я хост посуточной в Тюмени. Это «Добрый дом».» + Telegram · MAX.
3. Reader is inside (you/present tense/body in apartment/taxi/chat).
4. Number = price of burn or fix (00:12, 4 ночи, 5 000 ₽). Ban H1 list numbers as skeleton.
5. Host dialogue in prose — quote then illusion break.
6. One case → one verdict. One red line with numbers. **BAN body-as-timeline** (multiple `HH:MM`). Checklist AFTER moral.
7. Moral: first X, then money/key.
8. One lockpick question.
9. One mid comment fight-question (TG/MAX).
10. Guest pain only — no ЕГРН/Шакин/риэлтор. Sol MUST NOT encyclopedia.

---

## Body devices (после dense §1, never instead)

| Device | Пример shape |
|--------|----------------|
| «Не X. Не Y. А Z.» | Не «рядом». Не «5 минут». А 40 минут пешком с чемоданом. |
| Degradation → moral | Сначала фото крана. Потом чат. Потом перевод. Не наоборот. |
| Direct speech | «Утром будет» — обещали в чате, а выезд уже завтра. |
| Refusal | «Так не заселяем.» / «Даже за двойную цену.» |
| Aphoristic close | «Наш вывод простой.» + one metaphor before CTA |

**BAN:** vertical ladder (1 sentence per line) as §1 — Klyshin TG rhythm is for **Title** two-beat, not article lead.

---

## Engagement (лайк + коммент + подписка)

| Паттерн | Где | Пример |
|---------|-----|--------|
| **Mid comment fight-question** | середина, 1 раз | «Залог 5 000 — норм или перебор?» → ответ в **TG** `t.me/Dobriy_dom_72` или MAX |
| **Ban** | anywhere | «напишите в комментариях» — WP без формы комментариев |
| **Illusion break** | после цитаты хоста | «Была. И она не соврала.» / «Нет. Так не работает.» |
| **Lockpick question** | после диалога | «Где бойлер?» / «Сколько минут пешком до вуза?» |
| **CTA TG/MAX** | **один блок в конце** | `t.me/Dobriy_dom_72`, MAX — без hard sell, без double CTA |

---

## Голос

- **Простой разговорный русский** — как объясняешь другу у двери.
- **Добрый дом:** тёплый хост посуточной аренды в **Тюмени** (supply). Не риэлтор, не Шакин.
- **Demand Wordstat:** RF-wide (225); **inventory** только Тюмень.
- H1 = cable pain-scene + consequence; **«Тюмень» в H1 не обязательна**.
- Комфорт+, не люкс. STRUCTURE как у сильных Dzen-кейсов — без чужих тем и лиц.

---

## Русский язык (HARD FAIL)

- **Пиши как гость говорит:** код, ключница, залог, подъезд, домофон. Без лишних англицизмов.
- **Запрещён канцелярит:** «осуществить заселение», «данный объект», «в рамках», «является»,
  «справочный характер», «не заменяет юридическую консультацию».
- **Ban openers:** TL;DR, chopped lead, «Разберём», «В этой статье», «что проверить первым».
- Без «полный гайд», «2026», SEO-хвостов в H1.
- **Ban H1 skeleton:** «5 вопросов», «7 шагов» as article structure.
- Без эмодзи. `dzen_rf_pack` — мат запрещён (`shared/dzen-content-rules.md`).

---

## Dzen feed — 5 паттернов (Scout → Title → Writer → Sol)

| # | Паттерн | Scout | Title | Writer / Sol |
|---|---------|-------|-------|--------------|
| 1 | **Нумерованный список** | **NOT default** | H1 с числом — rare | N пунктов only if H1 promises; not skeleton |
| 2 | **Живой кейс с суммами** | залог / предоплата / удержали | сумма в H1 | one case → one verdict |
| 3 | **Страх → сцена в §1** | risk money/housing | «залог 5 000 ₽: когда вернут» | плотный кейс, not how-to |
| 4 | **Контраст с ответом в лиде** | посуточно или отель | вердикт в первой фразе | математика после вердикта |
| 5 | **Локальный + сезонный** | район, 1 сент, окно брони | без «Тюмень» в H1 OK | supply только Тюмень |

Scout: prefer **2–5**. Title rides **Wordstat P0 demand**, not legal essay.

---

## Заголовок (H1)

- **Cable case + consequence** — как сильные Dzen-H1, но mapped to **guest daily-rental**:
  parents 1 Sept, deposit, parking, reviews, hot water, neighbors, dog.
- Примеры shape (свой текст): ««Рядом с вузом» — оказалось 40 минут пешком» ·
  «Залог 5 000 ₽: на выезде сказали — не вернём» · «Почти внесли предоплату — в объявлении не было парковки».
- Wordstat P0 — demand spine **под** H1, не сырая SEO-фраза.
- **Ban H1:** «5 вопросов», «7 шагов», «что проверить первым», «лучшие», «ТОП-10», юридические хвосты.

---

## Открытие (лид)

- **1–2 плотных абзаца** — весь кейс на первом экране (цитата, ₽/ночи, что сломалось).
- **BAN duty-log:** день недели, календарная дата, `HH:MM`, «Тюмень, двор» в первом ударе.
- **NO TL;DR.** NO «Быстрый инсайт».
- **BAN chopped lead:** telegram-cosplay («02:14. Тюмень. Сын рядом.») — 8+ коротких строк вместо абзаца.
- Короткие удары — **после** посаженного кейса.
- Следом — identity + Telegram · MAX.

---

## Writer.html — обязательные элементы (HARD)

Sol и гейты ожидают в черновике:

1. **Цитата** хоста или гостя в кавычках
2. **₽ или число ночей** (залог, доплата, срок брони)
3. **Один illusion break** («Нет. Так не…» / «Была. И не соврала.»)
4. **Один mid comment fight-question** (ответ в TG/MAX)

**BAN в §1:** день недели, календарная дата, часы `HH:MM`, duty-log stamp.

---

## CTA и воронка (HARD)

**Один блок полной воронки в конце** (голос хоста, не баннер):

TG `https://t.me/Dobriy_dom_72` + MAX `https://max.ru/id660300569233_biz` +
сайт `https://добрыйдом-72.рф/` + booking + tel **+7 (993) 574-83-22** + менеджер `https://t.me/Dobriy_dom_Tyumen`

**Перекрёстные ссылки:** **3–4** уникальные живые `/blog/` URL (разные slug, HTTP 200).

**Бан:** double CTA, воронка в §1, ЕГРН, нотариус, суд, Шакин, риэлтор, +7 922 001 65 05, WhatsApp.

---

## Self-check

1. §1 = плотный кейс на первом экране, NO chopped lead, NO TL;DR?
2. Identity one-liner + Telegram · MAX после лида?
3. Reader inside (you/taxi/chat/apartment)?
4. One case → one verdict; checklist/FAQ AFTER moral only?
5. Date/time + quote + ₽/nights + illusion break + mid fight-question? (no date/clock in §1)
6. One lockpick question?
7. **Один** CTA-блок в конце (не два)?
8. ~1100–1800 слов, not encyclopedia?
