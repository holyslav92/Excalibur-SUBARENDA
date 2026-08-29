# Description inputs B04

topic_id: B04
tenant: Добрый дом (ПКОМПАНИИ), Тюмень, посуточная аренда
author_brand: Добрый дом
season_context: август 2026, вечерняя спешка перед заездом утром; гость переводит предоплату «чтобы не упустить»

Read: shared/dzen-description-rules.md (HARD constraints)

Output ONLY valid description-brief.json (JSON object, no markdown wrapper, no commentary).

## Title (H1) — description MUST NOT duplicate or paraphrase closely

«Перевёл предоплату за квартиру посуточно. Утром её уже сдали»

## Article opening (DO NOT truncate — double card FAIL)

First two paragraphs start with: «28 августа, 22:15. Гость едет в Тюмень утренним поездом…» and «А теперь тот же вечер — 22:15, та же спешка, а утром та же фраза: «Извините, уже сдали»…» — description must use DIFFERENT hook wording (not «28 августа», not «перевёл предоплату» as opening clone of H1).

## Article spine (for teaser energy, not spoiler checklist)

- Evening rush: «есть ещё трое желающих, держу до полуночи» — link in chat, card charged, picture «бронь подтверждена»
- Morning 08:40 at the door: other people live inside, ad deleted, phone silent — OR same phrase but paid on platform, real host, calendar desync on another service
- One morning phrase «уже сдали» → two routes: police (paid off-platform / fake link) vs platform support (real booking conflict)
- Lockpick from article: confirmation in personal account vs screenshot in messenger only
- Six-hour free cancellation window on Avito — easy to sleep through if paid at 22:15, problem at 08:40
- «Transfer to card for discount» = red flag; not the same as double booking with real owner
- Tyumen context in article but teaser need not stuff city name

## Research / Wordstat angle (background, not SEO paste)

- P0 spine: «аренда квартиры посуточно» 794 (Tyumen)
- Fear cluster: предоплата, бронь, «уже занято», отмена
- Klyshin hook family: cancel_prepay — evening action, morning break

## OG / description factory (HARD)

1. NEVER guest-burn price arithmetic (2500→6500) as Добрый дом's own price; one sum as hook OK, no price ladder
2. NEVER Святослав Шакин / The Риэлтор / «история Святослава»
3. ≠ title H1 above (no «перевёл предоплату… утром уже сдали» paraphrase)
4. ≠ truncated lead / opening scene (28 августа, 22:15, поезд в Тюмень…)
5. No label head («Проверка заселения», «Риэлтор Тюмень»)
6. No full TG/MAX/booking funnel — one hook only
7. Guest pain only — no ЕГРН/наследство/ипотека as spine
8. 1–2 sentences, ~120–220 chars (max 250, min 40)
9. Klyshin rhythm: case hook, разговорная первая реплика, интрига до клика

## Required JSON fields

topic_id, description, rhythm ("klyshin_case_hook"), geo ("Тюмень"), author_brand ("Добрый дом"), not_equal_title (true), not_truncated_lead (true), verdict ("PASS")

## Energy examples (do NOT copy verbatim)

| Title | OK teaser |
|-------|-----------|
| Код есть — из крана льёт холодное | Хост пишет «утром будет». Вы уже в квартире. Где бойлер — спросите до того, как замёрзнете. |
| В чате «можно с собакой» — у двери «не пустим» | «Можно» без породы и доплаты — не ответ. Один вопрос в переписке спасает заселение. |

For B04 energy: «держу до полуночи» / картинка «бронь подтверждена» vs запись в личном кабинете; «уже сдали» утром — мошенник или календарь; but NOT repeat H1 verbatim.
