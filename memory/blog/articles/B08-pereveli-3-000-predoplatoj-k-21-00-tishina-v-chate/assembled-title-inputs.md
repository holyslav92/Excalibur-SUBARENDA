# Assembled title inputs — B08

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened), NOT how-to
- BAN: «что проверить», «как снять», «разберём», HH:MM in H1 (use «к 21:00» OK? Title skill bans HH:MM — use «к вечеру» or «к девяти вечера» instead)
- Number = price of burn (3 000 ₽, +2 000 ₽)
- Guest pain: predoplata before keys, silence in chat
- ~40–70 chars
- Tyumen optional in H1
- dzen_pattern: 2

## Scout handoff

- P0: квартиры посуточно тюмень (3722/11916)
- angle: prepayment_before_keys
- shape hint: «Перевели 3 000 ₽. К 21:00 — тишина в чате» → fix HH:MM ban → «Перевели 3 000 ₽ предоплатой. К вечеру — тишина в чате» or similar two-beat

## Anti-dup H1

NOT: B01 code wrong door, B02 deposit plate, B04 third guest, B05 rating, B06 checkout, B07 kitchen

## Good calibration shapes (original text)

- «Перевели 3 000 ₽ «за бронь». К девяти вечера — тишина в чате»
- «Скинули предоплату на карту. Код так и не прислали — такси уже уехало»

## Output JSON schema

```json
{
  "topic_id": "B08",
  "h1": "...",
  "title_tag": "...",
  "meta_description": "...",
  "slug": "pereveli-3-000-predoplatoj-k-21-00-tishina-v-chate",
  "dzen_pattern": 2,
  "wordstat_p0": "квартиры посуточно тюмень",
  "two_beat_check": true
}
```
