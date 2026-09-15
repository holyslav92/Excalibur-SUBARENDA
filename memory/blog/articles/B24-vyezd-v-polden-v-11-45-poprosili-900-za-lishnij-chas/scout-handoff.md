Проверю обязательные источники, ротацию последних тем и доступность live Wordstat, затем соберу handoff только через Derouter.Не могу выполнить Scout handoff в этом окружении: нет доступа к обязательным инструментам MCP-KV (`wordstat_get_user_info` как первый вызов, live `top_requests`) и Derouter utility `gpt-5.6-terra`.

По жёсткому контракту нельзя:
- подтверждать или переносить частоты из входных данных вместо live MCP-KV;
- писать `.cursor/excalibur-blog-handoff.md` без Derouter;
- обновлять `memory/scout/klyshin-topic-bank.*` без доступа к файлам.

**WORDSTAT MCP BLOCKER / DEROUTER SCOUT BLOCKER.**  
Handoff не сформирован.
