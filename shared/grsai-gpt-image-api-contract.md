# Grsai image REST API Contract

Primary Cloud path for Excalibur BLOG cover/inline quad canvas when `IMAGE_PROVIDER=grsai`.

## Order of preference (mandatory)

```text
1. GRSAI_API_KEY set → scripts/excalibur_blog_grsai_gpt_image2_api.py
2. KIE_API_KEY set      → scripts/excalibur_blog_kie_gpt_image2_api.py (after Grsai fail + --fallback-kie)
3. neither              → BLOCKER (GRSAI API KEY MISSING / KIE API BLOCKER)
```

**FORBIDDEN as first try:** starting with vip, more than one vip per canvas/sheet, `flux2-pro-*`, Seedream, `nano_banana*`, `z-image`, `mcp-derouter/start-mcp.sh`.

## 2K quality policy (mandatory — owner)

1. **Ship only ≥2K:** factory canvas / output long side **≥2048** (quad contract **2048×1152** for 16:9).
2. **VIP economy (opt-in `GRSAI_VIP_ECONOMY=1`):** для **16:9** quad canvas можно сразу **один** vip-вызов (`vip_trigger=economy_skip_primary_16_9`) — primary non-vip иногда отдаёт ~1672×941. **По умолчанию OFF.**
3. **Standalone cover (`type_meme_sticker_v3`):** batch `standalone_cover=true` / `vip_disabled=true` → **primary only**, max 2 attempts, `GRSAI_FORBID_VIP=1`; затем pad-clear + factory logo paste.
4. **Иначе prefer non-vip** primary tier когда он отдаёт ≥2K нативно.
5. **VIP trigger (fallback):** non-vip не достигает ≥2K на не-16:9 аспектах, hard API fail → **один** vip-tier attempt.
6. **Do not default to VIP** когда non-vip успешно вернул long side ≥2048.
7. **Никогда не апскейлить** soft ~1672×941 до 2048 — только native vip 2K или ship native 1024×576 panel без Lanczos.

Logged in `quad-mcp-result-*.json`: `model_succeeded`, `used_vip_fallback`, `vip_trigger` (`2k_not_possible_on_primary` | `api_failure` | null), `native_long_side`, `delivery`.

## Model policy

1. Always **non-vip** first (`GRSAI_IMAGE_MODEL` — must not be vip).
2. **One vip** per sheet only when rules above fire.
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

**Non-vip (2K request):**

```json
{
  "model": "<GRSAI_IMAGE_MODEL>",
  "prompt": "...",
  "aspectRatio": "16:9",
  "resolution": "2K",
  "quality": "high",
  "webHook": "-1",
  "images": []
}
```

**VIP (native pixel size — aspectRatio rejected):**

```json
{
  "model": "<GRSAI_IMAGE_MODEL>-vip",
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
| `16:9` | 2048 (vip) / ~1672 (non-vip aspect-only — **undersized → vip**) | **2048×1152** |
| `9:16` | 2048 | per aspect |
| `1:1` | 2048 | 2048×2048 |
| `4:3` | 2048 | per aspect |
| `3:4` | 2048 | per aspect |

Non-vip with `aspectRatio`+`resolution=2K` may still return &lt;1920 long side → script raises `Grsai2KNotMetError` and escalates to vip **without** upscaling soft frames.

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
3. If long side &lt;1920 on non-vip → **vip** (no upscale of soft ~1672×941 frames)

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

- Fallback host `grsai.dakka.com.cn` after global exhausted (hard API only — **not** for 2K/size on non-vip)
- Model fallback: non-vip → one vip per sheet (`2k_not_possible_on_primary` or `api_failure`)
- Kie fallback when Grsai still fails and `KIE_API_KEY` set

## Related

- Kie fallback: `shared/kie-gpt-image-api-contract.md`
- Derouter (legacy): `shared/derouter-gpt-image-api-contract.md`
