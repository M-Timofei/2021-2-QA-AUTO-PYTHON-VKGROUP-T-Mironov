from ui.pages.base_page import BasePage
from ui.locators import target_locators

class LoginPage(BasePage):

    locators = target_locators.LoginPageLocators

    def log_in(self):
        self.click(target_locators.LoginPageLocators.LOGIN_BUTTON_LOCATOR)

        LoginInput = self.find(self.locators.LOGIN_LOCATOR)
        LoginInput.clear()
        LoginInput.send_keys('mironov.timofei@mail.ru')

        PasswordInput = self.find(self.locators.PASSWORD_LOCATOR)
        PasswordInput.clear()
        PasswordInput.send_keys('MyStrongPassword1')

        self.click(target_locators.LoginPageLocators.INPUT_BUTTON_LOCATOR)



