# Scout inputs — B03 — 2026-08-23 (YEKT summer)

## Wordstat preflight
- mcp-kv wordstat_get_user_info: OK (Yandex Cloud API)

## Published anti-dup (НЕ повторять)
- B01: коды/бесконтактное заселение
- B02: залог/скол на плите
- dogovor/pravila, otmena bronirovaniya, predoplata/pravila, early check-in, sublease, uборка, skrytye doplaty, sosedi, cena ot, internet TV

## Klyshin hook (contract_bans angle + pets)
- hook_id: pets_short_term
- original: «договор аренды — пункт про животных: что спросить до оплаты»
- angle: гость с питомцем посуточно — 5 вопросов до перевода денег
- signal: https://t.me/klyshin_A (angle bank contract_bans + pets cluster)

## Wordstat rework log
- probe «показания счетчиков аренда» 75 RU → слабый buyer cluster
- probe «жкх аренда квартиры» 256 RU → не buyer
- probe «продление аренды квартиры» 1025 RU → long-term bias
- probe «аренда квартиры с животными» RU 225: **1095** | Tyumen 55+11176: **4**
- probe «аренда квартиры посуточно с животными» RU: **45**
- probe «договор аренды квартиры с животными» RU: **185**
- rework: локализация на посуточную/субаренду Тюмень, buyer-жаргон «с питомцем», «можно с животными», не long-term
- **final P0:** «аренда квартиры с животными» **1095** (RU 225); Tyumen spine «посуточно с животными» 45

## Dzen pattern
- dzen_pattern: 3 (страх → инструкция в §1)
- dzen_shape_hint: «В объявлении «можно с питомцем» — а в правилах штраф. Что спросить до оплаты»

## Topic assignment
- topic_id: B03
- title_draft: «В объявлении написали «можно с котом». В правилах — штраф за шерсть»
- tenant: Добрый дом, посуточная Тюмень, август 2026, лето (не зима на обложке)
- supply: только посуточная/субаренда Тюмень
