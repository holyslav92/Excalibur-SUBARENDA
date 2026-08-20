# Codex + AnyModel in GitHub Actions

The workflow installs Codex CLI and configures it as an OpenAI-compatible
custom provider using the Responses wire protocol:

- `base_url`: `https://anymodel.org/v1`
- model: `gpt-5.6-terra`
- auth: `OPENAI_API_KEY` populated at runtime from `ANYMODEL_API_KEY`

Add only this repository secret:

```bash
gh secret set ANYMODEL_API_KEY --repo holyslav92/Excalibur-2-Cloud
```

The command reads the value from stdin and does not put it in git. The
workflow never stores the key in a file or prints it.

The schedule is 12:00, 14:00, 16:00, and 18:00 in UTC+5 (07:00, 09:00,
11:00, and 13:00 UTC). It can also be started manually with `workflow_dispatch`.

The setup gate remains mandatory: until `memory/setup/status.json` is complete,
Codex stops without generating or publishing an article.
