---
name: sorting-bookmarks
description: >
  Sort and categorize browser bookmarks from an HTML bookmarks file.
  Parses bookmarks, crawls URLs for content analysis, categorizes by topic,
  and generates a sorted HTML file for browser import.
  Triggers: sort bookmarks, categorize bookmarks, reorganize bookmarks,
  отсортируй закладки, категоризация закладок, разобрать закладки,
  organize bookmarks folder, HTML bookmarks file
---

# Sorting Bookmarks Skill

Автоматическая сортировка и категоризация закладок браузера из HTML-файла.

## Зависимости

- Python 3.10+
- crawl4ai (`pip install crawl4ai`)

## Воркфлоу

### 1. Получить файл закладок

Запроси у пользователя путь к HTML-файлу экспорта закладок (формат NETSCAPE-Bookmark-file-1), либо найди его автоматически через Glob (`*.html` в рабочей директории).

### 2. Обнаружение папок и выбор

Запусти скрипт для получения списка верхнеуровневых папок:

```bash
python <skill_dir>/scripts/list_folders.py \
  --file "<path_to_bookmarks.html>"
```

Скрипт выводит JSON со всеми папками верхнего уровня (depth=2), включая:
- `name` — название папки
- `bookmarks_count` — общее количество закладок (включая подпапки)
- `subfolders_count` — количество подпапок

Предложи пользователю выбрать папку для сортировки через `AskUserQuestion`. Покажи **все** найденные папки (до 4 самых крупных как опции, остальные пользователь может ввести вручную). В описании каждой опции укажи количество закладок и подпапок.

### 3. Парсинг и краулинг

Запусти скрипт для извлечения закладок из указанной папки и краулинга каждого URL:

```bash
python <skill_dir>/scripts/parse_and_crawl.py \
  --file "<path_to_bookmarks.html>" \
  --folder "<folder_name>" \
  --output bookmarks_analysis.json
```

Скрипт:
- Парсит HTML и извлекает все ссылки из указанной папки
- Дедуплицирует URL
- Краулит каждый URL батчами по 5 через crawl4ai
- Сохраняет результаты в JSON

**ВАЖНО:** Скрипт использует ручные батчи через `arun_many()`. НЕ используй `MemoryAdaptiveDispatcher` из crawl4ai — он содержит баг и возвращает результаты только первого батча.

### 4. Анализ результатов краулинга

Прочитай полученный `bookmarks_analysis.json`. Для каждой закладки доступны:
- `url` — адрес страницы
- `original_title` — заголовок из файла закладок
- `crawled_title` — заголовок, полученный при краулинге
- `description` — первые 300 символов контента страницы
- `success` — успешен ли краулинг
- `folder` — исходная подпапка

### 5. Категоризация

Используя руководство из `<skill_dir>/references/categorization-guide.md`:

1. Проанализируй каждую ссылку по `crawled_title` + `description`
2. Определи тематические категории
3. Распредели все URL по категориям
4. Создай файл `categories_mapping.json`:

```json
{
  "categories": {
    "Название категории": ["url1", "url2", ...],
    ...
  }
}
```

**Правила:**
- Каждый URL должен быть ровно в одной категории
- Оптимальный размер категории: 3-15 ссылок
- Если >20 — разбить на подкатегории
- Если <3 — объединить с родственной

### 6. Генерация HTML

Запусти скрипт для генерации итогового файла:

```bash
python <skill_dir>/scripts/generate_bookmarks.py \
  --analysis bookmarks_analysis.json \
  --mapping categories_mapping.json \
  --output bookmarks_sorted.html \
  --root-folder "<folder_name>"
```

Скрипт:
- Создаёт HTML в формате NETSCAPE-Bookmark-file-1 (импортируется в любой браузер)
- Сортирует папки и ссылки по алфавиту
- Валидирует: все URL из анализа присутствуют в маппинге

### 7. Валидация

Проверь результат:
- Все ссылки из анализа попали в итоговый HTML
- Нет дубликатов
- Формат корректен для импорта в браузер
- Категории логичны и сбалансированы по размеру

Предложи пользователю проверить файл и при необходимости скорректировать категории.

### 8. Очистка временных файлов

После завершения всех шагов (включая возможные корректировки от пользователя) удали временные файлы:

```bash
rm -f bookmarks_analysis.json categories_mapping.json
```

## Совместимость

### Windows
- Все скрипты используют `sys.stdout.reconfigure(encoding="utf-8")` для корректной работы с кириллицей
- В bash-командах используй `/dev/null`, НЕ `nul`

### Формат закладок
- Вход: HTML-файл экспорта закладок (Chrome, Firefox, Edge — все используют NETSCAPE-Bookmark-file-1)
- Выход: HTML-файл в том же формате, пригодный для импорта обратно в браузер
