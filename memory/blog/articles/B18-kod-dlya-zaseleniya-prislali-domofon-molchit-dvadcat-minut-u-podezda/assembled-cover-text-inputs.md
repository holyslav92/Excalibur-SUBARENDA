# Cover-text inputs B18

Return ONLY valid cover-text.json per cover-text skill. NO BLOCKER.

H1: «Код уже есть. Только в подъезд не попасть — 20 минут с чемоданом»
cover_hook MUST match H1 pain (code for apartment sent, intercom silent, 20 min with suitcase at entrance). May shorten for poster Cyrillic (2–8 words MAX):
  GOOD patterns: «Код есть — подъезд не открылся» (5 words)
  OR: «Код прислали — домофон молчит» (5 words)
  OR: «Двадцать минут у домофона с чемоданом» (5 words)
  OR: «Код от квартиры — дверь подъезда молчит» (6 words)
  DO NOT exceed 8 words in hook
Season: early autumn 2026 Tyumen — light jacket weather — NO winter, NO snow, NO fur coats, NO New Year
Phone in scene on cover: +7 (993) 574-83-22 on tape/magnet/sticker/screen — never post-paste pill
Cover scene: person at intercom panel + large Cyrillic hook; early autumn entrance, NOT winter
inline_count 3 (tenant canon)

Key facts from article.html:
- Guest had 4-digit apartment code in chat before arrival — «бесконтактное заселение, ключница на месте»
- Correct address, correct entrance — pressed intercom 3 times, silence: no click, no voice
- Stood 20 minutes between suitcase and closed door with no way in
- Taxi already left — 600 ₽ ride wasted
- Code opens apartment (second door), NOT entrance (first door) — two independent checkpoints
- Key locker often inside entrance — code useless while locked outside
- Host message «сейчас позвоню в управляющую» — improvisation, not a plan
- Incomplete instructions: address + apartment code only — no entrance code, no intercom method, no backup
- Smart intercom app may fail — need pre-stated backup: entrance code, dial apartment number, meet in person
- Question before payment: how do you open the ENTRANCE if intercom silent?
- 15 minutes without clear answer = already an answer
- Moral: «Заселение начинается у подъезда, не у квартиры» — check entrance first, then pay
- Checklist: how entrance opens, backup if intercom silent, who answers late check-in, key locker inside or outside, entrance number + floor
- Related: empty key locker after code worked (B13), wrong door/address (B01), silence after prepayment (B08)

Wordstat guest queries (Tyumen): квартиры посуточно тюмень (~5220), бесконтактное заселение посуточно

Output ONLY valid JSON for cover/cover-text.json — exact Cyrillic inscriptions for 3 inline frames (inline_1, inline_2, inline_3).
Poster cover: early-autumn Tyumen entrance / intercom silence + big hook matching H1 in Cyrillic.
NO Latin except brand whitelist. Use «интернет» not Wi-Fi.
NO logo in generation — factory paste after.
NO host face on cover.

GATE HARD LIMITS:
- hook: MAX 8 words — highlight must be exact substring of hook
- each inline label: MAX 4 words AND must contain at least one Cyrillic letter (not digits-only «600 ₽»)
  GOOD: «600 рублей такси», «три нажатия», «код от квартиры»
  BAD: «600 ₽» alone (no Cyrillic)
- sticky: optional, max 5 words
