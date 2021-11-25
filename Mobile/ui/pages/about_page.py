from ui.pages.base_page import BasePage
from ui.locators.android_locator import AboutPageLocators

class AboutPage(BasePage):
    locators = AboutPageLocators()

    def check_about(self):
        version_from_display = self.find(self.locators.VERSION_ID).get_attribute("text").split(' ')[-1]
        copyright = self.find(self.locators.COPYRIGHT)
        assert version_from_display == self.config['global_version']
        assert copyright.is_displayed()