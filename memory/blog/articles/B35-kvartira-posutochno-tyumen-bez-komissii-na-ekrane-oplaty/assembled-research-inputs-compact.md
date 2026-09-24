# B35 research compact input for Derouter (2026-09-24, Asia/Yekaterinburg)

Write **only** `research-notes.md` sections in Russian. No BLOCKER, no shell, no h2/lead/FAQ/action_outline.

**CASE (Tyumen guest-night, Avito-style travel checkout):** Guest filtered short-term listings with **«без комиссии»** (or «цена как у хозяина»), picked a Tyumen flat, saw nightly/card price that looked final enough to compare with hotel. On the **last in-app payment screen** before confirm, a separate line appeared — **«комиссия сервиса» +1 187 ₽** — and the payable total jumped. Money stays **inside official checkout**, not a host chat «переведите ещё раз» (B33) and not a door zalog (B34). Klyshin hook (editorial mechanics): «В карточке написали „без комиссии“. На последнем шаге оплаты сервис всё равно добавил строку — и сумма выросла.» **Anti-dup:** not B32 (3400/ночь vs 8816 итог за две), not B33 (duplicate prepay off-platform), not B34 (filter «без залога» vs card at door).

**lockpick_question (from Scout):** «Где в карточке строка про комиссию сервиса и можно ли увидеть итог до брони?»

**verdict (Scout):** Сначала открыть полный расчёт и увидеть строку комиссии платформы, потом сравнивать варианты по **итоговой сумме за весь срок**. Цена в фильтре — ещё не цена проживания.

**reader_problem:** Выбрал «без комиссии» в Тюмени, сравнил варианты по цене в выдаче/карточке; на подтверждении оплаты увидел +1 187 ₽ сервисной строкой и не понял, успел ли сравнить честный итог с отелем/другой квартирой.

**reader_outcome:** Понимает, что фильтр «без комиссии» ≠ обещание нулевого сбора платформы на checkout; отличает **комиссию сервиса в расчёте** от залога, уборки, доплаты хозяину и второго перевода; перед «Оплатить» раскрывает **полный расчёт** и сравнивает **итог за даты**, а не только ₽/сутки; сохраняет скрин фильтра + экран оплаты; при расхождении — поддержка площадки, не повторная оплата в чат.

**Wordstat (mcp-kv live 2026-09-24, regions 55+11176 / 225):**
- «квартиры посуточно тюмень» — **4274** (55+11176); top: «снять квартиру посуточно в тюмени» 1208; «авито квартиры посуточно тюмень» 311
- «авито посуточно комиссия» — **1024** (225); supporting: «сколько комиссия авито посуточно» 227; «комиссия авито за бронирование квартиры посуточно» 18
- «квартиры посуточно без комиссии» — **314** (225); single cluster, weak alone — Scout kept Tyumen spine + commission sub-angle

**practical_facts:**
- SERP Tyumen (research-serp 2026-09-24): Avito посуточно URL + copy «снять посуточно **без комиссии**… фильтры и сортировка»; Яндекс Недвижимость категория `…/posutochno-i-bez-komissii/` («1581 объявление» в сниппете) — marketing/filter intent «без комиссии», not a guarantee about every line on payment screen.
- **1 187 ₽** in CASE — **composite parameter** from Scout/Klyshin beat; no verified public screenshot or booking ID in research; do not present as universal Avito tariff.
- Official **host-side** commission (not the same label as guest «комиссия сервиса»): host.avito.com/season-2026 — базово **20%**, **17%** после советов 1 уровня, **15%** после 1+2; host.avito.com/release-q1-2026 — с **8 апреля 2026** комиссия по заявкам до **20%**, снижение до **17%** при мгновенном бронировании.
- host.avito.com/release-q1-2026: уборка — либо «**включено в цену**», либо «**отдельной строкой**» в бронировании; цель — гость видит **итоговую стоимость** (parallel UX lesson: checkout may add lines beyond ₽/ночь).
- host.avito.com/course/lesson-3 (2026-09-24 fetch): комиссия Авито за онлайн-бронирование удерживается из платежа гостя; размер **предоплаты** хозяин настраивает (33/50/100% и т.д.); **запрет** просить гостя платить **напрямую** / уходить с площадки — контраст с **легальной** строкой сервиса **внутри** checkout.
- Avito Журнал (WebSearch snapshot 2026-09-24, journal booking instruction): гость вносит **предоплату через Авито Путешествия** (СБП/карта), «оплачивайте бронирование **только внутри сервиса**»; фильтры по цене/условиям, отдельного акцента «без комиссии» в инструкции нет — гость должен дойти до шага оплаты.
- avito.ru/legal/promo/best-price-travel/ (search snippet): промокод = скидка на **«услуг организатора»** на сервисе; правила бронирования → avito.ru/legal/realty_rules/online-booking (direct fetch from Cloud **IP-blocked** 2026-09-24 — cite URL, no invented quote).
- Distinct beats: **B33** — второй перевод **мимо** checkout; **B35** — первый платёж **в** checkout, но итог выше обещания фильтра; **B32** — арифметика ночей/срока, не отдельная «комиссия сервиса».
- Dobry Dom tenant: прямое бронирование позиционирует «**без комиссий агрегаторов**» vs Avito/агрегаторы (channel post 2026-09-24) — контекст альтернативы, не доказательство суммы 1187 ₽.

