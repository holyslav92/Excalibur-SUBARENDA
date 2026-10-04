# Cover-text inputs B45

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: «Правила потом»: 2 ночи посуточно — на выезде штраф за мусор

cover_hook: two-beat — guest paid 2 nights (~7 200 ₽), skipped rules link, on checkout host claims 900 ₽ fine for trash/dishes and threatens deposit hold. 2–8 words MAX Cyrillic poster hook.
  GOOD patterns:
  - «Две ночи оплачены — на выезде штраф 900» (6 words)
  - «Правила не читали — штраф на выезде» (5 words)
  - «Оплатили две ночи — штраф за мусор» (5 words)
  highlight: exact one-word substring of hook (Cyrillic)

Season: **early October 2026 Tyumen** — autumn, yellow leaves, light jacket, mild evening — NO winter hero, NO snow, NO fur coats, NO New Year, NO blizzard
Phone on cover scene: +7 (993) 574-83-22 on tape/magnet/sticker — never wrong number
Cover scene: kitchen checkout mood — delivery boxes, cups in sink, trash bag by door; large Cyrillic hook; October apartment mood (NOT winter)
inline_count **3** (inline_1 … inline_3 — tenant inline_image_count 3)

Key facts from article.html:
- Message on checkout: «по правилам — штраф 900 ₽ за мусор и посуду, иначе удержим залог»
- Guest paid ~7 200 ₽ for two nights in Tyumen; expected no extra charges
- Rules link was in booking card; guest planned to open «потом»
- Deposit not yet withheld — threat «иначе удержим», not completed charge
- Trash in story: delivery boxes, several cups in sink, bag by door
- Main ad did not mention trash fines; rules came as separate file after payment
- 900 ₽ ≈ eighth of ~7 200 ₽ total — painful surprise at door
- Guest should ask: what was published before pay; save screenshots and checkout photos
- Moral: сначала правила и фото, потом спор о штрафе
- Dobry dom: read rules before «забронировать»; clarify what «уборка включена» means
- Related: B23 уборка включена — штраф на выезде; B34 залог в фильтре vs у двери

Wordstat guest queries (Tyumen): квартиры посуточно тюмень, квартира посуточно правила, снять квартиру посуточно в тюмени

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
