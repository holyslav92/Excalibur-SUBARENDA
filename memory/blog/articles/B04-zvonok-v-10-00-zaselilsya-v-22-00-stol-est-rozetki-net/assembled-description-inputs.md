# Description inputs B04

topic_id: B04
tenant: Добрый дом (ПКОМПАНИИ), Тюмень, посуточная аренда
author_brand: Добрый дом
season_context: август 2026, командировочный гость, вечерний заезд ~22:00, созвон в 10:00

Read: shared/dzen-description-rules.md (HARD constraints)

Output ONLY valid description-brief.json (JSON object, no markdown wrapper, no commentary).

## Title (H1) — description MUST NOT duplicate or paraphrase closely

«Звонок в 10:00. Заселился в 22:00 — у стола нет розетки»

## Article opening (DO NOT truncate — double card FAIL)

First two paragraphs start with: «Гость зашёл в квартиру в Тюмени в 22:10…» and «В квартире стола не оказалось. Была узкая кухонная столешница…» — description must use DIFFERENT hook wording.

## Article spine (for teaser energy, not spoiler checklist)

- Business traveler arrives ~22:00; video call with client at 10:00 next morning
- Ad promised «рабочий стол, Wi‑Fi, документы для отчёта»
- «Стол» = narrow kitchen counter; nearest outlet behind fridge, cord too short
- Wi‑Fi works in hallway, video breaks in room
- Host answers «чек?» with one word: «Потом»
- Guest re-opens listings at 23:40 with suitcase and morning call looming
- Lockpick questions from article: photo of desk + outlet + chair; 2‑min video call from that chair; «Поезд 23:40, выезд 15:00 — сколько и кто встретит?»
- Check-in windows may contradict «24/7» in same card
- Documents: ООО/ИП/самозанятый/физлицо — ask before payment, not after
- Teaser ≠ full checklist of 5 items; one hook only

## Research / Wordstat angle (background, not SEO paste)

- P0: «квартиры посуточно тюмень» 5534
- Secondary: «командировка квартира» (Tyumen 41)
- Pain: галочки «стол» и «Wi‑Fi» vs реальное рабочее место для видеосвязи
- Market reference «от 1,5 тыс.» — NOT Добрый дом price; do not use price ladder in teaser

## OG / description factory (HARD)

1. NEVER guest-burn price arithmetic (2500→6500, 500₽/hour ladder) as Добрый дом's own price
2. NEVER Святослав Шакин / The Риэлтор / «история Святослава»
3. ≠ title H1 above (no repeat «звонок в 10:00 / заселился в 22:00 / у стола нет розетки» as main hook)
4. ≠ truncated lead (22:10, кухонная столешница, холодильник, 23:40 чемодан…)
5. No label head («Проверка заселения», «Риэлтор Тюмень», «5 советов командировочному»)
6. No full TG/MAX/booking funnel — one hook only
7. Guest pain only — no ЕГРН/наследство/ипотека
8. 1–2 sentences, ~120–220 chars (max 250, min 40)
9. Klyshin rhythm: case hook, разговорная первая реплика, интрига до клика
10. Do NOT put «Добрый дом» inside description text — brand lives in author_brand field only (see B01/B03 teasers)

## Required JSON fields

topic_id, description, rhythm ("klyshin_case_hook"), geo ("Тюмень"), author_brand ("Добрый дом"), not_equal_title (true), not_truncated_lead (true), verdict ("PASS")

## Energy examples (do NOT copy verbatim)

| Title | OK teaser |
|-------|-----------|
| Код есть — из крана льёт холодное | Хост пишет «утром будет». Вы уже в квартире. Где бойлер — спросите до того, как замёрзнете. |
| В чате «можно с собакой» — у двери «не пустим» | «Можно» без породы и доплаты — не ответ. Один вопрос в переписке спасает заселение. |

For B04 energy: «рабочий стол» в карточке vs розетка за холодильником; «Потом» на вопрос про чек; видеосвязь в 10:00 — but NOT repeat H1 time formula as main hook if too close to title.
