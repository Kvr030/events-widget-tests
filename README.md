# Events Widget Test Automation

Автоматизированные тесты для страницы [Конструктор календаря мероприятий](https://dev.3snet.info/eventswidget/).

##  Содержание
- [О проекте](#о-проекте)
- [Что тестируется](#что-тестируется)
- [Особенности реализации](#особенности-реализации)
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Структура проекта](#структура-проекта)
- [Результаты](#результаты)

##  О проекте
Тестовое задание на автоматизацию QA. Реализовано на `Python` + `Playwright` + `pytest`.

##  Что тестируется
| Тест | Описание |
|------|----------|
| `test_page_loads` | Проверка загрузки страницы: title содержит "Конструктор", дропдаун виден |
| `test_switch_to_english` | Переключение языка на английский через hover-меню, проверка `/en/` в URL |

##  Особенности реализации
В процессе тестирования выявлены особенности страницы:
- **Два одинаковых меню** — десктопное и мобильное, видимое — последнее в DOM
- **Hover вместо click** — меню открывается только по наведению
- **Дубли ссылок** — локатор уточнён до `.dropdown-menu a[href*='/en/']` + `.last`
- **Медиафайлы** — заблокированы через `page.route()` для ускорения тестов

##  Технологии
- Python 3.13
- Playwright
- Pytest
- pytest-html (отчёты)

##  Установка и запуск

```bash
# Клонируем
git clone https://github.com/yourusername/events-widget-tests.git
cd events-widget-tests

# Создаём виртуальное окружение (рекомендуется)
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Ставим зависимости
pip install -r requirements.txt

# Устанавливаем браузеры Playwright
playwright install chromium

# Запускаем тесты
pytest
```

После запуска отчёт будет доступен: `reports/test_report.html`

##  Структура проекта
```
.
├── pages/
│   └── events_widget.py          # Page Object
├── tests/
│   ├── conftest.py                # Фикстуры (block_media, events_widget)
│   └── test_events_widget.py      # Тесты
├── reports/                        # HTML-отчёты (игнорируются git)
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

##  Результаты
Пример успешного запуска:
```
collected 2 items
tests/test_events_widget.py::test_page_loads PASSED
tests/test_events_widget.py::test_switch_to_english PASSED

=================================== 2 passed in 15.23s ===================================
```