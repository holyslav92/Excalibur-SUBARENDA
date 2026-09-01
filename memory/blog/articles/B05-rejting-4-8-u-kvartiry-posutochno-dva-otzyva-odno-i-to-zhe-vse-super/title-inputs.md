# Title inputs B05

topic_id: B05
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026

Read: research-notes.md, published-titles-only.md, scout handoff (memory/scout/.cursor/excalibur-blog-handoff.md)

Output ONLY valid title-brief.json (JSON object, no markdown wrapper). Do NOT return DEROUTER TITLE BLOCKER.

## Scout / case

- Guest in Tyumen sees apartment ~3 900 ₽/night with rating 4,8; two fresh reviews say identical «всё супер» with no detail
- klyshin_hook: reviews_not_rating | original: «4.8 — и два одинаковых „всё супер“»
- title_draft calibration: **Рейтинг 4,8. Два «всё супер» — и ночь за 3 900 ₽ уже не кажется удачной**
- dzen_pattern: 2 (кейс с суммами)
- klyshin_title_shape: prefer 2 (assertion + contrast) or 5 (цифра = цена ожога)
- angle: не звёзды — повторы, свежесть, конкретика в отзывах Avito/Sutochno глазами гостя до предоплаты

## Wordstat P0

- «квартиры посуточно тюмень» — 5463 (55+11176) — demand spine under H1
- «суточно отзывы» — 5880 (225) — national review-intent
- «авито квартиры посуточно тюмень» — 335 (55+11176)

## Anti-dup (published-titles-only.md)

Do NOT repeat: B01 wrong door code, B02 deposit/chip, B03 uni 40 min walk, B04 extra guest fee at door

## Hard constraints

- Two-beat stop-factor guest-night CASE H1 (~50–70 chars)
- Example shape: «Рейтинг 4,8. Два «всё супер» — и ночь за 3 900 ₽ уже не кажется удачной»
- NOT how-to, NOT guide, NOT «как снять», NOT «N советов»
- Ban: как снять, что проверить, N советов/шагов, разберём, topic label, ЕГРН, ипотека, Клышин
- Number = ₽ / rating / nights — not list count
- «Тюмень» in H1 optional
- verdict: PASS
