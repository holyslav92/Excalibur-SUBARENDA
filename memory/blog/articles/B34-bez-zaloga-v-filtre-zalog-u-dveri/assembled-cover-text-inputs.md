# Cover-text inputs B34

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: В фильтре — «без залога». У двери попросили 5 000 ₽ на личную карту

cover_hook MUST match H1 **two-beat** structure (filter «без залога» chosen → at door 5 000 ₽ to personal card before keys). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «Без залога в фильтре — пять тысяч у двери» (7 words)
  - «Фильтр без залога — перевод у двери» (5 words)
  - «В фильтре без залога — карта у двери» (6 words)
  - «Выбрал без залога — у двери пять тысяч» (6 words)
  DO NOT exceed 8 words in hook
  CRITICAL: gate splits hook on whitespace — em-dash «—» alone counts as one word. Max 7 words + optional «—» = 8 tokens total.
  highlight must be exact one-word substring of hook (Cyrillic word preferred for pink highlight)

Season: late September 2026 Tyumen — early autumn, yellow leaves, light jacket, mild evening — NO winter hero, NO snow, NO fur coats, NO New Year
Layout note: standalone cover + 2 quad canvases × 4 panels = 8 images (7 inline frames + cover); label all inline_1 … inline_7 for longform quad manifest
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: phone filter «без залога» + QR/card at apartment door — large Cyrillic two-beat hook matching H1; September mood, NOT winter

Key facts from article.html:
- Guest in Tyumen search: filter «без залога», one night 4 800 ₽, paid on platform, no deposit in card or booking terms
- At door with suitcase and tired child: «Страховой залог пять тысяч, на карту, потом ключи» + QR
- Host renames: «Это не залог, это страховка мебели» — same 5 000 ₽, personal card, off-order
- Three cases: disclosed deposit in card vs balance at check-in per booking vs surprise «insurance» at door
- Avito online booking: payment must stay on platform — card transfer at door breaks agreed terms
- Dobry dom rule: «Нет. Так не заселяем.» — no deposit if card says none; no new 5 000 on landing renamed
- Unlock question: «Где в условиях брони написано, что перед ключами нужно перевести 5 000 ₽ на личную карту?»
- Moral: «Сначала проверка. Потом перевод.» — filter «без залога» is a promise until keys
- Checklist: screenshot filter + terms; open order at door; distinguish booking balance vs new door sum; no SBP to individual if not in order

Wordstat guest queries (Tyumen): квартиры посуточно тюмень, снять квартиру посуточно в тюмени

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for **7** inline frames (inline_1 … inline_7).

JSON SHAPE (HARD — gate rejects wrong types):
```json
{
  "hook": "…",
  "highlight": "…",
  "sticky": "…",
  "wordstat_stickers": ["…", "…"],
  "inline_labels": {
    "inline_1": ["…", "…"],
    "inline_2": ["…", "…"],
    "inline_3": ["…", "…"],
    "inline_4": ["…", "…"],
    "inline_5": ["…", "…"],
    "inline_6": ["…", "…"],
    "inline_7": ["…", "…"]
  }
}
```
Each inline_* value MUST be an ARRAY of 2–6 strings (never a single string).
sticky: max 5 words total (no period-sentence).
Use «интернет» not Wi-Fi. Cyrillic «Авито» if needed.
NO logo in generation — factory paste after (cover only per gen_only canon).
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «5 000 ₽»)
  CRITICAL: spaced digits count as separate words — «4 800 ₽ за ночь» = 5 words BLOCK. Use «ночь 4800 ₽» or «4800 за ночь» (3 words).
  GOOD: «фильтр без залога», «QR у двери», «не в заказе»
  BAD: «5 000 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
