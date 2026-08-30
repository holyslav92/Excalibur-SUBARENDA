# Cover-text inputs — B04

tenant: ПКОМПАНИЯ «Добрый дом», Тюмень, посуточная аренда
season: конец августа 2026, ЛЕТО (НЕ зима, НЕ снег на обложке)
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
  "h1": "Заселился в 22:00. В 10:00 созвон — закрывающие обещают после выезда",
  "angle": "Поздний заезд в 22:00, видеосозвон в 10:00, закрывающие только после выезда — риск для авансового отчёта",
  "pain_scene": {
    "setup": "командированный снимает квартиру посуточно на 2 ночи, заселяется около 22:00",
    "turn": "утром в 10:00 обязательный видеосозвон, а закрывающие документы обещают только после выезда",
    "conflict": "к сроку авансового отчёта (3 рабочих дня) чек и акт могут не успеть; Wi‑Fi и стол не проверены до оплаты",
    "strong_verb": "обещают после выезда"
  },
  "wordstat": {
    "p0": "квартиры посуточно тюмень",
    "p0_frequency": 5523,
    "secondary": "снять квартиру посуточно в тюмени",
    "secondary_frequency": 1755
  }
}
```

## Wordstat Tyumen (live, guest queries)

- квартиры посуточно тюмень — 5523
- снять квартиру посуточно в тюмени — 1755
- квартиры посуточно в тюмени недорого — 441
- квартиры посуточно тюмень от хозяев — 142
- квартиры посуточно тюмень рядом — 77

## article facts for inline panels (match FIGURE slots from drafts/writer.html)

inline_1 — Заезд в 22:00: 22:10 у подъезда; 40 минут на проверку; заезд с 15:00; выезд до 12:00; деньги уже ушли
inline_2 — Wi‑Fi: «есть Wi‑Fi» без цифр; дальняя комната — обрыв на 3-й минуте; 1,2 Мбит/с для 720p; вопрос: скорость у стола
inline_3 — Стол: барная стойка; табурет без спинки; фото стола обязательно; розетка рядом; закрыть дверь
inline_4 — Документы: «после выезда»; 3 рабочих дня на отчёт; чек на 10-й день; 4 200 ₽ за 2 ночи; самозанятый — чек «Мой налог»
inline_5 — Вердикт: сначала стол, скорость, закрывающие; потом деньги и ключ; ночной заезд — норма, если проверили до оплаты
inline_6 — 6 сообщений до оплаты: фото стола; скриншот Wi‑Fi; заезд 22:00 письменно; статус арендодателя; комплект документов; срок в договоре
inline_7 — Добрый дом: стол и закрывающие до брони; тел +7 (993) 574-83-22; MAX и Telegram

## H1 (do not copy as hook)

Заселился в 22:00. В 10:00 созвон — закрывающие обещают после выезда

## Good hook examples (style)

- «Код есть — вода холодная»
- «Залог не вернули — скол на плите»
- «Чек обещали — пришёл на десятый день»
- «Созвон в 10:00 — Wi‑Fi в комнате нет»

## BAN

English headlines, SEO dumps, realtor/ЕГРН stickers, invented numbers not in article, winter/snow scene.
