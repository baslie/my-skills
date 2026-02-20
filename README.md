# Claude Best Practices

Моя личная коллекция скиллов, конфигов и лучших практик для [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview). Автор: [Роман Пуртов](https://roman-purtow.ru)

## Скиллы

| Скилл | Описание |
|-------|----------|
| [building-wireframes](./skills/building-wireframes) | Генерация lo-fi макетов в HTML с Tailwind CSS |
| [changelog-tracker](./skills/changelog-tracker) | Отслеживание обновлений Claude Code с умными дайджестами |
| [cleanup-nul-files](./skills/cleanup-nul-files) | Удаление файлов `nul` из проекта (артефакт Windows) |
| [committing-changes](./skills/committing-changes) | Коммит и пуш с автогенерацией сообщения |
| [restarting-server](./skills/restarting-server) | Перезапуск Node.js dev-сервера с очисткой кэша (Vite, Next.js, Nuxt, Remix и др.) |
| [sorting-bookmarks](./skills/sorting-bookmarks) | Сортировка и категоризация закладок браузера из HTML-файла |
| [ui-ux-pro-max](./skills/ui-ux-pro-max) | Комплексное руководство по дизайну UI/UX (50+ стилей, палитры, шрифты, стеки) |

## Промпты

| Промпт | Описание |
|--------|----------|
| [humanize-ai-text](./prompts/humanize-ai-text.md) | Переписывание текста для обхода ИИ-детекторов (Grammarly, GPTZero, Turnitin) |

## Конфигурация

В директории [`claude-config/`](./claude-config) находятся конфигурационные файлы Claude Code:

- **[`settings.json`](./claude-config/settings.json)** — настройки: язык общения, канал обновлений, переменные окружения
- **[`CLAUDE.md`](./claude-config/CLAUDE.md)** — глобальные инструкции: язык, Windows-специфика (`/dev/null` вместо `nul`), автоочистка артефактов, интеграция с Context7 MCP, декомпозиция задач

## Установка

Скиллы устанавливаются по [официальной документации Anthropic](https://docs.anthropic.com/en/docs/claude-code/skills).

## Использование

После установки скиллы вызываются слэш-командами в Claude Code:

```
/building-wireframes — создать wireframe
/changelog-tracker   — посмотреть обновления Claude Code
/committing-changes  — закоммитить изменения
/restarting-server   — перезапустить сервер
/sorting-bookmarks   — отсортировать закладки браузера
```

Или опишите задачу естественным языком:

> «Создай wireframe для лендинга SaaS-продукта»
> «Что нового в Claude Code?»
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
