# Cover-text inputs B26

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Квартира на пятом этаже. Лифт встал — 2 ночи, чемодан внизу

cover_hook MUST match H1 **two-beat** structure (5th floor + stopped elevator + suitcase below after payment). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «Лифт есть» — пятый этаж» (4 words)
  - «Пятый этаж» — лифт встал» (4 words)
  - «Чемодан внизу» — пятый этаж» (4 words)
  - «Лифт встал» — чемодан у бордюра» (5 words)
  - «Галочка лифт» — пять этажей» (4 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: autumn September 2026 Tyumen — light jacket, fallen leaves, golden light — NOT winter, NO snow, NO fur coats
Phone in scene on cover AND inline_1, inline_3, inline_7: +7 (993) 574-83-22 on tablo/magnet/intercom/screen — never post-paste pill
Cover scene: guest with suitcase at apartment entrance, elevator notice «лифт не работает», large Cyrillic two-beat hook; person in scene; autumn mood
inline_count 7 (cover poster + 7 inline panels = 8 frames)
Max 1 cat meme across all 8 frames — prefer people-meme or diagram on inlines only

Key facts from article.html:
- Chat line «Лифт есть, заезжайте» — guest paid 8 400 ₽ for two nights
- Card had elevator checkbox — elevator exists in building but stopped for repair on arrival day
- Apartment on 5th floor; suitcase at curb after taxi
- Handwritten notice on elevator door: «Лифт не работает»
- Guest asked «Лифт есть?» — got honest «да» but not «works today» or floor
- Host reply pattern: «На пятом. Обычно лифт ходит, сегодня ремонт. Поднимайтесь»
- Guest: «Но вы писали, что лифт есть» — host: «Так он есть. Просто сегодня не работает»
- Two scenarios: no elevator at all vs broken today — different questions
- Ask BEFORE payment: exact floor, elevator working TODAY, repair photo, baggage help, which entrance
- Paper on door may be stale — message host before climbing stairs
- Moral: «Сначала проверка. Потом перевод.»
- Related: B18 domofon, B06 chemody mezhdu, B01 beskontaktnoe zaselenie

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4570), снять квартиру посуточно в тюмени (~1404)

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for cover + 7 inline frames (inline_1 … inline_7).
Poster cover: autumn Tyumen entrance — guest + suitcase + elevator notice + big two-beat hook in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only)
  GOOD: «восемь тысяч четыреста», «пятый этаж», «лифт встал»
  BAD: «8 400 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
- inline_labels: 2-6 labels per panel, each 1-4 words
