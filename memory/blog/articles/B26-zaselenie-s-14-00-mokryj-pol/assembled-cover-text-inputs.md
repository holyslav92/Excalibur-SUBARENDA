# Cover-text inputs B26

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Заезд с двух. 105 мин с чемоданом: пахнет химией, мокрый пол, «ещё пять»

cover_hook MUST match H1 theme (wet floor, 105 min wait with suitcase, chemical smell, «ещё пять»). May shorten for poster Cyrillic (2–8 words MAX):
  PREFER hook that names wet floor OR 105 min OR chemical smell (not only «ещё пять»).
  GOOD patterns:
  - «Заезд с двух — мокрый пол» (5 words) — PREFERRED
  - «105 минут с чемоданом у двери» (5 words)
  - «Пахнет химией — пол мокрый» (4 words)
  - «Пришли вовремя — пол мокрый» (4 words)
  - «Заезд с двух — ещё пять» (5 words)
  - «Мокрый пол — сто пять минут» (5 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: early autumn September 2026 Tyumen — light jacket, yellow leaves — NOT winter, NO snow
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: apartment entrance — guest with suitcase, wet floor shine, bucket and mop; chemical smell mood; large Cyrillic hook; September mood
inline_count 7 (poster + 7 inline panels = 8 images total)

Key facts from article.html:
- Guest arrived on time at 14:00 check-in, 2 nights, 3 200 ₽ prepaid first night
- Wet floor in hallway, bucket and mop, host says «Ещё пять минут, уборка» — third «ещё пять» that day
- Smells of household chemicals, bedding stacked on chair not on bed
- 105 minutes with suitcase: partly on stair landing, partly in cafe across street (420 ₽ coffee and bun)
- «Заезд с двух» for guest means enter and live — not door open into unfinished cleaning
- Same-day guest turnover: short window between checkout and next check-in
- Host substitutes access for readiness — key yes, door open, but floor wet, smell, no place for bag
- Money layer: 420 ₽ cafe, 105 min lost from short 2-night trip
- Rushed cleaning while guest present → bad review risk later
- Ask BEFORE payment: will others checkout same day? When cleaning done? Bedding made? Dry floor?
- Trap: «ещё пять минут», «подъезжайте, разберёмся», «дверь откроем»
- Moral: «Сначала проверка. Потом перевод.» / «Нет. Так не заселяем.»
- Related siblings: B21 early check-in cleaning, B11 wet bath mat, B18 domofon, B23 checkout cleaning fee

Wordstat guest queries (Tyumen): квартиры посуточно тюмень, снять квартиру посуточно в тюмени

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 7 inline frames (inline_1 … inline_7).

REQUIRED JSON SHAPE (inline_labels values MUST be arrays of 2-6 short strings, NOT single strings):
```json
{
  "hook": "…",
  "highlight": "…",
  "sticky": "…",
  "wordstat_stickers": ["…", "…"],
  "inline_labels": {
    "inline_1": ["мокрый пол", "заезд с двух", "чемодан у двери"],
    "inline_2": ["пахнет химией", "ведро и швабра", "ещё пять минут"],
    "inline_3": ["сто пять минут", "лестничная площадка", "кафе через дорогу"],
    "inline_4": ["…", "…", "…"],
    "inline_5": ["…", "…", "…"],
    "inline_6": ["…", "…", "…"],
    "inline_7": ["…", "…", "…"]
  }
}
```
Poster cover: early-September Tyumen apartment entrance — suitcase + wet floor + large Cyrillic hook.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only)
  GOOD: «мокрый пол», «сто пять минут», «пахнет химией»
  BAD: «3 200 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
