from ui.pages.base_page import BasePage
from ui.locators.android_locator import NewsPageLocator
from utils.decorators import wait

class NewsPage(BasePage):
    locators = NewsPageLocator()

    def check_news_mark(self):
        try:
            if self.find(self.locators.ITEM_NEWS).is_displayed():
                return True
        except:
            return False

    def select_news(self):
        self.click_for_android(self.locators.NEWS_FM)
        # ожиданием проверяем, что появилась галочка
        wait(self.check_news_mark, error=AssertionError, timeout=30, check=True)
        self.driver.back()
        self.driver.back()