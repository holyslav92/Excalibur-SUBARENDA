# Cover-text inputs B26

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Квартира дешевле отеля за ночь. За две ночи — 13 400 ₽

cover_hook MUST echo H1 two-beat (cheaper per night in search → full trip total shocks). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «В карточке дешевле — в счёте 13 400» (5 words)
  - «4 200 за ночь — итог 13 400» (5 words)
  - «Дешевле в поиске — дороже в счёте» (5 words)
  - «Квартира дешевле — счёт 13 400» (4 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: mid-September autumn 2026 Tyumen — yellow leaves, light jacket, bright apartment — NOT winter, NO snow, NO frost
Phone in scene on cover: +7 (993) 574-83-22 on tablo/magnet/screen — never post-paste pill
Cover scene: guest at laptop/phone sees booking final screen with itemized fees; large Cyrillic two-beat hook under H1 mood; September autumn light through window
inline_count 7 (2 canvases longform)

Key facts from article.html:
- Search: apartment 4 200 ₽/night vs hotel 4 800 ₽/night — mental math 8 400 vs 9 600 for 2 nights
- Final payment screen: base 8 400 ₽ + cleaning, linens, service fee, guest/parking surcharges = 13 400 ₽ total
- 5 000 ₽ «extra» above base — not necessarily fraud; guest compared storefront price to full bill
- Tyumen example: cleaning 1 500 ₽ separate line; deposit 5 000 ₽ on another listing (4 700 ₽/night)
- Guest trap: saw 4 700 ₽ and thought that was the price
- Deposit 5 000 ₽ is NOT trip cost if returned — two wallets: payment total vs refundable deposit
- Key question before pay: what is on final screen AND what returns from deposit
- Compare same dates, same nights, same guest count — full stay total not «от» per night
- Host practice: stop payment until line-by-line total shown
- Moral: «Сначала проверка. Потом перевод.»

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4724), снять квартиру посуточно в тюмени (~1452)

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 7 inline frames (inline_1 … inline_7).

REQUIRED JSON SHAPE (inline_labels values are ARRAYS of 2-6 short strings each, NOT single strings):
```json
{
  "hook": "…",
  "highlight": "…",
  "sticky": "…",
  "inline_labels": {
    "inline_1": ["…", "…", "…"],
    "inline_2": ["…", "…"],
    …
    "inline_7": ["…", "…", "…"]
  },
  "wordstat_stickers": ["…", "…"]
}
```
Poster cover: mid-September Tyumen apartment — guest comparing phone/laptop booking screen + large two-beat hook in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
Max 1 cat meme across article — prefer people-meme on one inline only.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words (count every space-separated token including digits and ₽) AND must contain at least one Cyrillic letter
  BAD (5 words): «4 200 ₽ за ночь», «Отель — 4 800 ₽», «Сверх базы: 5 000 ₽»
  GOOD (≤4): «4 200 за ночь», «отель 4 800», «итог 13 400», «уборка 1 500»
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
