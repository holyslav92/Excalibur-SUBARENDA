# Assembled research inputs — B21 (conductor → Derouter research)

**Return ONLY research-notes markdown in response; do NOT return DEROUTER RESEARCH BLOCKER.**

Ты — Derouter utility tier (gpt-5.6-terra). Live fetch, Wordstat MCP-KV, SERP and URL checks уже выполнены conductor 2026-09-14. Используй факты ниже как есть; синтезируй полный research-notes.md. Скрипт запишет файл.

## Meta
- topic_id: B21
- research_date: 2026-09-14
- timezone: Asia/Yekaterinburg
- tenant: Добрый дом, посуточная аренда Тюмень
- format: guest CASE (early check-in paid, apartment not ready until 14:00 cleaning)
- angle_guard: early check-in / cleaning readiness / key handover time — NOT burn-at-door/domofon, NOT boiler/hot water, NOT smoking/smell, NOT kommunalka, NOT deposit refund, NOT legal dispute

## Scout handoff (2026-09-14)
- klyshin_hook: early_checkin | «Ранний заезд обещали. Ключи — только после уборки.»
- final P0: «квартиры посуточно тюмень» 4826 (55+11176), 10308 (225)
- supporting: «квартиры посуточно ранний заезд» 197 RU / 5 Tyumen+oblast
- case numbers (scenario, not market stats): 1 500 ₽ early fee, 890 ₽ forced cafe/taxi, 9:10 arrival, 14:00 cleaning, 4h50m wait, 2 nights
- lockpick_question: «Во сколько квартира реально свободна после предыдущих гостей и что входит в ранний заезд: уборка, смена белья и ключ — или только обещание принять оплату?»
- signal_urls: https://t.me/klyshin_A, https://добрыйдом-72.рф/blog/, https://t.me/Dobriy_dom_72

## Overlap check (published-titles-only.md)
- B06 covers late checkout / luggage at door (different angle)
- B18 burn-at-door/domofon — skip
- B19 smell/smoking — skip
- B20 boiler/hot water — skip
- B21 is NEW angle: paid early check-in vs actual apartment readiness after cleaning

## Wordstat live (2026-09-14, MCP-KV)
| phrase | region | volume |
|---|---|---:|
| квартиры посуточно тюмень | 55+11176 | 4826 |
| снять квартиру посуточно в тюмени | 55+11176 | 1501 |
| аренда квартиры тюмень посуточно | 55+11176 | 169 |
| квартиры посуточно ранний заезд | 225 | 197 |
| снять квартиру посуточно с ранним заездом | 225 | 81 |
| ранний заезд посуточно | 225 | 273 (parent; top child = квартиры посуточно ранний заезд 197) |

## Fresh signals this week (2026-09-08 — 2026-09-14)

### 1) Scout external_signal + Klyshin CASE mechanic — 2026-09-14
- Source: handoff + https://t.me/klyshin_A
- Mechanic: promise in chat → specific surcharge → morning arrival with luggage → refusal to honor agreed time → cost of waiting → short question before payment
- Original hook: «Ранний заезд обещали. Ключи — только после уборки.»

### 2) Restfor.ru guest guide — published/updated 10.09.2026
- URL: https://restfor.ru/kak-snyat-kvartiru-posutochno/
- Key facts:
  - Table «Что уточнить»: row «Ранний заезд и поздний выезд» → need «Подтверждённое время и стоимость»
  - «Посуточная аренда не обязательно означает 24 часа с момента вашего появления. Ориентируйтесь на часы заезда и выезда в подтверждении брони.»
  - Example: mandatory cleaning fee 1 500 ₽ added to total (illustrative calculation, not market price)
  - Direct booking: fix in writing before transfer — dates, check-in/out time, price, deposit
  - Sutochno.ru payment rules verified by author 10.09.2026 (context only)

### 3) Tutu.ru travel journal — real support case (accessed 2026-09-14)
- URL: https://www.tutu.ru/geo/journal/polezno-passazhiru/article/rannij-zaezd-i-pozdnij-vyezd/
- Standard check-in often 14:00, checkout 12:00
- Cleaning window between turnovers often 12:00–14:00; in hotels max 3 hours per RF hotel rules
- Real case: guest booked apartment with remote check-in, requested early check-in 3h earlier (11:00 not 14:00). Host didn't send instructions; guest came early, stood at door until ~14:00. Apartment not cleaned; dirty dishes and used bedding; maid also late 30 min
- Early/late check-in must be agreed in advance; host not obliged to confirm
- If agreed, get written confirmation and fee before arrival to avoid surprises

