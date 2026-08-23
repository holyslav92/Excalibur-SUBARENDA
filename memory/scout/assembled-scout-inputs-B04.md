# Scout assembled inputs — B04 (Добрый дом / посуточная)

## Task
topic_id: B04
tenant: Excalibur-SUBARENDA / Добрый дом — посуточная аренда Тюмень
hook bank id: utilities_counters

## Anti-dup (do not duplicate angles)
published-titles.md: B01 заселение/код, B02 залог/скол на плите
EXCALIBUR_RECENT_WP_POSTS slugs: dogovor-arendy-pravila, otmena-bronirovaniya, pereveli-predoplatu, priehal-v-sem-utra, zabroniroval-posutochno-subarenda, perevel-zalog, beskontaktnoe-zaselenie, uborka-syomnoj, skrytye-doplaty, sosedy, czena-ot, internet-i-tv
NO existing slug on utilities/JKH/счётчики — green field.

## Klyshin hook (original)
id: utilities_counters
original: «показания счётчиков — не переплатить ЖКХ»
angle: как фиксировать при посуточной/субаренде; «коммуналка включена» vs доплата на выезде
signal: https://t.me/klyshin_A (angle bank; live feed Aug 2026 — сделки/ЕГРН, не ЖКХ; angle only)

## Wordstat preflight
wordstat_get_user_info: OK (MCP-KV Yandex Cloud)

## Wordstat probes (regions 55+11176 unless noted)
| probe | volume |
|-------|--------|
| показания счетчиков аренда | 3 |
| жкх аренда квартиры | 1 (format odd) |
| коммунальные платежи аренда | 24 |
| коммунальные платежи при аренде квартиры | 2 |
| что значит коммунальные платежи включены без счетчиков | 4 |
| жкх аренда | 6 |
| что такое жку при снятии квартиры | 13 |
| коммунальные платежи квартира | 105 |
| коммунальные платежи | 1051 |
| показания счетчиков | 16810 |
| показания счетчиков тюмень | 8360 |
| подать счетчики тюмень | 256 |
| оплатить коммунальные услуги тюмень | 61 |

Compare RU 225:
| phrase | volume |
|--------|--------|
| коммунальные платежи квартира | 12751 |
| показания счетчиков тюмень | 9428 |
| что такое жку при снятии квартиры | 652 |
| жкх аренда | 740 |

## Rework decision
Weak on rental+счётчики combo → localized Tyumen + buyer jargon:
- spine: коммунальные платежи квартира (105 local / 12751 RU)
- rental guest: что такое жку при снятии квартиры (13 / 652)
- counter fix: показания счетчиков (16810 / тюмень 8360)
Final P0 phrase: «коммунальные платежи квартира» 105

## Dzen pattern
dzen_pattern: 3 (страх денег → инструкция в §1)
dzen_shape_hint: «ЖКХ включено» в объявлении — что снять на заселении, чтобы не доплатить на выезде

## Title draft (Klyshin rhythm, not final H1)
«Коммуналка в цене» — на выезде прислали доплату по счётчикам

## Short title for research_start
Коммуналка в цене — доплата по счётчикам на выезде

## Proposed slug
kommunalka-v-cene-doplata-po-schetchikam-na-vyezde

## signal_urls (≥2)
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://добрыйдом-72.рф/blog/skrytye-doplaty-pri-arende-kvartiry-kak-ne-pereplatit (скрытые доплаты — sibling, не дублировать)

## Stickers / H2 seeds from Wordstat
- что такое жку при снятии квартиры
- что значит коммунальные платежи включены без счетчиков
- показания счетчиков на заселении / выезде
- коммунальные платежи квартира — кто платит при посуточной

Write handoff in Russian per scout skill checklist fields.
