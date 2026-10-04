# Cover-text inputs B44

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: В чате посуточно: залог 3 000 ₽ — на оплате заморозка 11 400, кода нет

cover_hook: two-beat — chat promised deposit 3 000 → bank hold 11 400, no door code yet. 2–8 words MAX Cyrillic poster hook.
  GOOD patterns:
  - «В чате 3000 — на оплате 11400» (5 words)
  - «Залог 3000 в чате — заморозка 11400» (5 words)
  - «Обещали залог 3000 — заморозили 11400» (4 words)
  highlight: exact one-word substring of hook (Cyrillic)

Season: **October 2026 Tyumen** — autumn, yellow leaves, light jacket, mild evening — NO winter hero, NO snow, NO fur coats, NO New Year
Phone on cover scene: +7 (993) 574-83-22 on tape/magnet/sticker — never wrong number
Cover scene: phone with chat + payment screen hold amount; large Cyrillic hook; October apartment mood
inline_count **3** (inline_1 … inline_3 — tenant inline_image_count 3)

Key facts from article.html:
- Host in chat: «залог три тысячи, не переживайте»
- Guest taps Pay; bank shows hold/freeze 11 400 ₽
- No door code yet; available balance drops
- 11 400 may bundle nights, cleaning, service fee, deposit — not necessarily «deposit ×4»
- Hold (preauth) ≠ final charge; may unblock or capture later
- Anxiety worse when code missing and host silent
- Three questions before pay: what lines make total, deposit blocked or charged, when/how deposit returns
- Dobry dom: explain total before confirm; code by clear order
- Moral: сначала проверка, потом перевод
- Related sibling: B32 card 3400 vs pay 8816 for two nights

Wordstat guest queries (Tyumen): квартира посуточно залог, квартиры посуточно тюмень, снять квартиру посуточно в тюмени

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
