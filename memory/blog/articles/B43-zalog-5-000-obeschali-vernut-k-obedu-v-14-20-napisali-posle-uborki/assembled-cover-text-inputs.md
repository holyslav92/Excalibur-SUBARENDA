# Cover-text B43

H1: 5 000 ₽ залога посуточно: обещали «к обеду». В чате — «после уборки»

Article gist (from article.html):
- Guest paid 5 000 ₽ deposit before check-in; host promised return «к обеду» after keys returned.
- After checkout: no damage claims, but at 14:20 message changed to «верну после уборки» — no new time, no hold amount.
- Pain: suitcase at station, promise dissolved into host's cleaning schedule.
- Before transfer: need sum, return deadline, transfer method, hold rules in chat — not «потом».
- On exit: photo/video, ask «претензий нет? возврат к какому времени?»; save both «к обеду» and «после уборки» messages.
- Tyumen short-term rental host voice «Добрый дом»; editorial composite story.

Season on cover (HARD): **осень** — October vibe in hook or sticky or inline_3 (cool morning, wet leaves, station with luggage — not summer beach).

Wordstat Tyumen (live P0):
- залог посуточно (compare RU 225; Tyumen cluster)
- квартиры посуточно тюмень
- снять квартиру посуточно в тюмени

Phone in scene only (+7 993 574-83-22) — do not add phone field to JSON.

Output: ONLY valid JSON for cover/cover-text.json per skills/cover-text-excalibur-blog/SKILL.md
- hook 2-8 words Cyrillic, not copy H1 verbatim
- highlight one word from hook (case-insensitive match)
- sticky ≤5 words
- wordstat_stickers 1-3 guest queries
- inline_labels inline_1..inline_3 only (tenant inline_image_count=3), each 2-6 labels, 1-4 words each
