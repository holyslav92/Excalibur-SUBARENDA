# Cover-text inputs B45

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: «Заселение 24/7» посуточно. В чате: +1 800 ₽ за ночной заезд

cover_hook: two-beat — card promised round-the-clock check-in → at door after midnight chat demands +1 800 ₽ for night arrival. 2–8 words MAX Cyrillic poster hook (avoid Latin «24/7» in hook — use «круглосуточно» or «ночью»).
  GOOD patterns:
  - «В карточке круглосуточно — в чате +1800» (5 words)
  - «Обещали заселение ночью — доплата 1800» (5 words)
  - «Круглосуточно в объявлении — у двери доплата» (5 words)
  highlight: exact one-word substring of hook (Cyrillic)

Season: **October 2026 Tyumen** — autumn, yellow leaves, light jacket, mild evening — NO winter hero, NO snow, NO fur coats, NO New Year
Phone on cover scene: +7 (993) 574-83-22 on tape/magnet/sticker — never wrong number
Cover scene: phone chat at midnight, suitcase at door; large Cyrillic hook; October apartment mood
inline_count **3** (inline_1 … inline_3 — tenant inline_image_count 3)

Key facts from article.html:
- Card: «Заселение 24/7», «Бесконтактный заезд», «Встретим в любое время»
- Two nights prepaid ~5 600 ₽ via platform
- Flight delayed; guest arrives deep at night with suitcase, low phone battery
- Host earlier: «Да, конечно, ждём»
- At door: «Ночной заезд +1 800 ₽, переводом на карту. Без доплаты заселю утром»
- Surcharge not in listing/rules before booking
- Market night check-in sometimes 1 500–2 000 ₽ if disclosed upfront — problem is surprise at door
- Do not pay to personal card without checking conditions; screenshot chat, contact platform support
- Moral: сначала проверка, потом перевод
- Related: B13 empty keybox, B21 early check-in cleaning wait

Wordstat guest queries (Tyumen): квартиры посуточно тюмень, заселение в квартиру посуточно, бесконтактное заселение посуточно

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
