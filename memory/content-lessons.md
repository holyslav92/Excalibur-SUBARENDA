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
