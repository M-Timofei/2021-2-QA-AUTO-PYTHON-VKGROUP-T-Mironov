from ui.pages.base_page import BasePage
from ui.locators import target_locators

class LoginPage(BasePage):

    locators = target_locators.LoginPageLocators

    def log_in(self):
        self.click(target_locators.LoginPageLocators.LOGIN_BUTTON_LOCATOR)

        login_input = self.find(self.locators.LOGIN_LOCATOR)
        login_input.clear()
        login_input.send_keys('mironov.timofei@mail.ru')

        password_input = self.find(self.locators.PASSWORD_LOCATOR)
        password_input.clear()
        password_input.send_keys('MyStrongPassword1')

        self.click(target_locators.LoginPageLocators.INPUT_BUTTON_LOCATOR)