# Cover-text inputs — B03

tenant: ПКОМПАНИЯ «Добрый дом», Тюмень, посуточная аренда
season: конец августа, лето, родители + будущий студент перед 1 сентября
topic_id: B03

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
- Phone +7 (993) 574-83-22 is painted IN SCENE by Cover agent (tape/magnet/screen) — do NOT add pill field; mention in sticky or labels only if natural.

## title-brief.json

```json
{
  "h1": "Привезли сына к вузу — «рядом» оказалось 40 минут пешком",
  "angle": "Проверка пешего маршрута до конкретного корпуса вуза до оплаты брони",
  "pain_scene": "Родители бронируют жильё на 2–4 ночи по обещанию «рядом с вузом», а после приезда выясняют, что до нужного корпуса нужно идти 40 минут.",
  "wordstat": {
    "p0": "квартиры посуточно тюмень",
    "p0_frequency": 5534,
    "secondary": "снять квартиру посуточно в тюмени",
    "secondary_frequency": 1749
  }
}
```

## Wordstat Tyumen (live, guest queries)

- квартиры посуточно тюмень — 3822
- снять квартиру посуточно в тюмени — 1138
- квартиры посуточно тюмень рядом — 39
- квартиры посуточно тюмень от хозяев — 87
- квартиры посуточно в тюмени недорого — 338

## article.html facts for inline panels (match FIGURE slots)

inline_1 — «Рядом с вузом» не адрес: ТюмГУ много корпусов; «три остановки» ≠ пешком; 27 августа 19:20
inline_2 — утро и уверенность: 40 мин пешком; заезд с 14:00; поезд утром — чемоданы с вами
inline_3 — вопрос-отмычка: «Сколько минут пешком до корпуса?»; карта режим пешком; не «далеко ли»
inline_4 — конец августа спешка: «решать сегодня»; предоплата до просмотра; от 1,5 тыс. не ваша цена
inline_5 — вердикт: сначала карта и корпус; потом деньги и ключ; не фото → предоплата
inline_6 — чеклист: адрес корпуса; точный адрес квартиры; маршрут пешком; письменно заезд/выезд
inline_7 — Добрый дом: спросить корпус; назвать минуты честно; тел +7 (993) 574-83-22

## H1 (do not copy as hook)

Привезли сына к вузу — «рядом» оказалось 40 минут пешком

## Good hook examples (style)

- «Код есть — вода холодная»
- «Залог не вернули — скол на плите»
- «Рядом с вузом» — три остановки (too long?)

## BAN

English headlines, SEO dumps, realtor/ЕГРН stickers, invented numbers not in article.
