# Assembled title inputs — B15

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened), NOT how-to, NOT guide
- Two beats: period, em dash, colon, or contrast («Только», «А потом»)
- MUST include figure: ₽ / ночи / минуты / люди (gate FAIL without digit)
- BAN: «что проверить», «как снять», «разберём», HH:MM in H1 (words «ночью»/«утром» OK)
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: person booking nightly stay in Tyumen — not host-operator report
- ~40–70 chars in h1
- Tyumen optional in H1 (P0 demand spine is «квартиры посуточно тюмень» — under H1, not SEO tail)
- klyshin_title_shape: 3 — [Прямая речь/обещание]. [Что вскрылось у двери]
- dzen_pattern: 2 — NOT list/how-to

## Scout handoff

- topic_id: B15
- slug: napisali-bez-zaloga-u-dveri-5000
- klyshin_hook: no_deposit_at_door | «Написали одно — у двери другое» (guest pain, not legal essay)
- title_draft calibration: «Написали «без залога». У двери попросили 5 000 ₽»
- P0: «квартиры посуточно тюмень» 3552 (55+11176)
- P1 guest cluster: «квартира посуточно без залога» 1173 (225)
- angle: filter/card «без залога», nights prepaid ~7–9k ₽, host demands 5 000 ₽ deposit at door «вернём после уборки»
- anti_dup: B02 = deposit not returned after checkout (chip); B04 = surcharge for third guest at door; B05 = «после уборки» on return morning. B15 = «без залога» promise vs first-time 5 000 ₽ at threshold

## Editorial case figures (from research-notes)

- 5 000 ₽ demanded at door (must appear in H1)
- 2–3 nights prepaid (~7–9 000 ₽ — optional in H1 if 5 000 ₽ present)
- scene: suitcase at door, card said no deposit

## Anti-dup H1 (published)

NOT duplicate B04 «доплата за третьего»; NOT B02 «залог не вернули»; NOT B05 «после уборки» return angle; any duplicate of published-titles-only.md

## Good calibration shapes (ORIGINAL text only — scout draft is anchor)

- «Написали «без залога». У двери попросили 5 000 ₽» (preferred two-beat)
- «В карточке — без залога. У двери: переведите 5 000 ₽»
- Shape anchor: promise «без залога» + door demand 5 000 ₽ contrast

## Output JSON schema

```json
{
  "topic_id": "B15",
  "h1": "...",
  "title": "...",
  "slug": "napisali-bez-zaloga-u-dveri-5000",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 3,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
```
