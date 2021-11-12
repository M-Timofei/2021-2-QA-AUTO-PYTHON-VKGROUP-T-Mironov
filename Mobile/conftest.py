import pytest
from appium import webdriver
from ui.capability import capability_select
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)

def get_driver(appium_url):
    desired_caps = capability_select()
    driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
    return driver

@pytest.fixture(scope='function')
def driver():
    appium_url = 'http://127.0.0.1:4723/wd/hub'
    browser = get_driver(appium_url)
    yield browser
    browser.quit()