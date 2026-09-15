Не могу сформировать `.cursor/excalibur-blog-handoff.md` в этом интерфейсе: по контракту handoff-проза должна быть создана только через Derouter utility (`gpt-5.6-terra`), а доступ к shell/utility здесь отсутствует.

Входные данные готовы к передаче в команду:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role scout \
  --system-file skills/scout-excalibur-blog/SKILL.md \
  --user-file <assembled-scout-inputs.md> \
  --output .cursor/excalibur-blog-handoff.md \
  --article-dir <article_dir_or_memory/scout>
```

После генерации требуется выполнить:

```bash
python3 scripts/excalibur_blog_wordstat_gate.py handoff
```

Оснований для Wordstat blocker во входе нет: указан успешный `wordstat_get_user_info`, финальный guest P0 — «квартиры посуточно тюмень» с `4724` для регионов `55+11176` и сравнением `10016` по РФ (`225`).
