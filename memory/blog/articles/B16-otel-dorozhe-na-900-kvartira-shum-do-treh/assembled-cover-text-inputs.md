# Cover-text inputs B16

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Отель был дороже на 900 ₽ за ночь. Квартира — две ночи без сна
cover_hook MUST match H1 pain (same story beat — hotel +900 ₽/night vs apartment + two sleepless nights from corridor noise). May compress for poster Cyrillic (2–8 words MAX):
  GOOD patterns: «Тихо как дома» — коридор до трёх | Дешевле на 900 — две ночи без сна | Квартира дешевле — коридор до трёх
  DO NOT exceed 8 words in hook. Price «900» may stay if total words ≤8.
Season: early September 2026 Tyumen, warm late-summer apartment near elevator landing — NO winter, NO snow, NO fur coats, NO New Year
Phone: +7 (993) 574-83-22 in article TEXT only — NOT on cover image (gen_only_human_v1)
4 images total (1 cover + 3 inline), inline_count 3

Key facts from article.html:
- Host wrote «Тихо, как дома» — apartment cheaper than hotel by 900 ₽/night for couple, three nights
- Night 1: not apartment noise — corridor: doors slam, elevator arrives, people talk on landing until 3 AM
- Night 2: same — two nights without sleep, morning meetings with foggy head
- Night 3: booked hotel ~4 500 ₽ — savings of 900 ₽/night became extra cost + two lost nights
- Nobody lied on purpose — «тихо, как дома» means different things to host (inside flat) vs guest (sleep)
- «Тихая квартира» in listing = windows, fridge, exhaust — guest buys sleep, hears landing/lift
- Host can't stop lift or neighbors at 3 AM — must warn BEFORE payment, not «ну это же МКД» in morning
- Reviews high rating «чисто», «удобное заселение» — rarely mention corridor, lift, landing at night
- Ask host: near lift? hear landing? night noise complaints? not just «у вас тихо?»
- Hotel +900 ₽: not perfect silence but 24/7 desk, staff at 3 AM, sometimes another room — compare YOUR hotel vs THIS flat
- Related articles: «тихий дом» music at 23:40, «тихий центр» crane at 6:30, rating 4,8 two «всё супер»
- Moral: «Сначала проверка. Потом перевод.» — five questions before payment (noise in reviews, lift location, who answers at night, quiet rules, what hotel gives for +900)
- Closing list: reviews mention night noise? flat vs lift/door? who answers at night? quiet rules? hotel difference for +900?

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~5220), снять квартиру посуточно в тюмени (~1689), квартира посуточно тюмень шум

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).
Poster cover: early-September Tyumen apartment corridor/elevator noise mood + big hook matching H1 in Cyrillic painted on physical object in scene.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi if needed.
NO logo in generation — factory paste after.
NO host face on cover.
NO meme panels (gen_only_human_v1 — photoreal only).
wordstat_stickers optional array for inline context only — NOT rendered on cover.

GATE HARD LIMITS:
- hook: 2–8 words Cyrillic, highlight must be exact substring of hook
- sticky: ≤5 words
- each inline label: 1–4 words AND must contain at least one Cyrillic letter (not digits-only)
  GOOD: «900 рублей за ночь», «лифт на площадке», «до трёх утра»
  BAD: «900 ₽» alone (no Cyrillic), «4 500 ₽» alone
- inline_1..3: each 2–6 labels
