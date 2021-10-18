import pytest
from selenium import webdriver
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.profile_page import ProfilePage
from ui.pages.navbar_page import NavbarPage

@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)

@pytest.fixture
def dashboard_page(driver):
    return DashboardPage(driver=driver)

@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver=driver)

@pytest.fixture
def navbar_page(driver):
    return NavbarPage(driver=driver)

@pytest.fixture(scope='function')
def driver():

    browser = webdriver.Chrome(executable_path='D:\mail\HomeWorks\chromedriver.exe')
    url = 'https://target.my.com/'

    browser.maximize_window()
    browser.get(url)
    yield browser
    browser.close()

