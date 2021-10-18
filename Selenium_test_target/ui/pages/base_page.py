from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators import target_locators

CLICK_RETRY = 3

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout = None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator):
        return self.wait().until(EC.presence_of_element_located(locator))

    def click(self, locator):
        for i in range(CLICK_RETRY):
            try:
                # Перед тем, как кликнуть, ждем прогрузки страницы (отслеживая спиннер)
                self.wait(timeout = 15).until(EC.invisibility_of_element(target_locators.BasePageLocators.SPINNER_LOCATOR))
                elem = self.find(locator)
                elem = self.wait().until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except (StaleElementReferenceException, TimeoutException, ElementClickInterceptedException):
                if i == CLICK_RETRY - 1:
                    raise

    # Проверяем, что находимся на нужной странице через URL, предварительно ожидая прогрузки страницы
    def check_url(self, url):
        self.wait().until(EC.url_contains(url))
        assert self.driver.current_url == url