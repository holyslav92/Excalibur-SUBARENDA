# Cover-text inputs — B05

tenant: ПКОМПАНИЯ «Добрый дом», Тюмень, посуточная аренда
season: начало сентября 2026, без снега/зимы
topic_id: B05

## Output contract (HARD)

Return ONLY valid JSON (no markdown fences, no commentary) matching:

```json
{
  "hook": "...",
  "highlight": "...",
  "sticky": "...",
  "wordstat_stickers": ["...", "..."],
  "inline_labels": {
    "inline_1": ["...", "..."],
    "inline_2": ["...", "..."],
    "inline_3": ["...", "..."],
    "inline_4": ["...", "..."],
    "inline_5": ["...", "..."],
    "inline_6": ["...", "..."],
    "inline_7": ["...", "..."]
  }
}
```

Rules:
- hook: 2–8 words, Cyrillic cable guest pain scene. NOT copy H1 verbatim.
- highlight: exactly ONE word FROM hook (pink on cover).
- sticky: ≤5 words, illusion break / reaction sticker.
- wordstat_stickers: 1–3 guest queries from Wordstat Tyumen (below). NO ЕГРН/риэлтор.
- inline_labels: 2–6 labels per inline_1…inline_7, each 1–4 words, facts from article.
- NO host face in hook. NO +7 922 001 65 05.
- Phone +7 (993) 574-83-22 is painted IN SCENE by Cover agent — do NOT add pill field.

## title-brief.json

```json
{
  "h1": "Рейтинг 4,8. Два «всё супер» — и 3 900 ₽ под вопросом",
  "title": "Квартиры посуточно в Тюмени: рейтинг 4,8 и два «всё супер»",
  "subject": "Отзывы о квартире посуточно перед предоплатой",
  "angle": "Гостю важны не только звёзды, но и свежесть, повторяемость и конкретика отзывов на Avito и Суточно: два одинаковых «всё супер» не объясняют, за что платить 3 900 ₽ за ночь."
}
```

## Wordstat Tyumen (live, guest queries)

- квартиры посуточно тюмень — 5463
- снять квартиру посуточно в тюмени — 1754
- авито квартиры посуточно тюмень — 335
- квартиры посуточно в тюмени недорого — 442

## article.html facts for inline panels

inline_1 — два отзыва «всё супер, рекомендую» слово в слово; рейтинг 4,8; двушка у аквапарка; 3 900 ₽ за ночь
inline_2 — за цифрой 4,8: среднее арифметическое; «Проживание состоялось» и «Не удалось заселиться»; «Не договорились» отдельно
inline_3 — с 15.06.2023 онлайн-бронь на Авито обязательна; после брони сервис просит отзыв; короткие однотипные фразы
inline_4 — два одинаковых отзыва — сигнал проверить, не накрутка; полезный отзыв: район, заселение, фото, чистота, ответ хозяина
inline_5 — вопрос-отмычка: «Что именно было „супер“ — заселение, чистота или только 4,8?»; попросить свежее фото кухни/окна
inline_6 — предоплата, залог, что входит в 3 900 ₽; доплаты за гостей; сохранить договорённости в переписке
inline_7 — сначала проверка, потом деньги и ключ; пять минут переписки дешевле 3 900 ₽; +7 (993) 574-83-22

## H1 (do not copy as hook)

Рейтинг 4,8. Два «всё супер» — и 3 900 ₽ под вопросом

## Good hook examples (style)

- «Два „всё супер“ — и 3 900 ₽»
- «Рейтинг 4,8 — отзывы пустые»
- «Звёзды есть — деталей нет»

## BAN

English headlines, SEO dumps, realtor/ЕГРН stickers, invented numbers not in article, Avito as Latin brand in hook.
