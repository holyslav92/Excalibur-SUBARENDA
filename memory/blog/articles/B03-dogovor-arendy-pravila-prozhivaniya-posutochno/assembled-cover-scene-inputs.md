# Cover-scene inputs B03 — Добрый дом

Output ONLY valid JSON matching scene-draft.json schema. No markdown wrapper.

## Meta
- topic_id: B03
- tenant: Добрый дом, Тюмень, посуточная аренда
- season: лето 2026 (август), солнечно, зелень — НЕ зима, НЕ снег
- H1 context (do NOT copy verbatim): Перевёл предоплату — потом прочитал 7 запретов в договоре
- cover_hook from cover-text.json: Перед оплатой прочитайте правила аренды
- highlight: оплатой
- sticky: Сначала прочитайте условия

## Wordstat stickers (use 1-3)
- квартиры посуточно тюмень — 6446
- договор аренды квартиры — 1974

## Anti-repeat (14d — DO NOT reuse)
- B01: night entrance phone code, keybox suitcase
- B02: kitchen chip on stove August evening

## Cover rules
- brand_logo_paste: NO logo in generation, TOP-RIGHT empty pad 8-12%
- cover_phone post-composite only: +7 (993) 574-83-22 bottom-left, NOT in logo pad
- light & bright high-key #FFFFFF, sun flare, NO dark cinematic
- meme cat or catalog people-meme sticker ≤12% bottom-left
- NO Shakin/host face, NO WordPress UI
- WOW magazine poster, bold Russian display type

## H2 anchors for 7 inlines
1. Быстрый инсайт — labels: 7 запретов, 3 минуты чтения, правила до оплаты, оплата = согласие
2. Почему перевод денег иногда считается согласием — ст. 438 ГК, оферта, оплата как акцепт
3. Вот где подставят — заезд 15:00, 2 гостя, ключи, отмена, балкон
4. Семь пунктов до перевода — часы, гости, ключи, курение, отмена, назначение, залог
5. Что проверить за 3 минуты — оферта, адрес, рейс, гости, отмена, ключи, чат
6. У нас в «Добром доме» — условия на сайте, бесконтактный заезд, коды заранее
7. Частые вопросы — перевод≠согласие, код другу, ранний заезд, залог

## Logo inline slots (factory paste after split)
inline_1, inline_3, inline_7 — TOP-RIGHT empty pad on those panels only

## Visual types preference
inline_1: labeled_checklist
inline_2: comparison_table (оплата vs акцепт)
inline_3: comparison_table (реклама vs договор)
inline_4: labeled_checklist (7 пунктов)
inline_5: process_flow (3 минуты чеклист)
inline_6: guest_checkin_scene (бесконтактный заезд)
inline_7: schema_faq_ui

## Required JSON fields
cover_emotion, scene_hint (cover), cover_motifs (composition, location, meme, prop_set, sticker_set, joke), wordstat_stickers, cover_phone_cta, logo_paste_inline_slots, slots.inline_1..7.scene_hint
