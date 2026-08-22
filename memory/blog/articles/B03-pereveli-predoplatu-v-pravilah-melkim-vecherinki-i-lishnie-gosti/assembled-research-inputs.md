# Assembled research inputs — B03 (2026-08-22)

## Topic
- topic_id: B03
- title: Перевели предоплату. В правилах мелким: вечеринки и лишние гости
- tenant: Добрый дом, посуточная аренда Тюмень, голос комфорт+, НЕ юрист/ЕГРН/суд
- season: август 2026, лето
- angle: 7 пунктов в договоре/правилах проверить ДО перевода предоплаты (стороны, гости, курение, вечеринки, время выезда и т.д.)
- anti-dup: НЕ про коды/заселение (B01), НЕ про залог/скол (B02)

## Scout handoff (2026-08-22)
- Klyshin hook: contract_bans — «что нельзя делать по договору аренды»
- original hook: правила проживания аренда (117 RU — слабый)
- rework → P0: «аренда квартиры посуточно» — 48407 RU / 787 Tyumen (55+11176)
- dzen_pattern: нумерованный список, 7 пунктов до перевода
- signal_urls: https://t.me/klyshin_A, tenant booking/TG

## Wordstat (MCP-KV, accessed 2026-08-22)
| phrase | RU 225 | Tyumen 55+11176 |
|--------|--------|-----------------|
| аренда квартиры посуточно | 48407 | 787 |
| аренда квартиры тюмень посуточно | — | 188 |
| договор посуточной аренды квартиры | 2411 | 48 |
| правила проживания посуточно | 482 | — |
| правила проживания в квартире посуточно | 337 | — |
| правила проживания гостей в посуточной квартире | 44 | — |

Cover stickers candidate: аренда посуточно, Тюмень, правила проживания

## Fresh signal this week (accessed 2026-08-22)
1. **Tenant TG @Dobriy_dom_72** (live channel): посты лета 2026 — «до перевода денег стоит проверить не картинку, а условия: что входит в цену, во сколько реально заезд и выезд, как устроен возврат залога»; «скрытые доплаты за уборку, коммуналку и жёсткое время выселения».
   URL: https://t.me/s/Dobriy_dom_72
2. **Live Tyumen listings Aug 2026** — правила в карточках до оплаты:
   - kvartirka.com/446532: заезд 15:00, выезд 12:00, без вечеринок, курение запрещено, возраст от 21, залог 2000₽, предоплата 17%
   - kvartirka.com/470571: заезд 14:00, выезд 12:00, без вечеринок/питомцев, залог 1000₽
   - tyumen.sutochno.ru/2113445: заезд после 14:00, выезд до 12:00, курение запрещено, до 3 гостей в цене
3. **Avito Host course** (official platform): договор даже на 1 сутки; памятка с запретом курения, вечеринок; число гостей, время заезда/выезда, залог.
   URL: https://host.avito.com/course/lesson-5

## Practical facts from sources (DO NOT invent)

### Why guests miss the fine print
- Переводят предоплату по красивому объявлению, а ограничения (вечеринки, лишние гости, поздний выезд) — в мелком тексте правил или оферты (DirectLine, SAS.com.ru).
- На площадках правила часто в блоке «Правила дома» / «Правила проживания» — отдельно от фото (Sutochno, Kvartirka listings).
- Хозяева дублируют правила в объявлении, переписке и договоре — «три раза», иначе гость «не заметил» запрет (SAS.com.ru journal).

