---
status: PASS
topic_id: B08
mode: gen_only_slice4
attempts: 1
provider: grsai-vip (GRSAI_VIP_ECONOMY=1)
---

## Artifacts

| File | Role |
|------|------|
| `cover/canvas-slice4.png` | Source 2048×1152 2×2 grid (1 Grsai draw) |
| `cover/cover.png` | Cover tile + factory logo paste |
| `cover/inline-01.png` | Inline 1 — «Галочка не считает гостей» |
| `cover/inline-02.png` | Inline 2 — ночной магазин / Пятёрочка |
| `cover/inline-03.png` | Inline 3 — чек-лист до перевода |
| `cover/logo-composite-stamp.json` | Logo paste stamp PASS |
| `cover/cover_qa.json` | Cover-QA PASS |
| `cover/slice4-mcp-result.json` | Grsai result metadata |

## Logo placement

- Corner: **top_right**
- XY: (1060, 20)
- Size: 120×82 px (~10% tile width)
- Cover only; inlines: 0 logos

## Gates

| Gate | Status |
|------|--------|
| cover_text_gate | PASS |
| motif_gate | PASS |
| slice4_gate | PASS |
| cover_qa_gate | PASS |

## Scene

- Hook on physical object: newspaper «Одно полотенце на четверых» (cover panel)
- Season: early September, sunny, high-key — NO winter
- Phone in scene: **skipped** (`forbid_cover_phone_on_image=true` in tenant-config)
