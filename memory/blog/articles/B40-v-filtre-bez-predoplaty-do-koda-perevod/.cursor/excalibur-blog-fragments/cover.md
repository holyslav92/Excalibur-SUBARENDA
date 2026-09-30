status: PASS
topic_id: B40
canon: dobry_dom_gen_only_human_v1
pipeline: slice4_grid_1x_image_api (1× Grsai VIP 2048×1152 → 4 PNG)
artifacts:
  - cover/cover.png
  - cover/inline-01.png
  - cover/inline-02.png
  - cover/inline-03.png
  - cover/canvas-slice4.png
gates: cover-text PASS, slice4 PASS, logo-composite PASS, cover_qa PASS
notes: vip tier used as automatic fallback after primary undersized 1672px canvas
