# Scout inputs — слот 2026-09-25 YEKT (12:11)

## Constraints (slot)
- Один CASE «Добрый дом», не гайд. Гостевая боль, не Клышин-юрист (ЕГРН/суд).
- Anti-dup: B01 код/чужая дверь; B02 залог/скол плита; не повторять недавние WP (залог в фильтре, предоплата, комиссия, мин. сутки, бельё…).
- Wordstat preflight: wordstat_get_user_info OK (2026-09-25).

## Wordstat (MCP-KV, regions 225 — вся РФ)
| probe | total / top |
|-------|-------------|
| посуточно с собакой | 777 — «посуточно с собакой» 777, «посуточная квартира с собакой» 403, «снять квартиру посуточно с собакой» 305 |
| ключница посуточно | 33 (слабо) |
| бойлер не работает | 1832 (общий ЖКХ, не только посуточно) |
| соседи шум квартира посуточно | API empty/low |

## Wordstat Tyumen (55+11176)
«посуточно с собакой тюмень» — totalCount 6 (слабо локально; supply = Тюмень, demand spine = RF «посуточно с собакой» 777).

## Rework log
1. Klyshin angle: «кажется договорились → у двери новое условие» (механика, не сюжет канала).
2. Hook bank: hidden rules / доплата / залог под другим названием.
3. Weak Tyumen volume → final P0 = **«посуточно с собакой»** (777 RF) + cluster «снять квартиру посуточно с собакой» (305).
4. Skip rejected: pure «бойлер» (encyclopedia repair intent); «ключница» (33); duplicate zalog-at-door posts.

## P0 topic
- topic_id: **B03**
- subject: **собака / pet fee / «можно с животными» vs доплата при заселении**
- title_seed (two-beat): «В объявлении — «можно с собакой». У двери попросили 3 000 «за шерсть»»
- slug_hint: posutochno-s-sobakoy-doplata-u-dveri
- klyshin_hook: guest-rules-at-door | original: «договорились в чате → на месте другие цифры»

## signal_urls
- https://t.me/klyshin_A
- https://добрыйдом-72.рф/blog/
- https://t.me/Dobriy_dom_72

## Interlink candidates (live siblings, не B01/B02 duplicate angle)
- /blog/bez-zaloga-v-filtre-zalog-u-dveri/
- /blog/kvartira-posutochno-tyumen-bez-komissii-na-ekrane-oplaty/
- /blog/instrukciya-zaseleniya-posutochno-ne-tot-podezd/
- /blog/posutochno-tyumen-oplatili-3-nochi-vnutri-chuzhie-chemodany/
