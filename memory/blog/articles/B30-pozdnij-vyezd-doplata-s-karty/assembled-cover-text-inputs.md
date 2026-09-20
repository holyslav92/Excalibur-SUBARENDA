# Cover-text inputs B30

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Продление до двух согласовали. После сдачи ключей с карты списали 1 800 ₽

cover_hook MUST match H1 **two-beat** structure (agreed extension until 2pm → after keys returned, 1 800 ₽ charged from card). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «До двух согласовали — списали с карты» (5 words)
  - «Ключи сдал — минус полторы тысячи» (5 words)
  - ««До двух можно» — пуш в такси» (5 words)
  - «Продление согласовали — карта минус» (4 words)
  - «Согласовали до двух — списали полторы» (5 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: early autumn September 2026 Tyumen — mild, yellow leaves, light jacket — NO winter hero, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: lockbox/key handoff + phone bank push — large Cyrillic two-beat hook matching H1; September mood, NOT winter
inline_count 3 (poster + 3 inline panels)

Key facts from article.html:
- Chat: «До двух можно» — extension agreed; checkout rules said noon, extended to 14:00
- Keys in lockbox ~14:38 — 38 minutes after agreed time
- In taxi: bank push −1 800 ₽ — guest: «Я же ключи уже сдал»; host: «Поздний выезд по тарифу»
- No price for extension in chat before exit; no rule after 14:00; no warning about auto charge from card
- Guest thought hold was «zalog» — saw new charge after exit, not return
- Moral: «Сначала проверка. Потом перевод.» — three lines before keys: time, extension fee, rule after time
- Related: B21 early check-in wait, B06 suitcases between checkout and train, B28 hold vs charge, B23 different 1800 story (sheets)

Wordstat guest queries (Tyumen): квартиры посуточно тюмень, снять квартиру посуточно в тюмени

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).
Poster cover: September Tyumen — lockbox/keys + bank push beat + big two-beat hook in Cyrillic matching H1.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «1 800 ₽»)
  GOOD: «полторы тысячи», «ключи в локбоксе», «поздний выезд»
  BAD: «1 800 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
