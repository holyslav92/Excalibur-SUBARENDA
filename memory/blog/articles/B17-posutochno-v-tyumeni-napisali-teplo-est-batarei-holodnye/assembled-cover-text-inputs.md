# Cover-text inputs B17

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Написали «тепло есть». За окном +6 °C — батареи холодные на 2 ночи
cover_hook MUST match H1 pain (same story beat — host wrote «тепло есть» in listing and chat, outside +6 °C, cold radiators for two paid nights). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns: ««Тепло есть» — батареи холодные» (4 words)
  OR: «Написали «тепло есть» — мёрзнут» (4 words)
  OR: ««Тепло есть» — в комнате шестнадцать» (5 words)
  DO NOT exceed 8 words in hook
Season: mid-September 2026 Tyumen, early autumn — yellow leaves, light jacket, +6 °C outside, NOT winter hero, NO snow, NO fur coats, NO New Year, NO December frost scenes
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/screen — never post-paste pill
4 images total (1 cover + 3 inline), inline_count 3

Key facts from article.html:
- Listing and chat said «Тепло есть» when guest asked about heating
- Guest paid 6 800 ₽ for two nights, arrived evening
- Outside about +6 °C; room 16–17 °C; radiator under window cold — palm can stay on section
- Bathroom riser same cold; condensate on window by night; blanket not solution — sleeping in jacket
- Host replies: «Сезон ещё не начался», «УК скоро включит», «Возьмите плед, одна ночь»
- «Отопление есть» ≠ «батарея греет сегодня» — city waits for +8 °C average 5 days
- After city start, heat reaches flats unevenly — guest has only two nights
- Guest should photo/video cold radiator + thermometer; ask what host does tonight
- Options: host brings heater, relocates, refund night/part — not «season not started»
- Don't buy heater yourself without host confirmation in chat
- If host silent: saved chat, photos, platform support — UК is host's job not guest's
- Key question before payment: «Батареи уже греют в этой квартире сегодня вечером или отопление только после старта сезона?»
- Good answer: «Греют, сезон дали в среду» or «Ещё нет, но два конвектора включу до приезда»
- Evasive «там всё есть, не переживайте» = negative answer
- Related: «кухня есть» three nights in cafe, «всё включено» taxi surcharge, «тихий центр» crane, «всё для гостей» wet mat
- Moral: «Сначала проверка. Потом перевод.» — check radiator same day before money

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~5220), снять квартиру посуточно в тюмени (~1689), квартира посуточно тюмень (~search cluster)

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).
Poster cover: early-September Tyumen apartment cold-radiator autumn mood + big hook matching H1 in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «6 800 ₽»)
  GOOD: «6 800 рублей», «две ночи оплачены», «батарея холодная»
  BAD: «6 800 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
