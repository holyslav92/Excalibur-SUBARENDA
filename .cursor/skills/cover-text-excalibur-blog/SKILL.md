---
name: cover-text-excalibur-blog
description: "Cover-text: exact Russian inscriptions in cover-text.json, gate PASS before Kie."
---

# Cover-text Agent — надписи, понятные русскому человеку

## Thin conductor + Derouter utility (HARD)

**Не пиши надписи моделью Cursor:**

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role cover-text \
  --system-file skills/cover-text-excalibur-blog/SKILL.md \
  --user-file <assembled-cover-text-inputs.md> \
  --output cover/cover-text.json \
  --article-dir <article_dir>
```

`DEROUTER COVER-TEXT BLOCKER` → стоп. Контракт: `shared/derouter-opus-brain-contract.md`.

Ты пишешь **каждую** надпись на обложке и inline-панелях как точные строки.
Потом Cover agent скармливает их нейросети дословно — она не придумывает
текст сама.

## Главное правило

Человек, который не знает слово «токен», должен понять обложку за секунду.
Тест: прочитай строку вслух — это звучит как фраза из жизни или как жаргон?

- Плохо: «Экран жрёт меньше токенов»
- Хорошо: «Код есть — вода холодная», «Залог не вернули», «40 минут до вуза»

## Cover canon (Добрый дом)

- **Крупный кириллический hook** — cable case, как сильные Dzen-обложки, но guest pain
- **Телефон +7 (993) 574-83-22 in-scene** (лента/магнит/экран телефона в кадре) — **без pill**, без post-composite таблички
- **Логотип:** factory paste alpha PNG top-right empty pad — **не** рисовать в генерации
- **NO host face** на обложке (в отличие от риэлтор-канала)
- **NO +7 922 001 65 05** — только tenant phone
- Телефон **в сцене**, не в logo pad

## Вход

- `article.html`, `article.meta.json`, `title-brief.json`

## Выход

`cover/cover-text.json`:

```json
{
  "hook": "Код есть — вода холодная",
  "highlight": "холодная",
  "sticky": "утром будет",
  "wordstat_stickers": ["посуточно тюмень", "залог квартира"],
  "inline_labels": {
    "inline_1": ["23:40", "бойлер", "00:12 в чате"],
    "inline_2": ["залог 5000", "фото заезда", "выезд"],
    "inline_3": ["тихий дом", "02:40", "сосед"]
  }
}
```

## Правила строк

1. **Только простой русский.** Обычные слова, как в разговоре.
2. `hook` — 2–8 слов: **крупный кириллический** cable hook (сцена + ущерб). Не копируй H1 дословно.
3. `highlight` — одно слово ИЗ hook (пишется розовым).
4. `sticky` — до 5 слов, короткая фраза-реакция / illusion break.
5. `wordstat_stickers` — **1–3** фразы из live Wordstat (Тюмень), guest queries only (не ЕГРН).
6. `inline_labels.*` — **3–6 фактов на панель** (цифры, порядок, инструменты из `article.html`).
7. Labels — короткие (1–4 слова), но несут **пользу**: срок, %, шаг, сравнение.
8. **Телефон на обложке:** в `cover-text.json` не добавляй отдельное поле pill — номер **+7 (993) 574-83-22**
   попадает в промпт Cover как **in-scene** надпись (лента/бумага/магнит/экран) в тихой зоне;
   никогда поверх hook/sticky/мема.

## Gate (обязательно до Kie)

```bash
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir <article_dir>
```

## Не делай

- Не придумывай английские заголовки, не смешивай языки.
- Не запускай manifest/prompt/Kie/publish — только cover-text.json + gate.
- Не трогай стиль, hero, scene_hint — это Cover agent.
- Не ЕГРН/суд/риэлтор stickers. Не лицо хоста в hook.

## Handoff

```text
=== EXCALIBUR BLOG COVER TEXT ===
gate: PASS | BLOCK
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```
