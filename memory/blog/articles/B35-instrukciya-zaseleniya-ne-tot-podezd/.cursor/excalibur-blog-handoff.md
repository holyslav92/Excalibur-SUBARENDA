# .cursor/excalibur-blog-handoff.md

```yaml
topic_id: B35
status: ready_for_article
brand: Добрый дом
market: посуточная аренда в Тюмени
date: 2026-09-24
time: "12:00 YEKT"

title_draft: "Прислали инструкцию на три страницы. Подъезд оказался чужой"
slug_draft: instrukciya-zaseleniya-posutochno-ne-tot-podezd

dzen_pattern: 2
dzen_shape_hint: "PDF с подъездом и кодом — а дверь в другом дворе; 35 минут с чемоданом"

wordstat_preflight: "mcp-kv wordstat_get_user_info OK (conductor 2026-09-24)"

hook_id: instruction_wrong_entrance
klyshin_original: «Инструкцию прислали. Всё по пунктам. Только дверь — не та»
klyshin_angle: самозаселение по тексту vs реальный подъезд/двор; не код/ключница
klyshin_signal_url: https://t.me/klyshin_A

wordstat_rework_summary: >
  probe «инструкция по заселению в квартиру посуточно» 73 (225) / 1 (55+11176) →
  spine «квартиры посуточно тюмень» 9275 (225) / 4274 (55+11176) →
  supporting «не вернули залог за квартиру посуточно» cluster 72 (225) →
  final P0 «квартиры посуточно тюмень» 4274 (55+11176) | 9275 (225)

wordstat_summary: >
  mcp_kv live |
  regions 55,11176,compare225 |
  P0 «квартиры посуточно тюмень» 4274 (55+11176) |
  9275 (225) |
  angle probe «инструкция по заселению в квартиру посуточно» 73 (225)

signal_urls:
  - https://t.me/klyshin_A
  - https://t.me/s/klyshin_A
  - https://добрыйдом-72.рф/blog/
  - https://t.me/Dobriy_dom_72

anti_dup: не дублировать B13/B18/B01 (код/ключница/домофон); угол — неверный подъезд в инструкции

case_brief: >
  Гость оплатил 2 ночи, получил длинную инструкцию (подъезд 2, код, этаж).
  Приехал вечером сентября, такси уехало. Дом верный, подъезд/двор — нет.
  30–40 минут переписка «вы не туда». Сумма/ночи в §1.

wp_category_slugs: [posutochno, zaselenie]
```
