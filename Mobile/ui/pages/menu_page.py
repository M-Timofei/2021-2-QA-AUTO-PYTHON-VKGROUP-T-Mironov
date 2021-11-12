from ui.pages.base_page import BasePage
from ui.locators.android_locator import MenuPageLocators
from ui.pages.news_page import NewsPage
from ui.pages.about_page import AboutPage

class MenuPage(BasePage):
    locators = MenuPageLocators()

    def go_to_news(self):
        self.swipe_up_to_element(self.locators.NEWS, 5)
        self.click_for_android(self.locators.NEWS)
        return NewsPage(self.driver)

    def go_to_about(self):
        self.swipe_up_to_element(self.locators.ABOUT_BUTTON, 5)
        self.click_for_android(self.locators.ABOUT_BUTTON)
        return AboutPage(self.driver)