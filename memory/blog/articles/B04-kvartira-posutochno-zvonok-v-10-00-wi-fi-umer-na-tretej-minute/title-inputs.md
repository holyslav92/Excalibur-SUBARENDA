# Title inputs B04

topic_id: B04
tenant: Добрый дом (от лица компании), Тюмень, посуточная аренда
season_context: конец августа 2026, командировочный сезон

Read: research-notes.md, published-titles-only.md, .cursor/excalibur-blog-handoff.md

Output ONLY valid title-brief.json (JSON object, no markdown wrapper, no commentary).

## Scout handoff

- Hook: sept_business_trip — Wi-Fi падает на видеосозвоне в 10:00
- Original: «Звонок в 10:00. Заселился в 22:00.»
- dzen_pattern: 3 (страх → инструкция)
- dzen_shape_hint: созвон сорвался → что спросить до оплаты

## Wordstat P0

- «квартиры посуточно тюмень» 5500 (55+11176) / 12325 (225)

## Anti-dup

- B01: код/дверь — SKIP
- B02: залог/скол — SKIP
- Recent WP: розетки, закрывающие, где работать — SKIP those angles
- Fresh: Wi-Fi/speedtest/видеосозвон

## Hard constraints

- Klyshin rhythm, ~50–70 chars, cable pain + consequence
- H1 may be WITHOUT «Тюмень»
- Ban: «5 советов», «7 шагов», «полный гайд», «2026», ЕГРН
- One variant, verdict PASS
- Include: topic_id, h1, title, subject, angle, verdict, pain_scene, wordstat, checks

## Research pain

Видеосозвон в 10:00 рвётся на 3-й минуте; в объявлении «быстрый интернет»; роутер в коридоре.
