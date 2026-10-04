# Assembled research inputs — B44 — 2026-10-04 YEKT

## Meta
- topic_id: B44
- research_date: 2026-10-04
- format: guest CASE, Tyumen short-term rental only
- NOT legal Klyshin / NO EGRN storyline
- Scout hook (editorial mechanics): deposit_before_keys | original: «Сначала проверка. Потом перевод. Не наоборот.»
- Composite editorial case (no verified booking ID): in chat «залог 3 000 ₽»; on payment screen bank holds/blocks 11 400 ₽; check-in code not sent yet
- angle_rotation: NOT B34 (cash zalog at door), NOT B02 (return after damage), NOT B32-only (commission stack without hold), NOT B40 (transfer before code)
- overlap: B34 bez zaloga u dveri, B02 zalog return, B32 checkout total, B30 card hold after checkout

## Wordstat MCP-KV live 2026-10-04
- «квартира посуточно залог» regions 55+11176: totalCount 22 (top: квартира посуточно залог 22; квартиры посуточно без залога 5)
- «квартиры посуточно тюмень» 55+11176: totalCount 3963
- «посуточно комиссия» RU 225: totalCount 1769 (top: авито посуточно комиссия 991)
- «залог посуточно вернут» RU 225: totalCount 110 (top: не вернули залог за квартиру посуточно 31)
- «не вернули залог за квартиру посуточно» RU 225: totalCount 31
- Scout handoff P0 spine: «квартира посуточно залог» 17 (55) — minor drift vs live 22; use live 22

## Fresh community signals (this week)
- https://t.me/s/Dobriy_dom_72 — early Oct 2026 posts:
  - «Без комиссии» в фильтре — на экране оплаты +1 187 ₽ комиссия сервиса (4200×2 nights guest math); хозяин: «комиссия площадки»; урок: считать итог экрана, не только чат/ночь
  - 3 Oct 2026 «Выходные с мамой» — бронь заранее, бесконтактный заезд
  - 3 Oct «5 минут в квартире: батарея, окно, горячая вода» — проверка после входа
- https://t.me/s/klyshin_A — active channel; recent posts are long-form real estate/legal consumer topics, NOT a verified Tyumen deposit-hold transcript. Hook is Scout topic-bank only.

## SERP noise (ignore for case)
- Primary SERP polluted with «заморозка вкладов 2026» — NOT guest topic

## Live source facts (accessed 2026-10-04)

### Sutochno.ru official
- help/gosti/safety: prepay only via sutochno.ru; amount must match booking; no extra payments between prepay and check-in; host cannot demand off-platform prepay
- sj/iz-chego-skladivaetsya-stoimost (10 Dec 2025): guest sees full booking sum; cleaning and extra guests in calculation; **no separate guest commission** beyond host price; prepay 15–100%
- blog/rules: host must list standard/season prices, extra guests, **insurance deposit (страховой депозит)**, cleaning — amounts guest will pay; guests refuse when real price exceeds expected
- Superguest status mentions possibility to check in without deposit (platform program) — not universal

### Hold vs charge (payment explainer, not bank tariff)
- Yandex Pay blog (updated 12 Feb 2026): preauthorization = temporary block without final debit; capture later or unblock; client sees held sum in statement; if business does not confirm debit, hold lifts and funds return; **typical hold several days; in some cases up to ~30 calendar days depending on issuer bank rules** — do NOT cite as specific Sber/Tinkoff tariff
- Directline.pro zalog article (7 Aug 2026): deposit ≠ prepay; prepay counts toward stay, deposit returns after checkout if no damage; **hold/freeze** described as industry pattern for online deposit (vendor RealtyCalendar example) — money frozen on guest account until stay ends; warn guest before booking
- B30 prior research referenced Bronevik industry blog on preauth for deposits — same class of fact

### Distinction for B44 wound
- Guest pain: messenger promised small **deposit** (3 000 ₽) but **payment page authorization** shows much larger **11 400 ₽** before keys/code — fear: is it all gone? is it rent+deposit+fees stacked? why pay before code?
- 11 400 ₽ is title anchor only — do not invent formula unless shown on hypothetical screenshot; example decomposition for internal writer only: could equal stay+fees+deposit hold in one authorization line on some gateways (platform-dependent)
- **Hold ≠ списание**: available balance drops; not necessarily merchant received all yet
- Code not sent yet amplifies risk feeling (B18/B22 adjacent but B44 is **amount on card before access**)

### Constraints
- No specific bank %/commission digits
- No claim incident happened at Dobriy Dom or named aggregator
- Avito legal page blocked from cloud IP — use Wordstat avito commission cluster + Dobriy post as behavior signal, not Avito tariff table
- Not legal advice; not Klyshin EGRN content

## writer_safe_urls (tenant + scout)
- https://t.me/Dobriy_dom_72
- https://t.me/Dobriy_dom_Tyumen
- https://max.ru/id660300569233_biz
- https://добрыйдом-72.рф/
- https://добрыйдом-72.рф/booking/
- https://t.me/klyshin_A
- https://sutochno.ru/help/gosti/safety
- https://sutochno.ru/sj/iz-chego-skladivaetsya-stoimost-bronirovaniya
- https://sutochno.ru/blog/rules
- https://pay.yandex.ru/blog/articles/holdirovanie-platezhey-dlya-biznesa
- https://www.directline.pro/connect/p/zalog-pri-sdache-kvartiry-posutochno/

## Derouter instruction
Output ONLY complete `research-notes.md` body in Russian using section headers matching B30/B43 canon:
# research_date
# reader_problem
# reader_outcome
# practical_facts
# constraints
# typical_errors
# voice_angle
# surprising_fact
# fresh_signal_note
# wordstat_stickers
## official_verifications
# source_table
# writer_safe_urls

No h2_outline, no lead, no FAQ. No shell instructions. No BLOCKER text.
