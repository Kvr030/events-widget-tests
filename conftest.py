import pytest
from playwright.sync_api import Page, Route
from pages.events_widget import EventsWidget


@pytest.fixture(autouse=True)
def block_media(page: Page):
    """Блокирует медиафайлы для всех тестов автоматически"""

    def handle_route(route: Route):
        if route.request.resource_type in ["image", "media", "video", "audio"]:
            route.abort()
        else:
            route.continue_()

    page.route("**/*", handle_route)
    yield


@pytest.fixture
def events_widget(page: Page) -> EventsWidget:
    """Фикстура для работы с виджетом событий"""
    return EventsWidget(page)
