# Assembled title inputs — B42

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor guest night: [filter «2-комн» promise]. Then [second door = storeroom / sleep burn]
- Two beats: period or em dash between beats (scene shape — «в фильтре»)
- MUST include figure: **10 800 ₽** (two nights) OR **1 500 ₽** (discount dispute) from research editorial case
- Word **посуточно** in H1 OR ensure body will have it in first sentence (prefer in H1 if natural)
- BAN: «что проверить», «как снять», «разберём», «N советов», HH:MM in H1
- BAN skeleton «Сняли квартиру посуточно. Хотели X. У двери: +₽»
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин phone
- Guest: family of 3, Tyumen short-term, filter «двухкомнатная»
- klyshin_title_shape: **5** (scene — в фильтре)
- dzen_pattern: **2** (case with sums)
- ~40–70 characters target; max 85

## Scout handoff

- topic_id: B42
- slug: posutochno-tyumen-dvuhkomnatnaya-vtoraya-kladovaya
- klyshin_original: «Двухкомнатная в фильтре. Вторая — не спальня.»
- title_draft (anchor — refine, do not blindly paste): «В фильтре — двухкомнатная. Вторая комната — кладовая с коробками»
- P0: двухкомнатная посуточно 3993 (RU225); квартиры посуточно тюмень 3940 (55+11176)
- anti_dup: NOT B25 (two beds on photo); NOT B04 (third guest surcharge at door) as same H1

## JSON schema

Return object with keys: h1, title_seo, slug, topic_id, klyshin_title_shape, dzen_pattern, primary_query, notes
