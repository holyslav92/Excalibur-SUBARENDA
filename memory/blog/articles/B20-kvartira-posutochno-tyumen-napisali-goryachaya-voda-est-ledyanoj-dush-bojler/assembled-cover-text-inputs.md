# Cover-text inputs B20

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: Написали «горячая вода есть». Ночью — ледяной душ и 80 минут до тепла

cover_hook MUST match H1 **two-beat** structure (promise in card → cold shower + long wait). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns (two-beat):
  - «Горячая вода есть» — ледяной душ» (5 words)
  - «Написали есть» — ледяной душ» (4 words)
  - «Вода есть» — восемьдесят минут» (4 words)
  - «Обещали горячую — ледяной душ» (4 words)
  - «Горячая есть» — ждать час» (4 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: September 2026 Tyumen — late summer/early autumn, light jacket — NO winter hero, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: bathroom/shower + boiler indicator + large Cyrillic two-beat hook; September apartment mood, NOT winter
inline_count 7 (poster + 7 inline panels)

Key facts from article.html:
- Card said «горячая вода есть» — guest arrived late September evening with two bags in hallway
- First thing: shower — ice cold, not «slightly warm», truly icy
- 5 200 ₽ for two nights paid
- Wrote host: «Горячая же есть? Почему ледяная?» — reply «Сейчас нагревается, подождите»
- Waited 20 min — cold; 40 min — still cold
- 50-liter tank fully cooled needs 80+ minutes to heat (1.5–2 kW element)
- «есть» in listing = system installed, NOT temperature at tap in first 5 minutes
- Previous guests' showers can drain the tank before you arrive
- Blinking boiler indicator — may mean heating OR error (NTC, scale, board) — no universal decode
- Don't open/repair boiler yourself — photo indicator, message admin with timestamp
- Night chat exists for this — don't silently twist knobs
- Checklist: ask tank volume, is it on, when last shower BEFORE payment
- At check-in: open hot tap 30 seconds BEFORE unpacking bags
- Cold water → photo blinking light + write admin immediately
- Don't sleep thinking «sort it in morning» — lose evidence and leverage
- Moral: «Сначала проверка. Потом перевод.»
- Related siblings: B11 mokryj kovrik (card vs reality), B19 ne kurili zapah, B08 tishina v chate, B17 kommunalka schet

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4826), снять квартиру посуточно в тюмени

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 7 inline frames (inline_1 … inline_7).
Poster cover: September Tyumen bathroom — icy shower + boiler blink + big two-beat hook in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «5 200 ₽»)
  GOOD: «пять тысяч двести», «восемьдесят минут», «мигает индикатор»
  BAD: «5 200 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat
