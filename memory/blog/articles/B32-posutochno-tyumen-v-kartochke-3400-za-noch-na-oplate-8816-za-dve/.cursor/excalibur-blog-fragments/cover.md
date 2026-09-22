---
status: PASS
topic_id: B32
pipeline: slice4_grid_1x_image_api (gen_only_slice4, 1 canvas 2048×1152 → 4 panels)
grsai: vip tier (primary undersized 1672×941, 1 vip attempt)
attempts: 1 generation (+ vip fallback)
---

## Artifacts

- `cover/canvas-slice4.png` — source 2K grid
- `cover/cover.png` — cover tile + factory logo paste
- `cover/inline-01.png`
- `cover/inline-02.png`
- `cover/inline-03.png`
- `cover/slice4-mcp-batch.json` / `slice4-mcp-result.json`
- `cover/logo-composite-stamp.json` — PASS
- `cover/cover_qa.json` — PASS
- `cover/quad-manifest.json` — motifs + wordstat

## Gates

- cover-text-gate: PASS
- slice4_gate: PASS
- cover_qa_gate: PASS
- motif_gate: recorded

## Notes

- Tenant `inline_image_count: 3` → one slice4 canvas (not 2×8 longform).
- Logo factory paste **cover only** (gen_only_human; inline 1/3/7 logo not applied).
- Phone: manifest `+7 (993) 574-83-22`; gen_only slice4 prompt forbids phone on cover image — QA `forbid_phone_on_cover_image: true`.
