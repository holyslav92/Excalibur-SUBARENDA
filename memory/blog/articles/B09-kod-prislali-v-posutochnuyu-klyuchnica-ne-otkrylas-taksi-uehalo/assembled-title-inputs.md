# Assembled title inputs — B09

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened), NOT how-to
- BAN: «что проверить», «как снять», «разберём», «N советов», HH:MM in H1
- Number = price of burn (такси 480 ₽, отель 3 200 ₽) or minutes waiting
- Guest pain: keybox panel dead, code received but lock won't open
- ~40–75 chars
- Tyumen optional in H1
- dzen_pattern: 2
- Must include core focus marker: посуточн/квартир/заселен/ключниц

## Scout handoff

- P0: квартиры посуточно тюмень (5320/11765)
- angle: keybox_frozen_panel
- shape hint: «Код прислали. Ключница не открылась. Такси уже уехало» — **MUST include figure in H1**: 480 ₽ такси / 35 минут / 5 попыток

## Anti-dup H1

NOT: B01 wrong door code, B02 deposit, B08 prepay silence, B06 checkout, B07 kitchen

## Required H1 (use exactly or very close)

**«Код прислали. 35 минут у двери — такси 480 ₽»**

Must contain digit + ₽ or minutes. Two-beat: нормально → ужас.

## Output JSON schema

```json
{
  "topic_id": "B09",
  "h1": "...",
  "title_tag": "...",
  "meta_description": "...",
  "slug": "kod-prislali-v-posutochnuyu-klyuchnica-ne-otkrylas-taksi-uehalo",
  "dzen_pattern": 2,
  "wordstat_p0": "квартиры посуточно тюмень",
  "two_beat_check": true
}
```
