SCOUT BLOCK

Не могу корректно выпустить handoff: в текущем окружении недоступны обязательные инструменты и файлы для проверки контракта:

- Derouter utility `gpt-5.6-terra` — handoff-проза должна проходить только через него;
- MCP-KV Wordstat — требуется самостоятельный preflight `wordstat_get_user_info`;
- `memory/scout/klyshin-topic-bank.md` и `.json`;
- `shared/published-titles.md` для проверки последних N=3;
- свежий внешний сигнал `klyshin_A` и дополнительный tenant-сигнал.

Переданные вами частоты и строки Wordstat нельзя использовать как замену обязательному live-вызову. Поэтому `.cursor/excalibur-blog-handoff.md` не создаю и полный handoff не выдаю.
