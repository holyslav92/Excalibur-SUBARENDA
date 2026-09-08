# Assembled research inputs — B14

**Return ONLY research-notes markdown in response; do NOT return DEROUTER RESEARCH BLOCKER.**

Live fetch, Wordstat MCP-KV, Telegram dates and URL checks are already done by the conductor. Use the facts below as-is; do not refuse synthesis.

research_date: 2026-09-08
topic_id: B14
tenant: Добрый дом, посуточная аренда Тюмень
hook_id: neighbors_night
format: CASE, 700–1100 слов

## Scout handoff summary

- Title draft: «Написали «тихий дом». В 23:40 соседи включили музыку»
- Klyshin hook: neighbors_night | original: «В объявлении тихо. В 23:00 за стеной — вечеринка»
- Angle: гость внутри; хост обещал «тихий дом»; в 23:40 музыка за стеной; стук в дверь; moral: сначала этаж/соседи/правила, потом оплата
- dzen_pattern: 2 (case_with_sums_and_dates)
- Wordstat P0: «квартиры посуточно тюмень» 5220 (55+11176) / 11084 (225)
- Wordstat rework: «соседи шум посуточно» 2 (partial); «шум соседей» 240; «аренда квартиры посуточно» 710; «аренда квартир посуточно тюмень» 183
- signal_urls: https://t.me/klyshin_A, https://добрыйдом-72.рф/blog/, https://t.me/Dobriy_dom_72
- Case spine: 2 ночи ~8 400 ₽; сентябрь 2026; хост берёт конфликт в чат
- Anti-dup: B12 = внешний шум (стройка/дорога, «тихий центр»); B14 = соседи через стену, вечеринка 23:40. NOT legal EGRN guide.

## Overlap check (published-titles-only)

Already covered: B01–B13 (see published-titles-only.md). B12 «тихий центр» + кран/стройка за окном — другой источник шума. B14 = обещание «тихий дом» + соседи-вечеринка через стену.

## Meta

- topic_id: B14
- research_date: 2026-09-08
- tenant: Добрый дом, Тюмень, посуточная аренда
- case_angle (Scout): ночь без сна в посуточной Тюмень; обещание «тихий дом»; соседи-вечеринка в 23:40; хост берёт конфликт в чат; 2 ночи ~8 400 ₽; сентябрь 2026
- klyshin original hook: «В объявлении тихо. В 23:00 за стеной — вечеринка»
- moral for Writer: сначала этаж/соседи/правила дома, потом оплата — НЕ юридический гайд по ЕГРН
- anti-dup: B12 = внешний шум (стройка/дорога за окном, «тихий центр»); B14 = соседи через стену, музыка в 23:40. Не смешивать.

## Wordstat (MCP-KV, regions 55+11176, accessed 2026-09-08)

| phrase | volume | note |
|--------|--------|------|
| квартиры посуточно тюмень | 5220 | Scout P0 final |
| снять квартиру посуточно в тюмени | 1689 | top child |
| шум соседей | 240 | niche, complaint intent |
| соседи шум посуточно | 2 | totalCount-only partial |
| аренда квартиры посуточно | 710 | parent cluster |
| аренда квартир посуточно тюмень | 183 | localized |

Demand: broad Tyumen short-term rental; neighbor-noise phrases weak alone — article stays guest CASE not legal FAQ.

## Fresh signals this week (2026-09-01 — 2026-09-08)

### S-FRESH-1: МегаТюмень — часы тишины
- URL: https://megatyumen.ru/obshestvo/chasy-tishiny-v-tyumeni-chto-zapresheno-kogda-i-komu-zhalovatsya/
- Published: 2026-09-03 16:29
- Source type: regional news (this week)
- Key facts: будни 22:00–08:00; выходные 22:00–09:00; дневной тихий час 13:00–15:00; штрафы гражданам 1 000–2 000 ₽; полиция 102/112; УК не может штрафовать
- Relevance: свежий сигнал недели; 23:40 = нарушение в будни; гость может ожидать, что «позвонят в УК» — но УК не уполномочена

