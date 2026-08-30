# Description inputs B04

topic_id: B04
tenant: Добрый дом, Тюмень, посуточная аренда
author_brand: Добрый дом
season_context: август 2026, перед 1 сентября; родитель ищет квартиру на 4 ночи рядом с общежитием

Read: shared/dzen-description-rules.md (HARD constraints)

Output ONLY valid description-brief.json (JSON object, no markdown wrapper, no commentary).

## Title (H1) — description MUST NOT duplicate or paraphrase closely

«Попросили фото паспорта до оплаты — под угрозой бронь и данные»

## Article opening (DO NOT truncate — double card FAIL)

First two paragraphs start with: «28 августа в 22:15 Марина искала квартиру в Тюмени…» and «Вы сидите на кухне с телефоном и узнаёте эту вилку…» — description must use DIFFERENT hook wording.

## Article spine (for teaser energy, not spoiler checklist)

- Host asks for full passport photos + selfie with passport BEFORE payment, address, or host name
- Pressure: «ещё двое смотрят, решайте сейчас» — guest fears losing the only flat near campus
- Fork: refuse → lose booking; send → stranger gets documents + money, no way to verify
- Passport request alone ≠ fraud — but order matters: address, dates, price first; data for contract later
- Red flags: manager in another chat, all pages, selfie without reason, urgent transfer to individual card
- Marina asked for address + call; got «не доверяете?» and ghosting — found same flat in other ads
- Guest pain: бронь vs персональные данные до проверки объекта

## Research / Wordstat angle (background, not SEO paste)

- P0: «паспорт при заселении в квартиру посуточно» 99
- Secondary: «фото паспорта при заселении в квартиру посуточно» 52
- Pain: просьба паспорта до оплаты — норма или развод?

## OG / description factory (HARD)

1. NEVER guest-burn price arithmetic (2500→6500) as Добрый дом's own price
2. NEVER Святослав Шакин / The Риэлтор / «история Святослава»
3. ≠ title H1 above
4. ≠ truncated lead / opening scene (28 августа, Марина, кухня с телефоном…)
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

For B04 energy: «пришлите паспорт и перевод» до адреса / «ещё двое смотрят» — but NOT repeat H1's «под угрозой бронь и данные» as main hook.
