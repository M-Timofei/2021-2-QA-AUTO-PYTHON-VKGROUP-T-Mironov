import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.profile_page import ProfilePage

class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self,driver, request: FixtureRequest):
        self.driver = driver

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')
        self.dashboard_page: DashboardPage = request.getfixturevalue('dashboard_page')
        self.profile_page: ProfilePage = request.getfixturevalue('profile_page')