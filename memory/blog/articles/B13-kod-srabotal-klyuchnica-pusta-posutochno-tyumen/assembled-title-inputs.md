# Assembled title inputs — B13

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened at the door), NOT how-to, NOT guide
- Two beats: period, em dash, colon, or contrast («Только», «А потом»)
- MUST include figure: ₽ / ночи / минуты / люди (gate FAIL without digit)
- BAN: «что проверить», «как снять», «разберём», HH:MM in H1 (words «ночью»/«утром» OK)
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: person booking nightly stay in Tyumen — not host-operator report
- ~40–70 chars in h1
- Tyumen optional in H1 (P0 demand spine is «квартиры посуточно тюмень» — under H1, not SEO tail)
- dzen_pattern: 2 — [Утверждение]. [Опровержение/обрыв]
- klyshin_title_shape: 2

## Scout handoff

- topic_id: B13
- slug: kod-srabotal-klyuchnica-pusta-posutochno-tyumen
- klyshin_hook: parking_keybox | «Код открыл ключницу — ключа внутри нет»
- title_draft calibration: «Код сработал. Открыли ключницу — внутри пусто»
- P0: «квартиры посуточно тюмень» 5220 (55+11176) / 11084 (225)
- P1: «бесконтактное заселение посуточно» 59
- angle: гость у подъезда ~23:40, код открыл ящик, ключа нет, такси уехало
- lockpick: «Есть фото ключницы и тест кода до оплаты?»
- anti_dup: B01 wrong door code; WP no-code-at-night — here code WORKS but box EMPTY

## Editorial case figures (from research-notes, editorial reconstruction)

- ~35 minutes waiting at door
- ~480 ₽ second taxi (optional in H1 if fits length)

## Anti-dup H1 (published)

NOT: B01 wrong door code, B02 deposit, B03 walk distance, B04 third guest, B05 rating, B06 checkout, B07 kitchen cafe, B08 prepay silence, B09 parking, B10 included taxi, B11 towels, B12 quiet center crane

## Good calibration shapes (ORIGINAL text only)

- «Код сработал. Пустая ключница — 35 минут у двери»
- «Код открыл ящик. Внутри пусто — второе такси 480 ₽»
- Shape anchor: «Код сработал. Открыли ключницу — внутри пусто» + add figure for gate

## Output JSON schema

```json
{
  "topic_id": "B13",
  "h1": "...",
  "title": "...",
  "slug": "kod-srabotal-klyuchnica-pusta-posutochno-tyumen",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 2,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
```
