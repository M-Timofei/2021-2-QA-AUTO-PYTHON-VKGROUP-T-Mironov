from ui.pages.base_page import BasePage
from ui.pages.segments_page import SegmentsPage
from ui.pages.campaign_page import CampaignPage
from ui.locators import target_locators
from ui import urls

class DashboardPage(BasePage):
    url = urls.URL_DASHBOARD
    locators = target_locators.DashboardPageLocators()

    def go_to_create_company(self):
        self.wait_spinner()
        try:
            self.click(target_locators.DashboardPageLocators.NEW_COMPANY_LOCATOR_2)
        except:
            self.click(target_locators.DashboardPageLocators.NEW_COMPANY_LOCATOR_1)

        return CampaignPage(self.driver)

    def go_to_create_segment(self):
        self.wait_spinner()
        self.click(target_locators.DashboardPageLocators.AUDIENCE_LOCATOR)

        return SegmentsPage(self.driver)