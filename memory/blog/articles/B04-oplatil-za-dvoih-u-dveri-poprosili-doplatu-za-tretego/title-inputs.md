# Title inputs B04

topic_id: B04
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: август 2026, late summer

Read: research-notes.md, published-titles-only.md, scout handoff

Output ONLY valid title-brief.json (JSON object, no markdown wrapper).

## Scout / case

- Guest books for 2, pays prepay, arrives with 3 people, host demands extra fee at door
- Original shape: «Оплатил за двоих. У двери попросили доплату за третьего»
- dzen_pattern: 2 (кейс с суммами)
- klyshin_title_shape: prefer 1 or 3 (action → catastrophe / quote → reveal)

## Wordstat P0

- «доплата за гостя» — 272 (225)
- «квартира посуточно тюмень» — 5500 (55+11176) — demand spine under H1

## Anti-dup

Do NOT repeat: B01 wrong code, B02 deposit/chip, B03 parents uni, recent WP: passport, wifi, 10:00/22:00, prepaid occupied, towels, construction, kitchen, reviews, checkout train, hotel vs apt

## Hard constraints

- Two-beat stop-factor CASE H1 (~50–70 chars)
- Ban: как снять, что проверить, N советов/шагов, разберём, topic label
- Number = ₽ or nights, not list count
- verdict: PASS
