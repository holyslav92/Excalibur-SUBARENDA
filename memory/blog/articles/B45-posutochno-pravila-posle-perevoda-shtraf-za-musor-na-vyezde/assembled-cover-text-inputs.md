# Cover-text inputs B45

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Две ночи посуточно: PDF после перевода — на выезде 3 800 ₽ за пакеты

cover_hook: two-beat — paid two nights, rules PDF after transfer, checkout demand 3 800 ₽ for garbage bags. 2–8 words MAX Cyrillic poster hook aligned with H1 pain (NOT verbatim H1 copy).
  GOOD patterns:
  - «Оплатили — PDF с правилами потом» (5 words)
  - «На выезде 3800 за пакеты» (4 words)
  - «Правила после перевода — 3800 у двери» (5 words)
  highlight: exact one-word substring of hook (Cyrillic)

Season: **early October 2026 Tyumen** — autumn yellow leaves, light jacket, mild morning/evening — NO winter hero, NO snow, NO fur coats, NO New Year
Phone on cover scene: +7 (993) 574-83-22 on tape/magnet/sticker — never wrong number
Cover scene: phone with chat PDF + garbage bags at door; large Cyrillic hook; October apartment mood
inline_count **3** (inline_1 … inline_3 — tenant inline_image_count 3)

Key facts from article.html:
- Guest: «В объявлении про мусор ни слова»
- Two nights paid; suitcase at door; taxi almost there
- After transfer: file «Правила проживания» with garbage instruction + «компенсация расходов на вывоз мусора — 3 800 ₽»
- Listing had no line about garbage/checkout fees
- Host: «Правила отправил, вы же оплатили»
- Payment may be акцепт (ст. 438 ГК) only for conditions visible at pay time; PDF after pay is different story
- «Компенсация» needs breakdown: what cost, how much, proof
- Save: listing screenshot before pay, transfer receipt, PDF pages with fees, photos at check-in (kitchen, bin, balcony)
- Dobry dom: rules before pay, short message not 10-page PDF; «Сначала правила. Потом ключ.»
- Ask before pay: «Есть ли сборы на выезде, в том числе за мусор?»
- Related sibling: B23 cleaning included vs linen charge on checkout

Wordstat guest queries (Tyumen): правила проживания посуточно, квартиры посуточно тюмень, снять квартиру посуточно в тюмени

Output ONLY valid JSON for cover/cover-text.json.

JSON SHAPE:
```json
{
  "hook": "…",
  "highlight": "…",
  "sticky": "…",
  "wordstat_stickers": ["…", "…"],
  "inline_labels": {
    "inline_1": ["…", "…"],
    "inline_2": ["…", "…"],
    "inline_3": ["…", "…"]
  }
}
```

GATE HARD LIMITS:
- hook: 2–8 words — highlight exact substring of hook
- each inline label: 1–4 words, MAX 28 chars, Cyrillic required
- sticky: max 5 words
- wordstat_stickers: 1–3 phrases
- inline_labels: 2–6 labels per panel
NO Latin except brand whitelist. NO logo in generation.
