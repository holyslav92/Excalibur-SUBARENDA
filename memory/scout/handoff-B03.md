# Scout handoff B03 — субаренда квартиры, риск для гостя

topic_id: B03
slug: subarenda-kvartiry-risk-gostya-posutochno-tyumen
title_draft: Забронировал посуточно. Выяснилось — квартира в субаренде
angle: 7 проверок до оплаты: кто реальный арендатор, право субаренды, что спросить в мессенджере; Тюмень inventory «Добрый дом» (субаренда как бизнес-модель хоста, не шаблоны договоров)
tenant: Добрый дом — посуточная аренда / субаренда Тюмень
klyshin_hook: sublease_chain | original: «субаренда квартиры — где риск для гостя» | angle: проверка прав субарендатора до оплаты

wordstat_preflight: mcp-kv wordstat_get_user_info OK (2026-08-21 YEKT)

wordstat_rework: probe A «субаренда квартиры» 2954 → rework «субаренда квартир посуточно» 304 → «что такое субаренда квартиры» 204 → «субаренда» (similar) 42746 lawyer-cluster skip as P0 → probe B «квартиры посуточно тюмень» 14841 → «снять квартиру посуточно тюмень» 5550 → «субаренда тюмень» 25 weak local → compare 55+11176 «субаренда квартиры» 65 / «субаренда квартир посуточно» 11 → final P0 «субаренда квартиры» 2954 (buyer spine; article angle = guest risk посуточно, not договор образец)

wordstat: mcp_kv live | regions 225,compare225 | P0 «субаренда квартиры» 2954 | P1 «субаренда квартир посуточно» 304 | P1 «квартиры посуточно тюмень» 14841 | compare225 local «субаренда квартиры» 65

season_note: YEKT 2026-08-21 late summer — topic/cover in-season (no winter hero: snow, ice, frozen keybox, −25)

signal_urls:
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://xn---72-9cdob8azaodt6k.xn--p1ai/blog

anti_dup:
- B01: бесконтактное заселение / код от чужой двери — different pain
- B02: залог / скол на плите — different pain
- WP slugs blocked (existing live articles): uборka-syomnoj-kvartiry, skrytye-doplaty, sosedy, czena-ot, pokazaniya-schyotchikov, syomnaya-kvartira-chto-nelzya, internet-i-tv, pravila-prozhivaniya-v-otele, oczenka-kvartiry, chto-vhodit-v-stoimost

bank_evaluation_2026-08-21:
- deposit_return_cleaning — skip anti-dup B02 + WP uборka-syomnoj-kvartiry
- hidden_fees — skip anti-dup WP skrytye-doplaty
- neighbors_relations — skip anti-dup WP sosedy
- price_from_ads — skip anti-dup WP czena-ot
- utilities_counters — skip anti-dup WP pokazaniya-schyotchikov
- contract_bans — skip anti-dup WP syomnaya-kvartira-chto-nelzya
- sublease_chain — PICK B03 (P0 2954)
- check_in_contactless — skip anti-dup B01
- move_one_day — weak/generic (переезд чеклист ~5; аренда квартиры на сутки 2433 без guest-pain hook)
- internet_tv_rental — skip anti-dup WP internet-i-tv
- alt rejected: поздний заезд 1635 — hotel-heavy, not host посуточно spine
