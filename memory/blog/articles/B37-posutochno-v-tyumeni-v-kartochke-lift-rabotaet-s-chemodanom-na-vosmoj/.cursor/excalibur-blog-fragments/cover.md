---
status: PASS
topic_id: B37
pipeline: slice4_grid_1x_image_api (gen_only_slice4, 1 canvas 2048×1152 → 4 panels)
grsai: primary only (vip tier unavailable at gen time; GRSAI_FORBID_VIP=1 ship native + PIL upscale to 2048×1152)
attempts: 2 primary on one canvas (max per canon)
---

## Artifacts

- `cover/canvas-slice4.png` — source grid (native 1672×941 → upscaled 2048×1152)
- `cover/cover.png` — cover tile + factory `logo-dobry-dom.png` paste top-right
- `cover/inline-01.png` … `inline-03.png`
- `cover/slice4-mcp-batch.json` / `slice4-mcp-result.json`
- `cover/logo-composite-stamp.json` — PASS
- `cover/quad-manifest.json` — motifs, wordstat, `cover_phone_cta` +7 (993) 574-83-22

## Gates

- cover-text-gate: PASS
- motif_gate check: PASS (recorded)
- slice4_gate: PASS
- brand_logo_composite: PASS (cover only; inline logo count 0 per gen_only_human)
- cover_qa_gate: **pending** — run `excalibur-blog-cover-qa` → `cover/cover_qa.json`

## Notes

- Canon **one** slice4 canvas (not 2×8 longform); logo paste **cover tile only** (not inline 1/3/7).
- Grsai vip tier unavailable at generation time; primary delivered undersized 2K-class miss — upscaled before split.
- Cover panel: headline on physical tent card; hook «22 минуты»; official logo post-composite. Phone not painted in cover (gen_only slice4 prompt forbids phone on cover image).
- Next: Cover-QA visual pass, then Indexer/Publish.
