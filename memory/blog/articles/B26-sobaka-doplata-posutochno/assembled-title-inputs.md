# Assembled title inputs — B26

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor guest night: [normal]. Then [horror] / quote / number
- Two beats: period, em dash, colon, or contrast («Только», «А потом»)
- MUST include figure: ₽ / ночи / дни / люди (gate FAIL without digit)
- BAN: «что проверить», «как снять», «разберём», «N советов», HH:MM in H1
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: person who booked nights in Tyumen with dog, saw «можно с собакой», hit with breed surcharge at check-in door
- ~40–70 chars in h1
- Tyumen optional in H1 (P0 demand spine is «квартиры посуточно тюмень» — under H1, not SEO tail)
- klyshin_title_shape: 3 — direct speech «можно с собакой» + check-in horror 2 500 ₽
- dzen_pattern: 2 — case with sums

## Scout handoff

- topic_id: B26
- slug: sobaka-doplata-posutochno
- klyshin_hook: dog_breed_fee | original: «Можно с животными» в объявлении — а при заезде доплата за породу/размер
- title_draft calibration: «Можно с собакой» написали. При заезде — 2 500 ₽ за «крупную породу»
- P0: «квартиры посуточно тюмень» 4570 (55+11176), compare RF «посуточно с собакой» 886
- angle: guest booked with dog; card said pet-friendly; at door host demands 2 500 ₽ for «крупная порода» and/or hair deposit
- anti_dup: NOT B24 «можно с детьми» + child fee; NOT B02 deposit checkout; NOT B10 taxi; NOT B23 cleaning
- case_number: 2 500 ₽; «можно с собакой» vs breed surcharge at check-in door

## Editorial case figures (from research-notes)

- editorial composite 2 500 ₽ for «крупная порода» at check-in (NOT Добрый дом tariff)
- promise in card: «можно с собакой» / «можно с животными»
- conflict moment: AT check-in door, before keys — undisclosed breed/size surcharge
- NOT checkout deposit dispute (that's B02)

## Anti-dup H1 (published)

NOT: B24 ««Можно с детьми» в карточке. При заезде: 1 500 ₽ за 2 ночи, 6-летнему» (children, not dog)
NOT: B02 deposit, B10 taxi, B23 cleaning, B13 code/keybox
NOT repeat published titles in published-titles-only.md

## Good calibration shapes (ORIGINAL text only)

- ««Можно с собакой» написали. При заезде — 2 500 ₽ за «крупную породу»»
- ««Можно с животными» в карточке. У двери — 2 500 ₽ за крупную породу»
- Shape anchor: pet-friendly promise + check-in breed surcharge with sum (NOT how-to, NOT legal essay)

## Output JSON schema

```json
{
  "topic_id": "B26",
  "h1": "...",
  "title": "...",
  "slug": "sobaka-doplata-posutochno",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 3,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
```
