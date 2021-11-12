from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

class PageNotLoadedException(Exception):
    pass

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    CLICK_RETRY = 3
    BASE_TIMEOUT = 5

    def find(self, locator, timeout=BASE_TIMEOUT):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def find_everything(self, locator, timeout=BASE_TIMEOUT):
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def wait(self, timeout=BASE_TIMEOUT):
        return WebDriverWait(self.driver, timeout=timeout)

    def click_for_android(self, locator, timeout=BASE_TIMEOUT):
        for i in range(self.CLICK_RETRY):
            try:
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == self.CLICK_RETRY - 1:
                    raise

    def swipe_up(self, swipetime=200):
        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        x = int(dimension['width'] / 2)
        start_y = int(dimension['height'] * 0.8)
        end_y = int(dimension['height'] * 0.2)
        action. \
            press(x=x, y=start_y). \
            wait(ms=swipetime). \
            move_to(x=x, y=end_y). \
            release(). \
            perform()

    def swipe_up_to_element(self, locator, max_swipes):
        already_swiped = 0
        while len(self.driver.find_elements(*locator)) == 0:
            if already_swiped > max_swipes:
                raise TimeoutException(f"Error with {locator}, please check function")
            self.swipe_up()
            already_swiped += 1

    def swipe_left_to_element(self, locator_from, locator_to, max_swipes):
        already_swiped = 0
        while len(self.driver.find_elements(*locator_to)) == 0:
            if already_swiped > max_swipes:
                raise TimeoutException(f"Error with {locator_to}, please check function")
            self.swipe_left(locator_from)
            already_swiped += 1

    def swipe_left(self, locator):
        web_element = self.find(locator, 10)
        left_x = web_element.location['x']
        right_x = left_x + web_element.rect['width']
        upper_y = web_element.location['y']
        lower_y = upper_y + web_element.rect['height']
        middle_y = (upper_y + lower_y) / 2
        action = TouchAction(self.driver)
        action. \
            press(x=right_x, y=middle_y). \
            wait(ms=300). \
            move_to(x=left_x, y=middle_y). \
            release(). \
            perform()