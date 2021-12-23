import pytest
from cases.ui.pages.login_page import LoginPage
from cases.ui.pages.main_page import MainPage
import allure
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from db.model import UserModel
from cases import urls
from utils.builder import UserBuilder

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)

def get_driver():

    options = Options()
    options.add_experimental_option("prefs", {"download.default_directory": '/tmp/selenium/Downloads'})

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "94.0",
        "selenoid:options": {
            "enableVNC": True,
        }
    }

    browser = webdriver.Remote(
        command_executor='http://selenoid:4444/wd/hub', options=options,
        desired_capabilities=capabilities)

    browser.maximize_window()
    return browser

@pytest.fixture(scope='function')
def driver():
    with allure.step('Init browser'):
        browser = get_driver()
        browser.get(urls.BASE_URL)

    yield browser
    browser.quit()

@pytest.fixture(scope='session')
def cookies(create_user_for_cookie):
    driver = get_driver()
    driver.get(urls.BASE_URL)
    login_page = LoginPage(driver)
    login_page.authorization(username=create_user_for_cookie.username,
                             password=create_user_for_cookie.password)
    cookies = driver.get_cookies()
    driver.quit()
    for cookie in cookies:
        del cookie['domain']
        return cookie

@pytest.fixture(scope='session')
def create_user_for_cookie(bd_client):
    username, password, email = UserBuilder.user()
    user_for_cookie = UserModel(
        username='cookie' + username,
        password=password,
        email=email,
        active=True,
        access=True,
        start_active_time=datetime.now()
    )
    bd_client.create_user_in_db(user_for_cookie)
    return user_for_cookie



