# Title inputs B03

topic_id: B03
slug: pervaya-noch-posutochno-holodnaya-voda-boyler-tyumen
article_dir: memory/blog/articles/B03-zaselilsya-posutochno-v-dushe-ledyanaya-voda-a-bojler-molchit

## HARD (PR#52 case-delivery gate @ stage title)

- H1 = **two-beat guest night CASE**: [normal setup]. Then [horror turn] — NOT guide/how-to/N steps/listicle.
- **Two-beat break** required: period + second clause, or em dash, or contrast («Только», «А потом»).
- **Figure in H1** required (gate): digit + ₽/руб, OR «N минут/ноч/час», OR 3+ digit number, OR «двух/трёх» people/nights.
- ~40–70 chars (max 85). Strong verb. Klyshin cable rhythm — **your text**, not @klyshin_A copy.
- **No** clock HH:MM in H1. No «как снять», «что проверить», «5 вопросов», «полный гайд», «2026», SEO tail, label head («О горячей воде…»).
- Tyumen in H1 optional. Do not duplicate B01/B02 scenes.

## Scout handoff (angle)

- hook_id: guest_boiler_hot_water_first_night
- original Klyshin: «первая ночь посуточно — в душе ледяная вода, бойлер не прогрелся»
- dzen_pattern: 2 (case with realistic figure from research — e.g. «40 минут» promise vs cold shower)
- title_draft direction (improve, add figure): «Заселился посуточно. В душе — ледяная вода, а бойлер молчит»

## Wordstat P0 (demand spine under H1, not raw in title)

- P0: «квартиры посуточно тюмень» — 4209 (regions 55+11176); RU 225 — 9221
- P1: «снять квартиру посуточно в тюмени» — 1191

## Anti-dup published H1

- B01: «Оплатил квартиру посуточно. Код прислали от чужой двери»
- B02: «Снял квартиру посуточно. Залог не вернули — нашли скол на плите»

## Research spine (facts for rejected_variants / h2_candidates only)

- First night, cold shower, boiler off or not heated; card says «душ/горячая вода»
- 50L boiler full heat ~90–120 min, not universal «40 minutes»
- Questions before payment; save chat promises

Read full: research-notes.md in this directory.

## Output

Return **ONLY** valid JSON object `title-brief.json` (no markdown fence).

Required fields: topic_id, h1, title (same as h1), subject, angle, verdict PASS, char_count, generated_via, pain_scene, wordstat, supply_vs_demand, checks, h2_candidates (5–7), stickers, rejected_variants (3+), notes.

Match richness of B02 title-brief.json structure in sibling article dir B02-perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem.
