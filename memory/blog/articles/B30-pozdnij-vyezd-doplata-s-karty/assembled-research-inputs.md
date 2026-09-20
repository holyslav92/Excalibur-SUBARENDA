# DEROUTER RUNTIME

You are the utility-tier research synthesizer inside `excalibur_blog_derouter_opus_chat.py` on a host with filesystem and network. Write the complete `research-notes.md` document in Russian per SKILL below. Do **not** output `DEROUTER RESEARCH BLOCKER`, meta-refusal, or shell instructions — only the research notes body with all required sections.

# Assembled research inputs — B30 (2026-09-20)

## Topic and handoff

- topic_id: B30
- title_draft: «Выезд до 14:00 согласовали. Уехали в 14:38 — с карты списали ещё 1 800 ₽»
- format: guest CASE only (Tyumen short-term rental), NOT guide, NOT legal essay, NO invented statutes as «ваше право»
- reader: guest who booked daily rental in Tyumen (command trip / family weekend)
- voice tenant: «Добрый дом», host perspective in Sol — NOT claiming this incident happened at Dobry Dom
- case mechanics (editorial composite from Scout hook):
  - standard checkout in rules often 12:00; guest asked to stay until 14:00; host/manager agreed in chat (verbally or message)
  - guest left at 14:38 (38 minutes after agreed 14:00)
  - after departure: additional 1 800 ₽ captured/charged from card (preauth hold or linked card), guest had not seen this sum in the original booking total
  - guest pain: «мы же договорились до двух» vs «вы нарушили время / тариф почасовой»
- lockpick_question: «До какого часа выезд и сколько стоит каждая лишняя минута — и где это зафиксировано до оплаты?»
- refusal beat pattern: «Правила в договоре» / «Автоматически по тарифу» после keys already returned
- moral: согласованный поздний выезд = письменно время + цена + что будет при превышении; карта — не чёрный ящик после выезда
- 1 800 ₽ is scenario anchor from title, NOT Tyumen market tariff
- Do NOT copy Klyshin purchase/inheritance stories; do NOT invent court outcomes or «статья X даёт оспорить»
- Anti-dup vs B06 (baggage window after 12:00 checkout, not card fee), B21 (early check-in + cleaning wait), B23 (1 800 ₽ linen/cleaning at checkout), B17 (utilities bill), B02 (deposit skол)

## Scout Klyshin hook (2026-09-20)

- hook_id: late_checkout_fee
- original rhythm: checkout_train_bags → reworked to late checkout fee + card charge
- angle: agreed late checkout, then post-departure card debit
- signal_urls: https://t.me/klyshin_A (channel active week of 2026-09-14–20; live posts are purchase-law topics — hook is editorial from topic bank, same pattern as B21/B23)
- dzen_shape_hint: «Кейс с суммой: поздний выезд согласовали, но после отъезда списали 1 800 ₽ — что спросить до заселения»

## Wordstat (MCP-KV live 2026-09-20)

- «квартиры посуточно тюмень»: 4423 (regions 55+11176) — Scout handoff logged 9530 same day earlier probe; use live 4423 in notes with note both probes same day
- «снять квартиру посуточно в тюмени»: 1311 (55+11176)
- «поздний выезд»: 9868 (225); 106 (55+11176) — hotel-skewed nationally, weak Tyumen cluster
- «доплата за поздний выезд»: 92 (225)
- «поздний выезд сколько стоит»: 224 (225)
- P0 demand spine: «квартиры посуточно тюмень»; do NOT claim P0 for «доплата за поздний выезд»

## Fresh community / industry signals (accessed 2026-09-20)

### Dobry Dom TG (tenant channel, this week)
- URL: https://t.me/Dobriy_dom_72
- Post ~2026-09-20: бесконтактное заселение удобно для «позднего заезда и раннего выезда» — зона риска неверный код/домофон; условия лучше уточнять до брони
- Post ~2026-09-19–20: фиксация состояния квартиры при заезде (фото) — снимает споры при выезде
- Post ~2026-09-20: продление на день — «условия продления лучше уточнять заранее»
- CTA only — NOT proof of B30 incident

### Directline.pro deposit article (updated 2026-08-07)
- URL: https://www.directline.pro/connect/p/zalog-pri-sdache-kvartiry-posutochno/
- Deposit may cover delayed checkout if contract/rules warned in advance
- Hold (холд) vs transfer: money frozen on guest card until checkout inspection
- Retention requires prior warning of rules; photo/video after checkout for damage
- Industry legal comment (not statute text): удержание только если гость предупреждён заранее

### Directline rules memo
- URL: https://www.directline.pro/connect/p/pravila-prozhivaniya-v-posutochnoj-kvartire/
- Memo should state check-in/check-out times, deposit return, early/late stay conditions

### Tutu.ru guest journal
- URL: https://www.tutu.ru/geo/journal/polezno-passazhiru/article/rannij-zaezd-i-pozdnij-vyezd/
- Typical apartment window: check-in ~14:00, checkout ~12:00; gap for cleaning
- Late checkout must be agreed in advance; often extra fee; hotel rules PP for hotels — apartments same negotiation logic per Tutu
- Through Tutu: agreed early/late with payment → new voucher = guaranteed; chat-only agreement weaker
- Real case: guest paid early check-in, waited at dirty apartment — separate angle (B21) but shows «оплатили доп — ждали у двери»

