import pytest
from cases.ui.pages.login_page import LoginPage
from cases.ui.pages.main_page import MainPage
from selenium.webdriver.remote.webdriver import WebDriver
from _pytest.fixtures import FixtureRequest
import allure
import os
import time

class NextTabException(Exception):
    pass

class BaseCaseUI:
    authorize = False

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, temp_dir):

        yield

        time.sleep(1)
        screenshot = os.path.join(temp_dir, 'img.png')
        driver.get_screenshot_as_file(screenshot)
        allure.attach.file(screenshot, 'img.png', attachment_type=allure.attachment_type.PNG)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, bd_client, mock_client, request: FixtureRequest):
        self.driver: WebDriver = driver
        self.bd_client = bd_client
        self.mock_client = mock_client

        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')

        if self.authorize:
            cookie = request.getfixturevalue('cookies')
            with allure.step(f"add_cookie"):
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.main_page = MainPage(driver)

    @allure.step('Go to next tab')
    def go_to_next_tab(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
        except IndexError:
            raise NextTabException('Новая вкладка не открылась')