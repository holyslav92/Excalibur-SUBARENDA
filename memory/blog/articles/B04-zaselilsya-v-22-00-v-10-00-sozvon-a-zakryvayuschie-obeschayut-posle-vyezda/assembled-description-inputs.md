# Description inputs B04

topic_id: B04
tenant: Добрый дом (ПКОМПАНИИ), Тюмень, посуточная аренда
author_brand: Добрый дом
season_context: август 2026, командировка на 2 ночи, поздний заезд ~22:00, видеосозвон в 10:00

Read: shared/dzen-description-rules.md (HARD constraints)

Output ONLY valid description-brief.json (JSON object, no markdown wrapper, no commentary).

## Title (H1) — description MUST NOT duplicate or paraphrase closely

Заселился в 22:00. В 10:00 созвон — закрывающие обещают после выезда

## Article opening (DO NOT truncate — double card FAIL)

First two paragraphs start with: «29 августа, 22:10, Тюмень. Инженер выходит из такси…» and «Он и не переживал. Выехал 31 августа… чек на десятый день… 4 200 ₽» — description must use DIFFERENT hook wording. Do NOT repeat «29 августа», «инженер», «такси», «барная стойка», «4200» or price ladder.

## Article spine (for teaser energy, not spoiler checklist)

- Command trip 2 nights, mandatory video call at 10:00 next morning
- Late check-in ~22:00 leaves ~40 minutes to verify apartment before sleep
- No proper desk — bar counter and stool; Wi‑Fi OK in hallway, drops in quiet back room
- Host reply: «Всё сделаем после выезда, не переживайте» re closing docs (receipt, act)
- Advance expense report due within 3 business days after return — receipt arrived day 10
- Lockpick questions: desk + Wi‑Fi speed at laptop spot; landlord status (self-employed vs IP); when exactly closing docs issued
- NOT rozetka angle (already in WP); NOT duplicate B01/B02/B03 angles
- Rule: стол, скорость, пакет закрывающих — потом деньги и ключ

## Research / Wordstat angle (background, not SEO paste)

- P0: «квартиры посуточно тюмень» 5523
- Pain: «документы после выезда» vs 3-day advance report deadline
- «Есть Wi‑Fi» ≠ speed at work spot

## OG / description factory (HARD)

1. NEVER guest-burn price arithmetic (2500→6500, 4200→personal money ladder) as Добрый дом's own price
2. NEVER Святослав Шакин / The Риэлтор / «история Святослава»
3. ≠ title H1 above
4. ≠ truncated lead / opening scene (29 августа, инженер, такси, чек на десятый…)
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

For B04 energy: «после выезда» vs три рабочих дня на авансовый отчёт; или «есть Wi‑Fi» vs скорость у стола — but NOT repeat H1's «22:00 / 10:00 созвон» as main hook if too close to title.
