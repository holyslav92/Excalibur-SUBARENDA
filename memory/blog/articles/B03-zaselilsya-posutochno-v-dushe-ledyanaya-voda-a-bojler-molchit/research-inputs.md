# Research inputs — B03

Read: research-context.json, research-serp.json, .cursor/excalibur-blog-handoff.md
Date: 2026-09-26 (Asia/Yekaterinburg / Europe/Moscow)
Topic: первая ночь посуточно — ледяная вода в душе, бойлер не прогрелся / молчит
Tenant: Добрый дом — посуточная аренда Тюмень, operational guest facts (NOT legal essay)
Anti-dup: B01 = бесконтактное заселение / коды; B02 = залог не вернули; B03 ONLY hot water / boiler first night

## Klyshin × Wordstat (handoff)

- hook_id: guest_boiler_hot_water_first_night
- original: «первая ночь посуточно — в душе ледяная вода, бойлер не прогрелся»
- signal: https://t.me/klyshin_A
- P0 «квартиры посуточно тюмень» — 4209 (regions 55+11176); RU 225 compare 9221
- P1 «снять квартиру посуточно в тюмени» — 1191 (55+11176); RU 225 3143
- Narrow probes (RU 225, WORDSTAT PARTIAL — top list absent): «горячая вода посуточно» 39; «нет горячей воды посуточно» 19; «горячая вода квартира посуточно» 28; «бойлер квартира посуточно» 2

## Fresh signals (week of 2026-09-22 — accessed 2026-09-26)

1. Telegram @Dobriy_dom_72 (tenant channel): post about fixing apartment state at check-in — explicitly lists «исправность техники» among what should be verified before/during заселение; warns against deferring «на потом» (t.me/s/Dobriy_dom_72, fetched 2026-09-26). Same channel: posts this week on late check-in, mismatch with listing, contactless access — local operational voice.
2. Telegram @Dobriy_dom_72: post on listing mismatch («на фото есть … заявлена тишина») — angle adjacent: amenities in card vs reality (2026-09-26 fetch).
3. Scout angle channel: https://t.me/klyshin_A (real-estate stories; hook assigned in handoff, not a tariff source).

## Community / experience (older but factual patterns — label age)

- vc.ru/services/2143010 — guest booked Avito posutochno, hot water turned off from day 5, not disclosed in listing; host offered discount then tied refund to positive review (Aug 2025).
- pravoved.ru/question/4192284 — Sutochno.ru booking, days without hot water, shared boiler for studios, boiler burned out; compensation dispute (Jul 2024).
- forum.baxi.ru t=9672 — hot water only triggers from shower tap, not sink, until flow sensor «warmed up»; simultaneous washing machine affects taps (May 2024) — illustrates non-obvious plumbing, not «host fraud».
- t-j.ru/long-short-rent/ — for daily rental hosts often install electric boiler when central hot water shut off in summer; guests less tolerant than long-term tenants.

## Technical / operational facts (manufacturer & calculator sources)

- timberk.ru article + elec.ru calculator: 50 L storage heater from ~15°C to ~60°C ≈ 1.5–2 h at 1.5–2 kW TЭН; table ~78 min @ 2 kW for 50 L; full cold tank longer.
- Resanta product spec example: 50 L, 1.5 kW, ~100 min to 75°C (catalog data, not every apartment).
- Typical apartment: 50–80 L storage OR flow-through (6–12 kW); flow gives hot while power on, storage needs refill time after emptying.
- Host may leave boiler OFF between guests to save electricity → first guest waits full heat cycle.
- «Подождите 40 минут» is not universal; cold tank + 1.5 kW can be 90–120+ minutes.
- Late arrival: guest expects shower immediately; boiler may still heating.
- Mid-shower cold: storage depleted or flow heater overload / pressure drop.
- Instruction issues: guest must open hot tap, toggle switch on boiler panel, wait for indicator — user error happens (community anecdotes in SERP snippets).

## Questions guest should ask BEFORE payment (operational)

- Источник ГВС: центральная или электробойлер (накопительный / проточный)?
- Если бойлер: объём (л), включён ли до заезда, где выключатель/инструкция?
- Сколько реально ждать горячую воду после заезда вечером?
- В карточке «есть душ/ГВС» — это круглосуточно или «нагреется к утру»?
- Куда писать ночью, если воды нет (канал, не только Avito chat)?

## What to save in chat

- Screenshot of listing line about hot water / amenities.
- Host written answer: boiler type, on/off, expected wait.
- If promised «горячая вода есть» before arrival — timestamped message.
- Photo of boiler panel if dispute (optional at check-in).

## Constraints for Writer

- No legal essay, Rosпотребнадзор, court outcomes as main spine.
- No залог / предоплата / комиссия / собака / PDF подъезд as primary conflict (anti-dup list).
- vc.ru/pravoved cases = patterns, not statistics.
- Do not invent Добрый дом boiler specs or SLA; CTA from tenant only.
- Interlink sibling: B01 beskontaktnoe-zaselenie (late arrival + contactless) — contextual only.

## CTA (tenant-config)

- booking: https://добрыйдом-72.рф/booking/
- blog: https://добрыйдом-72.рф/blog/
- telegram channel: https://t.me/Dobriy_dom_72
- telegram manager: https://t.me/Dobriy_dom_Tyumen
- max: https://max.ru/id660300569233_biz
- phone: +7 993 574-83-22

## Season

YEKT autumn 2026-09-26 — no winter pipe-freeze hero; optional note that autumn turnover between guests is high.

Output: research-notes.md with research_date 2026-09-26, source_table (accessed_at today), writer_safe_urls, reader_problem, reader_outcome, practical_facts, constraints, voice_angle, surprising_fact if sourced, wordstat_stickers, NO h2_outline/lead/FAQ skeleton.
