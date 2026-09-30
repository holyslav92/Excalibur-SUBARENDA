# Assembled inputs for Derouter research — B41

research_date (today_iso): 2026-09-30
topic_id: B41
tenant: Добрый дом, Тюмень, посуточная аренда
primary_query: квартиры посуточно тюмень
case angle: guest paid 2 nights; house rules PDF promise «тишина после 23:00»; at 01:17 drilling/assembly noise from neighboring flat; host says «не мы, соседи»; guest cannot sleep, second night at risk.

## Scout handoff
- hook neighbors_rules_night_noise
- title_draft: «В правилах — «тишина после 23:00». В 1:17 — дрель за стеной»
- wordstat P0: «квартиры посуточно тюмень» 3984 (55+11176), RU 8838; «посуточно соседи шум» totalCount 22 RU; «шум соседей аренда квартиры» totalCount 16 RU
- dzen_pattern: 2

## Anti-dup (published titles only)
- B14: тихий дом + музыка 23:40 — different (music party, not drill after rules)
- B12: тихий центр + стройка у окна днём — not night drill after rules PDF
Do not copy B14/B12 plots.

## Fresh community signal this week (required)
**t.me/s/Dobriy_dom_72, 30.09.2026 ~09:27** (forward Dobry Content): mismatch listing vs reality — explicitly mentions guests check only price/district while «заявлена тишина, а окна на шумную дорогу»; details should be clarified before payment. URL: https://t.me/s/Dobriy_dom_72

## SERP / reference (accessed 2026-09-30)
- gogov.ru silence law Tyumen 2026: quiet hours framing, late luggage advice — https://gogov.ru/silence-law/tyumen
- Dzen cluster «закон о тишине посуточно Тюмень» — sleeping districts vs specific house (snippet in research-serp.json)
- VK wall post pattern «соседи спят — гости отдыхают» — check surroundings not only photos (research-serp)

## Wordstat MCP live 2026-09-30
regions 55,11176,225 — see scout handoff counts above.

## Writer scenario facts (fictional case, Tyumen short-term stay)
- Dates: check-in 28.09.2026 ~21:40, noise 29.09.2026 01:17
- Paid: 2 nights, 4 600 ₽/night on platform receipt (9 200 ₽ total) — illustrative
- Rules PDF line: «с 23:00 до 08:00 — режим тишины в квартире и общих зонах»
- Guest message to host 01:22; host reply 01:31 «это соседи, мы не можем их остановить»
- Guest pain: sleep before business meeting / exam; cannot relocate at night without losing money

## Interlink siblings (published, for Writer/Sol only slugs)
- /blog/napisali-tihij-dom-v-23-40-sosedi-vklyuchili-muzyku/
- /blog/napisali-tihij-centr-v-6-30-za-oknom-kran/
- /blog/bez-zaloga-v-filtre-zalog-u-dveri/
- /blog/instrukciya-zaseleniya-posutochno-ne-tot-podezd/

## CTA writer_safe
https://t.me/Dobriy_dom_72 , https://max.ru/id660300569233_biz , https://добрыйдом-72.рф/booking/ , +79935748322 , https://t.me/Dobriy_dom_Tyumen

## official_verifications
NOT_REQUIRED — no bank/gov fee digits as thesis. Silence law hours from gogov as background only, not legal essay.

## OUTPUT INSTRUCTION (HARD)
You are inside excalibur_blog_derouter_opus_chat.py --role research.
Write ONLY markdown file research-notes.md body (sections: reader_problem, reader_outcome, practical_facts, constraints, source_table, writer_safe_urls, official_verifications).
No refusals, no meta about running scripts, no BLOCKER text.
