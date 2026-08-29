# Cover-text inputs — B04

tenant: ПКОМПАНИЯ «Добрый дом», Тюмень, посуточная аренда
season: **лето**, конец августа, жара, утренний поезд в Тюмень, спешка перед заездом
topic_id: B04
cover_season_note: Summer season cover — светлая high-key сцена, солнечный блик, летний вайб (не зима/снег)

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
- inline_labels: 3–6 labels per inline_1…inline_7, each 1–4 words, facts from article.
- NO host face in hook. NO +7 922 001 65 05.
- Logo: factory paste PNG top-right empty pad — Cover agent, NOT in this JSON.
- Phone +7 (993) 574-83-22: painted IN SCENE (tape/magnet/screen/лента) by Cover agent — in-scene only, NEVER on logo pad, NO pill/post-composite field in JSON.

## title-brief.json

```json
{
  "h1": "Перевёл предоплату за квартиру посуточно. Утром её уже сдали",
  "angle": "вечернее действие — утренний обрыв; предоплата vs «уже сдали»",
  "pain_scene": {
    "setup": "гость в спешке переводит предоплату вечером",
    "turn": "утром «уже сдали» / чужие жильцы у подъезда",
    "conflict": "мошенничество, двойная бронь или рассинхрон календарей"
  },
  "wordstat": {
    "spine": "аренда квартиры посуточно — 794",
    "clusters": ["предоплата", "отмена брони посуточно", "аренда квартиры тюмень посуточно"]
  }
}
```

## Wordstat Tyumen (live MCP-KV, regions 55+11176)

- аренда квартиры посуточно — 794
- аренда квартиры тюмень посуточно — 208
- авито аренда квартир посуточно — 42
- договор посуточной аренды квартиры — 44

Guest-query stickers (pick 1–3, readable on cover):
- аренда квартиры тюмень посуточно
- авито аренда квартир посуточно
- аренда квартиры посуточно

## article.html facts for inline panels (match FIGURE slots)

inline_1 — два маршрута «уже сдали»: вне площадки = мошенничество; внутри = конфликт бронирований; сохранить переписку и чеки
inline_2 — кому/где/за что: ФИО = договор; ссылка из чата ≠ площадка; 20 000 ₽ по ссылке; цена −15% торопят
inline_3 — 6 часов Авито: бесплатная отмена; 22:15 оплата → 04:15 окно; 08:40 у подъезда; день в день — без возврата
inline_4 — рассинхрон календарей: две площадки; хозяин настоящий; «занято» ≠ автоматом обман; поддержка площадки
inline_5 — чат до оплаты: адрес, даты, цена, заезд; код ≠ доказательство; залог заранее; не только голосовое
inline_6 — чеклист: ФИО получателя; платёж внутри брони; бронь в ЛК; тариф отмены; 22:15→04:15; полиция vs поддержка
inline_7 — Добрый дом: условия до оплаты; Telegram/MAX; +7 (993) 574-83-22; своя дверь утром

## Key scene numbers (use in labels)

- 28 августа, 22:15 — вечерняя оплата
- 08:40 — у подъезда, чужие жильцы
- 6 часов — окно отмены Авито
- 04:15 — конец бесплатной отмены
- 20 000 ₽ — списание по ссылке (ProOren)
- 15% ниже рынка — красный флаг

## H1 (do not copy as hook)

Перевёл предоплату за квартиру посуточно. Утром её уже сдали

## Good hook examples (style)

- «Код есть — вода холодная»
- «Ссылка «для брони» — утром пусто»
- «Деньги ушли — в квартире чужие»
- «Вечером перевёл — утром сдали»

## BAN

English headlines, SEO dumps, realtor/ЕГРН stickers, invented numbers not in article, cover_phone_cta pill field.
