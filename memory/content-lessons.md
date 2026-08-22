# Excalibur BLOG — content lessons (review-only)

Proposals for human review. Content Learner does **not** auto-edit Writer/Sol prompts.

---

## LESSON-20260822-1017-B03-derouter-scout-research-blockers
status: proposed
topic_id: B03
category: other
confidence: high

### Evidence
- artifact: memory/blog/articles/B03-otmena-bronirovaniya-posutochno-vozvrat-predoplaty/research-agent-report.json#derouter_status
  finding: `derouter_status: BLOCKER` — utility returned BLOCKER stub; research-notes.md written manually from verified serp + harant + wordstat per fallback instruction.
- artifact: memory/scout/derouter-opus-stamp-scout.json + automation memory 2026-08-21
  finding: prior run hit `DEROUTER SCOUT` HTTP 402 `budget_exceeded`; B03 scout completed after budget top-up (stamp present, Wordstat MCP dual gate logged in scout-inputs-assembled.md).
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json absent — evidence_gate SKIP.
- metrika_signal: none — `METRIKA CREDENTIALS BLOCKER` (YANDEX_METRIKA_OAUTH_TOKEN / YANDEX_METRIKA_COUNTER_ID unset).

### Named blockers
- DEROUTER_SCOUT_BLOCKER (402 budget_exceeded on prior attempt)
- DEROUTER_RESEARCH_BLOCKER (utility BLOCKER stub; manual synthesis)
- METRIKA_CREDENTIALS_BLOCKER
- EVIDENCE_SKIPPED

### Keep
- Scout dual gate Klyshin hook × MCP-KV Wordstat with rework log (P0 «отмена бронирования» RU 14147 / Tyumen 104).
- Research manual fallback: live harant q-201970 + q-193619, freshness_audit PASS, wordstat_audit PASS.
- Explicit `derouter_status` + `derouter_note` in research-agent-report.json (audit trail).

### Change
- Preflight Derouter budget (`DEROUTER_API_KEY`) before Scout/Research; surface 402 in Director handoff.
- After Research BLOCKER stub: one automatic retry of `excalibur_blog_derouter_opus_chat.py --role research` before manual fallback.
- Configure Cloud Secrets: `YANDEX_METRIKA_OAUTH_TOKEN`, `YANDEX_METRIKA_COUNTER_ID`.

### Never again
- Silent Composer prose for Scout/Research when Derouter utility fails.
- Drop research freshness/wordstat audits because Derouter synthesis stubbed.

### Proposed apply
- Director preflight checklist: Derouter budget + Metrika secrets before pipeline start.
- Document Research BLOCKER retry in `shared/derouter-opus-brain-contract.md` (human review).

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260822-1017-B03-cover-ai-logo-cleanup
status: proposed
topic_id: B03
category: other
confidence: medium

### Evidence
- artifact: memory/blog/articles/B03-otmena-bronirovaniya-posutochno-vozvrat-predoplaty/cover/cover_qa.json#notes
  finding: pre-composite pads cleaned + factory PNG re-paste PASS; inline logos on 01/03/07 only (3); TOP-RIGHT fixed.
- artifact: memory/blog/articles/B03-otmena-bronirovaniya-posutochno-vozvrat-predoplaty/cover/logo-composite-stamp.json
  finding: `forbid_ai_drawn_logo: true`, `pre_composite_dir: cover/pre-composite`, official `logo-dobry-dom.png` sha256 stamped.
- metrika_signal: none (credentials blocker).

### Named blockers
- COVER_AI_LOGO_PAD (generation drew lockup in TOP-RIGHT pad — recovered by pad cleanup before composite)

### Keep
- Cover-QA gate `forbid_ai_drawn_logo_pre_composite` + `official_logo_pixels_only`.
- Workflow: save pre-composite → inspect/clean AI lockup (curtains/heart/wordmark/white plate) → `excalibur_blog_brand_logo_composite.py` paste canonical PNG.
- Cover-scene prompts: «NO brand logo in generation — factory pastes PNG after split» + «TOP-RIGHT empty pad ONLY».

### Change
- Cover agent: always run logo composite from `cover/pre-composite/`; never paste over uncleaned AI lockup.
- If QA sees dashed frame / curtains icon / «Добрый дом» wordmark in pad → FAIL pre-composite, clean pad, re-paste (do not regenerate full quad unless pad uncleanable).

### Never again
- Accept AI-drawn logo lockup as «close enough» under factory PNG overlay.
- Skip `logo-composite-stamp.json` before Cover-QA PASS.

### Proposed apply
- Add one-line reminder to `.cursor/skills/cover-excalibur-blog/SKILL.md`: mandatory pre-composite pad inspect before composite (human review — no auto skill edit this run).

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260822-1017-B03-live-page-theme-gate
status: proposed
topic_id: B03
category: other
confidence: high

### Evidence
- artifact: memory/blog/articles/B03-otmena-bronirovaniya-posutochno-vozvrat-predoplaty/live-page-report.json
  finding: BLOCK — FAQPage jsonld=0 vs visible=1; BlogPosting URL ≠ permalink; `#article-content` missing; `.post-thumbnail` missing; FAQ JSON-LD ≠ visible FAQ.
- artifact: memory/blog/articles/B02-*/live-page-report.json + B01-*/live-page-report.json
  finding: **same error set on B01 and B02** — systemic theme/gate mismatch, not B03-only.
- artifact: memory/blog/articles/B03-otmena-bronirovaniya-posutochno-vozvrat-predoplaty/article.meta.json#theme_blocks
  finding: faq/quiz/side_stickers = skip; publish set `_excalibur_blog_skip_theme_faq` meta (wp-publish-result OK).
- artifact: memory/blog/wp-publish-log.md
  finding: article + media HTTP 200; live-page BLOCK classified as theme contract / JSON-LD parity (same class as B02).
- metrika_signal: none (credentials blocker).

### Named blockers
- LIVE_PAGE_THEME_GATE
- ASSUMED_BEHAVIOR (gate expects `#article-content` + `.post-thumbnail` + inline FAQPage JSON-LD on live HTML; theme may render differently)

### Keep
- `theme_blocks.*=skip` in article.meta.json before publish.
- Thematic FAQ only in article body (one H2 «Частые вопросы»).
- Publish still uploads content/media; post is live at published permalink.

### Change
- Fixer: align WP theme single-post template with `shared/live-page-contract.md` — add `#article-content` wrapper, `.post-thumbnail`, inject FAQPage/BlogPosting JSON-LD from `_excalibur_blog_schema` meta OR relax gate selectors to match actual theme markup (after inspecting live HTML).
- Do not treat identical B01/B02/B03 BLOCK pattern as per-article content defect.

### Never again
- Mark pipeline DONE / skip fixer solely because FTP upload succeeded while live-page gate BLOCK repeats unchanged.
- Add second theme FAQ when `theme_blocks.faq=skip`.

### Proposed apply
- `memory/pipeline-fix-queue.md` incident INC-20260822-1017-fixer-live-page-theme-gate (open).
- Target: `scripts/excalibur_blog_live_page_gate.py` and/or theme deploy `scripts/excalibur_blog_theme_contract_deploy.py` after live HTML inspection.

### Durable applied
- none — pending fixer (≥3 runs evidence: B01, B02, B03)

### Resolution
status: recorded
