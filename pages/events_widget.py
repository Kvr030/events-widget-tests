import allure
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
        """Открыть страницу"""
        with allure.step("Открыть страницу Events Widget"):
            self.page.goto(self.url)
        return self

    def switch_to_en(self):
        """Переключение на английский через hover + клик"""
        with allure.step("Навести курсор на дропдаун языка"):
            self.dropdown_toggle.hover()

        with allure.step("Кликнуть по английскому языку"):
            self.lang_en.click()

        with allure.step("Подождать загрузки страницы после смены языка"):
            self.page.wait_for_load_state("networkidle")