### 4) Sutochno.ru journal — 20.08.2025 (platform rules, accessed 2026-09-14)
- URL: https://sutochno.ru/sj/ranniy-zaezd-i-pozdniy-vyezd
- Industry standard: check-in ~14:00, checkout ~12:00
- Reasons hosts resist: turnover economics, scheduled cleaning staff
- Host can: allow on request, charge extra (up to full day), or forbid
- If early check-in allowed, can pay on platform or after host approval
- Verbal agreement before prepayment is weak; obligations after prepayment only
- Host can change booking terms in platform after guest agrees
- Free early check-in possible if apartment empty previous night
- Realistic: 3am unlikely free; couple hours deviation often OK for long stays

### 5) RentTools.io host guide — 05.06.2026 (accessed 2026-09-14)
- URL: https://renttools.io/ru/blog/early-check-in-fee-math
- Early check-in = two products: «already ready» vs «rush cleaning on turnover day»
- Deciding question for host: was anyone in apartment previous night?
- Previous night empty → apartment already clean → early check-in low/no cost
- Same-day turnover → cleaning not done → early check-in means dirty apartment OR rushed cleaning
- Standard turnover window 11:00 checkout / 15:00 check-in = 4h; cleaning eats most of it
- Never admit before turnover cleaning finished — no fee makes half-cleaned apartment acceptable
- Partial compromise: store luggage in hallway from 11:00, not full check-in

### 6) VseUberu.ru cleaning expert — updated 16.01.2026 (accessed 2026-09-14)
- URL: https://vseuberu.ru/blog/kak-organizovat-uborku-posutochnyix-kvartir
- Current cleaning after every checkout, no exceptions
- Minimum «cleaning window» between checkout and next check-in: 2–3 hours for studio/1-room; 4–5 hours for larger or force majeure

### 7) Sutochno extranet superhost interview (accessed 2026-09-14)
- URL: https://extranet.sutochno.ru/blog/interwiewsuperhost-maksimirkutsk
- Early check-in free if previous guest left or apartment vacant; host asks previous guest checkout time, cleans, next guest may enter 11–12 if agreed

## Practical mechanics for Writer (facts only)
- Standard turnover in daily rental: checkout ~12:00, standard check-in ~14:00 — industry norm on Sutochno and Tutu
- «Early check-in» in listing ≠ guaranteed key at that hour if same-day turnover + cleaning not finished
- Paying early-check surcharge before confirming apartment readiness time creates guest risk: money sent, apartment still occupied by cleaning
- Host excuse «you arrived earlier than agreed» breaks down if agreed time was 9:00 and guest arrived 9:10
- Guest waiting cost: luggage in hallway/entrance/cafe; family with kids or work laptop on knees
- Alternative before payment: ask when previous guests leave AND when apartment will be fully ready with clean linen and key — in one message with fee amount
- Tutu case shows worst outcome: enter before cleaning finished → dirty dishes, used bedding
- Luggage storage at hotel/administrator or station locker is Tutu-suggested alternative if early check-in unavailable — context, not main story
- B06 already published «Выезд в полдень. Поезд через 4 часа — чемоданы у подъезда» — different hook (late checkout vs train), do not repeat

## Constraints for Writer
- Do NOT claim incident happened at specific Добрый дом property
- Do NOT turn into legal dispute, contracts, penalties
- Do NOT repeat B18/B19/B20 families
- Voice: warm calm host Добрый дом; hero = guest
- Numbers 1 500 / 890 / 9:10 / 14:00 / 4h50m are case-scenario prices, not verified market tariffs
- P0 phrase «квартиры посуточно тюмень» embed naturally in housing choice context
- No bank/JKH official tariff digits in this article

## writer_safe_urls (CTA)
- https://t.me/Dobriy_dom_72
- https://t.me/Dobriy_dom_Tyumen
- https://max.ru/id660300569233_biz
- https://добрыйдом-72.рф/
- https://добрыйдом-72.рф/blog/
- https://www.tutu.ru/geo/journal/polezno-passazhiru/article/rannij-zaezd-i-pozdnij-vyezd/
- https://sutochno.ru/sj/ranniy-zaezd-i-pozdniy-vyezd
- https://restfor.ru/kak-snyat-kvartiru-posutochno/

## Output instructions for Derouter research role
Write research-notes.md with sections:
research_meta, reader_problem, reader_outcome, practical_facts, demand_signal (table), constraints, useful_case_mechanics, typical_mistakes, voice_angle, surprising_fact, source_table (each row accessed_at 2026-09-14), writer_safe_urls
NO h2_outline, NO lead, NO FAQ skeleton, NO action_outline
Russian language
