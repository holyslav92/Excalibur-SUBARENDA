# .cursor/excalibur-blog-handoff.md

```yaml
topic_id: B39
status: ready_for_article
brand: Добрый дом
market: посуточная аренда в Тюмени
date: 2026-09-29
time: "17:00 YEKT"

title_draft: "Оплатили на сайте. У двери — договор на три страницы и ещё 3 000 ₽"
slug_draft: oplatili-na-sajte-u-dveri-dogovor-i-doplata-posutochno-tyumen

dzen_pattern: 2
dzen_shape_hint: "Онлайн-оплата прошла → у двери бумажный договор с новыми строками и доплатой"

wordstat_preflight: "mcp-kv wordstat_get_user_info OK (2026-09-29)"

hook_id: paper_contract_at_door
klyshin_original: «Оплатили. У двери — «подпишите, без этого ключ не отдам»»
klyshin_angle: бумажный договор после онлайн-оплаты; скрытая строка про залог/уборку
klyshin_signal_url: https://t.me/klyshin_A

wordstat_rework_summary: >
  probe «договор у двери посуточно» empty →
  «договор посуточной аренды» 3982 (225) / 94 (55+11176) →
  spine «квартиры посуточно тюмень» 4194 (55+11176) | 9212 (225)

wordstat_summary: >
  mcp_kv live 2026-09-29 |
  regions 55,11176,compare225 |
  P0 «договор посуточной аренды» 3982 (225) 94 (55+11176) |
  demand spine «квартиры посуточно тюмень» 4194 (55+11176)

angle_rotation: >
  checked last N=3 B35–B37 |
  burn-at-door skip: partial (not code/door-wrong) |
  boiler skip: yes (B20,B38 draft) |
  lift skip: yes (B37) |
  minimum-nights skip: live slug oplachena-odna-noch-minimum-dvoe-sutok on site

external_signal:
  primary: "Klyshin mechanics: оплата прошла → бумага у двери → отказ без подписи"
  secondary: "Guest pain RF-wide договор посуточной аренды; supply Тюмень"
  signal_urls:
    - https://t.me/klyshin_A
    - https://t.me/s/klyshin_A
    - https://добрыйдом-72.рф/blog/
    - https://t.me/Dobriy_dom_72

final_p0:
  phrase: "договор посуточной аренды"
  volume_tyumen_and_region: 94
  volume_russia: 3982
  regions:
    - 55
    - 11176
  compare_region: 225

supporting_queries:
  - phrase: "квартиры посуточно тюмень"
    volume_tyumen_and_region: 4194
    volume_russia: 9212
  - phrase: "предоплата посуточно"
    volume_russia: 705

wp_category_slugs:
  - posutochno
  - zaselenie
```
