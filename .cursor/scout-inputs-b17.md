# Scout inputs — 2026-09-12 YEKT slot (11:03)

## Run context
- date: 2026-09-12 (Asia/Yekaterinburg, early autumn)
- tenant: Добрый дом / добрыйдом-72.рф
- topic_id candidate: B17
- slot: CASE only, not guide

## Angle rotation (last N=3)
- B16 «Рейс отменили. 4 200 ₽ обещали вернуть…» — cancel/prepay refund
- B15 «Рабочий стол» обещали… — wifi/commandirkovka
- B14 «Тихий дом»… — neighbors/noise
- burn-at-door skip: NO (not from that family)
- skip families saturated: hot_water, neighbors, dog, hidden_fees, early_checkin, cancel_prepay (flight variant done)

## Selected hook (fresh)
- klyshin_hook_id: sept_cold_radiators_guest
- original: «Написали «отопление есть». В сентябре за окном +6 °C — батареи ледяные, хозяин: «город ещё не включил»»
- angle: seasonal guest-night burn; promise «тепло/отопление» vs cold radiators on check-in; NOT hot water shower (published), NOT winter hero on cover (September autumn OK)
- dzen_pattern: 5 (local seasonal Tyumen)
- dzen_shape_hint: «Написали «тепло есть». За окном +6 °C — батареи холодные»

## Wordstat (MCP-KV live)
wordstat_preflight: mcp-kv wordstat_get_user_info OK

Probes:
| phrase | regions | volume |
|--------|---------|--------|
| батареи холодные | 225 | 7704 |
| в квартирах холодно батареи | 225 | 393 |
| холодно в квартире | 225 | 31989 (utility bias) |
| отопление посуточно | 225 | 36 |
| квартиры посуточно тюмень | 55+11176 | 4929 |
| аренда квартиры посуточно | 225 | 40694 |
| штраф за отмену бронирования | 225 | 360 (not picked — B16 cancel family) |
| отель или посуточная квартира | 225 | 283 (hotel_vs_daily parked) |

wordstat_rework: probe «отопление посуточно» 36 (225) → «батареи холодные» 7704 / «в квартирах холодно батареи» 393 → guest cluster «квартиры посуточно тюмень» 4929 (55+11176) | compare «аренда квартиры посуточно» 40694 (225)

final P0: «квартиры посуточно тюмень» 4929 (55+11176) | supporting «батареи холодные» 7704 (225)

## Title draft (two-beat, not final)
«Написали «тепло есть». За окном +6 °C — батареи холодные»

## Anti-dup check
NOT duplicate: B10 all-inclusive, B13 keybox, B16 flight cancel, hot water article on WP

## External signal
- klyshin_A angle bank (mechanics only)
- site blog guest pains seasonal

## Output request
Write `.cursor/excalibur-blog-handoff.md` with topic_id B17, slug suggestion, dzen_pattern 5, all wordstat lines, angle_rotation block.
