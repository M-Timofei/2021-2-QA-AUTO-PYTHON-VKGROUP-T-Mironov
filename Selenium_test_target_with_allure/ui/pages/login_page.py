import allure
from ui.pages.base_page import BasePage
from ui.locators import target_locators
from selenium.webdriver.support import expected_conditions as EC
from ui import urls

class LoginPage(BasePage):
    url = urls.URL_BASE

    def log_in(self, user, password):
        self.logger.info(f'Loging with {user} and {password}')
        with allure.step(f'Loging with {user} and {password}'):
            self.click(target_locators.LoginPageLocators.LOGIN_BUTTON_LOCATOR)
            self.find(target_locators.LoginPageLocators.LOGIN_LOCATOR).send_keys(user)
            self.find(target_locators.LoginPageLocators.PASSWORD_LOCATOR).send_keys(password)
            self.click(target_locators.LoginPageLocators.INPUT_BUTTON_LOCATOR)

    def check_invalid_password(self):
        self.logger.info('Input valid login and invalid password')
        with allure.step('Input valid login and invalid password'):
            self.log_in('mironov.timofei@mail.ru', 'InvalidPassword')
        self.logger.info('Check error')
        with allure.step('Check error'):
            self.wait().until(EC.url_contains('error_code'))
            elem = self.find(target_locators.LoginPageLocators.INVALID_PASSWORD_LOCATOR)
            assert elem.is_displayed()

    def check_invalid_login(self):
        self.logger.info('Input invalid login and valid password')
        with allure.step('Input invalid login and valid password'):
            self.log_in('invalid.login', 'MyStrongPassword1')
        self.logger.info('Check error')
        with allure.step('Check error'):
            self.wait().until(EC.visibility_of_element_located(target_locators.LoginPageLocators.INVALID_LOGIN_LOCATOR))
            elem = self.find(target_locators.LoginPageLocators.INVALID_LOGIN_LOCATOR)
        assert elem.is_displayed()