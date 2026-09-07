# Scout handoff B13 — пустая ключница при бесконтактном заселении

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-09-07)
klyshin_hook: parking_keybox | original: «Код открыл ключницу — ключа внутри нет» (mechanics: бесконтакт / keybox, NOT wrong door)
wordstat_rework: probe «ключница посуточно» empty (55+11176) → «ключница» 69643 (225 furniture bias) → «бесконтактное заселение посуточно» 59 (55+11176) / 2993 (225) → «аренда квартиры посуточно» 710 (55+11176) → final P0 «квартиры посуточно тюмень» 5220 (55+11176) / 11084 (225)
wordstat: mcp_kv live | regions 55+11176 compare 225 | P0 «квартиры посуточно тюмень» 5220 | P1 «бесконтактное заселение посуточно» 59 | P1 «снять квартиру посуточно в тюмени» 1689 | compare RU «бесконтактное заселение посуточно» 2993
season_note: YEKT 2026-09-07 early September — summer/light cover; NO winter hero
topic_id: B13
slug: kod-srabotal-klyuchnitsa-pusta-posutochno-tyumen
title_draft: Код сработал. Открыли ключницу — внутри пусто
angle: гость у подъезда, код открыл ящик, ключа нет — 23:40, такси уехало; lockpick: «Есть фото ключницы и тест кода до оплаты?»
anti_dup: B01 wrong door code; WP 2026-09-07 no-code-at-night — different angle (empty box, not missing/wrong code)
dzen_pattern: 2
wp_category_slugs: posutochno, zaselenie
