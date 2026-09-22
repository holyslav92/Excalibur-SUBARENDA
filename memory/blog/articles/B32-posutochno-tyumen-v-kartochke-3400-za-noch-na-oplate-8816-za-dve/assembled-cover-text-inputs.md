# Cover-text inputs B32

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: В карточке 3 400 ₽ за ночь. На оплате — 8 816 ₽ за две ночи

cover_hook MUST match H1 **two-beat** structure (card shows 3 400 ₽/night → payment step 8 816 ₽ for two nights). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «В карточке 3400 — на оплате 8816» (5 words)
  - «3400 в карточке — 8816 на оплате» (5 words)
  - «Карточка три четыреста — оплата восемь тысяч» (5 words)
  - «В карточке 3400 — кнопка 8816» (5 words)
  - «Три четыреста в карточке — восемь восемьсот на оплате» (6 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook (Cyrillic word preferred for pink highlight)

Season: early autumn 22 September 2026 Tyumen — mild, yellow leaves, light jacket — NO winter hero, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: phone/booking checkout screen + payment total surprise — large Cyrillic two-beat hook matching H1; September mood, NOT winter
inline_count 3 (poster + 3 inline panels)

Key facts from article.html:
- Guest searched квартира посуточно в Тюмени, two nights; card showed bold 3 400 ₽/night → mental math 6 800 ₽
- Payment button: 8 816 ₽ total — gap 2 016 ₽ vs expectation
- Breakdown: 6 800 ₽ lodging + 816 ₽ service (+12% editorial example) + 1 200 ₽ cleaning once per booking
- Effective ~4 408 ₽/night after stack — compare hotel on full total, not shelf price
- One-liner unlock: «А где до оплаты увидеть всю сумму — вместе с уборкой и сервисным сбором?»
- Moral: «Сначала проверка. Потом перевод.» — price per night is vitrine, not cash register
- Related interlinks: «всё включено» taxi 2 400; уборка на выезде 1 800; доплата за третьего у двери
- Editorial numbers — not Dobry dom tariff; illustrate checkout stack pattern

Wordstat guest queries (Tyumen): квартиры посуточно тюмень, снять квартиру посуточно в тюмени, квартиры посуточно в тюмени недорого

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).

JSON SHAPE (HARD — gate rejects wrong types):
```json
{
  "hook": "…",
  "highlight": "…",
  "sticky": "…",
  "wordstat_stickers": ["…", "…"],
  "inline_labels": {
    "inline_1": ["строка1", "строка2", "строка3"],
    "inline_2": ["…", "…"],
    "inline_3": ["…", "…"]
  }
}
```
Each inline_* value MUST be an ARRAY of 2–6 strings (never a single string).
sticky: max 5 words total (no period-sentence — e.g. «итог до оплаты» or «сначала проверка»).
Poster cover: 22 Sep 2026 autumn Tyumen mood + booking card vs payment total beat + big two-beat hook in Cyrillic matching H1.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «8816 ₽»)
  GOOD: «сервисный сбор», «уборка отдельно», «итог на оплате»
  BAD: «8 816 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
