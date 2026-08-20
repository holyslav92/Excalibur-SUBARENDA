# Создание репозитория Excalibur-SUBARENDA

Cloud Agent **не имеет прав** `createRepository` для аккаунта `holyslav92`.
Адаптированная копия живёт на ветке `excalibur-subarenda-copy` в Excalibur-2-Cloud
до переноса.

## Шаги для holyslav92

```bash
gh repo create holyslav92/Excalibur-SUBARENDA --public \
  --description "Excalibur content factory for Добрый дом (посуточная аренда / субаренда, Тюмень)"

git clone https://github.com/holyslav92/Excalibur-2-Cloud.git /tmp/excalibur-src
cd /tmp/excalibur-src
git fetch origin excalibur-subarenda-copy
git checkout excalibur-subarenda-copy

git clone https://github.com/holyslav92/Excalibur-SUBARENDA.git /tmp/excalibur-sub
cd /tmp/excalibur-sub
git checkout -b main 2>/dev/null || true
rsync -a --exclude .git /tmp/excalibur-src/ /tmp/excalibur-sub/
git add -A
git commit -m "Initial import: Excalibur-SUBARENDA for Добрый дом"
git push -u origin main
```

## Не мерджить

Ветку `excalibur-subarenda-copy` **не** мерджить в `main` Excalibur-2-Cloud (The Риэлтор).

## После push

1. Cursor Cloud Environment → репозиторий **Excalibur-SUBARENDA**
2. Secrets: `PUBLIC_SITE_URL`, WP/SFTP для добрыйдом-72.рф
3. 4× Automation YEKT — см. `CLOUD-AUTOMATION.md`
4. Заменить `memory/cover/assets/identity-real/` (NEED_REPLACE)
