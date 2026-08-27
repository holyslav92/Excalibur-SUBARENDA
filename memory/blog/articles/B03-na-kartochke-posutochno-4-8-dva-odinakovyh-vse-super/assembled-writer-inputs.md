# Writer B03 — meaning draft (Derouter Opus only)

## Task
Write MEANING draft for `drafts/writer.html`. Topic B03 — отзывы и рейтинг при выборе квартиры посуточно.
**Facts ONLY from research-notes.md below.** Do NOT invent ratings, review counts, prices, or platform stats not in research.

## H1 (fixed — do NOT output `<h1>` in draft)
Выбрал квартиру с оценкой 4,8. Перед оплатой нашёл одинаковые отзывы

## Dzen pattern
**Case with sums/dates** (pattern 2): one guest case → one verdict. NOT numbered-list skeleton. NOT «5 вопросов» / «7 шагов».

## Voice (HARD)
- **Delivery:** Klyshin rhythm — short blows after dense case, scene first, «вот где подставят», practical verdict
- **Meaning:** host посуточной в **Тюмени**, бренд **«Добрый дом»**, comfort+, «как для своих»
- **NOT:** юрист, риэлтор, Шакин, ЕГРН, нотариус, суд, «мы лучшие», бизнес-класс, люкс, мрамор
- Simple spoken Russian. Reader inside the scene (you / present tense / chat / phone screen).

## CASE delivery — 10 rules (HARD)
1. **§1 = 1–2 плотных абзаца** — whole case on first screen: date, city, quote, ₽/ночи, what broke. NO chopped 3-word lead. NO TL;DR.
2. **Identity after lead:** «Я хост посуточной в Тюмени. Это «Добрый дом».» + Telegram · MAX (mention channels, not full funnel dump).
3. Reader is inside (you/present tense/body in apartment/taxi/chat).
4. Number = price of burn (₽, nights, minutes). Ban H1 list numbers as skeleton.
5. Host dialogue in prose — quote then **illusion break** (one: «Нет. Так не…» / «Была. И не соврала.»).
6. One case → one verdict. Retell with timeline. **Checklist AFTER moral**, never as spine.
7. Moral: first understand reviews, then pay.
8. One **lockpick question** (e.g. «Жалоба на шум из отзывов ещё актуальна?»).
9. One **mid comment fight-question** (e.g. «4,8 с копипастой — доверяете или нет?») — answer in TG or MAX.
10. Guest pain only — no encyclopedia dump.

## Mandatory elements in HTML (HARD)
1. **Date or time** in opening (e.g. «26 августа, 23:40»)
2. **Quote** host or guest in quotation marks
3. **₽ or number of nights** (booking cost, nights, deposit — from case, not invented)
4. **One illusion break**
5. **One mid comment fight-question**

## Length
~**1100–1800 words** — развёрнутый CASE. Not checklist-landing 2500+.

## Funnel in BODY (mandatory — NOT banner dump at end)
a) **After the practical checklist** (order of checking reviews before payment): one line like
   «Полный порядок проверки — в канале» with link **https://t.me/Dobriy_dom_72**
b) **After block «у нас так» / how we work in Добрый дом** (reviews, responses, transparency):
   mention **MAX https://max.ru/id660300569233_biz** OR manager **https://t.me/Dobriy_dom_Tyumen** —
   we answer in messenger before you pay, not after problems

**End (short, not a link banner):** booking **https://добрыйдом-72.рф/booking/** or site **https://добрыйдом-72.рф/**, phone **+7 (993) 574-83-22**

## Interlink (1–3 published siblings — contextual only)
- B01: https://добрыйдом-72.рф/blog/beskontaktnoe-zaselenie-posutochno-tyumen/ — only if заселение/связь из отзывов, без повторения угла B01
- B02: https://добрыйдом-72.рф/blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/ — only if спор/залог из отзывов, без повторения угла B02
Do NOT duplicate B01/B02 topics as main spine.

## H2 candidates (from title-brief — tighten, develop case)
- Почему 4,8 на Авито и 9+ на Суточно.ру — не одна и та же оценка
- Что скрывается в блоке «Отзывы без оценки» на Авито
- Как отличить живой отзыв от шаблона «всё супер»
- Низкие оценки: что искать в отзывах 1–3 звёзды
- Свежесть важнее среднего балла
- Ответы хозяина: реакция или отписка «робота»
- Посуточно Тюмень: что спросить в чате до оплаты
- Как мы в «Добрый доме» смотрим на отзывы → **MAX/manager funnel hook after this block**

