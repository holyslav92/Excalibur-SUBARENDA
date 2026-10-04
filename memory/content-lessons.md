# Excalibur BLOG — content lessons (review-only)

Proposals for humans; Writer prompt protected. See `shared/content-learning-contract.md`.

## LESSON-20260925-1506-B03-cover-qa-json-gate-split
status: active
topic_id: B03
category: other
confidence: high

### Evidence
- artifact: `memory/blog/articles/B03-posutochno-tyumen-v-filtre-mozhno-s-sobakoj-u-dveri-otkaz/cover/cover_qa.json`
  finding: stamped `status: PASS` with all `checks: true` (incl. `forbid_ai_drawn_logo_pre_composite`, `official_logo_pixels_only`, `forbid_logo_white_plate`) while `excalibur_blog_cover_qa_gate.py` FAIL on same tree (drawn lockup, gray/white logo plates, unofficial post-composite logo pixels on cover + inline-04–07).
- artifact: `memory/pipeline-fix-queue.md#INC-20260925-1500-cover-qa-gate-json-script-split`
  finding: publish preflight previously required only `cover/cover.png` existence; B03 (pet-filter / «с собакой» case) shipped with JSON↔script split.
- artifact: none (skipped under human-first-v2)
  finding: `content-evidence-report.json` absent; evidence_gate SKIP — no editorial evidence table for this run.
- metrika_signal: none — `METRIKA CREDENTIALS BLOCKER` (no `memory/analytics/metrika-latest.json` ingest); behavioral cohort not available for B03 day-0.

### Named blockers
- ASSUMED_BEHAVIOR — Cover-QA handoff treated agent-stamped JSON as publish truth without script exit 0.
- EVIDENCE_SKIPPED — no content-evidence-report for causal content-quality claims.
- METRIKA_CREDENTIALS — cannot correlate cover defect with on-site behavior this run.

### Keep
- CASE angle for B03 (filter «можно с собакой» vs отказ у двери / доплата) — title, description-brief, and article shipped; live URL published.
- Cover-QA checklist fields in `cover_qa.json` remain useful as human-readable audit list when aligned with script.

### Change
- Treat `cover/cover_qa.json` `status: PASS` as handoff hint only; publish and Cover-QA close only after `python3 scripts/excalibur_blog_cover_qa_gate.py` exit 0 on the article dir (enforced post–B03 in publish preflight).
- For pet-filter and similar high-visual CASE topics, regen all inline panels that still fail `forbid_*_logo_*` before stamp — partial canvas regen (B03 notes: canvas-2 inline 04–07 untouched) preserves gate FAIL under honest script.

### Never again
- Publish when `cover_qa.json` says PASS but cover QA gate script FAIL.
- Stamp `official_logo_pixels_only: true` without script verifying factory PNG paste on cover and each inline.

### Proposed apply
- Pipeline/tooling only (no Writer prompt): already landed via fixer — see Durable applied.
- Optional human follow-up: regenerate B03 cover/inline assets until gate PASS (live post already up; cosmetic/brand risk on featured image).

### Durable applied
- `scripts/excalibur_blog_wp_publish.py` — publish preflight invokes `excalibur_blog_cover_qa_gate.py`; rollback: revert prereq block + `tests/test_publish_cover_qa_prereq.py`.
- `agents/excalibur-blog-cover-qa.md`, `skills/cover-qa-excalibur-blog/SKILL.md` — HARD rule JSON insufficient without script OK; rollback: restore prior agent/skill text.
- `shared/excalibur-wp-publish-contract.md` — documents script gate; rollback: doc revert.
- Applied by fixer commit `e92fc99c` / INC-20260925-1500-cover-qa-gate-json-script-split (content-learner did not duplicate apply).

### Resolution
status: recorded

