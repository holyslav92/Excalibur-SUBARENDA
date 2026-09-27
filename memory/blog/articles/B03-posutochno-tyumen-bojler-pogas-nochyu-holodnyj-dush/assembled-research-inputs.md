# Assembled inputs for Derouter research synthesis — B03

research_date (today_iso): 2026-09-27
topic_id: B03
tenant: Добрый дом, Тюмень, посуточная аренда
primary_query: посуточно тюмень бойлер погас ночью холодный душ

## Scout handoff (2026-09-27)

- klyshin_hook: utilities_counters → angle: guest night without hot water (boiler/shower), not utility meter readings
- external_signal: guest infrastructure failure night one; contrast warm host check before check-in
- signal_urls: https://t.me/klyshin_A , https://dzen.ru/holyslav , https://добрыйдом-72.рф/blog/ , https://t.me/Dobriy_dom_72
- wordstat P0: «квартиры посуточно тюмень» 9212 RU225; «снять квартиру посуточно в тюмени» 3175 RU225
- title_draft / dzen: case with time 23:10, boiler failure after check-in to short-term rental

## Article case angle (Writer scenario — not a news claim)

Guest checked into a Tyumen short-term rental; at 23:10 the water heater (boiler) stopped heating; shower ran cold; host replied to wait until morning. Contrast: card/listing promises shower and towels; first night hygiene and sleep quality at stake.

## Anti-dup (published titles only)

- B01: contactless check-in wrong code
- B02: deposit not returned, chip on stove
Do not re-tell those plots.

## Wordstat MCP live (regions 55, 11176, 225) — accessed 2026-09-27

Phrase «квартиры посуточно тюмень» totalCount 9212; top: same 9212, «снять квартиру посуточно в тюмени» 3175, «квартиры посуточно тюмень недорого» 956, avito variants 659/482, без посредников clusters 489–287.

Phrase «снять квартиру посуточно в тюмени» totalCount 3175; top mirrors above; «сколько стоит снять квартиру посуточно в тюмени» 11.

Phrase «бойлер квартира аренда» — API returned totalCount 13 only (no phrase list). WORDSTAT PARTIAL for this cluster.

Phrase «горячая вода квартира» totalCount 33504; top buyer-adjacent: «в квартире нет горячей воды» 2715, «как включить горячую воду в квартире» 1001, «отключение горячей воды в квартире» 1498, temperature/norm queries — mostly long-term resident intent, not posutochno; use only as background for “no hot water” pain language.

Interpretation: demand cluster is Tyumen posutochno search; hot-water/boiler is narrow — article must hook on posutochno stay + night-one infrastructure, not ЖКХ norms essay.

## Fresh signal this week (required)

**ProГород NN, 25.09.2026** — «Сантехник поставил точку… выключать бойлер на ночь или оставлять включенным»
URL: https://progorodnn.ru/news/160533
Facts: working storage heater cycles via thermostat; overnight shutoff saves little if guest needs evening/morning hot water; timer useful for tariff scheduling; do not store water at 30–40°C long (microbes); turn off for repair, faults (burning smell, sparks, leak, shock, breaker trips), long absence; maintenance (scale, anode) affects consumption more than nightly off switch.

## Tyumen city context (not same as broken boiler in flat)

**Тюменский курьер, 19.06.2026** — «Холодный душ по расписанию»
URL: https://tm-courier.ru/2026/06/19/holodnyj-dush-po-raspisaniyu/
Facts: USTEC press — stage 3 hydraulic tests; hot water absent at 1540 objects in parts of Tyumen (Mayak, Dom oborony, Zarechny, center) for ~two weeks while testing 216 km networks. Distinguish: city-wide planned GVS shutdown vs in-apartment boiler/thermostat failure at 23:10.

## Community / forums / Q&A

**Pravoved.ru Q3717476** (question 25.05.2023, Moscow — long-term relevance for posutochno guest rights framing)
URL: https://pravoved.ru/question/3717476/
Facts: rented flat for one day (posutochno); no hot water, no warning; host did not answer; could not wash; lawyer advises written claim with demands, proof of delivery; court if ignored. Not legal advice in article — “save messages, document time, written demand” level only.

