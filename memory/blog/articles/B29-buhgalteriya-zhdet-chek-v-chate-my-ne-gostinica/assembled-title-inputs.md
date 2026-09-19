# Assembled title inputs — B29

**Return ONLY valid JSON for title-brief.json; do NOT return DEROUTER TITLE BLOCKER**

Ты — Derouter utility tier Title agent. Верни JSON title-brief.

## Requirements (HARD)

- H1 = two-beat stop-factor guest night: [paid/stayed]. Then [accounting horror] / quote / «мы не гостиница»
- Two beats: period, em dash, colon, or contrast («Только», «А потом»)
- MUST include figure: **2 ночи** (editorial case — NO invented ₽ sum in research)
- BAN: «что проверить», «как снять», «разберём», «N советов», **HH:MM in H1** (Klyshin hook has 10:00/22:00 — do NOT put clock times in H1)
- BAN: ЕГРН, наследство, ипотека, Шакин, риэлтор, Клышин, +79032334201
- Guest audience: **business-trip guest** who paid for **2 nights** in Tyumen apartment; AFTER checkout accounting asks for receipt; host in chat: «мы не гостиница», no fiscal check
- ~40–70 chars in h1 (max gate ~85)
- Tyumen optional in H1 (P0 demand spine «квартиры посуточно тюмень» — under H1, not SEO tail)
- klyshin_title_shape: **3** — direct speech + what surfaced (accounting vs chat refusal)
- dzen_pattern: **2** — case with beats, not N tips list

## Scout handoff

- topic_id: B29
- slug: buhgalteriya-zhdet-chek-v-chate-my-ne-gostinica
- klyshin_hook: sept_business_trip | original rhythm only: «Звонок в 10:00. Заселился в 22:00.» — **do not copy times into H1**
- title_draft calibration: «Оплатили 2 ночи по счёту. Бухгалтерия просит чек — в чате: «мы не гостиница»»
- dzen_shape_hint: «Оплатили 2 ночи. Бухгалтерия просит чек — «мы не гостиница»»
- P0: «квартиры посуточно тюмень» 4423 (55+11176); document spine «чек командировка проживание» 307
- angle: guest expected hotel-style receipt; private host refuses after payment; bank transfer + chat ≠ guaranteed advance report pack
- anti_dup: NOT B15 Wi‑Fi/10:00 call desk; NOT B08 silence after prepay; NOT B22 passport/code; NOT spravka-dlya-buhgalterii how-to repeat
- case_number: **2 ночи** (no ₽ invented)

## Editorial case figures (from research-notes)

- Fixed: Tyumen, business guest, **2 nights**, paid before/during stay, accounting request **after** checkout
- Typical host chat pattern: «мы не гостиница», «чек не дадим», «скиньте выписку», «пришлём потом»
- Do NOT invent payment amount; sum not in brief

## Anti-dup H1 (published)

NOT: B15 ««Рабочий стол» обещали. За 11 400 ₽ — журнальный столик» (Wi‑Fi, not receipts)
NOT: B08 prepay silence, B22 passport, B02 deposit checkout
NOT repeat any title in published-titles-only.md in article dir

## Good calibration shapes (ORIGINAL text only — refine length)

- «Оплатили 2 ночи. Бухгалтерия просит чек — в чате: «мы не гостиница»»
- «Оплатили 2 ночи по счёту. Бухгалтерия просит чек — «мы не гостиница»»
- Shape anchor: nights paid + accounting demand + host quote refusal (NOT legal essay, NOT how-to)

## Output JSON schema

```json
{
  "topic_id": "B29",
  "h1": "...",
  "title": "...",
  "slug": "buhgalteriya-zhdet-chek-v-chate-my-ne-gostinica",
  "subject": "...",
  "angle": "...",
  "klyshin_title_shape": 3,
  "wordstat_p0": "квартиры посуточно тюмень",
  "verdict": "PASS"
}
```
