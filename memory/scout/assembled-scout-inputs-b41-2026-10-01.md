# Scout inputs B41 — 2026-10-01 YEKT (cron slot 12:00 UTC)

## Constraints (slot HARD)
- Один guest-night CASE «Добрый дом», не гайд. Факты только Тюмень.
- Anti-dup published + live WP drift: не код/ключница (B13,B18,B35), не залог-плита B02, не «без залога/предоплаты у двери» (B34,B40), не лифт B37, не Wi‑Fi созвон (LIVE posutochno-wifi-obeshchali…), не комиссия на экране (LIVE kvartira-posutochno-tyumen-bez-komissii…), не минимум ночей B39, не соседи/drill LIVE, не кухня→кафе 7 200 ₽ B07 (другой угол: поломка плиты + доставки).
- Сезон: 1 октября, осень, не зимний герой. Обложка — текущий сезон.
- ViralDzen handoff: memory/scout/viral-dzen-handoff.json PASS (travel hub; angle — понятная связь при поломке/позднем заезде, не копировать viral body).

## Wordstat (MCP-KV live 2026-10-01)
- wordstat_preflight: wordstat_get_user_info OK
- probe «посуточно или отель» (225): total 324; top «квартира посуточно или отель» 250
- probe «комиссия посуточно квартира» (225): total 1073; top «квартиры посуточно без комиссии» 338
- probe «квартира с кухней посуточно» (225): totalCount 88 (API sparse list)
- probe «квартиры посуточно тюмень» (55+11176): **3984**; supporting «снять квартиру посуточно в тюмени» 1104
- compare «квартиры посуточно тюмень» (225): **8838**
- wordstat_rework: hook kitchen_vs_hotel weak on «кухня посуточно» alone → guest cluster «квартиры посуточно тюмень» + contrast «посуточно или отель» для demand spine
- **final P0:** «квартиры посуточно тюмень» **3984** (55+11176) | compare RU **8838**

## Klyshin (mechanics only)
- hook_id: kitchen_vs_hotel (queue_active)
- original: «Три ночи. Кухня «есть» — или каждый день кафе?»
- localized angle: в карточке «полноценная кухня» / «готовить как дома» → плита не зажигается на 2-й вечер, гость вынужден в доставку; сумма сгоревших ₽
- signal: https://t.me/klyshin_A

## Proposed case
- topic_id: B41
- title_draft (two-beat): «Написали «кухня как дома». На второй вечер плита не зажигается — 4 200 ₽ на доставках»
- slug_draft: posutochno-tyumen-kuhnya-kak-doma-plita-ne-zazhigaetsya-dostavki
- guest pain: скрытая зависимость от техники, хозяин «мастер завтра», дети/командировка устали
- dzen_pattern: 2 (кейс с суммами)
- wp_category_slugs: posutochno, zaselenie

## angle_rotation
- checked last N=12: burn-at-door family saturated (B34,B40,B39,B35) → skip door/predoplata clone
- reason: kitchen appliance failure + delivery burn — fresh vs B07 cafe spend

## signal_urls
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72
