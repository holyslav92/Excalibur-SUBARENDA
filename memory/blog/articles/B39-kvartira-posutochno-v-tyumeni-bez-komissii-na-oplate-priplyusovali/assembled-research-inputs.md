# Assembled inputs for Derouter research synthesis — B39

research_date (today_iso): 2026-09-29
topic_id: B39
tenant: Добрый дом, Тюмень, посуточная аренда
primary_query: квартиры посуточно тюмень без комиссии скрытая доплата на оплате

## Scout handoff

See memory/scout/scout-inputs-2026-09-29.md

## Article case angle (illustrative guest scenario — not a claim about a real Dobry Dom booking)

Guest in Tyumen books two nights on an aggregator; filter shows «без комиссии» or «цена без наценки». On the payment screen before card charge, a line appears: service fee / cleaning / platform commission — about 1 187 ₽ on top of the nightly total already shown in the card. Guest is one tap from paying; chat with host has not started yet. Contrast: headline price vs checkout stack.

## Anti-dup

Do not retell B32 price stack (3400 vs 8816 full stack), B33 Avito double transfer, B34 zalog at door. This case is specifically **commission line on payment screen** after «без комиссии» filter.

## Wordstat MCP live — accessed 2026-09-29

- RU225 «комиссия посуточно» total 1807; «авито посуточно комиссия» 1014; «квартиры посуточно без комиссии» 307
- RU225 «квартиры посуточно без посредников» 42068
- Tyumen 55+11176 «квартиры посуточно тюмень» 4194; «авито квартиры посуточно тюмень» 301

## SERP / fresh (use research_start serp + live fetch)

Expand from research-serp.json in article dir. Need at least one source accessed 2026-09-29 about Avito/Sutochno service fees or guest complaints on checkout surprises (forums, Q&A, news). Distinguish: host-side Avito commission vs guest-facing service fee on booking apps.

## CURATOR LIVE FETCH 2026-09-29 (use these — do NOT refuse)

1. **Sutochno.ru help** https://sutochno.ru/sj/iz-chego-skladivaetsya-stoimost-bronirovaniya — accessed 2026-09-29  
   Guest pays prepayment 15–100%; cleaning/extra guests shown in calculation; «Суточно.ру не берёт с вас комиссию» — guest-facing line items should appear before pay, not surprise after filter «без комиссии» on third-party mirrors.

2. **TravelTribe digest 2026** https://traveltribe.ru/blog/sutochno-ru-2026/ — accessed 2026-09-29  
   Platform license fee 15–25% embedded in listing price, not always shown as separate line; compare total on same dates across apps.

3. **Wordstat** (MCP 2026-09-29): RU225 «комиссия посуточно» 1807; «авито посуточно комиссия» 1014; «квартиры посуточно без комиссии» 307; Tyumen «квартиры посуточно тюмень» 4194.

4. **Fresh community** https://t.me/s/Dobriy_dom_72 — posts week of 2026-09-29 about reading **итог на экране оплаты** vs фильтр «без наценки» (curator: channel discussed payment-screen stack vs card headline — use as tone signal only).

5. **research-serp.json** in article dir — Avito Tyumen posutochno, Sutochno Tyumen listings (accessed 2026-09-29).

## Output contract (HARD)

Output **only** valid `research-notes.md` body (markdown sections like B37 lift article: reader_problem, practical_facts, constraints, source_table).  
**Forbidden:** DEROUTER RESEARCH BLOCKER, shell instructions, meta-refusal.  
Also write `research-agent-report.json` with status PASS (you may output as second file section or director will add — if single output, research-notes only).  
Comfort+ Tyumen illustrative totals: 2 nights × 3 800 ₽ = 7 600 ₽ + service/cleaning line ~1 187 ₽ = 8 787 ₽ (composite case math).
