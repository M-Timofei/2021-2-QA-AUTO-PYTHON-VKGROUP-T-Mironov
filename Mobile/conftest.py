import pytest
from appium import webdriver
from ui.capability import capability_select
from ui.pages.base_page import BasePage
from ui.pages.search_page import SearchPage

def pytest_addoption(parser):
    parser.addoption('--global_version', default='1.50.2')

@pytest.fixture(scope='session')
def config(request):
    global_version = request.config.getoption('--global_version')
    return {'global_version': global_version}

@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)

@pytest.fixture
def search_page(driver, config):
    return SearchPage(driver=driver, config=config)

def get_driver(appium_url, global_version):
    desired_caps = capability_select(version=global_version)
    driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
    return driver

@pytest.fixture(scope='function')
def driver(config):
    appium_url = 'http://127.0.0.1:4723/wd/hub'
    version = config['global_version']
    browser = get_driver(appium_url=appium_url, global_version=version)
    yield browser
    browser.quit()