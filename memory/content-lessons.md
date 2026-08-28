# Content lessons (review-only)

## 2026-08-28 — B03 pack_vs_flat / полотенца

- **topic_id:** B03
- **evidence:** none (content-evidence SKIP)
- **metrika:** METRIKA CREDENTIALS BLOCKER — OAuth/counter not in env; no causal traffic read this run
- **keep:** Klyshin pack_vs_flat hook + Wordstat P0 «аренда квартиры посуточно» (47k RU) / «квартира посуточно тюмень» (5.5k); чеклист до оплаты + воронка TG после чеклиста, MAX в блоке «у нас так»
- **change (low confidence):** interlink anchors на sibling — формулировка с токенами из catalog title («залог», «скол»), иначе crosslink-qa FAIL при «депозит» vs «залог»
- **never_again:** hardcoded punycode/unicode site URLs в article.html для link-verify — только `/blog/{slug}/` + `{{SITE_BASE}}` для booking
- **proposed apply:** none (single run); repeat crosslink anchor mismatch → patch crosslink skill example
