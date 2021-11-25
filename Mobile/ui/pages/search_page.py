from ui.pages.base_page import BasePage
from ui.pages.menu_page import MenuPage
from ui.locators.android_locator import SearchPageLocators
from utils.decorators import wait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage(BasePage):
    locators = SearchPageLocators()

    def input_text(self, text, locator = locators.KEYBOARD):
        self.click_for_android(locator)
        self.find(self.locators.INPUT_TEXT_LOCATOR).send_keys(text)
        self.click_for_android(self.locators.ENTER_SEARCH_BUTTON)
        self.driver.hide_keyboard()

    def go_to_menu_page(self):
        self.click_for_android(self.locators.MENU_BUTTON)
        return MenuPage(self.driver, self.config)

    def check_article_on_display(self):
        try:
            try:
                self.input_text('Russia')
            except:
                self.input_text('Russia', locator=self.locators.KEYBOARD_2)
            self.wait(timeout=5).until(EC.element_to_be_clickable(self.locators.TEXT_IN_ARTICLE))
            text_in_article = self.find_everything(self.locators.TEXT_IN_ARTICLE)[0].get_attribute("text")
            if 'государство' in text_in_article:
                return True
            else:
                return False
        except:
            return False

    def wait_result_on_display(self, locator, text):
        try:
            if text in self.find_everything(locator)[-1].get_attribute("text"):
                return True
        except:
            return False

    def check_population(self):
        # вводим Russia и дожидаемся, когда статья появится на странице
        wait(self.check_article_on_display, error=AssertionError, timeout=30, check=True)
        self.swipe_left_to_element(self.locators.LOW_PANEL, self.locators.POPULATION_LOCATOR, 5)
        self.click_for_android(self.locators.POPULATION_LOCATOR)
        # ждем, когда ответ появится на экране
        wait(self.wait_result_on_display, error=AssertionError, timeout=30, check=True, locator=self.locators.CARD_TITLE, text = 'млн')
        total_population = self.find(self.locators.CARD_TITLE).get_attribute("text")
        assert total_population == '146 млн.'

    def check_calculator_result(self):
        self.input_text('3+2')
        # ждем, когда ответ появится на экране
        wait(self.wait_result_on_display, error=AssertionError, timeout=30, check=True, locator = self.locators.RESULT_LOCATOR, text = '5')
        result = self.find_everything(self.locators.RESULT_LOCATOR)[-1].get_attribute("text")
        assert result == '5'

    def check_news(self):
        self.input_text('news')
        name_of_news = self.find(self.locators.RADIO_NAME).get_attribute("text")
        assert name_of_news == "Вести ФМ"