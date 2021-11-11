import logging
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ui import urls
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

def get_driver():
    options = Options()
    manager = ChromeDriverManager(version='latest', log_level=logging.CRITICAL)
    browser = webdriver.Chrome(manager.install(), options=options)
    browser.maximize_window()
    return browser

@pytest.fixture(scope='function')
def driver():
    url = urls.URL_BASE
    browser = get_driver()
    browser.get(url)
    yield browser
    browser.quit()