# .cursor/excalibur-blog-handoff.md

```yaml
topic_id: B37
status: ready_for_article
brand: Добрый дом
market: посуточная аренда в Тюмени
date: 2026-09-29
time: "11:00 YEKT"

title_draft: "В карточке лифт работает. С чемоданом на восьмой — 22 минуты по лестнице"
slug_draft: lift-v-kartochke-est-s-chemodanom-na-vosmoj-posutochno-tyumen

dzen_pattern: 2
dzen_shape_hint: "Обещание лифта в карточке vs табличка «не работает» и багаж на лестнице"

wordstat_preflight: "mcp-kv wordstat_get_user_info OK (2026-09-29)"

hook_id: high_floor_lift_out
klyshin_original: «Этаж высокий. Лифт на табличке — не работает. Багаж уже в подъезде»
klyshin_angle: лифт в объявлении vs реальность при заселении; тяжёлый багаж
klyshin_signal_url: https://t.me/klyshin_A

wordstat_rework_summary: >
  probe «лифт не работает квартира посуточно» empty (225) →
  «посуточно лифт» totalCount 27 (225) →
  «снять квартиру посуточно высокий этаж» 29 (225) →
  final P0 «квартиры посуточно тюмень» 4194 (55+11176) |
  supporting «снять квартиру посуточно в тюмени» 1201 (55+11176)

wordstat_summary: >
  mcp_kv live 2026-09-29 |
  regions 55,11176,compare225 |
  P0 «квартиры посуточно тюмень» 4194 (55+11176) |
  lift probes weak RF-wide → Tyumen-localized guest case on spine

angle_rotation: >
  checked last N=3 B34–B36 |
  burn-at-door skip: no (lift angle fresh) |
  boiler skip: yes (B20 published) |
  dog skip: yes (B26,B36)

external_signal:
  primary: "Klyshin mechanics: этаж + табличка на лифте + багаж у подъезда"
  secondary: "Guest pain RF-wide lift/этаж weak; demand spine посуточно Тюмень"
  signal_urls:
    - https://t.me/klyshin_A
    - https://t.me/s/klyshin_A
    - https://добрыйдом-72.рф/blog/
    - https://t.me/Dobriy_dom_72

final_p0:
  phrase: "квартиры посуточно тюмень"
  volume_tyumen_and_region: 4194
  volume_russia: null
  regions:
    - 55
    - 11176
  compare_region: 225

supporting_queries:
  - phrase: "посуточно лифт"
    volume_russia: 27
  - phrase: "снять квартиру посуточно высокий этаж"
    volume_russia: 29
  - phrase: "снять квартиру посуточно в тюмени"
    volume_tyumen_and_region: 1201

wp_category_slugs:
  - posutochno
  - zaselenie
```
