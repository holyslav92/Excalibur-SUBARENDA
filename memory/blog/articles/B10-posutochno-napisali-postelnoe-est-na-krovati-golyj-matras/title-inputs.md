# Title inputs B10

topic_id: B10
tenant: Добрый дом, Тюмень, посуточная аренда
season_context: сентябрь 2026, ранняя осень, вечерний заезд после дороги

Read: research-notes.md, published-titles-only.md, .cursor/excalibur-blog-handoff.md

**OUTPUT:** Return ONLY valid title-brief.json (JSON object, no markdown wrapper, no commentary). Do NOT return DEROUTER TITLE BLOCKER or refusal. Script saves output.

## Scout / case

- Guest books apartment; listing says «постельное бельё и полотенца есть» — arrives to bare mattress, one set for several people, or host says «найдём позже»
- klyshin_hook: pack_vs_flat | original: «Собрал чемодан — в квартире нет полотенец»
- title_draft shape (MUST keep «голый матрас» + gate figure): **«Написали „постельное есть“. На кровати — голый матрас, нас троих»** OR add ₽/minutes to same shape
- Preferred h1 (passes gate): **Написали «постельное есть». На кровати — голый матрас, нас троих**
- dzen_pattern: 2 — кейс с суммами и датами
- dzen_shape_hint: «В объявлении — „постельное есть“. На кровати — [факт]» + цифра: ₽ срочной покупки, допкомплект 500 ₽, ожидание 90 минут, или «нас троих/четверо»
- klyshin_title_shape: prefer 1 (обыденное → катастрофа) or 3 (прямая речь → что вскрылось)
- angle: pack_vs_flat — «есть» ≠ число комплектов на каждого гостя; NOT parking (B09), prepay (B08), kitchen (B07), keys (B01), deposit (B02)
- lockpick: «Сколько комплектов постельного и полотенец — на каждого гостя?»
- moral: сначала число комплектов, потом деньги и ключ

## Research burn numbers

- Срочный комплект белья: ~2 200–3 800 ₽ (рыночный диапазон, не точная цена Тюмени)
- Допкомплект в карточке «Суточный Рай»: 500 ₽
- Ожидание хоста: 40–90 минут (редакционный якорь)
- Гости: пара или семья 3–4 человека; один комплект на нескольких

## Wordstat P0

- «квартиры посуточно тюмень» — 11765 (225) / 5320 (55+11176) — demand spine under title/meta, not raw SEO in H1
- «постельное белье посуточно» — 282 (225)
- «постельное белье в посуточную квартиру» — 78 (225)

## Anti-dup (published-titles-only.md)

Do NOT repeat: B01 code/wrong door, B02 deposit/chip, B03 uni 40 min, B04 third guest fee, B05 rating 4,8, B06 checkout/luggage, B07 kitchen/café 7200, B08 prepay silence 3000, B09 parking 600

## Hard constraints (gate will BLOCK otherwise)

- Two-beat stop-factor guest-night CASE H1 (~40–70 chars) — already happened burn, NOT how-to
- Shape: [normal promise]. Then [horror] / quote / number — example «Написали „постельное есть“. На кровати — голый матрас»
- **Gate requires figure in H1:** ₽ OR nights OR minutes OR «двоих/троих» — bare matress alone FAILS gate
- BAN how-to, N советов/шагов, разберём, topic label, HH:MM in H1
- Ban: как снять, что проверить, лучшие, ЕГРН, ипотека, Клышin, риэлтор
- «Тюмень» in H1 optional; title/meta may carry Wordstat spine lightly
- Fields: topic_id, h1, title, subject, angle, klyshin_title_shape (1-10), verdict: PASS
