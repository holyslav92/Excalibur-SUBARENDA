# Description inputs B03

topic_id: B03
tenant: Добрый дом (ПКОМПАНИИ), Тюмень, посуточная аренда
author_brand: Добрый дом
season_context: август 2026, бронь перед 1 сентября; родители с будущим студентом на 2–4 ночи

Read: shared/dzen-description-rules.md (HARD constraints)

Output ONLY valid description-brief.json (JSON object, no markdown wrapper, no commentary).

## Title (H1) — description MUST NOT duplicate or paraphrase closely

«Привезли сына к вузу — «рядом» оказалось 40 минут пешком»

## Article opening (DO NOT truncate — double card FAIL)

First two paragraphs start with: «27 августа, 19:20, Тюмень. Отец держит чемодан…» and «Мать сказала: «Так тут же написано — рядом с университетом»…» — description must use DIFFERENT hook wording.

## Article spine (for teaser energy, not spoiler checklist)

- Parents book 2–4 nights before Sept 1; ad says «рядом с вузом»
- Son needs a specific campus building tomorrow at 9:00; map shows 40 min walk one way
- «Рядом с вузом» can mean district, bus stop, or one Tyumen State Univ building — not the one child needs
- Host may honestly say «три остановки» — that's transit, not walking distance
- Lockpick question from article: «Сколько минут пешком до корпуса на такой-то улице?»
- Tyumen State Univ has many addresses (Volodarskogo, Lenina, Semakova, etc.)
- End-of-August urgency: «решать сегодня» before payment — but teaser ≠ full CTA funnel

## Research / Wordstat angle (background, not SEO paste)

- P0: «квартиры посуточно тюмень» 5534
- Pain: «рядом с вузом» vs конкретный корпус на карте пешком
- «Три остановки» ≠ пешая доступность

## OG / description factory (HARD)

1. NEVER guest-burn price arithmetic (2500→6500) as Добрый дом's own price
2. NEVER Святослав Шакин / The Риэлтор / «история Святослава»
3. ≠ title H1 above
4. ≠ truncated lead / opening scene (27 августа, чемодан, мать сказала…)
5. No label head («Проверка заселения», «Риэлтор Тюмень»)
6. No full TG/MAX/booking funnel — one hook only
7. Guest pain only — no ЕГРН/наследство/ипотека
8. 1–2 sentences, ~120–220 chars (max 250, min 40)
9. Klyshin rhythm: case hook, разговорная первая реплика, интрига до клика

## Required JSON fields

topic_id, description, rhythm ("klyshin_case_hook"), geo ("Тюмень"), author_brand ("Добрый дом"), not_equal_title (true), not_truncated_lead (true), verdict ("PASS")

## Energy examples (do NOT copy verbatim)

| Title | OK teaser |
|-------|-----------|
| Код есть — из крана льёт холодное | Хост пишет «утром будет». Вы уже в квартире. Где бойлер — спросите до того, как замёрзнете. |
| В чате «можно с собакой» — у двери «не пустим» | «Можно» без породы и доплаты — не ответ. Один вопрос в переписке спасает заселение. |

For B03 energy: «три остановки» / «рядом с вузом» vs пеший маршрут до корпуса — but NOT repeat H1's «40 минут пешком» as main hook if too close to title.
