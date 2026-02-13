# Claude Best Practices

Моя личная коллекция скиллов, конфигов и лучших практик для [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview). Автор: [Роман Пуртов](https://roman-purtow.ru)

## Скиллы

| Скилл | Описание |
|-------|----------|
| [building-wireframes](./skills/building-wireframes) | Генерация lo-fi макетов в HTML с Tailwind CSS |
| [cleanup-nul-files](./skills/cleanup-nul-files) | Удаление файлов `nul` из проекта (артефакт Windows) |
| [committing-changes](./skills/committing-changes) | Коммит и пуш с автогенерацией сообщения |
| [find-skills](./skills/find-skills) | Поиск и установка скиллов из экосистемы |
| [frontend-design](./skills/frontend-design) | Production-grade фронтенд с уникальным дизайном |
| [nextjs-app-router-patterns](./skills/nextjs-app-router-patterns) | Паттерны Next.js 14+ App Router с Server Components и streaming |
| [playwright-cli](./skills/playwright-cli) | Автоматизация браузера для тестирования и парсинга |
| [restarting-server](./skills/restarting-server) | Перезапуск dev-сервера с очисткой кэша |
| [skill-creator](./skills/skill-creator) | Руководство по созданию скиллов |
| [tailwind-design-system](./skills/tailwind-design-system) | Дизайн-системы с Tailwind CSS и токенами |
| [tailwind-v4-shadcn](./skills/tailwind-v4-shadcn) | Tailwind v4 + shadcn/ui с CSS-переменными |
| [vercel-react-best-practices](./skills/vercel-react-best-practices) | 57 правил оптимизации React/Next.js от Vercel |

## Конфигурация

В корне репозитория находятся конфигурационные файлы Claude Code:

- **`settings.json`** — настройки: язык общения, канал обновлений, переменные окружения
- **`CLAUDE.md`** — глобальные инструкции: язык, Windows-специфика (`/dev/null` вместо `nul`), автоочистка артефактов, интеграция с Context7 MCP, декомпозиция задач

## Установка

Скиллы устанавливаются по [официальной документации Anthropic](https://docs.anthropic.com/en/docs/claude-code/skills).

## Использование

После установки скиллы вызываются слэш-командами в Claude Code:

```
/building-wireframes — создать wireframe
/committing-changes  — закоммитить изменения
/frontend-design     — сверстать интерфейс
/restarting-server   — перезапустить сервер
```

Или опишите задачу естественным языком:

> «Создай wireframe для лендинга SaaS-продукта»
> «Перезапусти сервер и очисти кэш»
> «Сделай коммит всех текущих изменений»

## Структура скиллов

```
skills/
├── skill-name/
│   ├── SKILL.md           # Определение скилла
│   ├── assets/            # Шаблоны, изображения
│   └── references/        # Дополнительная документация
```

## Лицензия

[MIT](LICENSE)
