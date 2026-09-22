# Cover-text inputs B33

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Бронь на Авито уже оплачена. В чате: второй перевод на карту

cover_hook MUST match H1 **two-beat** structure (Avito booking already paid → chat asks second card transfer). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «На Авито оплачено — снова на карту» (6 words)
  - «Бронь оплачена — второй перевод» (4 words)
  - «Чек есть — просят перевести снова» (5 words)
  - «Оплата прошла — дубль на карту» (5 words)
  - «Заказ оплачен — в чате ещё раз» (6 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook (Cyrillic word preferred for pink highlight)

Season: early autumn 22 September 2026 Tyumen — mild, yellow leaves, light jacket — NO winter hero, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: phone with Avito «оплачено» + chat bubble «продублируйте на карту» — large Cyrillic two-beat hook matching H1; September mood, NOT winter
inline_count **7** (standalone poster + 7 inline panels from 2 quad canvases — like B30 longform manifest)

Key facts from article.html:
- Guest booked Tyumen two nights; total 8 000 ₽: 4 200 ₽ via Avito + 3 800 ₽ at check-in per order/card
- After «оплачено» status + receipt, chat: «Предоплату на карту продублируйте, бухгалтерия не видит»
- Host line: «Это другая оплата» / «отмените заказ — переведёте напрямую 8 000»
- Not zalog — same prepayment twice; zalog must be pre-disclosed separately (B28 link)
- Host commission context season 2026: 20% / 17% / 15% on Avito — explains motive, not guest obligation
- After cancel + card transfer: no protected order; support 8 804 700-04-40 with order number + screenshots
- Dobry dom rule: «Нет. Так не заселяем.» — no second prepayment off-platform if already paid on Avito
- Moral: «Сначала проверка. Потом перевод.» — paid booking is lock on platform, card off-order removes it
- Unlock question: «А где в заказе Avito написано, что предоплату нужно платить второй раз на карту?»

Wordstat guest queries (Tyumen): квартиры посуточно тюмень, снять квартиру посуточно в тюмени, авито квартиры посуточно тюмень

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
Poster cover: 22 Sep 2026 autumn Tyumen + Avito paid order vs chat card transfer beat + big two-beat hook in Cyrillic matching H1.
Use «Авито» Cyrillic not Latin Avito. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after (cover + inline slots 1,3,7 per tenant).
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «4 200 ₽»)
  GOOD: «второй перевод», «чек в заказе», «не отменяйте»
  BAD: «4 200 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
