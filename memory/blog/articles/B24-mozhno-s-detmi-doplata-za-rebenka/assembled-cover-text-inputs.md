# Cover-text inputs B24

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: «Можно с детьми» в карточке. При заезде: 1 500 ₽ за 2 ночи, 6-летнему

cover_hook MUST match H1 **two-beat** structure (badge in card → door surcharge for child). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «Можно с детьми» — 1 500 у двери» (5 words)
  - «В карточке с детьми» — доплата за шестилетнего» (5 words)
  - «Значок с детьми» — полторы тысячи при заезде» (6 words)
  - «Семья с ребёнком» — доплата у подъезда» (5 words)
  - «Можно с детьми» — ребёнок не в цене» (5 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: early autumn September 2026 Tyumen — light jacket weather — NOT winter, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: apartment doorway check-in + family with suitcase + child + large Cyrillic two-beat hook; September mood, NOT winter
inline_count 3 (poster + inline 1-3)

Key facts from article.html:
- Card badge «можно с детьми» — family booked 2 nights for 8 400 ₽ (2 adults + child)
- Guest read badge as: child included in price; host read as: allowed to enter, child billed separately
- At door host: «За шестилетнего — полторы тысячи за две ночи. Это в правилах»
- Extra crib 500 ₽ if needed — also named at door, not before payment
- Child tired after road, suitcases at door — refusing is harder than paying 1 500 ₽
- Badge answers only «will they accept a child» — NOT whether child counts in guest count or needs extra fee
- One direct question before payment: «ребёнку шесть — он входит в базовое число гостей или считается сверх?»
- Ask total for all nights in one number: 2 adults + 6-year-old, crib yes/no
- Save card screenshot with badge + chat with price before transfer
- Related siblings: B04 third guest at door, B10 taxi 2 400 after «all included», B06 checkout vs train
- Moral: «Сначала проверка. Потом перевод.» — price for child cannot appear on threshold

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4826), снять квартиру посуточно в тюмени

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1 … inline_3).
Poster cover: early-September Tyumen apartment doorway — family with child + suitcase + big two-beat hook in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «1 500 ₽»)
  GOOD: «1 500 рублей», «шесть лет», «можно с детьми»
  BAD: «1 500 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