### S-FRESH-2: Telegram @Dobriy_dom_72 — тишина в описании
- URL: https://t.me/Dobriy_dom_72 (forwarded «Добрый Контент»)
- Accessed: 2026-09-08
- Source type: tenant community
- Key quote: «заявлена тишина, а окна выходят на шумную дорогу» — гость замечает после оплаты
- Relevance: ecosystem signal про слово «тишина» в объявлении; B14 = соседи за стеной, не дорога (отличать от B12)

### S-FRESH-3: Telegram @Dobriy_dom_72 — шум не на фото
- URL: https://t.me/Dobriy_dom_72
- Accessed: 2026-09-08
- Key quote: «шум, которого не видно на фото» — проверять район и отзывы до брони
- Relevance: до оплаты спросить про соседей/этаж

### S-FRESH-4: tyumen-info.ru — памятка администрации
- URL: https://tyumen-info.ru/society/2026/08/24/36154.html
- Published: 2026-08-24
- Source type: regional news (city admin repost)
- Key facts: те же часы тишины по Закону ТО №3; УК/ТСЖ не наделены полномочиями штрафовать
- Relevance: подтверждение региональных норм

## Fresh signals this week (required)

1. **megatyumen.ru** — «Часы тишины в Тюмени: что запрещено, когда и кому жаловаться», published **2026-09-03 16:29**. Regional media reminder: Tyumen quiet hours, fines, police 102/112, UK cannot fine. Fresh news this week.

2. **tyumen-info.ru** — «О соблюдении тишины и покоя граждан в Тюмени: подробная памятка», published **2026-08-24** (city admin repost). Same law refs; UK/ТСЖ not empowered to fine.

3. **Telegram @Dobriy_dom_72** (tenant channel, accessed 2026-09-08): forwarded post from «Добрый Контент» — «Несоответствие квартиры описанию… заявлена тишина, а окна выходят на шумную дорогу» — ecosystem signal that «тишина» in listing ≠ reality; guest notices after payment. Related angle, B14 differs (neighbors through wall, not street).

4. **Telegram @Dobriy_dom_72** (same scrape): «Рядом — не адрес, а маршрут… шум, которого не видно на фото» — check district/reviews before booking.

5. Scout signal_urls: https://t.me/klyshin_A , https://добрыйдом-72.рф/blog/ , https://t.me/Dobriy_dom_72

## Tyumen quiet law (official + regional, for guest context only — NOT article spine)

**Закон Тюменской области от 29.03.2022 № 3** (tyumen-pravo.ru, accessed 2026-09-08):
- Weekdays quiet: 22:00–08:00
- Weekends/holidays: 22:00–09:00
- Daily daytime quiet hour: 13:00–15:00
- Prohibited: loud TV/radio/music devices, screams, musical instruments, construction noise, etc.
- Responsibility via КоАП ТО (article 1.1): citizens warning or fine 1 000–2 000 ₽ (construction up to 5 000 ₽)

**At 23:40 on Tuesday 2026-09-08** (weekday): music through wall = inside legally protected quiet period (since 22:00).

**Police** 102/112 — authorized to record violations (megatyumen, tyumen-info). **UK/ТСЖ** — cannot issue fines or stop noise by force; may inform only.

## Guest pain — short-term rental specifics (NOT permanent resident guide)

- Guest chose object for 1–2 nights; cannot «договориться с соседями годами».
- Listing said «тихий дом» / «тихо» — subjective; photos and star rating do not show adjacent apartment behavior.
- Reviews rarely mention «соседи за стеной» unless previous guest complained.
- Temporary guest has less social capital: knocking on stranger's door at night is stressful; calling police from rented flat feels extreme for many.
- Host/manager who knows building should be first line: contact neighbor, УК, or guide guest — case angle says host takes conflict into chat.
- Guest cannot easily «съехать» at 23:40 without losing money and sleep; 2 nights ~8 400 ₽ is editorial case sum (Scout), not market average.
- Party noise often = bass through slab/wall; guest may hear vibration more than melody.
- Floor matters: middle floors hear neighbors above and beside; ground floor may hear entrance hall; host should know typical complaints for that entrance.
- Before payment guest can ask host: which side neighbors, any party flats, house rules on quiet hours, recent complaints — answers should be concrete not «у нас всегда тихо».
- Distinguish: street/traffic noise (B12) vs adjacent apartment party (B14).

