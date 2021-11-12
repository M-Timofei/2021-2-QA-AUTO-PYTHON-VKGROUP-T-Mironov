from ui.pages.base_page import BasePage
from ui.pages.search_page import SearchPage
from ui.locators.android_locator import MainPageLocators

class MainPage(BasePage):
    locators = MainPageLocators()

    def skip_windows(self):
        self.click_for_android(self.locators.DENY_BUTTON)
        self.click_for_android(self.locators.DENY_BUTTON)
        return SearchPage(self.driver)