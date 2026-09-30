# .cursor/excalibur-blog-handoff.md

```yaml
topic_id: B39
status: ready_for_article
brand: Добрый дом
market: посуточная аренда в Тюмени
date: 2026-09-30
time: "11:04 YEKT"

title_draft: "В фильтре — «от одной ночи». У домофона: «минимум двое суток»"
slug_draft: posutochno-tyumen-v-filtre-ot-odnoj-nochi-u-domofona-minimum-dvoe-sutok

dzen_pattern: 2
dzen_shape_hint: "Фильтр/цена за одну ночь vs отказ заселить без второй ночи у домофона"

wordstat_preflight: "mcp-kv wordstat_get_user_info OK (2026-09-30, conductor)"

hook_id: min_nights_at_door
klyshin_original: «В карточке — от одной ночи. У двери — только от двух»
klyshin_angle: правила брони и минимальный срок на месте; не бесконтакт/код
klyshin_signal_url: https://t.me/klyshin_A

wordstat_rework_summary: >
  probe «заселение в квартиру посуточно» 2662 (225) guest intent →
  avoid бесконтакт saturated →
  angle min nights at door →
  final P0 «квартиры посуточно тюмень» 4194 (55+11176) | 9212 (225) |
  supporting «снять квартиру посуточно в тюмени» 1201 (55+11176) | 3175 (225)

wordstat_summary: >
  mcp_kv live 2026-09-30 |
  regions 55,11176,compare225 |
  P0 «квартиры посуточно тюмень» 4194 (55+11176) | 9212 (225)

angle_rotation: >
  checked last N=3 B35–B37 |
  burn-at-door skip: no (min-nights angle) |
  boiler skip: yes B20/B38 |
  dog/lift skip: yes B36/B37

external_signal:
  primary: "Klyshin mechanics: фильтр одна ночь → отказ/доплата за две у двери"
  secondary: "Guest booking rules; Tyumen spine посуточно"
  signal_urls:
    - https://t.me/klyshin_A
    - https://t.me/s/klyshin_A
    - https://добрыйдом-72.рф/blog/
    - https://t.me/Dobriy_dom_72

final_p0:
  phrase: "квартиры посуточно тюмень"
  volume_tyumen_and_region: 4194
  volume_russia: 9212
  regions:
    - 55
    - 11176
  compare_region: 225

supporting_queries:
  - phrase: "заселение в квартиру посуточно"
    volume_russia: 2662
  - phrase: "снять квартиру посуточно в тюмени"
    volume_tyumen_and_region: 1201
    volume_russia: 3175

wp_category_slugs:
  - posutochno
  - zaselenie
```
