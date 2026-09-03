# DEROUTER TASK — output ONLY research-notes.md body

Write the complete `research-notes.md` file in Russian as raw markdown.
Rules:
- Start with `# research-notes.md` then YAML-style bullet metadata (topic_id, slug, research_date).
- Include sections: reader_problem, reader_outcome, practical_facts, constraints, case_material_status, tyumen_local, wordstat_summary (table), source_table (table with accessed_at 2026-09-03), official_verifications (N/A if no bank tariffs), writer_brief, voice_angle, surprising_fact, writer_safe_urls.
- NO preamble, NO "DEROUTER BLOCKER", NO explanation of your process, NO h2_outline, NO lead, NO FAQ.
- Facts only from inputs below; mark collective case as editorial.

---

# Assembled research inputs — B09

**research_date:** 2026-09-03  
**topic_id:** B09  
**slug:** snyal-kvartiru-posutochno-sozvon-v-10-00-wi-fi-ne-tyanet  
**title_draft:** Снял квартиру посуточно. Созвон в 10:00 — Wi-Fi не тянет  
**market:** посуточная аренда, Тюмень, командировочный гость  
**season:** сентябрь 2026, ранняя осень, НЕ зима  

## Scout / Klyshin handoff

- **hook_id:** `sept_business_trip`
- **original hook:** Звонок в 10:00. Заселился в 22:00. Стол, розетки, Wi‑Fi на созвон, закрывающие — до оплаты.
- **angle:** Guest on business trip; Wi‑Fi speed fails morning video call; host promised "есть интернет".
- **klyshin window:** 2026-08-29 — 2026-08-31 (queue slot)
- **signal_urls:** https://t.me/klyshin_A
- **final P0:** квартиры посуточно тюмень — 5320 (regions 55+11176)
- **guest sub-cluster:** Wi‑Fi / интернет для созвона при посуточной аренде
- **rework:** weak «командировка» alone (69 RU) → localized Tyumen spine + Wi‑Fi pain

## Published overlap (titles only — do NOT duplicate angles)

- B01: wrong door code / contactless check-in
- B02: deposit not returned / scratch on stove
- B03: «near university» distance lie
- B04: extra guest fee at door
- B05: fake reviews / rating 4.8
- B06: checkout time vs train, luggage
- B07: kitchen promised vs eating in cafes
- B08: prepayment silence before check-in

**B09 focus:** Wi‑Fi speed/reliability for morning work call after late check-in — NOT prepayment, NOT codes, NOT deposit, NOT kitchen, NOT checkout.

## Wordstat MCP-KV (live, accessed 2026-09-03)

| phrase | region | volume | top related |
|--------|--------|--------|-------------|
| квартиры посуточно тюмень | 55+11176 | 5320 | снять квартиру посуточно в тюмени 1681; недорого 418; без посредников 371; авито 338 |
| снять квартиру посуточно в тюмени | 55 | 1134 | недорого 233; без посредников 150; центр 21 |
| квартира посуточно командировка | 225 | 69 | only self-phrase in top |
| уборка посуточных квартир | 225 | 1951 | вакансии 755; host-side demand signal |

## Fresh signals (week of 2026-08-27 — 2026-09-03)

### 1. Klyshin Telegram — sept_business_trip (community, Aug 29–31 window)
- Hook: business traveler needs desk, outlets, real Wi‑Fi for calls, closing documents BEFORE payment.
- Moral angle from bank: verify work setup before money, not after keys.

### 2. Newsler.ru — 27 августа 2026, 10:00 (news)
- URL: https://www.newsler.ru/travel/2026/08/27/kak-vybrat-kvartiru-posutochno-i-udachno-zaselitsya
- Practical guide: inspect apartment in first minutes; check what you need first (bedding, towels, dishes, sleeping place).
- If something missing — message host immediately.
- Smell of damp, cold radiator, slow drain — evaluate concrete fix timeline, not promises.
- Does NOT mention Wi‑Fi specifically but supports «check essentials on arrival, not from photos».

### 3. NEWS.ru — 29 августа 2026 (news)
- URL: https://news.ru/society/pochemu-ne-rabotaet-mobilnyj-internet-29-avgusta-prichiny-sboi-v-rossii
- Mobile internet outages in dozens of Russian regions Aug 29; users can't load video, apps unstable.
- Regions named: Moscow, SPb, Novosibirsk, Krasnodar, Moscow oblast, Sverdlovsk, Samara, Nizhny, Irkutsk, Chelyabinsk.
- Reason cited: temporary restrictions for security (drone threat).
- **Relevance:** mobile hotspot backup for morning Zoom is unreliable in Aug–Sep 2026 context.

### 4. Techno-news.net — 26 августа 2026 (news)
- URL: https://techno-news.net/2026/08/26/news_58506/
- Fragmented internet instability across Russia; operator complaints MTS, Beeline, Megafon in various regions.
- Not Tyumen-specific but sets context for backup plans.

### 5. SERP community echoes (older but pattern confirmation)
- VK wall-40180261: guest rented apartment with router visible in photo but speed too low even to send email; had to find coworking urgently.
- Domclick blog blocked from fetch (anti-bot) — SERP snippet suggests: test speed at 22:10 not minute before 9:00 meeting; ask host to reboot router.

## Official / technical references (for speed thresholds)

### Zoom support (official)
- URL: https://support.zoom.com/hc/ru/article?id=zm_kb&sysparm_article=KB0060759
- 1:1 high-quality video: 600 kbps up/down
- 1:1 HD 720p: 1.2 Mbps up/down
- Group HD 720p: 2.6 Mbps up / 1.8 Mbps down
- Screen share + video thumbnail: 50–150 kbps
- Zoom adapts quality to available bandwidth

