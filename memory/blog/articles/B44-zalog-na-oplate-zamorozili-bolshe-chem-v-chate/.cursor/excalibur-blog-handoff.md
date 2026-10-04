wordstat_preflight: mcp-kv wordstat_get_user_info OK (conductor 2026-10-04 YEKT)
klyshin_hook: deposit_before_keys | original: «Сначала проверка. Потом перевод. Не наоборот.» | angle: в чате мелкий залог, на экране оплаты крупный холд до кода и заселения
wordstat_rework: probe «залог на карте посуточно» RU API sparse → «залог посуточно вернут» 110 RU → spine «квартира посуточно залог» 17 (Tyumen 55) + «посуточно комиссия» 1769 RU как контекст скрытой суммы на checkout
wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартира посуточно залог» 17 (55) | RU supporting «не вернули залог за квартиру посуточно» 31 | «посуточно комиссия» 1769 (225)
angle_rotation: checked last N=12 | burn-at-door skip: yes | reason: не код/ключница/наличный залог у двери (B34); не возврат залога за скол (B02); не «залог к обеду» live WP; угол — холд на карте больше обещанного в чате до заселения
dzen_pattern: 2
dzen_shape_hint: «В чате 3 000 — на оплате заморозили 11 400, код ещё не прислали»
topic_id: B44
title_draft: «В чате залог 3 000 ₽. На оплате банк заморозили 11 400 — код ещё не прислали»
primary_query: квартира посуточно залог
priority: P0
slug_draft: posutochno-tyumen-v-chate-zalog-3000-bank-zamorozil-11400
wp_category_slugs: posutochno, zalog
signal_urls:
- https://t.me/klyshin_A
- https://t.me/s/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72
