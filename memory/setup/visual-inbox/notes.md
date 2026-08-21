# Visual inbox — Добрый дом

## Режим

`brand_logo_paste` — официальный PNG **только** через factory paste после генерации.
**NEVER** просить image model нарисовать lockup.

## Official logo

- Положите обновление сюда: `logo-dobry-dom.png`
- Скопировать в: `memory/cover/assets/brand/logo-dobry-dom.png`
- Обновить `canonical_sha256` в `shared/tenant-config.json` → `logo_composite`

```bash
sha256sum memory/cover/assets/brand/logo-dobry-dom.png
python3 scripts/excalibur_blog_identity_real.py --stage-from-inbox
```

## Правила paste

- Cover: always ONE logo TOP-RIGHT 8–12%
- Inlines: 2–3 of 7 only (default inline_1, inline_3, inline_7)
- Generation: empty TOP-RIGHT pad — NO drawn curtains+flower/wordmark/dashed frame
