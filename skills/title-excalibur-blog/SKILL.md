---
name: title-excalibur-blog
description: Invent one catchy human H1 with clear subject. No SEO tails, no label heads.
---

# Title Agent — цепкий заголовок с понятной темой

## Thin conductor + Derouter powerful (HARD)

**Не пиши H1 моделью Cursor.** Собери `--user-file` из research + Scout handoff:

```bash
python3 scripts/excalibur_blog_derouter_opus_chat.py \
  --role title \
  --system-file skills/title-excalibur-blog/SKILL.md \
  --user-file <assembled-title-inputs.md> \
  --output title-brief.json \
  --article-dir <article_dir>
```

`DEROUTER TITLE BLOCKER` → стоп. Контракт: `shared/derouter-opus-brain-contract.md`.

## Вход

- `research-notes.md` текущей темы (включая Wordstat-фразы из Scout/Research)
- `published-titles-only.md` — только чтобы не повторить угол, не образец
- `shared/SOUL.md` + `shared/article-style.md` — голос H1 (коротко, с глаголом)
- `shared/dzen-content-rules.md` — **полный** канон (rules.html + news + РФ DENY)
- `shared/rf-blocked-entities.json` — H1 не про Meta/Instagram/…

## Что такое хороший заголовок

Заголовок — **цепкая первая реплика / кейс** в ритме Klyshin (юрист-сторителлинг),
но факты и город — **Святослав Шакин / Тюмень**. Не копипаст канала Клышина.

- **Case hook:** сцена, противоречие, разговорная первая строка («Расписку написали. Денег не получили» — *свой* вариант, не плагиат).
- **Тема (subject) обязательна** — покупатель понимает риск/объект сделки.
- **Сильный глагол**, активный залог. Не label head («Проверка ЕГРН») и не SEO-хвост.
- **Коротко**, ~50–70 символов. Без «полный гайд», «2026», двоеточие+ключ.
- Энергия примеров (не копировать): «Моего образования хватит»; «В квартире живёт бабушка. Только бабушки нет»; «Автооценка может стоить миллион».

Угол из Scout: `klyshin_hook` в handoff + final P0 Wordstat как **demand spine** (не вставлять в H1; stickers/H2 — из reworked live queries).

## Wordstat (MCP-KV — обязательно для угла)

Из Scout handoff (`wordstat_rework` + `wordstat:` с **mcp_kv live** частотами):

- Final P0 buyer-фразы (не brand «риэлтор тюмень») → demand spine под case-hook H1
- 1–2 живые формулировки для lead / H2 candidates (из reworked cluster)
- Cover-text возьмёт топ для `wordstat_stickers` (1–3 high-frequency из того же pull)

**Не** вставляй сырую SEO-фразу в title. H1 = Klyshin rhythm; Wordstat = spine под ним.

## Выход

`title-brief.json` в article_dir:

```json
{
  "topic_id": "B114",
  "h1": "…",
  "title": "…",
  "subject": "что за тема (имя/инструмент), входит в h1",
  "angle": "почему этот заголовок",
  "verdict": "PASS"
}
```

Один вариант. Не список 5–20.

## Запрещено

- SEO-хвосты: «без копипаста», «за вечер», «полный гайд», «2026»,
  двоеточие с ключом.
- Label heads и голые существительные без действия.
- Игровой заголовок (метафора → суть) и заголовок-«открывашка».
- Прячь тему/имя продукта, если оно и есть тема.
- Кликбейт, оценочные суждения как факт, «СМИ сообщили».
- Клон прошлой серии и копипаст подачи чужого сигнального канала.

## Как думать

1. Выпиши из research тему/имя (OpenAI, Router, Make, …) и конфликт/боль.
2. Собери предложение: тема + сильный глагол + следствие для читателя.
3. Проверь по Дзен-правилам: честно, информативно, без интриги.
4. Сравни с `published-titles-only.md`: похоже — меняй угол.

## Handoff

```text
=== EXCALIBUR BLOG TITLE ===
topic_id:
h1:
incident_report: none | memory/pipeline-fix-queue.md#INC-...
```
