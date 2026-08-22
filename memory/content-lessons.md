# Content lessons — Excalibur BLOG (Добрый дом)

Review-only proposals. Writer prompt protected — durable apply only after repeat evidence or human approval.

---

## LESSON-20260822-0711-B03-scout-handoff-assembly-derouter-refusal
status: proposed
topic_id: B03
category: other
confidence: medium

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json absent; gate SKIP
- artifact: memory/scout/scout-inputs.md
  finding: manually assembled Klyshin hook (contract_bans) + Wordstat rework log + final P0 «аренда квартиры посуточно» 48407/787
- artifact: .cursor/excalibur-blog-handoff.md
  finding: handoff written after assembly; topic_id B03, dzen_pattern 1, title_draft preserved
- artifact: memory/scout/derouter-opus-stamp-scout.json
  finding: Derouter scout utility call completed after assembly (request_id chatcmpl-bbb23dedf57d47378e8af79a)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER (YANDEX_METRIKA_OAUTH_TOKEN / COUNTER_ID unset)

### Named blockers
- DEROUTER_SCOUT_REFUSAL
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Klyshin×Wordstat dual gate: original hook + rework probes logged before P0
- Anti-dup ledger check (B01/B02) in scout-inputs
- Handoff fields: wordstat_preflight, klyshin_hook, wordstat_rework, dzen_pattern, season_note

### Change
- When Derouter scout refuses or returns DEROUTER SCOUT BLOCKER: assemble `memory/scout/scout-inputs.md` from Klyshin bank + live MCP-KV Wordstat (no invented frequencies), then retry Derouter with `--user-file` pointing at assembled inputs — never write handoff prose in Cursor
- Log refusal + assembly path in scout-inputs header (timestamp, probe table, final P0)

### Never again
- Drop scout on first Derouter refusal without Wordstat-backed assembly
- Invent Wordstat volumes when MCP-KV unavailable (WORDSTAT MCP BLOCKER instead)
- Cursor-authored handoff replacing Derouter scout output

### Proposed apply
- Document assembly fallback in scout skill checklist: refusal → assemble scout-inputs → retry Derouter → handoff
- Optional stamp `scout-assembly-fallback.json` when Derouter skipped

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260822-0712-B03-cover-qa-ai-drawn-logo-pre-composite
status: proposed
topic_id: B03
category: other
confidence: high

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json absent
- artifact: cover/cover_qa.json
  finding: regen v2 PASS; `forbid_ai_drawn_logo_pre_composite: true`; notes cite pre-composite pads cleaned before factory paste
- artifact: cover/logo-composite-stamp.json
  finding: `forbid_ai_drawn_logo: true`, `pre_composite_dir: cover/pre-composite`, official logo pasted top-right on cover + inline-01/03/07
- artifact: cover/cover-agent-report.md
  finding: Regen v2 + pre-composite pad clean before factory paste; cover_qa PASS
- artifact: cover/quad-mcp-batch-01.json (prompt FORBID block)
  finding: explicit ban on AI lockup (curtains+flower, dashed frame, «Добрый дом» text, white plate in logo pad)
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- AI_DRAWN_LOGO_PRE_COMPOSITE (initial gen)
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- brand_logo_paste mode: factory PNG only, never model-drawn lockup
- drawn_logo_gate on pre-composite snapshots before composite stamp
- Logo slots: cover + inline_1, inline_3, inline_7 (not all 7)

### Change
- On drawn_logo_gate FAIL: regen canvases with strengthened FORBID logo block in quad prompts; snapshot clean pre-composite; run `excalibur_blog_brand_logo_composite.py` only after pre-composite passes drawn_logo_gate
- Cover-QA must include `forbid_ai_drawn_logo_pre_composite` (added B03; B01/B02 lacked explicit check)

### Never again
- Paste official logo over AI-drawn lockup without regen/clean pre-composite pad
- Skip pre-composite snapshot before factory paste
- Allow green-curtains+red-flower or dashed-frame lockup in generation pad

### Proposed apply
- Default Cover regen playbook: drawn_logo_gate FAIL → regen + pad clean → composite → cover_qa
- Align B01/B02 cover_qa stamp with forbid_ai_drawn_logo_pre_composite on next touch

### Durable applied
- none

### Resolution
status: recorded

---

## LESSON-20260822-0713-B03-kie-fallback-derouter-image-exhausted
status: proposed
topic_id: B03
category: other
confidence: high

### Evidence
- artifact: none (skipped under human-first-v2)
  finding: content-evidence-report.json absent
- artifact: cover/quad-mcp-result-01.json, cover/quad-mcp-result-02.json
  finding: `"source": "kie-api"`, state success — both quad canvases via Kie fallback
- artifact: cover/cover-agent-report.md
  finding: `image_provider: kie-fallback (Derouter exhausted)`
- artifact: scripts/excalibur_blog_derouter_gpt_image2_api.py#run_kie_fallback
  finding: `--fallback-kie` runs `excalibur_blog_kie_gpt_image2_api.py` after Derouter retries exhausted
- artifact: cover/cover_qa.json
  finding: Kie fallback canvases passed full Cover-QA including logo/phone/utility gates
- metrika_signal: none — METRIKA CREDENTIALS BLOCKER

### Named blockers
- DEROUTER_IMAGE_EXHAUSTED
- EVIDENCE_SKIPPED
- METRIKA_CREDENTIALS_MISSING

### Keep
- Primary path: Derouter REST 2K quad (`preferred_image_flow.provider: derouter-rest`)
- Kie as documented fallback only after Derouter auth/5xx/retry exhaustion
- Same quad batch prompts and split pipeline regardless of image provider

### Change
- Always pass `--fallback-kie` to `excalibur_blog_derouter_gpt_image2_api.py` for cover quad generation in production
- Stamp `source` in quad-mcp-result-*.json (kie-api vs derouter-rest) for audit
- After Kie fallback, still run drawn_logo_gate + logo composite + cover_qa — provider change does not skip QA

### Never again
- BLOCK publish solely because Derouter image exhausted when Kie fallback available and credentialed
- Silent provider switch without result JSON source stamp
- Skip Cover-QA because fallback canvases «look fine»

### Proposed apply
- Cover skill/agent: mandate `--fallback-kie` on both quad batch invocations
- Monitor Derouter image error rate; if ≥2 articles hit Kie fallback in 7d → fixer incident for Derouter quota/routing

### Durable applied
- none

### Resolution
status: recorded
