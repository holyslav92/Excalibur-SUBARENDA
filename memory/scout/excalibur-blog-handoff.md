SCOUT BLOCK.

Не могу завершить handoff по контракту: в текущем интерфейсе недоступны MCP-KV Wordstat и Derouter utility tier. Поэтому я не могу подтвердить обязательный preflight `wordstat_get_user_info`, заново получить live-частоты и передать handoff через:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py ...
```

Предоставленные в запросе частоты не заменяют обязательный live MCP-вызов. Файл `.cursor/excalibur-blog-handoff.md` не создан.