**Woman.ru thread** (forum, accessed via search snippet 2026-09-27; direct fetch 428)
URL: https://www.woman.ru/home/economy/thread-boyler-v-kvartire-kak-osnovnoy-istochnik-goryachey-vody-id6413072/
Facts: renters reject flats where tiny boiler is only GVS source; ~15 minutes hot water complaint; commenters note 50L often insufficient vs 100L+ for shower; sometimes boiler only during summer city shutdown. Subjective forum, not Tyumen-specific.

**Otzovik review summary** (fetch blocked by bot wall 2026-09-27)
URL: https://otzovik.com/review_16654410.html
Facts from search index: Yaroslavl short stay during building GVS outage; host warned in Sutochno chat; temporary flow heater workaround; weak pressure/temperature tradeoffs. Use as pattern “warn before booking / workaround”, not as Tyumen stat.

## SERP snippets (research-serp.json, searched 2026-09-27) — patterns only, do not copy Dzen prose

- Listings filter «бойлер водонагреватель» on Avito Tyumen posutochno — hosts advertise boiler as amenity.
- Tenant Dzen URLs in SERP describe late check-in + cold shower + host says “turn on boiler, wait 40 minutes” — same pain family as B03 case (different plot details).
- tyumen.sutochno.ru, marketplace aggregators in cluster.

## Tenant CTA (writer_safe, no invented SLA)

From tenant-config: https://t.me/Dobriy_dom_72 , https://t.me/Dobriy_dom_Tyumen , https://max.ru/id660300569233_biz , https://добрыйдом-72.рф/booking/ , tel +79935748322
Blog interlink context (site fetch 500 on 2026-09-27): https://добрыйдом-72.рф/blog/
Published sibling slugs for interlink if relevant: B01 beskontaktnoe-zaselenie; B02 zalog cleaning — only contextual outbound per pipeline.

Internal paths mentioned in tenant content canon (verify on site): /chto-vhodit-v-stoimost-kvartiry-posutochno-polnyj-spisok-uslug/ , /pravila-prozhivaniya-v-otele-chto-proverit-do-oplaty-chtoby-ne-poteryat-dengi/

## official_verifications

NOT_REQUIRED — no bank tariff or gov fee digits as article thesis. PP RF 354 mentioned only on Pravoved in long-term GVS context; do not teach ЖКХ перерасчёт as main posutochno guest remedy without lawyer.

## Constraints for Writer

- Do not promise Добрый дом has 24/7 plumber, specific boiler volumes, or response minutes unless confirmed in live object listing/chat.
- Separate: (A) city summer GVS shutdown, (B) host forgot to enable boiler before guest, (C) equipment fault at night, (D) undersized boiler for family shower.
- Host “wait until morning” after 23:10 fault = communication/process failure; working boiler normally may need 30–60+ minutes reheat after full drain depending on volume (Eddison 30L review: ~1.5 h first heat — from Otzovik product review index, not posutochno).
- Do not use neighbor research-notes as prose template.
- No h2 outline, no lead paragraph, no FAQ skeleton in output.

## Output format required in research-notes.md

YAML-style header fields: research_date, topic_id, tenant
Sections: reader_problem, reader_outcome, practical_facts (bullets), constraints, voice_angle, surprising_fact (if sourced), source_table (markdown table with accessed_at 2026-09-27 on every row), writer_safe_urls, wordstat_stickers (5 phrases with counts from live data above), optional official_verifications if empty say NOT_REQUIRED

Derouter: synthesize in Russian, factual tone, internal reference for Writer/Sol only.

## CRITICAL — response shape for this API call

You are already running inside `excalibur_blog_derouter_opus_chat.py --role research`. Do NOT tell the user to run the script again. Do NOT refuse synthesis.

Your **entire** assistant message must be **only** the complete `research-notes.md` document (markdown), matching B01/B02 section structure: header fields, reader_problem, reader_outcome, practical_facts, constraints, voice_angle, surprising_fact, source_table (every row accessed_at 2026-09-27), writer_safe_urls, wordstat_stickers, official_verifications (NOT_REQUIRED). Minimum ~80 lines of useful facts. No h2 article outline, no lead, no FAQ.
