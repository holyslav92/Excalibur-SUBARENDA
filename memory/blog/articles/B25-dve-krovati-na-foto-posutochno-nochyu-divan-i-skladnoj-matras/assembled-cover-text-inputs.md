# Cover-text inputs B25

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: На фото две кровати. Ночью троих — диван и складной матрас

cover_hook MUST match H1 **two-beat** structure (two beds on photo → night reality sofa + folding mattress). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «На фото две кровати — ночью диван» (5 words)
  - «Две кровати на фото — матрас на полу» (6 words)
  - «В карточке две кровати — диван и пол» (6 words)
  - «На фото кровати — ночью диван» (5 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: early autumn September 2026 Tyumen — light jacket weather — NOT winter, NO snow
Phone in scene on cover: +7 (993) 574-83-22 on tablo/magnet/screen — never post-paste pill
Cover scene: three adult guests late evening in apartment — one sees sofa + folding mattress vs listing photo with two beds; large Cyrillic two-beat hook; September mood
inline_count 7 (2 canvases longform)

Key facts from article.html:
- Card header «2 кровати», main photo shows two made beds in different rooms
- Three adults, 2 nights, ~10 400 ₽ prepaid
- Host chat: «Две кровати, троим нормально, всем будет удобно»
- Reality: one double bed in bedroom, sagging sofa-bed in living room, folding mattress on floor for third adult, thin sheet without second bedding set
- Host: «Диван же тоже спальное место. В карточке написано»
- Guest: «На фото две кровати. Мы за две ночи заплатили, а не за диван и пол»
- Block «Спальные места» separates main vs additional surfaces
- Ask before payment: type of each place (bed, sofa-bed, folding mattress), photos unfolded, bedding for all
- Moral: «Сначала проверка. Потом перевод.»

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4724), снять квартиру посуточно в тюмени (~1452)

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 7 inline frames (inline_1 … inline_7).
Poster cover: early-September Tyumen apartment — three tired adults + large two-beat hook in Cyrillic; person in scene.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
Max 1 cat meme across article — prefer people-meme on one inline only.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
