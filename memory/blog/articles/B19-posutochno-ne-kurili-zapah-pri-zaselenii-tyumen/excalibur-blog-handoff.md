# Scout handoff B03

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-09-13)

klyshin_hook: smoke_smell_checkin | original: «В объявлении — «не курили». Зашли — запах сигарет и окно на замке.» | angle: маркетинг «чистая/не курили» vs реальность при заселении; гость уже внутри, окно не открывается | signal: https://t.me/klyshin_A

wordstat_rework: probe «курение квартира посуточно» 54 (225) → «запрет курения аренда квартиры» 46 → «запах в квартире посуточно» 12 → localize «аренда квартиры посуточно» 664 (55+11176) → final P0 «квартиры посуточно тюмень» 4826 (55+11176) | compare RU 10385

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4826 | «аренда квартиры посуточно» 664 | «курение квартира посуточно» 54 (225)

angle_rotation: B19 = smoke_smell_checkin; burn-at-door skip (B18 — вход); skip_last5: hot_water, neighbors, dog, hidden_fees; сенсорный кейс внутри квартиры, не у двери

dzen_pattern: 2 — кейс с суммами и датами

dzen_shape_hint: «Написали „не курили“. В спальне — запах и окно на замке»

topic_id: B19

short_title: «Не курили»: запах и окно на замке

title_draft: «Написали «не курили». В спальне — запах и окно на замке»

slug: napisali-ne-kurili-v-spalne-zapah-i-okno-na-zamke

signal_urls:
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

external_signal: https://t.me/klyshin_A

queue_slot: B19

season_note: 2026-09-13, воскресенье, ранняя осень; сентябрь, тёплый вечер, жёлтые листья, не зима

interlink_siblings:
- B18: код/домофон/подъезд 20 мин
- B17: коммуналка/счётчики 1 840 ₽
- B16: рейс отменили/предоплата 4 200 ₽

wp_category_slugs:
