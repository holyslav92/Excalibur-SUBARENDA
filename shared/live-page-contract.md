# Live page contract

Publish считается завершённым только после проверки фактической live-страницы.

## До публикации

`article.meta.json` должен отключать добавляемые темой универсальные блоки:

```json
{
  "theme_blocks": {
    "faq": "skip",
    "quiz": "skip",
    "side_stickers": "skip"
  }
}
```

В статье остаётся ровно один тематический FAQ. Универсальный FAQ, квиз и
боковые стикеры темы не должны дублировать контент.

## После публикации

Publish запускает:

```bash
python3 scripts/excalibur_blog_live_page_gate.py \
  --permalink <permalink> \
  -o <article_dir>/live-page-report.json
```

`live-page-report.json` должен иметь `status: PASS` и подтвердить:

- HTTP 200 и ожидаемый title/body;
- один тематический FAQ, без FAQ темы;
- theme share chrome (`.article-share` / `<!-- Share buttons -->` / «Поделиться»)
  после последнего FAQ-ответа **не** считается текстом ответа — gate обрезает
  FAQ body до share row (INC-20260720-2036);
- FAQPage JSON-LD parity с visible FAQ использует ту же нормализацию пробелов
  после strip inline `<a>`, что и `schema_gate` (INC-20260720-2028);
- **Dobry dom / kov4eg theme:** gate принимает `entry-content`,
  `articles-typical__content` или article wrapper с `inline-quad`; featured —
  `post-thumbnail` или `articles-typical__image` (INC-20260822-1017);
- **Schema /blog parity:** canonical и BlogPosting URL сравниваются с
  опубликованным permalink с учётом `/blog/{slug}/` vs `/{slug}/`
  (INC-20260822-1017);
- **Theme JSON-LD lag:** если тема ещё не выводит meta-schema в `<head>`,
  publish передаёт `expected_schema_jsonld` из payload — gate сверяет FAQPage
  и BlogPosting с тем, что записано в `_excalibur_blog_schema_jsonld`
  (INC-20260822-1017). `excalibur_blog_wp_publish.py` перед upload идемпотентно
  вызывает `excalibur_blog_theme_contract_deploy.py --deploy` (можно
  `--skip-theme-deploy` в emergency);
- dash parity: WP `wptexturize` может заменить ASCII `--` в HTML на em dash
  (`—` / `&#8212;`), пока FAQPage JSON-LD хранит `--` — gate схлопывает
  em/en dash и `--+` в один `-` (INC-20260721-1655);
- backslash parity: publish bootstrap обязан `wp_slash` post title/content/
  excerpt перед `wp_insert_post`/`wp_update_post` (INC-20260723-1254). Иначе
  literal `\` в Windows paths исчезает из visible FAQ, а FAQPage JSON-LD
  (meta + `wp_slash`) сохраняет → false FAQ mismatch;
- нет theme quiz и side stickers;
- нет дублей CTA/контента;
- cover/inline media доступны, alt честен;
- schema и canonical относятся к текущей статье.

FAIL = `LIVE PAGE BLOCKER`: нельзя писать `PIPELINE DONE`, обновлять ledger как
успешно опубликованный или запускать post-run learning как успешный запуск.
