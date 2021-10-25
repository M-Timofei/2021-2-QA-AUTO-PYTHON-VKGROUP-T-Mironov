from ui.pages.base_page import BasePage
from ui.locators import target_locators

class DashboardPage(BasePage):

    locators = target_locators.DashboardPageLocators()

    def log_out(self):
        self.wait_spinner()
        self.click(target_locators.DashboardPageLocators.ACCOUNT_BUTTON_LOCATOR)
        self.click(target_locators.DashboardPageLocators.OUTPUT_BUTTON_LOCATOR)