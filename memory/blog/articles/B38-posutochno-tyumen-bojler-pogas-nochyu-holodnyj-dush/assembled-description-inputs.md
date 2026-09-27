# Description inputs B38

Return ONLY valid description-brief.json. NO BLOCKER.

H1: В карточке был душ. В 23:10 бойлер погас — вода стала ледяной
dzen_pattern: 2
Angle: в карточке «просторный душ, всегда горячая вода»; пара после 12 часов в дороге; в 23:10 вода тёплая полторы минуты — потом ледяная; индикатор бойлера мигает красным за декоративной панелью; хозяин в 23:26: «мастер завтра». Guest pain: вы уже внутри, ребёнок устал, душ нужен сейчас — а ответ переносит проблему на утро; «всегда горячая» в объявлении ≠ вода из крана ночью.
Teaser for Dzen card — NOT duplicate H1 (avoid echoing «23:10», «бойлер погас», «в карточке был душ» as in title). NOT lead copy (lead opens with суббота 26 сентября, дорога из Екатеринбурга, 4 200 ₽, 8 400 ₽, 5 000 ₽ залог — do not echo that opening or repeat those sums). Klyshin rhythm, 1-2 sentences (~120-220 chars).
Brand: Добрый дом (author_brand field only). HARD: description text must NOT contain «Добрый дом» together with 3–5 digit amounts (gate). No guest-burn price ladder. No Шакин / The Риэлтор. Prefer NOT putting brand name in teaser if awkward — author_brand stays in JSON.
Geo: Тюмень. Guest pain: бойлер ночью, ледяной душ, «мастер завтра», накопительный водонагреватель, переписка после заселения, посуточная аренда.
Wordstat P0: квартиры посуточно тюмень (9212).
Key hooks (pick one): «мастер завтра» в полночь, когда вы уже под душем; «всегда горячая» — про строку в объявлении или про кран в 23:10; бойлер за панелью, пока не замёрзнете; один вопрос про автомат и объём бака до оплаты.
Stickers from title: холодная вода ночью, бойлер выключился, хозяин обещает мастера завтра, переселение или возврат.

Article lead (DO NOT truncate): composite Tyumen case, late shower after long drive, boiler indicator behind panel.
Research voice: отличить плановое ГВС города от поломки в квартире; фиксировать переписку; не обещать время мастера от Доброго дома.
