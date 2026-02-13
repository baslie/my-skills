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

## Шаг 3: Проверка зависимостей

Проверь наличие `node_modules`. Если директория отсутствует — установи зависимости:

```bash
[ ! -d "node_modules" ] && <manager> install
```

Замени `<manager>` на определённый в Шаге 2 пакетный менеджер (`npm`, `yarn`, `pnpm`, `bun`).

## Шаг 4: Определить кастомный порт

Перед остановкой процессов проверь конфиги на наличие переопределённого порта:

| Технология | Конфиг | Паттерн для поиска |
|------------|--------|-------------------|
| Vite | `vite.config.*` | `port:` или `server.port` |
| Next.js | `package.json` scripts | `--port` или `-p` флаг |
| Nuxt | `nuxt.config.*` | `port:` в `devServer` |

Если найден кастомный порт — используй его вместо стандартного диапазона. Иначе используй стандартный диапазон из Шага 5.

## Шаг 5: Остановить процессы на диапазоне портов

При занятом порте серверы автоматически берут следующий (3000 → 3001 → 3002). Освобождай весь диапазон:

| Технология | Диапазон портов |
|------------|-----------------|
| Next.js/Nuxt/Remix/CRA | 3000-3010 |
| Vite | 5173-5183 |
| Gatsby | 8000-8010 |
| Parcel | 1234-1244 |

**Определение ОС и остановка процессов (bash):**

```bash
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OSTYPE" == "win32" ]]; then
  # Windows (Git Bash)
  for port in $(seq START END); do
    netstat -ano | grep ":$port " | grep LISTENING | awk '{print $5}' | while read pid; do
      taskkill //PID $pid //F 2>/dev/null
    done
  done
else
  # Unix/Mac
  for port in $(seq START END); do
    lsof -ti:$port | xargs -r kill -9 2>/dev/null
  done
fi
```

Замени `START` и `END` на границы диапазона портов для технологии (или кастомный порт из Шага 4).

**Примечание:** Команды игнорируют ошибки если порты уже свободны (`2>/dev/null`).

## Шаг 6: Очистить кэш

Удали только существующие директории кэша для определённой технологии:

| Технология | Директории для удаления |
|------------|-------------------------|
| Next.js | `.next/` (включая `.next/cache/turbopack` для Turbopack) |
| Nuxt | `.nuxt/`, `.output/` |
| Vite | `node_modules/.vite/` |
| Remix | `.cache/`, `build/` |
| Gatsby | `.cache/`, `public/` |
| Parcel | `.parcel-cache/`, `dist/` |
| CRA | `node_modules/.cache/` |

**Кросс-платформенная очистка (работает в Git Bash и Unix):**

```bash
[ -d "path" ] && rm -rf "path"
```

Замени `path` на директорию кэша. Git Bash на Windows поддерживает `rm -rf`.

## Шаг 7: ORM / Code Generation (если применимо)

Проверь наличие `prisma/schema.prisma` в проекте. Если файл существует:

### 7.1: Сгенерировать Prisma Client

Generated client часто находится в `.gitignore` и требует перегенерации:

```bash
npx prisma generate
```

### 7.2: Применить миграции

```bash
npx prisma migrate dev
```

Если запросит имя миграции — значит есть незакоммиченные изменения схемы. Введи осмысленное имя.

### 7.3: Засеять базу данных (если настроен seed)

Проверь наличие секции `prisma.seed` в `package.json`. Если она есть:

```bash
npx prisma db seed
```

**Примечание:** Если Prisma не используется — пропусти этот шаг полностью.

## Шаг 8: Запустить dev-сервер

1. Прочитай `scripts` из `package.json`
2. Найди dev-скрипт в порядке приоритета: `dev` → `start` → `serve` → `develop`
3. Запусти с определённым в Шаге 2 менеджером:

```bash
<менеджер> <скрипт>
```

Запусти с `run_in_background: true`.

## Шаг 9: Проверить доступность сервера

Подожди 5 секунд и проверь доступность (работает в Git Bash и Unix):

```bash
sleep 5 && curl -s --max-time 5 http://localhost:PORT > /dev/null && echo "Server OK" || echo "Server not responding"
```

Замени `PORT` на:
- Кастомный порт из Шага 4, если найден
- Иначе первый порт из диапазона технологии (3000, 5173, 8000 или 1234)

**Fallback проверка:** Если сервер не отвечает на основном порту — проверь соседние порты из диапазона:

```bash
for port in $(seq START END); do
  curl -s --max-time 2 http://localhost:$port > /dev/null && echo "Server running on port $port" && break
done
```

## Шаг 10: Вывести итоговый отчёт

После всех шагов выведи таблицу со статусом каждого шага:

```
| Шаг | Статус |
|-----|--------|
| Остановка процессов (порты ...) | Done / Skipped |
| Очистка кэша | Done / Skipped |
| ORM / Code Generation | Done / Skipped / N/A |
| Установка зависимостей | Done / Skipped |
| Dev-сервер | Running on :PORT / Failed |

Сервер доступен: http://localhost:PORT
```

Замени PORT на фактический порт, а статусы — на реальные результаты каждого шага.
