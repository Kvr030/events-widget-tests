# Events Widget Test Automation

Автоматизированные тесты для страницы [Конструктор календаря мероприятий](https://dev.3snet.info/eventswidget/).

##  Содержание
- [О проекте](#о-проекте)
- [Что тестируется](#что-тестируется)
- [Особенности реализации](#особенности-реализации)
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Запуск в CI/CD](#запуск-в-cicd)
- [Просмотр отчётов](#просмотр-отчётов)
- [Структура проекта](#структура-проекта)

##  О проекте
Тестовое задание на автоматизацию QA. Реализовано на `Python` + `Playwright` + `pytest` с формированием Allure-отчётов и возможностью запуска через GitHub Actions.

##  Что тестируется

| Тест | Описание |
|------|----------|
| `test_page_loads` | Проверка загрузки страницы: title содержит "Конструктор" |
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
- Allure Reports
- GitHub Actions (CI/CD)

##  Установка и запуск

```bash
# Клонируем
git clone https://github.com/Kvr030/events-widget-tests.git
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
pytest --alluredir=allure-results

# Смотрим отчёт локально (требуется Allure CLI)
allure serve allure-results
```

##  Запуск в CI/CD

Тесты можно запускать через GitHub Actions:

1. Перейдите в репозиторий на GitHub
2. Откройте вкладку **Actions**
3. Выберите workflow **"Run Tests with Allure Report"**
4. Нажмите **"Run workflow"** → выберите окружение → **"Run workflow"**

##  Просмотр отчётов

После выполнения тестов Allure-отчёт автоматически публикуется на GitHub Pages:

```
https://kvr030.github.io/events-widget-tests/
```

Отчёт содержит:
-  Графики прохождения тестов
-  Детальные шаги выполнения
-  Вложения (логи, скриншоты)
-  Историю всех запусков

##  Структура проекта

```
.
├── .github/
│   └── workflows/
│       └── run-tests.yml          # CI/CD pipeline
├── pages/
│   └── events_widget.py           # Page Object
├── tests/
│   ├── conftest.py                 # Фикстуры (block_media, events_widget)
│   └── test_events_widget.py       # Тесты
├── allure-results/                  # Сырые данные Allure (игнорируются git)
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

##  Пример результата

```
collected 2 items
tests/test_events_widget.py::test_page_loads PASSED
tests/test_events_widget.py::test_switch_to_english PASSED

=================================== 2 passed in 15.23s ===================================
