topic_id: B17  
slug: napisali-teplo-est-za-oknom-6-gradusov-batarei-holodnye

title_draft: «Написали «тепло есть». За окном +6 °C — батареи холодные»

dzen_pattern: 5  
dzen_shape_hint: «Написали «тепло есть». За окном +6 °C — батареи холодные»

external_signal: klyshin angle bank + seasonal Tyumen guest pain (September heating start)

signal_urls:
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/

wordstat_preflight: mcp-kv wordstat_get_user_info OK

klyshin_hook: sept_cold_radiators_guest | original: «Написали «отопление есть». В сентябре за окном +6 °C — батареи ледяные» | angle: seasonal guest-night; promise тепло vs cold radiators; NOT hot water, NOT winter cover hero | signal: memory/scout/klyshin-topic-bank.json

wordstat_rework: probe «отопление посуточно» 36 (225) → «батареи холодные» 7704 / «в квартирах холодно батареи» 393 (225) → final P0 «квартиры посуточно тюмень» 4929 (55+11176) | clusters tried: отопление посуточно, батареи холодные, холодно в квартире, квартиры посуточно тюмень

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4929 | supporting «батареи холодные» 7704 (225) | compare «аренда квартиры посуточно» 40694 (225)

angle_rotation: checked last N=3 (B16 cancel, B15 wifi, B14 neighbors) | burn-at-door skip: no | reason: fresh heating/seasonal family

case_angle: Гость бронирует квартиру посуточно в Тюмени, читает в описании «тепло есть», а вечером при +6 °C за окном понимает: батареи холодные, ночевать придётся в одежде. Исследованию нужен практический ракурс гостя: что уточнить до предоплаты, как проверить обещание «тепло» в сезон запуска отопления и какой выход просить у хозяина, если квартира не пригодна для ночёвки.
