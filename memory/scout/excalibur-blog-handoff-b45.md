# Scout handoff — B45 — 2026-10-04 YEKT

> Derouter utility (scout) returned false `WORDSTAT MCP BLOCKER` despite live MCP-KV preflight in conductor; handoff stamped from conductor Wordstat + assembled inputs.

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-10-04)
klyshin_hook: hot_booking_skip_house_rules | original: «Если я сейчас начну задавать вопросы, квартиру заберёт следующий» | angle: гость посуточно не открыл памятку до оплаты — на выезде штраф за мусор/посуду (ритм klyshin_A/3186, не юр-кейс) | signal: https://t.me/klyshin_A/3186
wordstat_rework: probe «правила проживания посуточно» 387 (225) / 3 (55) → «правила проживания в квартире посуточно» 283 (225) → «уборка посуточно» 1932 (225, host bias) → «отмена брони посуточно» 53 (225) → final P0 «квартиры посуточно тюмень» 3889 (55+11176) | 8881 (225) | clusters tried: правила проживания, уборка, отмена брони, spine тюмень
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 3889 | RU 8881 | supporting «снять квартиру посуточно в тюмени» 1071 (55+11176) | 2990 (225)
angle_rotation: checked last N=12 | burn-at-door skip: yes | reason: не код/ключница/заселение, не залог (B44/B02), не предоплата, не pet/noise/boiler/vuz families; штраф по памятке ≠ B23 простыни; ≠ third-guest surcharge clone
dzen_pattern: 2
dzen_shape_hint: «Спешная оплата на даты — памятку открыли после списания, на выезде сумма за мусор/посуду»

```yaml
topic_id: B45
status: ready_for_research_start
brand: Добрый дом
market: посуточная аренда в Тюмени
date: 2026-10-04
slot: "2026-10-04 YEKT"

title_draft: "Оплатили две ночи. На выезде прислали штраф за мусор — правила не читали"
short_title_research_start: "Оплатили две ночи. На выезде прислали штраф за мусор — правила не читали"
slug_draft: posutochno-tyumen-pravila-prozhivaniya-shtraf-musor-vyezd
slug_hint: posutochno-tyumen-pravila-prozhivaniya-shtraf-musor-vyezd

hook_id: hot_booking_skip_house_rules
guest_pain: скрытая доплата / правила проживания (штраф на выезде)
anti_dup_rationale: >
  Не повторяет бан слот 2026-10-04 (B01,B13,B18,B22,B35 код; B02,B44 залог; B08,B40 предоплата;
  B26,B36 pet; B20,B38 boiler; B14 соседи; B03 вуз). Отличие от B23 — не простыни, а штраф по памятке
  (мусор/посуда) после спешной оплаты; отличие от B10/B32 — не «всё включено»/комиссия в карточке.

case_sketch: >
  Две ночи, Тюмень, пара на даты когда «последние варианты». Хост пишет: «бронь снимут через час».
  Гость оплачивает на площадке, ссылку на правила не открывает. На второй день — пакет у входа в квартиру,
  две кружки в раковине. На выезде в чате: штраф по пункту памятки (сумма в ₽), угроза удержать депозит
  или «доплатить переводом». Lockpick для статьи: «Пришлите памятку до оплаты — что считается штрафом?»

h1_shape_preview: >
  Двухтакт: (1) оплатили ночи / даты горят; (2) на выезде штраф по правилам, которые не читали.
  Стоп-фактор ночи, не how-to.

final_p0:
  phrase: "квартиры посуточно тюмень"
  volume_tyumen_and_region: 3889
  volume_russia: 8881
  regions: [55, 11176]
  compare_region: 225

supporting_queries:
  - phrase: "правила проживания посуточно"
    volume_russia: 387
    volume_tyumen: 3
  - phrase: "правила проживания в квартире посуточно"
    volume_russia: 283
  - phrase: "снять квартиру посуточно в тюмени"
    volume_tyumen_and_region: 1071
    volume_russia: 2990

wp_category_slugs: [posutochno, zaselenie]
primary_query: квартиры посуточно тюмень
priority: P0

signal_urls:
  - https://t.me/klyshin_A/3186
  - https://t.me/s/klyshin_A
  - https://добрыйдом-72.рф/blog/
  - https://t.me/Dobriy_dom_72
```
