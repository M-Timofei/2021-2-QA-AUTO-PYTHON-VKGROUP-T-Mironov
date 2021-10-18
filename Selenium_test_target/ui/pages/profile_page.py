from ui.pages.base_page import BasePage
from ui.locators import target_locators

# Для нового имени и телефона для каждого теста генирируем новую численную часть
import random
RandomNumber = random.randint(100, 1000)

class ProfilePage(BasePage):
    locators = target_locators.ProfilePageLocators()

    def editing_contact_information(self):
        self.click(target_locators.ProfilePageLocators.GO_TO_PROFILE_BUTTON_LOCATOR)

        NewNameInput = self.find(self.locators.CHANGE_FIO_LOCATOR)
        NewNameInput.clear()
        NewName = 'NewName'+str(RandomNumber)
        NewNameInput.send_keys(NewName)

        NewPhoneInput = self.find(self.locators.CHANGE_PHONE_LOCATOR)
        NewPhoneInput.clear()
        NewPhone = '+79001002000'+str(RandomNumber)
        NewPhoneInput.send_keys(NewPhone)

        self.click(target_locators.ProfilePageLocators.SAVE_CHANGES_BUTTON_LOCATOR)
        self.driver.refresh()

        assert self.find(self.locators.CHANGE_FIO_LOCATOR).get_attribute('value') == 'NewName'+str(RandomNumber)\
                and self.find(self.locators.CHANGE_PHONE_LOCATOR).get_attribute('value') == '+79001002000'+str(RandomNumber)