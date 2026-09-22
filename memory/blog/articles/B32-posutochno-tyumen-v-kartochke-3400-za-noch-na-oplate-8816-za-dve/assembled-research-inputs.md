# Assembled research inputs — B32 (Cursor conductor → Derouter research)

## Mandate for Derouter

- Output **only** valid `research-notes.md` markdown body (sections: research_date, reader_problem, reader_outcome, practical_facts, constraints, typical_errors, voice_angle, surprising_fact, fresh_signal_note, wordstat_stickers, official_verifications, source_table, writer_safe_urls).
- **NOT** h2 outline, NOT lead, NOT FAQ skeleton, NOT legal essay.
- Guest CASE: Tyumen short-term rental, **2 nights**, card shows **3 400 ₽/night** → guest mentally totals **6 800 ₽**; checkout shows **8 816 ₽** with **+12% service** and **1 200 ₽ cleaning** (Scout/Klyshin editorial hook — composite, not verified booking).
- `research_date`: **2026-09-22** (Asia/Yekaterinburg / YEKT).
- Every `source_table` row: `accessed_at: 2026-09-22`.
- Language: Russian.
- Explicit: **только markdown notes, без BLOCKER, без shell, без meta-refusal**.

## Topic metadata

- topic_id: B32
- slug: posutochno-tyumen-v-kartochke-3400-za-noch-na-oplate-8816-za-dve
- title_draft: «В карточке 3 400 ₽ за ночь. На оплате — 8 816 ₽ за две»
- primary_query / P0: «квартиры посуточно тюмень»
- Scout hook: `checkout_price_stack` | klyshin_original: «В карточке 3 400 ₽ за ночь. Две ночи — 6 800 ₽. На оплате +12% сервиса и 1 200 ₽ уборка» | signal https://t.me/klyshin_A
- dzen_shape_hint: «За ночь квартира казалась дешевле отеля — пока не открыли шаг оплаты с +12% и уборкой»
- Brand: Добрый дом (Tyumen) — **do not claim this exact checkout happened on Dobry Dom or one named aggregator**; composite guest case localized to Tyumen.

## Anti-dup (published titles only)

- B05 rating vs price
- B07 «кухня есть» hidden food cost
- B10 «всё включено» taxi
- B17 communalka on checkout
- B23 «уборка включена» → **1 800 ₽ on exit** (post-stay dispute, not pre-pay stack)
- B29 receipt / not a hotel
- **New angle:** **per-night card line vs full checkout total** (service % + cleaning before pay); compare full stay to hotel, not nightly teaser.

## Wordstat (Scout handoff + MCP attempt 2026-09-22)

MCP-KV `wordstat_get_top_requests` failed twice (API 499 cancelled). Use Scout live handoff + mark WORDSTAT PARTIAL.

| phrase | regions | totalCount | note |
|--------|---------|------------|------|
| квартиры посуточно тюмень | 55, 11176 | 4409 | final P0 |
| квартиры посуточно тюмень | 225 | 9372 | RU compare |
| комиссия посуточно | 225 | 1903 | supporting |
| уборка посуточно | 225 | 1932 | supporting |
| посуточно или отель | 55, 11176 | 8 | weak Tyumen |
| отель или посуточная квартира | 225 | 280 | hotel contrast |
| квартира посуточно тюмень цена | 225 | 92 | local price |
| отели тюмень | 55, 11176 | 7002 | hotel contrast demand |

## Editorial math (hook anchors — not court-verified)

- 3 400 × 2 = **6 800 ₽** (nights only, guest mental model).
- +12% of 6 800 = **816 ₽** (service line in hook).
- +**1 200 ₽** cleaning (flat per stay in hook).
- Total **8 816 ₽**; gap vs 6 800 = **2 016 ₽** «цена невнимательности» (handoff editorial brief).

## Fresh community / news (week ~2026-09-15 — 2026-09-22)

1. **https://t.me/s/Dobriy_dom_72** — September 2026 posts (views/time stamps on channel feed):
   - «Несоответствие квартиры описанию» — **гость часто проверяет только цену и район**, детали замечает **после оплаты**; совет прояснять до бронирования (local tenant channel).
   - «Нужно остаться ещё на день» — спрос влияет на **цену и доступность**; продление заранее.
   - «Скидка 10% раннее бронирование» — **прямые цены без комиссий агрегаторов**, заявленная экономия 15–25% vs посредники (marketing claim by tenant, not universal market stat).
   - Бесконтактное заселение / ночной заезд — проверять не только адрес и цену.
