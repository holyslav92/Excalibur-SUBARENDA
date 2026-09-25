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
