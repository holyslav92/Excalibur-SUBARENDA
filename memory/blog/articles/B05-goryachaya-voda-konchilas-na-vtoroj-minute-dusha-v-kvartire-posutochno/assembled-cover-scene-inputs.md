# Cover-scene inputs B05

H1: Горячая вода была. На второй минуте душ — холод
cover hook: Вода кончилась прямо в душе
highlight: кончилась
sticky: А бойлер просто висит
Season: late August 2026 Tyumen — warm summer evening, NO snow NO ice NO winter coats
Phone in cover scene: +7 (993) 574-83-22 on tape/note in bathroom or door area — IN SCENE, not post-paste pill
Logo: factory paste AFTER gen only — empty TOP-RIGHT pad 8-12%; NO drawn logo
Cover style: person in scene (wet tired guest in shower/bathroom) + large Cyrillic hook headline — NOT empty stock room
Max 1 cat meme across all 8 images (prefer people-meme Roll Safe or Harold on one inline only)
Logo slots after gen: cover + inline_1, inline_3, inline_7

Case: guest after late flight, self check-in, prepaid 3500₽; chat said «горячая вода есть»; shower warm 2 min then ice; storage boiler empty/not reheated.

H2 anchors:
1. Две минуты, после которых уже не работает инструкция
2. Что на самом деле происходит с баком
3. Вопрос был не про бойлер
4. Две отмычки перед переводом
5. Наш вывод после этой ночи
6. (technical checklist) — use inline_6 labels
7. Если нужна квартира в Тюмени на ночь — pre-pay questions

Output ONLY valid JSON (no markdown fences):
{
  "cover_emotion": "...",
  "cover_motifs": { composition, location, meme, prop_set, sticker_set, joke },
  "wordstat_stickers": ["посуточно тюмень", "бойлер в квартире", "нет горячей воды"],
  "slots": {
    "cover": { "scene_hint": "≤200 chars", "alt": "..." },
    "inline_1" .. "inline_7": { "scene_hint": "≤180 chars", "alt": "..." }
  }
}

Keep scene_hint compact English/RU mix like B04. NO Shakin/host identity. Guests OK in cover scene.
