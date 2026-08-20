# Yandex Metrica → Excalibur content learning

Docs hub: https://yandex.ru/dev/metrika/

## Purpose

Pull **on-site** page stats (pageviews/users) via Reports API and feed
`excalibur_blog_site_feedback_ingest.py` → `memory/content-lessons.md`.

This is **not** SERP CTR. For search CTR use Yandex Webmaster / GSC later.

## Secrets (Cloud Secrets / env — never commit)

```env
YANDEX_METRIKA_OAUTH_TOKEN=...   # OAuth, scope metrika:read
YANDEX_METRIKA_COUNTER_ID=...    # numeric counter id
```

Get token:

1. Create app at https://oauth.yandex.ru/
2. Enable Metrika access `metrika:read`
3. Open `https://oauth.yandex.ru/authorize?response_type=token&client_id=<app_id>`
4. Put token + counter id into Cursor Cloud Secrets

## Agent vs script

- **Agent** (content-learner / Director): запускает на **каждом post-run**
  после publish/skip, до записи lessons.
- **Script** `excalibur_blog_metrika_fetch.py`: deterministic API pull + slug map from `shared/published-articles.md`.
- **Script** `excalibur_blog_site_feedback_ingest.py`: writes LESSON blocks.

Канонический обязательный вызов:

```bash
python3 scripts/excalibur_blog_metrika_fetch.py --days 30 --ingest
```

`--ingest` автоматически передаёт ingest-скрипту дедупликацию идентичного
наблюдения. Поэтому каждый cron-run забирает свежий snapshot, но не плодит
одинаковый LESSON при повторном запуске за тот же период.

Успех: handoff содержит `metrika_feedback: PASS`, `period_days: 30` и
`matched_rows`. Ошибка credentials/API — `METRIKA FEEDBACK BLOCKER` и incident;
нельзя молча пропустить шаг или выдумать метрики.

## Commands

```bash
# ledger smoke (no API)
python3 scripts/excalibur_blog_metrika_fetch.py --dry-run-ledger

# fetch last 30 days → memory/site-feedback-metrika.json
python3 scripts/excalibur_blog_metrika_fetch.py --days 30

# fetch + ingest lessons
python3 scripts/excalibur_blog_metrika_fetch.py --days 30 --ingest
```

## API used

```http
GET https://api-metrika.yandex.net/stat/v1/data
Authorization: OAuth <token>
ids=<COUNTER_ID>
metrics=ym:s:visits,ym:s:users,ym:s:pageviews,ym:s:bounceRate,ym:s:avgVisitDurationSeconds,ym:s:pageDepth
dimensions=ym:s:startURLPath
date1=...&date2=...
```

`startURLPath` is the session landing path and is compatible with session
metrics. Paths are matched to ledger slugs (`/my-slug/` → `my-slug` →
`topic_id`). A cohort analysis is written to
`memory/analytics/metrika-latest.json`; only its actionable rows can become
content-learning lessons.

## Git-safe artifacts (secret-scan)

`excalibur_blog_metrika_fetch.py` writes commit-bound files under `memory/`.
On write it must:

- set `counter_id` to `[REDACTED]` — never persist live `YANDEX_METRIKA_COUNTER_ID`;
- normalize every `url_path` to path-only `/slug` (strip `https://host/...`,
  malformed `/https://host/slug`, `{{SITE_BASE}}` / `{{SITE_HOST}}` /
  `[REDACTED]` prefixes).

Before commit, secret-scan Metrika JSON/CSV for live `PUBLIC_SITE_URL` host and
numeric counter id. Live credentials stay in Cloud Secrets / env only.

## Blockers

- Missing secrets → `METRIKA CREDENTIALS BLOCKER` (exit 2), do not invent metrics.
- 401 → token invalid / wrong header.
- 403 → app missing `metrika:read` or user has no access to counter.
