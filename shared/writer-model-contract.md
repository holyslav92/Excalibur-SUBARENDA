# Writer / Sol — powerful tier (Derouter Opus REST)

> Канонический контракт всего «мозга» фабрики:
> **`shared/derouter-opus-brain-contract.md`**

Writer и Sol — **powerful tier** (`claude-opus-5` via Derouter REST).

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role writer|sol \
  --system-file <skill.md> \
  --user-file <inputs.md> \
  --output <drafts/writer.html|article.html> \
  --article-dir <article_dir>
```

- **Model:** `claude-opus-5` (env `DEROUTER_OPUS_MODEL`, семейство Claude Opus 5)
- **Auth:** `DEROUTER_API_KEY` только из Cloud Secrets
- **Endpoint:** `https://api.derouter.ai/openai/v1/chat/completions`

Utility tier (`gpt-5.6-terra`) — Research, Description, Cover-text, Schema, Cover-scene. См. brain contract.

## Fail loud

`DEROUTER WRITER BLOCKER` / `DEROUTER SOL BLOCKER` — без тихого fallback на Composer или Terra.

Полный контракт: `shared/derouter-opus-brain-contract.md`.
