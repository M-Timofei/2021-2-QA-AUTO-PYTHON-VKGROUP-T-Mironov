from ui.pages.base_page import BasePage
from ui.locators import target_locators

# Для нового имени и телефона для каждого теста генирируем новую численную часть
import random
random_number = random.randint(100, 1000)

class ProfilePage(BasePage):
    locators = target_locators.ProfilePageLocators()

    def contact_information_input(self, text, number, locator):
        new_data_input = self.find(locator)
        new_data_input.clear()
        new_data = text+str(number)
        new_data_input.send_keys(new_data)

    def editing_contact_information(self):
        self.wait_spinner()
        self.click(target_locators.ProfilePageLocators.GO_TO_PROFILE_BUTTON_LOCATOR)

        self.contact_information_input('NewName', random_number, self.locators.CHANGE_FIO_LOCATOR)
        self.contact_information_input('+79001002000', random_number, self.locators.CHANGE_PHONE_LOCATOR)

        self.click(target_locators.ProfilePageLocators.SAVE_CHANGES_BUTTON_LOCATOR)
        self.driver.refresh()
        self.wait_spinner()
        assert self.find(self.locators.CHANGE_FIO_LOCATOR).get_attribute('value') == 'NewName'+str(random_number)
        assert self.find(self.locators.CHANGE_PHONE_LOCATOR).get_attribute('value') == '+79001002000'+str(random_number)