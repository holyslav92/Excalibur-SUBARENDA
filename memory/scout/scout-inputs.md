# Scout inputs — 2026-08-25 Asia/Yekaterinburg

## Tenant & date
- Tenant: Добрый дом — посуточная аренда / субаренда Тюмень
- Date: 2026-08-25 (лето, обложка — текущий сезон, не зима)
- topic_id next: B03 (B01, B02 published in repo ledger)

## Anti-dup (HARD — do NOT repeat angles)
**Repo published (ledger):**
- B01: бесконтактное заселение / код от чужой двери
- B02: залог не вернули / скол на плите

**Site blog already live (titles only — do NOT duplicate):**
горячая вода, соседи ночью, скрытые доплаты, собака, паспорт, договор, отмена брони, вечеринки, ранний заезд, субаренда

**Skip families from bank:** burn-at-door saturated; early_checkin used; hidden_fees angle used.

## Angle rotation (last N=3)
Published in repo: B01 (burn-at-door codes), B02 (deposit hold).  
burn-at-door skip: yes for NEW burn-at-door; parents_sept_uni is different family (parents/uni/2-4 nights).  
Reason: queue hook #1 for window 26–28.08 YEKT; not код/заселение/залог duplicate.

## Klyshin hook (queue slot 1)
- hook_id: parents_sept_uni
- queue_window: 2026-08-26 — 2026-08-28 YEKT (today 25.08 — next slot, pre-sept uni season)
- original hook_ru: «Привёз сына в вуз. Три ночи. В объявлении — „рядом с вузом“.»
- angle: 2–4 ночи на оформление, не годовая аренда; что проверить кроме «рядом»
- lockpick: сколько минут пешком до корпуса?
- klyshin_signal rhythm: §1 = ожог сейчас; moral: сначала маршрут/корпус, потом оплата
- dzen_pattern_prefer: 2 (кейс) или 5 (локальный+сезонный сентябрь/вуз)

## Wordstat preflight
wordstat_get_user_info: OK (2026-08-25, MCP-KV Yandex Cloud API)

## Wordstat live probes (regions 55+11176 Tyumen+область; compare RU 225)

| probe | freq 55+11176 | notes |
|-------|---------------|-------|
| квартира посуточно тюмень | 5875 | P0 spine; top: квартиры посуточно тюмень 5875, снять квартиру посуточно в тюмени 1902 |
| снять квартиру посуточно в тюмени | 1902 | P1 |
| снять квартиру на сутки тюмень | 391 | weak alone |
| аренда квартир посуточно тюмень | 207 | P2 |
| аренда квартиры на несколько дней | API empty | rework skip phrase |
| квартира посуточно рядом с вузом | API empty | too narrow |
| аренда квартиры на несколько дней тюмень | API empty | too narrow |

**Compare RU 225:**
| probe | freq 225 |
|-------|----------|
| квартира посуточно | 1271992 |

## Wordstat rework log (for handoff)
probe «аренда квартиры на несколько дней» empty → probe «квартира посуточно рядом с вузом» empty → probe «снять квартиру на сутки тюмень» 391 → probe «снять квартиру посуточно в тюмени» 1902 → final P0 «квартира посуточно тюмень» 5875

clusters tried: multi-day rental, vuz proximity, daily Tyumen, посуточно Tyumen spine

## Final P0
«квартира посуточно тюмень» — 5875 (regions 55+11176)
Top exact phrase from API: «квартиры посуточно тюмень» — 5875 (use in wordstat line for gate seed «квартиры посуточно»)
National compare: «квартира посуточно» — 1271992 (region 225)

## Gate note for handoff wordstat line
Must include buyer seed «квартиры посуточно» with frequency in wordstat: field (e.g. P0 «квартиры посуточно тюмень» 5875).

## External signals (today)
1. https://t.me/klyshin_A — rhythm reference: lockpick question «А где спит бабушка?» → map to guest «Сколько минут пешком до корпуса?»; refusal beat «Нет. Так не работает.»
2. https://добрыйдом-72.рф/blog/ — live titles confirm anti-dup list; site covers hot water/neighbors/fees/dog/passport/contract/cancel/parties/early checkin/sublease/deposit/code — NOT parents/uni sept window
3. https://dzen.ru/holyslav — tenant dzen channel (signal URL canon)
4. https://t.me/holyslav92 — holyslav signal

## Dzen / RF gates
- Read dzen-content-rules + rf-blocked: no Meta/IG/VPN heroes; guest pain only; no ЕГРН/наследство/ипотека/Шакин
- Facts: Добрый дом хост посуточной Тюмень, не копипаст канала Клышина (юрист покупатель)

## Output request
Write `.cursor/excalibur-blog-handoff.md` with ALL required fields:
- wordstat_preflight, klyshin_hook, wordstat_rework, wordstat, angle_rotation
- topic_id: B03
- slug draft (latin)
- title_draft (Klyshin rhythm, guest pain, NO H1 list numbers like «5 шагов»)
- dzen_pattern: 5 or 2 (NOT 1)
- dzen_shape_hint
- season_note: summer 2026-08-25 YEKT, sept uni approaching
- queue_slot: 1 | parents_sept_uni
- signal_urls list
- anti_dup note

Title angle: parents drove son to university, 2-4 nights while paperwork — «рядом с вузом» in ad but 40 min walk to campus; NOT yearly rental essay.
