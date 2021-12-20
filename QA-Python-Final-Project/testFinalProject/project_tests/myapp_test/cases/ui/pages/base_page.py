import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class PageNotLoadedException(Exception):
    pass

class BasePageUI(object):

    CLICK_RETRY = 3
    BASE_TIMEOUT = 60 # timeout намеренно завышен в связи с немощным процессором, где необходимо, он занижен

    def __init__(self, driver):
        self.driver = driver

    def wait(self, timeout=BASE_TIMEOUT):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=BASE_TIMEOUT, should_be_visible=False):
        if should_be_visible:
            return self.wait(timeout).until(EC.visibility_of_element_located(locator))
        else:
            return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Clicking on {locator}')
    def click(self, locator, timeout=BASE_TIMEOUT):
        for i in range(self.CLICK_RETRY):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < self.CLICK_RETRY - 1:
                    raise

    @allure.step('Input data: {text}')
    def input_data(self, locator, text):
        elem = self.wait(timeout=self.BASE_TIMEOUT).until(EC.element_to_be_clickable(locator))
        elem.clear()
        self.find(locator).send_keys(text)