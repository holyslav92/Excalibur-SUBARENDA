# Assembled title inputs — B17

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened), NOT how-to, NOT guide
- Two beats: period, em dash, colon, or contrast («Только», «А потом»)
- MUST include figure: ₽ / ночи / дни / люди (gate FAIL without digit)
- BAN: «что проверить», «как снять», «разберём», «N советов», HH:MM in H1
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: person who checked out clean, waiting for deposit refund on the way to station
- ~40–70 chars in h1
- Tyumen optional in H1 (P0 demand spine is «квартиры посуточно тюмень» — under H1, not SEO tail)
- klyshin_title_shape: 1 or 3 or 5 — promised morning refund → «after cleaning» with no deadline
- dzen_pattern: 2 — case with sum and dialogue rupture

## Scout handoff

- topic_id: B17
- slug: zalog-5-000-obeschali-vernut-utrom
- klyshin_hook: deposit_cleaning_deferral | original: «Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»»
- title_draft calibration: «Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»»
- P0: «квартиры посуточно тюмень» 4 929 (55+11176), 10 527 (225)
- angle: guest checked out on time, apartment clean, keys in lockbox, photos sent; host promised «вернём утром после выезда»; next morning 10:00 message «залог вернём после уборки» — no date, no full sum confirmation, no transfer method
- anti_dup: B02 = deposit withheld for chip on stove (damage dispute); B16 = prepayment refund after cancelled flight; B17 = clean checkout, deposit frozen by vague «after cleaning» — different wound
- case_number: 5 000 ₽; two nights; promised «утром»; tension at station with frozen money

## Editorial case figures (from research-notes)

- 5 000 ₽ deposit (typical range 2 000–5 000 ₽ for daily rent)
- checkout at 12:00, keys in lockbox, clean apartment, photos in chat
- next morning instead of refund: «Залог вернём после уборки» — no calendar date, no full amount, no transfer method
- guest already in taxi to station; money not stolen but inaccessible

## Anti-dup H1 (published)

NOT: B02 «Снял квартиру посуточно. Залог не вернули — нашли скол на плите» (damage deposit)
NOT: B16 «Рейс отменили. 4 200 ₽ обещали вернуть за три дня — срок вышел» (prepay cancel)
NOT: B08 silence, B13 keybox empty, B14 neighbors — see published-titles-only.md

## Good calibration shapes (ORIGINAL text only)

- «Залог 5 000 ₽ обещали вернуть утром. Утром написали: «после уборки»»
- «Перевели залог 5 000. А утром — «вернём после уборки»»
- Shape anchor: promised morning refund + vague deferral without deadline (NOT how-to, NOT «не вернули залог» essay)

## Output JSON schema

```json
{
  "topic_id": "B17",
  "h1": "...",
  "title": "...",
  "slug": "zalog-5-000-obeschali-vernut-utrom",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 1,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
```
