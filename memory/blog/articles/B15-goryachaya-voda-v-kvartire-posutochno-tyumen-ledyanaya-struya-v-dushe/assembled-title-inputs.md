# Assembled title inputs — B15

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened), NOT how-to, NOT guide
- **Target shape (mandatory, or very close):** «Горячая вода есть». В душе — ледяная струя, ждать полчаса
  - Gate needs a **digit figure** (₽ / минут / ночи) — if «полчаса» fails, use «40 минут» or «30 минут» (host says ~40 min in case) OR add money «за 8 400 ₽» while keeping two beats
- Two beats: period after promise, em dash or comma contrast in second beat
- BAN: «что проверить», «как снять», «разберём», N советов/шагов, HH:MM in H1
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: person booking nightly stay in Tyumen — not host-operator report
- ~40–70 chars in h1
- Tyumen optional in H1 (P0 demand spine «квартиры посуточно тюмень» — under H1, not SEO tail)
- klyshin_title_shape: 2 — [Утверждение]. [Опровержение/обрыв]
- dzen_pattern: NOT list/how-to

## Scout handoff

- topic_id: B15
- slug_hint: napisali-goryachaya-voda-est-v-dushe-ledyanaya-struya
- klyshin_hook: hot_water_boiler | «Горячая вода есть» — в душе ледяная, хозяин: «подождите, бойлер»
- title_draft calibration: «Горячая вода есть». В душе — ледяная струя, ждать полчаса
- P0: «квартиры посуточно тюмень» 5134 (55+11176)
- angle: listing promises hot water; check-in ~21:00; icy shower; host: turn on boiler, wait 40 min; 7800–9600 ₽ for 2–3 nights already paid
- anti_dup: B10 hidden fees/taxi; B13 code/keybox; B14 neighbors/noise — B15 is ONLY water/boiler/GVS promise

## Editorial case figures (from research-notes)

- ~7800–9600 ₽ for 2–3 nights (editorial reconstruction; pick one round sum if needed for gate)
- Host wait instruction: ~40 minutes (or «полчаса» in H1 if digit added elsewhere)
- Check-in around 21:00 — NO HH:MM in H1

## Anti-dup H1 (published)

NOT duplicate any title in published-titles-only.md / shared/published-titles.md

## Good calibration shapes (ORIGINAL text only)

- «Горячая вода есть». В душе — ледяная струя, ждать 40 минут
- ««Горячая вода есть». Три ночи за 8 400 ₽ — ледяной душ»
- Shape anchor: promise «горячая вода есть» + icy shower + wait time or money figure

## Output JSON schema

```json
{
  "topic_id": "B15",
  "h1": "...",
  "title": "...",
  "slug": "napisali-goryachaya-voda-est-v-dushe-ledyanaya-struya",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 2,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
```