## Structure order
1. Dense case lead (§1)
2. Identity line
3. H2 sections developing the case (platform rules woven in, not term dump)
4. Moral / verdict (one case → one verdict)
5. Practical checklist (7 steps from research — AFTER moral)
6. **TG funnel** after checklist
7. «У нас так» block → **MAX/manager funnel**
8. Short closing + booking/phone (no double CTA banner)

## Output format
- HTML fragment ONLY: **NO `<h1>`**, NO markdown fences, NO `<figure>` tags
- Allowed tags: h2, h3, p, b, i, a, ul, ol, li, blockquote
- Place `<!-- FIGURE inline_N -->` comments where Sol will add images (optional, 3–5 markers)

## BANNED
ЕГРН, нотариус, суд, «я адвокат», «Разберём», «В этой статье», WhatsApp, Шакин, +7 922 001 65 05,
«мы лучшие», бизнес-класс, chopped telegram-cosplay lead, FAQ as spine, research date in lead,
claiming Dobry Dom has specific rating/review count without research proof,
saying identical reviews prove fake reviews (research: not proof of накрутка)

---

## research-notes.md (facts source)

### reader_problem
Гость в Тюмени открывает карточку на Авито или Суточно.ру: 4,8 и десяток «всё супер», но до предоплаты непонятно — реальные ли отзывы, что в низких оценках, насколько свежие.

### reader_outcome
За 5–10 минут до оплаты: низкие оценки, повторяющиеся жалобы, шаблоны, свежесть, ответы хозяина, разница Авито vs Суточно.ру.

### practical_facts (use in prose)
- Читать отзывы 1–3 звёзд; искать повторяемость (шум, вода, ключи, фото, заселение)
- Один повторяющийся негатив важнее единичной эмоции
- Смотреть даты; годичный отзыв ≠ сейчас; несколько отзывов в один день — повод присмотреться (не доказательство накрутки)
- Шаблон «всё супер» без деталей — сигнал, но короткий живой отзыв тоже бывает
- Ответы арендодателя: спокойный ответ по существу = хозяин не игнорирует
- Спросить до брони: «Жалоба на [шум/воду/ключи] из отзывов ещё актуальна?»

**Авито:**
- Шкала 1–5, рейтинг = среднее; у частников с первой оценки, у компаний после третьей; у объекта — после 3 отзывов
- Одна «2» может снизить 5,0 до 3,5 (официальный пример Авито)
- 4 типа отзывов: «Проживание состоялось», «Не удалось заселиться», «Не договорились», «Не общались»
- В рейтинг входят только первые два типа
- «Не договорились» и «Не общались» — блок «Отзывы без оценки», на звёзды не влияют
- С 15.06.2023 онлайн-бронь обязательна для посуточных на Авито; после брони платформа запрашивает отзыв
- Модерация; фейки — удаление, блокировка 90 дней; шаблонные одинаковые ответы хозяина = «робот» (официально Авито)
- На негатив — ответ в сутки; обжалование — до 3 календарных дней
- Переписка в чате платформы, не WhatsApp

**Суточно.ру:**
- Шкала до 10; фильтр «9+»; «Суперхозяева»
- «4,8» Авито и «9+» Суточно — разные шкалы, сравнивать нельзя
- Отзыв только после брони через сервис; модерация и платежи
- 27.08.2026: 2 479 отзывов 9,0+ за месяц на votes page; свежие — июль 2026
- 14 дней на отзыв после выезда; публикация одновременно после проверки; 30 дней на ответ хозяина

**Если отзывов нет:** Отелло (июнь 2026) — у части апартаментов отзывы недоступны; не заменять отсутствие отзывов предположением

**Порядок проверки (checklist after moral):**
1. Средняя оценка + число отзывов
2. Низкие оценки + «Отзывы без оценки» на Авито
3. Повторяющиеся темы: чистота, шум, вода, фото, заселение, связь
4. Свежесть и группировка дат
5. Ответы хозяина
6. Один конкретный вопрос в чат до оплаты
7. Переписка на платформе

**Локальный:** Wordstat «квартиры посуточно тюмень» 5675 (снимок запросов, не бронирования). Не заявлять рейтинг/число отзывов «Добрый дом» без подтверждения.

**surprising_fact for prose:**
- Два отзыва «Не договорились» видны, но не снижают рейтинг
- Авито предупреждает хозяев про одинаковые ответы как «робота»
- 4,8 и 9+ — разные шкалы

## published-titles-only (anti-dup — do not repeat angles)
- B01: бесконтактное заселение / код от чужой двери
- B02: залог не вернули / скол на плите
