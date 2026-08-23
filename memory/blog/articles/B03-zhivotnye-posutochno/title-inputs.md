# Title inputs B03

topic_id: B03
slug_draft: v-obyavlenii-mozhno-s-kotom-v-pravilah-shtraf
tenant: Добрый дом, посуточная аренда Тюмень

## handoff
- klyshin_hook: pets_short_term | «договор аренды — пункт про животных: что спросить до оплаты»
- dzen_pattern: 3 (страх → инструкция в §1)
- dzen_shape_hint: страх «можно с питомцем» → 5 вопросов до оплаты
- title_draft: В объявлении написали «можно с котом». В правилах — штраф за шерсть
- wordstat P0: «аренда квартиры с животными» 1095 RU / 4 Tyumen
- stickers: договор аренды квартиры с животными 185; посуточно с животными 45

## reader_problem
Гость едет с котом на посуточную, видит «можно с животными» в объявлении, не сверяет с правилами и договором до оплаты — на месте штраф или доплата.

## anti_dup (published titles)
- B01: Оплатил квартиру посуточно. Код прислали от чужой двери
- B02: Снял квартиру посуточно. Залог не вернули — нашли скол на плите
Не дублировать: коды/заселение, залог/скол, топ-N, гайд 2026, полный список.

## constraints
- Klyshin cable rhythm: короткий удар, сцена, противоречие
- ~50–70 символов; сильный глагол; без SEO-хвоста и «Тюмень» в H1 (опционально)
- Demand spine P0 под H1, не сырая фраза в заголовок
- Pattern 3: страх в H1 → инструкция в лиде (или cable scene как B01/B02)
- Запрещено: топ-N, гайд 2026, полный список, label head, кликбейт

Output ONLY valid title-brief.json (JSON object, no markdown wrapper).
Fields: topic_id, h1, title, subject, angle, verdict (PASS).
