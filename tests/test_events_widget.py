import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Загрузка страницы")
@allure.story("Проверка базовой функциональности")
def test_page_loads(events_widget):
    """
    Тест 1: Проверка загрузки страницы
    """
    events_widget.navigate()

    expect(events_widget.page).to_have_title(
        "Конструктор календаря мероприятий - 3Snet"
    )

    title = events_widget.page.title()
    allure.attach(
        f"Title страницы: {title}",
        name="Информация о заголовке",
        attachment_type=allure.attachment_type.TEXT,
    )


@allure.feature("Переключение языка")
@allure.story("Интернационализация")
@allure.severity(allure.severity_level.CRITICAL)
def test_switch_to_english(events_widget):
    """
    Тест 2: Переключение языка на английский
    """
    events_widget.navigate()
    events_widget.switch_to_en()

    expect(events_widget.page).to_have_url("https://dev.3snet.info/en/eventswidget/")

    final_url = events_widget.page.url
    allure.attach(
        f"URL после переключения: {final_url}",
        name="URL после переключения",
        attachment_type=allure.attachment_type.TEXT,
    )