### Wi‑Fi diagnostics (editorial/technical, not legal)
- tvrts.ru article: in MDU, Wi‑Fi often worse in evening; 2.4 GHz congested; test cable vs Wi‑Fi to see if provider line OK.
- iXBT Live May 2026: router «stutters» when air crowded; Zoom freezes; full Wi‑Fi bars ≠ speed.
- Practical checks: speedtest near router vs far room; try 5 GHz if separate SSID; ethernet to laptop if port exists.

## Market / platform context

### Avito blog (official Avito domain)
- URL: https://www.avito.ru/blog/zarabatyvat-na-trendah-kak-otdyhayut-puteshestvenniki-v-rossii
- Travelers expect: clean bathroom, electricity, **Wi‑Fi** as basic amenity set.
- Business relevance: listings promise Wi‑Fi as checkbox, not Mbps.

### Avito host course
- URL: https://host.avito.com/course/lesson-1
- Describe check-in/out times, documents for business travelers in listing.
- Rules in description protect host in disputes (e.g. guest arrives 12:00 when check-in from 14:00).

### Industry blog (Tochka/reklama)
- URL: https://reklama.tochka.com/blog/posutochnaya-aranda-na-avito-i-kak-eto-rabotaet
- Guest frustration scenario: arrived tired, no Wi‑Fi or kettle — guaranteed irritation.
- Good practice: Wi‑Fi password visible, basic amenities.

## Tyumen local — coworking fallback (if apartment Wi‑Fi fails)

Aggregator kovorkingi.ru (accessed 2026-09-03):
- Multiple coworkings in Tyumen; day passes from ~350–1000 ₽/day, hourly from ~350–1000 ₽/hour depending on space.
- Workkode (wkode.co): business center near embankment; meeting rooms, webinar room; ul. Tsiolkovskogo 9.
- Catalog lists 9 coworkings; prices indicative, verify before visit.

**Use as:** guest emergency option for 10:00 call, NOT as ad for specific coworking.

## Tyumen rental market snippets (context only)

- yourenta.ru Tyumen listings: standard pitch «Wi-fi» in amenities for business travelers; check-in often 14:00, late arrival after 20:00 may need prepayment rules.
- Panda Home Tyumen site: «стабильный Wi‑Fi» for business trips + closing documents — competitor positioning, not verified speed.

## Case skeleton (editorial, collective)

- **Who:** business traveler, commandировка в Тюмень, сентябрь 2026.
- **Booking:** short-term apartment, in listing/ch chat «есть Wi‑Fi», «подойдёт для работы».
- **Timeline:** check-in ~22:00 after travel; morning video call 10:00 (MSK or local YEKT — Writer picks one and stays consistent).
- **Night:** guest assumes internet OK; maybe sees router/password sticker; doesn't run speed test (tired, late).
- **Morning:** Zoom/Teams stutters, drops at ~3 min or won't connect; speedtest shows e.g. 0.3–0.8 Mbps or high ping.
- **Host response patterns (neutral):** «перезагрузите роутер», «у всех работает», «это у вас ноутбук», silence until after call window.
- **Stakes:** work call with client/boss; may need closing documents for accounting after trip.
- **NOT in case:** fraud accusations, platform lawsuit, winter heating, wrong door code.

## Surprising facts (sourced)

1. Zoom needs only ~1.2 Mbps for 720p 1:1 — yet many «Wi‑Fi» apartments fail even that in far room or peak hours.
2. Listing «Wi‑Fi» on Avito is amenity checkbox — no Mbps guarantee in standard template.
3. Late August 2026: mobile backup for video calls unreliable in many regions (NEWS.ru Aug 29).
4. MDU evening Wi‑Fi collapse is often neighbor congestion, not «bad host internet» — but guest still needs fix by 10:00.

## Constraints for Writer

- Guest-night CASE 700–1100 words; scene at door/morning desk, not tech tutorial.
- September Tyumen, early autumn; no snow, no -30°C, no heating complaints.
- Do not duplicate B01–B08 plot devices.
- No bank tariffs / no official_verifications needed unless Writer adds bank claims.
- Do not invent specific apartment address, host name, or exact ruble rent unless marked as case detail.
- Closing documents (закрывающие) — mention as business-trip stake from Klyshin hook, don't turn into accounting guide.
- CTA channels: https://t.me/Dobriy_dom_72, https://max.ru/id660300569233_biz, https://добрыйдом-72.рф/booking/
- MAX positioning: automation with neural nets, Make, Cursor AI — not «клуб».

## writer_safe_urls

- https://support.zoom.com/hc/ru/article?id=zm_kb&sysparm_article=KB0060759
- https://www.newsler.ru/travel/2026/08/27/kak-vybrat-kvartiru-posutochno-i-udachno-zaselitsya
- https://news.ru/society/pochemu-ne-rabotaet-mobilnyj-internet-29-avgusta-prichiny-sboi-v-rossii
- https://www.avito.ru/blog/zarabatyvat-na-trendah-kak-otdyhayut-puteshestvenniki-v-rossii
- https://host.avito.com/course/lesson-1
- https://tvrts.ru/news/pochemu-v-mnogokvartirnom-dome-wi-fi-rabotaet-khuzhe-sosedskie-seti-kanaly-i-peregruzhennyy-efir/
- https://t.me/klyshin_A
- https://t.me/Dobriy_dom_72
- https://добрыйдом-72.рф/booking/
