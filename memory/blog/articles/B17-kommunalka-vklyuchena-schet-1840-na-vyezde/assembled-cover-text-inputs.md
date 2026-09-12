# Cover-text inputs B17

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: «Коммуналка включена». На выезде — счётчики и 1 840 ₽
cover_hook MUST match H1 pain (utilities promised included, checkout meter photos + 1 840 ₽ demand). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns: «Включено обещали — доплата на выезде» (5 words)
  OR: «На выезде доплатили 1 840 рублей» (5 words)
  OR: «Три ночи — счёт по счётчикам» (5 words)
  OR: «Коммуналка включена — доплата на выезде» (5 words)
  DO NOT exceed 8 words in hook
Season: September 2026 Tyumen — early autumn, light jacket weather — NO winter, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/screen — never post-paste pill
inline_count 3 (tenant canon)

Key facts from article.html:
- Guest rented one-room apt in Tyumen for 3 nights, paid ~9 600 ₽ (3 200 ₽/night)
- Listing said clearly: «коммуналка включена» — not partial, not by meters
- Normal stay: light, shower, kettle, TV, phone chargers — no industrial load
- On checkout with suitcase at door: 3 meter photos + request to pay 1 840 ₽ «по факту»
- Host quote: «Это по факту расхода — свет, вода, стиралка»
- No starting meter readings photographed at check-in; no «starting from here» in chat
- Electric: final 12 847, host claims start 12 418 → delta 429 kWh × 4,29 ₽ ≈ 1 841 ₽
- 429 kWh in 3 nights ≈ 143 kWh/day — unrealistic for normal guest stay
- Normal 3 nights: 25–55 kWh + 0,4–1,0 m³ water → total utilities ~150–320 ₽ not 1 840 ₽
- Without start readings, host can fold previous month into guest bill
- Checkout pressure: guest leaving soon, inconvenient to argue, easy to pay to end talk
- Key question before payment: «Коммуналка в цене или по счётчикам?»
- If included — get one-line confirmation in chat before transfer
- If by meters — tariffs, starting readings, who records at check-in
- Related cases: taxi 2 400 extra after «all included», deposit not returned, paid for two asked for third
- Moral: «Сначала проверка. Потом перевод.» — final price before money, not at checkout with meter photos
- Checklist: included or separate (written), tariffs + start readings if meters, what’s in utilities, any checkout extras, total for whole stay

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~5220), снять квартиру посуточно в тюмени (~1689)

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).
Poster cover: early-September Tyumen apartment checkout / meter-photo shock + big hook matching H1 in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «1 840 ₽»)
  GOOD: «1 840 рублей», «три ночи», «показания при заезде»
  BAD: «1 840 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