### TravelLine KB (PMS industry)
- URL: https://www.travelline.ru/support/knowledge-base/kak-nastroit-doplatu-za-pozdniy-vyezd/
- Hosts configure late checkout: free, fixed fee, % of night, hourly fixed, hourly auto (day rate / 24 × hours), or forbidden
- Option to include late checkout in prepayment; on cancel penalty may include that fee
- «Выделять доступность» — late checkout only if next day free (blocks inventory)

### Bronirui Online KB
- URL: https://bronirui-online.ru/baza-znaniy/nastrojki/rannij-zaezd-pozdnij-vyezd/
- Example late checkout rule: after 10:00 fixed 2 000 ₽ for exit; hourly 500 ₽ early check-in example
- Guest may see surcharge when picking times in booking module if enabled

### Bronevik industry blog (deferred payment / hold)
- URL: https://bronevik.com/ru/blog/stati/otlozhennyy-platezh-v-gostinichnom-biznese
- Hotels use preauth for minibar, damage, late checkout; capture or release after checkout; bank release timing varies (industry description, not one bank tariff)

### Yandex Pay blog (hold mechanics, general)
- URL: https://pay.yandex.ru/blog/articles/holdirovanie-platezhey-dlya-biznesa
- Hold = temporary block; capture later for actual services; auto-release if not confirmed in bank window

### Rospotrebnadzor press (hotel services rules context)
- URL: http://26.rospotrebnadzor.ru/press-center/pr/14348/
- For **hotel** services: checkout time set by provider; late departure fee «в порядке, установленном исполнителем» if disclosed
- Constraint for Writer: private apartment daily lease is often **договор аренды/оказания услуг**, not automatic application of hotel PP — cite hotel rules only as analogy for «расчётный час», not as «закон для всех квартир»

### Sutochno extranet legal memo (host-side)
- URL: https://extranet.sutochno.ru/blog/legal-issues
- Contract must list price, deposit, living rules, grounds for withhold; avoid vague «штрафы запрещены» wording

### VK community (host education, secondary)
- URL: https://vk.com/wall-216363519_203 — late checkout surcharge why/when (snippet in SERP)

## Turnover / time math for case

- Agreed extension: until 14:00
- Actual keys/handover: 14:38 → +38 min beyond agreement
- If host uses hourly tariff example 500 ₽/h (Bronirui industry example only), 38 min might be billed as full hour or pro-rata — must be in rules, not assumed
- 1 800 ₽ scenario may equal e.g. 3×600 or fixed «нарушение расчётного часа» from rules guest never saw — Writer must not invent formula; keep «сумма из переписки/скрина, не из воздуха»

## Guest checklist facts (practical, not lead)

- Before pay: standard checkout time, cost of late checkout, hourly vs fixed, max allowed late time
- If manager agrees extension in chat: ask single message to confirm «выезд до 14:00, доплата X ₽, при выезде после 14:00 — Y ₽/час или Z ₽ фикс»
- Ask whether card is **hold** for deposit and whether host can **capture extra** after checkout without second consent
- At handover: send «ключи сдал в 14:38» with timestamp in chat; photo of empty apartment optional
- After unexpected debit: save chat, booking rules screenshot, bank push/SMS; contact host then platform/bank per their process — do NOT promise chargeback outcome

## Dobry Dom tenant defaults (voice reference, not case)

- Brand: check-in/out and extensions «по договорённости», бесконтакт; clarify before booking
- CTAs from tenant-config: https://t.me/Dobriy_dom_72, https://t.me/Dobriy_dom_Tyumen, https://max.ru/id660300569233_biz, https://добрыйдом-72.рф/booking/, tel:+79935748322

## Overlap guard (published-titles-only)

- B06: checkout 12:00 vs train — luggage, not 14:38 card charge
- B21: paid early check-in, cleaning until 14:00
- B23: 1 800 ₽ at checkout for linen/cleaning dispute
- B17: utilities 1 840 ₽ at checkout

## Required output sections

research_date, reader_problem, reader_outcome, practical_facts, constraints, typical_errors, voice_angle, surprising_fact, fresh_signal_note, wordstat_stickers, official_verifications (empty table OK if no bank tariff digits), source_table (accessed_at 2026-09-20 each row), writer_safe_urls

## official_verifications

No bank/developer exact tariff claims required. If mentioning hold timing — only as ranges from industry blogs (Bronevik/Yandex Pay), not as «тариф Сбера».

## writer_safe_urls

https://t.me/Dobriy_dom_72
https://t.me/Dobriy_dom_Tyumen
https://max.ru/id660300569233_biz
https://добрыйдом-72.рф/
https://добрыйдом-72.рф/booking/
https://t.me/klyshin_A
https://www.tutu.ru/geo/journal/polezno-passazhiru/article/rannij-zaezd-i-pozdnij-vyezd/
https://www.directline.pro/connect/p/zalog-pri-sdache-kvartiry-posutochno/
https://www.directline.pro/connect/p/pravila-prozhivaniya-v-posutochnoj-kvartire/
https://www.travelline.ru/support/knowledge-base/kak-nastroit-doplatu-za-pozdniy-vyezd/
https://bronirui-online.ru/baza-znaniy/nastrojki/rannij-zaezd-pozdnij-vyezd/
https://bronevik.com/ru/blog/stati/otlozhennyy-platezh-v-gostinichnom-biznese
http://26.rospotrebnadzor.ru/press-center/pr/14348/
https://extranet.sutochno.ru/blog/legal-issues
