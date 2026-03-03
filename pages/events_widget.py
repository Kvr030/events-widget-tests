from playwright.sync_api import Page, expect


class EventsWidget:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://dev.3snet.info/eventswidget/"
        # Локаторы
        self.dropdown_toggle = page.locator(
            "span.dropdown-toggle:has(span#current-language)"
        )
        self.lang_en = page.locator(
            ".dropdown-menu a[href='https://dev.3snet.info/en/eventswidget/']"
        ).last

    def navigate(self):
        """Переход на страницу"""
        self.page.goto(self.url)

    def switch_to_en(self):
        """Переключение на английский через hover + клик"""
        self.dropdown_toggle.hover()
        self.page.wait_for_timeout(1000)  # Даём время появиться меню
        self.lang_en.click()
        self.page.wait_for_timeout(2000)
