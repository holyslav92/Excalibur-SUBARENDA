# Cover-text inputs B24

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Выезд в полдень. За четверть часа — 900 ₽ за «лишний час»

cover_hook MUST match H1 **two-beat** structure (checkout at noon → 900 ₽ for «extra hour» before noon). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «Выезд в полдень» — 900 за четверть часа» (5 words)
  - «Уборщица в 11:45» — 900 за «лишний час»» (5 words)
  - «До полудня ещё ваше» — просят 900» (5 words)
  - «Четверть часа до выезда» — счёт 900» (5 words)
  - «Выезд в двенадцать» — уборщица уже ждёт» (5 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: early autumn September 2026 Tyumen — light jacket, yellow leaves, mild — NO winter hero, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: apartment interior at checkout — open suitcase, child at breakfast, cleaner knock at door + large Cyrillic two-beat hook; early September mood, NOT winter
inline_count 3 (poster + 3 inline panels)

Key facts from article.html:
- Message at 11:45: «900 ₽ за каждый лишний час. Уборщица уже ждёт»
- Agreed checkout noon; guest still packing, child eating breakfast, keys on table
- Two nights paid 8 400 ₽ total
- Cleaner knocks, asks urgent transfer before noon — pressure at checkout
- «Extra hour» starts AFTER agreed checkout time, NOT when cleaner arrives
- 900 ₽/hour can be valid IF agreed in advance and after noon
- Trap: host shifts paid boundary because cleaning schedule is tight
- Rule: «Сначала проверка. Потом перевод.» — find agreed hour in chat first
- Related siblings: B06 chemodyany mezhdu, B21 rannij zaezd, B23 prostyni, B17 kommunka

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4724), снять квартиру посуточно в тюмени

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).
Poster cover: early September Tyumen checkout scene — suitcase + big two-beat hook in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «900 ₽»)
  GOOD: «девятьсот рублей», «четверть часа», «уборщица у двери»
  BAD: «900 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
