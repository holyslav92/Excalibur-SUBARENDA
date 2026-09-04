# Cover-text inputs B10

Return ONLY valid JSON for cover/cover-text.json per cover-text skill. NO BLOCKER prose.

**H1:** «Горячая вода есть». Включили душ — лёд и 40 минут нагрева

**Subject:** Горячая вода и выключенный бойлер при заселении в квартиру посуточно в Тюмени.

**cover_hook for Cyrillic poster (2–8 words, NOT verbatim H1):** «Горячая вода есть» — включили душ, лёд и 40 минут нагрева. Suggested two-line poster: line1 «Горячая вода есть» line2 «душ — лёд, 40 минут»

**Season:** early September 2026, Tyumen — autumn light, NO winter, NO snow on cover.

**Phone:** +7 (993) 574-83-22 (tenant phone, not in JSON fields — Cover agent handles sticker).

**inline_count:** 3 (cover + inline_1..inline_3 only).

**wordstat_p0:** квартиры посуточно тюмень

**Facts from article for inline_labels:**
- Guest arrived by car after road trip, turned on shower ~10 min after entry — ice-cold water
- Boiler found OFF in bathroom; ~40 minutes to heat after turning on
- Listing said «горячая вода есть» and «всё для душа» before payment
- Early September: city hot-water shutdowns should be over; cold water likely from off boiler/Vacation/ECO mode
- Central GVS: give 1–2 min flush; if still cold — photo faucet + boiler display, message host
- Ask before payment: «Где бойлер и как включить ДО душа?»
- Rule: сначала проверка, потом перевод

**Required JSON keys:** hook, highlight, sticky, wordstat_stickers (1–3 guest queries), inline_labels with inline_1, inline_2, inline_3 (each 2–6 labels, 1–4 words).
