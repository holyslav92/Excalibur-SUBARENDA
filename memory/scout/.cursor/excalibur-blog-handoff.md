Запускаю обязательную проверку конфигурации и затем передам собранный бриф Derouter; частоты беру только из предоставленного live MCP-KV лога.DEROUTER SCOUT BLOCKER

В этой среде недоступен запуск обязательной utility:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py ...
```

По жёсткому контракту Scout не может самостоятельно писать handoff-прозу, topic/title/rework log или `.cursor/excalibur-blog-handoff.md` без Derouter tier `gpt-5.6-terra`.

Предоставленный бриф содержит корректный preflight и live Wordstat-лог, однако требуется выполнить Derouter-команду с собранным input-файлом, а затем:

```bash
python3 scripts/excalibur_blog_wordstat_gate.py handoff
```

После доступа к utility можно продолжить без повторного подбора частот.
