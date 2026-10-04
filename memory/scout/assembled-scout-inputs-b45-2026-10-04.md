# Scout inputs B45 — 2026-10-04 YEKT

## Slot
- topic_id: **B45**
- tenant: Добрый дом, посуточно Тюмень
- editorial_canon: dobry_dom_voice_reset_v1 / PR #52 case-only (не гайд)
- run_date: 2026-10-04 (октябрь, обложка — осень, не зима героем)

## ViralDzen (STEP 0 PASS)
- hub: travel
- viral_source (angle only, do not copy): Ozon Travel техподдержка / отмена брони
- guest_angle_ru: после дороги в Тюмень гость хочет ясный контакт и доступ, не «тишину в чате»
- tyumen_wound_hint: сдвиг по времени прилёта + неопределённость с заселением

## Anti-dup (published + live WP — не повторять H1/угол)
- B21 ранний заезд / уборка до 14:00
- B40 предоплата до кода
- B01/B13/B18 код/ключница/домофон
- B44 залог/заморозка на оплате
- LIVE: pravila-prozhivaniya-shtraf-musor-vyezd, zalog-posle-uborki, wifi-sozvon, drill-sosedi, bez-komissii-na-ekrane-oplaty

## Klyshin hook (original, mechanics not Moscow/legal)
- hook_id: `night_checkin_surcharge`
- hook_ru: «В карточке заезд с 14:00. Рейс посадил в 00:35 — в чате: ночной заезд +2 500 ₽»
- angle: скрытая доплата за поздний заезд после оплаты ночей; гость уже в такси/у подъезда; NOT early-wait B21, NOT predoplata B40
- lockpick question: «С какого часа у вас начинается ночной заезд и он в цене?»
- delivery mechanics: диалог-улика → короткий отказ хоста → «Сначала время в договорённости. Потом ключ. Не наоборот.»

## Wordstat (MCP-KV live 2026-10-04, regions as noted)
| phrase | region | volume / note |
|--------|--------|----------------|
| квартиры посуточно тюмень | 55+11176 | 3889 |
| снять квартиру посуточно в тюмени | 55+11176 | 1071 |
| бесконтактное заселение посуточно | 225 | 2508 |
| бесконтактное заселение в квартиру посуточно как это | 225 | 580 |
| правила проживания в квартире посуточно | 225 | 283 |
| комиссия посуточно квартира | 225 | 1059 (host/platform bias — не P0) |
| поздний заезд посуточно | 225 | totalCount 37 only (partial) |
| ночной заезд посуточно | 225 | totalCount 13 only (partial) |

### Rework log
- weak «ночной/поздний заезд» counts → anchor demand on **бесконтактное заселение посуточно** (2508 RU) + localize supply **квартиры посуточно тюмень** (3889)
- final P0 phrase: **квартиры посуточно тюмень** (3889, 55+11176); compare RU spine **бесконтактное заселение посуточно** (2508)

## Title draft (two-beat case H1, not how-to)
«Заезд с 14:00. Самолёт сел в 00:35 — в чате: ночной заезд 2 500 ₽»

## Short slug hint
posutochno-tyumen-nochnoj-zaезд-v-chate-2500

## signal_urls
- https://t.me/s/klyshin_A
- https://t.me/s/Dobriy_dom_72
- https://добрыйдом-72.рф/blog/
- memory/scout/viral-dzen-handoff.json

## Scout output request
Write `.cursor/excalibur-blog-handoff.md` with: topic_id B45, final title draft, hook, wordstat table, rework log, anti-dup note, case scene bullets for Research.
