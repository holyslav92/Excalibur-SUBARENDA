# Cover-text assembled inputs B03

OUTPUT: **ONLY** valid JSON object for `cover/cover-text.json`. No markdown fences. No commentary.

## Task
Write exact Russian inscriptions for quad cover (hook + sticky + wordstat_stickers + inline_labels for inline_1..inline_7).
Image model renders ONLY these strings. Simple spoken Russian — guest pain, not SEO jargon.

## Topic
- topic_id: B03
- subject: отзывы и рейтинг при выборе квартиры посуточно на Авито и Суточно.ру
- H1 (reference — do NOT copy hook verbatim): Выбрал квартиру с оценкой 4,8. Перед оплатой нашёл одинаковые отзывы

## Case facts from article.html (use in hook/labels)
- 26 августа 23:40, Андрей, Тюмень, 4 ночи, 3 200 ₽/сутки, 12 800 ₽ всего
- Карточка: рейтинг 4,8, 11 отзывов, все «всё супер»
- Три отзыва одной датой; хозяин 11 раз ответил одинаково: «Спасибо, ждём вас снова!»
- Avito 1–5 vs Sutochno.ru до 10 / «9+» — разные шкалы
- Блок «Отзывы без оценки» — два «Не договорились», не влияют на 4,8
- Один вопрос хозяину до оплаты лучше десяти шаблонов
- Moral: сначала понять отзывы, потом платить
- Читать сначала 1–2–3 звезды, потом остальное

## Season / scene canon (HARD)
- **Late summer:** 27 августа 2026, YEKT — тёплый свет, конец лета
- **NOT winter:** no snow, no frost, no «минус 25 °C», no frozen keybox
- Cover phone **in-scene only:** +7 (993) 574-83-22 (лента/магнит/экран — Cover agent places it; do NOT add phone field to JSON)
- **Logo:** factory paste PNG top-right — **NOT** in cover-text.json, do NOT invent logo_lockup

## Wordstat stickers (live Tyumen 11176 + RF — guest queries only)
Use 1–3 of these exact phrases in `wordstat_stickers`:
- «квартиры посуточно тюмень» — 5675 Tyumen
- «снять квартиру посуточно в тюмени» — 1819 Tyumen
- «суточно ру отзывы» — demand spine (RF 3715)
- «авито посуточно отзывы» — 374 RF

NOT: ЕГРН, суд, риэлтор, SEO tails.

## inline_labels mapping (7 panels — facts from article)
- **inline_1:** Avito 4,8 vs Sutochno 9+ — разные шкалы, не сравнивать
- **inline_2:** «Отзывы без оценки», «Не договорились», не в рейтинг
- **inline_3:** 11 одинаковых ответов хозяина, копипаста ≠ накрутка
- **inline_4:** сначала 1–2–3 звезды, темы: шум, вода, ключи
- **inline_5:** три отзыва одной датой, свежесть важнее среднего
- **inline_6:** один вопрос в чат до оплаты, переписка на площадке
- **inline_7:** порядок проверки 5–10 минут, Добрый дом — ответы руками

## JSON schema (strict)
```json
{
  "hook": "2–8 words, cable guest-pain, NOT H1 copy",
  "highlight": "one word FROM hook (pink accent)",
  "sticky": "≤5 words reaction / illusion break",
  "wordstat_stickers": ["1–3 phrases"],
  "inline_labels": {
    "inline_1": ["2–6 labels, 1–4 words each"],
    "inline_2": [...],
    "inline_3": [...],
    "inline_4": [...],
    "inline_5": [...],
    "inline_6": [...],
    "inline_7": [...]
  }
}
```

## Gate rules (must PASS) — HARD
- hook 2–8 words, Cyrillic, highlight substring of hook
- sticky ≤5 words
- each inline_N: 2–6 labels, **each label STRICTLY 1–4 words** (count every token; «один и тот же текст» = 5 words = FAIL), ≤28 chars
- Previous FAIL: inline_3.label «один и тот же текст» — 5 words. Shorten all labels to max 4 words.
- Cyrillic only (Latin only whitelisted brands — none needed here)
- NO host face in hook text
- NO +7 922 001 65 05

## BANNED in strings
ЕГРН, нотариус, суд, риэлтор, зимние образы, «накрутка доказана», English headlines.
