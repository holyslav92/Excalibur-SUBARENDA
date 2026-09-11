# Cover-text inputs B17

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Залог 5 000 ₽ обещали вернуть утром. А потом — «после уборки»
cover_hook MUST match H1 pain (same story beat — 5 000 ₽ deposit, promised return next morning, then «after cleaning» with no date). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns: «Обещали утром — после уборки» (4 words)
  OR: «Залог пять тысяч — утро прошло» (5 words)
  OR: «Вернуть утром — стало после уборки» (5 words)
  OR: «Утром обещали — деньги зависли» (4 words)
  DO NOT exceed 8 words in hook
Season: autumn September 2026 Tyumen — golden leaves, light jacket, business+leisure trip — NO winter, NO snow, NO fur coats, NO New Year, NO December
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/screen — never post-paste pill
8 images total (1 cover poster + 7 inline), inline_count 7

Key facts from article.html:
- September Tyumen, two nights: part work trip, part walk around city
- Couple paid 5 000 ₽ deposit separately before stay
- Before payment chat: «Вернём утром после выезда»
- Checkout at noon as agreed: keys in keybox, dishes done, towels folded, trash out
- Guest filmed kitchen, room, bathroom on phone, sent photos to chat — not expecting fight, but contactless = proof in chat
- Next promised morning: host message «Залог вернём после уборки» — no day, no hour, no amount status
- Already in taxi, suitcases in trunk, train won't wait — no claims named (no chip, stain, broken cabinet)
- Money didn't vanish — it froze; concrete promise became open-ended wait
- «After checkout» became «after cleaning» — guest can't see or control cleaning process
- Cleaning after checkout is normal for host inspection — but doesn't cancel earlier promised morning return
- Host rule: take money upfront without naming return day on clean checkout = bad practice
- Must say before keys: when money goes back + how (card, SBP, reverse transfer)
- Key question before transfer: «В какой день и на какой счёт вернёте залог, если квартира сдана чистой?»
- Keybox convenient but removes joint walkthrough — chat + photos become normal protection
- Three lines in chat before deposit: return day, return method, condition (full sum if clean, photo+calc if claim)
- Guest often asks about area, bed, parking, contactless check-in — but deposit at last moment; pause one minute
- Moral: «Сначала срок возврата залога. Потом перевод. Не наоборот.»
- Deposit without return date = suitcase in storage without ticket number
- Related siblings: checkout noon train 16:30 luggage, contactless check-in Tyumen, deposit not returned on checkout, cancelled flight prepaid refund
- Host CTA: Telegram · MAX · добрыйдом-72.рф/booking

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~5220), снять квартиру посуточно в тюмени (~1689), залог посуточно тюмень

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 7 inline frames (inline_1 … inline_7).
Poster cover: early-autumn September Tyumen apartment / deposit-freeze mood + big hook matching H1 in Cyrillic.
NO Latin except brand whitelist. Use «перевод», «чат», not SBP/IBAN.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «5 000 ₽»)
  GOOD: «5 000 рублей», «утром обещали», «после уборки»
  BAD: «5 000 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- inline_labels: 2–6 labels per panel
