# Cover-text inputs B23

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: В карточке: «уборка включена» — 3 ночи. Выезд: фото простыни — 1 800 ₽

cover_hook MUST match H1 **two-beat** structure (promise in card → checkout sheet photo + 1 800 ₽ demand). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «Уборка включена» — 1 800 за простыню» (6 words)
  - «Включена уборка» — доплата на выезде» (5 words)
  - «Три ночи платил» — фото простыни» (5 words)
  - «Обещали уборку» — 1 800 на выезде» (5 words)
  - «Уборка в цене» — счёт за бельё» (5 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: early autumn September 2026 Tyumen — light jacket weather — NOT winter, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: apartment doorway checkout + crumpled sheet photo on phone + large Cyrillic two-beat hook; September mood, NOT winter
inline_count 7 (poster + 7 inline panels)

Key facts from article.html:
- Card said «уборка после выезда включена» — guest booked 3 nights for 10 800 ₽
- Normal stay: slept on provided linens, no parties, no flooded mattress
- Host at checkout: «Уборка включена — это после вас. А простынь — отдельно, 1 800 ₽»
- Phone screen: crumpled sheet photo, stain at edge, flash glare
- Guest with suitcase and train ticket at door — keys not yet returned, taxi waiting
- Two readings of same line: guest = cleaning includes linens; host = cleaning is floors/bathroom/trash, laundry is separate
- No rule citation, no damage definition, no check-in linen photo for comparison — only photo + pay now
- Legitimate damage charges need prior rules (example range 500–1 000 ₽ per item — not justification for 1 800 ₽)
- Three categories: normal use (creases, body marks) vs extra cleaning (pets, kitchen mess) vs real damage (burn, blood, ink)
- Deposit 2 000–5 000 ₽ is not blank check; deposit ≠ extra payment — easy to confuse at door
- Ask host BEFORE booking: does «уборка включена» cover linen change, laundry, floors, bathroom?
- Photo bed, linens, towels, kitchen, bathroom at check-in — 5 minutes saves checkout dispute
- On checkout: ask written basis for any extra charge; compare claim to check-in photos
- Don't transfer urgent sum until rule + proof shown
- Related siblings: B17 kommunalka 1 840 ₽, B10 taxi 2 400 after «all included», B02 deposit not returned
- Moral: «Сначала проверка. Потом перевод.»

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4826), снять квартиру посуточно в тюмени

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 7 inline frames (inline_1 … inline_7).
Poster cover: early-September Tyumen apartment checkout — sheet photo on phone + big two-beat hook in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «1 800 ₽»)
  GOOD: «1 800 рублей», «три ночи», «фото простыни»
  BAD: «1 800 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
