# Assembled title inputs — B16

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened), NOT how-to, NOT guide
- Two beats: period, em dash, colon, or contrast («Только», «А потом»)
- MUST include figure: ₽ / ночи / дни / люди (gate FAIL without digit)
- BAN: «что проверить», «как снять», «разберём», «N советов», HH:MM in H1
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: person who cancelled trip before check-in, waiting for prepayment refund
- ~40–70 chars in h1
- Tyumen optional in H1 (P0 demand spine is «квартиры посуточно тюмень» — under H1, not SEO tail)
- klyshin_title_shape: 1 or 4 or 5 — cancel trip + refund deadline passed
- dzen_pattern: 2 — case with sums and dates

## Scout handoff

- topic_id: B16
- slug: otmenili-rejs-predoplatu-vernut
- klyshin_hook: cancel_prepay | original: «Поездку сорвали. Предоплату обещали вернуть — сроки плывут»
- title_draft calibration: «Отменили рейс. 4 200 ₽ обещали вернуть за три дня — срок вышел»
- P0: «квартиры посуточно тюмень» 4 929 (55+11176), 10 527 (225)
- angle: guest cancelled Tyumen trip before check-in due to cancelled flight; 4 200 ₽ prepayment; host replied «вернём после проверки за три дня»; day 4 — no refund yet
- anti_dup: B08 = silence before check-in (host doesn't answer); B16 = host answered, promised deadline, deadline expired — different wound
- case_number: 4 200 ₽; promised 3 days; tension on day 4

## Editorial case figures (from research-notes)

- 4 200 ₽ prepayment for one or two nights
- promised refund «after check, within three days»
- day 4: deadline passed, no transfer or «still checking»
- cancelled flight triggered trip cancellation (background trigger, not aviation law essay)

## Anti-dup H1 (published)

NOT: B08 «Перевели 3 000 ₽ предоплатой. К вечеру — тишина в чате» (silence before keys)
NOT: B02 deposit, B04 third guest, B13 code/keybox, B14 neighbors, B15 workspace
NOT repeat published titles in published-titles-only.md

## Good calibration shapes (ORIGINAL text only)

- «Отменили рейс. Предоплату 4 200 обещали вернуть за три дня — срок вышел»
- «Поездку сорвали. 4 200 ₽ обещали за три дня — на четвёртый тишина»
- Shape anchor: cancelled trip + promised refund sum + expired deadline (NOT how-to)

## Output JSON schema

```json
{
  "topic_id": "B16",
  "h1": "...",
  "title": "...",
  "slug": "otmenili-rejs-predoplatu-vernut",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 1,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
```
