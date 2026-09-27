# Cover-text inputs B38

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: В карточке был душ. В 23:10 бойлер погас — вода стала ледяной

cover_hook MUST match H1 **two-beat** structure (card promised shower/hot water → at 23:10 boiler off, icy water). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «В карточке душ — в 23:10 ледяная» (6 words)
  - «Обещали душ — в 23:10 ледяная» (5 words)
  - «Бойлер погас — вода ледяная» (4 words)
  - «Карточка с душем — ночью ледяная» (5 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook (Cyrillic word preferred)

Season: September 2026 Tyumen — early autumn, yellow leaves, light jacket, mild evening — NO winter hero, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: bathroom/shower + red blinking boiler indicator + large Cyrillic two-beat hook; September apartment mood, NOT winter
inline_count **7** (poster + inline_1 … inline_7 — tenant inline_image_count 7 longform)

Key facts from article.html:
- Saturday 26 September, couple from Yekaterinburg by car, tired child
- Card: «просторный душ, всегда горячая вода» — studio near Lesopark, 4 200 ₽/night, 8 400 ₽ prepay, 5 000 ₽ cash deposit at door
- Host left in four minutes after keys
- 23:10 shower: warm 1.5 min then ice cold; 30 L boiler red blink behind decorative panel
- 23:12 message to host; 23:26 reply one line: «мастер завтра»
- Child washed from kettle/casserole on induction; morning host offered 500 ₽ discount; deposit returned
- 30 L boiler = one short shower for family; reheat 40–90 min
- Second scenario: tripped breaker — fix in 2 min if you know «ВН» in panel
- Host chat patterns: «всё работает» vs guest asks central vs boiler
- Four questions before prepay: central or boiler volume, heat time, night response, money if no shower
- Dobry dom: instruction before trip, boiler on constant heat, cleaner checks tap before check-in
- Moral: cold shower at 23:10 = host who did not check water, not always broken boiler
- Extra panels inline_4–7: 8 400 ₽ prepay Thursday; 5 000 ₽ cash deposit in podjezd; host gone in 4 minutes; child washed from kettle; tripped breaker «ВН» two minutes; video cold tap + boiler + chat time; related B20 migayushij boiler link

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~9212), снять квартиру посуточно в тюмени (~3175)

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for **7** inline frames (inline_1 … inline_7).

JSON SHAPE (HARD — gate rejects wrong types):
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
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: **MAX 4 words AND MAX 28 characters** AND must contain at least one Cyrillic letter
  GOOD: «23:12 в чат», «ответ 23:26», «предоплата 8400», «залог пять тысяч»
  BAD: «написали в двадцать три двенадцать» (5 words, >28 chars)
  BAD: «ответ в двадцать три двадцать шесть» (6 words)
  BAD: «хозяин ушёл за четыре минуты» (5 words)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
- inline_labels: 2–6 labels per panel (skill says 3–6 preferred)
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.
