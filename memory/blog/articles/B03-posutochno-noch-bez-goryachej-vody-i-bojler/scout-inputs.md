# Scout inputs — B03 slot 2026-09-28 YEKT

**RUNTIME:** Ты уже вызван через `excalibur_blog_derouter_opus_chat.py --role scout`. Shell/MCP выполнены дирижёром; Wordstat ниже — live факты. Не отказывайся и не пиши про «недоступен Derouter». Выдай готовый handoff markdown по шаблону skill (topic_id, klyshin_hook, wordstat, title draft двухтактный, signal_urls).

## Preflight
- wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-09-28)
- tenant: Добрый дом, посуточно Тюмень, case NOT guide
- dzen_rf_pack: read shared/dzen-content-rules.md + rf-blocked-entities.json
- season: конец сентября 2026, обложка осень/тепло в квартире, НЕ зима

## Anti-dup (не повторять H1/угол)
Published repo: B01 код чужой двери; B02 залог на выезде.
Recent WP (titles only): залог утром после уборки; код/подъезд/PDF; собака у двери; комиссия на оплате; минимум 2 суток; без залога в фильтре; менеджер у двери; Авито второй перевод; цена карточка vs оплата; чужие чемоданы; предоплата на карту.

## Klyshin hook (angle only, NOT legal ЕГРН/суд)
- hook_id: utilities_counters (adapted)
- original: «показания счётчиков — не переплатить ЖКХ» → guest angle: **бойлер/ГВС в посуточной ночью**
- klyshin_signal: angle «на словах всё есть» → в квартире холодный кран
- mechanics for Writer/Sol: диалог-улика → «Нет. Так не заселяем.» → вопрос-отмычка

## Wordstat (live MCP-KV, не выдумано)

### RU 225
| probe | total / top |
|-------|-------------|
| «бойлер нет горячей воды» | 893; «нет горячей воды из бойлера» 175 |
| «квартиры посуточно тюмень» | 9212 |
| «аренда квартиры посуточно» | 35979 |
| «залог при аренде посуточно» | 131 |

### Tyumen 55+11176
| probe | note |
|-------|------|
| «квартиры посуточно» | 12245 total; «квартиры посуточно тюмень» **4194** |

### Rework log
1. Hook «бойлер нет горячей воды» — узкий (893), но честный guest pain посуточно.
2. Spine demand: **final P0 «квартиры посуточно тюмень»** — 9212 (225), 4194 (55+11176).
3. Stickers/H2 из related: «снять квартиру посуточно в тюмени» 3175 (225); «как включить водонагреватель» 6755 (related cluster).

## Topic card for pipeline
- topic_id: B03
- slug draft: posutochno-noch-bojler-ledyanaya-voda (may refine after Title)
- story spine: гость заселился вечером, в душе ледяная вода, хозяин/чат: «подождите час, бойлер нагреется» / «мы экономим, включим утром»
- numbers: 1–2 ночи, сумма брони 4 800–6 200 ₽, время 22:40–01:10
- Tyumen only in body; H1 may omit «Тюмень»
- NOT: guide «как включить бойлер», NOT «N советов»

## Output
Write handoff to `.cursor/excalibur-blog-handoff.md` with topic_id B03, signal_urls, final P0, title draft двухтактный (case night).
