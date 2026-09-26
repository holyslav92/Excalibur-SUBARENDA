# Excalibur BLOG — content lessons (review-only)

## LESSON-20260926-1547-B03-cover-pad-no-ai-lockup
status: proposed
topic_id: B03
category: other
confidence: medium

### Evidence
- artifact: cover/cover_qa.json + INC-20260926-1537-cover-qa-logo-pad-gate
  finding: Cover-QA FAIL `forbid_ai_drawn_logo_pre_composite`, `forbid_logo_white_plate`; gen filled TOP-RIGHT with AI lockup (шторы+цветок/рамка) and white plate; opencv pad scrub before factory paste insufficient.
- metrika_signal: none (METRIKA CREDENTIALS BLOCKER this run)

### Named blockers
- COVER_LOGO_PAD_AI_LOCKUP

### Keep
- TOP-RIGHT 8–12% reserved for factory PNG paste only; phone post-composite, not in pad.
- Explicit prompt bans already list curtains+red flower / dashed frame / gold house — keep in every quad prompt.

### Change
- Treat pad as **empty scene texture** (high-key фон), not a “logo staging” — models invent tenant lockup when pad is named as brand zone.
- On pad/lockup FAIL: **regen quad** with stronger TL scene hint «TOP-RIGHT чистый pad БЕЗ логотипа/штор/цветка»; composite scrub is backup, not primary fix.

### Never again
- Rely on `clear_logo_pad` / `scrub_generation_logo_pad` alone when drawn lockup or white tablichka is visible pre-composite.
- Accept white/gray card under pad “for readability” — triggers `forbid_logo_white_plate`.

### Proposed apply
- review-only (cover skill + quad prompts); durable composite scrub already in fixer INC-20260926-1537.
