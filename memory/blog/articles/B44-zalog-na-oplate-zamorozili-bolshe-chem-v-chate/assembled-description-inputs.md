# Description inputs B44

Return ONLY valid description-brief.json. NO BLOCKER. No meta about scripts.

H1: В чате посуточно: залог 3 000 ₽ — на оплате заморозка 11 400, кода нет
Angle: в чате «залог три тысячи»; гость жмёт оплату — банк показывает заморозку 11 400 ₽; код от двери ещё не прислали; баланс упал, непонятно залог это или всё сразу.
Teaser for Dzen card — NOT duplicate H1, NOT lead copy (lead opens with «Залог три тысячи, не переживайте» — хозяин в чате, 11 400 на экране, кода нет). Klyshin rhythm, 1–2 sentences (~120–220 chars).
Brand: Добрый дом (author_brand field only). HARD FAIL if «Добрый дом» appears in description text in same sentence as any ₽/руб digit — keep brand OUT of description body OR mention brand with zero money digits nearby. No Шакin. One sum 11 400 or 3 000 as hook OK without brand name. No 3000→11400 ladder.
PREVIOUS FAIL: paired «Добрый дом» with 11 400 ₽ in one teaser — rewrite.
Geo: Тюмень. Guest pain: hold vs залог, состав авторизации до кода.
Wordstat P0: квартира посуточно залог.
