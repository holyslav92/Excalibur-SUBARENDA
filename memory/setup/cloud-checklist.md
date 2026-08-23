# Cloud checklist — Добрый дом (Excalibur-SUBARENDA)

Ответы yes/no. **Секреты сюда не писать.**

| Пункт | Статус | Комментарий |
|-------|--------|-------------|
| Репозиторий подключён к Cursor Cloud Environment | yes | origin: holyslav92/Excalibur-SUBARENDA |
| **Не** подключать Excalibur-2-Cloud | required | Другой тенант (The Риэлтор) |
| Automation Tools → **Memories = OFF** | action_needed | Выключить вручную |
| Secrets: PUBLIC_SITE_URL | action_needed | `https://xn---72-9cdob8azaodt6k.xn--p1ai` |
| Secrets: FTP_HOST / FTP_USER / FTP_PASS / FTP_ROOT / FTP_PORT / FTP_TRANSPORT | action_needed | Timeweb FTP: vh368.timeweb.ru, port 21, root `sublease/public_html` |
| Secrets: EXCALIBUR_BLOG_ALLOW_PUBLISH | runtime only | `yes` только в Cloud Secrets; в git всегда `no` |
| Cover logo lockup | done | `memory/cover/assets/brand/logo-dobry-dom.png` на всех 8 |
| MCP-KV Wordstat (Scout **hard gate**) | required | dashboard connector |
| Image API key (Derouter) | required | `DEROUTER_API_KEY` в Cloud Secrets |
| Yandex Metrika tokens | optional | Content-learner |
| deploy llms после publish | yes | `publish_options.deploy_llms_after_publish=true` |
| First-run automation = Setup prompt | done | `memory/setup/status.json` complete |
| Daily automation = CLOUD-AUTOMATION.md | pending | 3× день YEKT 10/14/17 — `.cursor/automations/dobry-dom-3x.yml` |

## Разница First-run vs Daily

- **First-run:** тенант и voice уже заполнены; визуал = logo lockup (готово).
- **Daily:** Scout → Research → … → Cover-QA → Indexer; Publish только при FTP Secrets + `EXCALIBUR_BLOG_ALLOW_PUBLISH=yes` (runtime).