## LESSON-20260929-0650-B37-slice4-grsai-vip-wordstat-postcomposite
status: proposed
topic_id: B37
category: other
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: `content-evidence-report.json` absent; evidence_gate SKIP — editorial evidence table not used.
- artifact: `memory/blog/articles/B37-posutochno-v-tyumeni-v-kartochke-lift-rabotaet-s-chemodanom-na-vosmoj/cover/slice4-mcp-result.json`
  finding: Grsai primary attempt 2; `vip_trigger: vip_tier_unavailable`; `delivery: native_undersized_no_vip`; native 1672×941 vs target 2048×1152 — slot shipped after PIL upscale + mechanical quarter slice (canon `on_exhaust`).
- artifact: `memory/blog/articles/B37-posutochno-v-tyumeni-v-kartochke-lift-rabotaet-s-chemodanom-na-vosmoj/cover/cover_qa.json` + `cover/logo-composite-stamp.json`
  finding: Wordstat phrases («квартиры посуточно тюмень», «снять квартиру посуточно в тюменi») **post-composited on cover.png after** factory logo paste; Cover-QA re-run PASS with `wordstat_stickers_1_3: true`; regen_log documents gen forbids in-scene stickers.
- artifact: `memory/blog/articles/B37-posutochno-v-tyumeni-v-kartochke-lift-rabotaet-s-chemodanom-na-vosmoj/cover/quad-split-report.json` + `slice4-gate.json`
  finding: **One** slice4 canvas → cover + 3 inlines (4 PNG total); not legacy 2×8-frame / 7-inline longform; `python3 scripts/excalibur_blog_cover_qa_gate.py` exit 0 on publish tree.
- artifact: `memory/blog/articles/B37-posutochno-v-tyumeni-v-kartochke-lift-rabotaet-s-chemodanom-na-vosmoj/wp-publish-result.json`
  finding: publish PASS 2026-09-29 (post 5125, featured + 3 inline uploads).
- metrika_signal: none — `METRIKA FEEDBACK BLOCKER` (`YANDEX_METRIKA_OAUTH_TOKEN` / `YANDEX_METRIKA_COUNTER_ID` unset); see `memory/pipeline-fix-queue.md#INC-20260925-1506-content-learner-metrika-credentials`.

### Named blockers
- METRIKA_CREDENTIALS — behavioral cohort unavailable; no causal CTR/retention claims for B37 day-0.
- GRSAI_VIP_UNAVAILABLE — VIP tier down at gen time; primary-only undersized delivery accepted under canon exhaust.
- EVIDENCE_SKIPPED — no content-evidence-report for editorial-quality claims beyond cover pipeline artifacts.
- CANON_DOC_DRIFT — `memory/cover/cover-canon.json` still lists `wordstat_stickers.cover: FORBIDDEN` while B37 factory workflow post-composites 1–3 stickers after logo (human canon sync needed).

### Keep
- CASE lift + чемодан + «22 минуты» angle shipped with slice4 grid (подъезд/лифт narrative in inline panels despite cover panel = гостиная scene).
- Order of factory steps when stickers needed: Grsai slice4 draw → quad split → **logo paste cover tile only** → **Wordstat sticker post-composite** → Cover-QA + gate script before Indexer/Publish.
- Single Grsai draw + mechanical quarter crop (`dobry_dom_gen_only_human_v1`); logo never on inline tiles.

### Change
- Treat Grsai `vip_tier_unavailable` as expected env state (batch note: VIP permanently disabled): log `native_undersized_no_vip` in `slice4-mcp-result.json` / cover_qa `regen_log`; upscale before split; do not block publish if slice4_gate + cover QA script PASS.
- Cover-QA must visually confirm **post-composite** Wordstat stickers (readable, 1–3, no overlap with logo pad) — not demand stickers inside Grsai generation prompt (gen_only forbids factory typography/sticker collage in-scene).
- Cover agent handoff: explicitly flag **slice4 (4 PNG)**, not 8-frame set, in fragment `cover.md` (B37 did this).

### Never again
- Request Wordstat sticker text inside the Grsai slice4 prompt as painted scene typography (use manifest + factory post-composite after logo).
- Assume VIP retry will upsize to true 2048 long side when API returns `vip_tier_unavailable` — ship slot per canon after max primary attempts.
- Run Cover-QA stamp before Wordstat post-composite when manifest requires stickers (re-QA after sticker paste, as B37).

