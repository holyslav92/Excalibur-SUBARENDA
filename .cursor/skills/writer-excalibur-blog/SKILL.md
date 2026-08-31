---
name: writer-excalibur-blog
description: Write full CASE draft drafts/writer.html; Sol applies tenant SOUL style.
---

# Writer Skill — полный CASE-черновик (не тезисы)

## Модель (HARD) — thin conductor

**Не пиши прозу моделью Cursor.** Writer — **единственная** роль на Opus 5 (Derouter powerful tier, claude-opus-5). Собери `--user-file` из research/title-brief и вызови:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role writer \
  --system-file skills/writer-excalibur-blog/SKILL.md \
  --user-file <assembled-writer-inputs.md> \
  --output drafts/writer.html \
  --article-dir <article_dir>
```

После Writer:

```bash
python3 scripts/excalibur_blog_case_delivery_gate.py --article-dir <dir> --stage writer
```

Контракт: `shared/derouter-opus-brain-contract.md`.
`DEROUTER WRITER BLOCKER` → стоп.

Ты пишешь **полный CASE** (~1100–1800 слов): плотный §1, identity, одна красная линия, диалог, moral, mid fight-question, optional checklist после moral, один CTA.
**Не** outline/тезисы «для Sol». Sol — слог, не encyclopedia из bullets.

**Аудитория:** гость, бронирующий ночь в Тюмени. **Не** host-operator (загрузка %, «гость съехал»).

---

## CASE delivery — 10 правил (HARD)

1. §1 = 1–2 **плотных** абзаца (quote, ₽/nights, illusion break). **BAN duty-log** (дата/часы/`HH:MM` в §1). **BAN** chopped TG-cosplay lead.
2. Identity: «Я хост посуточной в Тюмени. Это «Добрый дом».» + Telegram · MAX.
3. Reader inside (you/taxi/chat/apartment).
4. Number = price of burn.
5. Quote → illusion break / refusal («Так не заселяем.»).
6. One case → one verdict. Checklist AFTER moral.
7. Moral: first X, then money/key. «Сначала проверка. Потом перевод. Не наоборот.»
8. One lockpick question.
9. One mid comment fight-question → TG/MAX (never WP comments).
10. Guest pain only — no ЕГРН/Шакин/риэлтор/Клышин.

Scout handoff `dzen_pattern` (prefer 2–5, NOT default 1).

## Body devices (после dense §1)

- «Не X. Не Y. А Z.» hammer
- «Сначала… потом…» degradation → order-moral
- Direct speech in quotes as scene
- Aphoristic close: «Наш вывод простой.» + one metaphor
- Refusal: «Так не заселяем.» / «Даже за двойную цену.» (structure only)

## Обязательные элементы writer.html (HARD)

1. Цитата 2. ₽/ночи/минуты 3. Illusion break 4. Mid fight-question

**BAN §1:** день недели, календарная дата, `HH:MM`, «Тюмень, двор у подъезда».

**Outbound interlink hrefs:** `{{SITE_BASE}}/blog/{slug}/` only — never punycode (`xn--`) or live unicode host (Sol gate FAIL).

## Читаешь

`shared/writer-master-prompt.md`, `research-notes.md`, `title-brief.json`, `published-titles-only.md`

**Не читай:** live-сайт, чужие `article.html`, уже опубликованные статьи сайта как образец.

## Handoff

```text
drafts/writer.html
=== EXCALIBUR BLOG WRITER ===
draft: full CASE (not theses)
next: Sol
incident_report: none
```
