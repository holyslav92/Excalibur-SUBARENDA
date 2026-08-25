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

- Плохо: «Экран жрёт меньше токенов» (мишанина: что за экран, что за жрёт)
- Хорошо: «Cursor стал дешевле», «Агент сам отвечает на заявки»,
  «Почта и таблицы теперь внутри Cursor»

## Вход

- `article.html`, `article.meta.json`, `title-brief.json`

## Выход

`cover/cover-text.json`:

```json
{
  "hook": "Cursor стал дешевле на треть",
  "highlight": "дешевле",
  "sticky": "новой модели нет",
  "wordstat_stickers": ["квартира тюмень", "проверить егрн"],
  "inline_labels": {
    "inline_1": ["заявление 3 августа", "минус 20–30%", "без новой модели"],
    "inline_2": ["с работой за экраном", "минус 80%", "проверь сам"],
    "inline_3": ["MCP", "навыки", "экран"]
  }
}
```

## Правила строк

1. **Только простой русский.** Обычные слова, как в разговоре. Жаргон
   («токены», «рантайм», «harness») — только если без него тему не назвать,
   и тогда рядом простое объяснение в другой надписи.
2. `hook` — 2–8 слов: кто + что случилось + зачем мне. Не копируй H1
   дословно, не пиши определение, не метафору без темы.
3. `highlight` — одно слово ИЗ hook (пишется розовым).
4. `sticky` — до 5 слов, короткая фраза-реакция.
5. `wordstat_stickers` — **1–3** фразы из live Wordstat (Тюмень).
6. `inline_labels.*` — **3–6 фактов на панель** (цифры, порядок, инструменты из `article.html`). Не слоганы настроения, не «типичные ошибки» без конкретики.
7. Labels — короткие (1–4 слова), но несут **пользу**: срок, %, шаг, сравнение.
   брендов (Cursor, Make, MCP, AI, OpenAI…).
8. **Телефон на обложке:** в `cover-text.json` не добавляй отдельное поле pill — номер **+7 (993) 574-83-22**
   попадает в промпт Cover как **in-scene** надпись (лента/бумага/магнит) в тихой зоне снизу или сбоку;
   никогда поверх мема/кота/sticky/заголовка.

## Gate (обязательно до Kie)

```bash
python3 scripts/excalibur_blog_cover_text_gate.py --article-dir <article_dir>
```

## Не делай

- Не придумывай английские заголовки, не смешивай языки.
- Не запускай manifest/prompt/Kie/publish — только cover-text.json + gate.
- Не трогай стиль, hero, scene_hint — это Cover agent.

## Handoff

```text
=== EXCALIBUR BLOG COVER TEXT ===
gate: PASS | BLOCK
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```