### Proposed apply
- Human: align `memory/cover/cover-canon.json` `wordstat_stickers` block with gen_only factory post-composite allowance (cover tile only, after logo paste).
- Human: refresh Cover-QA / Cover skills prose from «8 PNG / 7 inline» to slice4 4-panel canon (do not auto-edit skills from this single lesson per Writer/skill protection — queue for owner).
- Env: resolve Metrika credentials (existing INC) and re-run learner ingest for B37 cohort when vars land.

### Durable applied
- none — first named slice4+VIP+wordstat-postcomposite lesson; Grsai undersized pattern also seen on B05/B08 but different cover pipelines; no automated skill/canon edit this run.

### Resolution
status: recorded

## LESSON-20261002-1358-B42-dvushka-vtoraya-kladovaya-day0
status: proposed
topic_id: B42
category: structure
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: `content-evidence-report.json` absent; `excalibur_blog_content_evidence_gate.py` → SKIP.
- artifact: `memory/blog/articles/B42-posutochno-tyumen-dvuhkomnatnaya-vtoraya-kladovaya/case-delivery-gate.json`
  finding: `status: PASS` — H1 dialogue + «в фильтре двухкомнатная / за второй дверью кладовая» CASE shipped; `exclude_slug` from `article.meta.json` excluded self from anti-clone vs 12 live (no false skeleton match on merge tree).
- artifact: `memory/blog/articles/B42-posutochno-tyumen-dvuhkomnatnaya-vtoraya-kladovaya/wp-publish-result.json`
  finding: publish PASS 2026-10-02 (WP post 5179, 7 inline, featured, categories).
- metrika_signal: none — `METRIKA FEEDBACK BLOCKER` (`YANDEX_METRIKA_OAUTH_TOKEN` / `YANDEX_METRIKA_COUNTER_ID` unset); see `memory/pipeline-fix-queue.md#INC-20260925-1506-content-learner-metrika-credentials`.

### Named blockers
- EVIDENCE_SKIPPED — no editorial evidence table; no causal quality claims.
- METRIKA_CREDENTIALS — behavioral cohort unavailable for B42 day-0.
- LOW_SAMPLE — fresh publish; no on-site cohort to match.

### Keep
- «Вторая не сдаётся» / кладовая за второй дверью wound distinct from door-surcharge-only skeletons; filter-two-room + 10 800 ₽ price anchor in H1/meta_ab.
- Case-delivery anti-clone with `exclude_slug` on in-flight article dir before live ledger refresh — B42 gate clean without fixer.

### Change
- none durable — re-run Metrika ingest after credentials land to attach cohort for `posutochno-tyumen-dvuhkomnatnaya-vtoraya-kladovaya`.

### Never again
- Treat missing Metrika env as silent skip in content-learner (must log BLOCKER + existing INC).

### Proposed apply
- Env: resolve Metrika secrets; re-ingest and optional lesson confidence bump when matched_rows > 0.
- Human: none for anti-clone — `exclude_slug` already wired in `excalibur_blog_case_delivery_gate.py`.

### Durable applied
- none — day-0 SKIP+Metrika-only; no repeat pattern for automated apply.

### Resolution
status: recorded

## LESSON-20261003-1254-B43-crib-filter-weak-wordstat-sol-shrink
status: proposed
topic_id: B43
category: structure
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: `content-evidence-report.json` absent; `excalibur_blog_content_evidence_gate.py` → SKIP.
- artifact: `memory/scout/scout-assembled-input-2026-10-03.md`
  finding: Klyshin `hook_id: crib_filter_promise` — filter amenity vs pay/tomorrow; Wordstat «квартира посуточно с детской кроваткой» **37** (225); rework logged: weak crib → keep guest crib angle, spine P0 «квартиры посуточно тюмень» 3963 (55+11176) | 8919 (225).
- artifact: `memory/blog/articles/B43-posutochno-tyumen-v-filtre-detskaya-krovatka-v-chate-zavtra-za-2500/case-delivery-gate.json`
  finding: `status: PASS` — H1 «детская кроватка» + chat «завтра за 2 500 ₽» CASE shipped (`dobry_dom_voice_reset_v1`).
