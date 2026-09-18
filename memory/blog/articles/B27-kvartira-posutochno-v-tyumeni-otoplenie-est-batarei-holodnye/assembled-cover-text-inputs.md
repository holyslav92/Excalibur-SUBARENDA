# Cover-text inputs B27

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: «Отопление есть»: 2 ночи, +14 °C — ледяные батареи, «УК не включила»

cover_hook MUST echo H1 cable pain (card promises heating → guest finds +14 °C and ice-cold radiators; host says «УК not started yet, tomorrow»). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns:
  - ««Отопление есть» — ледяные батареи» (4 words)
  - «Обещали отопление — +14 в комнате» (5 words)
  - ««Отопление есть» — сорок минут в куртке» (6 words)
  DO NOT exceed 8 words in hook
  highlight must be exact one-word substring of hook

Season: early autumn September 2026 Tyumen — light jacket weather, yellow leaves, cool evening — NOT winter, NO snow, NO fur coats, NO blizzard
Phone in scene on cover: +7 (993) 574-83-22 on tablo/magnet/screen — never post-paste pill
Cover scene: guest in light jacket on sofa touching cold radiator; phone chat «УК завтра»; large Cyrillic hook; September Tyumen mood
inline_count 7 (2 canvases longform)

Key facts from article.html:
- Card: «отопление есть» — guest reads as warm room tonight
- Two nights prepaid 8 400 ₽ (4 200 ₽/night); cool early-autumn evening check-in
- Room +14 °C; guest sat 40 minutes on couch in jacket
- Radiators ice cold like stair railings; touched twice
- Host reply: «УК ещё не включила, завтра должны» — first paid night already running
- No heater, no second blanket, no alternative apartment offered
- «Есть» = pipes in building, not heat on guest dates; season starts after 5 days below +8 °C outdoors
- Tyumen past years ~21–23 Sept start; if cold days not counted — wait ~1–2 Oct
- Norm +18 °C room; at +14 °C below norm — not caprice
- Parallel cases: «горячая вода есть» cold shower; «всё для гостей» one wet mat; «кухня есть» three nights in café; «коммуналка включена» 1 840 ₽ bill
- Host practice: say central heating in building, season not started, heater + warm blanket, evening temp estimate — before payment
- Checklist: heating on your dates?, evening temp number?, heater + second blanket?, plan if cold?, screenshot card, photo thermometer + radiator at check-in, don't accept «tomorrow UК» as only plan
- Moral: «Сначала проверка. Потом перевод.» Guest pays to take off jacket and sleep — not for radiators on wall

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~4724), снять квартиру посуточно в тюмени (~1452)

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 7 inline frames (inline_1 … inline_7).
Poster cover: early-September Tyumen — guest in jacket by cold radiator + large hook in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
Max 1 cat meme across article — prefer people-meme on one inline only.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter
- sticky: optional, max 5 words
- wordstat_stickers: 1–3 guest-query phrases from Wordstat

GATE REWORK (fix these — em dash counts as word):
- inline_1: «2 ночи — 8400 ₽» = 5 words → shorten to 4 max (e.g. «8400 ₽ две ночи»)
- inline_3: «Первая ночь уже идёт» = 5 words → shorten (e.g. «Первая ночь идёт»)
- inline_4: «Есть — трубы в доме» = 5 words → shorten (e.g. «Трубы есть тепла нет»)
- inline_5: «Норма — от +18 °C» and «+14 °C — ниже нормы» = 5 words each → max 4 words each
