# Cover-text inputs B16

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Рейс отменили. 4 200 ₽ обещали вернуть за три дня — срок вышел
cover_hook MUST match H1 pain (same story beat — cancelled flight, 4 200 ₽ prepaid, promised refund in three days, fourth day no money). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns: «Рейс отменили — срок вышел» (5 words)
  OR: «Обещали три дня — денег нет» (5 words)
  OR: «4 200 рублей — срок вышел» (4 words, include Cyrillic «рублей» not digits-only)
  DO NOT exceed 8 words in hook
Season: early September 2026 Tyumen, autumn business-trip mood — golden leaves, light jacket weather — NO winter, NO snow, NO fur coats, NO New Year, NO December
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/screen — never post-paste pill
4 images total (1 cover + 3 inline), inline_count 3

Key facts from article.html:
- Guest booked two nights in Tyumen, paid 4 200 ₽ prepaid
- Flight cancelled day before check-in; guest asked for refund immediately
- Host replied politely: «Вернём после проверки, в течение трёх дней»
- Fourth day: same minus 4 200 ₽ on card, host says «ещё проверяем»
- Problem: «three days» without calendar send date, channel (platform vs direct transfer), working vs calendar days
- One question before payment: «Если поездка сорвётся до заселения, в какой день и каким способом вы вернёте предоплату?»
- Good answer needs date + channel, not «after verification»
- Collect: receipt, listing cancellation terms, full chat with promise, flight cancellation proof
- Related: prepaid silence in chat (3 000 ₽), paid for two asked extra for third, deposit not returned
- Moral: «Сначала проверка. Потом деньги и ключи.» — refund date and method before transfer
- Host must name refund amount, free-cancel deadline, calendar send date, route (platform or same transfer)

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~5220), снять квартиру посуточно в тюмени (~1689)

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).
Poster cover: early-September Tyumen autumn apartment / travel-cancel mood + big hook matching H1 in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «4 200 ₽»)
  GOOD: «4 200 рублей», «три дня обещали», «четвёртый день тишина»
  BAD: «4 200 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