### 7 checklist points for Writer (guest POV, not legal template)
1. **Кто сдаёт** — ФИО/компания в договоре или оферте; если посредник — кто отвечает на связи (Avito course, Pravoved 4198705). Не углубляться в ЕГРН/суд.
2. **Сколько человек** — лимит проживающих и можно ли приглашать гостей/ночующих сверх брони; ответственность за действия «лишних» людей (DirectLine, Pravoved 1887711 — наниматель отвечает за нарушения сожителей).
3. **Вечеринки и шум** — типичный запрет «без вечеринок»; кейс: ДР без предупреждения → соседи → штраф хозяину (DirectLine). Тишина по региону: **Тюмень** 22:00–08:00 будни, 22:00–09:00 выходные, 13:00–15:00 ежедневно (Закон ТО №3 от 29.03.2022).
4. **Курение** — почти всегда запрет в квартире и часто на лестнице; связано с пожарной безопасностью (DirectLine, listings).
5. **Животные** — отдельное согласование; «без питомцев» в карточках — норма (Kvartirka listings).
6. **Заезд и выезд** — типично 14:00–15:00 / 12:00; поздний выезд и ранний заезд — только по согласованию и часто за доплату; фиксировать в переписке (MK Krasnoyarsk May 2026, listings). **Не разворачивать в статью про залог** — только как пункт «во сколько уходить».
7. **Что будет за нарушение** — досрочное прекращение, удержание из залога в пределах ущерба (SAS.com.ru пример формулировки); не писать про механику возврата залога (B02).

### Constraints for Writer
- Не юридический шаблон договора, не статьи ГК/JK цитатами.
- Не ЕГРН, нотариус, суды.
- Залог — упомянуть только как «есть в правилах», без чеклиста фиксации/сколов (B02).
- Бесконтакт/коды — не тема (B01).
- Суммы залогов в примерах — только из listings как рыночная вилка, не как цена «Добрый дом».
- Точные условия «Добрый дом» — только booking/менеджер.

### voice_angle
Спокойный чеклист «Добрый дом»: заранее проговорить правила, не у двери; мессенджер до оплаты.

### surprising_fact
Часто спорят не из-за «юридической силы», а потому что гость не открыл блок «Правила дома» на площадке — а там уже стоят «без вечеринок» и лимит гостей.

## source_table (for synthesis)
| source | type | url | accessed_at |
|--------|------|-----|-------------|
| Wordstat MCP-KV | keyword | live | 2026-08-22 |
| Scout handoff | internal | memory/scout/scout-inputs.md | 2026-08-22 |
| Добрый дом TG | tenant/community | https://t.me/s/Dobriy_dom_72 | 2026-08-22 |
| Kvartirka Tyumen listing | marketplace | https://kvartirka.com/residence/446532/ | 2026-08-22 |
| Kvartirka Tyumen listing 2 | marketplace | https://kvartirka.com/residence/470571/ | 2026-08-22 |
| Sutochno Tyumen | marketplace | https://tyumen.sutochno.ru/2113445 | 2026-08-22 |
| Avito Host course | official platform | https://host.avito.com/course/lesson-5 | 2026-08-22 |
| DirectLine rules memo | media | https://www.directline.pro/connect/p/pravila-prozhivaniya-v-posutochnoj-kvartire/ | 2026-08-22 |
| SAS.com.ru journal | media | https://www.sas.com.ru/ls/journal/posutochnaya-arenda-kvartiry-kak-sdavat-zakonno-schitat-pribyl-i-ne-voyevat-s-pod-yezdom.230/ | 2026-08-22 |
| Hozyain.pro | media | https://hozyain.pro/arenda-posutochno-kak-sdat-kvartiru-bez-problem-shtrafov-i-syurprizov/ | 2026-08-22 |
| Закон ТО тишина | official | https://tyumen-pravo.ru/zakon/2022/03/29/n-3/ | 2026-08-22 |
| Pravoved guests Q | community | https://pravoved.ru/question/1887711/ | 2026-08-22 |
| Добрый дом booking | tenant | https://добрыйдом-72.рф/booking/ | 2026-08-22 |

## writer_safe_urls
- https://добрыйдом-72.рф/booking/
- https://t.me/Dobriy_dom_72
- https://max.ru/id660300569233_biz
- https://t.me/Dobriy_dom_Tyumen
- tel:+79935748322
- https://добрыйдом-72.рф/blog/beskontaktnoe-zaselenie-posutochno-tyumen/
- https://добрыйдом-72.рф/blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/

## overlap_note
B01 = коды/заселение. B02 = залог/фиксация/возврат. B03 = правила проживания в договоре/оферте до оплаты: гости, вечеринки, курение, время, стороны.
