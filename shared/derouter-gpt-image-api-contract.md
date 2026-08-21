# Derouter image REST API Contract

Primary Cloud path for Excalibur BLOG cover/inline quad canvas generation.

## Order of preference (mandatory)

```text
1. DEROUTER_API_KEY set → scripts/excalibur_blog_derouter_gpt_image2_api.py
2. KIE_API_KEY set      → scripts/excalibur_blog_kie_gpt_image2_api.py (after Derouter auth/5xx + one retry)
3. neither              → BLOCKER (DEROUTER API KEY MISSING / KIE API BLOCKER)
```

**FORBIDDEN:** `flux2-pro-text-to-image`, `flux2-pro-image-to-image`, Seedream, `nano_banana*`, `z-image`, `mcp-derouter/start-mcp.sh` (broken stdio MCP).

## Host (images — HARD)

**Always** `https://api-direct.derouter.ai/openai/v1` for image gen/edits.

- Timeout: **≥240s** client; default script **600s**
- **Do not** use `https://api.derouter.ai` for images — Cloudflare ~100s → **HTTP 524** on long gen
- Fallback alias: `https://api-direct.apikey.cloud/openai/v1`

Text (factory brain): `scripts/excalibur_blog_derouter_opus_chat.py` — Opus 5 = Writer only; everything else Terra. См. `shared/derouter-opus-brain-contract.md`.

## Text → image

`POST /images/generations` (JSON):

```json
{
  "model": "<DEROUTER_IMAGE_MODEL>",
  "prompt": "...",
  "size": "2048x1152",
  "quality": "auto"
}
```

- `size` / `quality` optional; omit → 2K medium tier
- Explicit quad 16:9 2K = **`2048x1152`**
- **No** `aspect_ratio` field (batch may carry it for Kie only; Derouter script ignores it)
- Response: **`data[0].b64_json`** (PNG base64) — **not** a URL

Script decodes b64 → `cover/canvas-quad-NN.png` (from batch `output_canvas`) and writes `quad-mcp-result-NN.json` with `local_path` for `quad_apply`.

## Image → image

`POST /images/edits` (multipart/form-data):

```text
-F model=<DEROUTER_IMAGE_MODEL>
-F prompt="..."
-F image=@identity-real.png
```

- **No** `input_urls`, no JSON data-URL
- Multi-ref: repeat `-F image[]=@file`
- Output still `b64_json`

Canvas 1: `prefer_local_reference` + `identity_reference_local` → local file attach only.

Canvas 2: no local ref → `/images/generations` (t2i).

## Auth

- `DEROUTER_API_KEY` only (Cursor Cloud Secrets). Missing → `DEROUTER API KEY MISSING`
- `DEROUTER_IMAGE_MODEL` required (id from GET `/v1/models`)
- Optional: `DEROUTER_IMAGE_SIZE` (default `2048x1152`), `DEROUTER_IMAGE_QUALITY` (default `auto`)
- Never commit, print, or copy keys into git/PR/logs

Doctor: **WARN** when `DEROUTER_API_KEY` or `DEROUTER_IMAGE_MODEL` missing; Cover gen **BLOCKs**.

## Cover command

```bash
python3 scripts/excalibur_blog_derouter_gpt_image2_api.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --batch cover/quad-mcp-batch-01.json \
  --result cover/quad-mcp-result-01.json \
  --fallback-kie
```

Then:

```bash
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 2 --inject-html
```

## Retry

- One retry per host on auth/5xx/524 (`--max-retries 1`)
- Fallback host `api-direct.apikey.cloud` after primary exhausted
- `--fallback-kie` when Derouter still fails and `KIE_API_KEY` set

## Price / quality

- 2K tier (`quality: auto`); do **not** request 4K unless owner asks

## Related

- Quad canvas: `shared/blog-cover-quad-canvas-contract.md`
- Kie fallback: `shared/kie-gpt-image-api-contract.md`
