# Scout inputs — 2026-09-04 YEKT slot

## Date context
- today_iso: 2026-09-04
- timezone: Asia/Yekaterinburg
- weekday: четверг
- season: начало сентября, осень (обложка — текущий сезон, не зима)

## Tenant
- Добрый дом, посуточная аренда Тюмень
- dzen_pattern prefer 2–5 (NOT numbered list default)
- Guest pains only — NO ЕГРН/суд/наследство/Москва/риэлтор

## Published titles (anti-dup, last 8)
| topic_id | title |
| B01 | Оплатил квартиру посуточно. Код прислали от чужой двери |
| B02 | Снял квартиру посуточно. Залог не вернули — нашли скол на плите |
| B03 | Привезли сына к вузу — «рядом» оказалось 40 минут пешком |
| B04 | Оплатили за двоих. У двери попросили доплату за третьего |
| B05 | Рейтинг 4,8. Два «всё супер» — и 3 900 ₽ под вопросом |
| B06 | Выезд в полдень. Поезд через 4 часа — чемоданы у подъезда |
| B07 | Хозяин написал «кухня есть». За три ночи в кафе ушло 7 200 ₽ |
| B08 | Перевели 3 000 ₽ предоплатой. К вечеру — тишина в чате |

## Angle rotation (last N=3: B06,B07,B08)
- burn-at-door (код/дверь): skip — B01 saturated family
- deposit/scratch: skip — B02
- prepayment silence: skip — B08 just published
- parking_before_booking: ACTIVE queue slot 04–07.09 — fresh angle

## Klyshin hook (queue)
- hook_id: parking_before_booking
- original angle: «Парковка рядом» — шлагбаум не пускает
- lockpick: место, пропуск, номер авто — до брони, не у барьера
- dzen_pattern: 2 (кейс с суммами и датами)

## Wordstat preflight
- wordstat_get_user_info: OK (Yandex Cloud API)

## Wordstat live probes (MCP-KV)

### P0 spine
- «квартиры посуточно тюмень» RU 225: 11765 | Tyumen 55+11176: 5320
- «снять квартиру посуточно в тюмени» RU: 4216

### Hook probes
- «парковка аренда квартиры» RU 225: 111 (weak alone)
- «парковка посуточно» RU 225: 5648 (mostly airport parking — not guest apartment)
- «аренда парковочного места» related: 6083

### Rework log
1. probe «парковка аренда квартиры» 111 → guest parking at apartment weak nationally
2. rework «квартиры посуточно тюмень» 11765 / 5320 local → demand spine
3. angle: parking/barrier/guest car at ЖК — rides P0 «квартиры посуточно тюмень» with parking lockpick

### Final P0
- phrase: «квартиры посуточно тюмень»
- volume: 11765 (RU 225), 5320 (55+11176)
- guest intent: book apartment + need car parking confirmed before pay

## Title draft (two-beat, NOT final Title role)
«Написали «парковка рядом». У шлагбаума: «пропуска нет»»

## topic_id
B09

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/

## Task
Write the complete scout handoff markdown. The calling script `excalibur_blog_derouter_opus_chat.py` saves your reply to `.cursor/excalibur-blog-handoff.md` — you do NOT need filesystem or MCP access.

**OUTPUT RULES (HARD):**
- Return ONLY the handoff markdown body (no refusal, no "cannot write", no DEROUTER SCOUT BLOCKER).
- Include all required lines: topic_id, title_draft, klyshin_hook, wordstat_rework, wordstat, angle_rotation, dzen_pattern, dzen_shape_hint, signal_urls, external_signal.
- Wordstat frequencies are already verified live in this prompt — use them as-is.
