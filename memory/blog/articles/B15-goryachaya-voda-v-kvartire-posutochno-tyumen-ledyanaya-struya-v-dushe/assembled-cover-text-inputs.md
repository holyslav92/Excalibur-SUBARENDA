# Cover-text inputs B15

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: «Горячая вода есть». В душе — ледяная струя, ждать 40 минут
cover_hook MUST match H1 pain (same story beat — «горячая вода есть» promise + icy shower stream + wait 40 minutes). May split two lines for poster Cyrillic:
  line1 ««Горячая вода есть»»
  line2 «В душе — ледяная струя, 40 минут»
Season: early September 2026 Tyumen, late evening bathroom/apartment mood — NO winter, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/screen — never post-paste pill
4 images total (1 cover + 3 inline), inline_count 3

Key facts from article.html:
- Listing wrote «Горячая вода есть» + «всё для душа», bathroom photos, confident offer
- Guest paid 7800–9600 ₽ upfront for 2–3 nights, late check-in after travel
- Opens door, expects quick shower and sleep — icy stream from tap
- Host in chat: «включите бойлер, подождите 40 минут»
- 50–80 L boiler fully cold may need 1–2 hours, not always 40 minutes
- Could be flow heater (needs power) or central hot water with seasonal limits in September
- Guest shouldn't discover system type in icy shower — host must describe upfront
- Subtle swap: host prep task becomes guest task — find boiler, switch on, wait, decide if usable
- Same mechanic as «всё для гостей» (wet mat), «кухня есть», prepaid chat silence, rating 4,8 with identical reviews
- Wordstat gap: «квартиры посуточно тюмень» ~5134 vs «в квартире нет горячей воды» ~2589 — people search standing in bathroom
- Ask before payment: «Где бойлер, был ли включён до заезда, сколько ждать?»
- Evasive answer = signal; need system type, ready at check-in, who switches on, if not heated
- Moral: «Сначала проверка. Потом перевод.»
- If already icy shower: fix time, who acts, relocation/partial refund before checkout

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (5134), в квартире нет горячей воды (2589), снять квартиру посуточно в тюмени

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).
Poster cover: early-September Tyumen bathroom / icy shower mood + big hook matching H1 in Cyrillic.
NO logo in generation — factory paste after.
NO host face on cover.

STRICT GATE FORMAT (must PASS excalibur_blog_cover_text_gate.py):
- hook: ONE line, 2-8 words total, Cyrillic only, no newlines
- highlight: exactly ONE word that appears inside hook (will be pink highlight)
- sticky: 1-5 Russian words, NOT phone number
- inline_labels: object with inline_1, inline_2, inline_3 — each value is ARRAY of 2-6 strings, each string 1-4 words
- wordstat_stickers: array of 2-3 Tyumen guest search phrases (no digits required)

Example shape:
{
  "hook": "«Горячая вода есть» — ледяной душ",
  "highlight": "ледяной",
  "sticky": "Сначала проверка — потом перевод",
  "wordstat_stickers": ["квартиры посуточно тюмень", "в квартире нет горячей воды", "снять квартиру посуточно в тюмени"],
  "inline_labels": {
    "inline_1": ["7800–9600 ₽", "поздний заезд", "«всё для душа»", "ледяная струя"],
    "inline_2": ["включите бойлер", "ждать 40 минут", "1–2 часа нагрев", "гость ищет автомат"],
    "inline_3": ["где бойлер", "включён до заезда", "сколько ждать", "до оплаты спросить"]
  }
}
