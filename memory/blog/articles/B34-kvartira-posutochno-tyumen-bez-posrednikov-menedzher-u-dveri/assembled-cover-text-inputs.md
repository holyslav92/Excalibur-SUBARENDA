# Cover-text inputs B34

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: «От хозяев» в фильтре. У двери менеджер: ещё 2 000 ₽ на карту

cover_hook MUST match H1 **two-beat** structure (filter «от хозяев» / без посредников → manager at door + card transfer 2 000 ₽ not in booking). **Must mention September Tyumen season** in the hook (early autumn student move-in mood). 2–8 words MAX Cyrillic poster headline.

  GOOD patterns (season + two-beat):
  - «Сентябрь в Тюмени — менеджер у двери» (5 words) + sticky carries filter beat
  - «От хозяев в сентябре — 2 000 у двери» (7 words)
  - «Сентябрь, Тюмень: от хозяев — доплата у двери» (7 words)
  - «Фильтр от хозяев — у двери ещё 2 000» (7 words) — add «сентябрь» if fits in 8 words
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook (Cyrillic word preferred for pink highlight)

Season: **23 September 2026 Tyumen** — mild early autumn, yellow leaves, light jacket, student arrivals — NO winter hero, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: filter «от хозяев» on phone + manager with tablet at apartment door + «2 000 на карту» — large Cyrillic two-beat hook matching H1; September mood, NOT winter
inline_count **3** (tenant inline_image_count=3 — inline_1 … inline_3 only)

Key facts from article.html:
- Guest searched **квартиры посуточно тюмень без посредников**, filter «от хозяев», booked **two nights**
- **7 400 ₽** paid via platform — full price in booking, no extra lines
- At door: stranger with tablet: «I'm manager, owner busy. 2 000 ₽ for paperwork — card transfer»
- **2 000 ₽** not in price, notes, or chat; word «manager» not in listing
- Pressure line: «But you already arrived»
- Filter narrows search but doesn't guarantee owner at door; new mandatory fee after payment is the scam pattern
- Unlock question: «Who checks in in person and is there a fee besides booking price?»
- Dobry dom: «Нет. Так не заселяем.» — **Сначала проверка. Потом перевод.**
- Sutochno support: 8 (800) 555-26-08, +7 (499) 653-99-26
- Interlink siblings: B04 door extra guest, B18 code/domofon, B28 zalog

Wordstat guest queries (Tyumen live): квартиры посуточно тюмень без посредников (244), снять квартиру посуточно в тюмени без посредников (114), квартиры посуточно в тюмени недорого без посредников (126)

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for **3** inline frames (inline_1 … inline_3).

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
    "inline_3": ["…", "…"]
  }
}
```
Each inline_* value MUST be an ARRAY of 2-6 strings (never a single string).
sticky: max 5 words total (no period-sentence).
Poster cover: 23 Sep 2026 autumn Tyumen + «от хозяев» filter vs manager at door + 2 000 card beat + big hook in Cyrillic matching H1.
Use «интернет» not Wi-Fi. No Latin Avito — say «площадка» or «бронь».
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «7 400 ₽»)
  GOOD: «две ночи», «фильтр от хозяев», «не в брони»
  BAD: «7 400 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat

---

RETRY (gate failed): hook was 9 words — MUST be 2-8 words exactly. Use hook «Сентябрь: от хозяев — 2 000 у двери» (8 words) OR «Сентябрь в Тюмени — менеджер у двери» (5 words). Count every token separated by space.
Fix labels: MAX 4 words each — «семь тысяч в брони» not «7 400 ₽ в брони»; «две тысячи на карту» not «2 000 ₽ на карту». Every label needs Cyrillic letters.
