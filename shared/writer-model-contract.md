# Writer — Opus 5 only (Derouter REST)

> Канонический контракт всего «мозга» фабрики:
> **`shared/derouter-opus-brain-contract.md`**
>
> **Opus 5 = Writer only; utility gpt-6-luna**

Writer — **единственная** роль на powerful tier (`claude-opus-5-5` via Derouter REST).
Sol, Scout, Title и все прочие текстовые роли — utility tier (`gpt-6-luna`).

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role writer \
  --system-file <skill.md> \
  --user-file <inputs.md> \
  --output drafts/writer.html \
  --article-dir <article_dir>
```

- **Model:** `claude-opus-5-5` (env `DEROUTER_OPUS_MODEL`, семейство Claude Opus 5.5)
- **Auth:** `DEROUTER_API_KEY` только из Cloud Secrets
- **Endpoint:** `https://api.derouter.ai/openai/v1/chat/completions`

Utility tier (`gpt-6-luna`) — Scout, Title, Sol, Research, Description, Cover-text, Schema, Cover-scene. См. brain contract.

## Fail loud

`DEROUTER WRITER BLOCKER` — без тихого fallback на Composer или utility gpt-6-luna.

Полный контракт: `shared/derouter-opus-brain-contract.md`.