- artifact: `memory/blog/articles/B43-posutochno-tyumen-v-filtre-detskaya-krovatka-v-chate-zavtra-za-2500/wp-publish-result.json`
  finding: publish PASS 2026-10-03 (WP post 5211, featured + 3 inline, categories 101/104/106).
- artifact: word-count probe (article tree, same tokenizer as gate plain text)
  finding: `drafts/writer.html` **1137** words → `article.html` **941** words after Sol (~17% shrink); canon target band 650–1100 — gate min 650 satisfied, but landed ~160 words below Writer meaning budget and below informal 1100 upper intent for CASE mode B.
- metrika_signal: none — `METRIKA FEEDBACK BLOCKER` (`YANDEX_METRIKA_OAUTH_TOKEN` / `YANDEX_METRIKA_COUNTER_ID` unset); see `memory/pipeline-fix-queue.md#INC-20260925-1506-content-learner-metrika-credentials`.

### Named blockers
- EVIDENCE_SKIPPED — no editorial evidence table; no causal quality claims from evidence report.
- METRIKA_CREDENTIALS — behavioral cohort unavailable for B43 day-0.
- LOW_SAMPLE — fresh publish; no on-site Metrika match possible this run.
- WEAK_WORDSTAT_NICHE — amenity-specific query 37 (225); demand carried by spine P0 only (expected Scout rework, not skip).

### Keep
- `crib_filter_promise` wound (filter tick vs paid/tomorrow delivery) distinct from B24 child surcharge / B36 dog / B42 closet-room skeletons.
- Scout dual-gate pattern: do not drop hook on crib volume 37; localize via «квартиры посуточно тюмень» P0 + in-text amenity conflict (mirrors B24 «с детьми» rework).
- Outbound interlink to family/sleep siblings (`mozhno-s-detmi-doplata-za-rebenka`, `dve-krovati-na-foto-…`) — `interlink-gate.json` PASS.

### Change
- Sol handoff (human/Sol skill review, not Writer prompt): when Writer draft >~1050 words, Sol should preserve checklist/utility blocks (what to ask in chat before pay, 2 500 ₽ line items) rather than compress to ~940 — target upper half of 650–1100 for filter-amenity CASEs with weak SEO tail.
- After Metrika credentials: re-ingest and attach cohort for slug `posutochno-tyumen-v-filtre-detskaya-krovatka-v-chate-zavtra-za-2500`; do not infer crib-niche SEO failure from day-0.

### Never again
- Skip `crib_filter_promise` solely because «детская кроватка» Wordstat <50 without rework log + spine P0 (B43 shipped correctly).
- Treat missing Metrika env as silent skip in content-learner.
- Auto-edit `shared/writer-master-prompt.md` or Sol skill from one Sol-shrink observation.

### Proposed apply
- Env: resolve Metrika secrets (existing INC); optional confidence bump if matched_rows > 0 and retention OK vs family-amenity siblings.
- Human: Sol agent/skill note — «preserve Writer utility when Terra Sol shortens >15%»; repeat on second article before any script gate change.
- Scout: no change — weak amenity + strong spine already canon.

### Durable applied
- none — first named `crib_filter_promise` + Sol-shrink lesson; B24 weak child cluster is parallel but different hook; no automated apply.

### Resolution
status: recorded

## LESSON-20261004-0756-B44-deposit-hold-chat-checkout-day0
status: proposed
topic_id: B44
category: structure
confidence: low

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: `content-evidence-report.json` absent; `excalibur_blog_content_evidence_gate.py` → SKIP.
- artifact: `memory/scout/excalibur-blog-handoff.md`
  finding: Klyshin `hook_id: deposit_before_keys` — chat small deposit vs large card hold before code; Wordstat rework: sparse «залог на карте посуточно» → spine P0 «квартира посуточно залог» **17** (Tyumen 55) | RU «не вернули залог за квартиру посуточно» 31 | «посуточно комиссия» 1769 (225) as checkout-sum context; angle_rotation excludes B34 door-zalog / B02 return / live «залог к обеду».
