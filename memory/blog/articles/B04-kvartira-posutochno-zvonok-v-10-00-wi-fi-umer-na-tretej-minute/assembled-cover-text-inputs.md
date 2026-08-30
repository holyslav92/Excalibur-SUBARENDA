# Cover-text inputs — B04

tenant: ПКОМПАНИЯ «Добрый дом», Тюмень, посуточная аренда
season: конец августа 2026, лето, НЕ зима
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

## title-brief.json

```json
{
  "h1": "Созвон в 10:00 сорвался на 3-й минуте — Wi‑Fi подвёл",
  "angle": "Скорость и стабильность интернета для командировочного видеосозвона",
  "pain_scene": "Гость заселяется в 22:00, утром в 10:00 выходит на важный видеосозвон, но Wi‑Fi обрывается уже на третьей минуте, хотя в объявлении обещан быстрый интернет.",
  "wordstat": {
    "p0": "квартиры посуточно тюмень",
    "frequency_rf": 12325,
    "frequency_regions": 5500
  }
}
```

## Wordstat Tyumen (live, guest queries)

- квартиры посуточно тюмень — 3808
- снять квартиру посуточно в тюмени — 1172
- посуточно тюмень — 5775
- квартиры посуточно в тюмени недорого — 319
- квартиры посуточно тюмень от хозяев — 89
- снять посуточно в тюмени — 1727

## article.html facts for inline panels (match FIGURE slots)

inline_1 — что сломалось: 22:10 заселение; Wi‑Fi ловит; мессенджер летает; 23:40 сериал буферизуется
inline_2 — разговор до оплаты: роутер у стола; speedtest; тестовый созвон 2 мин; отказ без Wi‑Fi
inline_3 — вопрос-отмычка: «где роутер?»; «сколько Мбит у стола?»; «интернет хороший» — уход
inline_4 — мораль: сначала связь; потом ключи; Wi‑Fi не видно на фото; проверка до оплаты
inline_5 — чеклист 4 пункта: SSID и пароль до заезда; speedtest upload; репитер/mesh; тестовый созвон
inline_6 — Добрый дом: инструкция заранее; менеджер на связи; честное «нет»; без залога в конверте
inline_7 — коротко: 10:03 картинка встала; 10:12 подъезд; 11:40 возврат 5600 ₽; 8400 ₽ три ночи

## Key numbers from article

- Заезд 22:10, созвон 10:00, обрыв 10:03, подъезд 10:12, переписка 11:40
- 8 400 ₽ три ночи вперёд; ~5 600 ₽ за две оставшиеся ночи
- Роутер в прихожине за двумя стенами; полторы палки Wi‑Fi у стола
- Нужен ровный upload 3–5 Мбит, не 100 Мбит скачивания

## H1 (do not copy as hook)

Созвон в 10:00 сорвался на 3-й минуте — Wi‑Fi подвёл

## Good hook examples (style)

- «Код есть — вода холодная»
- «Залог не вернули — скол на плите»
- «Быстрый интернет» — на третьей минуте
- Созвон встал — роутер в прихожей

## BAN

English headlines, SEO dumps, realtor/ЕГРН stickers, invented numbers not in article, winter/snow scenes.
