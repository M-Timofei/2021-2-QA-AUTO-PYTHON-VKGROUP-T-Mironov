import allure
import time
from ui import urls
from ui.locators import target_locators
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging

class PageNotLoadedException(Exception):
    pass

class BasePage(object):
    url = urls.URL_BASE
    locators = target_locators.BasePageLocators

    CLICK_RETRY = 3
    BASE_TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('test')
        self.is_opened()

    def is_opened(self, timeout = BASE_TIMEOUT):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True

        raise PageNotLoadedException(f'{self.url} did not open in {timeout} sec for {self.__class__.__name__}.\n'
                                 f'Current url: {self.driver.current_url}.')

    def wait_spinner(self, timeout=BASE_TIMEOUT):
        self.wait(timeout).until(EC.invisibility_of_element(target_locators.BasePageLocators.SPINNER_LOCATOR))

    def wait(self, timeout=BASE_TIMEOUT):
        return WebDriverWait(self.driver, timeout=timeout)

    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def find(self, locator, timeout=BASE_TIMEOUT):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Clicking allure step on {locator}')
    def click(self, locator, timeout=BASE_TIMEOUT):
        self.logger.info(f'Clicking on {locator}')
        for i in range(self.CLICK_RETRY):
            try:
                self.find(locator, timeout=timeout)
                elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                elem.click()
                return
            except (StaleElementReferenceException, ElementNotInteractableException):
                if i == self.CLICK_RETRY-1:
                    raise

    @allure.step('Input data: {text}')
    def input_data(self, locator, text):
        self.logger.info(f'Input data: {text}')
        elem = self.wait(timeout=10).until(EC.element_to_be_clickable(locator))
        self.scroll_to(elem)
        elem.clear()
        self.find(locator).send_keys(text)