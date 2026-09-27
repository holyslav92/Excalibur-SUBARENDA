# .cursor/excalibur-blog-handoff.md

```yaml
topic_id: B37
status: ready_for_article
brand: Добрый дом
market: посуточная аренда в Тюмени
date: 2026-09-27
time: "09:00 YEKT"

title_draft: "В карточке лифт работает. С чемоданом на восьмой — 22 минуты по лестнице"
slug_draft: lift-v-kartochke-est-s-chemodanom-na-vosmoj-posutochno-tyumen

dzen_pattern: 2
dzen_shape_hint: "лифт в описании есть — на месте табличка «не работает»; 22 минуты с багажом"

wordstat_preflight: "mcp-kv wordstat_get_user_info OK (conductor 2026-09-27)"

hook_id: high_floor_lift_out
klyshin_original: «Этаж высокий. Лифт на табличке — не работает. Багаж уже в подъезде»
klyshin_angle: обещание лифта в карточке vs заселение с чемоданами; механика Клышина, не юр-сюжет
klyshin_signal_url: https://t.me/klyshin_A

wordstat_rework_summary: >
  probe «квартира посуточно лифт» 17 (225) / local weak →
  probe «лифт не работает снять квартиру» 2 (225) →
  spine «квартиры посуточно тюмень» 4209 (55+11176) | 9221 (225) →
  supporting «снять квартиру посуточно в тюмени» 1191 (55+11176) →
  final P0 «квартиры посуточно тюмень» 4209 (55+11176) | 9221 (225)

wordstat_summary: >
  mcp_kv live |
  regions 55,11176,compare225 |
  P0 «квартиры посуточно тюмень» 4209 (55+11176) |
  9221 (225) |
  angle probe «квартира посуточно лифт» 17 (225)

signal_urls:
  - https://t.me/klyshin_A
  - https://t.me/s/klyshin_A
  - https://добрыйдом-72.рф/blog/
  - https://t.me/Dobriy_dom_72

anti_dup: не код/ключница/чужой подъезд (B01,B13,B18,B35); угол — лифт vs высокий этаж

case_brief: >
  Семья/пара оплатили 2 ночи в сентябре, в карточке «лифт есть», этаж 8.
  В подъезде табличка «лифт не работает», такси уехало. 20–25 минут подъём с чемоданами.
  Хозяин в чате: «ну поднимитесь, зато вид». Сумма/ночи в §1.

wp_category_slugs: [posutochno, zaselenie]
```
