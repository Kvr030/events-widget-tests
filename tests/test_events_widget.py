import pytest
from playwright.sync_api import expect

from pages.events_widget import EventsWidget


def test_page_loads(events_widget):
    """Проверка что страница открывается и title содержит 'Конструктор'"""
    events_widget.navigate()
    title = events_widget.page.title()
    assert "Конструктор" in title, f"Title не содержит 'Конструктор': {title}"


def test_switch_to_english(events_widget):
    events_widget.navigate()
    events_widget.switch_to_en()
    """Проверяем что в URL появился en (началась смена языка)"""
    assert "/en/" in events_widget.page.url
