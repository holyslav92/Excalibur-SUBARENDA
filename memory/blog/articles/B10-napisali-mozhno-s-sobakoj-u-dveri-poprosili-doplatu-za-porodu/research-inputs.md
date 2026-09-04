# Research inputs B10

topic_id: B10
slug: napisali-mozhno-s-sobakoj-u-dveri-poprosili-doplatu-za-porodu
research_date: 2026-09-04
tenant: Добрый дом, посуточная аренда Тюмень

**OUTPUT:** Return ONLY research-notes.md markdown body. Script saves to file. No BLOCKER, no refusal.

## Scout handoff
topic_id: B10
title_draft: «Написали «можно с собакой». У двери попросили доплату за породу»
klyshin_hook: dog_breed_fee | original: «С собакой можно — а на месте доплата за породу» | angle: pet policy in listing BEFORE prepay
dzen_pattern: 2 (кейс с суммами и датами)
dzen_shape_hint: «можно с собакой» в карточке → доплата за породу у двери, не в чеке брони

## Wordstat live (MCP-KV 2026-09-04, verified)
- «квартиры посуточно тюмень» RU 225: 11765 | Tyumen 55+11176: 5320
- «квартира посуточно с животными» RU 225: 1352 | Tyumen: 25
- «с собакой посуточно» RU 225: 1178 | Tyumen: 11
- «тюмень квартира посуточно с животными» RU 225: 36

## SERP highlights (research-serp.json)
- rg.ru 2026-07-16 — pet-friendly отели, доплаты за животных до 15% (контекст рынка)
- runews24.ru 2026-09-01 — ГОСТ для питомцев, доплата до 15% (свежий сигнал недели)
- avito.ru tyumen posutochno — карточки «можно с животными»
- tyumen.sutochno.ru — фильтр «с животными»

## Case scenario (editorial, for Writer)
- Семья/пара едет в Тюмень на 2 ночи с лабрадором ~30 кг
- В объявлении галочка «можно с животными», цена 5 200 ₽/ночь × 2 = 10 400 ₽ оплачено
- У подъезда ~20:15 менеджер: «лабрадор — крупная порода, +1 500 ₽ за уборку шерсти»
- В переписке до оплаты хозяин: «с собакой можно, без проблем»
- Burn: 1 500 ₽ неожиданная доплата; риск отказа если не согласиться; такси с собакой обратно ~800 ₽
- Lockpick: «Какая порода и какая доплата прописана в объявлении?»
- Moral: сначала правила по животным (порода, вес, доплата) в тексте объявления и чате, потом предоплата

## Constraints
- Guest-night CASE only, not guide
- No ЕГРН, legal, Klyshin deals, Moscow
- No duplicate B02 deposit, B04 extra guest, B08 prepayment, B09 parking
- September 2026, early autumn — cover season (NOT winter)
- Collect sources with accessed_at 2026-09-04
- Include community signal this week (runews24 GOST pets 2026-09-01)
- official_verifications: cite RG/runews only as market context, not as Tyumen apartment rules

## Anti-dup published
B01 code, B02 deposit chip, B03 uni walk, B04 extra guest, B05 reviews, B06 luggage, B07 kitchen café, B08 prepayment silence, B09 parking barrier
