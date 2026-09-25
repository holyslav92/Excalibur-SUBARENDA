# Title inputs B03

Read: research-notes.md, memory/scout/scout-inputs-2026-09-25.md (Klyshin hook + case direction)
Output ONLY valid title-brief.json (JSON object, no markdown fence).

Constraints:
- Двухтактный Klyshin CASE hook (не гайд, не «N вопросов», не «как снять»)
- Тема: pet-friendly фильтр vs отказ/лимит веса у двери, посуточно, гость с крупной собакой
- Wordstat P0 spine под H1 (не в H1 сырой фразой): «посуточная квартира с собакой» 403 RU; «снять квартиру посуточно в тюмени» 3143 RU
- Scout two-beat draft (перефразируй, не копируй дословно): фильтр «можно с собакой» → у двери «до 5 кг, не пройдёт»
- case_delivery_gate HARD: two-beat (. — : ? !); **обязательна цифра-фигура** — ₽ (напр. 3 000 ₽ из рынка), или 3+ цифры, или «двоих/троих»; «5 кг» одной цифрой НЕ проходит gate; no clock HH:MM; length ~40–70; no how-to
- Пример проходящего ритма (свой текст): «В фильтре — «с собакой». У двери насчитали 3 000 ₽ за вес»
- Anti-dup published: B01 код/чужая дверь; B02 залог/скол на плите — другая сцена
- Tyumen в H1 не обязательна
- dzen_pattern: живой кейс (pattern 2) или контраст фильтр vs дверь (pattern 4) — один shape
- subject + angle fields required; verdict PASS

Include: topic_id B03, slug posutochno-tyumen-v-filtre-mozhno-s-sobakoj-u-dveri-otkaz, generated_via derouter line
