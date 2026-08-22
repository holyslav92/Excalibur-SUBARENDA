# Research inputs — B03 (assembled for Derouter)

research_date: 2026-08-22
timezone: Europe/Moscow
tenant: Добрый дом — посуточная аренда Тюмень, comfort+, не юрист
topic_id: B03
title: Отмена бронирования посуточно — возврат предоплаты
primary_query: отмена бронирования посуточно — возврат предоплаты
priority: P0

## CRITICAL DISTINCTION (must preserve in notes)

Article is about DAILY RENTAL APARTMENTS (посуточно / квартиры), NOT hotels.
SERP is flooded with hotel rules from 1 March 2026 (PP 1912, hotel services rules) — use ONLY as background context, clearly separated.
Private short-term apartment rental = contract + platform terms + consumer law (if host is IP/self-employed/org), NOT hotel PP 1912 rules unless object is classified as hotel.

## Scout handoff

- Klyshin hook: cancellation_refund | «планы сорвались — вернут ли предоплату?»
- final P0: «отмена бронирования» RU 14147 / Tyumen 104
- dzen_pattern: 3 (страх → инструкция)
- anti_dup: не коды (B01), не залог/скол (B02), не вечеринки в правилах
- interlink: beskontaktnoe-zaselenie, perevel-zalog, skrytye-doplaty

## Wordstat (MCP-KV live, accessed 2026-08-22)

| phrase | volume |
|--------|--------|
| отмена бронирования | 14147 RU / 104 Tyumen |
| бесплатная отмена бронирования | 935 |
| отмена бронирования возврат средств | 724 |
| условия отмены бронирования | 663 |
| штраф за отмену бронирования | 458 |
| суточно отмена бронирования | 379 |
| квартиры посуточно тюмень | 6446 Tyumen |

Cover stickers: штраф за отмену 458, возврат средств 724, суточно отмена 379

## Fresh community signal (accessed 2026-08-22)

URL: https://harant.ru/questions/q-201970/
Date posted: 12.06.2026
Question: Guest booked room in guest house, cancelled 5+ days before check-in. Hosts refuse to return 12,000 rub prepayment citing offer contract.
Lawyer answers (consensus):
- Full prepayment retention citing offer alone is NOT lawful (ст. 32 ЗоЗПП, п. 1 ст. 782 ГК РФ)
- Guest may refuse service anytime; host may deduct ONLY documented actual expenses (not penalty, lost profit, idle room)
- Offer clause excluding refund regardless of expenses may be void (ст. 16 ЗоЗПП)
- IF object is registered hotel/classified accommodation: PP RF 27.11.2025 №1912 п.16 — full refund if cancelled before check-in day; 5+ days qualifies
- Guest houses in individual homes under FZ 127-FZ (07.06.2025) — PP 1912 does NOT apply, but general consumer/GK rules on actual expenses remain
- Practical steps: written claim, attach booking/payment/cancellation proof; Rosпотребнадзор or court if refused

NOTE: case is guest house, not apartment — but pain pattern identical for посуточно guests (prepayment + offer + refusal).

## SERP summary (research-serp.json, searched 2026-08-22)

Most results = hotel rules March 2026 (100% refund if cancel before check-in). Examples:
- pulsfid.ru, azo-hotels.com, advokaty32.ru, renlife.ru — all hotel-focused
- harant.ru q-201970 in community search — guest house prepayment case
- harant.ru q-215011 — hotel prepayment retention

For APARTMENTS посуточно:
- Relations depend on host status (физлицо vs ИП/самозанятый/организация)
- If host is entrepreneur: ст. 32 ЗоЗПП — refuse anytime, pay only actual documented expenses
- If host is private individual (not entrepreneur): ГК РФ chapter 35 (найм), contract terms matter more; ЗоЗПП may not apply
- Platform rules (Avito, Суточно.ру, Ostrovok apartments, direct booking) add cancellation windows — guest agrees at payment but cannot override ЗоЗПП where applicable
- harant.ru q-193619 (Avito booking): 6-hour free cancel clause challenged; 2 months before check-in — no actual expenses possible

## Angle for Добрый дом (tenant)

Guest transferred prepayment, plans fell through, host/platform says «non-refundable». What to ask BEFORE payment: free cancellation window, % retention, refund timeline to card, written confirmation in messenger.
Supply: only посуточная аренда Тюмень, comfort+.

## CTA (tenant-config)

- Site: https://добрыйдом-72.рф/
- TG channel: https://t.me/Dobriy_dom_72
- MAX: https://max.ru/id660300569233_biz
- Manager: https://t.me/Dobriy_dom_Tyumen
- Phone: +7 993 574-83-22

## Interlink siblings (published)

- /blog/beskontaktnoe-zaselenie-posutochno-tyumen/
- /blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/
- /blog/skrytye-doplaty-pri-arende-kvartiry-kak-ne-pereplatit/

## Published titles (anti-dup only)

| B01 | beskontaktnoe-zaselenie-posutochno-tyumen | Оплатил квартиру посуточно. Код прислали от чужой двери |
| B02 | perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem | Снял квартиру посуточно. Залог не вернули — нашли скол на плите |

## Constraints for Writer

- Не ЕГРН, не суд, не адвокат — бытовая инструкция для гостя
- Не путать отель март 2026 с квартирой посуточно
- Факты только из источников ниже
- No h2_outline, no lead, no FAQ skeleton
- official_verifications: N/A unless citing platform TOS with exact terms

## Output required

research-notes.md sections: research_date, reader_problem, reader_outcome, practical_facts, constraints, voice_angle, surprising_fact, fresh_signal_note, wordstat_stickers, source_table (accessed_at 2026-08-22 each), writer_safe_urls, official_verifications (N/A row ok), overlap_note

research-agent-report.json: status PASS, fresh_signal URL, official_source_audit NOT_REQUIRED (no bank tariffs)
