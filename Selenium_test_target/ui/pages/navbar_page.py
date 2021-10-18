from ui.pages.base_page import BasePage
from ui.locators import target_locators
from ui import urls

class NavbarPage(BasePage):

    locators = target_locators.NavbarPageLocators()

    # если в файле теста в параметрах написан неподдержимаемый раздел, выводим соответствующую ошибку
    def go_to_bar(self, bar):
        if bar.lower() == 'статистика':
            self.click(target_locators.NavbarPageLocators.STATISTICS_BUTTON_LOCATOR)
            self.check_url(urls.url_statistics)
        elif bar.lower() == 'инструменты':
            self.click(target_locators.NavbarPageLocators.TOOLS_BUTTON_LOCATOR)
            self.check_url(urls.url_tools)
        else:
            raise RuntimeError (f'Unsupporting bar: {bar}')
