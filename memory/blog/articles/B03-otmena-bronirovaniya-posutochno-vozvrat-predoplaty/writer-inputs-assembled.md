# Writer inputs assembled — B03

## Role
You are Excalibur BLOG Writer. Output ONLY a clean HTML fragment for `drafts/writer.html`.
NO `<h1>`. NO markdown fences. NO wrapper `<html>`/`<body>`.
Meaning draft — facts and structure; Sol will apply tenant voice later.

## H1 (for context only — do NOT output h1)
Планы сорвались — предоплату удержали. Что выяснить до оплаты

## dzen_pattern: 3 — страх → инструкция в §1
- **Paragraph 1 (opening):** name the money risk (prepayment held after cancelled plans) → immediately tell the reader what to check/do first (before paying or when disputing).
- Not a legal dump. Calm host instruction for short-term rental guest in Tyumen.
- Season: August 2026, summer. No winter scenarios.

## Title brief
- topic_id: B03
- slug: otmena-bronirovaniya-posutochno-vozvrat-predoplaty
- subject: отмена бронирования посуточно — возврат предоплаты
- angle: Klyshin rhythm — money at stake when plans collapse; what to ask BEFORE payment

## Reader problem
Guest transferred prepayment for short-term apartment, plans fell through, host or platform says "non-refundable" citing offer terms. Unclear whether money must be returned, how much can be withheld, what to ask before paying.

## Reader outcome
Understand hotel vs short-term apartment difference; when prepayment is refundable; questions before transfer (free cancellation window, withholding, refund timeline); what to save in correspondence if cancellation already happened.

## Facts (ONLY from research — do not invent)

### Hotel ≠ short-term apartment
From March 2026 media/SERP about hotels (PP RF №1912): cancel before check-in day → full prepayment refund. This applies to classified accommodation (hotels), NOT ordinary apartment rental by individual without hotel status. Mention as context with clear disclaimer — do NOT present hotel rules as apartment rules.

### Community case 1 (harant q-201970, 2026-06-12)
Guest booked guest house room, cancelled 5+ days before check-in; hosts refused to return 12,000 ₽ citing offer contract. Lawyers: withholding entire prepayment by offer alone is unlawful; under consumer law art. 32 and GC art. 782 clause 1, customer may refuse anytime, compensating only **documented actual expenses** (not penalty, not lost profit). Offer clause excluding refund regardless of expenses may be void (art. 16 consumer law).

### Community case 2 (harant q-193619, 2026-05-21)
Avito booking, 2 months before check-in; platform refused refund — "free cancellation" window expired (6 hours after booking). Lawyer: refusing far before check-in, no actual expenses; art. 32 consumer law and art. 782 GC give refund right; 6-hour penalty clause may be challenged. Save receipts and correspondence.

### Landlord status matters (harant blog, updated 2026-07-13)
If apartment rented by IE, self-employed or organization systematically providing accommodation — consumer law applies (art. 32: refuse anytime minus proven expenses). If individual without entrepreneur status on one-off deal — GC chapter 35 (lease), consumer law does NOT apply; refund terms per contract and GC.

### Advance vs deposit (задаток)
If payment not formally documented as задаток (GC art. 380), courts often treat as advance (GC art. 487) — if deal fails, full return.

### Platform rules
Avito, Sutochno.ru, direct booking — part of offer: flexible/moderate/strict cancellation. Guest agrees on payment, but with entrepreneur provider rules cannot worsen consumer position below consumer law.

### What to ask BEFORE payment (Добрый дом angle)
1. Free cancellation window (hours/days)
2. Percent or amount withheld on late cancellation
3. Refund timeline to card
4. Written confirmation of terms in messenger or booking
5. Whether landlord is IE/self-employed

### If cancellation already happened
Record date and method of cancellation; request calculation and documents for actual expenses; send written claim with booking, payment, cancellation proof. Exact Добрый дом terms — only from current site conditions or manager.

### Do NOT confuse with
- B02: deposit (залог) on checkout — link contextually if natural
- B01: contactless check-in codes — link contextually if natural
- This article: prepayment for booking BEFORE check-in only

### Surprising fact
Fresh SERP materials about hotels and 100% refund from March 2026 — guest of short-term apartment may wrongly think "law already decided everything", but for private rental key are contract, host status, platform rules.

## Constraints
- For guest, NOT legal consultation: no lawsuits, no "must go to court", no ЕГРН, no notary, no court, no "I am a lawyer".
- Do not state exact platform withholding percentages without citing their current terms; general wording ("depends on cancellation tariff on platform").
- Supply: short-term rental Tyumen, comfort+; not hotels/hostels as main topic.
- Simple spoken Russian. Short paragraphs. No канцелярит.
- Banned words: ЕГРН, нотариус, суд, «я адвокат», «мы лучшие», бизнес-класс, WhatsApp.
- Phone ONLY: +7 (993) 574-83-22

## Structure (suggested H2)
- Opening §1: fear → instruction (pattern 3)
- Where they get you (отель vs квартира, оферта, 6 часов на Авито)
- Чек-лист вопросов до оплаты (5 questions — fulfill H1 promise)
- Что сохранить если отмена уже случилась
- «У нас так» brand block — Добрый дом: written terms before payment, messenger support, instruction before check-in (only brand_facts_allowed from tenant)
- FAQ (3-4 questions)
- Final CTA: booking + phone

## CTA funnel IN BODY (HARD placement)
1. **After checklist (questions before payment):** link to Telegram channel for "полный список" → https://t.me/Dobriy_dom_72
2. **After «у нас так» brand block:** MAX https://max.ru/id660300569233_biz OR manager https://t.me/Dobriy_dom_Tyumen — we send instructions before check-in
3. **Final:** booking https://добрыйдом-72.рф/ and phone +7 (993) 574-83-22

## Interlink (1-3 published siblings — contextual in H2, not spam)
- /blog/beskontaktnoe-zaselenie-posutochno-tyumen/ — B01 contactless check-in (different pain: codes, not prepayment)
- /blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/ — B02 deposit on checkout (not prepayment — clarify distinction)

Use relative paths `/blog/...` in href.

## Also create mentally (separate artifact): dzen-excerpt.json
hook + first_screen + takeaway for Dzen card. Not in writer.html.

## Anti-dup (do not repeat these topics as main angle)
- B01: contactless check-in codes
- B02: deposit not returned, chip on stove

## Output
Clean HTML fragment, 1200-1800 words Russian text, multiple `<h2>`, `<p>`, `<ul>/<ol>` where useful, `<a href>` for CTAs and interlinks.