**constraints:** Composite case; no invented Klyshin channel quote (hook = Scout editorial); **1187 ₽** only as case parameter; host **%** only from official_verifications; do not call host fraudster; Tyumen guest-night CASE not legal/consumer guide; avito.ru main/legal pages may be IP-blocked — mark fetch limits in source_table; not B33/B34/B32 body reuse.

**voice_angle:** Phone in hand: filter «без комиссии» in search vs payment sheet with «комиссия сервиса»; calm «итог другой» before comparing with hotel.

**surprising_fact:** RU Wordstat **1024** on «авитo посуточно комиссия» vs **314** on «квартиры посуточно без комиссии» — guests search both «without commission» listings and «Avito commission» in the same market.

**fresh_signal_note (week of 2026-09-24):**
- **t.me/s/Dobriy_dom_72** accessed **2026-09-24**: свежие посты (04:06–09:27): продление/цена при спросе; **«несоответствие… гость проверяет только цену и район, детали после оплаты»**; **«прямые цены без комиссий агрегаторов»** на сайте vs агрегаторы; «не переводите повторно» / карта неизвестному — соседние safety beats, не цитата про 1187 ₽.
- **t.me/s/klyshin_A** feed active **2026-09-24** (timestamps ~04:40); rental checkout hook **не** verified as channel post text — Scout/Klyshin editorial for B35.
- Scout signal_urls: t.me/klyshin_A, dzen.ru/holyslav

**official_verifications table rows (required for host % and product rules):**
| Avito host commission tiers season 2026 | арендодатель | 20% / 17% / 15% | https://host.avito.com/season-2026 | 2026-09-24 | yes |
| Commission increase from 8 Apr 2026 + instant booking 17% | арендодатель | до 20%; 17% with instant book | https://host.avito.com/release-q1-2026 | 2026-09-24 | yes |
| Cleaning fee may appear as separate booking line | гость/хозяин (UX) | отдельная строка или в цене | https://host.avito.com/release-q1-2026 | 2026-09-24 | yes |
| Host must not take payment off-platform | гость | запрет прямой оплаты | https://host.avito.com/course/lesson-3 | 2026-09-24 | yes |
| Online booking rules hub | гость | entry point terms | https://www.avito.ru/legal/realty_rules/online-booking | 2026-09-24 | partial (IP block, URL only) |

**source_table:** each row `accessed_at: 2026-09-24`; types: official, community, wordstat, serp, media; include mcp-kv wordstat rows.

**writer_safe_urls:** https://t.me/Dobriy_dom_72, https://t.me/Dobriy_dom_Tyumen, https://max.ru/id660300569233_biz, https://добрыйдом-72.рф/booking/, https://добрыйдом-72.рф/, https://t.me/klyshin_A, https://www.avito.ru/tyumen/kvartiry/sdam/posutochno/-ASgBAgICAkSSA8gQ8AeSUg, https://realty.yandex.ru/tyumen/snyat/kvartira/posutochno-i-bez-komissii/, https://host.avito.com/season-2026, https://host.avito.com/release-q1-2026, https://host.avito.com/course/lesson-3, https://www.avito.ru/journal/articles/kak-zabronirovat-zhilyo-na-avito-onlayn-podrobnaya-instrukciya, https://www.avito.ru/legal/realty_rules/online-booking, https://www.avito.ru/legal/promo/best-price-travel/, https://dzen.ru/holyslav
