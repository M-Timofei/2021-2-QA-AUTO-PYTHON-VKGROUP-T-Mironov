from cases.ui.pages.base_page import BasePageUI
from cases.ui.locators.locators import RegistrationPageLocators

class RegistrationPage(BasePageUI):

    def create_account(self, username, password,  email, second_password=None,):
        if second_password is None:
            second_password = password
        self.input_data(RegistrationPageLocators.INPUT_USERNAME, username)
        self.input_data(RegistrationPageLocators.INPUT_EMAIL, email)
        self.input_data(RegistrationPageLocators.INPUT_PASSWORD, password)
        self.input_data(RegistrationPageLocators.INPUT_PASSWORD_CONFIRM, second_password)
        self.click(RegistrationPageLocators.CHECKBOX)
        self.click(RegistrationPageLocators.REGISTRATION_BUTTON)

    def error_massage(self):
        return self.find(locator=RegistrationPageLocators.ERROR_MASSAGE, should_be_visible=True).text


