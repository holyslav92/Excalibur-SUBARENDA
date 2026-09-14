# Cover-text inputs B21

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Ранний заезд оплатили. У двери с чемоданом — почти 5 часов ожидания

cover_hook MUST match H1 **two-beat** structure (paid early check-in → hours waiting at door with suitcase). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «Ранний заезд оплатили» — пять часов у двери» (5 words)
  - «Оплатили заезд» — чемодан у двери» (4 words)
  - «Заселим с утра» — уборка до обеда» (5 words)
  - «Полторы тысячи» — пять часов ожидания» (4 words)
  - «Оплатили ранний» — ключ не готов» (4 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: early autumn September 2026 Tyumen — light jacket, yellow leaves, mild — NO winter hero, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: apartment entrance / courtyard with suitcase + large Cyrillic two-beat hook; early September mood, NOT winter
inline_count 3 (poster + 3 inline panels)

Key facts from article.html:
- Guest paid 1 500 ₽ for early check-in after night train, arrived at door with suitcase ~10 min after agreed morning hour
- Host reply: «До обеда не готово, уборка» — almost 5 hours waiting between courtyard, entrance, cafe, back
- Extra 890 ₽ on coffee, second coffee, taxi with suitcase there and back
- Guest thought «paid early check-in» = «apartment ready»; host took money without confirming cleaning/bedding/key
- Gap between checkout (~12:00) and check-in (~14:00) is normal cleaning window — 2–3 hours studio, 4–5 larger
- Early check-in is NOT a button — must confirm previous guests left, cleaning done, bedding changed, key free
- Trap point: chat BEFORE transfer — ask when apartment free, what «early check-in» includes
- Rule: don't take early check-in fee until apartment confirmed ready at named hour
- Moral: «Сначала проверка. Потом перевод.»
- Related siblings: B08 predoplata tishina, B04 dopлата za tretego, B18 domofon molchit, B06 vyezd chemodyany

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4826), снять квартиру посуточно в тюмени

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).
Poster cover: early September Tyumen entrance — suitcase at door + big two-beat hook in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «1 500 ₽»)
  GOOD: «полторы тысячи», «пять часов», «уборка до обеда»
  BAD: «1 500 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
