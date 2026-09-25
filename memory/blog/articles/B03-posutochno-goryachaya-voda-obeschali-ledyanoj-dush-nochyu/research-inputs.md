# Research inputs — B03

Assembled: 2026-09-25 (Europe/Moscow), conductor live fetch + MCP-KV Wordstat
Read: `.cursor/excalibur-blog-handoff.md`, `research-context.json`, `research-serp.json`, `memory/scout/scout-inputs-B03.md`, `published-titles-only.md`

## Topic assignment
- topic_id: B03
- slug: posutochno-goryachaya-voda-obeschali-ledyanoj-dush-nochyu
- title_draft: «Написали «горячая вода есть». В 23:40 из душа — ледяная струя»
- dzen_pattern: 2 — обещание в карточке → поздний заезд и ледяной душ → хозяин про город/бойлер → цена первой ночи и проверка до заселения
- external_signal: осень 2026, Тюмень; гостевой кейс посуточной квартиры без юр-крючка; обложка — осенний свет
- Klyshin: utilities_counters | original «показания счётчиков — не переплатить ЖКХ» | rework angle: сначала проверка воды/бойлера, потом ночь

## Anti-dup (titles only)
- B01 бесконтактное заселение / код чужой двери
- B02 залог не вернули / скол на плите
- НЕ повторять ЖКХ-энциклопедию и не уходить в ЕГРН/наследство

## Scout signal_urls (verify/extend)
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## Wordstat (MCP-KV wordstat_get_top_requests, accessed 2026-09-25)

### Region 225 (Россия)
| phrase | totalCount / top line | notes |
|--------|----------------------|-------|
| в квартире нет горячей воды | 2709 | P0; top: почему в квартире нет горячей воды 659; нет горячей воды в квартире что делать 269; в съемной квартире нет горячей воды 11; **почему ночью нет горячей воды в квартире 9** |
| нет горячей воды в квартире что делать | 269 | buyer cluster |
| проточный водонагреватель или бойлер | 1286 | бойлер или проточный что лучше 945; водонагреватель проточный или бойлер в квартире 202; related «как правильно включить бойлер» in similar |

### Regions 55+11176 (Тюмень)
| phrase | totalCount | notes |
|--------|----------|-------|
| в квартире нет горячей воды | 47 | локальный объём |
| аренда квартиры в тюмени посуточно | 86 | Tyumen sticker / localize |

Handoff final P0: «в квартире нет горячей воды» 2709 RU + buyer посуточно Tyumen 86

## SERP (research-serp.json, searched 2026-09-25)
- Tenant Dzen case lines (snippets): «Горячая вода есть» в карточке; поздний заезд; ледяная струя; хозяин в чате «включите бойлер, подождите 40 минут» / «80 минут до тепла»
- otvet.mail.ru/question/269831164 — гость: в бойлере закончилась горячая вода, ледяной душ (fetch 504 today; snippet in SERP)
- community_experience VK walls — жилые жалобы на отключение ГВС (контекст города, не посуточно)

## Live web sources (accessed 2026-09-25)

### Fresh news / community this week
1. **Megatyumen 25.09.2026** — «В Тюмени ощутимо похолодало», пятница 25 сентября: днём до +14°C, к полуночи +9°C, ветер до 6 м/с; ночью ощущается холоднее. URL: https://megatyumen.ru/obshestvo/v-tyumeni-oshutimo-poholodalo-prognoz-pogody-na-pyatnicu-25-sentyabrya-2026-goda/
   - Angle for guest: после дороги в прохладную осеннюю ночь душ с ледяной водой бьёт сильнее, чем «просто нет ГВС летом».

2. **Megatyumen 11.09.2026** — ул. Рабфаковская, 2: третью неделю нет ГВС; УК «Ямал»: сломан бойлер дома, сроки до НГ; администрация подтвердила отключение водонагревателя из‑за неисправности. URL: https://megatyumen.ru/obshestvo/malenkih-detej-v-tazike-ne-namoesh-v-tyumeni-zhiteli-odnogo-iz-domov-tretyu-nedelyu-sidyat-bez-goryachej-vody/
   - Angle: в карточке квартиры «горячая вода есть» не отличает **городскую магистраль** от **домового бойлера**; гость в посуточной не живёт в чате дома.

