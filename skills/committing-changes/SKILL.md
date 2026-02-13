---
name: committing-changes
description: Коммитит и пушит все изменения в проекте с автоматически сгенерированным релевантным commit message. Используй когда нужно закоммитить и запушить текущие изменения.
allowed-tools: Bash(git *)
---

# Committing Changes

Коммитит все текущие изменения и пушит в remote-репозиторий.

## Шаг 1: Посмотреть статус и diff

Выполни параллельно:

```bash
git status
```

```bash
git diff --staged --stat && git diff --stat
```

```bash
git log --oneline -5
```

Если изменений нет (нет untracked, modified, staged файлов) — сообщи пользователю что коммитить нечего и заверши.

## Шаг 2: Добавить файлы в staging

Добавь все изменённые и новые файлы:

```bash
git add -A
```

**ВАЖНО:** Перед добавлением проверь что в списке нет:
- `.env`, `.env.local`, `.env.production` — файлы с секретами
- `credentials.json`, `*.pem`, `*.key` — ключи и сертификаты
- Больших бинарных файлов (>10 MB)

Если такие файлы обнаружены — **предупреди пользователя** и исключи их из staging.

## Шаг 3: Сгенерировать commit message

Посмотри diff staged-изменений:

```bash
git diff --staged
```

На основе diff сгенерируй **краткий и релевантный** commit message на английском:

- Формат: `<type>: <short description>`
- Типы: `feat`, `fix`, `refactor`, `style`, `docs`, `chore`, `test`, `perf`
- Описание — 1 строка, до 72 символов, по сути изменений (что и зачем)
- Если изменений много — добавь тело (body) через пустую строку с перечислением ключевых изменений

Примеры:
- `feat: add portfolio filtering by category`
- `fix: resolve broken image fallback on project pages`
- `chore: update dependencies and clean up cache files`

## Шаг 4: Создать коммит

```bash
git commit -m "$(cat <<'EOF'
<сгенерированный commit message>
EOF
)"
```

## Шаг 5: Запушить в remote

```bash
git push
```

Если remote не настроен или push отклонён — сообщи пользователю об ошибке.

## Шаг 6: Вывести итог

После завершения выведи:

```
| Действие | Результат |
|----------|-----------|
| Файлов изменено | N |
| Commit message | <message> |
| Ветка | <branch> |
| Push | Done / Failed |
```
