# Cover-text inputs B15

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: «Рабочий стол» обещали. За 11 400 ₽ — журнальный столик
cover_hook MUST match H1 pain (same story beat — promised work desk + 11 400 ₽ for three nights + coffee table instead). May split two lines for poster Cyrillic:
  line1 ««Рабочий стол» обещали»
  line2 «11 400 ₽ — журнальный столик»
Season: early September 2026 Tyumen, warm late-summer business-trip apartment — NO winter, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/screen — never post-paste pill
4 images total (1 cover + 3 inline), inline_count 3

Key facts from article.html:
- Guest on business trip, three nights, paid 11 400 ₽ upfront
- Chat promised: «всё есть», fast internet, documents will be sent
- Late check-in: called at 10:00, arrived around 22:00
- Instead of work desk — coffee table by sofa; socket behind sofa, cable doesn't reach
- Wi-Fi in room ~8 Mbps: messenger works, video call breaks — colleagues hear «you're dropping out»
- Host: «ну вы же не просили отдельно рабочее место» — formally true, practically useless for work
- «Wi-Fi есть» ≠ video call will work — need speed test from laptop spot, not near router
- Work place needs: table for laptop+papers, chair, light, socket within cable reach — ask photo of table+socket in one frame
- Closing documents: «справку пришлём после выезда» — bad word «потом»; fix list and deadline in chat before payment
- Reviews 4,8 won't tell about desk/socket/Wi-Fi for video calls
- Related: «всё включено» taxi 2 400 ₽, prepaid silence in chat, checkout 12:00 train 16:30
- Moral: «Сначала проверка. Потом перевод.» — ask desk photo, Wi-Fi test from work spot, documents before payment
- Host must show work spot, socket, speed measurement before transfer

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~5220), снять квартиру посуточно в тюмени (~1689), квартира посуточно тюмень командировка

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).
Poster cover: early-September Tyumen apartment work-from-home fail mood + big hook matching H1 in Cyrillic.
NO Latin except brand whitelist. Use «интернет», «созвон», not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS (attempt 2 still BLOCK):
- hook: MAX 8 words — USE THIS EXACT PATTERN (7 words): «Рабочий стол» — журнальный столик
  OR (5 words): Обещали стол — дали столик
  DO NOT put price in hook (11 400 adds words)
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «11 400 ₽»)
  GOOD: «11 400 рублей», «звонок в десять», «заезд в десять»
  BAD: «10:00 звонок», «22:00 заезд», «11 400 ₽» (no Cyrillic)
- highlight must be exact substring of hook