- artifact: `memory/blog/articles/B44-zalog-na-oplate-zamorozili-bolshe-chem-v-chate/case-delivery-gate.json`
  finding: `status: PASS` — H1 chat 3 000 ₽ vs bank hold 11 400 before code (`dobry_dom_voice_reset_v1`).
- artifact: `memory/blog/articles/B44-zalog-na-oplate-zamorozili-bolshe-chem-v-chate/wp-publish-result.json`
  finding: publish PASS 2026-10-04 (WP post 5218, featured + 3 inline, categories 101/102).
- artifact: `memory/blog/articles/B44-zalog-na-oplate-zamorozili-bolshe-chem-v-chate/interlink-gate.json`
  finding: outbound 4 siblings (prepay silence, washer+zalog, price stack 3400→8816, filter no-prepay) — PASS.
- artifact: `memory/blog/articles/B44-zalog-na-oplate-zamorozili-bolshe-chem-v-chate/cover/slice4-mcp-result.json`
  finding: Grsai `delivery: native_undersized_no_vip` 1672×940 → upscale/split shipped; Cover-QA + slice4 gate PASS (parallel to LESSON-20260929-0650-B37).
- artifact: word-count probe (plain text, same tokenizer as prior lessons)
  finding: `drafts/writer.html` **1080** words → `article.html` **982** words after Sol (~9% shrink); within 650–1100 band; less compression than B43 crib CASE.
- metrika_signal: none — `METRIKA FEEDBACK BLOCKER` (`YANDEX_METRIKA_OAUTH_TOKEN` / `YANDEX_METRIKA_COUNTER_ID` unset); see `memory/pipeline-fix-queue.md#INC-20260925-1506-content-learner-metrika-credentials`.

### Named blockers
- EVIDENCE_SKIPPED — no editorial evidence table; no causal quality claims from evidence report.
- METRIKA_CREDENTIALS — behavioral cohort unavailable for B44 day-0.
- LOW_SAMPLE — fresh publish; no on-site Metrika match possible this run.
- WEAK_WORDSTAT_NICHE — Tyumen P0 «квартира посуточно залог» 17; demand carried by rework + checkout/commission context (expected Scout pattern, not skip).

### Keep
- `deposit_before_keys` wound (promised chat deposit vs payment-screen hold before keys) distinct from B34 «без залога у двери», B40 prepay-before-code, B02 return/scratch, live return-timing posts.
- Scout dual-gate: do not drop hook on Tyumen 17; log rework + supporting RU clusters + spine; ship dzen_shape «3 000 в чате — 11 400 на оплате, код нет».
- Outbound interlink cluster to prepay/price-stack/zalog siblings — strengthens buyer checkout literacy without cloning saturated return-zalog H1s.

### Change
- After Metrika credentials land: re-ingest (`--days 30 --ingest`) and attach cohort for slug `posutochno-tyumen-v-chate-zalog-3000-bank-zamorozil-11400`; do not infer niche SEO failure from day-0.
- Human (optional): if second `deposit_before_keys` article shows Sol shrink >15%, review Sol skill for preserving «what to screenshot before pay / hold vs charge» utility blocks — B44 ~9% only; no Writer prompt edit.

### Never again
- Skip `deposit_before_keys` solely because Tyumen zalog P0 <50 without rework log + angle_rotation (B44 shipped correctly).
- Treat missing Metrika env as silent skip in content-learner.
- Auto-edit `shared/writer-master-prompt.md` from one weak-Wordstat deposit lesson.

### Proposed apply
- Env: resolve Metrika secrets (existing INC); optional confidence bump when `matched_rows` > 0.
- Scout: no change — weak local P0 + commission context already canon.
- Cover: no new durable apply — Grsai undersized pattern covered by B37 lesson.

### Durable applied
- none — day-0 SKIP + Metrika BLOCKER; deposit-hold angle first named lesson; no repeat pattern for automated apply.

### Resolution
status: recorded
