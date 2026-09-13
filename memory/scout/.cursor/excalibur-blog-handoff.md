Принял слот B20: проверю ротацию и файлы банка, затем передам собранный контекст Derouter для обязательного handoff.DEROUTER SCOUT BLOCKER: в текущей среде недоступны shell/Derouter utility и файловая запись, поэтому я не могу легитимно сформировать или записать `.cursor/excalibur-blog-handoff.md`.

Wordstat-данные из входа приняты как уже пройденные live-проверки, но handoff-прозу по контракту должен генерировать только `gpt-5.6-terra` через:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role scout \
  --system-file skills/scout-excalibur-blog/SKILL.md \
  --user-file <assembled-scout-inputs.md> \
  --output .cursor/excalibur-blog-handoff.md \
  --article-dir <article_dir_or_memory/scout>
```

После генерации требуется запустить:

```bash
python3 scripts/excalibur_blog_wordstat_gate.py handoff
```

Не создаю handoff вручную, чтобы не нарушить обязательный Derouter-only контракт.
