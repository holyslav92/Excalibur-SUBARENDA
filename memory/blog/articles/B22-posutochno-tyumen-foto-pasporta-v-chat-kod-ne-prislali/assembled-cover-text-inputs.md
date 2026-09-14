# Cover-text inputs B22

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: «Оплатили 3 ночи. Фото паспорта в чат — код не пришёл, багаж у двери»

cover_hook MUST match H1 pain (paid 3 nights, passport photo sent in chat, no access code, luggage at door). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns:
  - «Паспорт в чат — кода нет» (4 words)
  - «Оплатили ночи — код не пришёл» (4 words)
  - «Фото паспорта — код не пришёл» (4 words)
  - «Отправили паспорт — кода нет» (4 words)
  - «Три ночи оплатили — кода нет» (4 words)
  - «Паспорт отправили — багаж у двери» (4 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: early autumn September 2026 Tyumen — light jacket, mild — NO winter, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: apartment entrance / courtyard with suitcase + large Cyrillic hook; early September mood, NOT winter
inline_count 3 (poster + 3 inline panels)

Key facts from article.html:
- Guest paid 3 nights upfront: 12 300 ₽ before taxi even turned into courtyard
- Host in chat: «Пришлите паспорт и селфи — код пришлю сразу» when guests already at entrance with suitcase
- Sent full passport spread + selfie with document in hand — reply «в течение пяти минут» then silence
- No code, no apartment number, no floor — almost 40 minutes at door, suitcase on tile, child needs toilet
- Then «Нужна ещё одна проверка, напишите на другой номер» — chat moved off booking thread
- Documents don't open the lock — they just went to a stranger's phone
- Pressure: «Отправьте сейчас, иначе бронь слетит» — guest with child and luggage at door
- SMS code «для привязки брони» — never forward; not related to check-in
- Normal order reversed: first object, dates, confirmation, access instruction — then minimal data
- Text data enough for contract; selfie with passport is separate heavier ask
- Rule: «Сначала проверка. Потом перевод.» — access before documents, not vice versa
- Checklist: address/dates in same chat, text vs photo, no selfie until explained, written access method, save chat, no SMS codes, platform support if silence >30 min
- Related siblings: B01 beskontaktnoe zaselenie, B08 predoplata tishina, B18 domofon molchit, B13 pustaya klyuchnica

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~5220), фото паспорта при заселении

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).
Poster cover: early September Tyumen entrance — suitcase at door + big hook matching H1 in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «12 300 ₽»)
  GOOD: «двенадцать тысяч», «сорок минут», «паспорт в чат»
  BAD: «12 300 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
