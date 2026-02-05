---
name: restarting-server
description: Перезапускает Node.js dev-сервер с очисткой кэша. Автоматически определяет технологию (Vite, Next.js, Nuxt, Remix, CRA, Gatsby, Parcel) и очищает соответствующие кэши. Используй когда сервер завис, не отвечает, HMR не работает, или нужна полная перезагрузка.
disable-model-invocation: true
allowed-tools: Bash(*), Glob, Read
---

# Restart Dev Server

Универсальный перезапуск Node.js dev-сервера с очисткой кэша.

## Шаг 1: Определить технологию

Проверь наличие файлов/директорий для определения стека:

| Признак | Технология |
|---------|------------|
| `next.config.*` или `.next/` | Next.js |
| `nuxt.config.*` или `.nuxt/` | Nuxt |
| `vite.config.*` или `node_modules/.vite/` | Vite |
| `remix.config.*` или `.cache/` + `build/server/` | Remix |
| `gatsby-config.*` или `.cache/` + `public/` | Gatsby |
| `.parcel-cache/` | Parcel |
| `react-scripts` в package.json | Create React App |

## Шаг 2: Определить пакетный менеджер

Проверь наличие lock-файла в корне проекта:

| Lock-файл | Менеджер | Команда запуска |
|-----------|----------|-----------------|
| `pnpm-lock.yaml` | pnpm | `pnpm run` |
| `yarn.lock` | yarn | `yarn` |
| `bun.lockb` | bun | `bun run` |
| `package-lock.json` или отсутствует | npm | `npm run` |

## Шаг 3: Остановить процессы на диапазоне портов

При занятом порте серверы автоматически берут следующий (3000 → 3001 → 3002). Освобождай весь диапазон:

| Технология | Диапазон портов |
|------------|-----------------|
| Next.js/Nuxt/Remix/CRA | 3000-3010 |
| Vite | 5173-5183 |
| Gatsby | 8000-8010 |
| Parcel | 1234-1244 |

**Windows:**
```bash
for /L %p in (3000,1,3010) do @(for /f "tokens=5" %a in ('netstat -ano ^| findstr :%p ^| findstr LISTENING') do taskkill /PID %a /F 2>nul)
```

**Unix/Mac:**
```bash
for port in $(seq 3000 3010); do lsof -ti:$port | xargs -r kill -9 2>/dev/null; done
```

**Примечание:** Команды игнорируют ошибки если порты уже свободны (`2>nul` / `2>/dev/null`).

## Шаг 4: Очистить кэш

Удали только существующие директории кэша для определённой технологии:

| Технология | Команда очистки |
|------------|-----------------|
| Next.js | `rm -rf .next/` (включая `.next/cache/turbopack` для Turbopack) |
| Nuxt | `rm -rf .nuxt/ .output/` |
| Vite | `rm -rf node_modules/.vite/` |
| Remix | `rm -rf .cache/ build/` |
| Gatsby | `rm -rf .cache/ public/` |
| Parcel | `rm -rf .parcel-cache/ dist/` |
| CRA | `rm -rf node_modules/.cache/` |

**Важно:** Перед удалением проверь существование директории через `ls` или `test -d`.

## Шаг 5: Запустить dev-сервер

1. Прочитай `scripts` из `package.json`
2. Найди dev-скрипт в порядке приоритета: `dev` → `start` → `serve` → `develop`
3. Запусти с определённым в Шаге 2 менеджером:

```bash
<менеджер> <скрипт>
```

Запусти с `run_in_background: true`.

## Шаг 6: Проверить доступность сервера

Подожди 5 секунд и проверь доступность:

**Windows:**
```bash
powershell -Command "Start-Sleep -Seconds 5; try { Invoke-WebRequest -Uri http://localhost:PORT -UseBasicParsing -TimeoutSec 5 | Out-Null; Write-Host 'Server OK' } catch { Write-Host 'Server not responding' }"
```

**Unix/Mac:**
```bash
sleep 5 && curl -s --max-time 5 http://localhost:PORT > /dev/null && echo "Server OK" || echo "Server not responding"
```

Замени `PORT` на первый порт из диапазона технологии (3000, 5173, 8000 или 1234).
