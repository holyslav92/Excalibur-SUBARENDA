# Cover-text inputs B28

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: «Бухгалтер: чек и справка до оплаты. 2 ночи — в чате «мы не гостиница»»

cover_hook MUST match H1 **two-beat** structure (accountant needs docs before payment → host chat «мы не гостиница»). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «Чек и справка до оплаты» (5 words)
  - «Бухгалтер ждёт чек» — «мы не гостиница»» (5 words)
  - «Две ночи — без чека не закроют» (5 words)
  - «Справка и чек» — «мы не гостиница»» (5 words)
  - «В чате: мы не гостиница» (4 words)
  - «Командировка две ночи» — «документов нет» (4 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: autumn 2026 Tyumen — light jacket, yellow leaves — NOT winter, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: business traveler with phone/chat + suitcase + large Cyrillic two-beat hook; autumn mood, person in scene, NOT winter
inline_count 3 (poster + inline 1-3)

Key facts from article.html:
- Accountant wrote before booking: need справка о проживании + чек; without them advance report won't close
- Business trip Tyumen — 2 nights only
- Guest asked host for closing docs; host one-liner: «Мы не гостиница»
- Private rental = найм жилья, NOT hotel form 3-Г — package: договор найма + чек/платёжка/Мой налог
- Guest almost paid before clarifying what documents they'll get
- Key question before payment: «Справку о проживании и чек для отчёта дадите до оплаты — в каком виде?»
- Good host answers concretely: самозанятый + договор + чек Мой налог; or ИП + кассовый чек с QR
- Bad answers: «потом решим», «вам зачем, вы же на две ночи»
- Advance report deadline: 3 рабочих дня after return
- Card promises «отчётные документы» ≠ guaranteed package — verify per booking
- Moral: «Сначала проверка. Потом перевод.» — ask for PDF samples before transfer
- Related siblings: B22 prepay before chat answer, B10 «all included» surprise, B06 checkout vs train

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4826), снять квартиру посуточно в тюмени

Output ONLY valid JSON — EXACT schema (field names matter):
```json
{
  "hook": "Чек и справка — мы не гостиница",
  "highlight": "справка",
  "sticky": "Сначала проверка",
  "wordstat_stickers": ["квартиры посуточно тюмень"],
  "inline_labels": {
    "inline_1": ["бухгалтер ждёт чек", "две ночи", "до оплаты"],
    "inline_2": ["договор найма", "чек мой налог", "не гостиница"],
    "inline_3": ["образцы в пдф", "спросите до перевода", "три дня на отчёт"]
  }
}
```
Use field name **hook** (NOT cover_hook). highlight = ONE word inside hook. inline_labels values = arrays of 2-6 strings each.
Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1 … inline_3).
Poster cover: autumn Tyumen — business traveler with phone showing chat + suitcase + big two-beat hook in Cyrillic; person in scene.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «1 500 ₽»)
  GOOD: «две ночи», «чек до оплаты», «мы не гостиница»
  BAD: «2 ночи» alone if no Cyrillic — prefer «две ночи»
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
