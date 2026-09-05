# Assembled title inputs — B11

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened), NOT how-to
- BAN: «что проверить», «как снять», «разберём», HH:MM in H1 (слова «утром»/«до обеда» OK)
- Number = price of burn: **5 000** (₽ optional in H1 if rhythm needs it)
- Guest pain: deposit return delay — promised «до обеда», then «после уборки», then «завтра»
- ~40–70 chars
- Tyumen optional in H1 (prefer false — city in lead)
- klyshin_title_shape: 1 or 4 (обещание → сдвиг)
- dzen_pattern: 2

## Target H1 (director lock — use unless gate fails)

«Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»»

## Scout handoff

- topic_id: B11
- slug: zalog-5-000-obeschali-vernut-utrom-utrom-napisali-posle-uborki
- klyshin_hook: deposit_cleaning_delay
- original: «Залог обещали вернуть утром. Утром — «после уборки».»
- P0 spine: «залог посуточно» — 3267 RU / 40 Tyumen
- buyer spine: «квартиры посуточно тюмень» — 5261 Tyumen
- angle: timing slip «утром → после уборки → завтра», NOT B02 damage dispute (скол на плите)

## Anti-dup H1 (published)

B01 code wrong door, B02 deposit/chip NOT return timing, B03 walk, B04 third guest, B05 rating, B06 checkout bags, B07 kitchen, B08 prepay silence, B09 parking, B10 all-inclusive taxi

## Research spine (from research-notes.md)

- 5 000 ₽ залог, обещание «до обеда на карту»
- 11:40 «после уборки», 12:30 «уборка не прошла», 18:00 «завтра»
- Conflict = срок без дедлайна, not «не вернули из-за скола»

## Output JSON schema

```json
{
  "topic_id": "B11",
  "h1": "Залог 5 000 обещали вернуть утром. Утром написали: «после уборки»",
  "title": "Залог посуточно: обещали утром — написали «после уборки»",
  "subject": "срок возврата залога после выезда из квартиры посуточно",
  "angle": "deposit_cleaning_delay — обещанный срок сменили на формулировку без времени",
  "klyshin_title_shape": 1,
  "verdict": "PASS"
}
```
