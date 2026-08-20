# Cloud checklist — The Риэлтор

Ответы yes/no. **Секреты сюда не писать.**

| Пункт | Статус | Комментарий |
|-------|--------|-------------|
| Репозиторий подключён к Cursor Cloud Environment | yes | origin: holyslav92/Excalibur-2-Cloud |
| Automation Tools → **Memories = OFF** | action_needed | Выключить вручную; docs: Memories ON by default |
| Secrets: PUBLIC_SITE_URL | action_needed | Значение: сайт тенанта (https в Secrets, в git — {{SITE_BASE}}) |
| Secrets: FTP_HOST / FTP_USER / FTP_PASS / FTP_ROOT | action_needed | Нужны перед Publish; локально — `memory/site.env.local` (gitignored) |
| Secrets: EXCALIBUR_BLOG_ALLOW_PUBLISH=yes | yes (local) | Runtime only — в Cloud Secrets, не в git; локально уже в site.env.local |
| DEROUTER_IMAGE_QUALITY=high | yes (local) | Cover Derouter; tenant `publish_options.derouter_image_quality` |
| MCP-KV Wordstat (Scout **hard gate**) | required in Cloud Tools | `wordstat_get_user_info` + `wordstat_get_top_requests`; dashboard connector — never git |
| MCP WordPress blob / image API (если нужны) | optional | WP уже на сайте тенанта |
| Image API key (Derouter) | required | `DEROUTER_API_KEY` в Cloud Secrets |
| Yandex Metrika tokens | recommended | Content-learner: `YANDEX_METRIKA_OAUTH_TOKEN` + counter id |
| CTA обязателен (TG + tel + MAX) | yes | `tenant-config.cta_required=true` |
| Interlink старых статей | yes | `interlink_old_articles=true` |
| deploy llms после publish | yes | `publish_options.deploy_llms_after_publish=true` |
| First-run automation = Setup prompt | yes | Этот прогон |
| Daily automation = CLOUD-AUTOMATION.md (после setup) | pending | 4× будни YEKT: 09:00, 12:00, 15:00, 17:00 (окно 9–17; не 20:00). Cursor Automations, не GHA |

## Разница First-run vs Daily

- **First-run:** заполнить тенанта, SOUL, визуал. Не Scout/Publish.
- **Daily:** после setup — канон Scout → Research → … → Cover-QA → Indexer; Publish только при FTP + `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` (runtime).
