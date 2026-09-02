# Title inputs B07

topic_id: B07
tenant: Добрый дом, Тюмень, посуточная аренда (комфорт+)
season_context: 2 сентября 2026; отопление в Тюмени включат не раньше конца сентября; ночью +7…+16

Output ONLY valid title-brief.json (JSON object, no markdown wrapper, no code fences).
Do NOT return DEROUTER TITLE BLOCKER.

## Case (from research-notes.md / scout handoff)

- Гость снял квартиру посуточно в Тюмени в сентябре. Ночью на улице +7, батареи холодные —
  отопление в городе ещё не включили. К утру в комнате +17.
- Попросил обогреватель. Хост у двери: «Есть, 500 ₽ за сутки — электричество».
- Реальная цена ночи обогревателя по тарифу 2026 — 45–65 ₽ (1,5 кВт × 10 ч × 4,29 ₽).
- Рана: либо +500 ₽, либо спать в куртке / в +17.
- klyshin_hook: klyshin_substitution_quote_break | «просили одно — подсунули платную услугу»
- dzen_pattern: 5 (локальный + сезонный), элементы pattern 2 (кейс с суммой)

## OWNER-APPROVED H1 SHAPE (HARD — follow exactly)

Shape: «Сняли квартиру посуточно. [чего хотели]. У двери: +₽ или [рана]».
Owner-approved calibration (live #4, structure only, do not copy words):
«Сняли квартиру посуточно. Хотели дождаться поезда. У двери: +2 100 ₽ или чемоданы в подъезд»

Requirements:
- Word «посуточно» MUST be in h1.
- Three beats: «Сняли квартиру посуточно.» → [wanted X, 2–3 words] → «У двери: +500 ₽ или [wound]».
- Figure = «+500 ₽» (one number only; no other digits except optionally «+17» as the wound temperature).
- Readable on a Dzen card in one breath; tired guest understands without rereading.
- **Length ≤ 85 characters (gate hard limit).** Count carefully.
- BAN: riddle titles, how-to («как снять», «что проверить», «что делать»), «N советов/шагов»,
  HH:MM clock, «под вопросом», topic labels, ЕГРН/ипотека/наследство/Клышин, «Тюмень» optional.
- Spoken Russian at the door, no SEO tail.

Candidate directions (calibration only; craft your own, keep ≤85 chars):
- «Сняли квартиру посуточно. Батареи холодные. У двери: +500 ₽ или спите в +17»
- «Сняли квартиру посуточно. Хотели тепла. У двери: +500 ₽ за обогреватель или куртка»

## Wordstat P0 (demand spine under H1 / title)

- «квартиры посуточно тюмень» — 5363 (55+11176)
- «снять квартиру посуточно в тюмени» — 1696 (55+11176)
- «когда в тюмени включат отопление» — 830 (55+11176), рост 63→285 показов/день 28–31.08

## Anti-dup (published-titles-only.md + live)

Do NOT echo: B01 код от чужой двери; B02 залог/скол; B03 вуз 40 минут; B04 доплата за третьего;
B05 рейтинг 4,8; B06 выезд/поезд/чемоданы; live: горячая вода/душ, ранний заезд, парковка 800,
лапа 3000, паспорт, Wi-Fi, розетка, отель vs квартира, предоплата.

## Fields

`topic_id`, `h1`, `title` (may carry Wordstat spine lightly, e.g. «Квартира посуточно в Тюмени: …»),
`subject` (one line), `angle` (one line), `klyshin_title_shape` (1–10; here 3 or 5),
`manner_canon`: "dobry_dom_gen_only_human_v1", `verdict`: "PASS".
