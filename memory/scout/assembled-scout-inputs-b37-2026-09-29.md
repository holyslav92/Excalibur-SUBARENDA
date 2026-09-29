# Scout inputs B37 — 2026-09-29 YEKT (cron slot 06:00 UTC)

## Constraints (slot HARD)
- Один guest-night CASE «Добрый дом», не гайд. Факты только Тюмень.
- Anti-dup: published B01–B36 — не код/ключница/чужая дверь, не залог-плита B02, не собака B26, не бойлер B20/B38-draft, не соседи-музыка B14, не «всё включено» такси B10.
- Последние 3 published: B34 без залога у двери, B35 не тот подъезд, B36 собака отказ — семья burn-at-door не saturated для нового угла (лифт/этаж).
- Сезон: конец сентября, прохладно, багаж после поезда/такси. Зима героем — нет.

## Wordstat (MCP-KV live 2026-09-29)
- wordstat_get_user_info: OK
- «лифт не работает квартира посуточно» (225): API empty body — logged as weak probe
- «посуточно лифт» (225): totalCount 27
- «снять квартиру посуточно высокий этаж» (225): 29 (top: «на высоком этаже» 16)
- **final P0 spine:** «квартиры посуточно тюмень» → **4194** (55+11176) | compare RU queries weak on lift → localized case on Tyumen spine
- supporting: «снять квартиру посуточно в тюмени» → 1201 (55+11176)

## Klyshin (angle mechanics only, hook_id: high_floor_lift_out)
- original hook: «Этаж высокий. Лифт на табличке — не работает. Багаж уже в подъезде»
- angle: в карточке «лифт есть» / «удобно с багажом» vs табличка «не работает» при заселении; не юр-крючок
- signal: https://t.me/klyshin_A

## Proposed P0 case
- topic_id: B37
- title_draft (two-beat): «В карточке лифт работает. С чемоданом на восьмой — 22 минуты по лестнице»
- slug_draft: lift-v-kartochke-est-s-chemodanom-na-vosmoj-posutochno-tyumen
- guest pain: обещание лифта, тяжёлый багаж, дети/пожилые в сцене опционально
- wp_category_slugs: posutochno, zaselenie

## signal_urls
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## published-titles (excerpt last 5)
B32 price mismatch, B33 Avito double pay, B34 zalog filter lie, B35 wrong entrance PDF, B36 dog filter refuse
