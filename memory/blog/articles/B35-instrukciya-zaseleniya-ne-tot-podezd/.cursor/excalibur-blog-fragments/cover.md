---
agent: excalibur-blog-cover
status: PASS
topic_id: B35
---

## Artifacts

- `cover/cover.png`
- `cover/inline-01.png` … `cover/inline-07.png`
- `cover/canvas-quad-01.png`, `cover/canvas-quad-02.png`
- `cover/logo-composite-stamp.json` (cover + inline 1/3/7 factory paste)
- `cover/quad-manifest.json`, `cover/quad-mcp-batch-01.json`, `cover/quad-mcp-batch-02.json`

## Gates

- `cover-text-gate.json`: PASS
- `excalibur_blog_drawn_logo_gate.py`: PASS (slim)
- `cover_qa.json`: pending Cover-QA agent

## Generation

- Grsai `--model-tier auto` (primary → VIP 2K) × 2 canvases; recovery regen after pad-clear on drawn lockup
- Autumn / late September 2026 Tyumen, wet courtyard motif
