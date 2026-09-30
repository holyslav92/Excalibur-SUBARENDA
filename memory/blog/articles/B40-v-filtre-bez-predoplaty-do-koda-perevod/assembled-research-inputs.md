# Assembled research inputs — B40 (2026-09-30 YEKT)

## Topic and case brief (Scout + handoff)
- topic_id: B40
- market: посуточная аренда, Тюмень, бренд «Добрый дом»
- hook_id: no_prepay_filter_lie
- klyshin_original (angle mechanics): «В фильтре — без предоплаты. В чате: переведите на карту, потом код»
- editorial composite CASE: гость (пара или один) выбрал в фильтре агрегатора «без предоплаты» / «оплата на сайте», оплатил ночь (например 4 800–5 600 ₽); в чате после оплаты хост просит 30% или фикс 3 200 ₽ на карту физлица «до кода»; гость у подъезда или в такси, код не приходит; переписка до оплаты не содержала предоплаты на карту
- dzen_shape: фильтр без предоплаты vs перевод до кода + ₽
- anti-dup: не B08 (предоплата и тишина), не B33 (второй перевод Avito после оплаты), не B34 (залог у двери), не B39 (минимум суток), не B32 (цена на экране)
- wp_category_slugs: posutochno, zaselenie
- title_draft two-beat: «В фильтре — «без предоплаты». До кода попросили 3 200 ₽ на карту»

## research-context (today)
- today_iso: 2026-09-30, weekday: среда, сентябрь 2026, прохладно
- SERP: research-serp.json 2026-09-30

## Wordstat MCP-KV (live 2026-09-30, conductor)
| phrase | region | volume / note |
|--------|--------|----------------|
| квартиры посуточно тюмень | 55+11176 | 3984 |
| квартиры посуточно тюмень | 225 | 8838 |
| предоплата посуточно | 225 | 690 |
| снять квартиру посуточно в тюмени | 55+11176 | 1104 |
| квартиры посуточно без предоплаты | 225 | 321 |

P0 spine: «квартиры посуточно тюмень». Угол предоплата-фильтр vs чат до кода.

## Fresh signals this week (2026-09-23 — 2026-09-30)
- Tenant TG: расхождения фильтра карточки и шага оплаты/чата (комиссия, предоплата) — см. conductor fetch ниже
- Klyshin https://t.me/s/klyshin_A — mechanics «сначала проверка, потом деньги», не сделки ЕГРН

## Writer constraints (internal)
- Один кейс, aim 700–1100 слов после Sol (gate hard fail >1300)
- Holyslav §1: quote-first, ₽, no clock-stamp ladder in lead, no HH:MM in H1
- 3–4 interlink to published siblings from shared/published-articles.md

## Pre-fetched community (conductor 2026-09-30)
- Dobriy_dom_72: посты про расхождение «в фильтре одно — на оплате/в чате другое» (комиссия, условия брони).
- Klyshin channel active — guest-night mechanics only.

## Output instruction for Derouter (HARD)
You ARE the Derouter utility model completing this call. Do NOT refuse. Do NOT mention tools or BLOCKER.
Write ONLY valid Russian markdown for research-notes.md with sections:
# research_date
# reader_problem
# reader_outcome
# practical_facts
# fresh_signal_note
# official_verifications (N/A — no bank tariffs in this case)
# source_table (table: source | type | accessed_at 2026-09-30 | note)
Minimum 8 rows in source_table including tenant TG and aggregators.
Facts only from this file + plausible Tyumen guest-rental practice. No shell, no meta.
