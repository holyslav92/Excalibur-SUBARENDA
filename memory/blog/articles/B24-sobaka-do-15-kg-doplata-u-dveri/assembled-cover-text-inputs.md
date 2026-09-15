# Cover-text inputs B24

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: В чате: «собака до 15 кг». У двери: «крупная» — 2 500 ₽

cover_hook MUST match H1 **two-beat** structure (chat agreed dog up to 15 kg → at door «large» + 2 500 ₽ fee). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «До пятнадцати в чате» — «крупная» у двери» (5 words)
  - «Пятнадцать кило в чате» — две пятьсот у двери» (5 words)
  - «Согласовали до пятнадцати» — доплата у двери» (4 words)
  - «Четырнадцать кило в чате» — крупная у двери» (5 words)
  - «В чате до пятнадцати» — две пятьсот у двери» (5 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: early autumn September 2026 Tyumen — light jacket, yellow leaves, mild — NO winter hero, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: apartment entrance with guest, suitcase, dog on leash; large Cyrillic two-beat hook painted on physical object in scene; early September mood, NOT winter
inline_count 3 (poster + 3 inline panels)

Key facts from article.html:
- Guest asked «можно с собакой», host agreed «собака до 15 кг» in chat
- At door: «Крупная. Доплата 2 500 ₽ — или не заселяем»
- Dog mixed breed, 14 kg; taxi already left; 8 400 ₽ paid for two nights
- Trap: «можно с собакой» ≠ full agreement — need weight limit, breed rules, fee amount, deposit
- Four questions before payment: max weight number, breed/size limits, fee per night vs whole stay, deposit sum and return
- «Крупная собака» is not measurable until a number is named
- Rule at door is leverage, not a rule — pay 2 500 or don't check in
- Moral: «Сначала правила в переписке. Потом ключ.»
- Related siblings: B04 dopлата za tretego, B21 rannij zaezd, B23 uborka na vyezde, B22 pasport v chat

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4805), снять квартиру посуточно в тюмени (~1490)

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).
Poster cover: early September Tyumen entrance — dog on leash + suitcase + big two-beat hook in Cyrillic on scene object.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «2 500 ₽»)
  GOOD: «две пятьсот у двери», «четырнадцать кило», «до пятнадцати в чате»
  BAD: «2 500 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
