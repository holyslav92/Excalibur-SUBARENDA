# Cover-text inputs — B07

Output ONLY valid JSON object for cover/cover-text.json (no markdown fences). Do NOT return DEROUTER COVER-TEXT BLOCKER.

## Article

H1: Сняли квартиру посуточно. Хотели тепла. У двери: +500 ₽ или спать в куртке
H2 (in order): 1) «Почему батареи холодные, когда ночью +7» 2) «500 ₽ «за электричество» — считаем» 3) «Где гость отдал ключ от ситуации» 4) «Мой вывод как практика»
Case: сентябрь, Тюмень, отопления ещё нет, ночью +7, в комнате +17; хост у двери держит обогреватель: «500 ₽ за сутки — электричество»; реальная ночь обогревателя ≈64 ₽ (1,5 кВт × 10 ч × 4,29 ₽); выбор: доплата или спать в куртке.

## Cover canon for THIS article (owner, HARD)

Cover = WOW graffiti: the H1 spray-painted on a REAL wall in the photo (stairwell/landing wall next to an apartment door), huge readable Cyrillic street-art lettering, three lines = the three beats of the H1 EXACTLY (no rewording):
- cover_headline_line1: "Сняли квартиру посуточно."
- cover_headline_line2: "Хотели тепла."
- cover_headline_line3: "У двери: +500 ₽ или спать в куртке"
- cover_headline_medium: one English sentence for the image model describing the medium — spray-paint graffiti / street-art lettering painted directly on the real painted stairwell wall (two-tone Soviet-style panel-house landing: pale top, green/blue bottom), bold black + one accent colour (red for «+500 ₽»), slight drips, huge and readable at thumbnail; no tent card, no paper, no Canva pill, no stickers.
- No phone, no logo, no meme on cover (factory pastes logo later).

## Fields (gate rules)

- "hook": 2–8 Russian words, the cover thought in plain words (e.g. «Тепло за 500 ₽ у двери» — write your own), Cyrillic only.
- "highlight": exactly one word from hook.
- "sticky": "" (empty — no stickers in gen_only canon).
- "wordstat_stickers": ["когда в тюмени включат отопление", "снять квартиру посуточно в тюмени"] (for inline panels only).
- "inline_labels": for inline_1, inline_2, inline_3 — 2–4 short Russian labels each (1–4 words), matching H2 1–3 (батареи/норматив +8 °C/23 сентября; 500 ₽ vs 64 ₽/тариф 4,29; чат до перевода/вопрос про тепло). Cyrillic only; digits and ₽ allowed.
- Also include "cover_headline_line1", "cover_headline_line2", "cover_headline_line3", "cover_headline_medium" exactly as specified above (medium in English).
