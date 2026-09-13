# Cover-text inputs B19

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Написали «не курили». В спальне — запах и окно на замке: 35 минут ожидания ключа
cover_hook MUST match H1 pain (card promised «не курили», bedroom smells of smoke, window locked on child safety key, 35 min waiting in hallway). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns: «Не курили» — а пахнет» (4 words)
  OR: «Запах в спальне, окно на замке» (5 words)
  OR: «Тридцать пять минут у двери» (5 words)
  OR: «Обещали не курили — пахнет» (5 words)
  OR: «В спальне запах — окно закрыто» (5 words)
  DO NOT exceed 8 words in hook
Season: early autumn September 2026 Tyumen — light jacket weather — NO winter, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: hallway or bedroom doorway + large Cyrillic hook; early autumn apartment, NOT winter
inline_count 7 (poster + 7 inline panels)

Key facts from article.html:
- Card said «не курили» — family arrived evening with child and bags
- Opened bedroom — old tobacco smell in curtains, pillows, fabric, air
- Wrote host: «В спальне пахнет, окно не открывается» — reply «Сейчас уточню, подождите»
- Window has child safety lock, handle closed with key, opens only narrow gap (~8 cm)
- No key in apartment — cannot ventilate bedroom
- Stood in hallway 35 minutes — shoes on, bags not unpacked, child not settled
- Booking: two nights ~4 800 ₽ each — but issue is smell + locked window, not price
- Don't investigate who smoked — document fact: smell at entry, card promised otherwise
- Message template: «В спальне запах табака, проветрить не получается, окно закрыто на ключ»
- Video from doorway: door, bedroom, window handle, gap attempt
- Child safety vs broken mechanism — host must provide key or replacement
- Don't repair handle yourself — risk of damage dispute and deposit
- 35 minutes matters: before unpacking you can still refuse, replace, or get key
- After first night same conversation sounds different — «why did you stay?»
- Checklist: enter bedroom before unpacking; ask about child window locks and key location; write immediately; short video; wait for key/ventilation/replacement; don't DIY hardware
- Moral: «Сначала проверка. Потом перевод.»
- Related siblings: B11 mokryj kovrik (card vs reality), B02 zalog not returned, B16 predoplata before check, B18 domofon silent 20 min

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4826), аренда квартиры посуточно

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 7 inline frames (inline_1 … inline_7).
Poster cover: early-autumn Tyumen apartment — smoke smell + locked window + big hook matching H1 in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «4 800 ₽»)
  GOOD: «четыре тысячи восемьсот», «тридцать пять минут», «окно на замке»
  BAD: «4 800 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
