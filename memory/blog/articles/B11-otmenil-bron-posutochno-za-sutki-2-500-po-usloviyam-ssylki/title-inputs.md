# Title inputs B11

topic_id: B11
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026

Read: research-notes.md, published-titles-only.md

**OUTPUT:** Return ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER or refusal. Script saves output.

## Scout / case
- Guest books nightly rental in Tyumen via messenger, transfers **2 500 ₽** prepayment
- Cancels trip **1 day before** check-in (flight change / illness / business trip — do not pick one)
- Host replies with **link to terms**: prepayment not refunded / fully retained
- Conflict: rules were NOT discussed before payment; link appears **after** cancellation
- NOT «host disappeared» (B08) — host answers, cites link
- klyshin_hook / title_draft: **«Отменил за сутки. 2 500 ₽ — „по условиям ссылки“»**
- dzen_pattern: 2 — case with sums and guest-night stop-factor
- lockpick question (for article, not H1): «Какие условия отмены и когда вернут предоплату — до перевода?»

## Research burn numbers
- **2 500 ₽** — editorial case sum only, NOT typical Tyumen prepayment stat
- **1 day / за сутки** before check-in — cancellation timing
- Quote beat for second clause: «пo условиям ссылки» / «не возвращаем»

## Wordstat P0 (demand spine under H1, not raw in H1)
- «квартиры посуточно тюмень» — 11342 (225), 5261 (55+11176)
- «отмена брони посуточно» — 78 (225)
- «вернуть предоплату посуточно» — 81 (225)
- «предоплата квартира посуточно» — 754 (225)

## Anti-dup (published titles)
NOT: B01 code, B02 deposit/skolk, B03 uni walk, B04 third guest, B05 reviews, B06 luggage, B07 kitchen/cafe, B08 **3 000 ₽ silence in chat**, B09 parking, B10 all-inclusive taxi

B08 delta: B08 = money sent, **silence** before keys. B11 = **cancellation**, **link to terms**, 2 500 ₽ retention — different verb, object, beat.

## Hard constraints (PR #52 CASE delivery)
- **Two-beat stop-factor** H1: [normal action]. Then [horror/quote/figure] — already happened guest-night burn
- Shape calibration: «Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»»
- Target close to handoff: **«Отменил за сутки. 2 500 ₽ — „пo условиям ссылки“»** (keep 2 500 ₽; guest POV)
- ~40–70 chars; BAN HH:MM in H1
- BAN: как снять, N советов/шагов, разберём, topic label, полный гайд, лучшие
- «Тюмень» in H1 optional; title field may carry P0 spine for meta
- Fields: topic_id, h1, title, subject, angle, klyshin_title_shape (1-10), verdict: PASS
