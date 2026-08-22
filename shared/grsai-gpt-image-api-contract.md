# Grsai image REST API Contract

Primary Cloud path for Excalibur BLOG cover/inline quad canvas when `IMAGE_PROVIDER=grsai`.

## Order of preference (mandatory)

```text
1. GRSAI_API_KEY set → scripts/excalibur_blog_grsai_gpt_image2_api.py
2. KIE_API_KEY set      → scripts/excalibur_blog_kie_gpt_image2_api.py (after Grsai fail + --fallback-kie)
3. neither              → BLOCKER (GRSAI API KEY MISSING / KIE API BLOCKER)
```

**FORBIDDEN as first try:** starting with vip, more than one vip per canvas/sheet, `flux2-pro-*`, Seedream, `nano_banana*`, `z-image`, `mcp-derouter/start-mcp.sh`.

**Model policy (mandatory):**

1. Always primary tier first (``gpt`` + ``-image-`` + ``2``; or `GRSAI_IMAGE_MODEL` if set — must not be vip).
2. Only if that sheet fails (API error, `failed`/`violation`, timeout after host retries) → **one** vip-tier attempt for the same sheet.
3. Log `model_succeeded` in `quad-mcp-result-*.json` (no secrets).

Text roles stay on Derouter (`excalibur_blog_derouter_opus_chat.py`) — only image backend changes.

## Host

| Priority | Base URL | Region |
|----------|----------|--------|
| 1 (default) | `https://grsaiapi.com` | Global |
| 2 (fallback) | `https://grsai.dakka.com.cn` | China |

Override one run: `GRSAI_API_BASE` (bare host, no path).

Probe:

```bash
python3 scripts/excalibur_blog_grsai_base_probe.py
```

→ `memory/blog/grsai-image-base-probe.json` (status + short error, без ключа).

## Async draw API

### 1. Create task

`POST {base}/v1/draw/completions` (JSON):

```json
{
  "model": "<GRSAI_IMAGE_MODEL>",
  "prompt": "...",
  "aspectRatio": "16:9",
  "quality": "high",
  "webHook": "-1",
  "images": []
}
```

- **model:** primary tier first (see `excalibur_blog_grsai_gpt_image2_api.primary_model`); optional `GRSAI_IMAGE_MODEL` override (non-vip only)
- **vip fallback:** one vip-tier attempt per sheet after primary failure; vip uses `size: 2048x1152` (not `aspectRatio`)
- **webHook:** `"-1"` → sync polling mode (no callback URL)
- **images:** optional reference URLs or base64 data-URLs for i2i
- Response: `data.id` = task id

### 2. Poll result

`POST {base}/v1/draw/result` (JSON):

```json
{ "id": "<task_id>" }
```

- `status`: `running` → wait; `succeeded` → `results[0].url`; `failed` / `violation` → BLOCKER
- Default poll: 5s interval, max 900s

### 3. Download + upscale

Script downloads `results[0].url`, then **upscales canvas to 2048×1152** if Grsai returned a smaller 16:9 frame.

Writes `cover/canvas-quad-NN.png` + `quad-mcp-result-NN.json` with `local_path` for `quad_apply`.

## Auth

- `GRSAI_API_KEY` only (Cursor Cloud Secrets). Missing → `GRSAI API KEY MISSING`
- `GRSAI_IMAGE_MODEL` optional override for primary tier (must not be vip)
- Optional: `GRSAI_API_BASE`
- Never commit, print, or copy keys into git/PR/logs

Doctor: **WARN** when `GRSAI_API_KEY` missing and `image_api.provider=grsai`; Cover gen **BLOCKs**.

## Cover command

```bash
python3 scripts/excalibur_blog_grsai_gpt_image2_api.py \
  --article-dir memory/blog/articles/<topic_id>-<slug> \
  --batch cover/quad-mcp-batch-01.json \
  --result cover/quad-mcp-result-01.json
```

Then:

```bash
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 1 --inject-html
python3 scripts/excalibur_blog_quad_apply.py --article-dir <dir> --canvas-index 2 --inject-html
```

## Retry

- Fallback host `grsai.dakka.com.cn` after global exhausted
- Model fallback: primary tier → one vip-tier retry per sheet on API/moderation/timeout fail
- Kie fallback when Grsai still fails and `KIE_API_KEY` set

## Related

- Kie fallback: `shared/kie-gpt-image-api-contract.md`
- Derouter (legacy): `shared/derouter-gpt-image-api-contract.md`
