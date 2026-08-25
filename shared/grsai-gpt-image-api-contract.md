# Grsai image REST API Contract

Primary Cloud path for Excalibur BLOG cover/inline quad canvas when `IMAGE_PROVIDER=grsai`.

## Order of preference (mandatory)

```text
1. GRSAI_API_KEY set → scripts/excalibur_blog_grsai_gpt_image2_api.py
2. KIE_API_KEY set      → scripts/excalibur_blog_kie_gpt_image2_api.py (after Grsai fail + --fallback-kie)
3. neither              → BLOCKER (GRSAI API KEY MISSING / KIE API BLOCKER)
```

**FORBIDDEN forever:** `*-vip`, any `*-vip` model, starting with vip, `flux2-pro-*`, Seedream, `nano_banana*`, `z-image`, `mcp-derouter/start-mcp.sh`.

## 2K quality policy (mandatory — owner)

1. **Model:** only PRIMARY_MODEL_ID (`PRIMARY_MODEL_ID`). VIP permanently disabled.
2. **Request 2K:** `aspectRatio=16:9`, `resolution=2K`, `quality=high` on first attempt.
3. **Undersized retry:** if non-vip returns ~1672×941 (long side &lt;1920), **one** extra attempt on the **same** model with explicit `size=2048x1152` (alternate host). **Do not** escalate to vip.
4. **Ship native:** if still undersized after retry, ship the largest native non-vip frame. Log `vip_disabled`, `shipped_native` WxH. No upscale of soft ~1672×941 frames.
5. **2K-class upscale:** native long side ≥1920 but &lt;2048 → Lanczos upscale to **2048×1152** allowed.

Logged in `quad-mcp-result-*.json`: `model_succeeded`, `vip_disabled`, `used_vip_fallback` (always false), `delivery`, `native_long_side`, `shipped_native`.

## Model policy

1. **Only** PRIMARY_MODEL_ID (`GRSAI_IMAGE_MODEL` must not be vip).
2. **Never** call `*-vip` or any `*-vip` tier.
3. Text roles stay on Derouter (`excalibur_blog_derouter_opus_chat.py`) — only image backend changes.

## Host

| Priority | Base URL | Region |
|----------|----------|--------|
| 1 (default) | global Grsai host (see probe) | Global |
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

**First attempt (2K request):**

```json
{
  "model": "gpt-image-\u0032",
  "prompt": "...",
  "aspectRatio": "16:9",
  "resolution": "2K",
  "quality": "high",
  "webHook": "-1",
  "images": []
}
```

**Undersized retry (explicit pixel size on same model):**

```json
{
  "model": "gpt-image-\u0032",
  "prompt": "...",
  "size": "2048x1152",
  "quality": "high",
  "webHook": "-1"
}
```

- **webHook:** `"-1"` → sync polling mode (no callback URL)
- **images:** optional reference URLs or base64 data-URLs for i2i
- Response: `data.id` = task id

### aspectRatio → 2K long side (Grsai, resolution=2K)

| aspectRatio | Expected native long side | Factory target (16:9 quad) |
|-------------|---------------------------|----------------------------|
| `16:9` | ~1672 (non-vip aspect-only) or 2048 (explicit size) | **2048×1152** |
| `9:16` | 2048 | per aspect |
| `1:1` | 2048 | 2048×2048 |
| `4:3` | 2048 | per aspect |
| `3:4` | 2048 | per aspect |

Non-vip with `aspectRatio`+`resolution=2K` may return &lt;1920 long side → explicit-size retry, then ship native if still undersized.

### 2. Poll result

`POST {base}/v1/draw/result` (JSON):

```json
{ "id": "<task_id>" }
```

- `status`: `running` → wait; `succeeded` → `results[0].url`; `failed` / `violation` → BLOCKER
- Default poll: 5s interval, max 900s

### 3. Download + 2K gate

1. Download `results[0].url`
2. Assert **long side ≥2048** (or native ≥1920 → Lanczos upscale to **2048×1152** only for 2K-class sources)
3. If long side &lt;1920 on non-vip after explicit-size retry → **ship native** (`vip_disabled`, no upscale)

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

- Fallback host `grsai.dakka.com.cn` after global exhausted (hard API only)
- Undersized: one explicit-size retry on same PRIMARY_MODEL_ID (alternate host); then ship native
- Kie fallback when Grsai still fails and `KIE_API_KEY` set

## Related

- Kie fallback: `shared/kie-gpt-image-api-contract.md`
- Derouter (legacy): `shared/derouter-gpt-image-api-contract.md`
