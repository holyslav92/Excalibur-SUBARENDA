# Cover-text inputs — B04

tenant: ПКОМПАНИЯ «Добрый дом», Тюмень, посуточная аренда
season: конец августа 2026, лето, родители с дочерью перед 1 сентября — NO winter hero, NO snow/ice
topic_id: B04

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
- Phone +7 (993) 574-83-22 is painted IN SCENE by Cover agent (tape/magnet/screen) — do NOT add pill field.
- Logo memory/cover/assets/brand/logo-dobry-dom.png pasted AFTER gen, not drawn.

## title-brief.json

```json
{
  "h1": "Попросили фото паспорта до оплаты — под угрозой бронь и данные",
  "angle": "Гость получает просьбу прислать паспорт раньше понятных условий и оплаты и рискует одновременно бронью и персональными данными.",
  "pain_scene": "Перед поездкой хост просит фото паспорта в чате до оплаты, адреса и ясной договорённости. Гость боится отказаться и потерять квартиру, но не хочет отправлять документы незнакомцу.",
  "wordstat": {
    "p0": "паспорт при заселении в квартиру посуточно",
    "p0_frequency": 99,
    "secondary": "фото паспорта при заселении в квартиру посуточно",
    "secondary_frequency": 52
  }
}
```

## Wordstat Tyumen (live, guest queries)

- паспорт при заселении в квартиру посуточно — 3 (topic P0)
- фото паспорта при заселении в квартиру посуточно — 2 (topic secondary)
- квартиры посуточно тюмень — 5500
- снять квартиру посуточно в тюмени — 1761
- квартиры посуточно в тюмени недорого — 430

Prefer topic P0/secondary for wordstat_stickers; add general guest query if needed.

## article.html facts for inline panels (match FIGURE slots)

inline_1 — Марина 28 августа 22:15; четыре ночи; фото паспорта все страницы + селфи; перевод за первую ночь; адреса нет; «ещё двое смотрят»
inline_2 — паспорт сам не доказывает мошенничество; хосту может понадобиться для договора; «по новым правилам» — давление
inline_3 — «пришлите паспорт — держу квартиру» — нет; сначала адрес, даты, цена; документ после договорённости; паспорт + срочный перевод = нет паузы
inline_4 — менеджер в другом чате; все страницы; селфи без причины; «бронь снимаю через полчаса»; цена −20%; ссылка «на банк»
inline_5 — «я тоже пришлю паспорт» — не гарантия; потери 5–30 тыс.; цена −20–30% как сигнал; проверяют адрес и созвон
inline_6 — Марина: «адрес и созвонимся»; «вы не доверяете?»; через 10 мин аккаунт молчит; та же квартира в двух объявлениях
inline_7 — порядок: адрес → проверка → бронь → данные → деньги и ключ; Добрый дом: адрес сначала, паспорт при заселении; +7 (993) 574-83-22

## H1 (do not copy as hook)

Попросили фото паспорта до оплаты — под угрозой бронь и данные

## Good hook examples (style)

- «Паспорт в чат — адреса нет»
- «Селфи с паспортом — перевод сейчас»
- «Ещё двое смотрят — решайте»

## BAN

English headlines, SEO dumps, realtor/ЕГРН stickers, winter/snow hero, invented numbers not in article.
