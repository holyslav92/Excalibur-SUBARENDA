# Title inputs B05

topic_id: B05
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: август 2026, конец лета / начало сентября

CRITICAL: Output ONLY valid title-brief.json (single JSON object, no markdown, no refusal).

## Scout / case

- Guest travels with dog, listing says «можно с лапой» / pets allowed
- After check-in host demands 3 000 ₽ surcharge (cleaning/pet fee) not mentioned before payment
- title_draft: «В объявлении — «можно с лапой». После заселения доплата 3 000 ₽»
- dzen_pattern: 2 (кейс с суммами)
- klyshin_title_shape: prefer 3 (quote → reveal) or 1 (action → catastrophe)

## Wordstat P0

- «посуточная квартира с собакой» — 600 (225)
- «аренда квартиры посуточно» — 792 (55+11176) — demand spine

## Anti-dup

Do NOT repeat: B01 code/door, B02 deposit/chip, B03 vuz distance, B04 third guest fee

## Hard constraints

- Two-beat stop-factor CASE H1 (~50–70 chars)
- Ban: как снять, что проверить, N советов/шагов, разберём, topic label
- Number = ₽ (3000), not list count
- slug: razreshili-s-lapoy-doplatu-nazvali-posle-zaseleniya
- verdict: PASS
