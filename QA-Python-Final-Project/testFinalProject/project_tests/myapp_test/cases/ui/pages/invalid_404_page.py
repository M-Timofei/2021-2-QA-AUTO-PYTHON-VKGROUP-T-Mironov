from cases.ui.pages.base_page import BasePageUI
from cases.ui.locators.locators import InvalidPageLocators
import allure

class InvalidPage(BasePageUI):

    @allure.step('Check error massage om 404 page')
    def check_error(self):
        return self.find(InvalidPageLocators.ERROR_MASSAGE).text
