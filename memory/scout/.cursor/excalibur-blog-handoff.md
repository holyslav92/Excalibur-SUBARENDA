DEROUTER SCOUT BLOCKER: в текущем окружении недоступны shell/Derouter utility и MCP-KV Wordstat, поэтому я не могу честно сформировать или записать `.cursor/excalibur-blog-handoff.md`.

Для B12 нужно запустить обязательный маршрут:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role scout \
  --system-file skills/scout-excalibur-blog/SKILL.md \
  --user-file <assembled-scout-inputs.md> \
  --output .cursor/excalibur-blog-handoff.md \
  --article-dir <article_dir_or_memory/scout>
```

Перед ним обязательны live-проверки `wordstat_get_user_info` и Wordstat-частот, затем:

```bash
python3 scripts/excalibur_blog_wordstat_gate.py handoff
```
