# cover-text inputs B03 — скрытые доплаты при посуточной аренде от хозяина

Output ONLY valid JSON for cover/cover-text.json per skill. No markdown fences, no commentary.

## Season / cover context

Summer 2026 YEKT — late August Tyumen. Light high-key cover season. No winter hero (no snow, ice, frozen keybox). Guests with summer trips, relocations, family visits.

## H1 (do NOT copy verbatim into hook)

«Всё включено», сказал хозяин. Я уточнил итоговую сумму

## Subject / angle

Hidden fees in daily rental from owner — ask total sum before payment. Host says "all included" but cleaning, extra guests, Wi‑Fi, parking may be separate lines.

## Pain scene

- Setup: host names price and promises «всё включено»
- Turn: before payment — cleaning, guests, Wi‑Fi or parking as separate lines
- Conflict: nightly price lower than total trip cost
- Action: guest asks total sum before transfer

## Key facts from article.html (use in inline_labels)

### inline_1 — две ночи по 2500 ₽
- 2 ночи × 2500 ₽ = 5000 ₽
- уборка +1500 ₽ → итого 6500 ₽
- +30% к стоимости ночей
- сравнивать итог, не цену ночи

### inline_2 — пять вопросов до перевода
- итоговая сумма за весь срок
- уборка входит или отдельно
- доплата за гостя/ребёнка/питомца
- парковка, Wi‑Fi, ранний заезд
- зафиксировать в переписке

### inline_3 — уборка отдельной строкой
- уборка 500–2000 ₽ по рынку
- на 2 ночи +1500 ₽ = +30%
- «по запросу» в карточках
- одна ночь + уборка — дорого

### inline_4 — гости, питомец, бельё
- +500 ₽ за комплект белья
- доплата с третьего гостя
- ранний заезд / поздний выезд платные
- депозит — отдельная строка

### inline_5 — ранний заезд / поздний выезд
- заезд после 14:00, выезд до 12:00
- «заезд в 9:00 — за какую сумму?»
- «может быть» ≠ подтверждение
- запасной план

### inline_6 — четыре разные строки оплаты
- цена проживания — за ночи
- сервисный сбор платформы
- предоплата — часть проживания
- залог ≠ цена проживания

### inline_7 — зафиксировать итог + Добрый дом
- одно сообщение с итогом
- «да, всё верно» до перевода
- сверить с подтверждением брони
- итог одной суммой до оплаты

## Wordstat stickers (live MCP-KV Tyumen 55+11176, 2026-08-24)

Pick 1–3 readable designer stickers from these verified queries:
- «снять квартиру посуточно от хозяина» — 326
- «аренда квартир посуточно тюмень» — 208
- «снять квартиру посуточно в тюмени» — 1993 (support cluster from scout)

## Hook guidance

2–8 words, simple Russian, who + what happened + why me. NOT copy H1. Examples of good tone: «Две ночи — не вся сумма», «Спроси итог до перевода».

## Anti-dup vs sibling articles

- B01: codes / contactless check-in — do NOT use codes, keybox, door
- B02: deposit refund / chip on tile — do NOT use залог refund as main hook (deposit may appear as one inline fact only)

## Required JSON shape

```json
{
  "hook": "...",
  "highlight": "one word from hook",
  "sticky": "up to 5 words",
  "wordstat_stickers": ["...", "..."],
  "inline_labels": {
    "inline_1": ["...", "...", "..."],
    "inline_2": ["...", "...", "..."],
    "inline_3": ["...", "...", "..."],
    "inline_4": ["...", "...", "..."],
    "inline_5": ["...", "...", "..."],
    "inline_6": ["...", "...", "..."],
    "inline_7": ["...", "...", "..."]
  }
}
```

Each inline panel: 3–6 labels, each 1–4 words, factual (numbers, steps, comparisons from article).

## GATE HARD RULES (must pass excalibur_blog_cover_text_gate.py)

- Every label: 1–4 words ONLY (count spaces). Examples that FAIL: «2 ночи × 2500 ₽» (5 tokens), «Может быть — не факт» (5 words).
- Every label MUST contain at least one Cyrillic letter. Labels like «+1500 ₽» or «+30%» alone FAIL — add Russian word: «уборка +1500 ₽», «плюс 30 процентов».
- No Latin except whitelisted brands. Wi‑Fi is OK as brand-ish? Actually Wi‑Fi has Latin - check gate... LATIN_WORD_RE finds Latin words. "Wi" and "Fi" might fail. B02 used no Wi-Fi in labels. Use «вай‑фай» or «интернет» instead.
- highlight must be exact word inside hook (case-insensitive match).

Previous gate BLOCK errors to fix:
- inline_1: «2 ночи × 2500 ₽» → shorten to «две ночи 5000» or «2500 за ночь»
- inline_3: «+1500 ₽» → «уборка 1500 рублей»
- inline_5: «Может быть — не факт» → «не подтверждено» or «может быть»
