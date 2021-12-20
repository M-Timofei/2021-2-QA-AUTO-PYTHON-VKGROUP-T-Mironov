from cases.ui.pages.base_page import BasePageUI
from cases.ui.locators.locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
import allure

class MainPage(BasePageUI):

    @allure.step('Определение username в углу страницы')
    def check_user_login(self):
        elem = self.find(MainPageLocators.LOGGED_AS)
        return elem.text

    @allure.step('Определение vk_id')
    def check_user_id(self):
        try:
            elem = self.find(MainPageLocators.VK_ID, should_be_visible=True, timeout=10)
            return elem.text
        except TimeoutException:
            return 'No vk_id for user'

    @allure.step('Логаут пользователя')
    def logout(self):
        self.click(MainPageLocators.LOGOUT_BUTTON)

    def click_popup(self, button, popup):
        action = ActionChains(self.driver)
        action.move_to_element(self.find(button)).click(self.find(popup)).perform()

    def click_brand(self):
        self.click(MainPageLocators.BRAND_BUTTON)

    def click_home(self):
        self.click(MainPageLocators.HOME_BUTTON)

    def click_python(self):
        self.click(MainPageLocators.PYTHON_BUTTON)

    def click_python_history(self):
        self.click_popup(MainPageLocators.PYTHON_BUTTON, MainPageLocators.PYTHON_HISTORY_BUTTON)

    def click_python_flask(self):
        self.click_popup(MainPageLocators.PYTHON_BUTTON, MainPageLocators.PYTHON_FLASK_LOCATOR)

    def click_linus(self):
        self.click(MainPageLocators.LINUX_BUTTON)

    def click_linus_centos(self):
        self.click_popup(MainPageLocators.LINUX_BUTTON, MainPageLocators.LINUX_BUTTON_CENTOS)

    def click_network(self):
        self.click(MainPageLocators.NETWORK_BUTTON)

    def click_network_news(self):
        self.click_popup(MainPageLocators.NETWORK_BUTTON, MainPageLocators.NETWORK_BUTTON_NEWS)

    def click_network_download(self):
        self.click_popup(MainPageLocators.NETWORK_BUTTON, MainPageLocators.NETWORK_BUTTON_DOWNLOAD)

    def click_network_examples(self):
        self.click_popup(MainPageLocators.NETWORK_BUTTON, MainPageLocators.NETWORK_BUTTON_EXAMPLES)

    def click_future_of_internet(self):
        self.click(MainPageLocators.FUTURE_OF_INTERNET_BUTTON)

    def click_what_is_an_api(self):
        self.click(MainPageLocators.WHAT_IS_AN_API_BUTTON)

    def click_smtp(self):
        self.click(MainPageLocators.SMTP_BUTTON)

    def python_zen(self):
        return self.find(MainPageLocators.PYTHON_ZEN).text