### Tyumen GVS / city context (official + press)
3. **Тюменская область сегодня 01.09.2026** — УСТЭК досрочно завершил 7-й этап опрессовок; ГВС ограничивали 11 дней вместо 14; 355 дефектов устранено; в межотопительный период 2026 ограничения **ещё на части объектов** (30 реконструкций, 25 линейных). URL: https://tumentoday.ru/2026/09/01/v_tyumeni_dosrochno_zavershili_posledniy_etap_opressovok/

4. **tyumen-info.ru 01.09.2026** — то же по УСТЭК; ссылка на ao-ustek.ru для сроков. URL: https://tyumen-info.ru/society/2026/09/01/38449.html

5. **АО «УСТЭК» official** — сервис по адресу: если УСТЭК не отключает, причина может быть в УК/внутридомовых сетях; контакт-центр +7 (3452) 38-62-00. URL: https://ao-ustek.ru/potrebitelyam/otklyucheniya/

6. **KP.RU 20.08.2026** — Геологоразведчиков, 15: после опрессовок месяц без нормальной воды, оранжевая холодная; админ: ремонт теплотрассы до 15 сентября (контекст «обещали дату — вода всё ещё странная»). URL: https://www.tumen.kp.ru/online/news/7132233/

### Host / guest mechanics (not bank tariffs)
7. **subsived.ru** (обновлено 12.06.2026) — посуточный хост: гостю нужна предсказуемая горячая вода; если бойлер включается отдельно — памятка; честно предупредить про напор. URL: https://subsived.ru/posutochnaya-arenda-kvartiry-pravila-riski-i-rabochiy-poryadok-dlya-sobstvennika/

8. **t-j.ru long-short-rent** — для посуточной аренды гости не терпят отключение ГВС как долгосрочники; часто нужен электробойлер. URL: https://t-j.ru/long-short-rent/

9. **kvartirka.com listing** (пример рынка) — в карточке явно: «Горячая вода есть! Бойлер имеется на время отключения». URL: https://kvartirka.com/residence/406906/

## Practical angles for Writer (facts only, no H2/lead)
- Три слоя правды: (а) город/УСТЭК отключил магистраль; (б) дом/УК без бойлера; (в) в квартире есть накопительный бойлер, но выключен, пустой или предыдущий гость «съел» объём.
- Накопительный бойлер: из SERP/кейсов хоста — ожидание **40–80 минут** после включения до нормального душа; ночной заезд = первая ночь без душа или кипяток из чайника.
- Проточник vs бойлер (Wordstat 1286): гость не различает; важно «открыл кран — тепло сразу или ждать».
- Проверка до оплаты/заезда: спросить в чате **источник** (центральная или бойлер), где выключатель/инструкция, снимок крана/панели бойлера; сверить адрес с ao-ustek.ru (если город — не спорить с хозяином о «включи бойлер»).
- Осень 2026 Тюмень: после опрессовок массовый график в основном закрыт, но точечные дома и квартирные бойлеры остаются риском (Рабфаковская кейс).
- Не юридический крючок: фокус на первой ночи, деньгах за ночь, честности карточки.

## Constraints
- dzen_rf_pack: без RF-blocked heroes; осенний свет на обложке, не зима-герой
- Case-only, Tyumen localize where natural
- No invented continuation of B01/B02 plots

## CTA / interlink (factory)
- booking: https://добрыйдом-72.рф/booking/
- blog: https://добрыйдом-72.рф/blog/
- TG channel: https://t.me/Dobriy_dom_72
- manager: https://t.me/Dobriy_dom_Tyumen
- MAX: https://max.ru/id660300569233_biz
- phone: +7 (993) 574-83-22
- Interlink published siblings: B01 beskontaktnoe-zaselenie-posutochno-tyumen; B02 perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem

## Derouter output requirements
Produce `research-notes.md` with: research_date 2026-09-25; reader_problem; reader_outcome; practical_facts; constraints; voice_angle; surprising_fact (if sourced); source_table (each row accessed_at 2026-09-25); writer_safe_urls; wordstat_stickers for cover (в квартире нет горячей воды, аренда квартиры в тюмени посуточно, бойлер); ## official_verifications only if bank/gov tariff digits — else state NOT_REQUIRED for УСТЭК factual quotes without tariff claims.
NO h2_outline, pain_solution_map, action_outline, FAQ skeleton, ready lead paragraph.
