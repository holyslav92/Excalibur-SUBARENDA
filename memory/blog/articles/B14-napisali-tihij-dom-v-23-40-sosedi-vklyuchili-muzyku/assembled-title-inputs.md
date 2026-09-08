# Assembled title inputs — B14

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor CASE (already happened), NOT how-to, NOT guide
- Two beats: period, em dash, colon, or contrast («Только», «А потом»)
- MUST include figure: ₽ / ночи / минуты / люди (gate FAIL without digit)
- BAN: «что проверить», «как снять», «разберём», HH:MM in H1 (words «ночью»/«утром» OK — NOT 23:40)
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: person booking nightly stay in Tyumen — not host-operator report
- ~40–70 chars in h1
- Tyumen optional in H1 (P0 demand spine is «квартиры посуточно тюмень» — under H1, not SEO tail)
- klyshin_title_shape: 2 — [Утверждение]. [Опровержение/обрыв]
- dzen_pattern: NOT list/how-to

## Scout handoff

- topic_id: B14
- slug: napisali-tihij-dom-v-23-40-sosedi-vklyuchili-muzyku
- klyshin_hook: neighbors_night | «Написали тихий дом. В 23:40 соседи включили музыку» (23:40 ONLY in body/angle — NOT in H1)
- title_draft calibration: two-beat with «тихий дом» promise vs neighbor music through wall
- P0: «квартиры посуточно тюмень» 5220 (55+11176)
- P1: «шум соседей» 240
- angle: guest books two nights (~8 400 ₽), host promises «тихий дом», loud music from next apartment at night; host helps via chat
- anti_dup: B12 = external noise (road/crane, «тихий центр»). B14 = neighbors through wall, «тихий дом»

## Editorial case figures (from research-notes)

- ~8 400 ₽ for two nights (editorial reconstruction)
- two nights stay
- loud music through wall at night (no HH:MM in H1)

## Anti-dup H1 (published)

NOT: B12 «тихий центр» + crane; B08 prepay silence; any duplicate of published titles in published-titles-only.md

## Good calibration shapes (ORIGINAL text only)

- «Написали «тихий дом». Две ночи за 8 400 ₽ — музыка за стеной»
- ««Тихий дом» в чате. Только ночью — бас из соседней» (add ₽/ночи if needed for gate)
- Shape anchor: promise «тихий дом» + neighbor music contrast + money/nights figure

## Output JSON schema

```json
{
  "topic_id": "B14",
  "h1": "...",
  "title": "...",
  "slug": "napisali-tihij-dom-v-23-40-sosedi-vklyuchili-muzyku",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 2,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
```
