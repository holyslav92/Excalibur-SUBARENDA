# Title inputs B03

Read: .cursor/excalibur-blog-handoff.md, published-titles-only.md, research-serp.json (SERP angles only)

Output ONLY valid title-brief.json (JSON object, no markdown wrapper, no code fences).

## Topic

- topic_id: B03
- slug: sosedi-postuchali-v-dver-nochyu-gost-posutochno-chto-delat-segodnya
- tenant: Добрый дом — посуточная аренда в Тюмени (supply); demand RF-wide

## Scout handoff

- klyshin_hook: neighbors_relations | original: «соседи в съёмной — без конфликтов» | angle: 7 шагов — гость посуточно не будит подъезд
- dzen_pattern: 3 (страх → инструкция в §1)
- dzen_shape_hint: страх ночного шума/стука → что делать хозяину с гостем посуточно сегодня
- wordstat P0 spine: «шум от соседей ночью» 213 (225 compare)
- wordstat secondary: «ночью шум от соседей что делать» 10 (225)
- Tyumen supply: «аренда квартир посуточно тюмень» 208 (55+11176)

## Constraints (HARD)

- ONE h1/title variant, verdict PASS
- Klyshin cable rhythm: короткий удар, сцена, сильный глагол (~50–70 chars)
- dzen_pattern 3 shape (свой текст): страх/риск → инструкция, как «Залог 5 000 ₽: когда удержат, когда вернут» — но про соседей/ночной шум/гостя посуточно
- Wordstat P0 — demand spine ПОД H1, не сырая SEO-фраза в заголовок
- «Тюмень» в H1 опционально — не SEO-набивка
- Бан: «полный гайд», «2026», «топ N», label head, SEO-хвост, CAPS, пустой кликбейт
- Не плагиат @klyshin_A

## Anti-dup (published titles)

- B01: «Оплатил квартиру посуточно. Код прислали от чужой двери» — НЕ коды/заселение
- B02: «Снял квартиру посуточно. Залог не вернули — нашли скол на плите» — НЕ залог/скол/депозит

## Required JSON fields (minimum)

topic_id, h1, title, subject, angle, verdict

Optional but welcome (B02 style): char_count, pain_scene, wordstat, checks, b01_b02_delta, lead_hint, h2_candidates, stickers, rejected_variants, generated_via
