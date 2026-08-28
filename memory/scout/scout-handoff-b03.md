# Scout handoff B03 — отель vs посуточная квартира

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-08-28)
klyshin_hook: hotel_vs_daily | original: «Две ночи в командировке. Отель 6800 или квартира 4200 — что выбрать?» | angle: контраст с цифрами до оплаты | signal: https://t.me/klyshin_A
wordstat_rework: probe «посуточно или отель» RU225 445 → «отель или посуточная квартира» 310 → «что лучше отель или квартира посуточно» 16 → supply «квартира посуточно тюмень» RU55 3822 → final P0 «отель или посуточная квартира» 310
wordstat: mcp_kv live | regions 225,55 | P0 «отель или посуточная квартира» 310 RU | supply «квартира посуточно тюмень» 3822 Tyumen | contrast «хостел тюмень» 1133
angle_rotation: checked last N=3 | burn-at-door skip: yes | reason: B01 + recent queue saturated check-in family
season_note: YEKT 2026-08-28 — late summer; cover = current season; NO winter hero
dzen_pattern: 4
dzen_shape_hint: «Отель 6800 или квартира 4200 на две nочи — где съэкономите и где потеряете»
topic_id: B03
slug: otel-ili-kvartira-posutochno-dve-nochi
title_draft: Две ночи. Отель 6800 или квартира 4200 — где съедите лишнее
anti_dup: B01 check-in codes; B02 deposit/plate scratch; live pack_vs_flat/kitchen/reviews/parking/checkout/parents/center — different angle (hotel vs flat choice)
cta: TG https://t.me/Dobriy_dom_72 after checklist; MAX https://max.ru/id660300569233_biz after «у нас так»; phone +7 993 574-83-22; booking https://добрыйдом-72.рф/
interlink: B01 /blog/beskontaktnoe-zaselenie-posutochno-tyumen/ ; B02 /blog/perevel-zalog-za-posutochnuyu-na-vyezde-skazali-ne-vernem/
