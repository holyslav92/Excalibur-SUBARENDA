# WP publish log

## B07 — 2026-09-02

- **topic_id:** B07
- **slug:** snyali-kvartiru-posutochno-v-komnate-17-u-dveri-500-za-obogrevatel
- **title:** Сняли квартиру посуточно. Хотели тепла. У двери: +500 ₽ или спать в куртке
- **post_id:** 4307
- **permalink:** /blog/snyali-kvartiru-posutochno-v-komnate-17-u-dveri-500-za-obogrevatel/
- **categories:** requested posutochnaya-arenda (101), sovety-gostyam (106) — на live WP терминов 101/106 нет, пост остался в «Без рубрики» (id 1), как и все предыдущие посты; см. INC-20260902-1320
- **featured_image:** 4308 (cover 2048×1152, graffiti H1, factory logo top-right)
- **inline_images:** 4309–4311 (3× wp-content/uploads/2026/09/…-inline-0N.png)
- **schema_meta:** ok
- **live-page gate:** PASS
- **cover_qa:** PASS (dobry_dom_gen_only_human_v1, 1 Grsai VIP draw, slice4, logo paste cover only)
- **dzen rss:** /feed/zen/ → 1 enclosure (full cover PNG), format-article/native-yes/evergreen/index, 4 img in content (featured + 3 inline)
- **interlink inbound:** B01 (3745)
- **publish_method:** sftp (FTP_TRANSPORT=sftp FTP_PORT=22 явно)
- **llms_deploy:** PASS (sftp)
- **writing model (owner one-shot override):** Derouter REST `claude-fable-5-1` для всех текстовых ролей (scout/research/title/writer/sol/description/cover-text/cover-scene/schema) через `--one-shot-model`; дефолт tenant-config (Opus 5 / Terra) не менялся
- **words:** 1007 (article.html), 994 live

## B06 — 2026-09-01

- **topic_id:** B06
- **slug:** vyezd-v-12-00-poezd-v-16-30-kuda-det-chemodany-mezhdu
- **title:** Выезд в полдень. Поезд через 4 часа — чемоданы у подъезда
- **post_id:** 4283
- **permalink:** /blog/vyezd-v-12-00-poezd-v-16-30-kuda-det-chemodany-mezhdu/
- **categories:** posutochnaya-arenda (101), sovety-gostyam (106)
- **featured_image:** 4284
- **inline_images:** 4285–4292 (8× wp-content/uploads/2026/09/…)
- **schema_meta:** ok
- **live-page gate:** PASS (9/9 img src → wp-content)
- **cover_qa:** BLOCK (paste_and_ship_on_exhaust — shipped like B05)
- **dzen cache bust:** cover-dzen-v3 + cover-dzen-v3-1024x576 uploaded; feed enclosure → …-cover-dzen-v3.png
- **interlink inbound:** B01 (3745)
- **publish_method:** sftp (FTP PASV data timeout on cloud; SFTP:22 OK)
- **llms_deploy:** FAIL (SFTP upload empty error — post live OK)

## B05 — 2026-09-01

- **topic_id:** B05
- **slug:** rejting-4-8-u-kvartiry-posutochno-dva-otzyva-odno-i-to-zhe-vse-super
- **title:** Рейтинг 4,8. Два «всё супер» — и 3 900 ₽ под вопросом
- **post_id:** 4262
- **permalink:** /blog/rejting-4-8-u-kvartiry-posutochno-dva-otzyva-odno-i-to-zhe-vse-super/
- **categories:** posutochnaya-arenda (101), sovety-gostyam (106)
- **featured_image:** 4263
- **inline_images:** 4264–4270 (7× wp-content/uploads/2026/09/…-inline-0N.png)
- **schema_meta:** ok
- **live-page gate:** PASS
- **dzen cache bust:** cover-dzen-v3 + cover-dzen-v3-1024x576 uploaded; feed enclosure → …-cover-dzen-v3.png
- **interlink inbound:** B01 (3745)
- **publish_method:** sftp (FTP PASV data channel timeout on cloud; SFTP:22 OK)

## B03 — 2026-08-28

- **topic_id:** B03
- **slug:** kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki
- **title:** Привезли сына к вузу — «рядом» оказалось 40 минут пешком
- **post_id:** 4108
- **permalink:** /blog/kvartiry-posutochno-v-tyumeni-k-1-sentyabrya-ryadom-s-vuzom-tri-ostanovki/
- **category:** posutochnaya-arenda (101)
- **featured_image:** 4109
- **inline_images:** 4110–4116 (7× wp-content/uploads/2026/08/…-inline-0N.png)
- **schema_meta:** ok
- **live-page gate:** PASS
- **interlink inbound:** B01 (3745), B02 (3777)
- **publish_method:** ftp (Timeweb PASV)
