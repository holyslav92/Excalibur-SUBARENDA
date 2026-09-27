# Title inputs B03

Read: research-notes.md, memory/scout/scout-inputs-2026-09-27.md, published-titles-only.md
Output ONLY valid title-brief.json (JSON object, no markdown wrapper).

topic_id: B03
slug: posutochno-tyumen-bojler-pogas-nochyu-holodnyj-dush

## Scout case hook (angle)
Klyshin rework: не счётчики ЖКХ, а горячая вода/бойлер в посуточной — гость уже внутри, холодный душ, хозяин «завтра мастер».
case_hook_ru: В объявлении — нормальный душ. В 23:10 из крана пошла ледяная вода, на табло бойлера ноль.

## Title direction (two-beat H1, NOT how-to)
Two beats like B01/B02: promise in card → night break (23:10, ice water, boiler off). NOT «5 вопросов», NOT colon SEO list, NOT «полный гайд».
Example shape only (do not copy verbatim): «В карточке — душ и полотенца. В 23:10 бойлер погас, из крана — лёд»

## Wordstat demand spine (under H1, not raw in title)
- final P0 RU225: «квартиры посуточно тюмень» — 9212
- alt: «снять квартиру посуточно в тюмени» — 3175
- narrow: «бойлер квартира аренда» — 13 (do not stuff boiler SEO into H1)

## Anti-dup published titles
- B01: Оплатил квартиру посуточно. Код прислали от чужой двери
- B02: Снял квартиру посуточно. Залог не вернули — нашли скол на плите

## Required JSON fields
topic_id, h1, title (same as h1), subject, angle, verdict PASS.
Match B02 richness where useful: pain_scene, wordstat spine, checks, h2_candidates, stickers, rejected_variants, char_count.
Tyumen optional in H1. ~50–70 characters. Strong verb, cable case scene.
