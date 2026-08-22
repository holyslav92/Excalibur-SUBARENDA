# Factory brain — Derouter REST (двухуровневый split)

**Тенант:** The Риэлтор  
**Провайдер:** Derouter REST API  
**Скрипт:** `scripts/excalibur_blog_derouter_opus_chat.py`  
**Endpoint:** `POST https://api.derouter.ai/openai/v1/chat/completions`  
**Fallback endpoint:** `https://api.apikey.cloud/openai/v1/chat/completions`  
**Auth:** `DEROUTER_API_KEY` только из Cloud Secrets

Источник истины по ролям: `shared/tenant-config.json` → `writing_model`.

**Opus 5 = Writer only; everything else Terra** — не возвращай scout/title/sol на powerful без явного решения тенанта.

## Два tier (HARD)

| Tier | Model id (Derouter) | Env override | Роли |
|------|---------------------|--------------|------|
| **powerful** | `claude-opus-5` | `DEROUTER_OPUS_MODEL` | writer |
| **utility** | `gpt-5.6-terra` | `DEROUTER_TERRA_MODEL` | scout, title, sol, research, description, cover-text, schema, cover-scene |

`resolve_model` выбирает tier по `--role`. **Не** используй глобальный `DEROUTER_TEXT_MODEL` как override всех ролей — если задан, он не переводит powerful-роли на non-Opus.

При 404 model id скрипт пробует алиасы (`gpt-5.6-terra`, `openai/gpt-5.6-terra` для utility; `claude-opus-5`, `anthropic/claude-opus-5` для powerful) и при smoke может зафиксировать рабочий id в tenant-config.

## Thin Cursor conductor (HARD)

Cursor Cloud Agent — **тонкий дирижёр**: git, shell, MCP Wordstat, image REST, Python gates.  
**Запрещено** писать прозу Scout/Research/Title/Writer/Sol/Description/Cover-text/Schema/Cover-scene моделью Cursor (Composer/Auto/inherit). **Не** переключать модель Cursor — conductor остаётся default Composer.

Для каждой текстовой роли:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role <scout|research|title|writer|sol|description|cover-text|schema|cover-scene> \
  --system-file <skill-or-agent.md> \
  --user-file <assembled-inputs.md> \
  --output <role-output-file> \
  --article-dir memory/blog/articles/<topic_id>-<slug>
```

1. Cursor **собирает** `--user-file` из входов (research, handoff, article.html…).
2. Cursor **вызывает** скрипт; берёт `--output` **как есть**.
3. Cursor **не переписывает** HTML/JSON/надписи после Derouter.
4. Stamp `derouter-opus-stamp-<role>.json` — tier + фактический model id (opus vs terra).

## Не Derouter chat (остаётся Cursor / Python / MCP)

- **Director** — оркестрация, Task, git, merge (Composer conductor, без article prose)
- **Wordstat** — MCP-KV (`wordstat_get_*`), не выдумывать частоты
- **Cover PNG** — Derouter image REST (см. `shared/derouter-gpt-image-api-contract.md`)
- **Cover-QA** — `scripts/excalibur_blog_cover_qa_gate.py` (pixel/gates)
- **Indexer / Publish / Fixer** — shell, WP, SFTP

## Fail loud (по роли)

`tenant-config.json` → `writing_model.fail_loud_if_unavailable: true`.

Если `DEROUTER_API_KEY` не задан или chat API недоступен после retry:

```text
DEROUTER <ROLE> BLOCKER
reason: DEROUTER_API_KEY missing or Derouter chat API unavailable; <tier> model not invoked
```

Скрипт делает **два полных вызова** роли (пауза `DEFAULT_RETRY_WAIT_SECONDS`, сейчас 5 с)
после первого `DerouterChatError`, прежде чем печатать BLOCKER (INC-20260822-1017).
Директор/Research при ручном recovery после BLOCKER обязан залогировать
`derouter_status` + `derouter_note` в `research-agent-report.json`.

Директор **останавливает** пайплайн. **Запрещено:** молча переключиться на Cursor Composer для article text.

## Smoke

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py --role smoke --smoke
```

- Terra ping (utility, cheaper) → `memory/setup/derouter-smoke-terra-stamp.json`
- Opus Writer one-liner → `memory/setup/derouter-smoke-opus-stamp.json`

## Запрещено

- `mcp-derouter/start-mcp.sh` — только REST
- Cursor-authored prose для любой роли из таблицы
- Тихий fallback на weaker model или Composer
- Документировать `model: claude-opus-5` / `gpt-5.6-terra` для Cursor Cloud Agent — эти id только для Derouter REST

## Legacy alias

`shared/writer-model-contract.md` — Writer-only Opus subset (Sol → utility Terra).
