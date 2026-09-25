# Scout handoff B03 — собака / доплата у двери

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-09-25, conductor live)

klyshin_hook: guest-rules-at-door | original: «в чате «можно» → у двери новая сумма» | angle: правила животных без фиксации до оплаты | signal: https://t.me/klyshin_A

wordstat_rework: probe «ключница посуточно» 33 RF → drop | probe «бойлер не работает» 1832 (repair intent) → drop for CASE slot | probe «посуточно с собакой» 777 RF → **final P0 «посуточно с собакой» 777** | clusters: «посуточная квартира с собакой» 403, «снять квартиру посуточно с собакой» 305 | Tyumen 55+11176 «посуточно с собакой тюмень» totalCount 6 → локализация в supply, не в H1

topic_id: B03
slug: posutochno-s-sobakoy-doplata-u-dveri
short_title: собака доплата у двери
subject: pet allowed in listing vs cash fee at check-in
dzen_pattern: case_two_beat
title_seed: «В объявлении — «можно с собакой». У двери попросили 3 000 «за шерсть»»

anti_dup: B01 contactless code; B02 zalog/skolk; not «без залога у двери» (2026-09-23 WP); not generic zalog return

signal_urls:
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

next: research_start --topic-id B03 --title "собака доплата у двери"
