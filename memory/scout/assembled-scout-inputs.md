# Scout assembled inputs — B15 slot 2026-09-08 YEKT

**Return handoff markdown for `.cursor/excalibur-blog-handoff.md` per scout skill. Do NOT return DEROUTER SCOUT BLOCKER unless API truly failed.**

## Date / tenant

- today: 2026-09-08 (Asia/Yekaterinburg / YEKT)
- season: early September, summer — NO winter hero on cover
- tenant: Добрый дом, посуточная Тюмень, case Dzen (NOT guide)
- repo: Excalibur-SUBARENDA only

## Angle rotation (last N=3 published)

- B12: «тихий центр» + стройка/кран
- B13: код + пустая ключница (burn-at-door family — SKIP new burn-at-door)
- B14: «тихий дом» + соседи музыка (neighbors family — SKIP)

## WP recent anti-dup (live catalog, NOT in published-titles yet)

ALREADY LIVE — do NOT repeat angle/H1:
- zaselilsya-v-22-00-v-10-00-sozvon-wi-fi-ne-vyderzhal (командировка Wi‑Fi)
- sozvonili-v-10-00-posutochno-k-22-30-koda-ne-bylo-otchet-gorit
- kvartira-posutochno-tyumen-poezd-v-07-20-zaezd-s-14-00
- otmenil-bron-posutochno-za-sutki-2-500-po-usloviyam-ssylki
- zalog-5-000-obeschali-vernut-utrom-utrom-napisali-posle-uborki
- posutochno-napisali-postelnoe-est-na-krovati-golyj-matras
- goryachaya-voda-i-bojler-pri-zaselenii-posutochno

Queue hooks 3→6→8→7 all used in ledger. Next fresh hook: **dog_breed_fee** (parked, restore eligible).

## Klyshin hook (original)

- hook_id: dog_breed_fee
- hook_ru: «Можно с собакой» — у двери доплата за породу или залог ×2
- angle: guest books with small/medium dog; chat says pet OK; at check-in host demands breed surcharge or doubled deposit «за шерсть/запах»; guest already paid nights + travel with dog
- klyshin mechanics: quote host → «Нет. Так не заселяем.» → lockpick: «Какая доплата за питомца и когда?» → moral: сначала правила питомца письменно, потом ключ
- NOT legal (no ЕГРН/наследство/ипотека)

## Wordstat (live MCP-KV, do not invent)

### wordstat_get_user_info: OK (Yandex Cloud API)

### Probes

| phrase | regions | top volume |
|--------|---------|------------|
| посуточная квартира с собакой | 225 | 571 |
| снять квартиру посуточно с собакой | 225 | 429 |
| квартира посуточно с собакой | 55+11176 | 8 (weak local — rework) |
| квартиры посуточно тюмень | 55+11176 | 5134 |
| квартиры посуточно тюмень | 225 | 10865 |
| аренда квартиры посуточно | 55+11176 | 704 |

### Rework log

probe «квартира посуточно с собакой» 8 (55+11176) → guest intent real at RU 571 → anchor P0 spine «квартиры посуточно тюмень» 5134/10865; angle stays pet surcharge at door

### final P0

- phrase: квартиры посуточно тюмень
- volume_tyumen: 5134 (regions 55+11176)
- volume_ru: 10865 (region 225)
- guest pain phrase: посуточная квартира с собакой (571 RU)

## Title draft (two-beat calibration, NOT final)

«Можно с собакой» написали. У двери доплатили 3 000 за «крупную породу»

## topic_id / slug proposal

- topic_id: B15
- slug: mozhno-s-sobakoj-u-dveri-doplatili-za-porodu

## Published titles anti-dup (B01–B14)

See shared/published-titles.md — no dog/pet article yet.

## dzen_pattern

Prefer 2 (case_with_sums) or 3 (fear_to_instruction in body only — NOT in H1)
