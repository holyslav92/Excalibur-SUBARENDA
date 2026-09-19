# Description inputs B29

Return ONLY valid description-brief.json. NO BLOCKER.

H1: Оплатили 2 ночи. Бухгалтерия просит чек — «мы не гостиница»
dzen_pattern: 3
Angle: командировочный гость оплатил 2 ночи в Тюмени переводом; после выезда бухгалтерия требует чек, хозяин: «мы не гостиница, чека не будет». Guest pain: посуточная ≠ гостиница с кассой; документы надо спрашивать до перевода, не после.
Teaser for Dzen card — NOT duplicate H1, NOT lead copy (lead opens with «Где чек за проживание?» and «2 ночи в Тюмени вы оплатили переводом» — do not echo those openings). Klyshin rhythm, 1-2 sentences (~120-220 chars).
Brand: Добрый дом (author_brand field only). HARD: description text must NOT contain the words «Добрый дом» if any 3–5 digit number appears. No Шакин. No price ladder. No guest-burn arithmetic.
Geo: Тюмень. Guest pain: авансовый отчёт, чек «Мой налог», отказ в чате после оплаты.
Wordstat P0: квартиры посуточно тюмень.
