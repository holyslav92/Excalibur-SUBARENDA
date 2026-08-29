# Cover-text inputs — B04

tenant: ООО «Добрый дом», Тюмень, посуточная аренда
season: конец августа 2026, лето (НЕ зима, НЕ снег, НЕ минусовые температуры на обложке)
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
- wordstat_stickers: 1–3 guest queries from Wordstat Tyumen (below). NO ЕГРН/риэлтор/авито.
- inline_labels: 3–6 labels per inline_1…inline_7, each 1–4 words, facts from article.
- NO host face in hook. NO +7 922 001 65 05.
- Phone +7 (993) 574-83-22 is painted IN SCENE by Cover agent (tape/magnet/screen) — do NOT add pill field; mention in sticky or labels only if natural.
- Logo memory/cover/assets/brand/logo-dobry-dom.png — factory paste top-right only, not in generation.

## title-brief.json

```json
{
  "h1": "Звонок в 10:00. Заселился в 22:00 — у стола нет розетки",
  "angle": "Что проверить у хозяина до оплаты: розетку у стола, реальную связь для видеозвонка и срок выдачи закрывающих документов",
  "pain_scene": "Командировочный приезжает около 22:00 после рабочего дня, а в 10:00 ему нужно выйти на видеосвязь. В карточке указаны Wi‑Fi и рабочий стол, но стол может оказаться кухонной стойкой без розетки, а закрывающие документы — обещанием «потом».",
  "dzen_stickers": ["10:00", "22:00", "стол есть", "розетки нет", "чек потом"],
  "wordstat": {
    "p0": "квартиры посуточно тюмень",
    "p0_frequency": 3825,
    "secondary": "снять квартиру посуточно в тюмени",
    "secondary_frequency": 1161
  }
}
```

## Wordstat Tyumen (live, guest queries, region 55)

- квартиры посуточно тюмень — 3825
- снять квартиру посуточно в тюмени — 1161
- квартиры посуточно в тюмени недорого — 328
- квартиры посуточно тюмень от хозяев — 90
- квартира посуточно тюмень снять на сутки — 48
- квартиры посуточно тюмень рядом — 39

## article.html facts for inline panels (match FIGURE slots)

inline_1 — сцена заезда: 22:10 в квартире; созвон в 10:00; тюменский август; стол = кухонная стойка; розетка за холодильником; Wi-Fi в коридоре
inline_2 — что спросить письменно: розетка в вытянутой руке; стул vs табурет; свет и фон; размер поверхности; LAN-порт у роутера
inline_3 — честная проверка: фото стол+розетка+стул; видеозвонок 2 мин с будущего стула; не скриншот теста у окна; «картинка стоит — стол рабочий»
inline_4 — документы: ООО/ИП/самозанятый/физлицо; чек с QR; ИНН до перевода; «потом» = выпрашивать после выезда; договор+акт+счёт
inline_5 — заезд/выезд: 24/7 vs 12:00–21:00; Первомайская 14:00–22:00; Горького 500 ₽/час; поезд 23:40, выезд 15:00; инструкция до оплаты
inline_6 — вердикт-чеклист: время заезда цифрами; фото рабочего места; статус кто выдаёт документы; Wi-Fi в комнате; деньги — последний шаг
inline_7 — Добрый дом: инструкция до оплаты; стол с розеткой на фото; документы до перевода; +7 (993) 574-83-22; Telegram/MAX

## H1 (do not copy as hook)

Звонок в 10:00. Заселился в 22:00 — у стола нет розетки

## Good hook examples (style)

- «Код есть — вода холодная»
- «Залог не вернули — скол на плите»
- «Стол есть — розетки нет» (dzen sticker rhythm, not H1 copy)

## BAN

English headlines, SEO dumps, realtor/ЕГРН stickers, winter/snow scenes, invented numbers not in article, Avito in wordstat_stickers.
