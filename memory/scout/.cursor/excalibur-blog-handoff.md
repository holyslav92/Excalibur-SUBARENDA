topic_id: B32  
title: В карточке 4 200 ₽. На оплате — 5 050. Ключ ещё не брали  
slug: v-kartochke-4200-na-oplate-5050-klyuch-eshe-ne-brali  
primary_query: квартиры посуточно тюмень комиссия цена в приложении  

dzen_pattern: 2  
dzen_shape_hint: «В карточке 4 200 ₽» → «На оплате 5 050» до ключа  

klyshin_hook: kitchen_vs_hotel + hidden_fees mechanics | original: «Три ночи. Кухня „есть“ — или каждый день кафе?» | reworked: финальная цена в приложении до получения ключа; гость видит одну цену за ночь, а на оплате агрегатор добавляет сервисный сбор или уборку | angle: сравнить квартиру и отель по честной итоговой сумме, не по цифре в карточке | signal: https://t.me/klyshin_A  

wordstat_preflight: mcp-kv wordstat_get_user_info OK  

wordstat_rework: probe «скрытая доплата посуточно» API totalCount-only → «посуточно комиссия» 1903 (225) → «авито посуточно комиссия» 1036 (225) → «квартиры посуточно без комиссии» 328 (225) → «отель или посуточная квартира» 280 (225) / 7 (55+11176) → «посуточно или отель» 355 (225) → final P0 «квартиры посуточно тюмень» 4409 (55+11176) | compare 9372 (225) | clusters tried: комиссия, без комиссии, отель или посуточная квартира, посуточно или отель, квартиры посуточно Тюмень  

wordstat: mcp_kv live | regions 55,11176,compare225 | P0 «квартиры посуточно тюмень» 4409/9372 | supporting: «посуточно комиссия» 1903 | «квартиры посуточно без комиссии» 328 | «отель или посуточная квартира» 280  

angle_rotation: checked last N=3 | burn-at-door skip: no (last3 = docs/cleaning/card/chemodany) | skip saturated: kod, zalog-skol, predoplata-live-slugs  

external_signal: guest final checkout line vs card price; compare hotel vs flat without surprise fees  

signal_urls: https://t.me/klyshin_A