## Practical facts from platforms / media (context)

- **Яндекс Аренда journal** (arenda.yandex.ru, updated 2026-04-27): short-term renters can leave if unhappy but moving is costly; noise includes music, shouts; regional quiet hours differ; phone sound meter apps help document but are not court-grade; first step often talk to neighbors, night noise → police.
- **Т—Ж** (t-j.ru/xuanzang/, 2026-01-18): when neighbors rent to noisy tenants, police call during active noise most effective; owner may be fined if police confirm; collective complaints stronger — written for permanent residents, not guests, but shows owner responsibility when flat is sublet.
- **Harant.ru** — consultative Q&A only, not official authority; mentions owner duties under ЖК — use cautiously, no legal promises in article.

## Editorial case boundary (Scout)

- Guest inside rented flat, first night, ~23:40, music from neighboring apartment «на полную».
- Had been promised «тихий дом» in chat or listing.
- Possibly knocked neighbor door — uncertain outcome; host active in messenger.
- 2 nights, ~8 400 ₽ total — editorial reconstruction, mark if used.
- September 2026, Tyumen, weekday evening.
- Do NOT invent: address, ЖК name, flat number, booking platform, host name, exact song volume dB.
- Do NOT open with EGRN / inheritance / legal term dump.

## Constraints

- Guest pain focus: sleep ruined, trust in «тихий дом» broken, what to ask before paying.
- Tyumen localization only.
- Not a «куда жаловаться» encyclopedia; law facts as background only.
- No bank/developer tariffs — official_verifications empty.
- writer_safe_urls from tenant: t.me/Dobriy_dom_72, t.me/Dobriy_dom_Tyumen, max.ru/id660300569233_biz, добрыйдом-72.рф/booking/, добрыйдом-72.рф/blog/

## surprising_fact (if sourced)

- УК в Тюмени не может оштрафовать шумного соседа — только полиция (megatyumen 2026-09-03, tyumen-info 2026-08-24). Guest expecting «позвонить в УК и чтобы прекратили» may be disappointed.

## voice_angle

- One night CASE: chat with host at 23:40, not police instruction list.
- Contrast: обещание тишины vs реальность за стеной.
- Moral: уточнить этаж, соседей, правила дома до оплаты.

## source_table rows for Derouter to embed (accessed_at = 2026-09-08)

| id | type | title | url | accessed_at | use |
|----|------|-------|-----|-------------|-----|
| S1 | news | Часы тишины Тюмень | megatyumen.ru/.../chasy-tishiny... | 2026-09-08 | fresh week |
| S2 | news | Памятка тишина Тюмень | tyumen-info.ru/.../36154.html | 2026-09-08 | regional |
| S3 | official | Закон ТО №3 тишина | tyumen-pravo.ru/zakon/2022/03/29/n-3/ | 2026-09-08 | quiet hours |
| S4 | community | TG Добрый дом тишина в описании | t.me/Dobriy_dom_72 | 2026-09-08 | tenant signal |
| S5 | community | TG шум не видно на фото | t.me/Dobriy_dom_72 | 2026-09-08 | tenant signal |
| S6 | media | Яндекс Аренда шумные соседи | arenda.yandex.ru/journal/post/shumnye-sosedi... | 2026-09-08 | mechanics |
| S7 | media | Т—Ж сдают шумным | t-j.ru/xuanzang/ | 2026-09-08 | owner context |
| S8 | wordstat | MCP-KV volumes | internal | 2026-09-08 | demand |
