# Cover-text inputs B24

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: На фото — стиралка. На третий день — прачечная за 600 ₽

cover_hook MUST match H1 **two-beat** structure (washer on listing photo → day three laundromat 600 ₽). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «На фото стиралка — прачечная 600 ₽» (5 words)
  - «На фото — стиралка. Третий день — 600 ₽» (6 words)
  - «Фото со стиралкой — раковина вместо» (5 words)
  - «На фото стиралка — раковина и прачечная» (6 words)
  - «Обещали стиралку — третий день прачечная» (5 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: early autumn September 2026 Tyumen — light jacket weather — NOT winter, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: bathroom listing photo vs reality — sink, hanger, folding dryer + laundromat bag on day three; large Cyrillic two-beat hook; September mood, NOT winter
inline_count 3 (poster + 3 inline panels: inline_1 … inline_3)

Key facts from article.html:
- Guest booked 3 nights in Tyumen for 8 400 ₽ after seeing washer under countertop in bathroom photo
- In apartment: sink, hanger, folding dryer near cold radiator — no washer in bathroom, kitchen, or hall
- Host reply: shared machine in basement, second entrance, key from neighbor in apt 14; then «being repaired»
- Guest hand-washed shirt in sink; September, windows closed, radiators cold — didn't dry
- Day three: laundromat self-service — wash 350 ₽, dry 150 ₽, powder 50 ₽ ≈ 600 ₽ total
- Dispute: guest asked partial refund; host refused — «machine exists but shared, not promised in unit»
- Core wound: photo promises in-unit washer; access is separate quest
- One question saves 600 ₽: «Стиральная машина в этой квартире или общая? Где именно и как попасть?»
- Ask for short video of bathroom with machine; save listing screenshot before payment
- Moral: «Сначала проверка. Потом перевод.»
- Related siblings: B07 kitchen photo vs café, B11 bathroom «everything for guests», B20 hot water

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4724), снять квартиру посуточно в тюмени (~1452)

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1 … inline_3).
Poster cover: early-September Tyumen bathroom — listing photo vs sink reality + laundromat bag + big two-beat hook in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «600 ₽»)
  GOOD: «600 рублей», «три ночи», «фото стиралки»
  BAD: «600 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
