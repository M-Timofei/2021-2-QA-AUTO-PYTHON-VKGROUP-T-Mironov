from ui.pages.base_page import BasePage
from ui.locators.android_locator import AboutPageLocators
from ui.capability import capability_select

class AboutPage(BasePage):
    locators = AboutPageLocators()

    def check_about(self):
        version = self.find(self.locators.VERSION_ID).get_attribute("text").split(' ')[-1]
        capability = capability_select()
        version_from_apk = capability['app'].split('_v')[-1].split('.apk')[0]
        copyright = self.find(self.locators.COPYRIGHT)
        assert version == version_from_apk
        assert copyright.is_displayed()