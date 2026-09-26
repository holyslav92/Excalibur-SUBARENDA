---
status: FAIL
topic_id: B03
---

## Artifacts

- cover/cover.png
- cover/inline-01.png … cover/inline-07.png
- cover/canvas-quad-01.png, cover/canvas-quad-02.png
- cover/logo-composite-stamp.json (PASS)
- cover/cover_qa.json (FAIL)

## BLOCKERs

1. **KIE API BLOCKER** — `api.kie.ai` createTask HTTP 402 (credits insufficient). Tenant `IMAGE_PROVIDER=grsai`: generation via GRSAI OpenAI-compatible `/v1/images/generations` using `excalibur_blog_derouter_gpt_image2_api.py` + `GRSAI_API_KEY` (not `excalibur_blog_kie_gpt_image2_api.py`).
2. **COVER QA GATE FAIL** — `forbid_ai_drawn_logo_pre_composite`, `forbid_logo_white_plate`; drawn lockup on pre-composite cover/inline-01; white pad under factory logo on inline-01/03/07; drawn logo on inline-02/04/05/06.

## Notes

- Canvas 1: 2 generation attempts (logo lockup). Canvas 2: 1 attempt.
- Factory logo TOP-RIGHT: cover + inline-01, inline-03, inline-07.
- Derouter cover-scene + batches OK.