2. **https://t.me/s/klyshin_A** — channel **active 22 Sep 2026** (e.g. post on ЦБ key rate 14%, views ~12.4K). Scout **checkout_price_stack** hook attributed to Klyshin topic bank; **no literal 3400/8816 post found in latest feed** — treat numbers as **editorial composite**, channel as freshness + signal URL.
3. **https://sutochno.ru/sj/iz-chego-skladivaetsya-stoimost-bronirovaniya** — published **10 Dec 2025** (official Sutochno journal): guest sees **full prepayment amount at booking**; **cleaning and extra guests included in calculation**; **«Суточно.ру не берёт с вас комиссию»** — no extra guest commission on top of host price (platform model differs from «+12% at checkout» hook).

## Official / platform facts (for Writer contrast — no bank tariffs)

### Sutochno.ru (official)

- **Cost breakdown article** (sj, 10.12.2025): host sets price; cleaning/extra guests **in booking calculation**; prepayment 15–100% shown when booking; **no separate commission charged to guest** beyond host amount.
- **https://sutochno.ru/help/gosti/safety** (help): prepayment only via sutochno.ru; if prepayment &lt;100%, rest to host at check-in; **«Между внесением предоплаты и заселением никакие дополнительные платежи не требуются»**; pay exactly amount in booking.
- **https://sutochno.ru/blog/rules** (host rules): must list **all** prices including **уборка**, extra guests, deposit; guests dislike when **real price exceeds expected**.
- **https://sutochno.ru/help/arendodateli/public/price** (host help): cleaning can be **included in stay price or separate line** in listing; affects total calculation.

### Implication for CASE

- Hook with **+12% service at payment** matches **some aggregators / OTA checkout UX**, not Sutochno’s stated «no guest commission» model.
- Writer: explain **platforms differ** — always open **payment breakdown** before confirm; compare **8 816 ₽** (or whatever total) to hotel for **same dates**, not to **3 400 × nights** alone.
- Do **not** accuse a named platform of fraud; structural guest rule from handoff.

## Guest mechanics (practical)

- Search cards often emphasize **«от X ₽ / сутки»** or one-night minimum display; **weekend/special dates** can change per-night average.
- **Flat cleaning fee** often per **booking**, not per night — two nights ≠ «уборка × 2».
- **Service fee** may be % of accommodation subtotal, fixed, or embedded in nightly rate depending on channel (Sutochno: embedded; others: may be separate line).
- **Guest count** can trigger extra-person charges not in base «2 guests included» price.
- **Taxes/fees** line on hotel sites — same mental trap when comparing apartment to hotel.
- Before pay: expand **детализация**, check dates, guests, pets, early/late fees, cancellation, deposit (may be separate hold, not in 8 816).

## Tyumen market context (SERP, not price survey)

- Local listings hubs: tyumen.sutochno.ru, Avito posutochno, 2GIS, Yandex Maps short-term category (research-serp.json 2026-09-22).
- Dobry Dom positions **direct booking** vs aggregators (channel posts) — Writer may mention as **one local option**, not as proof of hook incident.

## Constraints for Writer (from handoff)

- Reader = **guest**, not operator report.
- Dialog beat allowed: guest «3 400 за ночь» vs host «смотрим итоговую сумму» (generic host voice).
- Lockpick question: «Где до оплаты увидеть всю сумму с уборкой и сервисом?» → action: open breakdown, verify dates/guests/fees/cancel.
- Refusal bit: if total not visible before confirm — don’t pay (guest safety rule, not legal conclusion).
- Verdict: choose by **full stay total**, compare that to hotel.
- No Moscow/Dubai/MKAD cases; no legal-bank hook; Dobry Dom brand only light local context.

## CTA / writer_safe_urls (tenant)

- https://t.me/Dobriy_dom_72
- https://t.me/Dobriy_dom_Tyumen
- https://max.ru/id660300569233_biz
- https://добрыйдом-72.рф/
- https://добрыйдом-72.рф/booking/
- https://t.me/klyshin_A
- https://tyumen.sutochno.ru/
- https://sutochno.ru/sj/iz-chego-skladivaetsya-stoimost-bronirovaniya
- https://sutochno.ru/help/gosti/safety
- https://sutochno.ru/blog/rules
- https://sutochno.ru/help/arendodateli/public/price

## official_verifications

- No bank/gov tariff digits in scope.
- Sutochno claims (no guest commission; cleaning in calculation; no extra payments before check-in) — cite **official sutochno.ru** URLs above, not travel blogs.

## surprising_fact candidates

- Same city search: **«отели тюмень»** Wordstat 7002 (Tyumen+region) vs apartment P0 4409 — hotel comparison is a real search behavior, not Writer invention.
- On Sutochno official model, **+12% at checkout as separate service line** would **contradict** their published «no commission to guest» policy — case hook likely models **another channel** or generic OTA pattern; Writer must keep platform-agnostic tone.
