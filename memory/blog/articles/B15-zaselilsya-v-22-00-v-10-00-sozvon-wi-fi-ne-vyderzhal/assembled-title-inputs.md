# Assembled title inputs — B15

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened), NOT how-to, NOT guide
- Two beats: period, em dash, colon, or contrast («Только», «А потом»)
- MUST include figure: ₽ / ночи / минуты / люди (gate FAIL without digit)
- BAN: «что проверить», «как снять», «разберём», HH:MM in H1 (words «утром»/«ночью»/«после рейса» OK — NOT 22:00 or 10:00)
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: person booking nightly stay in Tyumen on business trip — not host-operator report
- ~40–70 chars in h1
- Tyumen optional in H1 (P0 demand spine is «квартиры посуточно тюмень» — under H1, not SEO tail)
- klyshin_title_shape: 1 or 2 — late check-in vs morning video call Wi-Fi failure
- dzen_pattern: 2 — NOT list/how-to

## Scout handoff

- topic_id: B15
- slug: zaselilsya-v-22-00-v-10-00-sozvon-wi-fi-ne-vyderzhal
- klyshin_hook: sept_business_trip | «Звонок в 10:00. Заселился в 22:00.» (clock ONLY in body/angle — NOT in H1)
- title_draft calibration (NO HH:MM in H1): two-beat late check-in + morning call Wi-Fi failure
- P0: «квартиры посуточно тюмень» 5134 (55+11176)
- angle: engineer/manager, 3 nights ~10 200 ₽, late flight check-in, morning video call fails on 3–5 Mbit Wi-Fi, outlet at bed not desk, closing docs unclear
- anti_dup: B12 noise/crane; B13 keybox; B14 neighbors music — B15 = business trip Wi-Fi/workspace/docs

## Editorial case figures (from research-notes)

- ~10 200 ₽ for three nights (editorial reconstruction, ~3 400 ₽/night)
- three nights stay
- morning video call fails on weak Wi-Fi (no HH:MM in H1)

## Anti-dup H1 (published)

NOT duplicate published titles in published-titles-only.md

## Good calibration shapes (ORIGINAL text only — gate-tested)

- «Три ночи за 10 200 ₽. Утром созвон — Wi‑Fi не выдержал»
- ««Wi‑Fi есть» в объявлении. Три ночи за 10 200 ₽ — утром созвон сорвался»
- Shape anchor: late check-in context + morning call Wi-Fi failure + money/nights figure; NO clock stamps in H1

## Output JSON schema

```json
{
  "topic_id": "B15",
  "h1": "...",
  "title": "...",
  "slug": "zaselilsya-v-22-00-v-10-00-sozvon-wi-fi-ne-vyderzhal",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 1,
  "wordstat_p0": "квартиры посуточно тюмень",
  "generated_via": "excalibur_blog_derouter_opus_chat.py --role title",
  "verdict": "PASS"
}
```
