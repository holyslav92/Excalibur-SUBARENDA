# Scout inputs — слот 2026-09-25 YEKT

## Tenant
Добрый дом, посуточная Тюмень, case-only (не гайд), dzen_rf_pack.

## Anti-dup (не повторять H1/угол)
- B01 код чужой двери
- B02 залог не вернули
- WP: zalog-utrom-posle-uborki, bez-zaloga, predoplata, komissiya, min nights, wrong entrance, chuzhie chemodany, linen stains, avito double pay
- НЕ юр-крючки ЕГРН/наследство

## Выбранный guest-pain угол
**Бойлер / горячая вода в первую ночь посуточно:** в карточке «горячая вода есть», гость заезжает поздно (командировка/поезд), в душе ледяная струя — хозяин: «город отключил» или «бойлер включите сами».

## Klyshin angle bank
- hook_id: `utilities_counters`
- original: «показания счётчиков — не переплатить ЖКХ»
- angle rework: механика «сначала проверка воды/бойлера, потом ночь» (не ЖКХ-энциклопедия)

## Wordstat preflight
mcp-kv wordstat_get_user_info OK (Cursor conductor live call 2026-09-25 UTC)

**CONDUCTOR ATTESTATION (HARD):** частоты ниже — прямые ответы MCP-KV `wordstat_get_top_requests` в этом прогоне. Derouter НЕ вызывает Wordstat; оформи handoff только из этих данных.

## Wordstat probes (live MCP-KV)
| phrase | region | top P0 | volume |
|--------|--------|--------|--------|
| в квартире нет горячей воды | 225 | в квартире нет горячей воды | 2709 |
| нет горячей воды в квартире что делать | 225 | (cluster) | 269 |
| в съемной квартире нет горячей воды | 225 | same | 11 |
| аренда квартиры посуточно тюмень | 225 | аренда квартиры в тюмени посуточно | 157 |
| аренда квартиры посуточно тюмень | 55+11176 | аренда квартиры в тюмени посуточно | 86 |
| проточный водонагреватель или бойлер | 225 | (similar) | 1201 |

## wordstat_rework log
probe «жкх аренда квартиры» → weak for case → probe «нет горячей воды в квартире» 2709 RU → localize посуточно Tyumen 86 → **final P0:** «в квартире нет горячей воды» (2709 RU) + sticker «аренда квартиры в тюмени посуточно» (86 TY)

## Topic assignment
- topic_id: B03
- slug draft: gorodskaya-voda-obeshchali-nochyu-ledyaniy-dush
- title draft (two-beat case, NOT how-to): «Написали «горячая вода есть». В 23:40 из душа — ледяная струя»

## signal_urls
- https://t.me/klyshin_A
- https://dzen.ru/holyslav
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## Season
2026-09-25 осень Тюмень (обложка осенний свет, не зима героем).
