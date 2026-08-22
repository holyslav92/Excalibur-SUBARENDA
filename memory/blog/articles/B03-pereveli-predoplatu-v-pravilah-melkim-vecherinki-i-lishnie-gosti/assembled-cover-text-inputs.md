# Cover-text inputs — B03 (Derouter Terra)

You are **Cover-text** for tenant **«Добрый дом»** (посуточная аренда квартир в Тюмени).

## Task

Write **ONLY** valid JSON for `cover/cover-text.json` — no markdown fences, no commentary.

Human must understand the cover hook in one second. Simple spoken Russian.

## Season / visual context (HARD)

Publication date: **2026-08-22** — **лето, август**. Cover scene will be bright/high-key summer. **No winter, snow, frost, −25°C, frozen keybox** on cover or inline labels.

## H1 (do not copy verbatim as hook)

Перевели предоплату. В правилах мелким: вечеринки и лишние гости

## Article facts (from article.html — use for inline_labels)

**Opening scene:** августовская пятница, двушка в центре Тюмени, предоплата за две ночи, правила пришли отдельным сообщением — гость пролистнул. Вечером приехали друзья, шесть человек вместо трёх. В час ночи звонок хозяину, в два приехал. Утром — досрочный выезд, залог не вернули.

**7 H2 themes:**
1. Сколько гостей можно — кто считается гостем (до 4 в объявлении vs двое в правилах; «на час» тоже гость)
2. Вечеринки — тишина с какого часа, сколько человек = шумная компания, жалоба соседей
3. Курение — балкон, вейп, кальян; сумма за нарушение
4. Заселение/выезд — после 14:00, до 12:00; ранний заезд / поздний выезд
5. Залог — сумма, основания удержания (курение, вечеринка, лишние гости, порча, ключи), срок возврата
6. Фото при заселении — видео одним дублем, пятна/сколы в день заезда
7. Правила до оплаты — текстом в чат, одна переписка

**Чеклист (7 пунктов):** гости на час, тишина, курение, время заезда/выезда, залог, фото, правила до оплаты.

**Добрый дом:** правила и залог до предоплаты одним сообщением.

## Wordstat (Тюмень 55+11176, live MCP-KV 2026-08-22)

Use 1–3 phrases for `wordstat_stickers`:
- аренда квартиры тюмень посуточно — 188
- правила посуточной аренды — 1
- снять посуточно — 15476 (similar)

title-brief stickers: правила посуточно, договор, Тюмень

## Required JSON shape

```json
{
  "hook": "2-8 words, who + what happened",
  "highlight": "one word FROM hook",
  "sticky": "up to 5 words",
  "wordstat_stickers": ["1-3 Tyumen phrases"],
  "inline_labels": {
    "inline_1": ["3-6 labels, 1-4 words each"],
    "inline_2": [],
    "inline_3": [],
    "inline_4": [],
    "inline_5": [],
    "inline_6": [],
    "inline_7": []
  }
}
```

**inline_1 … inline_7** — all 7 panels required. Each label 1–4 words, facts/numbers/steps from article. No mood slogans. Cyrillic only (no Latin except whitelisted brands — none needed here).

## Calibration (B02 sibling article)

```json
{
  "hook": "Залог не вернули — скол на плите",
  "highlight": "скол",
  "sticky": "Залог вернут?",
  "wordstat_stickers": ["залог посуточно", "Тюмень"]
}
```

## Good hook examples for THIS topic

- «Шесть гостей — залог не вернули»
- «Правила мелким — залог удержали»
- «Перевели предоплату — правила не читали»

## Bad hooks

- Copying H1 verbatim
- Winter / snow imagery
- Legal jargon without plain words
