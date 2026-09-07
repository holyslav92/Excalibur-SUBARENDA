# Cover-text inputs B13 — Добрый дом

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1 (reference, do NOT copy verbatim): «Две ночи, 8 400 ₽. К ночи кода нет — отчёт горит»
Season: early September 2026 — NO snow, NO winter hero, autumn business-trip mood
Tenant: Добрый дом, посуточная аренда Тюмень

## Case facts from article.html

- Business trip to Tyumen, two nights, ~8 400 ₽ paid
- Morning call ~10:00: calm voice «всё ок, вечером пришлю код»
- Guest left for work; by night — no code, closed entrance, suitcase on asphalt
- Chat replies: «сейчас пришлю» → silence
- Parallel: accounting needs contract + act + receipt by Monday — advance report won't close
- Only messenger chat + transfer screenshot — not enough for accounting
- Trap: softer than total silence — hope keeps guest waiting, loses time to find backup
- Before pay: ask closing docs, who is landlord, receipt from «Мой налог» if self-employed
- When code arrives, where sent, backup contact at night
- Intercom code vs lock code may differ; keybox option
- Host practice: text first (docs + entry instruction), then payment — never pay before code/docs in writing
- 9 questions checklist before payment
- Verdict: oral «всё ок» is not a key; written plan before money

## Wordstat guest queries (Tyumen 55+11176)

- квартиры посуточно тюмень
- снять квартиру посуточно в тюмени
- жильё посуточно тюмень

## Gate fix required

Previous attempt BLOCKED: inline_2.label "8 400 ₽ за 2 ночи" has 6 words — each label MUST be 1-4 words max.
Also BLOCKED: labels with only digits/symbols (e.g. "8 400 ₽") fail — every label needs at least one Cyrillic letter.


Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions.
inline_labels: inline_1, inline_2, inline_3 (3 inline panels per tenant gen_only_slice4).
Poster cover hook: 2–8 words, simple Russian, cable pain — person may be in scene (guest at door), large Cyrillic hook.
Phone +7 (993) 574-83-22 is Cover prompt sticker — do NOT add phone field to JSON.
NO logo in generation. NO +7 922 001 65 05.
