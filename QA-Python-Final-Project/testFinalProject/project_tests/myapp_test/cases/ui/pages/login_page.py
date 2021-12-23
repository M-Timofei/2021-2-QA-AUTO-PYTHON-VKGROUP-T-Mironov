from cases.ui.pages.base_page import BasePageUI
from cases.ui.locators.locators import LoginPageLocators
from cases.ui.pages.invalid_404_page import InvalidPage
from cases.ui.pages.registration_page import RegistrationPage
from cases import urls

class LoginPage(BasePageUI):

    def go_to_registration(self):
        self.click(LoginPageLocators.CREATE_ACCOUNT_BUTTON)
        return RegistrationPage(self.driver)

    def authorization(self, username, password):
        self.input_data(LoginPageLocators.INPUT_USERNAME, username)
        self.input_data(LoginPageLocators.INPUT_PASSWORD, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def error_massage(self):
        return self.find(locator=LoginPageLocators.ERROR_MASSAGE, should_be_visible=True).text

    def go_to_invalid_page(self):
        self.driver.get(urls.INVALID_PAGE)
        return InvalidPage(self.driver)